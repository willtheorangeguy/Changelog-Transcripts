**Jon Calhoun:** Hello and welcome to Go Time. Today we are joined by Brad Van UGT, the founder of Rattlesnake. How are you, Brad?

**Brad Van UGT:** Hey, Jon. I'm doing pretty good.

**Jon Calhoun:** Did I get the name right?

**Brad Van UGT:** You got it right, yeah. A lot of people don't, so - full credit.

**Jon Calhoun:** We're also joined by Mat Ryder. Mat, it's been a while... How are you?

**Mat Ryder:** Oh, it's great to be back. I'm good, thank you.

**Jon Calhoun:** How long has it been?

**Mat Ryder:** I don't know. But I've definitely missed everyone.

**Jon Calhoun:** Thanks, Mat. Alright, in this episode we're going to be talking about Rattlesnake, game engines and learning to code by building snake AI's, I guess... So I guess just to kick this off easily - Brad, tell us what Rattlesnake is.

**Brad Van UGT:** Rattlesnake is a competitive programming game, and we kind of take a bunch of cues from e-sports, sort of like more video games and casual gaming... So it's very much a community, as well as a competitive programming environment. You can sign up on the platform, you can do a bunch of challenges on your own, and try different sort of programming scenarios, or you can join some of our competitive play, and our leagues, and our ranked play in tournaments, and that sort of thing. But it's all based on the game Snake. So everyone that's participating is a developer, and they're building and writing and deploying effectively AI's, or in this case just web servers, that play the game on their behalf. So all the games are fully automated, and you can kick off games and see how well you do against various communities.

**Mat Ryder:** Brilliant.

**Jon Calhoun:** See, this is an interesting--

**Mat Ryder:** How fun does that sound?!

**Jon Calhoun:** It sounds fun. It's also like a weird -- not weird, but it's definitely a new genre of games.

**Brad Van UGT:** Yeah...

**Mat Ryder:** Snake.

**Jon Calhoun:** \[04:06\] It's definitely evolved recently... Because before that it used to be a crazy idea of like "Let's have people program AI's for games" and now it's popping up a lot more often, I feel like.

**Brad Van UGT:** Yeah. I think it's fascinating, and it's a lot of fun. I think that one of the things that we do differently - and there are other versions of this popping up as well, but we take a very e-sports sort of style to it, where we do show casting; we have live rankings, we have a weekly Twitch show called Snake Pit Live, which is like a sports centre style, like "Let's check in on who's entered the arena and who's knocked who out of first place" and this kind of thing. And there's back-stories, and people are representing schools, and nationalities... So there's really this sport angle to it that I think is really fun with what we're doing.

**Jon Calhoun:** Awesome. So going back to what Rattlesnake is... I've messed around with it a little bit, and as far as I can tell, you have several different modes, some of them ranging, like you said, challenges that are essentially just "Keep your snake alive" or complete some little objective, and a lot of those - correct me if I'm wrong, but they almost seem like they're ways to get people familiar with the environment and how things work... Is that correct?

**Brad Van UGT:** Yeah, it's very much like self-directed familiarity with the platform and the game. The core Rattlesnake experience kicks off once you get into ranked play, once you join a ranked arena, or you join one of our leagues or tournaments. That's where the real experience starts, and the challenges are there to get you going and to get you familiar with the core concepts and how you control your snake in an interesting and unique way.

**Jon Calhoun:** So let's say I did want to get into this... What does the setup look like for me as a developer if I'm getting into Rattlesnake?

**Brad Van UGT:** Yeah, I think this is another thing that makes Rattlesnake unique. Typically, a strong Rattlesnake developer is typically already a programmer, to some extent. We're not necessarily teaching you to program, it's more taking people that know how to program a little bit and giving them a venue to explore that on their own. So most Rattlesnake developers have a little bit of programming under their belt, they're familiar with a common language, they've deployed some apps, and they're familiar with that process. And then the actual building of a Rattlesnake - what you're doing is you're coding a web server to match an API. So it's kind of like a webhook API that we publish, and so you're actually programming the server side of the relationship. And the game engine, which kind of runs centrally and is heavily concurrent, is constantly sending web requests to your Rattlesnake, which is represented as this live web server that's somewhere; it's a URL that's reachable.

So that's kind of what you're wanting to bring to the table... If you know a little bit about how to deploy an app, or you're looking to figure out how to deploy a web server, and you understand what a basic HTTP API might look like, that's a perfect starting place to start getting involved. And we can talk about where it goes from there, but that's the base level you want to be at.

**Mat Ryder:** So does the game play out in real time, it's making live calls to your server?

**Brad Van UGT:** Yeah, absolutely. It's interesting -- so the game itself... I can talk about why, because I think it's interesting, but we've actually put a timeout on the request, so that you get a request from our game engine that says "Here's the current game state. You're in this game. Here's what the board looks like. What's your move?" And all of your opponents are going to get the same requests in real time as well. And you have a 500-millisecond window to get your response back to us and back to the game engine.

Your response is really simple - it's up, down, left or right. Which direction do you want to move. Then you have 500 milliseconds to decide that. But it's all happening in real-time, so if you don't hit that window, then your snake will just move forward at your own peril. If you're watching the game in real time, the rattlesnakes that are in the game are very fast, and the game plays back really fast. And then part of what we do on the platform is we slow games down to make it much more consumable to most people. So most of what you're seeing when you're interacting is actually replays, buffered replays of pre-run games that usually happened 5–10 minutes ago.

**Mat Ryder:** \[08:15\] Interesting. Yeah, because you can post your rattlesnake on the edge and really go fast.

**Brad Van UGT:** Yeah. Some of the top-tier competitors have figured out where we host the game engine out of, just by spinning up servers in different data centres and different clouds, so they've kind of triangulated where we are, so they've happened to collocate their rattlesnakes right next to the game engine to give them maximum compute time. That's what they're doing.

**Mat Ryder:** Yeah.

**Jon Calhoun:** So theoretically, if somebody was fast enough, they could actually play with their keyboard. They'd just have to respond within a set timeframe every time.

**Brad Van UGT:** So that's fascinating. We didn't always have the 500 milliseconds timeout; we've been doing this -- I'm getting into the history a little bit, but we've been doing this for over six years now, and it kind of started as like a live, in-person developer hackathon where everyone would spend the weekend building their rattlesnakes, and then we'd have a big tournament at the end.

The second year we did it we had one team that built a whole UI. So they were running their own client from their own server, they were WebSocket the entire board state out, they were rendering it in JavaScript, and then accepting keyboard inputs and returning the actually player-controlled snake. At the time, the timeout was five seconds, instead of 500 milliseconds, so it was very playable like that... So we gave them credit. I think they took like second or third place in that tournament of like \[unintelligible 00:09:43.03\]

**Mat Ryder:** Oh, they still didn't win.

**Brad Van UGT:** They still didn't win, which is ironic, but also speaks to --

**Mat Ryder:** Outsmarted by a robotic snake. It's embarrassing.

**Brad Van UGT:** I agree, I agree. But you didn't hear that from me.

**Mat Ryder:** Cheating and then still losing... Come on, at least win.

**Brad Van UGT:** I mean, they got second out of like 40 people, so that's not bad.

