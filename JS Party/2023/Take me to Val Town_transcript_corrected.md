**Jerold Santo:** Hello, hello to the internet, to all of our awesome JS Party listeners. I am your friend, Jerold, and I am joined today by my friend, Amal. What is going on, Amal?

**Amal Hussein:** Hi, everyone. So excited about today's show. I think I say that every time, but still, very excited.

**Jerold Santo:** You do. You're keeping the streak alive. I'm waiting for the moment when we come out, and you're "I just don't want to be here, and I am not excited, and I can't wait for this show to be over." That'll be a day...

**Amal Hussein:** That'll be the day...

**Jerold Santo:** I'm excited too, because we're here to take you not to Funky town, but to Val Town, and we're joined by Val creator, Steve. His friends call him Stevie. We're going to call him Steve for the first half of the show, and hopefully we'll get to Stevie by the end. What's up, Steve? Welcome.

**Steve Grouse:** Thanks. I'm doing well. We'll see how it goes. Stevie's for my close friends, but maybe. We'll see.

**Jerold Santo:** Okay. We'll set up some kind of code word or something that you can say to consent to the Stevie, and then we'll switch when we hear it. But for now, Steve, welcome. Val Town... Gosh, it looks a really cool thing. It's one of these ideas where I just landed on the website, and it just immediately connected with me, so much so that I covered it in our Changelog News, podcast and newsletter. Because right when you land, it says "If GitHub gists could run, and AWS Lambda were fun." And I just realized, after saying it aloud, it also rhymes, so bonus points for having a good tagline that rhymes... And as we all know if something rhymes it has to be true. I've heard that somewhere once. So this connected with me.

**Amal Hussein:** I think I've been saying your tagline wrong, because in my head I've been reading it as "and if AWS Lambdas were fun..." So can we settle it here? Is Lambda already plural, or ...? Because yeah, there is no s here.

**Jerold Santo:** That's true.

**Steve Grouse:** Yeah. I think about it without an S... But yeah, you're right, we made gists plural, so... It's a good point. Good copy editor.

**Amal Hussein:** Okay, excellent. Yay.

**Jerold Santo:** Well, there we go. We already fixed something, a controversy here - is it Lambda or Lambdas? Most of mine are Lamb Don't, because I was so annoyed by the platform when I tried it - this was early days - that I just kind of went back to my old school way of doing things. And yet here we are, with a great concept... So share it, Steve. The overall concept. Of course, we did the tagline, but why don't you give it more words, flesh it out? What are you trying to do with Val Town?

**Steve Grouse:** Yeah. So Val Town is a social website where you can write, run, deploy, share, schedule code, and we try to make simple things easy, and more complicated things possible. And we're starting with use cases that are around light computation, maybe integrations, prototypes of APIs, and we want to make that perfect and fun and quick to do. But the dream, the long-term dream is to scale up to be a full backend kind of replacement... But we hope to get there over time.

**Jerold Santo:** Where did this idea come from?

**Steve Grouse:** Well, I guess pieces of this idea I've been working on for years. I've been a big developer tools fan for many years. But this company really was instigated by this investor that I became friendly with. He invested in a lot of other dev tools companies, and I had just worked on a dev tools project that was trying to be a company, but it didn't work out, and I was asking him for ideas, and he had one. And yeah, his original pitch for Val Town was "Isn't it sad that there's dead code on the internet? Just code in just -- syntax-highlighted code, just in a blog, API documentation on Stack Overflow, and it just doesn't run if I copy and paste it somewhere, and then you have to install stuff... It's just, the loss of composability because there's dead code on the internet, just it's this -- it's a bigger tragedy than you might think; at least that's what we believe.

**Jerold Santo:** Why is it so tragic? What's such a tragedy about it? Copy/Paste is easy...

**Steve Grouse:** So where are you copying and pasting it there? A recent example of this - maybe you've seen this kind of memes of someone texting their developer friend "Oh, ChatGPT is writing me all this code. Your job is done." And then a couple seconds later the friend texts him, "But wait, where do I put this code?"

**Jerold Santo:** Right.

**Steve Grouse:** So I think particularly for beginner programmers, where do you put the code? How do you get the code to run? How do you get your development environment set up? A lot of the questions that Replit solves really well, or even Code Sandbox, or JS Fiddle, Val Town also is kind of going at that slice of the problem. Just load a URL, and then you're going. You don't have to figure out the environment, as well as the code.

**Amal Hussein:** Yeah, I appreciate that analogy a lot. There's a great quote on your website from someone who was complimenting Val Town that said "It's a practical middle option for not going too "enterprise" (lambda), or too consumer (Zapier)." Or Zapier, I've never been able to, I don't know --

**Jerold Santo:** I don't know either.

**Amal Hussein:** Yeah, this is another --

**Jerold Santo:** Pick one and stick with it.

**Amal Hussein:** \[06:17\] Babble/Babel... Yeah, so many debates on this. But can you -- I love that analogy of something in between AWS Lambda and Zapier. So could you kind of just walk us through the landscape of core problems Val Town sets out to solve, besides just code execution? ...which you said that you can do on Code Sandbox, or Replit...

**Steve Grouse:** Yeah, so Val Town - it's server-side compute. Some people like to think of us as CodePen for the backend, or JS Fiddle for the backend. So in that way, we're a lot like Replit, but we're a lot smaller, more composable snippets. So in that way, Twitter has been a big inspiration for us; each Val is like a tweet-size thing. And then they compose up really well, in the same way that you would make a tweet thread. Instead of one big tweet, it's like a tweet thread, and then each tweet can be individually liked, commented, retweeted. So vans can all be individually versioned, referenced, imported, commented on... We just added comments; you can comment on other people's vans.

But anyway, so in terms of that landscape of -- like, on the one hand you have AWS Lambda, which is totally scalable, but really hard to use, and on the other hand you have Zapier, which is just no code, Val Town sits in the middle in this weird way, particularly for programmers. If you're a programmer, and your natural way of thinking about automation is in code, I think Val Town is kind of designed for you.

