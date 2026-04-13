**Jerold Santo:** Oz, you wrote an article recently called "You Are Not Google", and it resonated and reverberated across the software developer linksphere, or whatever that is. We all read it, and we all talked about it. Why did that resonate so much with so many people?

**Oman Only:** Look, I was actually a little surprised. I thought there'd be an undercurrent of old people, let's say, who are nodding along, and they're like "Yes, finally somebody's speaking truth to the young ones", but actually... Yeah, it did surprisingly well across the board. A lot of people reached out afterwards being like "I've had this conversation with my manager" or "I inherited this codebase, or whatever... We're really struggling with exactly the thing that you're talking about, and I'm glad you put it out there."

I think we're just getting to the point now where there's been so much excitement, so much promise with some of these technologies... People have actually had time to implement them and see them in practice, and they're starting to get that voice in their head that says "Maybe this is too much. Maybe this is not the right thing."

A lot of people have actually spoken and written about this before, but just the timing I think is such that people are ready to hear this message.

**Jerold Santo:** Yeah. Well, we have short memories as software engineers, so it's nice to hear things, even if you've had that thought or read that before, bring them back up either to a new generation of people who haven't thought about these things, or to those of us who have and forgotten that principle and moved on.

**Adam Staravia:** I feel it's a key thing to keep being reminded of things like this... To even go back to reread books that were pivotal to you, or go reread or be reminded of things like this in your career, to sort of jolt you back into reality, like "Oh, stop chasing shiny objects!"

**Oman Only:** I think it's got to be a counterforce against the marketing machine of hype in new technologies, right? There's a lot of money behind things like Congo, so you've got this constant force online... You don't even realize; they're inventing acronyms, they're sponsoring conferences, and it's just kind of subliminal that there's this active paid force to get you to buy into the new technologies. But there's nobody who's like putting money behind Postgres and sponsoring conferences and got a marketing team inventing flashy acronyms... So we need that reminder just as a counterforce to capitalism, in a way.

**Jerold Santo:** \[04:05\] I was at the OSCAN London and there was actually a Postgres company in the vendors area. So there are people out there doing different things, but yeah, there are voices that are louder than others.

**Adam Staravia:** Or more well-funded.

**Jerold Santo:** Sure. Before we get too far into the weeds here, why don't you just give us the gist of this article? I think a lot of it is right there in the title, "You Are Not Google", but give us the high-level breakdown, and then we'll go into the details of your ways of fighting against this, and then we'll go from there. Give us the gist.

**Oman Only:** Yeah, so the gist is that there are some amazing technologies out there that are great for only a tiny, tiny fraction of companies. We see that they're great, but we forget to consider "Are they great for us?" This is a theme across computer science and software engineering; it's true for newer data stores, distributed data stores like Dynamo and its legacy, Cassandra, Risk and so on. It's true for large scale data flow engines like Map Reduce and its legacy, Hadoop and Spark and so on... But also true of other things, like software engineering practices, service-oriented architecture, where it's been amazingly successful in a very specific context. That very specific context is not your context, and so we just ended up as a community pretending like we do index every website in the world, or we do have tens of thousands of engineers whose teams need to be split up and interfaced.

The post just pulls together some of these trends that I've been seeing a lot of, this over-excitement about these technologies and these practices, and just threads them together like that.

**Jerold Santo:** This is a question that I posed - I think it was with James Pearce of Facebook... Coming from their side, especially as we cover the open source ecosystem and seeing Facebook open source its tools to lots of coverage, to lots of interest, and to lots of people starting to use them, and the question that I posed to him at the time was "Do you guys feel a responsibility for putting out there tools that may not solve other people's problems, but because of the massive interest and because it's Facebook or because it's Google (or whichever company), they received an outsized portion of developer mind share?" and he said that's something that they think about for sure, and they try to address it by way of documentation and giving talks and explaining where they're coming at this problem from.

But the article that you wrote, this principle of "You are not Facebook" or "You are not large company X" really puts the shift back onto the individual developer, not on the company that's open sourcing Cassandra, or putting out there Congo, or whatever, but to us, to actually from the other side not get swept away by the hype.