**Mat Ryder:** Oh, that's pretty good.

**Brad Van UGT:** It was pretty good. But they didn't get first. So now we have variable timeouts. The default is sort of 500 milliseconds, but we also run game modes where you're only getting like 100 milliseconds or 200 milliseconds to cut out opportunities for that sort of thing.

**Mat Ryder:** That's really cool.

**Jon Calhoun:** I noticed when I was looking at the game it also seemed like you could potentially play multiple games at once... Is that accurate?

**Brad Van UGT:** Yeah, I think that's very much part of the platform, and as you explore, and you start joining different ranked arenas, and you start playing with different friends and people at your school, you learn that your rattlesnake can be in multiple games at any given time. And what we really like about this is it mimics real web development. In order to be a competitive rattlesnake developer you have to think about not only latency, which we talked about, but you have to think about concurrency, of like "How can I be in multiple games at the same time and guarantee response times in all these different games, so that I'm competitive?"

So there's this fascinating, natural progression of like you start just by deploying a server that just goes a loop, or just goes up, or something like that, and then you get into concepts like concurrency, you get into concepts like code optimization, you get into concepts like collocation, and data centres, and this kind of stuff. So it gets really advanced in a really sort of like gentle way.

**Mat Ryder:** That's so great.

**Jon Calhoun:** I imagine this would also open the door for sort of like having a state on the server - which you can technically have at times - where you can sort of remember "In this game, this is the move I took, and here are what I think are the next possible states for the board... So you could almost preemptively start trying to compute potential next options. Now, granted, with food being placed on the board, because - for anybody who's played Snake (I'm assuming everybody has), there's little food pieces that are placed on the board, and when you eat one, you grow a little bit longer. And they're placed randomly.

**Mat Ryder:** And is that your score as well?

**Jon Calhoun:** I guess in most Snakes that's the score, but I don't know in Rattlesnake if it's anything but just surviving.

**Brad Van UGT:** \[11:58\] So this is a mechanic we added early on to make it competitive. I've mentioned we've been doing this for a number of years... The first time we held it, there was no health. There's that whole health mechanic that we had to add, again, in response to players being creative. So we learned that you could be a very competitive rattlesnake if you just went in the corner and hid. That was a valid strategy, and everyone else would eventually outgrow each other and run out of space... So I think a very competitive - this was the first year we did it - a very competitive strategy was just doing that. So we implemented this health mechanic - so you have a set amount of health, and you lose one health for every turn. So you have to eat on a minimum cadence in order to survive and to stick around... So we introduced that, and that's kind of what your score is. It's kind of like your length.

The other interesting thing that we added with the health that's kind of, again, our own take on the classic game, is for resolving head-to-head collisions. So if you go head-to-head with another rattlesnake, if you're both the same size, then you both get eliminated. But if you're longer, then the other player gets eliminated. And so this means there's this awesome trade-off between defensive and aggressive play. You can try to get food and try to gain length advantages and try to outmanoeuvre your opponent, but the trade-off there is you start to run out of space sooner. So you have to be a lot more strategic in how you're manoeuvring in order to pull that off.

But yeah, the randomness of the food is what sort of like -- you can precompute a bunch of states, and a lot of people do, and then you just have to throw away the bad ones after food spawns.

**Jon Calhoun:** I was going to say, this technically could open up the doors to pre-computing a bunch of states even when you don't have a web request in, just knowing you're in the middle of a game... And then when you get a response back, sort of deciding was one of those correct, or not, and sort of moving from there... Which could give you a huge advantage if you get things right, because then all of a sudden you could have a lot more precomputed.

But this definitely is the -- you must be at the high end of building your AI spectrum, because this is not like an intro level... It's not where you would start out, I don't think.

**Brad Van UGT:** Yeah. I mean, you start with very simple strategies of like "Try to not run into myself, and try to maybe find some food." And then it kind of grows from there. But we have -- just to talk about the API a little bit... So you're getting requests for every turn, but you're also getting a request for the start and end of every game. That exists so you can do resource allocation. You can do asynchronous process spin up or spin down; you can do storage if you want, or cross-request storage or persistent storage... And we have developers that do all of that stuff, and some of them take it to really incredible levels of complexity and pre-computation.

It's a fascinating... We think of it as solution space, but the solution space for what we're doing is very broad, and it just makes it -- like, no one's doing the same thing. No one's doing the same thing, no one has the same strategy, everyone has their own flavour and their own creativity that they're bringing to the table, and it makes the community really fun to be a part of.

**Mat Ryder:** Is it difficult to get into if you want to start? Are we at the point like Call of Duty, where the players on there now are just so good there's almost no point even trying? How do you tackle that?

**Brad Van UGT:** We're not there yet, and it's kind of an open question whether we get there... We have new players show up all the time and just start dominating leaderboards because they're deploying strategies that either learning algorithms haven't seen before, or they're learning a new way, or they're using this strategy... Or oftentimes we have players show up with -- we think of them as hand coded snakes, or hand coded rattlesnakes, that are employing strategies that the AI players haven't seen yet.

A perfect example of this is -- I'll tell a little bit of a story. So we ran Fall League last September, and we had a new Rattlesnake developer come in, no one had ever met them before; their username was Tofu. This is what they called themselves. And they picked this mid-beige colour, and their snake was blocks on both ends. They really played up the theme.

\[16:10\] But they just started destroying leaderboards all over the place. They were just winning game after game, and they were knocking out top-tier multi-year Rattlesnake developers. And we didn't know anything about this person, so we were like live casting games, we were on Twitch, we were talking about strategies, but we have no idea what tech they're using and how they're going about this.

And then we had one developer from the community study Tofu's games, like game after game, and they identified a very specific situation in which Tofu was vulnerable. So they programmed a rattlesnake to at all costs try to force this situation. And it was a situation where Tofu would go against the wall in a way that was disadvantageous for itself, and then if you caught this scenario, then you could cut it off really quickly.

So this one developer named Smallsco actually created a rattlesnake specifically for taking out Tofu, and they could beat Tofu regularly with this strategy. Their rattlesnake was terrible at beating anyone else, but they could beat this one top-tier competitor semi-reliably, because they had identified this weakness.

**Mat Ryder:** Wow, that's so cool.

**Jon Calhoun:** I imagine this is where Rattlesnakes starts to shine for experienced developers... I mean, you've talked about people who've been playing this for a while. Are people actually taking machine learning strategies and applying it to this? Is that what you mean by people who have never seen a strategy before, and they lose early on to it?

**Brad Van UGT:** Yeah, we're starting to see some AI and some reinforcement machine learning strategies being deployed... I think what's interesting - they tend to not be hypercompetitive, except in the Tofu case. And the reason I bring up that is because we don't actually know what Tofu was doing. We never actually met them. They destroyed Fall League and then they retired. And I think you can still find their profile on the website, and they changed their back-story to just be like "Officially retired as of this year." But we're starting to see more AI's or machine learning strategies pop up... But the community that follows this isn't about being the top-tier competitor. It's not about winning. It's about using this as a venue to try different things.