A couple of years ago, before this company, I tweeted about -- tweets are cool, they have timestamps. I tweeted "Wouldn't it be cool if there was something Zapier, but it felt more like a programming language?" And I think at the time the thing I was really focused on was getting all of your keys -- like, the main value in Zapier is that you press a button, and you can OAuth flow, authorize your Gmail account, and you can send emails from your Zapier, or just any service, you can just press a button and then the keys are injected into Zapier, and now you can do more things with that. So at the time, I was focused on that in a programming environment. And we have vague notions of that in Val Town; we haven't built it yet. It just hasn't been the bottleneck, it seems. If you're someone who's writing code anyway, like clicking a couple buttons, like copy a developer token into your app, into your Val Town keys isn't the main thing... The main thing that Val Town is good at is bringing everything to your fingertips; at least that's how some of our users describe it and I like to think about it. You can write a bunch of utility functions for yourself; other Val Town users are writing utility functions. And then whenever you want to do a thing, like, the first thing you should do is kind of search and see if someone else in Val Town has already done that thing.

I was playing with the Discord API today, and instead of parsing through the documentation, I just searched for the word "discord", and someone else had already made that API call that I wanted to do. So the thing about Val Town is that I can use that code, and I can be sure that it's going to work, because it already has worked in the Val Town environment. That's the magic of everyone shares the same runtime.

**Jerold Santo:** Right.

**Amal Hussein:** And you just said a really important keyword there, which I think is the secret sauce to all this, is being able to actually have a controlled environment and execution context. And so unlike things that are limited to just client-side, like Code Sandbox, or old school JS Fiddle, or whatever - these are kind of just running in the browser - you're able to kind of leverage storage of variables, and you can kind of keep state, you can also carry state throughout different executions. Can you talk a little bit about that?

**Steve Grouse:** Yeah, persistence is definitely something that we are good at. We're regretting some of the choices we've made, and we're looking to make them -- I'll tell you about what it looks now. So what it looks now is Val Town - from one Val, you can reference another Val state. So the way that works is if I'm in a Val foo, and I want to reference the value of another Val bar, I could just do @, and then the username... Steakhouse is my username, or @me to just reference my username, dot bar. And then it would reference bar. So the idea there is import's as easy as tagging on Twitter.

\[10:23\] But then if you wanted to update bar, what we have is you could just update the variable from foo, and the update will just persist to bar. So you could do @me.bar++. And if it was a number, it'll just be one bigger than it was before. And vans all have independent version history. So it just puts a new version of bar, that's a number one bigger.

**Jerold Santo:** One thing you said at the beginning there, Steve, was that it's more about where you run it, because we have all this code we talk about the copy and paste thing and the dead code on the internet... And I think that's really powerful, not just for beginners, because I definitely think that mindset... I used to teach coding boot camp-style web development 101, and getting people set up and running, and troubleshooting environments was such a time suck for that. And that was full stack, it wasn't merely in the browser, frontend. So Val Town and other options like it are just a boon for teaching people and getting people started. Most of them, like we've been talking about, are frontend oriented, whereas this is more of a full-stack serverless option.

In a way it's really cool, because on the website you have some use cases right there on the homepage that even though it's great for beginners actually speak to longtime developers as well, because there are certain things that we have to do, and it's easy to code those things up, but then the question was always like "Well, where is this going to run?" And then we all have our solutions, like "Well, maybe it is on Lambda, because I already am an AWS expert, and I can just get that thing going." Maybe I have a VPS that runs Linux, and I put all my random crap on there... Maybe I have a few strewn about; you know, home network, home lab... All these places. I have some cron jobs that run on my laptop. It's not a server, but it runs most of the time, and so I just cron job on my laptop, and I let it run things. But then we ask ourselves, "Well, how do I email myself? What's the easiest way to get myself a notification?" And I've been doing this lately, looking at like "Well, how do I push-notify myself reliably, from anywhere in the world, on a script?" Just like pipe it into something that sends it to a thing, versus me having to do a bunch of other things to get something done. Just like simply set up something small that scratches a particular itch.

And you have cron jobs, you have email yourself... So you have scheduled, you have notifications built-in... And for me, as an experienced developer even, when I think about where, it's just like "Well, you just throw it on Val Town." I have an account there, throw it on Val Town, and let it email me. Schedule it with Iron. And so I like that that focus is there from the beginning, where it seems attractive not just to people trying to get started, but also people just sick of having to manage where their code runs all the time. So I have a bunch of stuff that I could easily port, being its JavaScript and TypeScript... I could just create a Val Town account and start moving stuff up there, and not worry about "Did that crontab run because my laptop is closed?"

**Steve Grouse:** Yeah, exactly. The early vision is we want to slurp up all the things you have scattered on random DigitalOcean droplets, or servers you've been managing yourself, and manage those for you in a more centralized place. But the long-term thing is just thought about all the people and use cases that don't get built because it's just too cumbersome to set that up, and they don't already have a running server that runs their cron jobs... Or they're not on their laptops, and they can't set it up. So many of the vans I write are on my phone, in bed, or just on a train, or whatever.

**Jerold Santo:** You code on your phone, in bed?

**Amal Hussein:** Oh, God... Oh, boy...

**Steve Grouse:** \[13:58\] Oh, yeah. My first hour of work this morning --

**Jerold Santo:** Let's stop here and enjoy for a moment...

**Steve Grouse:** Yeah, so a user I saw on Discord was having trouble getting -- okay, so we just released a new version of the Val Town API, that lets you search vans, and just kind of do more things you'd want to do with Val Town from the API. And so they piped our OpenAI spec through a generator of an API client, with all the TypeScript types and everything, and they have it on GitHub.

So you can actually import GitHub clients, or whatever, GitHub code, right from GitHub. You don't have to publish it to NPM before you can use it in Val Town, because we do it through ESM imports. So anyway, I was showing them how to do it, all for my phone. I don't know, it took 20 minutes. And at the end of it I just copied the link to the Val, put it in the Discord, and they were off forking it and playing with it themselves.

**Amal Hussein:** Wow. And just to be clear, you were showing them how to import code that's publicly available on GitHub...

**Steve Grouse:** Their code.

**Amal Hussein:** Oh, their code.