**Oman Only:** Yeah, totally. You've got to expect that companies like that act in their own self-interest, right? They're not going to open source something unless they think they're getting value from that, whether that's being a magnet for engineers, getting just good PR generally, inviting contributors and offloading some of the work of maintenance, flushing out bugs and that kind of thing. They don't do it out of the goodness of their hearts. Sometimes it's just for retention. The engineers want to have their work seen publically, and they want to get the recognition for that. Facebook or a company like that will support that, to keep their engineers happy.

\[07:57\] But the objective is not to solve your problem. You've got to solve your problem. It's great that they provide these tools for you, but the onus is on you to read the paper, read the docs, read whatever it is that's available. Obviously, it's open source, so read the source code if you can, and really stop and think about your problem, consider the other technologies that might do as good a job, really be honest with yourself about what you need and why you're making this decision, and then pull the trigger. You can't just trust that because it's Facebook it's going to be good for you. Probably if it's good for Facebook it's not good for you.

**Jerold Santo:** We've just recently shipped a show with Gerhard Lazy where we talked about the real world situation of deploying Changelog.com, and that episode has received a lot of praise, Adam, because it was focused around a real-world problem. It wasn't just tools, it was about the Why and the What and the How, and Gerhard really brings a level and a logical method to the way he does things.

One thing that I've been cognizant of, Adam, and I'm curious if you are, with the Changelog itself, because as we cover open source software and the people that make it, do we sometimes contribute to the hype? How do we not just be -- because we like to cheerlead, we like to root people on, we love to see success, and sometimes I wonder if that's something that we have done, which is to just make more noise and less signal.

**Adam Staravia:** Yeah, that's a great thing to think about, because there are times whenever I feel we cover things because it's our duty and our position and our responsibility to share the news, right? And the news is what's happening. It's similar to Twitter and a retweet - did my retweet of that mean that I agree, disagree? Does it represent me or my feelings or did I retweet it because I wanted you to also see it? And I kind of feel like it's on us to sort of share, and it's on the audience to, as Oz is saying here in this article, it's like "Hey, you've got to read the docs, you've got to read the fine print." It's us sifting through and curating what's happening out there, and to a degree disseminating it, but not to every finite point, and I feel like that's sort of our game, it's that focus.

**Oman Only:** Yeah, I think we need the news. We need to know what's out there and what's just arrived that we don't know about, but if the news bringers can give us a bit of the historical context, I think that goes a long way. Some of the people I've spoken to, they don't realize that Cassandra is based off of Dynamo, so just for the sake of your listeners, this guy Avinash Lakshman, who worked on Dynamo at Amazon, moved to Facebook and really reimplemented Dynamo at Facebook, and that's what became Cassandra. Some changes - he got to work on the system twice, so you might say there are some improvements, but it's very similar to Dynamo, which also means that it's very well-documented and there's a great paper.

When somebody delivers news about Cassandra - which I guess is not news anymore, but there's going to be Cassandra's legacy as well - giving the context of "Hey, this derived from Dynamo. Dynamo was created specifically so that Amazon could have a high write availability shopping cart, because they lose money if you can't write to the shopping cart, but it's not such a big deal if the shopping cart is inconsistent, if you see your item twice in the cart..."

\[12:03\] As soon as you hear that, that that was the reason for Dynamo's creation, that they published a paper on it, and you can read it and learn a lot about the rationale and the context, and that became Cassandra, well then the news about Cassandra is less newsy and more like "Okay, this is now an open source version of this thing that worked really well for Amazon, so if I have a problem like Amazon's problem, I can use Cassandra."

Obviously, that takes a lot more work and maybe news is going to stop at like a one or two-sentence historical background, but just being like "Hey, shiny new technology! Cassandra is great because it scales!" That's less helpful than we as providers, reverberators of news could be.

**Jerold Santo:** Yeah.

**Adam Staravia:** Well, there are two sides to us, really - we've got our quick, poignant Twitter/weekly email that we ship out, and then we have deeper, more personal, more human, I guess...

**Jerold Santo:** Contextual, yeah.

**Adam Staravia:** ...contextual, with the podcast, and I think there are times when we hit -- let's say we news-jack something, or we hype train something just because it's on everybody else's minds, and it makes sense for us to cover it. We're not exactly advocating "Hey, because this shiny new tool is shiny and new doesn't mean it's the thing you should choose." We're doing our best to come as interested, curious technologists/developers and hopefully providing context to other people's choices and what fits them for their problems.