A lot of our developers are using this as a reason to get into reinforcement learning, to start looking at things like TensorFlow, or even to learn new cloud platforms. If you're looking for a reason to try GCP, or you're looking for a reason to get into Rust and see what it's like to program a web server in Rust - that's the primary use case that we're finding. It's more about a fascinating feedback mechanism and a fascinating way to explore a new language or a new technology where you can see progression on your own terms.

**Jon Calhoun:** Yeah. And as far as the learning goes, you have a process that's relatively easy to jump into, at least for Go. I haven't looked at the other languages. But the Go process was - literally, you say you want to start building in Go and you have a repl.it. Basically, it allows you to clone your project like you'd clone a GitHub repo, but it's cloned on this self-contained development environment where you can literally just hit the Run button, and you have a URL to connect your rattlesnake, and you just paste it into the Rattlesnake website, and you have something running.

Now, to be fair, it's a very bad AI. I think it chooses its moves randomly, so it kills itself a lot, but basically--

**Mat Ryder:** It's still better than a lot of AI.

**Brad Van UGT:** Yup.

**Jon Calhoun:** You've got something that's at least running, and you can verify "My code is connected to this server" and it gets you past all those initial hurdles, which historically with programming and learning to code and getting into something, usually that's the biggest barrier, is like just getting started. And then from there, it's an awesome starting point, which I've noticed repl.it and other things like that are awesome tools for getting people involved, and something that would otherwise take a lot of effort.

**Brad Van UGT:** \[20:03\] Yeah. I think that's one of the ways where it shines. Replit is a partner of ours, they support what we do, and we're fans of what they're doing, but also we have tutorials if you want to use Heroku. We're working on a tutorial now if you want to use Railway. The AWS team - there's an open source rattlesnake that was made using AWS SageMaker by the AWS SageMaker team that they built, and it's just to show off of like "Hey, if you want to try this, here's a fascinating way to try it." So what we're starting to see is the community is really giving back to us in that regard, in that they're making tooling... We think of them as starter projects, or starting repos, that have a lot of the infrastructure in place so you can just get to programming quicker, which is kind of the crux of it.

**Mat Ryder:** Yeah, I love that. I love the idea that AWS are using it. I imagine Google are going to do it... And maybe it could end up being a good way to settle IP disputes in the future.

**Brad Van UGT:** Yeah, 100%. It'll be like "Let's just take this to Rattlesnake, and we'll see what happens."

**Mat Ryder:** Let's Rattlesnake it out.

**Brad Van UGT:** It's interesting... So I mentioned we run leagues; we ran a spring league earlier this year, and the AWS team actually entered the league as an official AWS team. I think it was a team out of the Vancouver office. They got 39th out of like 300 developers. They didn't even come in top 20. But now they're fired up. Now they're "Oh, okay. We can't stand for this", and so we have other companies --

**Mat Ryder:** They're going to run it on the Google Cloud Platform?

**Brad Van UGT:** Yeah, maybe they should switch cloud platforms...

**Mat Ryder:** I was going to say that.

**Brad Van UGT:** But yeah, so now we have other large companies that are coming in, and they're like "Hey, our engineering team wants to play. What does this look like?" And that just makes it more fun. It makes it fun for everyone else competing as well.

**Mat Ryder:** Yeah. Is it good for like a team building thing? Someone in the Slack channel Gophers Slack, the GoTimeFM channel mentioned that they used it as a team building thing. I bet it is great for that, ain't it?

**Brad Van UGT:** Yeah, it's really fun. And we have some tools for that, and we help a couple -- like, it's not really our core effort, but we have larger engineering teams that have come in and been like "Hey, can we run one of these things?" And sometimes what we'll do is we'll run a little mini-tournament for them. Sometimes we even put them on Twitch if we're allowed, which is really fun... But sometimes we just run it privately for them as well. And then what we'll try to do is get the winners from those to come back into the community, and we'll get them on one of our shows, or we'll get them on Twitch, or we'll get them into a tournament that we're running.

Part of this is making the developers feel like rock stars. It should feel really cool if you win one of these things; it should be really cool if you develop this rattlesnake that is particularly good at destroying Tofu. We want you to feel like a hero in our community because of that.

**Mat Ryder:** Yeah. I wonder if that rattlesnake that beat Tofu was funded by Big Beef. \[laughter\]

**Jon Calhoun:** Oh, boy...

**Break:** \[23:07\]

**Jon Calhoun:** When people are getting into this learning process, I've noticed you have the challenges. Do you want to expand a little bit on what those are and how they help people get started?

**Brad Van UGT:** Yeah. The challenges are a new thing, and they're constantly evolving. We see the challenges as sort of like a bridge to get you into competitive play, because multiplayer play is where the strategies start to get fascinating. It's not terribly challenging or difficult to write an AI that can do well in the game Snake all by yourself. After a bit of effort you can get something that survives most of the time, and then you're just dealing with edge cases... So the challenges exist as sort of like this bridge to like "Okay, let's talk about how you avoid yourself, let's talk about how you get food, let's talk about how you avoid walls..." There's an interesting challenge where you can actually go up against yourself, and our goal there is, again, to introduce the idea of concurrency... Like, "Now here's a challenge where your server is actually playing two snakes on the same board, and you're trying to outmanoeuvre yourself." But what does that due to your latency? What does that due to your processing power? Let's introduce you to that, and then gradually bring you into more competitive multiplayer play.

**Mat Ryder:** It's genuinely getting me excited about doing this.

**Jon Calhoun:** The next questions I'd have are -- like, this is a great way to, like you said, learn new languages, try deploying to new servers... Have you guys thought about more of like the pros and cons, areas where this shines, versus areas where this is maybe not the best learning tool?

One of them you mentioned was if you're a beginner to programming in general, this is probably not the best fit, because it's not going to teach you a Hello World server; you're kind of expected to have a little more experience than that. Are there other use cases where it shines, or just ones where it's not quite as great?

**Brad Van UGT:** I mean, there's so obvious ones... We don't do really well with frontend. Obviously, there's no frontend programming involved in this. It has to be basically web-based dev. But beyond that, if you think of it as like web backend development, once you're in that area, basically anything goes. But I will underscore that if you're looking to learn to program, there are lots of things out there that are perfect at that; there are lots of things that take a gamified approach to it. There's lots of people out there that want to teach you to program. That's not really what we're doing. What we're doing is you're a level one programmer, you're a junior/intermediate programmer, and you're looking for a reason to try something new, you're looking for a venue to program recreationally. That's our core -- you know, we didn't set out on purpose to provide that; that just tends to be the type of developers that want to play, and so we've learned to kind of lean into that.

**Jon Calhoun:** I've noticed this type of game is very good for solidifying your reasoning and logic skills, whereas one of the areas I've seen this type of thing not do that well are things like if you want to get into code structure and building a really large-scale application, this doesn't necessarily teach you the skills to organize code and work with the team in that sense... If you're trying a new strategy out, you might whip some code together real quick, thinking "Let's see how this goes. I'm probably going to throw this code away, because it doesn't work."

**Brad Van UGT:** Yeah.