**Steve Grouse:** Yeah. So they made a GitHub package that's like an API client for Val Town, that they were going to use to build a Ray cast extension for Val Town. And I was like "Oh, well, it'd be awesome to use this within Val Town, to interact with the Val Town API from within Val Town." So a reason why that's going to be cool is there's no way -- so there are a lot of events on Val Town that you might want to get notified about. Like, if your Val threw an error when it ran, anytime - it ran via the API, it ran via a cron job and it threw an error. Or someone liked your Val, or if someone referenced your Val. There are all sorts of things you want to get notified about. And so our current plan - it sounds maybe a little pie in the sky, and it might be, but our current plan is to build all of those notifications in user space. So there'll just be a Val that I write for myself, that will pull for all these resources that I might care to be notified about, and if there are changes, it'll email me via console. Email, like you were talking about. Val Town makes it so easy to email yourself. And then there could be a bit of a marketplace on Val Town of this custom notification, filtering, throttling, debouncing functions. It's all fully programmatic and customizable. Anyway, it's an experimental idea that we're excited about... So that's why I wanted to get the API client running on Val Town, from GitHub.

**Jerold Santo:** Right. So at the end of this little snippet that you put from your phone, did you have a comment that said "Sent from my phone"? ...like, in your sig. Did you put that in your sig? \[laughter\] Yeah, "Please disregard any typos. Sent from my phone."

**Steve Grouse:** Yeah. Well, I guess when you're on Val Town, on your phone, and you hit Run, we could save that metadata somewhere, like "This Val was run from a phone..." \[laughs\]

**Jerold Santo:** It's kind of like the old Twitter client metadata, where it's like "From Tweet bot", back in the good old days.

**Amal Hussein:** Yeah. I feel like I need that line for anything I type which I haven't re-read. It'd be like, "I have not reread this, so if this sounds weird... Just FYI..." \[laughs\]

**Jerold Santo:** Yeah. "If this executes improperly, it was not TDD-ed. Just a disclaimer. I did not test this."

**Amal Hussein:** That's right. That's funny.

**Jerold Santo:** That's cool. Well, okay, so coding from your phone, coding as a beginner, or a person who just is sick of managing things. The where is really important, but the question that comes to my mind when I look at a platform this, which looks nice and free, it has a Pro plan, and blah, blah, blah, is like "Well, where is my code then? Where is Val Town? What's the address? What's the geocoordinates of our town? Where does my code actually go?"

**Steve Grouse:** Ohio. It goes to Ohio.

**Jerold Santo:** Ohio. Okay, cool.

**Steve Grouse:** Yeah. Everything right now is deployed on Render in their Ohio region.

**Amal Hussein:** Oh, so you weren't kidding. \[laughs\]

**Jerold Santo:** He was kidding and serious at the same time. The best kind of kidding.

**Steve Grouse:** Yeah.

**Amal Hussein:** Did you pick Ohio because it's like middle country?

**Steve Grouse:** \[17:58\] Exactly. Exactly. Yeah, it seemed like the middle of America, it seems solid. We do have a lot of users in China who probably hate our latency times... But it's fine for now. Most of Val Town can really scale horizontally, and go to the edge when we have enough money to hire a team to do the whole edge thing. We're trying to architect with that in mind. But for now, Ohio is fine.

**Jerold Santo:** Ohio. Is it just stored in a database, like as a string, or a text area? Get into some of the architecture. Where actually is it?

**Steve Grouse:** Yeah, sure. So I guess starting from the bottom of the backend, everything's stored in a Postgres database. So all your code for your vans, your output for your vans... And this is why we recently added a 100-kilobyte limit to what you can store in a Val, 250 kilobytes for the Pro Plan, because we just can't be abusing Postgres with more than that in the JSON columns... But we'll probably soon move to an R2 blob storage for all the things that should be stored in R2, and not Postgres. I guess one step above that would be our execution environment is Demo, and we manage our own Demo servers that execute user code in a sandboxed, isolated kind of way.

And we would kind of love to use another hosted service for that, Cloudflare workers or AWS Lambda, or really any of them. We would love to not have to manage a function as a service platform. The reason we have been forced to is that we have this weird requirement where Val Town is as much a deployment platform as it is an IDE. So if you hit Run or hit Save, your Val needs to run as fast as it would in a deployment. Your Val needs to run in 50 milliseconds, because that's what you'd expect from an IDE. But most of these function as a service platforms have a couple of seconds of latency to deploy your code, because they're not focused on someone doing rapid iteration, they're focused on "You've deployed it, and now it's going to run for forever."

So it anyway, maybe one of the functions as a service platform is listening to this and will consider taking pity on us, and making a better latency deployment thing. But in the meantime, we're doing our deployments ourselves on Demo. And then in the middle we have an API server that's just a Node server, and at the frontend it's a Remix/React server. And all four of those services are hosted on Render.

**Amal Hussein:** Interesting. I'm just curious, why are they coupled? Specifically, like, I'm going to run it locally, versus deploying it. I'm just curious why those two things are coupled at all. Like, when you hit Save, can there be a Save as Draft, versus save and deploy?

**Steve Grouse:** Well, so when you're developing and Val Town, normally -- so you can be doing one of two things. You can be writing a function, which is just - yeah, saving a function, which can happen pretty quickly. But then if you're running arbitrary JavaScript to test out the functions you've written, that's a thing you would do on Val Town that most functions as a service platforms don't have. And you're not testing out your lambda function from another lambda function; you use Postman, or something that. But on Val Town you have -- Val Town's a bit of a REPL environment, and so we need that code to deploy instantly, because it's a REPL.

**Amal Hussein:** Yeah, that makes sense. So kind of just shifting into maybe the architecture of a Val... So what languages can you use to write these little code snippets? And I'm curious also, do you plan to support different types of runtimes in the future?

**Steve Grouse:** So for the medium term it's just going to be JavaScript and TypeScript, and everyone's going to be on the same version of Demo. In the slightly longer term, we might allow different JavaScript runtimes, like different versions of Demo, or maybe Node, or Bun, like different JavaScript runtimes, and you could specify that at the Val level. And then in the longer term, we might allow other programming languages. But for now, a lot of the benefits of having everything in that lingua franca environment that we were talking about - those benefits are so great that we want to keep that for as long as possible. And to be honest, it's just so much less of a developer complexity for us to maintain just the one environment... So we're gonna stick with that for a long time.

**Amal Hussein:** \[22:16\] Yeah, JavaScript is the universal solvent, so I get that. Good choice. I think one of the things that really got me excited about this was seeing that one of the vans available was "Do you have a form that you need to add to your website?" Can you talk us through how that works, and just being able to kind of leverage a Val to take data that someone's typing onto your static site, and then having that go somewhere?