**Jerold Santo:** Yeah, the real danger is the cargo cult mentality, as you point out, Oz, in your article. We're going to go through -- you have an acronym of your own, talk about marketing hype, Oz... \[laughter\]

**Adam Staravia:** Come on!

**Jerold Santo:** UNSEAT! We'll go through the finer points in there, because I think there's some great advice in there, even though I've got some qualms with your acronym itself, because I can't help but bike shed...

I think what your overall call here - besides just to point out that this is a phenomenon inside our community which is problematic, as people end up with the wrong tools for the job, and don't find out until much later, and it's much more expensive to reverse that problem... But your overall call is for critical thinking. Or really, you just say -- I guess that's the 't' in your UNSEAT, there's 'think'... So I guess my question to you is what is it about us as software engineering community that makes us so susceptible to the new shiny, and we don't put critical reasoning -- and of course, I'm speaking generally here, so if you're a critical thinker, and you always make the right decisions, I'm not talking about you... But maybe it's just me - I easily just take the shiny, new choice without putting it through that rigorous thought process. What is it about developers that makes us this way?

**Oman Only:** You know, I don't think we're actually that bad. I think we do strive to make good choices and to be thoughtful, but we miss the mark a lot of the time, particularly the more junior engineers, the people who are -- well, I say that, but I still have this problem and I still need to be vigilant about it, so don't take that as me saying "Hey, you youngsters, you are the ones who are struggling to do this." I do this as well, but there's one thing I've observed about the software engineering community, which is that we love fast feedback loops; we love hacking and getting the feedback, and that's in some context excellent, that's something that we can use as a process to do perfect work - just a little bit of input, get some output, have a little REPL going, some quick feedback, Hot Reloading, whatever.

\[15:56\] This kind of thing is great in some contexts, but in other contexts you just need to sit back, turn off the computer, get a piece of paper, be thoughtful and really reason about the problem. That switch from fast feedback, fast input, see your results quickly, get that adrenaline rush of building something directly, to "Hey, let's slow down, let's take notes, let's question what we're actually doing... We have something that's working, but is it the best way that we could do this?" It's kind of counter to that fast feedback thing that works well for us in other contexts.

**Adam Staravia:** I wonder if it's similar to - and this may be very provocative... If it's similar to an addiction? Because I wonder if you can connect something like this to maybe something like where people are addicted to Instagram, or addicted to the feed, the next thing coming, where the reason why you do it is less about wise choices as a developer and more about our actual minds as human beings. We get this rush - you used the words "adrenaline rush"... I wonder if it's connected to something that's far above simply being a developer, if it's just a human flaw.

**Jerold Santo:** That's above my pay grade right there.

**Oman Only:** I think we're really lucky to have a craft where we can be totally engrossed in it, where we can get that feedback, where we have joy from it. It kind of stops feeling like work at those times, which is amazing. I'm sure you've had this experience where you've got this big problem to solve, you sit down, you start writing, and then you look up, your tea or your coffee is cold, it's nighttime, you're hungry... You totally don't know what happened for the last ten hours. That's an amazing, amazing feeling, but sometimes that's not what we're supposed to be doing. Sometimes it's not just sitting down and hacking on something and getting that physiological experience of doing this, like rock climbing, or tennis, or something... Sometimes we actually need to be more aware and less in the flow; we need to slow down, we need to counter our first instincts, we need to question ourselves.

The best engineers can do that, and they can switch between those. The rest of us are working up to that standard.

**Jerold Santo:** While we're speculating, I'll throw another thing into the ring... This is something that I've thought of in regard to this particular problem - perhaps it's part of the revolt against waterfall methodology, the agile movement, where it's like "Head West, young man. Let's just get going, and we'll figure out as we go", and we found out that that's a better way of building software than thinking through every possible thing, wait upfront for six months, and then being done with the design phase and moving on to the build phase, because six months ago we didn't know what we needed, and we realized that as you build software, things change, it's in motion as you're building it. So that perhaps leads to "Well, let's just get going. I'm just going to pick a tool, and I'm going to build it, and then we'll figure that out when we get there."

As with most things, the true best choices are in the grey areas, where you want to move fast, but you have to slow down to think as well. You can save yourself a lot of effort by putting some thought and some preparation, and still doing agile software development. So you don't have to just fly in everything.