**Jon Calhoun:** You and I were talking though at one point about one of the areas - it was before we got on air - that this could potentially go is sort of the testing realm... And this happened before we recorded this, I was trying to make a rattlesnake myself, and I've found myself really wanting to have a case where I could take sort of a test game state and be like "Alright, if I give this to my game, what does it do? Does it do what I want it to do?" And it'd be great to have some sort of way to give it a game state without having to manually construct everything that would be in the JSON, the whole request payload, and then to actually test your code and say "Does this give me the response?" And Brad, I believe you said that the community built some tools sort of like this.

**Brad Van UGT:** \[27:59\] Yeah. I think it was like -- your Rattlesnake AI is very easily unit-testable. It lends itself -- the inputs and the outputs are very well-defined... Of like, "Given this game state, if up is the only valid move, then I'd better return up 100% of the time." So you can add this sort of unit test...

I mentioned the idea of like - we've found that Rattlesnake development kind of follows this natural progression of web development as a whole. You start to think about latency, you start to think about performance and concurrency, but you also start to think about unit testing, or specifically regression testing, because that's a really easy way to make sure that you're not harming your AI as you continue to develop.

We have an endless backlog of things that we would like to do in this realm, but to touch on what you've mentioned specifically, the community has done a phenomenal job... We have a Discord server, we have open source GitHub repos, there's a large community that follows this and participates... And they've started to give back tools to the community. Someone built -- I think they call it a board generator, but basically it's like a little UI where you can paint a board state. You can add snakes, paint their locations, and then you can export that as a faked JSON game request, and then you can say "Okay, now import this as a test case that I want to hit against."

We've also had someone build a desktop app that actually lets you run games against the local snake. One of the interesting things - because everything's live - in order to test changes, you have to deploy your snake, \[unintelligible 00:29:21.26\] iteration time... But now there are tools where you can run CLI games locally, you can use this desktop -- it's called Mojave, if you're looking for it. You can run local games against your rattlesnake locally, and test out different scenarios, and you can pause and rerun frames, and this kind of thing. So it's fascinating to see what the community is doing to support this test-driven development.

**Jon Calhoun:** That to me is a really cool introduction to test-driven development and learning the value of tests... Because like you said, with regression tests and some of that, it's -- tutorials are often hard because they even have to simplify things so much that they don't really help you in the long term, or it's such a complicated application that you really don't understand everything... Whereas this one's one where there's just enough complication that you really understand what's going on, but it's simple enough that you clearly see "Obviously, if going this direction has caused me issues in the past..." You mentioned the one case of like the only way to not die is to go up, then you want to go up; but there's also other cases that aren't quite as -- they're not as clear-cut in that specific moment, but you know you want to test for them.

I guess an example I can give is when I was making my snake, when I'm messing around with different strategies, one of the things you could easily do was make a U-shape with your snake and then try to travel inside of it, so you essentially box yourself in. And you don't necessarily die in that first move, but you know you'll eventually die. So as you start to realize these cases, you can start to be like "I need a test case to make sure this doesn't happen anymore." And the development process is really natural in that sense. It's like, "Okay, the first thing I want to do is just not die or not run off the board. The next thing I want to do is not starve to death. The next thing I want to do is not go into another snake." You slowly add these things, and they can all be test cases of like "What do I do in this particular case?" and it's a really cool progression, similar to the natural development cycle.

**Brad Van UGT:** Yeah. It's a really natural progression, too. One of our team members, her name is Aurora, and she always says the first four steps of Rattlesnake are like first don't hit walls, don't hit yourself, don't hit other snakes, and then eventually try to find food. If you watch someone build a rattlesnake for the first time, that's always the steps they take, and it's typically in that order as well.

So the challenge is kind of like us leaning into that a bit more; we're starting to produce more content around how to achieve those first four steps. We've also thought about adding some more basic, some more base-level code to the projects that we publish. You mention that like -- I think the Go Starter Project just moves randomly, but we could start adding maybe some helper functions to do distance calculations, \[unintelligible 00:32:05.16\] or this kind of thing. Not solve the problems for you, but give you some of the tools that you're probably gonna want to use. Still let you apply them.

**Jon Calhoun:** \[32:15\] Yeah, definitely. So another thing we've sort of talked about is I believe you mentioned that you have a CLI for running this locally. And if I recall correctly, that's written in Go, which also means that essentially your entire game engine is written in Go then. Is that correct?

**Brad Van UGT:** Yes, it is. And most of it is open source. So if you go to our GitHub - I think it's called the Rules Repo - the entire game logic is implemented in Go and is open source, so that anyone can see it. We get this a lot, where developers are eliminated in cases where they don't necessarily think it was fair or whatever, and so we're able to point to source code that says "Well, we're running this code. You can take a look at it and see exactly what's happening." And a lot of devs like to look at the source code to debug order of operations in the game engine to figure out exactly when food consumption happens, when does elimination detection happens, so that they can program against these super-tight edge cases... And with that, again, the community built a little CLI tool for running games locally. So that's baked into that repo, and that's all written in Go.

We chose to write the game engine in Go because that was something we were familiar with, but I think it turned out to be a really phenomenal choice, and the community has really leaned into it.

**Jon Calhoun:** As far as writing a game engine in Go - have you ever written one in another language, or can you compare that to anything else?

**Brad Van UGT:** I think this is so unique... It's so unique in that the entire game engine is web-based and web-request based. So typically, if you're writing a game -- well, writing a game engine is kind of its own thing. I've written toy game engines, as most devs do at some point in their career, using Python and more scripting languages, or sometimes Lua-based... But I think this setup is pretty unique.

We originally chose Go mostly for performance. Because if you look at what's required of the engine, it's all very basic -- I'm going to say some things that obviously lend themselves towards choosing Go specifically, but very basic structures, very basic communications, but super-high concurrency and super-high performance requirements.

So you're looking at if we've got a game that's running -- you know, an average game is going to have four different players in it, and we're running 100–200 games at any given time, that's a lot of processing power and a lot of synchronous I/O to handle... So Go obviously makes that a lot simpler than it would be in other languages, for example.

The original game engine was actually written in Python. Like, old Python event loops - it was just a real pain to figure out what was actually happening. So we rewrote it four years ago.

**Jon Calhoun:** Okay. My follow-up question to this would be - you said you needed this to be open source, so people could look at it and actually see what's going on... And as Go developers, we often claim that Go is easy to read and consume, and that's one of the perks of it... Has this generally been true, given that I'm assuming that a huge chunk of your audience and people playing the game don't actually write Go code?

**Brad Van UGT:** I think that's an interesting question. I've never received complaints that the engine has been written in Go, so I would tend to agree with that and be like, for most developers, they can probably understand what's going on. We've also gone to great lengths to document the open source stuff fairly well and explain the high-level blocks that are in play... But I think that the simplicity of the language, the simplicity of the implementation definitely lends itself to be readable by most developers, even if they're not Go developers specifically.

**Jon Calhoun:** So following up to this, the one thing I did notice was that because this is written in Go, I feel like Go developers have a slight advantage, in the sense that they can then take the game engine or the rule set, and if they're trying to actually play out like "What are the next possible ten steps, depending on what moves are", and basically just doing a brute force sort of approach of "Play the next ten steps and see which of my moves will do best", you can do this pretty easily -- well, I say "pretty easily." You can do it probably more easily in Go, because you can actually import that code, and you're having a game engine running inside your code, and you can sort of work from there. Has that actually proven to be the case, where ones written in certain languages are more performant than others?