**Steve Grouse:** Yeah, Val Town is a really great pairing for a static site like Astro, or any of the static site generators... So you can do the whole thing 100% in Val Town, so Val Town server-side compute, but you can return HTML from a server. And now we're doing frontend things... So I think the way the Astro Like button -- there was a blog post someone wrote, I think the way he did it was, he just had one route, kind of basic get route, he made a Val that was an express handler Val. So there are a couple different types of vans. You could just write a function, just a JavaScript function, or you can write an Express.js handler that takes a request object and a response object and returns a response. So if it's a get request, it'll return a Like button component, and the number of likes, just as an HTML string that it'll construct in the Val. And if it's a POST request that's hitting this Express handler, then it'll add one to the count, like we were talking about before. Because you can persist data in Val Town. And that's it. It's really just six lines; the core concepts are just six lines. You can do more complicated things. I think he was doing fingerprinting to make sure that you can only hit the Like button a certain number of times, because it'll try and fingerprint your browser...

**Jerold Santo:** So where's the BTC miner Val? That's my question.

**Steve Grouse:** Yeah, that is funny. We haven't seen any abuse really in Val Town. We've had a couple of people try --

**Jerold Santo:** Oh, just wait.

**Steve Grouse:** I know, I know. It'll happen. It'll happen. Hopefully, it'll happen when we have the resources to deal with it. That would be nice.

**Jerold Santo:** Yeah. Totally.

**Steve Grouse:** We should put a notice up on our website, "Hackers, just wait until we raise our next round of funding before you--"

**Jerold Santo:** \[laughs\] "We'll really be able to support this operation when we'll have more money." Any public platform deals with abuse, and if you haven't yet, success will just bring that. And so yeah, hopefully it aligns with a time when you're fleshed out as a business enough to be able to deal with it as it comes up, because it certainly will. I can't remember who we were talking to most recently about that on the show, but we were talking about even GitHub's Actions, and how much GitHub Actions is actually just -- they're fighting it off, constantly. And it's just like, whenever you provide free public compute, at any scale, they'll scale it horizontally across your free plans in order to get it done. But in the good days right now, thankfully you don't worry about it right now, and hopefully they won't find you for a long time.

**Break**: \[25:25\]

**Jerold Santo:** You mentioned Dan Levine from Acts as being kind of the kickstarter to this idea, and you building it. I also was looking at your list of people involved, the team, and I noticed Ross Boucher - I'm not sure how his last name is pronounced - as an advisor. And Ross - I remember Ross from way back in the Cappuccino days. I'm actually a Cappuccino user from the outs.

**Steve Grouse:** Wow...!

**Jerold Santo:** So I was a big 280 North fan, from Francisco Tomsk, Ross and the third founder - I'm gapping it now; I've had him on the Changelog.

*Jerold here in post. Tom Robinson is his name. Sorry about that, Tom.*

**Jerold Santo:** So I apologize for gapping that... But yeah, Ross - immediately I was like "That name sounds familiar." He's also doing Run Kit, right? So Run Kit's a thing. I don't know much about Run Kit. I know it's popular amongst some. And he's an advisor, so it seems like Run Kit and Val Town have a lot of crossovers. Has he been instrumental in the design? He probably knows how to do a lot of these things, maybe even fighting fraud and abuse.

**Steve Grouse:** Yeah. So yeah, Run Kit was one of the main inspirations of Val Town, I would say. Yeah, Run Kit's a really cool platform. It's still embedded in NPM. So if you want to try any NPM package out, Run Kit is just right there, embedded, which is awesome. And Ross is great. He also is at least partially responsible for the early Stripe API...

**Jerold Santo:** Oh, yeah, yeah.

**Steve Grouse:** And making that so beloved by everybody. So he's --

**Jerold Santo:** Yeah, a talented guy.

**Steve Grouse:** Yeah, he's really wonderful at building developer products, and it's awesome that I get to chat with him all the time and get his advice on things. Dan introduced us. And he became -- I don't know how they became friends. Oh, actually, Dan's wife, Christina, was very early at Stripe, so that's probably how they all got to know each other.

**Jerold Santo:** Gotcha. Well, it sounds like you have some smart people behind what you're up to, which is always a vote of confidence. Let's talk about the business side of things, because anytime you're going to adopt any sort of platform, you're thinking, "Will this exist in three years?"

**Steve Grouse:** Yeah.

**Jerold Santo:** And especially if I'm going to put my code there. Now, thankfully, it's probably relatively portable, as long as I have small functions, and they're vanilla JS or TS for the most part. Obviously, there'll be some Val-specific APIs that I'm calling in there... But probably portable, as just a risk assessment from an adopter's standpoint. But what about from a business standpoint? I'd mentioned there's a pricing plan... What's the business going to look like? Where does the pricing plan come in? When do I start paying as a user, and then how are you going to actually keep Val Town around and not have to close down the tap, not turn it into a ghost town?

**Steve Grouse:** Yeah. Great, great questions. Yeah, I first wanted to address the point about developer lock-in and risk, because I'm definitely the first to be risk-averse when it comes to adopting new technologies. I got an email from someone who was trying to get me to be the first customer of their developer tool, and I was like "No, I'm sorry. It's too early. I don't want to be the first customer." And he was like "Isn't that a little..."

**Jerold Santo:** Hypocritical? \[laughter\]

**Steve Grouse:** Yeah. Like, isn't Val Town a new developer tool? How do you expect people to adopt it? And my answer is -- like, that's why we're so specifically going after hobbyists and amateur use cases right now. There are a couple of businesses, or maybe a bunch of businesses who are using Val Town, but they're bringing their fun hobby thing to work, and they're not expecting more than that because of how we're doing the branding. And sooner rather than later I think it'll become a mature platform, and it'll be more obvious that you'll want to use it at work.

\[30:15\] But anyway, we're trying to slow-roll that for this very reason, if you're only using it for kind of small things that you don't care about too much to begin with. Like we were saying before, one of the exciting things about Val Town are the things that wouldn't have gotten built before, because they were just too hard to get built, now will actually exist in the world, because they're so easy, and you could just do them on your phone as a hobby thing. So yeah, that's what we want to win to start, and build trust over time.