**Adam Staravia:** I do feel like there is this push to always be moving. "Motion creates emotion, motion shows progress, fix it along the way... You've got a race to do, so why not just get in the car, even if it has no wheels? We'll put them on the race" kind of feeling, and it's like "Well, we needed four wheels, not two" and you're halfway through the race and everybody else has already finished because they slowed down enough to think "How many wheels do we need?" You're right, motion is sort of the anti, where you're always forced to go forward, and forward is progress.

**Oman Only:** \[20:13\] Have you guys seen Rich Hickey's "Hammock Driven Development?"

**Adam Staravia:** Yes.

**Jerold Santo:** I have not personally watched it, even though I know it's one of his greatest hits...

**Adam Staravia:** That's true.

**Jerold Santo:** It's documented by Rich Hickey's greatest hits on Changelog.com.

**Oman Only:** It's totally worth it, it should definitely be... You know, maybe number two or three. It's got some great ones, but Hammock Driven Development is up there, even just for the name. You've got Hammock Driven Development, and you're like "Hm, what else is there driven development? What is this an alternative to?" You have this amazing visual as well, of this senior software engineer, someone really respected at the company, who's got his sprint planning points or whatever, he's about to stop work for the week and try and get his points, and the first thing he does is string up a hammock, just like sits there...

**Jerold Santo:** Nice.

**Oman Only:** Maybe a couple of hours later comes down, makes a coffee, goes back... This is how a lot of good software gets written, through first thinking about it. Agile doesn't leave that much room for that, or at least it doesn't encourage that. You need to fight to make room for yourself to think before you psyche yourself up for the week and get your sprint points.

Waterfall by default encourages that, it encourages the pre-planning, and it obviously has a lot of other downsides, and that's why as a community we've swung the pendulum away from that. But now the flip side is that it's up to us to really stop and think.

**Adam Staravia:** Coming up after the break we talk about UNSEAT. This is, in Oz's words, I promise, "It's a dorky acronym for you to follow the next time you find yourself googling some new technology to build or rebuild your architecture around." We break down each letter of the acronym, we talk about his clear intent for humour, but more importantly, Oz shares some serious wisdom to consider when evaluating your technologies. Stick around.

**Break:** \[22:24\]

**Jerold Santo:** So the acronym you came up with was UNSEAT. Your articles say "The next time you find yourself googling some cool new technology to build or rebuild your architecture around, I urge you to stop and follow UNSEAT instead." I'll just lay out the words here, the brief synopsis; we'll go into the details. I'll tell you, enumerate is the one that I struggle with here... Anyway, Understand (understand the problem), the N is "enumerate multiple candidate solutions" (that's a stretch, but I get it). The P is "Read the Paper" if you find the candidate solution. The H is "Determine the Historical context", which you've referenced in this conversation as well, and then the A is "Weigh Advantages against disadvantages", and then finally, the T, as we've mentioned previously, is "Think!"

How did you come up with this list and acronym you've got?

**Oman Only:** I'll be honest, this is pretty tongue-in-cheek, and the way that I came up with the acronym was to first think of the dorkiest acronym that I could... \[laughter\] And then fit everything else to it. So I was really pushing for UNCOOL. UNCOOL was tough, because of the two O's.

**Jerold Santo:** That would have been good, though.

**Oman Only:** UNSEAT -- I just needed to massage it a little bit, and "enumerate" was one of those things that I massaged. \[laughter\]

**Jerold Santo:** Well, it's funny because PHAT -- is that still in the Zeitgeist? I don't know... I mean, I know that \[unintelligible 00:25:37.18\]

**Oman Only:** I actually had to ask a millennial about that. I was like "If I say 'PHAT', do you know what that means?" and he was like "Yeah, I've heard that word. I think you can use it", so I went ahead with it, and here we are.

**Adam Staravia:** That's so funny, "I asked a millennial." \[laughter\]

**Oman Only:** Well, you know, I had a couple of people help me edit this, and one was like really doing copy editing, and the other one was helping me empathize a little but with my younger readers, so that was his input, the "That's okay."

**Adam Staravia:** So you started out with the dorkiest way to do it, which means you're (as you said, tongue-in-cheek) not trying to be overly serious. You're trying to make a point, but...

**Jerold Santo:** Memorable.

**Adam Staravia:** Yeah, in a memorable way, that's like "Hey, come on..." - I don't really know, how do you mean by that?

**Jerold Santo:** Like "It's okay to be UNSEAT, you don't have to be PHAT...", P-H-A-T.