**Brad Van UGT:** \[36:20\] I wouldn't necessarily say performant, but I would say there's a clear advantage to being able to run the actual game logic within your AI, within your bot.

**Mat Ryder:** You meanwhile they're actually battling?

**Brad Van UGT:** Yeah. So what you'll do is you can simulate future game states and then use the game engine in real time to resolve those game states and to resolve those moves. Speaking of natural Rattlesnake progression, I think this is kind of a more advanced level, but we do see it a lot. And a lot of developers will start to implement early versions of game logic themselves into whatever language they're doing, but we also have -- there's an ongoing project right now in the community to have the game engine cross-compile to WebAssembly. I don't know if that's a good idea or not... But that exists so that it would kind of maybe take down that barrier and allow anyone to start importing and running the rules locally. I think there's obviously performance hits attached to that, and if you choose to write your rattlesnake in Go, then there are clear advantages because the game engine itself is in Go... But I don't necessarily know that that's a hurdle. Again, part of what we really like about this is if you get to this stage, and you start thinking about -- the rule engine is actually written as an importable Go module, so you can just add it as a dependency to your app.

So you can start to think about things like "Okay, how do I add this as a dependency? How do I call out to the library? How do I measure the performance of it?" And again, those are all real-world software development scenarios and questions that a professional developer will regularly ask themselves.

So if you're willing to take a WebAssembly version of a cross-compiled version of this, what are the trade-offs? We kind of want you to go through that. I think, again, that's what makes us compelling.

**Mat Ryder:** Yeah. I wonder if people have done things like fuzzing as well with that technique. Probably, right?

**Brad Van UGT:** Yup.

**Mat Ryder:** Yeah.

**Brad Van UGT:** An early strategy will just be to select moves randomly, play out as many as you possibly can into the future, build a tree, prune the ones where you're losing, and then select the one where you survived the longest. Think of that as like an early look-ahead strategy... But you learn very quickly that that takes a lot of compute, because of the multiplayer nature of the game. Because everyone's moving on the same turn... So even looking one turn ahead, you need to run 4*n different states to look at that, and then that just explodes once you start to consider random food spawn, and that sort of thing.

**Mat Ryder:** And of course, you don't know what other players are going to do, do you?

**Brad Van UGT:** Yeah.

**Jon Calhoun:** I imagine you could get to a point where you could assume everybody's playing optimally, but that might also hurt your AI in the sense that not everybody is necessarily going to use your strategy and play optimally based on your strategy... So it could just be weird all-around. You almost need to put a bunch of weights into everything as to like "I don't really know what's going to happen."

**Brad Van UGT:** We have, again, very top-tier players that adjust those weights based on their opponents as well. So if they recognize -- in the request you get the name of your opponents, and if they recognize a name, they'll be like "Well, I know that this player tends to-- like, the safe, defensive strategy would have them move this way, but I know they tend to be more aggressive and a little bit more risky in their play, so I'm going to wait accordingly, and I'm going to take that in consideration."

And then that player can then counter -- there's this counter-play that goes back and forth, right? So long-term, the game gets closer to something like Rock, Paper, Scissors, where you can kind of counter moves... There's no AI that's going to win every game. That's not possible.

**Jon Calhoun:** \[40:06\] I definitely noticed some of that when I was... So I first started setting up my AI, and one of the first things you almost always -- I'm assuming most people do when you start looking at other snakes, is if I move here and another snake moves here, you're like "Well, we could both potentially die, depending on (like you said) snake length and stuff... And at the time I didn't even know about snake length, so I wasn't really sure what would happen... So I'm just like "Let's just avoid this move altogether." And I'm guessing most people do this, so early on, if you're thinking about it, you could probably safely go there knowing that most Ais are not going to take that chance... But like you said, there could be some snakes that you realize are super-aggressive there, and you're like "Oh, I don't want to risk that right now." So there are definitely a lot of factors that could go into that, deciding what to do.

**Brad Van UGT:** Yeah. In competitive play there's a couple different tiers and ranks. There's Bronze, Silver, Gold, and then Platinum and Elite. And Elite is typically the top 16 players at any given time, we try to keep that capped. But the Silver and the Gold play is fascinating, because you start to see -- like, the way you break out of those tiers is you start to realize that those trade-offs are being made by everybody, and you start to realize that you can take advantages of those.

So if I'm in a Gold tier, and I'm up against Gold tier competitors, I know that you're probably going to shy away from head-to-head collisions, because you haven't considered that; you haven't considered the future states in which you could win those. And so I can use that to be extra-aggressive, or I can use that to outmanoeuvre you in different situations. It's fascinating to watch how Gold play lends to Platinum play, and how it lends to Elite play.

**Jon Calhoun:** I assume those also are a way of making the game accessible... Because Mat had asked earlier if this is like Call of Duty, where essentially there's no point in starting. And I've noticed the games that do that tiered model, especially e-sports type games - you might not notice it playing, but as a spectator you can generally tell by watching the things that somebody does, or in this case a rattlesnake does, which tier they're probably gonna fall into.

**Brad Van UGT:** Yeah.

**Jon Calhoun:** My own personal experience is I played Star craft for a while and I kind of learned that you could be terrible at managing units in a battle, but as long as you got the macro-production stuff right, you could get to a pretty high tier, because it just didn't matter; as long as you would keep fighting over and over again, the other small things didn't matter as much. And I'm assuming in Rattlesnake it ends up being similar, where as long as your AI takes care of certain things, it will eventually get out of certain tiers, and this allows people to start in the low tiers as beginners, and then gradually move their way up.

**Brad Van UGT:** Yeah, that's exactly it. And we use -- most of the team is Star craft players; we've all played Star craft at some point. I think Star craft is a really apt analogy for that sort of progression. An example is for gold play there's no look-ahead. Most people are operating in a stateless fashion. It doesn't have to be stateful to be look-ahead, but they're only competing on the current board state, so you'll see general behaviour optimizing for self-survival, of like "How do I survive as long as possible in this situation? I'm just trying to avoid everything and not get myself into dangerous situations."

And you start to see things like \[unintelligible 00:43:07.08\] and this kind of algorithms to detect the traps, the self-trap scenarios that you pointed out... And then as you break out of that, then you start to get to the higher tiers. Absolutely, absolutely, and I think that's what makes this super-interesting.

**Break:** \[43:21\]

**Mat Ryder:** There's a great documentary about DeepMind doing the game Go, and they also -- you can find it online, there are videos of it playing Star craft... And they noticed when they were watching it that they would put them up against world-class players, and they realized that the AI would make silly little mistakes, things which is a player had made that mistake, you'd think this person's not going to win now. They've made this kind of schoolboy error. But then they AI goes on to win, and it turns out it just sort of didn't matter.

**Brad Van UGT:** It turned out it doesn't matter.

**Mat Ryder:** Yeah, in the end. Does that happen in Rattlesnake? Do the snakes act weird?