But anyway, back to your point about lock-in. I think we have 8 or 12 Val Town-specific things that you're going to have to replace if you want your code to run without changing any of the code... And we are working on knocking each of those down one by one, so that Val Town is fully a web standard-compliant platform, and really there's just like one or two or zero of these things, to get your Val Town code to run anywhere that JavaScript runs. Node, Demo, Bun, whatever. Well, not anywhere-anywhere. I don't know if you can get it running on every different deployed runtime, but at least locally on any of these platforms with very minimal tweaking. So that's an ongoing project.

**Amal Hussein:** That's really cool, yeah. You've got some domain-specific things, like you've mentioned; these are APIs that are specific to Val Town. They're invisible, because obviously, it's all in the execution context, so everything's preloaded... So things just work if I type @blahblahblah.

**Steve Grouse:** Yeah.

**Amal Hussein:** But I think a potential out for you all could be also just giving people access to the polyfills, or whatever... So maybe it's like an export out of Val Town, where it's like "Here --" In Val Town it's 50 lines, outside of Val Town maybe it's 120, or something. But you can give people an out that way, so you don't have to pollute the API for a use case that you're not as invested in. So just some free advice... \[laughs\]

**Steve Grouse:** Yeah. I think that's kind of the intermediate plan. Where we're heading --

**Jerold Santo:** It gets harder and harder the more you guys do.

**Steve Grouse:** We think that web standards are just the answer. So for example, the @ symbol, like you were referencing - it's so great, but it's a little bit too much magic, and then it's our own thing, and it's really complicated and costly to maintain... So the current plan is that in the future you'll type @stevekrouse.foo, like you normally do now, but then when you go to accept this completion, it doesn't actually accept it that way. It'll just complete to foo, and then it'll add at the top of your file and import, foo from, and then in quotes, VT/steakhouse/foo.

**Amal Hussein:** Yeah.

**Steve Grouse:** And so we'll get the best of both worlds. The import store will be totally web standard; you can copy and paste that code, it'll work everywhere. There's no @ symbol anymore, which is an invalid JavaScript identifier... But in terms of the developer experience, it would be just as fluid as it was before. So hopefully, it'll be the best of both worlds. That's the current plan.

But we're actually using your idea of a polyfill kind of transpiration method. It will be like the halfway house. So the old style of Val Town will work with new Val Town style of code through transpiration. So hopefully, it'll just take a couple of months to work through these non-web-standard decisions that I made a year ago, that I want to unwind.

**Amal Hussein:** Yeah, and thank you so much for sharing that insight and your thought process, and kind of where you are on the decision tree. I think one of the things when you're designing an API for public consumption, every decision, small or big, you're kind of stuck with it once it's out in the universe, and it's really hard... And so I would advise you, don't feel rushed to make this decision. Take your time. Because once you release it, it's out there. So just don't let the community pressure you into having an answer for that right away. But I will say, there's kind of two halves of this. There's the actually getting your code, or your "Val" to run, but there's also data. So to use your example from earlier - so Astro has a Like button that they've kind of got hooked up and working through a Val... And so those like counts - I would want to kind of be able to export that.

**Jerold Santo:** \[34:20\] Sure.

**Amal Hussein:** So I'd want to know, "Hey, when was the last time that this was working?" So let's say you went down... It'll be like "Did I just lose three days' worth of data?" If I wanted to move it to a different service... So are you letting people just export their data? Is there somewhere they can query and get that JSON? Or are you going to use Cloudflare's R2 for that? I'm just curious, what's the plan there?

**Steve Grouse:** Yeah. So similarly, we want to move away from our magic persistence to a straightforward key-value store that will be replaceable by any key-value store.

**Amal Hussein:** Got it.

**Steve Grouse:** We're really taking our time with that API, because there's no web standard key-value store really. Like, do we just use Regis? That's really complicated. Do we do something very simple? Anyway, we're thinking through what that API will be. But we want it to be so simple that you can choose your own -- while you're still using Val Town, swap out your data store for something else. Or if Val Town goes away, you can use whatever you want. We don't want to lock you into any Val Town magic with the key-value store.

Yeah, right now vans persistence - it's just another Val. That's kind of the idea behind the name Val Town; everything in Val Town's a Val. Functions are vans, express handlers are vans, JSON data is a Val... They're all values. Because JavaScript has first-class functions, first-class data. So it's easy to get stuff out, get stuff in...

**Amal Hussein:** Nice.

**Jerold Santo:** Well, I'm not going to tell you to reuse the local store's API... I certainly wouldn't do that. \[laughter\]

**Steve Grouse:** Yeah. It's an idea we considered. It's nice to have something you can point to. Like, "This is a web standard."

**Amal Hussein:** Yeah, but it's a dying one. But on the flip side of that, Index DB is not exactly a great API either, right? There are entire libraries created to just say "This is really painful to work with without a library", you know.

So you kind of beat me to the punch, I was going to ask you about what is the name? What is in that name, Val? It's so funny, once upon a time, baby Amal used to -- all her functions would... Like, I would use the variable name Reval, for like "return value." That was my go-to name for if I needed to just come up with something...

**Jerold Santo:** You couldn't think of a better one?

**Amal Hussein:** Exactly. On the spot, I'm like "Reval". So that was it.

**Jerold Santo:** I just call mine "data". Bar=data. I'm like "This is the data that we're dealing with here."

**Amal Hussein:** I love it.

**Jerold Santo:** That's pretty precise, isn't it?

**Amal Hussein:** Yeah, I love that. Super-precise. But yeah, that's cool. So Val... And so can we talk about the community aspect here? So there's this whole "Sharing is caring" kind of mantra in Val Town, like you said. You want the first thing anyone does - you know, before they create a Val - is to make sure that there isn't one that already exists, that does the thing that they want... And so can you talk a little bit about just what that journey's been like for you, kind of creating kind of a town square for vans? Because the discoverability of it, and that whole thing... What's that been like? I'm sure there are a lot of organic elements, but I'm just curious, for the stuff that isn't organic, how does your team help put that together?

**Steve Grouse:** Yeah. So a lot of our community happens in Discord, which - I didn't make the Discord. This is my second developer community. The first one was the Future of Coding, which started out as a podcast that I made just to talk about developer tools kind of things. And then a Slack community kind of sprung up around my podcast, which was very fun. And that's still going on without me.