**Adam Staravia:** P-H-A-T.

**Jerold Santo:** I feel like I have to say that every time, since we're audio-only...

**Adam Staravia:** I kind of have to go back in my own mind, because I'm 38, I have to think like "Is PHAT that PHAT, that was like saying "That's cool?" So saying UNSEAT is saying like 'uncool.' Just to give everyone context who may not be -- they're probably scouring to Urban Dictionary to get a context of that. It's like saying "This is uncool."

**Jerold Santo:** Right. I think Chris Tucker said it best on either Money Talks, or what was the movie he did with Jackie Chan? It wasn't Friday... Help me out here, guys.

**Adam Staravia:** Yeah, I know the movie. It was a couple...

**Jerold Santo:** Yeah, there was a sequel. Oh, it's going to be one of those shows where people are emailing us...

**Adam Staravia:** \[unintelligible 00:27:24.04\]

**Jerold Santo:** Oz, you can't help us out on this one?

**Oman Only:** No, it was with Jackie Chan...

**Adam Staravia:** Rush Hour.

**Jerold Santo:** Rush Hour, thank you. Oh, that would have killed me. And he said PHAT - Pretty Hot And Tempting. That was the way that Chris Tucker described PHAT. Remember that, Adam?

**Oman Only:** So we've reacronymed it. I didn't realize it was originally an acronym.

**Jerold Santo:** I think it was just a statement of like what's cool. It was just a word, kind of in appropriation of the word "fat", and I think he then backboned that during the movie. Now, I don't have the full history in front of me, but I do have that much. So he said it meant "Pretty Hot And Tempting", but now you have UNSEAT.

**Adam Staravia:** "Unpretty Hot And Tempting." \[laughter\]

**Jerold Santo:** Yeah...

**Adam Staravia:** \[28:16\] That's good context, though. It goes back to that what Oz said before, which was "Give something some history, give something some context", and I think that's just an interesting way to unravel this and bring some humour to it as well.

**Jerold Santo:** Yeah. What we are calling for here first is to understand the problem, and one thing that you state there is that people tend to think in solution domains and not in problem domains. Can you unpack that for us?

**Oman Only:** Yeah, so when I say 'problem domain', I really mean 'your problem', so your business, or your project, or your customers, really thinking about what it is that makes this your problem and not somebody else's problem. That's really the problem domain, the facts and context around that.

The solution domain is the set of tools that you could use, or the architectures that you could use... Really what it might look like, all the candidates of how you might solve this. Now, people think that spending time in the solution domain and considering "Hey, should I use language A or language B", that's what the main decision is about, and you're going to end up there, sure, but most of your time should really be spent asking questions, understanding your own problem, probing that as much as you can, and then out of that you'll be surprised how frequently the solution will just fall out, where you're like "Oh, so we expect to have this happen? We expect to have 10,000 customers use it this much every day, over this period of time, and every write needs to persist? Well, you know, then there's one solution for that, and it's this."

I very rarely see people spending too much time thinking about the problem, and I very frequently see people spending too much time thinking about the end solution, what the technology may be at the end. If you start to go down that path as well, it's just a trap. You start googling, you start reading articles, there's a debate on Reddit or something, and you get drawn into that whole thing. And they don't know about your problem, only you do.

So really, if there's one thing that you take from this conversation or this article is "Understand the problem." Spend the time, ask the questions, dig into it. Everything else should flow much more naturally after that.

**Jerold Santo:** Yeah. So in the next step you say "enumerate multiple candidate solutions", so not just your favourite tool of choice... Now, I start to get conviction on this one, because when it comes to data stores, I just tend to reach for Postgres, and because it's general purpose, I'm generally okay... But perhaps I'm being lazy in that regard. How many candidate solutions is sufficient, and why is it such an important aspect of being UNSEAT? \[whispering\] Oh, gosh...

**Adam Staravia:** You're struggling, huh? \[laughter\]

**Jerold Santo:** I'm struggling... But I like it though.

**Oman Only:** So how many are sufficient? I don't know. I would challenge you to at least think of one, and at least honestly give it a bit of a whirl because the temptation is always "I know this first thing, this default thing, and therefore it's always the best." I'm not saying you need to think of five necessarily, but at least yank yourself out of that confirmation bias, that prejudice that you have for the thing that you first thought of, and just look at it from one other perspective. Maybe after that you're going to think about another one or another one. But if all you do is temporarily yank yourself out of this deer in the headlights kind of fixation with your language or your operating system or your data store, that's great.