**Brad Van UGT:** Yeah, and I think -- I have a fascinating example of this. And these are hand coded snakes, so I'll add that these aren't necessarily machine learning or reinforcement learning-developed... But before Covid we used to run in-person events, and it was really fun, and we had show casters, and DJs, and stuff like that. The in-person 2019 championship we had one competitor and they were called Undefined Behaviour. Their rattlesnake was called Undefined Behaviour, and they entered it into the -- it was then called the Veteran, which was the top tier division. And they actually had accidentally coded a strategy that actively avoided food. And this was the first time that we'd ever seen this.

So they started to -- like, the casters are trying to cast this game, and they're like... And you can watch it, it's all on Twitch; you could watch the \[unintelligible 00:45:41.28\] and the casters don't know what to do with it, because this top-tier Veteran Rattlesnake developer just looks like it's going to starve out. It's doing everything it can possibly do to not consume food. And then at the very last second it would somehow make it out. It would somehow make it out of this situation.

We were all like "This is silly. Why is this snake even playing in the Veteran division?" But then they just kept winning games repeatedly. Winning games and defeating other people because their opponents would just get too long, and they weren't able to manoeuvre. And they ended up taking the first place.

And the finals broadcast for that tournament is one of the best Rattlesnake moments we've ever had, because no one expected much of this snake; no one expected it to do well, but this one developer had sort of accidentally stumbled into this very interesting macro strategy of just trying to stay as short as possible for as long as possible. And they took -- it was a $5,000 prize pool that they took home because of it. It was crazy.

**Mat Ryder:** Wow. I can smell a Netflix special coming on with this... \[laughter\] It sounds so dramatic, doesn't it?

**Brad Van UGT:** This is like "Follow a year of like a top-tier Rattlesnake developer..." It's like, the Tofu Documentary.

**Mat Ryder:** Yeah, it's just the rattlesnake that you follow.

**Brad Van UGT:** Yeah.

**Mat Ryder:** Yeah, he's the star.

**Brad Van UGT:** \[laughs\]

**Mat Ryder:** The Tofu \[unintelligible 00:46:57.23\]

**Brad Van UGT:** I love it, I love it.

**Jon Calhoun:** I love when you throw games into the mix with AI, because we all have this preconceived notion of what is good play in certain games, and then we quickly realize that the things we cared about might not actually matter in the grand scheme of things.

**Mat Ryder:** Good metaphor for life.

**Jon Calhoun:** It's hard to figure out what actually is the case and what isn't... Because Star craft one you mentioned, Mat - I remember seeing that too, and it's always challenging to see, because you'd wonder if pro players could actually learn from that type of thing, taking AI from games and watching them and deciding "Is my entire strategy based on the wrong -- am I prioritizing things incorrectly?" and we could see sort of what goes from there.

Now, granted, it might also be the case where an AI might be able to click or do something that's inhuman, so that's always a...

**Mat Ryder:** No, they actually made sure that this couldn't in the Star craft case with DeepMind. They made sure it could only see what the other player can see, and it could only interact at a slower rate, like one-click a second. So they even slowed it down.

**Brad Van UGT:** Oh, really? It was artificially--

**Jon Calhoun:** I know the click rate is always weird, because if you've ever watched a pro player play, they click a million times without doing anything, I feel like.

**Mat Ryder:** Yeah, sort of keeping warm and agile, aren't they?

**Jon Calhoun:** I'm like, "What does this actually translate into? What is their actual click rate of useful moves and--"

**Brad Van UGT:** \[48:17\] Like actions per minute versus clicks per minute?

**Jon Calhoun:** Yeah. What is the actual useful number, and does that actually matter? I'd be curious to see if you could take AI's and just bring that as low as possible to see "Does this make a difference in pro play or not?" That's the type of thing it'd be really fun to do with DeepMind if you had the opportunity to.

**Brad Van UGT:** Yeah. I think there's an interesting component of this... So looking back to DeepMind playing Star craft, or even like OpenAI playing Data - they were doing a very similar sort of show match there - it's really inaccessible for most people to watch those things and understand... Unless you're at this intersection of understanding how AI works and then also understanding how Star craft 2 works mechanically at a very high level, it's really hard to appreciate and understand what's going on. And one of the things where we kind of -- again, we didn't set out to do this, but Snake itself is hyper-accessible, because the mechanics are so simple. You're just moving up, down, left or right. And so we can start to watch these things unfold. We can watch this unconventional strategy completely disrupt these highly-developed AI's, and everyone in the audience understands why... Versus just like -- we don't have to go debug and debrief and figure out... It's not like the pro Seacraft 2 player watching the replay and trying to figure out where the advantage is gained. We all see it. We all see it happening in real time, and we understand where the deficiencies were.

**Mat Ryder:** Yeah, that's a perfect point.

**Jon Calhoun:** Snake is like -- we didn't even describe the Snake game, because I think we all just assumed everybody's played it before, because it's been on every device... I think every early cell phone had Snake -- well, maybe not everyone, but a lot of them did. But there were calculators, and everything else that had Snake that I can think of.

**Brad Van UGT:** Yeah. We think of it as like it's universally-recognizable, which is kind of -- again, we did it because it was fun, but it turned out to be this fascinating aspect of it. I mentioned we used to do live, in-person events and show matches and tournaments, and those events - they drew a crowd. We had people in the community who were not programmers, and just wanted to come out and watch it, because it was really fun to watch, and you could see what was going on... Versus, again, like a Star craft 2 e-sports, right? Most people who are watching that are either Star craft fans or Star craft players. There's a fascinating non-programmer-based audience for what we're doing.

**Mat Ryder:** Yeah, I could see that. If I wasn't a programmer, I'd watch it...

**Jon Calhoun:** I've seen some other games like it. I'm really interested in this space of programming AI's for games, because I've seen some other companies that do the whole "It's essentially meant to teach you" programming, and it goes -- it's kind of hit or miss sometimes. I feel like sometimes there are some big leaps that are hard, but there are even some games around that, isn't there? Like Something A Billion Humans, or something like that...

**Mat Ryder:** Yeah, I know what you mean. I'll find it.

**Brad Van UGT:** Or even things like Slither, or Generals was the other one... It started out as like a human-played game, but at the end of the day everyone was writing bots for it. That's just how it ran. Or you can also look at things like Screens is a fascinating example, which is like a full Steam-based game where I think you upload your JavaScript, and they run it for you, and it's all fully autonomous, but it's more of like an open world... Yeah, I think there are a lot of fascinating things cropping up in this space.

**Mat Ryder:** Yeah, Seven Billion Humans was that game. It's not quite the same thing, but it's a...

**Jon Calhoun:** It'll get you used to this concept of programming; it's not the same as programming, but it's like an awesome introduction for -- the way I described it was like if I wanted to get my nephews into programming without telling them that's what they're doing, I'd be like "Go play this game." Then afterwards you'd be like "You're basically programming."

**Mat Ryder:** Yeah, you really are. You literally have if statements and things where you give logic into a little character, and they've got to find their way home... And there's not seven billion of them, so the title is a little bit misleading there. I only counted 6.4 billion when I counted them...

**Brad Van UGT:** \[52:09\] \[laughs\]

**Jon Calhoun:** But yeah, that game was even interested in the sense that it -- didn't it even tell you if you had the shortest code possible, or the fastest code possible?

**Mat Ryder:** Yeah, yeah...