\[37:58\] This Discord community is going well. I don't know how many people are in it now. Whenever you message everyone in Discord, it just says "This will message over 500 people." So there are over 500 people. It's pretty chatty. We have four or five people who are kind of in there every day, asking questions, coming up with ideas... Those are my friends. Well, I didn't know them before now, but I like them a lot. It's fun to have some really passionate users always pushing the edges of things. And there's a lot that happens in Discord that I would overtime to push into the product. So we added comments on every Val, so anyone can comment on a Val.

The behaviour now is you make a cool Val, you copy and paste it into the Discord, and then people will comment on it on Discord. But we want to push that into the platform. You can like vans, and we have a trending filter, so you can just browse trending vans, like a front page of Val Town... But it's a little bit buried. And there's sometimes interesting things there.

**Amal Hussein:** So you guys don't have categories, for example, or tags, or... How does one discover a Val? How do I even just browse vans by type, or whatever else?

**Jerold Santo:** All the social networking features?

**Steve Grouse:** Yeah, exactly. Yeah, right now you can just search vans for exact text match. It's like a Postgres LIKE query. That's as good as we've got for searching. We've been resisting going to Elasticsearch, just to reduce the complexity of things... But yeah, maybe tags are in my future. I've built tagging systems before, maybe I will again...

**Jerold Santo:** Yeah. It's a feature that doesn't take long to develop, but it takes a long time to dispose of later... Because you're like "Oh, I can't believe I built this again... And here I am, with tags, six years later", and they're just a mess. And you're like "Why did I ever do that?"

**Steve Grouse:** Maybe this is an application for AI... We don't actually build tags, but we ask our AIs to tag things for us, or... I don't know.

**Amal Hussein:** Yeah. Or you just have a model that's trained on all the new vans, and incoming vans, and then someone just talks to a chatbot. That's the search of the future, right? It's like "I want to do this kind of thing", and then the AI would be like "Alright, well, we don't have anything that does exactly this, but if you combine these three vans, you can do it." Or "Here. Here's one Val, and then you just modify it." That could be a very useful way of handling them.

**Steve Grouse:** Totally. I think that's really the programming of the future, getting to use -- so it's not only like will AI be writing code for you, but it won't actually be rewriting everything... It'll pull runnable bits of code from other people that have been verified. So that's part of what Val Town is doing. When I make a little helper utility Val, it's like a mini NPM package. It's just like an atomic, usable snippet of code.

**Jerold Santo:** Do you expect people to ever have full-fledged systems? It sounds like your kind of did; that they're all just a bunch of vans put together...

**Steve Grouse:** Yeah. That's the dream.

**Jerold Santo:** That's the dream. So are there facilities in there to make that scalable and fast? I mean, it just feels like you're putting everything -- you're putting all your functions inside a Postgres database at the end of the day, right?

**Steve Grouse:** Oh, yeah.

**Jerold Santo:** And then you're like -- sure, there's caching, and there's warm-up, and stuff that... But it's like, you know, that could all run on one machine really fast, but we're going to run it on 75 machines across this network of vans, that you guys have a distributed network.

**Steve Grouse:** Yeah.

**Jerold Santo:** It's kinda like the microservices' thing over again, at the function level. So what are your thoughts on that?

**Steve Grouse:** I think there are going to be a lot of challenges. I think it's going to be really hard to pull this off. You could pick a number of different directions. Where my brain goes is let's say you have 10 or 100 functions that represent your backend, and now you want to make a change. In a normal server, this would be a pull request, where you'd have changes across them, and you'd make a branch, which is like a fork of all 100 functions. You get a copy of this environment, and then you'd have a pull request... Can we have change sets, or a pull request against 10 or 100 vans?

**Jerold Santo:** \[42:14\] Right.

**Steve Grouse:** ... I don't know, I hope so. At the extreme, or if I really succeed, I'm going to have to build kind of like all of GitHub over again into Val Town. And so you'll put like 100 vans in a folder, and you'll hit Fork, and it will create a branch of that folder that clones all your vans into a new environment... But what's nice about that it is all instantly deployed. You hit the Fork button, boom. You have a deployed fork, with its own name, like a preview branch. And then you go make your changes. And then now after you want to do a pull request to a folder of vans across 100.

**Jerold Santo:** Right.

**Steve Grouse:** Conceptually, it's possible. Yeah, that's the sort of thing that hopefully is a couple of rounds of VC funding away from me, so I can have a whole team that can work on it.

**Amal Hussein:** Yeah. I think the real question is really just if you do succeed in that, is it called Val Town, or is it called Val City, Val Metropolis? Val Planet...

**Steve Grouse:** \[laughs\] Right. I upgrade...

**Amal Hussein:** Yeah. Are there going to be tiers?

**Steve Grouse:** Val Universe...

**Amal Hussein:** Val Universe, yes.

**Steve Grouse:** Val Galaxy...

**Amal Hussein:** Or you just rebrand to Beta, you know... Just kidding. I don't know if anybody got the -- \[laughs\]

**Jerold Santo:** Well, maybe if we take the Twitter analogy -- sorry, the X analogy...

**Steve Grouse:** Oh, God...

**Jerold Santo:** Gosh... Because you're inspired by that, and vans are kind of your tweet, right? And then you have threads. And we talked about this a little bit. And I can see you threading together five, six, maybe seven.

**Steve Grouse:** Sure.

**Jerold Santo:** But nobody writes a book, a novel, and publishes it on Twitter, right? So maybe that whole thing is just like "You know what? That is a different project." And maybe those two are simpatico, and they play nice together. Every platform has to have its thing, and usually, where you start is where you end, even though you may try to change it into something else... And so maybe it won't ever be that full-fledged application delivery platform, and maybe that's just okay. Maybe the VCs don't think that's okay. And that's something Steve will have to wrestle with. But I think Val Town could be incredibly successful just by staying at this in this micro world. There's so much you can do with five, six or seven functions that are shareable, and just publicly-deployed, and this kind of stuff. So I can see where that could be the dream, but maybe it doesn't have to be.

**Amal Hussein:** And it's a very clever API, too. I just want to put that out there. I really love the fact that -- I'm like "Wow, this is a creative spin on the power and the beauty of the web."