\[32:00\] So maybe with Postgres you're not thinking "Hey, do I use MySQL instead?", it wouldn't make sense, but maybe you're thinking, "Hey, do I really need to actually persist this data? Is that really a part of the problem? Could I store it in a file? Could I store it in memory?" So maybe it's that kind of thinking instead that really gives you the different perspective. "Do I really need to solve this problem? Can I just call somebody up and talk to them about it instead?" But maybe at the end you use Postgres, I don't know.

**Jerold Santo:** Right.

**Oman Only:** It's just something to pull you out of the default path.

**Adam Staravia:** Do you have any examples where you enumerated the multiple candidate solutions as you mentioned here, and you were very thankful for doing that task, that discipline?

**Oman Only:** Yes, I have a story in there... I will not name the company, but this actually happened to them. They were using Kafka. The first design of their system was not very good, and they responded to that by really over-engineering their second system. It was Kafka and Samoa and all these really excellent technologies that operate at way, way larger scales than them, and really through a conversation with one of the engineers at the company we ended up with a design that would have more of a traditional relational data store, but which could have honestly been somebody writing into a book. That's actually the design that I push for. I actually push for the data store being somebody receives an email and physically writes it down, maybe in a couple of books.

**Adam Staravia:** Redundancy...

**Oman Only:** Yeah, redundancy. \[laughter\] Or maybe, you know, you have it in a spreadsheet AND a physical book... And I don't think they went for this design ultimately, so maybe I'm not exactly answering your question of when I was personally thankful for it, but...

**Adam Staravia:** Well, to advocate for something means that you must have had some sort of reward from doing the discipline, so I'm just wondering what was something you personally experienced from it.

**Oman Only:** Yeah, I mean... You know, just the satisfaction of ultimately being right. Maybe that's petty, but I live for that stuff. \[laughter\]

**Jerold Santo:** Nothing wrong with wanting to be right.

**Adam Staravia:** Yeah, must be right!

**Oman Only:** I think a lot of the time it comes down to just talking yourself down from the ledge; you get excited about something -- "Oh, I'm really excited about functional programming! Clojure is a really well-designed language, I'm going to use Clojure for this project." One path is to go down that and really feed off your enthusiasm and write your system in Clojure, and the other one is to say, "Hey, but I've actually been writing Python for five years, and it'll be fine if I write in Python. I will, as a company, do better; people will be able to understand me, we'll know how to deploy it if I write in Python." That's the kind of situation where you look back, and you think "Oh god, I'm glad that I didn't go with my first instincts on that."

**Adam Staravia:** Given the next point, I have a question for you, Jerold.

**Jerold Santo:** Yes.

**Adam Staravia:** And since you're using Postgres as your example here.

**Jerold Santo:** Yes.

**Adam Staravia:** If we follow what Oz says, he says to at least give one additional candidate solution to look at and enumerate over, and then once you've chosen that -- let's assume you chose Postgres, so point three is "Consider that candidate solution and then read the paper if there is one." And I just googled a Postgres paper and found a 36-page document from the University of California, Berkeley...

**Jerold Santo:** I know it very well.

**Adam Staravia:** You know it very well, I'm sure... \[laughter\] So this is my question - have you read this paper, the implementation of Postgres?

**Jerold Santo:** \[36:00\] That's funny you ask that, because I was just thinking as we were coming to this third point, you know, I was doing so well up until this one... \[laughs\] And maybe I'm coming out here as not a great developer, because when it comes to reading the paper - I'm trying to think of any papers that I've read with this particular goal in mind of like vetting a tool, where I've gone and said "I'm going to read the paper", and no, I've never read that Postgres document, to answer your question.

I'm just wondering how many people -- maybe I'm the only one here, but how many people will actually do this one? I don't know, Oz... Is this aspirational, number three, read the paper? Should we all be doing this every time?

**Oman Only:** Look, I think if it's a brand-new technology or if it's like 5–10 years old, yeah, you should read the paper. If there's one key paper... You know, if you can go and read the Dynamo paper, or something, read the paper. Because you're going to get so much useful context out of that.