**Jon Calhoun:** It did some programming-issue type things that programmers for whatever reason care about these things. Some of them make sense, like latency, or -- speed can matter, but whether your code is the shortest code possible is something that, weirdly, programmers like to check.

**Mat Ryder:** Yeah. I mean, that Seven Billion Humans --

**Brad Van UGT:** Was there like a score and experience attached to that?

**Jon Calhoun:** Yeah, so once you'd finish a level, it would show you whether -- if I recall correctly, it would show you "You were this close to the fastest solution" or "This close to the shortest solution", and sometimes those weren't the same, and sometimes they could be the same... So it sort of forced you to go back and try different ways and sort of see what's possible.

**Mat Ryder:** Yeah, it's really cool, it's really fun. I mean, that's for people who aren't programmers. Anyone can play that, within reason.

**Jon Calhoun:** Yeah, anybody can play that game. It gradually introduces you. As a programmer, you still play -- I still played it some and found it interesting, but it was hard for me to sit down and just play the whole game through is how I'd put it... Because it sometimes did feel like programming, because it was so relatable... \[laughter\]

**Mat Ryder:** Yeah, that's how you're programming in your real life; you've got an IDE that's just little blocks you move around, isn't it? It's adorable

**Brad Van UGT:** Yeah. Everyone at Google is just doing that \[unintelligible 00:53:31.20\]

**Jon Calhoun:** Alright, we're running near the end of the episode, Brad, so we're going to move over to your unpopular opinion.

**Jingle:** \[53:41\] to \[54:00\]

**Jon Calhoun:** So tell us what is your unpopular opinion.

**Brad Van UGT:** I don't know how unpopular this is, but I've started a couple different companies, I've co-founded a couple different companies. Rattlesnake is the one that I'm sort of currently operating, and it's the one I love the most, absolutely... But as I've built teams and tech teams and engineering teams, I've become a huge fan of non-negotiable job offers, especially at an early stage. I've hired a lot of developers over my career, and it just feels way better for both sides of the relationship when job offers are made open and transparent, and everyone's kind of putting their chips on the table right away, of like "I don't want to play this game of negotiating benefits or negotiating salary", and oftentimes developers don't want to do that either. It doesn't even have to be developers, but early-stage tech hires don't want to do that either. So I'm a firm believer that those job offers should be non-negotiable because it just builds so much trust on both sides. I can talk about that further, but that's where I want to start. If you have negotiable job offers, it tends to favour those that understand that they can negotiate...

**Mat Ryder:** That's what I was going to say.

**Brad Van UGT:** ...or those that have the social skills to do so, and not everyone does... And I think that's a real garbage situation, to learn that someone with the same job title as you received a higher comp package just because they asked for it and you didn't. What does that say about the team and the company at a high level?

**Jon Calhoun:** We don't think about it that much, but I could imagine this also affecting people's salaries based on their backgrounds. For instance, somebody who has their parents paying for their college and can afford to turn down a job offer, or try to negotiate with those risks involved... Versus somebody who's like "I just graduated with $100,000 in debt. I can't take the risk of upsetting them by asking for more money." Or that might be what's going through their head.

\[55:58\] In practice, job offers are probably rarely rescinded for trying to negotiate... But there's always that risk, and that could potentially mean that people who are already coming into the work environment with a slight handicap by not having parents who can pay for their school - I say "slight", but that's a pretty big handicap. But if you're coming in with that handicap, it sort of further amplifies it.

**Mat Ryder:** Yeah, and I suppose also -- like, I know from hiring myself that on average, female candidates would ask for about 10% less than men would, for whatever reason... And I suppose it helps like that. By the way, when that happened, I would tell them, because I'm a feminist hero... But I suppose it helps there, does it?

**Brad Van UGT:** Yeah, absolutely. I think of it as -- like, if you're doing non-negotiable job offers, you should be giving your best offer upfront, you know what I mean? You shouldn't be using non-negotiable job offers as a money-saving tactic. I think that's kind of the wrong way to do it. But you should be giving everyone the best offer that you can, regardless of their background, their experience level, if they're under-represented minorities, or whatever; everyone gets your best offer.

And what I also think is interesting is it really puts the onus on the hiring team to perform well and to make sure that we're getting great people through and that we're getting a diverse pipeline. If you can decide on what the comp package is before hiring, then it takes that entirely out of the process. We know what this role is, we know what we're going to pay them, and now we need to find someone who matches that and is looking for that... Versus like "We're just looking for anyone, and we'll pay them the minimum amount they're willing to agree to", which is...

**Mat Ryder:** Right, yeah.

**Jon Calhoun:** I guess it would also eliminate that whole "If we can get this person at this rate, it's a yes, but otherwise it's a no." It kind of gets rid of that whole in-between type state of trying to decide is it worth it or not.

I do like what you said about figuring out the role and what it's worth to you ahead of time. I think that'd be the hard part with the non-negotiable offers - there's a lot of orgs that... Like, a Google for example - when one of those companies are hiring, they aren't hiring for a specific role. So it's a really weird situation. It's not like you go in saying "I'm hiring for sales lead, at this specific project." But if they were forced to come up with actual salary ranges upfront and have non-negotiable offers, I feel like that would be more useful in that sense, because you'd know what you were going in for.

**Brad Van UGT:** Yeah, yeah. And along those lines, if you're doing this, you'd never have to ask -- there's always that question of like "What are your salary expectations?" or "What did you make in your last --", you know what I mean? Employers will always find sneaky ways to ask that question of what you were paid in your current or your previous role... And you always have to train interviewees to navigate that question and be ready for it. And this takes that question entirely out of the process. "This is what the package is. I'm telling you right now, it's our best offer. We think that you'd fit that." And either it's something they're willing to accept or not, but there's no conversation of like "Well, is it a bump over what you used to make? Can we get less because you were undervalued previously?" It takes that off the table as well.

**Mat Ryder:** Has that ever backfired? Have you ever regretted it? Have you ever lost somebody that you wish you hadn't?

**Brad Van UGT:** Yeah, totally. We've lost -- and when I say "we", in previous companies... But I've had strong candidates turn down offers, and I've learned to be very upfront with that early on in the process. If you interview someone you think it's a fit, have that compensation conversation very early with them, to make sure that no one's wasting anyone's time on either side. And if that doesn't align, then move on.

A stronger example of -- I wouldn't say backfiring, because I think that's too tough language, but there was a position that I was hiring for, and we had decided upfront what the comp package was going to be... And we lost 3-4 really great candidates who decided that that wasn't for them. And what we ended up doing is we had to increase the comp package. But what that came with is we actually also increased comp packages of the existing team as well, to match... Of like "Okay, you're all at this role, you're all at this level. We can't hire great people on your current comp package at this level, so clearly, something's wrong. So let's bring everyone up to a level that we can actually hire great people at, and assume that--" You know, we don't want to punish existing team members because they chose the lower salary two years earlier, right? And the market's changed.

**Mat Ryder:** \[01:00:26.18\] Well, they joined earlier.

**Brad Van UGT:** Yeah, exactly, which should be rewarded.

**Mat Ryder:** Yeah, it's the opposite way around. Very interesting. I wonder if that's going to be unpopular or not. I don't know. We will test this on our Twitter account @gotimefm. We'll ask the people and find out what they think. Very interesting though.

