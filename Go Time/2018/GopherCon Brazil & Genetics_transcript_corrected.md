**Erik St. Martin:** Welcome back, everybody, to another episode of Go Time. Today's episode is number 65. Today on the show we have myself, Erik St. Martin, Brian Petersen...

**Brian Petersen:** Hello!

**Carlisle Thompson:** Carlisle...

**Erik St. Martin:** Oh, weird... \[laughter\] No, my Skype just told me that it was reconnecting...

**Brian Petersen:** What...?!

**Erik St. Martin:** Yeah. Okay... \[laughs\] So we also have Carlisle Pinto here...

**Carlisle Thompson:** Hi, everybody.

**Erik St. Martin:** And our special guest for today is Vítor De Mario. You're one of the organizers of [Gopher Con](https://2017.gopherconbr.org/). Something else, you spoke at -- it was a lightning talk, I think, at Gopher Con last year...

**Vítor De Mario:** Yes.

**Erik St. Martin:** And you were talking about how you were working on genetics in Go. And calm down, people, I said genetics, not generics. \[laughter\]

**Vítor De Mario:** I didn't think about that, but it's going to be a problem.

**Carlisle Thompson:** You know, I did that, and [Scott Mansfield](https://twitter.com/sgmansfield) I think corrected me on Slack -- oh no, it was somebody else that corrected me... And I'm like, "Oh, I had never realized they were two different words", like they sound different, genetics and generics. I'm sure I said it the same way...

**Vítor De Mario:** I'm probably going to have the same problem. I'm Brazilian, just like Carlisle, and I don't have a lot of years living in the U.S., so it's probably going to be a bigger problem for me.

**Erik St. Martin:** Let's talk about the stuff you're working on first, because it's actually a fascinating use case for Go, and I know I get particularly excited about things people work on that are kind of outside the standard RESTful APIs and things.

**Vítor De Mario:** So I started working at a company called Mendelian about four years ago in São Paulo. I'm not originally from here, but I came here to work at it. I was told I was gonna work in Python at the beginning, I started learning Python, but then when I came here there was a small project built by our CEO, who is not a programmer, and he had started it in Go because he liked the language; he thought it was a language that he understood relatively well, so he started doing it on his own. He named the project Abracadabra, and it was supposed to be an annotator and classifier for mutations. We call them variants usually, but it's the same thing, it's just a mutation.

So what Mendelian does is we receive patients here who are sent to us by a physician who thinks they have a genetic disease, and we take their blood, we process it in our lab, and we work with all our bioinformatics tools, and then we generate reports in the end saying whether we found something, if they have a genetic disease or not... And one of these steps was built here. We have this software, Abracadabra; it added a lot of information into each one of the variants, which is the part that we call annotation, and we built a machine learning model we have run on forest in Go. There is a very cool library for doing that called [Cloud Forest](https://github.com/ryanbressler/CloudForest), built by [Ryan Bresler](https://github.com/ryanbressler).

\[03:53\] We used it, and we built a model here, and we started telling our physicians which variants were relevant in each case and which weren't, because everyone has a lot of mutations. So if we receive a patient -- back in the day we had 50,000 mutations for each one of us, even if we are healthy, and that's normal, so finding the one that is relevant in the middle of all of it is a big problem. In the beginning it was a very manual process, it had a lot of errors, and then we built this software in Go to try to find these mutations better and delivering them to our physicians before they had to start working on each case.

**Carlisle Thompson:** So you did like a free sorting of sorts to sort out who had malignant mutations?

**Vítor De Mario:** We usually say the word pathogenic.

**Carlisle Thompson:** Pathogenic mutations?

**Vítor De Mario:** Yes, yes. It's more like filtering, because we don't show the ones that are not relevant, because there is a lot of data in any case, even if it's a relatively simple case. But what we do is we filter it with the results of the machine of the machine learning software. All of that is written in Go, and all of that inside only one program.

**Carlisle Thompson:** That is pretty cool.

**Brian Petersen:** Alright, so I think we need to back up a little bit. You used about 30 words that meant nothing to me in that whole description. Something-something forest, something-- can you kind of back up and tell us about the process that gets used and what you're actually computing, where the data comes from? Help me out here, because I feel stupid, I'm sorry.

**Vítor De Mario:** No, it's fine.

**Carlisle Thompson:** Before I come across as smarter than Brian, because I didn't ask those questions - I've watched his [lightning talk](https://www.youtube.com/watch?v=GYLOmwIqP-M), so it sort of made sense to me... \[laughter\]

**Vítor De Mario:** You came prepared.

**Carlisle Thompson:** I came prepared, that's all.

**Vítor De Mario:** Yeah, so there are two pieces to this, two about the data. Usually, we have very little data. What comes out of our lab and comes out of the bioinformatics software is just a list of mutations. It says "Oh, for this person, she has a mutation on the chromosome tree, this specific mutation. She should have an [A](https://en.wikipedia.org/wiki/Adenine) here; she has a [G](https://en.wikipedia.org/wiki/Guanine). That's it. And we have a whole list for each person, saying every mutation that they have. But those don't mean much, because in this list of mutations there is the colour of your hair, the colour of your eyes - all the kind of things that make you who you are, make you special. And in the middle of all of it there's also things that cause diseases, so what we want to do is we want to separate these mutations from the ones that don't cause any problem.

The way we do it is the first part, without any machine learning, is just we have a lot of databases from bioinformatics tools; most of those we didn't build them, they are things that can be used by anyone working with bioinformatics. That tells us more information about each mutation, or about each position in the genome. They say, "Oh, this position is very conserved", so pretty much all the species we know that we have the sequence of their DNA, they have the same position, and we never see any different. So this becomes a number, which was created by a specific research project, and then this number is used by our software later to say if this is very relevant, to say if a mutation causes diseases or not.

So we add a lot of information to each one of these variants, so our lists become -- each position in this list of mutation becomes a lot of data. We know which proteins were affected... Everything that can be calculated using knowledge from biology and from genetics, and this becomes a huge list. There are thousands of small points like this for each mutation. So that's the point where we are before we start talking about machine learning.

After that, we have a huge matrix; you can think about this list, and a lot of these features become columns, so there's a quite big matrix, and we built a machine learning model using an algorithm called [random forest](https://en.wikipedia.org/wiki/Random_forest).

\[08:02\] It's not very popular these days; you're probably thinking a lot about deep learning and [TensorFlow](https://www.tensorflow.org/) and these kinds of things, but three or four years ago we weren't talking that much about it, and there are some studies that say that this algorithm (random forest) works well for genomics, for genetic data.

We started working on a library that is built in Go to create these kinds of models. The library is called Cloud Forest; it's pretty much just an implementation of this algorithm, and we've started passing our data with all of those extra columns into this software for it to build a big model trying to predict new mutations, if they were causing diseases or not, if they were pathogenic or not. So we did a lot of rounds, like cleaning up our data, trying to understand how each feature of this software works, because I'm not a specialist in machine learning... I don't know much about it, so I had to learn it while I was doing it.

In the end, we created several models, we started working with them, and one of those was better, and then we put it into the real software, and we started passing new data into it and trying to predict whether new patients that were coming in we could find their mutation earlier, or at least filter out a lot of the things that don't matter before we put it into a web page for our doctor's work. Does it make better sense now?

**Brian Petersen:** Much better sense.

**Erik St. Martin:** So I'm imagining there's not a lot of libraries for things like this already in Go...

**Vítor De Mario:** No.

**Erik St. Martin:** Was it really time-consuming to create this sort of stuff? I know this is why a lot of people keep falling back to Python in the machine learning and data science spaces, just because there are a lot of good libraries there.

**Vítor De Mario:** Yeah, we were kind of lucky in that scenario, because there was already, before we started working on this software, this library that I mentioned called Forest... And that's all it did - it did random forest models. This algorithm - that's the only thing it did. They created a few others, but the most important was this one, since it even had the name. It was pretty much luck... There was this guy that created it, Ryan Bresler; he was a researcher in genetics, and he liked Go, too... A few months before we started working on it, I guess. So since he liked both of those things, he started building the tool by himself, or just playing around with data, and it grew a little bit, and other people started picking it up, not just us.

So when we started working on it, we kind of knew that this algorithm will probably work well for the kind of data that we had, and we started looking for what's available... There was Ryan's library waiting for us, and it worked well.

Machine learning and Go in general, it's a bigger problem because there isn't that many good libraries, and if you want to use other things that don't necessarily fit your data that well, you don't have as many options as you do in Python and other frameworks and languages.

**Erik St. Martin:** I think it's getting better though...

**Vítor De Mario:** Yes, definitely.

**Erik St. Martin:** I've been seeing more and more stuff come out, especially over maybe the last year or two, but for a long time it was kind of a big deterrent from the scientific communities was like the lack of libraries, especially around some of the -- like Plum and things like that.

**Vítor De Mario:** It's definitely better now. There are a few people working with it. The name that comes to my mind immediately is [Daniel Whiten ack](https://twitter.com/dwhitena); he is working on [Pachyderm](https://github.com/pachyderm/pachyderm) and he has a book that came out recently, which is [Machine Learning With Go](https://www.packtpub.com/big-data-and-business-intelligence/machine-learning-go). I haven't read it yet unfortunately, but I believe he shows in the book many algorithms and how they can be implemented in Go.

So there are people trying to get Go to be a good language for it... Because of the performance and all those things, it can be theoretically a good language to do machine learning in the future, and it's getting better, definitely.

**Erik St. Martin:** Yeah, I know Daniel has been working with a lot of those communities and creating some stuff, and a lot of content, too. He spoke at Gopher Con -- actually, he's teaching Machine Learning With Go Workshop this year at Gopher Con in Denver.

**Vítor De Mario:** \[12:13\] Yeah, it's going to be great.

**Erik St. Martin:** Yeah, if you're into machine learning and Go, you definitely want to make friends with Daniel.

**Vítor De Mario:** Yes, he is THE guy in this area.

**Carlisle Thompson:** And we also interviewed him here.

**Erik St. Martin:** Yeah, he was [one of the first episodes](https://changelog.com/gotime/40)... I want to say it was within the first 20–25 episodes.

**Brian Petersen:** It was definitely early.

**Vítor De Mario:** There is also now an official client for TensorFlow. It's not that easy to build a model in Go if you're trying to use TensorFlow, but you can build a model in Python and upload it to Google Cloud ML, or maybe host it yourself and use your software to use it, to send you data into it. That's what we are doing now. We ended up moving away from Random Forest recently, in the last year, and now we are using TensorFlow and the software that talks to the TensorFlow model is still in Go.

**Erik St. Martin:** Okay, so you basically have your data scientists and things like that create the model in the tools that they're used to, but then you can of consume the model in Go.

**Vítor De Mario:** Exactly. In the beginning, the Random Forest story that I've told, it was pretty much just me with a few other people here, but most of it was built by me. Later, I told them "Okay, I'm not a specialist at this. We need people that actually know what they are doing." I can't really do a trial and error forever.

Now we have a person, Fernanda, who is a data scientist, and she knows a lot more about machine learning than we do, and she built a new model using TensorFlow. Most of our work was in Python, but then we integrated it into the Go software, and it consults her model through Go software.

**Erik St. Martin:** That's really awesome. And the performance of it, I imagine, is one of the key reasons why you're using it in this space, right?

**Vítor De Mario:** Yes, yes. As pretty much everything in Go, the performance is perfect. It's one of our bottlenecks, because there are a lot of things that are happening when we are trying to classify variants. We had it being one of the bottlenecks in the Random Forest world too, and same thing with TensorFlow now, because there is a lot of data going around, and you have to do a lot of computation in each mutation to try to find the result... But we are also experimenting a little bit with hosting the TensorFlow model inside the program, inside a container, we have our binaries, and it's working really well and are probably going to have perfect results. We already have pretty good results, but they are going to be really fast in the near future.

**Erik St. Martin:** I'm imagining this is CPU-bound, right?

**Vítor De Mario:** Yes, it is.

**Erik St. Martin:** Now, was this written in something prior, or was it just kind of whole new project and you kind of--

**Vítor De Mario:** It was a whole new project, yeah. In the lightning talk that Carlisle saw in Denver - I usually show a slide where the first version of the software is entirely in that slide; there's like 800 or 1,000 lines all in one file. Our CEO who was our programmer thought that was fine. That was one of the first things that we changed... "Okay, this is not a decent program. We've got to do some work on top of it." But it was completely new, he showed it to us. It was pretty much just an idea before, and there wasn't any prior software before it.

**Erik St. Martin:** All your IP in a single slide... \[laughs\]

**Vítor De Mario:** Yeah, pretty much. Now, of course there were other things that we were doing, but this whole annotation and classification thing - it was all there, in the first version.

**Erik St. Martin:** That's awesome.

**Carlisle Thompson:** Now, it's pretty striking to that a doctor -- he probably knew how to program before, I would imagine...

**Vítor De Mario:** \[16:01\] Yes, a little bit.

**Carlisle Thompson:** But he just picked up a brand new cutting-edge language that maybe didn't have that much documentation back then and examples, and just said "Hey, this looks great, and simple enough."

**Brian Petersen:** "Yeah, what the hell, I'll just write some code..."

**Carlisle Thompson:** "...and put it in production."

**Vítor De Mario:** He said many times to us, since that day, that if he could come back in time, he wouldn't be a doctor, he would be an engineer. So since he didn't do that, now he tries to do as much engineering as possible, when he has time for it. He's not only a doctor, he's also running the company, so there isn't much time for him to do that, but he's trying to do all of it at once.

**Brian Petersen:** Like the commercial "I'm not an engineer, but I play one on TV"?

**Vítor De Mario:** \[laughs\] Yeah.

**Erik St. Martin:** I'm not an engineer, but I play one on TV... \[laughs\]

**Vítor De Mario:** Yeah, nobody knows why he looked into Go and thought "Oh, this is better than Python" or "This is friendlier to me", but well... It worked, and it was a kind of happy accident.

**Erik St. Martin:** It could just be the amount of hype... You know, you go on a lot of programming forums and things, and a lot of people are experimenting with Go and Rust, because the past couple years that's really two of the main languages that have -- I guess Scala a bit, too... I'm trying to think of some other ones that have kind of got super-hyped in the last couple of years, but...

**Vítor De Mario:** I think he enjoyed the simplicity as well, because there wasn't much to learn in terms of the syntax of the language and that kind of thing. You could pick it up and start working in it pretty fast. He didn't have to learn what list comprehension is, or something like that, compared to other languages.

**Erik St. Martin:** That's sure, too. I mean, you look at some languages, and they're extremely confusing, and then you have languages that seem simple if you have programming background beforehand, but I guess it's hard to look at any language and think about what it might look like to somebody who's never programmed before.

I remember Ruby - "Oh, super, super readable", right? Well, not if you show a non-programmer, right?

**Brian Petersen:** That's true.

**Vítor De Mario:** Yes. If you have a background, you'll probably see things familiar there. I also think the explicitness, the fact that everything is quite clear in it helps you. Some of the more complicated topics like understanding why he should use an interface in a place, or why a big interface is a problem - that kind of thing is not that clear, but if we're talking about handling errors and seeing why something failed in a program, it's all very... Almost obvious. So he can read the code, and he can understand what it's going on. That helps a lot, too. Not only in terms of the syntax of the language.

**Carlisle Thompson:** Yeah, this is one thing that really strikes me about Go. You can write a very complex system without using any interface, or go routines or anything that could be complicated, depending on your experience in programming. Now, of course, the more code you write without using these things, the more you have to keep in your head, and you could potentially simplify it by using interfaces, and making it more efficient by using go routines... But you don't have to. You can have a perfectly functional program.

**Vítor De Mario:** Yeah, you can still survive without those things. The first version of the program that he showed us had none of those things, and for a while there wasn't anything. We were trying to separate things into packages, and we had our own problems trying to rebuild things in the way we were used to in other languages. We came from Java or from C\#, depending on who was working on each part of the code... So we tried to do the things that we thought were natural, and they didn't necessarily fit Go, so there was all of that, but... He had his own issues not knowing those things, and we also had them. After a while, we all kind of converged, understanding the language better.

**Brian Petersen:** \[20:06\] So you are one of the organizers of Gopher Con Brazil?

**Vítor De Mario:** Yes, I am. We are a team of five.

**Brian Petersen:** I heard it was a very successful event this last year. That was November...?

**Vítor De Mario:** Yeah, it was in November.

**Erik St. Martin:** I think this was year two...?

**Vítor De Mario:** The first one was November 2nd. Yes, the first one was in 2016, in November as well, and the second one was November last year. Carlisle was there.

**Brian Petersen:** I heard.

**Carlisle Thompson:** I was there... \[laughs\]

**Erik St. Martin:** I still want to make it. I was trying to get a passport and a visa turned around in time, and it just wasn't happening.

**Vítor De Mario:** Yeah, that's a big problem for people in the U.S.

**Carlisle Thompson:** I'm here to give a testimony - it was a fantastic event. The organizers -- I consider them all my friends, and I don't want to be like a fangirl, but they did everything they said they were going to do. There was no disappointment. All the speakers who were supposed to be there were, as per the latest roster, and it was just great. The talks were great, the hangout afterwards, and... I don't know, I had a great time, learned a ton, met new people... There were -- what, 200 people there? 200 attendees?

**Vítor De Mario:** We were saying about 250, more or less.

**Carlisle Thompson:** Yeah, I thought there was more than 200.

**Brian Petersen:** That's really awesome.

**Vítor De Mario:** Something around that. Yeah, we had about 180 in the first edition, something like that. We don't have the exact numbers, but based on the tickets here, it's what we were close to. So we can see that that's not that big of a growth from one year to the other, but one thing that changed a lot, that since things worked out for the first year - we didn't know how it was going to go - we invested a lot in the infrastructure, and we had a much better setup this year for audio, for video, for everything. So it kind of gave us the sensation that things were for real; now we are doing a professional conference.

I don't know if Carlisle had the same sensation, but for me - I was there for the first year, and then for the second, and there was a really huge difference.

**Carlisle Thompson:** I wasn't there for the first year, but I felt -- like I said, everything that was supposed to happen, happened. I didn't see any glitch. I was very pleased. It was very professional, very well put together, everything worked on the schedule, and I was very happy to see Google sponsoring the conference this year, and hopefully they will continue to do it. Sponsorships are so important; it's what allows conferences to get better and better, right? And as they learn what they need, they will be able to address things and make it better.

**Erik St. Martin:** You know what's funny - that was probably one of the first things Brian and I wanted to fix after our first year, too... We were like "We've got to do better A/V!"

**Brian Petersen:** Yeah... We had no idea what we were doing, and the second year it got a lot better.

**Vítor De Mario:** Yeah, I understand the feeling really, really well.

**Carlisle Thompson:** When are the videos going to be out?

**Vítor De Mario:** I don't know, we had some problems with it. It was supposed to be out already, but I can't give you a date yet. I hope soon, but I'm not really directly involved in that now, so I can't give you a date.

**Carlisle Thompson:** Okay. So for people thinking about going to the Gopher Con Brazil conference, if you're from outside Brazil and you need a visa, just heads up that you need to start working on the visa way before the trip.

**Erik St. Martin:** Yeah, months...

**Vítor De Mario:** Yeah, because it takes a while.

**Carlisle Thompson:** It takes a while.

**Erik St. Martin:** Speaking of people coming in from other countries, what kind of geographic demographics -- was it mostly a lot of people from Brazil and South America, or was it a lot of people flying in from other countries?

**Vítor De Mario:** \[24:06\] Most of the attendees were from Brazil. In the first year especially there were a lot of people coming from other places in South America, like Argentina and Peru, and they've even given talks. This year I don't think that many came; there was a group from Columbia... I think there was another group, but I don't remember exactly which country it was from. Other than that, we get mostly people from the U.S. that come to speak at the events, so...

Some of our talks are in English, and it's okay, we consider part of the conference to be bilingual. [Aditya (Mukherjee)](https://twitter.com/chimeracoder) who was one of the speakers this year, he wanted to submit a talk to us exactly because of this reason - he wanted to show how the Go language itself could be rewritten in other languages, how he could change the keywords into Bengali or Portuguese, and he said this is the place to do it, because the conference is bilingual.

We have a few people from the U.S. because of that, because of the talk submissions, and a few people from the rest of South America too, because of the proximity. But Brazil itself is huge. Some people come from bigger distances than the people from Argentina or Chile, just from inside Brazil.

**Erik St. Martin:** Oh, wow.

**Vítor De Mario:** Yeah. Brazil is a considered a continental country. It's bigger than a few continents, so... It's huge.

**Erik St. Martin:** Now I can't wait for the videos to come out, because I didn't even see Aditya's talk about translating. That's pretty cool.

**Vítor De Mario:** Yeah, because he did a [lightning talk](https://www.youtube.com/watch?v=oDFerBdr2J0&index=14&list=PL2ntRZ1ySWBfhRZj3BDOrKdHzoafHsKHU) with the same topic in Denver, and then he expanded it for Gopher Con Brazil.

**Erik St. Martin:** We got so caught up on the final day... I didn't catch any of the lightning talks, and that's one thing I haven't got a chance to do, is watch any of the videos for those.

**Brian Petersen:** He did a similar talk at Golang UK, and it was really, perfect... Actually, beyond good. It blew my mind. It was awesome.

**Vítor De Mario:** Yeah, I haven't seen anything similar to what he did, it was really impressive.

**Erik St. Martin:** So are you confident you're having a 2018 version?

**Vítor De Mario:** Yes, we already have everything set up with the venue. We're going to repeat the venue for the third time, and the date is already out, too. It's going to be at the end of September, from the [27th to the 29th](https://2018.gopherconbr.org/), I believe. We don't have yet speakers, and we haven't confirmed any of the sponsors yet, but the conference is definitely going to happen.

**Erik St. Martin:** So it sounds like your CFP will be out soon, too...

**Vítor De Mario:** We are probably going to start it in the beginning of April, I think.

**Erik St. Martin:** Okay, so a little later. If you want to speak at a Go conference, now is the time. What were we talking about the other night, Brian? There's like three or four Go conferences with CFP's...

**Brian Petersen:** Yeah, there's several CFP's open right now, which means it's a good time to polish off your editors and start writing proposals. We want yours, we want everyone's proposal.

**Vítor De Mario:** Yeah, I want to be one of the people sending a proposal to you as well, and to [Gopher Con in Iceland](https://gophercon.is/) and in other places too, but I haven't yet.

**Brian Petersen:** Excellent.

**Erik St. Martin:** So I heard that the [Rubicon CFP](https://events.linuxfoundation.org/events/kubecon-cloudnativecon-europe-2018/) for Copenhagen has something like 3,000 submissions. I don't want to see that many...

**Vítor De Mario:** I can't imagine having to select talks with that many... It's pretty much impossible.

**Erik St. Martin:** We had over 300 last year, or something like that. That was painful. I don't want to say painful, because I like reading the CFP's and things like that, and I find all the content fascinating, but trying to squeeze in time to review 300 proposals is a challenge... Especially because 200 of them wait till the last 48 hours.

**Vítor De Mario:** And some of them are perfect, but you have to say no anyway, because there aren't enough slots. I think this is one of the hardest parts.

**Erik St. Martin:** Oh, without a doubt. When you're looking at the ones that didn't make it, and it's not a reflection of them or the quality of their talk, it's just -- you've got 15 or 20 speaking slots and 300 proposals.

**Vítor De Mario:** \[28:15\] Yeah. We had between 50 and 60, and there were a few talks that I wanted to see in the conference and there weren't enough slots. I can't imagine with 300, like you, or like 1,300 or 3,000. I don't know the exact number for Rubicon... There are definitely going to be a lot of good materials that can't fit in the conference.

**Erik St. Martin:** I think we should just rent a city for like a month, and it's just Oprah Winfrey "You get a talk! And you get a talk! Everybody gets the talk!"

**Carlisle Thompson:** Yeah... And pay people's salary too for a month, like, "Take a sabbatical, we'll pay your salary. Just come to watch...", because we need people to watch the talks, too.

**Erik St. Martin:** Yeah, that's always difficult too, and this is why Carlisle was talking about sponsorships... With sponsorship money you're able to pay travel and accommodation and all that stuff for speakers, which is important, because not everybody works for a company that will fund them to go speak at a conference... Or even specific ones, depending on the technologies they work with versus where they want to go to talk.

**Carlisle Thompson:** But you know, sponsorships and volunteers - those things really make or break a conference. I remember last year - talking about CFP's - I was one of the people who helped review the CFP's, and I remember sitting... It was two weekends of coffee and nothing else but reviewing those CFP's, at the very end, and I reviewed every single one of them. [Dave Cheney](https://twitter.com/davecheney) was the one - I think he's always the one - to lead that effort of reviewing the CFP's, and at the end he said "All reviewers reviewed all the CFP's." It's a lot of work, and it makes a huge difference, but the more eyes that are on the process, the better the selection process is.

**Erik St. Martin:** Yeah, I was actually quite amazed that every talk was reviewed by every person.

**Vítor De Mario:** You get different opinions, and sometimes you say something, and you think the talk is good, or you think it isn't, and another person comes in and says, "No, but you didn't think about that." It changes my point of view completely. That happened a lot in our CFP, which was much smaller.

**Carlisle Thompson:** Yeah, absolutely.

**Vítor De Mario:** It definitely happened a lot on yours, too.

**Erik St. Martin:** And we actually tried to rotate our review committee too, every year, just to kind of make sure that it's not like an echo chamber where it's the same five or ten people selecting talks every year. This year maybe there weren't as many talks that target your experience, but next year there might be, because the committee is all different.

**Vítor De Mario:** Yeah, it makes things fresh.

**Brian Petersen:** Well, this year we have a new program chair at Gopher Con... It's going to be [Ashley McNamara](https://twitter.com/ashleymcnamara). Dave has handed over the sceptre.

**Vítor De Mario:** Yeah, given the reception to her talk last year, I think she's a great choice.

**Carlisle Thompson:** She's going to do a great job, for sure.

**Erik St. Martin:** We all love Ashley.

**Vítor De Mario:** Actually, I'm going to be a little bit mean here, because I met her in Denver for the first time, and she didn't know who I was, of course, because nobody knew back then, but she actually told me she would do a version of the logo of the software - I was talking about Abracadabra... He's a bunny these days, and he should become a gopher. And we never spoke about it again, and it never happened, so... I'd still like to do it.

**Carlisle Thompson:** Wait, a logo for your company?

**Vítor De Mario:** No, for the software, Abracadabra.

**Carlisle Thompson:** Which is a commercial software.

**Vítor De Mario:** \[31:55\] Yeah, yeah.

**Carlisle Thompson:** As far as I understand, she doesn't take money to do these -- logos for commercial products should be paid, but then...

**Vítor De Mario:** Yeah, that's a problem.

**Carlisle Thompson:** I'm sure she's like, "Well, if I'm not going to get paid, I'll just..." -- I don't know what she focuses on, but maybe something related to a commercial product is probably low on her priority list.

**Vítor De Mario:** It was never official. I only used it in the slides I do internally here, and the ones I did in Denver and at the first edition of Gopher Con Brazil. But now we are thinking about - not thinking, we're already working on - splitting the software into several parts, and some of it is going to be open source, or perhaps it can be a new logo for the open source version. We are going to need one.

**Brian Petersen:** Well, I know they take a lot of time, so...

**Vítor De Mario:** Oh yeah, definitely.

**Brian Petersen:** It's not an easy thing to do.

**Vítor De Mario:** Of course, she does a lot more than that, and logos for several cool open source software, so it's not guaranteed, but I'm kind of jealous of everyone that already got one. \[laughter\]

**Brian Petersen:** Everyone else has a logo... Yeah, I can understand that.

**Vítor De Mario:** Well, it's not fair. She has a lot on her plate.

**Brian Petersen:** Well, she has a day job, for sure.

**Vítor De Mario:** Yeah. My co-worker is saying here on the chat that we should open source the software as soon as possible to get a cool logo. \[laughter\]

**Brian Petersen:** Well, there are several other people in the community that are making logos, too. We should get you connected with some of them, so that you can get some good gopher logos if Ashley is too busy.

**Carlisle Thompson:** Yeah.

**Vítor De Mario:** That would be great.

**Brian Petersen:** I know she's been trying to focus a lot of her time lately on doing her main job, which is writing software... So we'll have to get you connected and see if she's got time.

**Vítor De Mario:** I'm sending in the chat the current version of what the bunny looks like.

**Erik St. Martin:** That's actually pretty funny. I can see this as like a pitch deck to the business on why you should open source your proprietary project. \[laughter\] It's like, "Number one - to get a cool logo." \[laughter\] They're like, "But how do we make money?" "Do you not see? I said cool logo!"

**Brian Petersen:** Yeah. "We have a logo from Ashley McNamara? Hello!

**Vítor De Mario:** Priority!

**Brian Petersen:** Yeah, that's an instant series A right there.

**Erik St. Martin:** Yeah, I mean, step one, have cool Ashley McNamara logo. Step two, question mark. Step three, profit.

**Brian Petersen:** Profit! Exactly.

**Vítor De Mario:** Sounds great to me.

**Erik St. Martin:** So looking at the time... Does everybody want to roll into interesting Go projects and news?

**Brian Petersen:** Yes!

**Carlisle Thompson:** Let's do it!

**Erik St. Martin:** Let's do it. I want to go first, because I think this is ridiculously cool.

**Brian Petersen:** Why do you get to go first?

**Erik St. Martin:** Because I never go first... So I'm stealing first.

**Brian Petersen:** Fine...

**Erik St. Martin:** So I came across -- I think it was last week sometimes... I think the GitHub username is hunterloftis, and the name of the project is called [PBR. It's a 3D renderer](https://github.com/hunterloftis/pbr)...

**Brian Petersen:** Wait a minute, PBR like Past Blue Ribbon?

**Erik St. Martin:** Correct.

**Brian Petersen:** Okay.

**Carlisle Thompson:** Is that in a document? Because I don't see it.

**Erik St. Martin:** It is, it's further down. I'm going to drop it in the channel. But it's a 3D renderer written in Go, and I just think that's ridiculously awesome.

**Brian Petersen:** Oh, wow!

**Erik St. Martin:** Yeah. I'm just really addicted to non-standard things written in Go, and I thought a 3D renderer in Go was pretty badass.

**Brian Petersen:** Wow, if you look at the examples on their GitHub repo, that's mind-blowing.

**Vítor De Mario:** Yeah, really impressive.

**Brian Petersen:** Impressive.

**Vítor De Mario:** This Millennium Falcon is so detailed. Wow.

**Brian Petersen:** Yup. Alright, I forgive you for going first, Erik. Carry on.

**Erik St. Martin:** \[laughs\] Alright, who's next?

**Brian Petersen:** \[35:59\] I have exciting news - the folks at Wallaroo Labs released the Wallaroo API for Go. [Wallaroo](https://github.com/WallarooLabs/wallaroo), if you haven't seen it, is some pretty amazing statistical software, streaming software... I don't even know how to describe it. It's really cool stuff, and it's written in [Pony](https://www.ponylang.org/), which is one of my favourite little side-languages to play with... And they have an [API now that's written in Go](https://github.com/WallarooLabs/wallaroo/tree/master/go_api), so if you want to learn about streaming and messaging and play with it in Go, the Wallaroo Go API is now available and it's pretty slick. I played with it this morning.

**Erik St. Martin:** I actually didn't see that... I'm looking at it now. There are too many cool things to play with.

**Brian Petersen:** Oh, it's ridiculous. I could quit my job and just play with things full-time and still run out of time to play with cool things.

**Erik St. Martin:** Yeah, there needs to be some sort of filter for whether we should play with stuff.

**Carlisle Thompson:** Isn't that us? Isn't that our job?

**Brian Petersen:** Oh, that's high, we're the filter. Dammit! Alright, so go play with this! I'm telling you, go play with Wallaroo, because it's really awesome. And Pony, too. If you like playing with languages, Pony is awesome, and it's named Pony because when the designer of the language told people everything he wanted to put in the language, somebody replied with "Well, why don't you just ask for a pony, too?" Because it has all the features.

**Erik St. Martin:** That's awesome.

**Carlisle Thompson:** That's hilarious.

**Erik St. Martin:** I think we've mentioned it before, but another cool language to play with is [Him](https://nim-lang.org/).

**Brian Petersen:** Yeah, I like Him, too.

**Erik St. Martin:** We'll have to do a Language of the Week/Month, or something, and just recommend some new language for people to play with.

**Brian Petersen:** Yeah, that's a good idea. Let's add that as a to-do note - talk about interesting languages every once in a while. Alright, so another project that came out yesterday, hit the wires hard is [Twirl](https://github.com/twitchtv/twirp), from Twitch, which is a competitor for [gRPC](https://grpc.io/). Twirl is a big deal because it does not require HTTP/2, and that's important if you're behind a load balancer that doesn't support HTTP/2. Twirl looks fast, and it looks pretty lightweight, and it looked to me particularly like the cognitive overhead of using Twirl might be just a little bit lighter than using gRPC. So I'm interested to try Twirl out, but I haven't yet.

**Vítor De Mario:** It also allows JSON payloads in the messages. So you can handcraft messages in it, and you can't with gRPC.

**Brian Petersen:** That's correct.

**Carlisle Thompson:** That's a good flexibility.

**Brian Petersen:** Yeah, very nice.

**Erik St. Martin:** I always wonder how people come up with these names, like Twirl. I mean, it looks almost like Twitch and RPC, except it's missing the C...

**Brian Petersen:** Yup. Naming is hard.

**Erik St. Martin:** Maybe it's just because it's other people's names, I like them better. But I feel like I couldn't come up with a name that's cool like that. Mine are very descriptive, like Go Database Client, you know?

**Brian Petersen:** \[laughs\]

**Carlisle Thompson:** Let's not talk about naming... I have currently a folder called Common, with a file named "shared.go"

**Brian Petersen:** Nice!

**Carlisle Thompson:** I know, help me...

**Brian Petersen:** That's an antipattern, by the way. Just FYI.

**Carlisle Thompson:** No kidding!?

**Vítor De Mario:** Is the package named "utils"?

**Carlisle Thompson:** The package is called "common", with one filename called "shared.go"

**Brian Petersen:** We're taking away your badge.

**Carlisle Thompson:** I need help, people... Seriously.

**Brian Petersen:** \[39:55\] We're sending [Ben Johnson](https://twitter.com/benbjohnson) over for an immediate Go Package intervention. \[laughter\] Are there any other interesting news?

**Carlisle Thompson:** I will go then. My friend Scott Borowski - he works with Congo, and he sent me news that they are doing an official MongoDB Go driver. This is interesting, because there is a heavily used Go driver already, but they decided to do what they're going to call [the official one](https://github.com/mongodb/mongo-go-driver), and put it on their repo, I suppose. And there is a big [blog post](https://engineering.mongodb.com/post/considering-the-community-effects-of-introducing-an-official-golang-mongodb-driver) explaining why they decided to do that.

I'm just saying this because for people who do use MongoDB, which is a lot of people, this might be relevant for them, and they might want to participate in this development, or not.

**Brian Petersen:** I'm confused, because I saw this headline and I didn't realize that this was talking about [GO](https://github.com/go-mgo/mgo)... So [Gustavo Diameter](https://twitter.com/gniemeyer) was the head of the GO project forever; 2011 I think is when that came out. And everybody in the community uses GO, and for the longest time, the people at Congo recommended GO as one of the best-written drivers that took advantage of all the possible features of Congo, and this blog post they wrote makes it sound like it's limiting and not really a great driver... So this is quite a flip in opinion for a company.

**Erik St. Martin:** Yeah, that's fascinating. I actually remember borrowing some of the BSON logic out of that driver, just because it was done so well.

**Brian Petersen:** Yeah, the driver is beautiful, and I don't know what the word count on this is, but it looks like 2,000 words talking about why this open source driver written by the community and contributed freely from people's spare time doesn't meet their needs. That's kind of a kick in the teeth for open source, isn't it?

**Carlisle Thompson:** I think it might be saying that, but it's also saying that they need more control as far as to what gets in, they need to have more say. Apparently, there are things that they wanted to get it that weren't getting in, as per community consensus, so they decided "Well, I guess we from our own community, with the ideals that will fit our goals better."

I don't know, I'm not taking sides, just trying to...

**Erik St. Martin:** So if I'm understanding this correctly, they're still going to do an open source driver, but now they are basically going to be the core maintainers of it, instead of trying to be a contributor to somebody else's.

**Brian Petersen:** Right. And they're not forking, they're just starting new.

**Carlisle Thompson:** Yeah.

**Vítor De Mario:** I heard another announcement by Gustavo himself that he wasn't gonna work on the GO driver anymore, and he was looking for someone else to take over him some time ago; I don't think he's doing that anymore. But with this post from the MongoDB guys, I kind of feel like they missed an opportunity in communication, so if they had talked to Gustavo, maybe they could take over the project themselves, and we would have the best of both worlds, perhaps.

**Brian Petersen:** It's also possible that this is a reaction, or that Gustavo's wanting to not maintain anymore as a reaction to this, I don't know... But no use attributing drama or malice where we don't know that there's any, but this certainly smells like it might have some.

**Carlisle Thompson:** We don't know that any conversation did or did not take place.

**Vítor De Mario:** Yes, that's true.

**Erik St. Martin:** \[43:52\] Yeah, it's actually interesting too, because... Like, I haven't read the post, so I don't know whether it speaks to this, but it's also quite possible that since the GO library came out, MongoDB as a database and platforming company has changed a lot, and evolved, and they may have learned new practices and things like that, and it would be a tremendous amount of work to put those into the existing library, and they felt it's easier to design from scratch. It seems more like a vision and planning and stuff that they mentioned here, just kind of scanning through it; there's not a lot that I see about like a technical nature. So it could be driven by some sort of technical thing, refactoring it to fit their new design.

**Brian Petersen:** Yeah. Well, I hope they treated Gustavo well, because he was a huge champion for the Go community and for Congo.

**Carlisle Thompson:** Yeah. And I actually owe him a contact to bring him on the show. I can't believe I haven't done that yet. Right? We want to have him on the show...?

**Brian Petersen:** Well, you can get him on the show when Vítor gets his Ashley gopher, and we'll just do all of it at once.

**Erik St. Martin:** I still remember the very first Gopher Con, and Gustavo was a speaker, and was helping us pack bags, stuff swag bags...

**Brian Petersen:** Yeah.

**Erik St. Martin:** I love seeing the community and the conferences and stuff like that all evolve, but I have very fond memories of the early days, where if you were given enough time, you could almost list everybody in the community.

**Brian Petersen:** Yeah, and the real central figures were the ones that were downstairs at the Marriott in Denver, helping us fill out swag bags and showing up early for the conference and working the -- like, [Cory Land](https://twitter.com/corylanou) working the registration desk while everybody else was watching conference talks. He didn't have to do that, but that was his contribution to the community. Those were nice days. And that sense of community has never left Go, which I love. I've got little goosebumps right now, because our community is so awesome.

**Erik St. Martin:** Now, Vítor, do you get a lot of volunteers for Gopher Con Brazil?

**Vítor De Mario:** We did a lot more this year than the last one, in 2017 than 2016, because I think a lot of people heard about it. Actually, one of the volunteers helped us a lot, and I kind of want to name her, which was [Ellen Forbes](https://twitter.com/ellenkorbes). I hope I'm saying her name right. She did a lot for us, and she was there -- before the conference started, she was already helping us, and she did a lot as the conference continued, and even in the last day he did one of the workshops with [Daniela Petruzalek](https://twitter.com/danicat83). They both teamed up and in the end they did one of the best workshops at the conference. So Ellen did a lot for us, and a lot of other people also talked about maybe helping as volunteers, but she was the main one.

**Erik St. Martin:** That's awesome.

**Brian Petersen:** Yeah, that's great.

**Erik St. Martin:** I applaud everybody who volunteers and helps out, especially for some of the conferences and stuff like that where they're not commercial events. It's a lot of people making sacrifices of their personal time... So for anybody who's willing to do that, I applaud them.

**Vítor De Mario:** Daniela wasn't actually a volunteer, but she kind of ended up being similarly to Ellen, because she spoke, she did a workshop, she came up with the idea of doing a diversity of scholarship for us for the first time as well, and she helped [Carlisle](https://twitter.com/carlisia) as well with her talk... She was pretty much everywhere. I don't know how she survived the conference doing everything that she did, but we wouldn't be the same without everything that Daniela did.

**Brian Petersen:** Well, speaking of that, if you go to her Twitter, which is [@Danicat83]((https://twitter.com/danicat83)), she's running a fundraiser to go talk at a conference in San Francisco, and I donated to that this morning because I would love to see her talk. So if you are able to go donate to that, it's definitely a worthy cause. She's an amazing helper in our community, so go help if you can.

**Carlisle Thompson:** \[48:19\] Absolutely.

**Brian Petersen:** Alright, how about \#FreeSoftwareFriday? Are we ready?

**Erik St. Martin:** Sounds good to me!

**Brian Petersen:** Alright, I've got to start this one, because Erik, I can't even believe you kicked me out of the last one. What the hell...? So \#FreeSoftwareFriday, this is big, too - how long have we waited for a new version of Bootstrap? A couple of years. [Bootstrap 4](https://github.com/twbs/bootstrap) dropped today, and it's looking good. And I'm sorry, but I know I'm going to lose my hipster credentials... I think pretty much anything made with Bootstrap looks good, and they did a great job with it, and I think Bootstrap websites are pleasing. Showing my age probably, but dammit, I like Bootstrap.

**Erik St. Martin:** It's interesting, because I cut my teeth in web development. I've gone from the table-based design, to DIV based in CSS and all that stuff, then the grid frameworks... Grid frameworks in CSS were like JavaScript frameworks now - so many new ones are getting kicked off all the time, and Bootstrap has kind of come around, and that's one of my favourites. There's two now that I kind of look at. I'll admit, I'm not as connected to that world, so there may be more now, and I may be wrong about the fact that CSS frameworks aren't popping up every day again.

**Brian Petersen:** They are, but Bootstrap is still the reigning champion.

**Carlisle Thompson:** And just for the fact that they were out there early on, when there was nothing... That was like, "Oh, wow... Life is changing."

**Brian Petersen:** Yeah, so big love to all the people contributing to Bootstrap and to Twitter for having the foresight to release that as a framework, thank you. Who's next?

**Carlisle Thompson:** I can go next. So today I felt virtuous for like a second and a half when I opened up my Twitter and I saw Frances tweets saying that he didn't know about something that I knew about... \[laughs\] I'm like, "Check that out!"

**Vítor De Mario:** That felt good, didn't it? \[laughter\]

**Brian Petersen:** Yeah, check me!

**Carlisle Thompson:** Not only I knew about it, but I've used it, and he's like "How did I not know about this?" So it just goes to show, you know, it bears repeating... Some of the projects bear repeating; not everybody knows about even the perfect stuff that's out there, so my shoutout goes to [Kelsey Hightower's](https://twitter.com/kelseyhightower) configuration library called [env config](https://github.com/kelseyhightower/envconfig), which is really neat. It just lets you hide your environment variables in a file, and using it in the application. It's pretty neat.

**Vítor De Mario:** Yeah, I've used it for many years and I love it. It's really flexible, it's really easy to use, and it solves a lot of problems.

**Erik St. Martin:** Yeah, I'm trying to remember... It's probably been a couple of years; I actually forgot about it, too. I know I used it a couple of years ago, but it's definitely been a while.

**Brian Petersen:** Yeah, we used it together back at that other job... Whatever that was.

**Erik St. Martin:** Yeah, it's actually surprising how many times Brian and I end up working together... I feel like we just can't get away from each other. We're like magnets. "I'm going to go off and work for this company", and then "Shhhhttt!" \[laughs\]

**Brian Petersen:** Yeah, I'm like that thing that's stuck on your shoe from the parking lot.

**Erik St. Martin:** Yeah, and Brian got a promotion -- was it last week, or the week before? Last week...

**Brian Petersen:** Last week, yeah.

**Erik St. Martin:** \[51:59\] So Brian now runs his own team and now Brian will be my boss again.

**Brian Petersen:** \[laughs\] Hurray!

**Erik St. Martin:** When Brian and I first met, he was my boss.

**Carlisle Thompson:** Congratulations, Brian.

**Brian Petersen:** Thank you, it's very exciting. We're running a team doing all open source work at Microsoft, and who would have thought those days were here? I love it so much...

**Vítor De Mario:** Yeah. If you had said that a few years ago, nobody would have believed you.

**Brian Petersen:** Yeah.

**Erik St. Martin:** Yeah, it really is amazing to see the evolution, and for us to -- you know, the developer advocates... Everybody kind of contributes to open source and stuff, but I think that Microsoft has been seeing that and loving that, so they wanted to kind of spin something up where at least a subset of us get to spend more of our time doing that than some of the other things that we do as developer advocates. And I am ridiculously excited to be working for Brian again, and on open source.

**Vítor De Mario:** You make a good team.

**Brian Petersen:** It's going to be kind of awesome.

**Vítor De Mario:** Pretty much everyone in the Go world knows about that.

**Erik St. Martin:** \[laughter\] Speaking of team, I still remember the first Gopher Con, because at this time everybody only knew each other by handles and names on mailing lists, and everybody was asking Brian and me how they would be able to recognize us, and Brian -- I forget who he told... He was like, "We're the ones that look like Penn and Teller", and I'm like "What?!" \[laughter\] Because he's so much taller than me...

**Brian Petersen:** I feel a little bit bad about that now...

**Erik St. Martin:** Does that mean I'm not allowed to talk?

**Brian Petersen:** Yes, it does. I'm sorry, no more talking for you.

**Erik St. Martin:** I think we were doing \#FreeSoftwareFriday, weren't we?

**Brian Petersen:** We were somewhere around there.

**Erik St. Martin:** Vítor, did you have somebody you wanted to give a shoutout to?

**Vítor De Mario:** Yeah, I have a library to talk about here on the show called [Go Releaser](https://github.com/goreleaser/goreleaser). It's done by another guy in Brazil, his name is Carlos Becker, and it's got like more than 2,000 stars on GitHub, and it creates Go binaries from pretty much every platform you can imagine, it helps you create GitHub releases, push your software as a homebrew formula and all those kinds of things. I've heard of other project using his software to make the release of new versions easier, and it's been pretty successful.

**Brian Petersen:** Yeah, Go Releaser is awesome. I have a confession to make... At my Golang UK talk I announced -- was it Golang UK? Some talk late last year I announced gopher. Rocks, which was the same thing - the ability to tag and release stuff to GitHub, and then three weeks after I did that talk, I found Go Releaser, and it's done, and it's beautiful, and it had a million better features than gopher. Rocks', and I just abandoned it, because Go Releaser does it all already, so... Yeah, thank you for that.

**Erik St. Martin:** I feel like that's almost every open source project I create... It's like, "Oh, this is awesome. Oh wait, somebody did it better than me."

**Brian Petersen:** "Anand moving on!"

**Erik St. Martin:** And I'm actually happy about that.

**Brian Petersen:** Yeah, it doesn't hurt my feelings, it's kind of awesome that it exists and it's far better.

**Vítor De Mario:** Yeah, I wanted to highlight it too because a Brazilian did it, so I kind of had to talk about it. And env config, which Carlisle talked about - I saw someone saying in the same thread that she mentioned (with Frances) that it's also kind of a competitor made by a guy from São Paulo here, which participates a lot in our meetups, which is... I don't remember the name of the library -- something-config, but it's from [arguments](https://github.com/crgimenes) on GitHub... So I'm kind of happy to see these projects coming out of Brazil. Sometimes we are kind of silent here, nobody knows what's going on, but there are a few cool projects coming out of the country as well.

**Carlisle Thompson:** \[56:07\] So people have to go to Brazil and meet all these amazing developers.

**Vítor De Mario:** Yes, and Gopher Con Brazil is the best opportunity for that. Everyone is going to be in the same place.

**Brian Petersen:** Isn't [Sure](https://github.com/tsuru/tsuru) come out of Brazil, too?

**Carlisle Thompson:** Yeah.

**Brian Petersen:** Okay.

**Vítor De Mario:** And I heard about Go Releaser because of Sure. One of the Sure guys, who is also one of the organizers of Gopher Con Brazil, [Guilherme](https://twitter.com/gbrezende), he was talking about it with the Go Releaser created on Twitter, so... Sure is one of our most successful projects, for sure.

**Carlisle Thompson:** Guilherme or [Andrews](https://twitter.com/andrewsmedina)?

**Vítor De Mario:** No, I saw Guilherme talking with Carlos.

**Carlisle Thompson:** So there are two Sure guys who are organizers of the Brazilian Gopher Con.

**Vítor De Mario:** Yes, one former, Andrews, and one current, Guilherme.

**Carlisle Thompson:** Yeah.

**Vítor De Mario:** They kind of switched places. Andrews left the team, they hired Guilherme. So they are both from the Gopher Con Brazil team. I think that was going to happen anyway. Sure is probably the biggest Go project in Brazil, and one of the teams that talk more on conferences everywhere, so one of them was going to be in the Gopher Con Brazil team. That was pretty much guaranteed.

**Brian Petersen:** How about you, Erik? Did you have a \#FreeSoftwareFriday today?

**Erik St. Martin:** I did. So last week or the week before we were kind of talking about serverless a little bit, and there's this really cool project by Alex Ellis called [OpenVAS](https://twitter.com/andrewsmedina), which is Open Functions as a Service. It can basically have your functions backed by Docker containers, and kind of way to do serverless that way. I think they call it like OpenVAS Notes, which allows you to have it backed by [Kubernetes](https://kubernetes.io/).

**Brian Petersen:** Yeah, OpenVAS by itself does't' require Kubernetes, but there is a -- I think they've got the Kubernetes bit merged in, so that you can use Kubernetes as part of OpenVAS if you want to, so you can deploy it on Kubernetes or off. It is really slick stuff.

**Erik St. Martin:** I'm actually really interested to see how this project itself advances, too... Especially with the building over Kubernetes, and stuff. I really am digging watching people build abstractions over the top of Kubernetes and Docker, and I feel like we're just getting more and more innovative.

**Brian Petersen:** Well, you've been preaching that for years now, that Kubernetes is just the foundation that we should be building our software on... Not a deployment platform, it's an architectural foundation, and I've been listening to you, because you're smart, and it makes sense to do that.

**Erik St. Martin:** \[58:55\] Yeah, but I mean, I think it's really going to be interesting over the next couple of years to see what people build to abstract even Kubernetes away... And I feel like I don't -- I have a vision enough to see that that's the thing that's going to happen, but I don't have a vision enough to be the creator of that thing.

Okay, so did we make it through everybody?

**Brian Petersen:** I think we did.

**Erik St. Martin:** Alright, anybody have any other projects or people you want to give shoutouts to before we close the show up? I will take that as a no. So thanks everybody for being on the show, especially thank you to Vítor for coming on and talking to us about genetics and not generics... \[laughter\]

**Carlisle Thompson:** Thanks, Vítor, for not talking about generics. \[laughter\]

**Vítor De Mario:** Yeah, I wouldn't go there. Thanks for having me on the show, and I'd like to thank Carlisle especially for talking with me about it and opening this opportunity.

**Carlisle Thompson:** Of course, it was so great to have you here. It was a great show.

**Vítor De Mario:** Thank you.

**Erik St. Martin:** Thanks everybody for listening. You can find us at GoTime.fm online, or on Twitter @GoTimeFM. If you want to be on the show, have suggestions for guests or topics, create an issue on github.com/gotimefm/ping, and with that, goodbye everybody, we'll see you next week.

**Brian Petersen:** Goodbye!

**Carlisle Thompson:** Bye!

**Vítor De Mario:** Goodbye!