I teach databases, I have a lot of students who use these technologies, and then they read the paper for the first time with me because I assign it as reading, so I see that. I see their eyes light up, and they say "Oh, really? Amazon uses it for that? They want high write availability? Well, we're using it for high read availability. This explains why we're getting this inconsistency." They read the paper, they get the context, and immediately they switch on and understand it at a deeper level than other people at their company who have been using that technology for longer but who just don't have the context.

So I think for a newer technology, particularly if there's one key paper, the Map Reduce paper, or something, that's fairly straightforward to read.

For something like Postgres, because it's older, and it's got a really long legacy, that's harder, and you need a little bit of a guide, like a trail guide. Googling and finding a paper, maybe it's good, maybe it's not... But if you've got someone to point you in the right direction and say "Okay, Postgres has a long legacy. Really it's based on system R. In the '70s there were some key ideas..." -- well, I shouldn't say "based on." A lot of people will be angry with me if they heard that. But a lot of the key ideas in these traditional relational database management systems are from system R in the '70s. Those are well-documented and there are some famous papers there that really -- if you're trying to understand the optimizer, there's one paper there that's still required reading in most databases courses. It's about the Bellwether optimization model. If you want to understand how Postgres really optimizes your query, you want to start by reading that paper from the '70s.

There are a couple of key papers like that, but they are hard to find. You can google "Bellwether optimization model" or you google "Postgres paper." So having a little bit of guidance there helps a lot.

Hopefully you've got senior folk at your company who can point you in the right direction. If you say "Hey, I really want to understand this at a foundational level", hopefully they'll point you to those kinds of resources and not Stack Overflow questions. But yeah, it is tough for sure. You need discipline, you need some spare time at work, ideally. You need to be at the kind of workplace where you can say "Hey, I'm going to read this paper for a couple of hours to get a better sense of what's going on here" and for people to be cool with that.

**Adam Staravia:** I would argue to that you should have to say "Hey, I'm gonna..." Maybe that is too helpful, but you shouldn't be treated like a child, where you have to ask for permission, to say "Let me read a paper to get more knowledge on what we're going to do." I mean, I don't know... \[laughter\]

**Oman Only:** Well, you don't get any sprint points for reading a paper.

**Adam Staravia:** That's true. Well, I think we're back to the whole waterfall/agile; we're forced to produce, and producing is code... Or commits, at least.

**Jerold Santo:** \[40:04\] This might be a good time to mention the Papers We Love repo on GitHub and that community, because what I was thinking there, Oz, as you were talking, is it'd be great to have a centralized curated place where you could just come and say "Okay, when it comes to Bistable or when it comes to Map Reduce, this is the paper, and it's right here." I was thinking "Yeah, I've heard of Papers We Love", so I was looking it up, and actually that's close to what they're doing. They have a data store section, and this is Bistable databases, Dynamo... So you can find all those papers in one centralized place, curated by a community. That takes out some of the legwork that may otherwise prohibit you from finding the best or the canonical paper for this particular subject or tool.

**Oman Only:** I'm glad you brought that up, because they deserve a shoutout. Great community overall, particularly in New York and San Francisco. Incredible organizers. I really would encourage folks to go to those meetups if there's one in their city. Great community, great turnout. There's always a thoughtful speaker focusing on one paper... But then the people in that audience are going to be the folk where you can't ask a question like that, "Hey, I'm trying to understand this thing. What would you read if you were me, or what would you be thinking about if you were me?" It's a totally different community to the standard meetups, so big ups to them.

**Adam Staravia:** For the listeners, if there's an easy thing you want to do right here and right now while you're listening, you can actually tweet @loveapaper. That has their repo link in it, so if you just want to say "Hey, I heard this on the Changelog", tweet that, it'll at least point any friends you have in the right direction. We'll obviously include a link in the show notes, too.

**Jerold Santo:** Absolutely. Oz, moving on in your checklist here... The fourth letter, the H is "Determine the Historical context", and I feel like that keys into number three, the paper, because really when you read the paper you're probably going to tease out the historical context. But the idea there is what you've said previously, where if you found out why Cassandra was such a key tool that was abstracted out because of their necessity for high availability writes. Well, now you know why they built it the way they did, and now you know whether it fits your needs or not.

**Oman Only:** Yeah, absolutely. If you can't find it from the paper, find it somewhere else, or just dig and ask those questions for yourself... Like "Why did Google build Map Reduce? What problem was it solving? What hardware were they using? How much were they paying for it and how much was that an issue, and how much of that fits?" That totally changes the equation.