**Jon Calhoun:** It's a weird one for me, because I don't know where I stand on it fully. I've seen some companies that -- the one that comes to mind is GitLab. They're remote for the longest time, and they had -- I think it was basically like specific price bans... I don't know if it was exactly this, but they did something where your location was affecting your salary and some other stuff that I didn't fully agree with, and it essentially came down to the point that I could never work there, because I would never get an offer competitive to what I currently had, and what I could currently get. So to me, I'd be looked at "Well, you've basically just eliminated a huge set of potential candidates, because what you're doing isn't competitive for the ones who at least have other offers. So in some ways, it kind of felt like they were taking advantage of the people who wanted some of the perks they offered, but couldn't get that offer somewhere else.

**Brad Van UGT:** Right.

**Jon Calhoun:** Now, the fact that you said that you tried to share this upfront or early on in the process - that helps a lot. In my mind, if the salary is transparent and non-negotiable for the role, it's nice -- I think most people agree that seeing salary ranges upfront is awesome for employees... But that's a rarity, I think.

**Brad Van UGT:** Yeah. There's a couple different takes on it. You can use non-negotiable salaries to save money. It can be used for the wrong reasons, or used -- I don't want to say "used for evil", but... You know what I mean? The motivations can be less than altruistic. And I'm not suggesting that with GitLab that was necessarily the case... But you can use it to be like "Well, we're going to actively underpay people, and we're just going to build a team around people that don't realize they're being undervalued", which can be a side effect if you're doing it wrong.

Another counter-point is most people these days are trained to negotiate, or taught to negotiate, or told to negotiate, so they're ready for that process. And if on face value you say "We don't negotiate salaries. Sorry" - that can come off a bit weird. You have to add the part of like "And we give perfect offers, and we try to be really competitive in the market, and we want to make sure that everyone's at the same level." You have to add those additional points, otherwise it gets dangerous.

**Jon Calhoun:** I could definitely see it being -- it's almost like you go to a used car lot, and they're like "We don't negotiate prices. These are the best prices we can offer", but then you find out later that if you're trading in a car, they'll negotiate that price though. So you do technically negotiate prices, you just do it differently.

**Brad Van UGT:** Yeah. Some people won't negotiate cash, but they'll negotiate options, or they'll negotiate vacation time... Like, you can't have some of it; you must be all-in, right?

**Jon Calhoun:** Yeah, I think that would be a huge thing, is that you have to commit to "This is what's fair, and we're going to be upfront and honest" otherwise it would be very frustrating as an employee down the road.

**Mat Ryder:** What I like about it is that it really does help those that aren't confident going into doing negotiations. Honestly, that isn't part of our job, really, so in a way it shouldn't be a requirement of getting well-compensated. I happen to be alright \[unintelligible 01:03:39.14\] Jon, can I have $2,000, please? Can I?

**Jon Calhoun:** \[laughs\] No, Mat. You cannot.

**Mat Ryder:** It doesn't always work,

**Jon Calhoun:** Not for me.

**Brad Van UGT:** Where do I wire it? Just let me know... \[laughter\] It worked on me, you're good.

**Mat Ryder:** \[01:03:55.21\] Yeah, thank you. I'd love to see your interview process... Do you go in and say like "Right, have a game of Snake on a whiteboard." \[laughter\]

**Brad Van UGT:** "What's the best move? You have 20 minutes." "How do you do look-ahead in real-time?"

**Mat Ryder:** Yeah, that's actually good questions, to be fair.

**Brad Van UGT:** I mean, we're a small team. We're only three full-time people. I think we're now going to go to four full-time people in a little bit. But we're very small in doing this, and we're very lucky and very fortunate to be able to do it... And we're supported by some perfect partners that let us do that. So we haven't had to do strong interviewing yet, but I think that's an interesting -- there's an interesting advantage here where our community, our users are all developers, and they're all very familiar with it. And they've seen the rules, they've played around with -- you know what I mean? They're very familiar coming in, so... I'd like to think we can hire from the community pretty well.

**Mat Ryder:** Yeah, I find that to be one of the greatest things about open source, is the people you meet doing it. I do often recommend to young developers or people that are new to development to get into some open source project, if you can, in some way. The opportunities are amazing. And you're right, if you're looking for somebody to hire, if you've already been working with them for a while, it becomes a very easy decision to make. Brilliant.

**Jon Calhoun:** As a new developer, getting into any company that has developer-facing tools of any sort is -- one of the suggestions I've given is to try to use those tools... As an example, back when Stripe was earlier on, if you wanted to get involved with Stripe you might have used their API clients and basically provided feedback of like "This was my experience. Here are the things that did well or didn't do well", and I think if you get into an interview process, that's going to make yourself a lot more attractive, rather that somebody who's like "Oh, I've never even touched your API, but I wanna work there." That's kind of a hard thing to believe right now.

Now, granted, that also means you have to have the time to do it, which is unfortunate, but I think that's better than the whole blanket send your resume to 100 people versus send it to like four or five that you give yourself the best changes possible with them.

**Mat Ryder:** I think it's worth considering.

**Brad Van UGT:** I think those are functions of scale, right? If your early Stripe and you have to move fast, and you have to move quick, then there's clear advantages to bringing on someone who knows what they're doing. But if you're current/present-day Stripe, a) your hiring requirements are super-high, obviously, but also, you want to make sure that you're bringing in a very broad spectrum of experiences and technologies, because you're just operating at such scale. So I think that changes over time, and I think that's okay for that to shift over the lifetime of a company, or an engineering team, specifically.

**Jon Calhoun:** I was more viewing it as like the individual applying's perspective. I've seen some people that just literally blanket send the resume to every company they can, and then they wonder why they don't hear back... And it's like, I would rather sit down and spend a week of like "Here are the five companies I'm applying to this week. How do I make myself have the best chances possible?" But that's just my perspective; I haven't done the whole "New junior developer trying to get a job" thing. I only had to do that once, and I got lucky, so it's hard to give advice on that front.

**Mat Ryder:** Another good Netflix show - dress Jon up like a schoolboy, with a little cap on, and shorts...

**Jon Calhoun:** I'm not sure what you're imagining...

**Brad Van UGT:** Undercover Junior?

**Mat Ryder:** Yes, exactly. \[unintelligible 01:07:14.04\]

**Jon Calhoun:** I've got like a schoolboy uniform, and I'm going to job interviews, and I'm just wondering where I'm working?

**Mat Ryder:** A little catapult you've got, walking around... You know... Chewing gum... \[laughter\] I mean, come on, it writes itself.

**Brad Van UGT:** I would watch it. I would watch that twice.

**Mat Ryder:** Yeah.

**Jon Calhoun:** Alright... Brad, thank you for joining us. It's great to have you and great to hear about Rattlesnake. Anybody who wants to check it out, it's at Battlesnake.com. Is that correct?

**Brad Van UGT:** Yeah, it's play.battlesnake.com. We're just opening up our summer competitive league. Pre-registration just opened up yesterday, so if you want to get involved, you've got a few years to get your snake ready... And then competitive play for the summer league will start in June.

**Mat Ryder:** Brilliant. I'm going to be watching this.

**Jon Calhoun:** Awesome. Thank you for joining us.