**Jerold Santo:** It is cool.

**Amal Hussein:** I love the -- like, you can add parameters to the URL in order to pass things into a Val function. That's pretty cool. And if you want to do things fancier, there's a whole Express kind of style API that you can use for more complex data... But I think it's pretty neat, so I agree with Jerold; there's a lot of magic and productivity and success in just keeping it simple.

**Steve Grouse:** Yeah. We will for a while -- someone in the Discord came in yesterday and was like "Can I abuse Val Town to make it a whole backend for my mobile app?" And he had a number of requirements that he wanted to know if we could scale to handle... And it was like "Yeah, we want to try. We want to try." That's what I hope success looks, where people use us for small things, we're good at small things, and then they abuse us for big things, and we can try to smooth out those rough edges over time. But maybe you're right, maybe it won't be possible to -- yeah, maybe books will never be written on Twitter, maybe whole backends will never be written on Val Town.

**Jerold Santo:** Well, I think you could probably do it. I mean, I don't know if there's a thread count limit on Twitter... I think you probably could publish a book on Twitter.

**Steve Grouse:** A novel?

**Jerold Santo:** \[45:59\] Yeah. And I just don't think it's advisable. And maybe that's the case with Val Town. Like, "Yeah, you can do it. We made it technically possible. It was really hard." And some companies are getting to that size. Maybe they're novellas. But it's just not advisable. Like, maybe you just need your own application delivery network for that. And you could also scale the size of a Val, perhaps. And I think that's kind of where you're pricing -- we didn't get into your pricing yet. I think that's where it comes in.

**Steve Grouse:** Oh, yeah.

**Jerold Santo:** So you know, we talk about small functions, and I think five lines, three lines, 17 lines... But what if a Val was a macro service, so to speak, in the analogy? ...and now you have these -- like, in the case of a mobile app, you have endpoints. And maybe one Val represents an endpoint. And that might not be a simple, small thing, eventually. Maybe that has its own little subroutines, and there's an API that Val publishes. I'm not sure how big that could get, but then you have basically each endpoint is a Val, and that might have its own things, and be bigger than we're thinking about it. Just an idea of a way of tackling the same thing. I don't think Val Town is too simple for endpoints for a mobile app. Conceptually, I think that that's safe. But endpoints for Stripe... Right?

**Steve Grouse:** Yeah, exactly. Exactly. Well, I guess -- scale is funny. Are we talking a company with one employee? Five employees? 10 employees? 1000 employees? It really changes.

**Jerold Santo:** Each order of magnitude, yeah.

**Steve Grouse:** Yeah. If you're like "Val Town will never be used by companies with 1,000 employees for their backend", sure. That might be true. But a 1,000-person company will use Val Town to share snippets of code, and to explain their API docs to other people... You know, enterprises will use Val Town internally, will use Val Town to show off their API externally... Or at least that's the dream. But yeah, Stripe is never going to move its architecture over, and that's fine.

**Jerold Santo:** Well, I'm speaking like application-scale... Yeah, totally. Well, speak to the pricing then... So in terms of scale. Because at a certain point, I do start paid, as a user. And of course, this is what keeps the lights on. So what's your plan there, and how does that work?

**Steve Grouse:** Yeah. So currently, we only have one plan. It's a Pro Plan at $10 a month, and it's - yeah, flat rate. We let you run intervals more frequently. So right now, the limit on the free plan is you could run an interval every 15 minutes, and on the Pro Plan it's every one minute. But we might be increasing or decreasing - depending on how you think about it - the limit on the Pro Plan to be once a second. We'll see if we can handle that.

I also mentioned how much persistence you can store in a Val - it's slightly different on each of the plans. Another thing we're going to add really soon, I think, is -- so we just launched yesterday, you can email a Val. So if my Val is Steakhouse. Foo, that's the name of the Val, you can email Steakhouse. Foo\[at\]Dalton.email, and it will trigger the Val, and it will pass in the parameters of that email as the first argument of the function of the Val... Which is cool. So it pairs with console. Email, which is how you'd email yourself from a Val.

But one of our long-term features people have been asking for is they want to email other people that are not themselves from Val Town. But we've resisted that because of email spam reasons. But we think we're going to open that up for Pro users, because it'll be easy to detect that behaviour, and turn it off if our pro users -- because they're tied to a credit card, and whatnot.

So yeah, little things that; things that cost us money, things that are potential for abuse, we gate those behind the Pro Plan. And right now, we don't want you to think about the Pro Plan as like you're paying for compute; you're paying for more like things around the edges, like being able to email arbitrary people, or run intervals all the freaking time. Over time, we're going to have to charge for compute if you want to do crazy amounts of compute. Like, above $10 a month. In theory, you should be able to do as much compute as you want on us, and we'll just kind of charge you for that proportionately. But we haven't reached that scale yet.

**Amal Hussein:** That's super-neat. Yeah, I would say please just -- my only ask of you, Steve, is just the sooner you can have a server that's not just based in Ohio, the better. The internet is for everybody! So if you have users in China, let's get some servers in Asia, right? That would be nice.

\[50:11\] But that being said, I'm just curious... It's been so insightful hearing you talking about this early-stage product that's obviously gained quite a bit of momentum... I'm curious to kind of hear about the decisions behind your stack. You mentioned a little bit earlier that you're using Remix, especially for the frontend. Out of curiosity, I went and looked up some statistics in the Chrome User Report around what frameworks were popular, and what the numbers are in the wild etc. and Remix came up with, I think, roughly 1,500 sites in the wild. And I jokingly made a comment to a friend of mine, like "I'm pretty sure 1,200 of those 1,500 sites are demo apps." But obviously, I was just joking. So I'm just curious, what was the decision behind kind of choosing Remix, and also just what decisions you were making when evaluating your frontend stack?

**Steve Grouse:** This really is more of a question for my co-founder, Tom Mac Wright. How we became friends - I was following him on the internet, and I just loved... Like, he tries all the new JavaScript technologies, and writes good reviews about them... So he did a good, hard look at Next and Remix, and maybe a couple others, but it was really between those two... And he went with Remix, which I was happy with. I've used Next in the past, and it's fine; it feels maybe a little heavier weight than Remix. Remix kind of fits more of our vibe, of like web-standard kind of things...