Whereas if you just google "Is Map Reduce a good tool for this job?", you're probably going to find the answer "Yes" somewhere; somebody said that, and you're ready to read it.

**Jerold Santo:** Well, maybe it's a good moment to add a little self-plug - another place that's great for historical context is podcasts, so find the podcast about the topic. That's one of the things we do. We've just recently had a show about Kubernetes, and we ask those kinds of questions: why was this born inside of Google? Why was it open sourced? What are the reasoning behind it? That's a great way to get historical context if you can't find it elsewhere. Heck, if we ever ship that transcripts feature, Adam, you could even just go read the historical context. \[laughter\]

**Adam Staravia:** Right here on the show you're gonna...? Ugh! I'm just kidding. We do, we need to get that out there.

**Jerold Santo:** I just got all depressed here on the show...

**Adam Staravia:** Oh man, don't do it... Don't do it. Listeners, we have transcripts since episode 200 of The Changelog... So that's a lot. That's like 54+ shows at this point; maybe more, since this show is probably more like episode 260, or something like that. So long story short, we have full transcripts, we just haven't shipped the feature yet. It's because we have other problems we're trying to solve, and that's okay.

**Jerold Santo:** We'll just keep telling ourselves that until we ship it.

**Adam Staravia:** That's the band-aid, that's what makes it okay.

**Jerold Santo:** Next two points here, just to finish up your acronym before we take another quick break is "Weigh the Advantages against the disadvantages." Do you want to expand upon that, or do you think that's self-explanatory, Oz?

**Oman Only:** \[44:11\] Look, it was mostly to get the "A" in there, but... \[laughter\] But you know, there are going to be tradeoffs. The main thing that we do as engineers is decided which tradeoffs to accept, and sometimes we're honest about that and sometimes we're not. To keep going with the Dynamo/Cassandra example, you trade off consistency. Maybe you want consistency. Probably you want consistency, so just being aware of that quid pro quo is what I'm saying there. You get the advantages, but that comes with disadvantages.

**Adam Staravia:** I liked the second half of that though, which was "Determine what was prioritized to achieve what was prioritized." So it makes sense advantages/disadvantages, but in that context it's about determining what was more important versus what wasn't as important, and does that align with your goals or your problem?

**Jerold Santo:** Well, that probably goes back to -- who was it...? Was it the Fred Brooks book, "There's no silver bullet"? We're always looking for the panacea, the perfect solution, the silver bullet to solve all our problems, and what we find out is there aren't any. Everything is a tradeoff, and that's what engineering is - picking the correct set of tradeoffs for your problem domain as you laid out, Oz... So absolutely, if you're going to prioritize something, you have to prioritize something else. Knowing those things before you go into the tool is just -- think, man... That's number six, Think.

**Adam Staravia:** I almost think this is like a par for the course, though. Obviously, you want to think, right? Did you feel like you had to drive that one home, Oz?

**Jerold Santo:** ...with an exclamation mark.

**Adam Staravia:** Yes.

**Oman Only:** You know, really, I want the whole article to just be Think with an exclamation mark and that's it. Just that one word. But you know, I ran that by somebody, and he was like, "Yeah, that's not going to do well, just an article with one word", so I fleshed it out a bit. But that's the core thing here, really.

**Adam Staravia:** Do you think the title "You Are Not Google" is much more sticky than just "Think"?

**Oman Only:** I'm glad I went with this then, but... You know, this is the main thing, and many of us have said this. We do need to say it, because we see thoughtlessness a lot... Even if we're reminding ourselves to be thoughtful as well when we say this.

Writing code is not really about writing, or writing a book is not really about writing. Thinking is the thing that we do mostly. Mostly, we're paid to think, and eventually that gets translated to running code. But the fact is, when you look, most people are jumping to the implementation, most people are jumping to a technology choice, most people are jumping to their way of writing code. We're not thinking.

\[47:06\] The thing that we know works in software engineering is thinking; everything else is contextual, everything else there are tradeoffs. Thinking is the one thing where you can reliably get better results by doing.

**Adam Staravia:** That's awesome. Oz, thanks so much for taking the time to write this post, to come on this show and share so much of what you know about software development and all the wisdom you've shared. I really appreciate your time, man.

**Oman Only:** Yeah, thank you.