**Amal Hussein:** It's faster, for sure.

**Steve Grouse:** Yeah. It's a little bit less proprietary kind of vibe... But I'm a huge fan of Tercel and Next, and depending on where these platforms go, I would not be shocked if a year from now I came back on this show and was like "And here's why we moved to Next." That could definitely be in our future.

**Amal Hussein:** Thank you for sharing.

**Jerold Santo:** Well, I'm super-excited about Val Town. We do have a couple of questions coming in from our chat... By the way, JS Party listeners, if you're not in the Changelog Community Slack, why not? It's totally free. Head to JSParty.fm/community, join there, hang out with us, talk while we record shows, talk in between shows... Why not?

So here's from Darcy Clarke... Hey, we know Darcy Clarke, don't we, Amal? He was just on the show a couple of weeks ago with the NPM Manifest Confusion... Is that what it's called? I love that term, if I got it right. So Darcy has been playing with Val Town, and he has a question. He says, "Is there a way today, or do you plan to support dynamic references? For example, today if I do @username.Val", and username is in brackets, "it doesn't work. So there's no way to export users or references." So I guess this would be for sharing purposes, like maybe you can't do that... Maybe you understand the question better than I do as the platform creator.

**Steve Grouse:** Totally. Yeah. Yeah, we don't support that now. So the reason we don't support that now is because of the magical way that imports work today. That's quite limited, which is part of why moving to web standards will be so exciting and important to our project. So right now, we parse the code for all your references, statically, we bundle those references in before the code even starts to run.

**Jerold Santo:** Gotcha.

**Steve Grouse:** So that's why we currently don't allow dynamic imports. But in the future, in the very near future, like in the next month or two, dynamic imports will just work.

**Amal Hussein:** Wow...

**Jerold Santo:** Okay. There you go, Darcy, it'll just work. Hang out for a month or two...

**Steve Grouse:** Like import, like await import, and then just give it a string, and you can construct that string dynamically. I guess already you can do imports in Val Town, and you can if you can construct -- well, actually, we try to block dynamic string construction, but there are ways around it. Some of our users have figured it out, and I can let you in on the secret.

**Jerold Santo:** Okay. Well, if there are ways around it, Darcy will find them, because he is a security buff, and he likes to find ways around things. In fact, he has another question about security things, that maybe I'll ask in the post show, just in case...

**Amal Hussein:** \[54:17\] I have some security things, too. Well, I mean, this has been a burning question in general, but why don't we go with Darcy's second question first, actually?

**Jerold Santo:** So are there future plans to sanitize secrets and values to protect users? It seems it's pretty easy to expose those in vans today. And he has some code...

**Steve Grouse:** Yes. Yes. Oh, that's a great question. If you ever create code that exposes your own secrets, you could delete code from Val Town immediately. Or you can send us a message, and we'll make sure it's totally gone. That's easy enough. Obviously, if someone else exposed a secret, just let us know and we'll remove that for them. But yes, we do have an idea, or a couple ideas to help protect you from shooting yourself in the foot in this way, for sure.

One idea we have, that I think is easy enough to build, that we'll probably do in the next month or two is we'll just check on any output that you're doing from Val Town - we'll just check it against all of your secrets. And if we see any of your secrets in the output, we'll just redact it and send you a message. So that's simple enough. Maybe we'll build on that, and do a secret detector; if we see a random-looking string, we'll say "We think this is a secret and we've redacted it. Let us know if it's not a secret, and we'll show people what it is." So anyway, there's a lot we can do there.

**Amal Hussein:** Or hopefully AI. Hopefully you can use AI for that.

**Steve Grouse:** Yeah.

**Amal Hussein:** I mean, quite frankly, you don't have to -- but yeah, hopefully somebody open sources that in general, because I think that's a very useful thing; like a smart linter, one that isn't just using a regex. But yeah, so my question is just kind of around -- I know that, for example, Cloudflare workers have very kind of tight execution contexts, everything's sandboxed, but things are running on the same machine, from different companies, from different requests etc. And so I'm just curious how you all have taken that consideration into your architecture, and what guarantees security here?

**Steve Grouse:** So right now, most of our security model is coming from Demo, which - that's kind of their main value proposition, that it offers pretty tight security guarantees. But over time, we'll probably just keep wrapping things in containers to just doubly and triply secure you. I think that's kind of what people do these days. You create an enclave, then you create another, and whatever; you create a number of things... What's the one that the Amazon -- I always forget the name; Amazon's open source container runtime thing that they use internally for Lambda... Anyway, I'm sure most people listening to this probably --

**Amal Hussein:** Blazer? Racer? Phaser. Let's just call it Blazer and move on.

**Steve Grouse:** Yeah, we can move on. Yeah, right now we're doing pretty well. In the history of the company we have had some exploits found, from like white-hat hackers... And it's been amazing. We have really -- I think Val Town attracts the kind of person who loves to escape sandboxes, and so we have users who spend so much time... Like, all they're trying to do is find exploits in Val Town and escape our sandbox... And so it gives me so much confidence in our platform, because we have these brilliant people who've found all these exploits, reported them, we've closed them, we've improved the security system to a point where we haven't gotten an exploit reported in many, many months. So I'm feeling very secure about things these days.

**Amal Hussein:** Cool. Awesome. Well, thank you so much for sharing that, and congrats on your product journey, and can't wait to see Val Town become City, and Metropolis, and Planet, Universe... Eventually rebrand, obviously, because -- just kidding. \[laughs\] But yeah, thank you so much.

**Steve Grouse:** Yeah. Thanks for having me.

**Jerold Santo:** Alright, listener, the website, if we haven't said it enough times on the show, is Val.town. Cool use of one of those new top-level domains. Check it out, let us know what you think in the comments. We'd love to hear from you what you're building, and share the code that you build. Put some vans out there to the world. Come into our JS Party channel and share your vans with us, and we can collaborate on some cool public code.

That is the show for this week. Steve, thanks once again for joining us. This has been awesome. Amal, thank you so much for copiloting. A real human with me today, not a GitHub Copilot. I can't avoid that joke anytime it comes across my radar, even though I've said it 17 times on the show. Okay, I'm going to hit this Outro button before I keep talking more. Bye, you all. It's been fun.
