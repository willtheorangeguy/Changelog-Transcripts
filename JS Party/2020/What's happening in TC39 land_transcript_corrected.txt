**Kevin Ball:** Hello, JS Party people, and welcome to this week's JS Party! I'm Ball, I will be your MC today, and I'm joined by three wonderful people I'm so excited to introduce, especially because I have three firsts going on.

First off, Emma is joining us. This is the first time I'm on a podcast with you since you moved. How's it going, Emma?

**Emma Bosnian:** It's going great. I'm living in a house full of cardboard, of IKEA. I literally live in IKEA now. So it's great.

**Kevin Ball:** Awesome! Next, Amal - first time I'm on an episode with you when you're actually on the team... I think we've interviewed before, but welcome. So excited to have you.

**Amal Hussein:** Thank you. So excited to be here, Ball.

**Kevin Ball:** And next, we have a super-special guest. Jordan Harland is joining us to talk about TC39 and what's coming down the pipe. Jordan, how are you doing?

**Jordan Harland:** Good, thanks. Great to be here.

**Kevin Ball:** So let's get started by talking a little bit -- Jordan, can you introduce yourself and what your role is with TC39?

**Jordan Harland:** Yeah, sure. I'm Jordan, I kind of have a couple roles on TC39 - the primary one is actually just as a delegate, meaning I represent my employer, and provide feedback on proposals, I champion proposals myself, and I attend the meetings, which are six times a year. But the other role that I have is I'm one of the editors of the specification, and have been for about 2,5 years. At the moment there's four. The number has changed... Historically, there was one, and now we have kind of a group of people to help share the workload.

So the editors are responsible for merging changes into the specifications once the committee has agreed on them, and can make editorial judgment calls about how things are worded... But the semantics are decided by the wider committee.

**Kevin Ball:** Alright. And just in case anyone on our listening crew doesn't know already, TC39 - the specification you are editing is...?

**Jordan Harland:** Sorry, yes - TC39 is the Technical Committee that writes the specification for JavaScript, the language that runs \[unintelligible 00:03:50.00\]

**Kevin Ball:** So exceedingly relevant for those of us on JS Party. Let's do just a super-quick overview of what the process is, and then dive into the fun stuff about what are the things coming down the pipe.

**Jordan Harland:** \[04:01\] Yeah, absolutely. Ever since 2015, ES6, we've been operating under a process where every year we release a new edition of the specification, with whatever changes have landed in the interim... And there's a process with multiple stages for proposals to move through in order to land in the language. So the earliest stage is stage zero, which is kind of like "I've got this wild idea." Stage one is the committee agrees that this is a problem that we need to explore further. Stage two is "This is the solution. We want to solve the problem and put in a solution in the language, and we have a pretty good idea of what that solution looks like." Stage three is the solution is pretty much finished, and until it's actually implemented and shipped in browsers and other engines, we won't know about any other changes we need to make until that time. And stage four is when it's finished and lands in the specification.

**Kevin Ball:** And so with Babel we can start using these about stage zero, right?

**Jordan Harland:** Certainly you could, you have the ability to do so, but I phrased those stages very carefully, in that the actual solution isn't finalized until stage three. So the earlier in the stage process that you use something, the more likely it is to change in a way that will cause a lot of churn and breakage in your codebase. So while it's great to experiment with early-stage proposals, it's generally a very ill-advised idea to use them in production before stage three.

**Amal Hussein:** Yeah... Thanks for asking that very poignant question, Ball... Because for me, stage zero is like an idea. Stage zero is anybody from the internet can submit a pull request, and it's a stage zero proposal. So there's no barrier to entry. Well, I mean anyone-is. Actually, Jordan, could you clarify that?

**Jordan Harland:** Yeah, absolutely. So anyone can write a proposal, but in order to be considered an actual proposal, a TC39 delegate has to champion it, meaning they have to put their name to it and agree to drive it through the process and shepherd it. And there can be more than one champion, but there has to be at least one. And although there's not a strict requirement for stage zero beyond "It's got a champion", typically we don't add things to the list in the proposals repo on GitHub until it's both championed and also at least added onto an agenda, planned to be discussed in that coming meeting.

**Amal Hussein:** Okay, got it. So there is an "anybody view", but that "anybody view" is in the pull requests, as opposed to the merged items that reflect on the list. Is that correct?

**Jordan Harland:** Right.

**Amal Hussein:** Okay, got it.

**Jordan Harland:** Yeah. And certainly, anybody can author a pull request to change something in a specification, but we have two big categories - editorial and normative. Editorial is like you just worded it differently, you spelled some things differently; normative is where runtime JavaScript code could observe the difference, and normative changes require committee agreement/consensus, and depending on what the change is, we sort of make judgment calls whether something needs to be a proposal or just a pull request.

**Kevin Ball:** What are some of the strangest proposals that have come through?

**Jordan Harland:** There have been a lot of ideas that people have. I'm hesitant to call out specific ones, because I don't want the individuals who came up with them to be discouraged...

**Kevin Ball:** Aww...

**Jordan Harland:** But I would say that folks often will have a favourite concept in a different language, and will naturally expect that concept to work in JavaScript, and will come up with what they think is a good solution to provide that feature, without really thinking through all the rest of the consequences. So it might be that the concept is actually great, but that solution is inappropriate for JavaScript... But it also could be that that concept is inappropriate for JavaScript, and those discussions are difficult to have without discouraging people from interacting. I'm sure I could dredge up specifics, but I don't have anything off the top of my head.

**Emma Bosnian:** I'm curious, how did you become part of the TC39 panel?

**Jordan Harland:** \[08:03\] Sure. So I was maintaining the es5-shim and es6-shim back in 2014. I still am, but at the time, they were basically the primary way anybody polyfilled JavaScript language features, meaning like provided them to an older browser that didn't ship them already... And as a result, I had to kind of pay attention to the specification itself in order to implement those correctly.

One of the maintainers of jQuery actually reached out to me on Twitter and asked if I wanted to attend as a guest. In that first meeting I was able to provide advice that changed the specification. That was a perfect feeling. It was very exciting to be able to have made a substantive change to such an important language... So I kind of caught the bug and immediately started advocating that my company joined and sent me as a delegate \[unintelligible 00:08:56.28\]

**Emma Bosnian:** This is just a PSA for anyone listening, that Twitter is actually a very important networking and marketing tool. So if you want to branch out and join new organizations and get new career opportunities, I highly recommend it.

**Amal Hussein:** Yeah, it's definitely the millennial marketing tool, more so than LinkedIn. I feel like LinkedIn is for businesspeople, and...

**Emma Bosnian:** And weird VCs.

**Amal Hussein:** ...VCs and marketers that want to connect with each other... And Twitter is how the rest of us connect and market and promote our work and interests. But yeah, Jordan - super-fascinating insight. I think for me what's really cool about seeing the evolution of this TC39 story is more and more involvement from practitioners, I would say. There's always, I would say, involvement from implementers... And for those of you wondering "What are implementers?" Implementers are people who work at browsers that write the C++ code that the JavaScript engines use. Those are implementers, and then there are a bunch of language nerds that are typically part of these language committees, that are very into language design, but maybe more removed from the day-to-day actual usage of that language. Then you have folks like Jordan, who come from the web developer world, that are practitioners, so the folks that are actually using that language.

So what you have is this triangle of implementers, language nerds - sorry, I can't come up with a better word for that - and then you have web developers. And I think the push-pull tension between those three groups is how you have this -- it has produced this lovely body of work since ECMAScript 2015.

Speaking of body of work, let's get into talking about what's coming down the pipeline. Ball, should we start with -- do we want to work our way from idea to serious, or do we want to go from serious to idea? How do we want to do this?

**Kevin Ball:** That's a good question. Well, let's take a couple just out of sequence, where we just say "What are the most interesting to you think happening right now?" and then we can do something a little more systematic in the next couple segments. Jordan, what's the most interesting proposal of any stage to you right now?

**Jordan Harland:** I have a couple. One of them is class fields; private and public class fields, which is currently stage three. It's shipped in a couple browsers, and hopefully moving to stage four soon... But it is still stage three.

Also, Records and Tuples - that's in stage two. That's a new primitive. It's like an immutable object or an immutable array, but it's a primitive, so you can compare them with equal signs, and OT compares their contents instead of just their identity.

\[11:54\] So like two objects that have a key A with the value 1 aren't equal, but two records that have those same contents are equal. Immutable.js and Dimmer and a few other libraries in the space all are attempting to solve these problems, and Records and Tuples will be a way in the language to do that.

**Amal Hussein:** Is it a new built-in, essentially?

**Jordan Harland:** Yes.

**Amal Hussein:** Okay. Alright, so for those of you wondering "What's a built-in?" Well, we have objects like map, and set, and number, and array, that are all built-ins. So with ECMAScript 6, which is ECMAScript 2015, we have a few new built-ins, I think. Symbol is another I can think of... So this would be a new thing, as opposed to an extension of something that's pre-existing.

I'm really curious, when these new built-ins get added to the language, what's the reaction from implementers? Because I keep thinking of JavaScript engines as this \[unintelligible 00:12:46.17\] code, and I'm just curious what it's like to manage that. I'm not sure what the coding patterns are in terms of being able to reuse functionality, and how folks maintain performance benchmarking... I'm an implementer, somebody wants me to create a whole new built-in - what happens?

**Jordan Harland:** Yeah, whether it's syntax, or a primitive, or API like map and set, or something. The general sense I get is that the way implementers think about these things is how they might build it in a way where it can be made fast either immediately or in the future. And in particular, they think about "Will this new feature make existing code patterns slower?" and that's usually a big no-no. So it's fine if a new thing is slow, but it's not fine if a new thing slows down old things. And it's also only fine if a new thing is slow, I think, if they think that it's possible to make it faster in the future. I'm not an implementer, so I'm not 100% sure that's how they approach it, but that's the sense I get from these conversations.

And then as you mentioned, there are implementers and language aficionados and practitioners, but all of us have our own opinions, and we all use JavaScript in some way... So the conversations end up getting really complex, because everyone's wearing multiple hats at the same time when they're expressing an opinion.

**Amal Hussein:** And I just want to clarify too, I think you brought up an interesting point around not wanting to make existing things slower by adding this new feature or built-in... I can think of decorators; that kind of was rejected because of that reason, from my understanding... Can you shed some light on that?

**Jordan Harland:** Yeah, so specifically for decorators it had advanced to stage two, and was on its third or fourth iteration... And the champions asked for stage three for the proposal, and a couple implementers withheld consensus for that advancement; so it wasn't like rejecting the proposal, but basically saying that the solution had been designed that they couldn't figure out -- they were convinced that any way they implemented it was going to make all classes slower, not just decorated ones. And that was not something they found acceptable.

So the decorators proposal is still a stage two thing. It's a problem the committee wants to solve in the language, but it's not clear really what the solution is gonna look like at the moment.

**Kevin Ball:** Can be really quick for the proposals you highlighted -- I think for someone who's not living in this space, this sound kind of dry... Like, okay, it's this new fundamental attribute. So let's explore a little bit about what that enables. You hinted at it a little bit talking about Dimmer, but what does having these immutable types enable us to do with JavaScript that we can't do very well right now.

**Jordan Harland:** Yeah, it's essentially fast comparison by content. Everything in JavaScript compares roughly by identity. You could argue that primitives compare by content, like 3=3. But if you have a complex data structure, with like an object or an array, any equality has to inefficiently move through every key-value pair or every item in the array, or every item in the set, and so forth, in order to do those comparisons.

\[16:08\] React, for example, has a bunch of things that they do to do shallow comparisons... And then when the shallow comparisons fail, they just re-render everything. So if you're a React developer, you may have been familiar with peer components, or the use Memo component wrapper, all of which are designed to try and avoid the performance hit from doing deep comparisons of objects. With Records and Tuples then you no longer need to do a deep comparison, you just compare them directly, and effectively immediately it will tell you "This has the same stuff" or "It doesn't have the same stuff."

You're right that it's dry. A lot of the stuff we do in TC39 is dry. It's low-level capabilities. Or it's sugar, abstractions, better/simpler ways to do things. Day-to-day developers are probably going to get a lot more excited about something like temporal, which is a new proposal for - it's stage two right now - basically providing a much better way to do dates and time than the pretty broken data object we have... Because temporal is something developers are gonna use directly, whereas Records and Tuples - they may or may not use them directly.

**Kevin Ball:** But they're going to make the web faster for everyone using React, which I'm pretty excited about...

**Jordan Harland:** Potentially, yeah. And I'm hesitant to claim that it will definitely make React faster, but either way, there are a lot of libraries that will be able to use them under the hood in order to make the web faster, even if you're not using them directly.

**Amal Hussein:** That makes a lot of sense. I think for me what's fascinating about this is built-ins -- for those of you who use Babel, which is probably the majority of you, Babel helps us create transforms or polyfills; and for things like built-ins, what Babel does is -- you need a polyfill, because there's no one-to-one mapping. It's not syntactic sugar, or whatever. It's not an extension of something... So I would imagine that the polyfill for Records and Tuples is probably really simple. So for those of you who maybe want to get a little bit of under-the-hood exposure to some of these language specifications, I would highly recommend looking at the polyfills... Because those are written in JavaScript, and usually they're fairly easy to follow along.

**Kevin Ball:** Awesome.

**Jordan Harland:** Yeah, the way I became more familiar with the spec was definitely looking at the polyfill code for a specific function where I knew how it worked, so I knew how it was built. That helped a lot. I think that's perfect advice.

**Amal Hussein:** Yeah. Well, thank you, Mr. Jordan... And I just learned today that you are Mr. Babel before Babel, if anyone didn't catch that, in the sense that you were creating these shims and polyfills before Babel was a thing, before Build Tools became the thing. I didn't know that you had this cool callback story, Jordan...

**Jordan Harland:** To be clear, I didn't create them... I mainly just took them over and became the maintainer of them,

**Amal Hussein:** Okay, got it.

**Jordan Harland:** These have been things the web had been using for a while.

**Amal Hussein:** Okay, cool. Yeah, I was going to say, the typical open source hero story, of like maintainer gets burnt out, new maintainer takes over and does the shepherding...

**Kevin Ball:** Alright, so let's now take a quick break, and we'll be back shortly to talk a title bit more specifics about what's going to happen in the next year coming out of TC39.

**Break:** \[19:33\]

**Kevin Ball:** Alright, let's get back to it. Emma was saying that for her, proposals really reminded her of something a little different from TC39. Emma, do you want to take us into this?

**Emma Bosnian:** Really my favourite proposal that I've ever seen was the one on The Bachelor, and my favourite ones are the ones where they get rejected. Rejections are not fun if you're the person being rejected, but they're interesting for the onlookers... So I'm curious, why would a proposal in TC39 get rejected? Give us all the dirty details.

**Jordan Harland:** Sure. I've had a number of proposals rejected...

**Amal Hussein:** TC39 drama.

**Jordan Harland:** I had one that I tried to get advancements at the last meeting, and it got blocked. So it happens a lot... I think that it kind of depends on what kind of proposal it is. When they're for something that's really foundational for the language, and it'll change a lot of stuff, it'll be a huge deal, then people are a lot more nervous about advancing it, and they want to be a lot more confident about the consequences before they move it on... Whereas something simple - it's a lot tougher to come up with a good reason not to move it forward.

One of the proposals that went well was object. Values and object.entries. Those were relatively straightforward; we already had object.keys... Keys, values and entries were already concepts... There were a bunch of libraries in the ecosystem that already did this stuff, so there weren't that many reasons to reject that proposal. People would just kind of massage the shape of it; they'd have bike shed type opinions.

But then I had another proposal that was like `Error.isError()`, like `Array.isArray()`. I wanted a way to determine if something was an error reliably...

**Amal Hussein:** Okay, that sounds super \[unintelligible 00:22:21.09\] `Error.isError()` I feel like that is like--

**Emma Bosnian:** What's your thought process behind that? \[laughs\]

**Amal Hussein:** Swoosh! `Error.isError()` Yeah, explain, please.

**Jordan Harland:** Essentially, there's the concept -- if you're familiar with iframes, how you can have a different array constructor in an iframe, and you can't in the regular web page... Those are called realms. So if you wanna -- you can't use instance of array to determine if an array from an iframe is an array or not, because it's a different array constructor. So you have to use the `Array. IsArray()` function to tell you if something is really an array or not. And similarly, there isn't any cross-realm way to say something's an error. You can only say instance of error, and that doesn't work if it's from an iframe.

**Amal Hussein:** So realms, for anyone who doesn't know what realms are - realms are different environments within the browser. We can kind of think about it that way. Service workers - its own kind of environment realm where web worker is, iframes are... So when you're in a browser, your main document is like the main realm, and each of these realms has a different "this" instance. And I think we can get into talking about "this" in a little bit, because Jordan is the one who proposed global "this", which is a thing we can discuss in a bit. So realms are these spaces, these different contexts.

Now that we kind of know what realms are, could you explain again what is all this instance and reference tracking that doesn't equate? I'm not clear on why that happens. Could you explain?

**Jordan Harland:** \[23:55\] So if you do two square brackets, that makes an array, and that has a.constructor property, and then that array's.constructor property is going to be the Array function. But if you do the square brackets inside an iframe and also do it on the main part of the web page, and you try and do triple equals with those constructors, that's not going to be equal. They're different constructors. Those two array functions are different.

**Amal Hussein:** Yeah, I know. That makes sense. I would understand that to be different, because they're different objects in memory though.

**Jordan Harland:** That's exactly right.

**Amal Hussein:** Okay. But I'm just saying, why is that a realm issue, versus like I just create array 1, array 2, and I say "Is array 1 and array 2 equal?" and I would expect no...

**Kevin Ball:** Well, I think we're trying to figure out the class, right? Like, is this an array that I can work with?

**Jordan Harland:** Yes. What kind of thing is it.

**Kevin Ball:** Yeah, what type of thing is it.

**Amal Hussein:** I see, I see. Got it, okay. Thank you for clarifying.

**Jordan Harland:** And if somebody gives you a value, and you don't know what it is, and you want to figure out what kind of thing it is, and you want to see if it's an array, `Array. IsArray()` is the only way to do that that's always correct.

**Amal Hussein:** Yeah. Well, I'm just curious though - if somebody passes me a null value or a symbol, and I try to call Disarray or Is Error on that...

**Kevin Ball:** I think it's a class method, right? So it's a method on the array class.

**Jordan Harland:** Yeah, it's a static method.

**Amal Hussein:** Correct, yeah. I'm just saying - would I just get an error saying "Property is not there"?

**Jordan Harland:** It would return false.

**Kevin Ball:** No, you'd pass in your value, right? So you're not calling object. IsArray, you're calling array. IsArray pass object.

**Amal Hussein:** Okay, got it, got it. Sorry, yeah. I'm spacing out on the API. The API is -- you pass it the thing. Okay, got it.

**Emma Bosnian:** I'm going to propose to Jordan right now, because look - I really want a class... I'm not getting down on one knee, because I'm too tired.

**Amal Hussein:** You're going to have to get in line on the Jordan proposal. I think I beat you to that.

**Emma Bosnian:** Okay, well, I'm cutting the line...

**Amal Hussein:** \[laughs\]

**Kevin Ball:** Have you ever been propositioned on a podcast before? \[laughter\]

**Emma Bosnian:** This is turning weird, but --

**Jordan Harland:** As you say, Ball, this is a day of firsts... \[laughter\]

**Emma Bosnian:** Plot twist. Jordan, we actually brought you here to pitch you all of our ideas. This is like Shark Tank, but for TC39.

**Amal Hussein:** Yeah. We're holding him hostage, actually. Can we just advance some proposals now that we have you hostage?

**Emma Bosnian:** Okay, so I know we've got `Array. IsArray()`. I want Array. WhyIsMyArrayNotAnArray. Tell me where it went wrong. \[laughter\]

**Jordan Harland:** I actually have a NPM package called IsThatEqual, where you can pass it two things and there's a why function in it. You can pass it two things, and it'll give you some text that tells you why they're different, if that's helpful...

**Emma Bosnian:** Oh...!

**Kevin Ball:** Close, close.

**Amal Hussein:** Yeah, and that is the classic definition of the one-line package, right? That is the Left Pad of JavaScript, in many ways...

**Jordan Harland:** That is way more than one line, but yeah...

**Amal Hussein:** Oh, it is? Okay... Well, you know, I feel like I could write that in one line, Jordan. Shame on you. \[laughs\] Just kidding...

**Jordan Harland:** Challenge accepted. Pull requests open. \[laughter\]

**Amal Hussein:** No, just kidding. Actually, I'll just take a tangent on module design... What's his -- is it Sinuous? I never know how to pronounce his name. The cool dinosaur guy who has every single package on NPM.

**Jordan Harland:** I don't know how to pronounce it out loud either.

**Amal Hussein:** Okay, so I'm happy that this is a universally shared problem. Ball, do you know?

**Kevin Ball:** I don't even know who you're talking about.

**Amal Hussein:** Oh, you know who I'm talking about. Sinuous... Minors...

**Jordan Harland:** I usually read it as Indre Sorus, but I have no idea if that's right.

**Amal Hussein:** Alright, well Indre Sorus -- somebody correct us. Somebody tweet us the video, or the correct pronunciation of his name. Indre Sorus...

**Kevin Ball:** Oh, that guy...

**Amal Hussein:** That person, yes.

**Kevin Ball:** I recognize it from your name of him.

**Amal Hussein:** How would you read that in your head?

**Kevin Ball:** I don't know.

**Amal Hussein:** Okay. Alright, so Indre Sorus said this one time - he's actually kind of a fountain of knowledge, but he said that for him, it doesn't really matter whether a module is one line or a thousand lines, in the sense that it abstracts away some behaviour. So lines of code is not necessarily a useful metric to judge a package by. I would say dependencies is though, for me. When I'm always picking packages, I'm like "How many dependencies do you have?" Because ultimately, all those dependencies become your problem, as soon as you import this into your app... In the sense that you might have peer dependency conflicts, downstream security issues... So just a tangent there on picking modules - don't judge the lines of code.

**Jordan Harland:** \[28:32\] Well, you mentioned Left Pad... While that happens, I was actually in the middle of proposing `String.prototype.padStart()` and `String.prototype.padEnd()`, which were stage two at the time, and it was very amusing to me that almost every Hacker News comment that said "That's just a one-line thing", they all wrote it wrong. Every one of them had bugs. So even a one-line change can often be very difficult to write correctly, and so there's a lot of value in having a separately well-tested, well-used package to abstract that away.

**Kevin Ball:** I don't think anyone who's ever worked with a regular expression would doubt you on that.

**Jordan Harland:** \[laughs\]

**Emma Bosnian:** So I really want to know what this syndrome is called, when you vehemently believe that something is part of this TC39 spec and it is not? Because today I had one of those moments where we were working, and I'm like "Alright, we need to check if our array is empty. Array. IsEmpty. It's definitely on there, I know it is." I know I can just check that length is zero, but I was 99% sure that that existed, and it didn't. So what is that called? We've got to come up with some name, because I'm not the only one that's experienced this.

**Jordan Harland:** It might be the same phenomenon as remembering how to spell Bernstein Bears.

**Emma Bosnian:** Dunning-Kruger -- I don't know how to spell that.

**Jordan Harland:** But there's a meme out there that it's a parallel universe thing, so maybe it's that. Maybe it really existed in the universe you're from.

**Kevin Ball:** Yeah, the Bernstein versus Bernstein. My kids are really into Bernstein Bears right now... But I always thought it was Bernstein.

**Amal Hussein:** That's super-cool.

**Kevin Ball:** They also have like -- they're not internally consistent. I've been reading a lot of them now... They reference their honeymoon location like five times differently, in different books... So this sort of "I think it's there, but it's not there" is not unique to TC39.

**Amal Hussein:** Jordan, do you want to tell us about `global This`, since we talked about realms?

**Jordan Harland:** Sure.

**Amal Hussein:** What stage is that in? And also, from my understanding, there is this kind of hoopla around the name itself, and maybe can you shed some light on how hard it is to name things when you're writing ECMAScript specs? Because there's only a limited number of keys on a keyboard, and there's a lot of stuff that's already taken... How does that work?

**Jordan Harland:** Well, the proposal itself was basically the global. There wasn't a universal way in the language to reference it. So browsers had window, Node had global, other engines had nothing, or something different... So this was a proposal to come up with a single way to reference it. Just pick a spelling and let's all agree that this is the magic word that references the global object, and we're done.

The challenge in naming it was twofold. The first was that I started out just calling it global. Then we shipped it, and then it broke Flickr.

**Amal Hussein:** Wait, Flickr is still a thing...?

**Jordan Harland:** Flickr.com. Well, at the time that we shipped it, in 2017 or something, it very much was.

**Amal Hussein:** Oh, wow.

**Jordan Harland:** I haven't been to it recently.

**Amal Hussein:** I'm sure it's still a thing. The web has a long arc, yeah.

**Jordan Harland:** But it was using an old version of moment, that was compiled with an in-house bundler tool, and just the way that it did that ended up breaking when global was a variable that already existed... Which sucked, but also it meant that that name was just kind of not an option, because one thing that is the most important part of TC39 is "Do not break the web." So anything that causes any noticeable number of websites to break is just not something browsers are gonna want to ship, and so it's not something we put in the specification.

\[32:12\] Then I had to come up with a new name, and there was a lot of bike sheds, there were a lot of ideas thrown out, and what I ended up doing was asking another browser to gather data about which ones were already in use, basically trying in advance to see which names would work. I came up with 30 names, and the response was "That's too many. Give us five." I put global on there as a control, and then I put a few others, including `global This`, which is the name it ended up having... They looked at the number of websites using it, and the result was that `global This` was the safest option.

**Amal Hussein:** It was the name that nobody else thought of, because it was so bad, like nobody used it, and it was available... Like those crappy domain names... \[laughs\]

**Kevin Ball:** If you want to add new keywords, you got a pick words that nobody would ever think to use.

**Amal Hussein:** That's exactly right, Ball.

**Jordan Harland:** Yeah. So there was a lot of reaction. Basically, that name, `global This`, was approved by the committee, and we went forward with it, and about two months later a couple folks with large Twitter followings noticed it. A bunch of people showed up on the repo, very angry that the name that we chose wasn't one that they liked, and with different ideas.

What finally ended up relaxing it was another committee member, Yulia, who works at Mozilla - she helped me write a naming document that was basically a bunch of constraints, like musts, and should, and must not and should not... And for each constraint, it explained what it was and why it existed, and then for each one it said "These are the names that this allows. These are the names that are still okay with this constraint." And after you're done reading through that document, it turns out it's pretty difficult to still disagree with the name. You can dislike it, of course, but it becomes apparent why it was one of the few options. That was really helpful, and I want to do that for anything I do that's contentious around proposals in the future, because that changed what was a very nightmarish couple of weeks of GitHub notifications for me, into a very manageable \[unintelligible 00:34:26.16\]

**Amal Hussein:** Streamlined, yeah. I've got to say, I've been doing a lot of thinking around change management, and nerd herding, and what the most efficient way to do that is, and I think that strategy that you took is really cool. We'll link that document that you created in the show notes, so folks can take a look at it as well... But yeah, that's super-neat.

**Kevin Ball:** And did that document also lead to smooth?

**Amal Hussein:** Oh...

**Jordan Harland:** I don't remember the exact order in which these happened, but smooth was because the original name for array.prototype.flat was array.prototype.flatten, and it turns out that a library called Moo Tools had used that word, so it would break websites if arrays started having a flatten method... And one of the champions -- or the champion for that proposal posted a (I think) mostly joking GitHub issue saying that he was going to rename it from flatten to smooth, and a lot of folks took it very seriously, and some folks even tried to create a campaign to make it web-incompatible to name it smooth. They tried to make it so that websites would break if arrays started having smooth.

**Amal Hussein:** I thought that was a little taking it too far though. I thought that was not nice. It was like people trying to actively start a guerilla campaign to jeopardize the success of this proposal. It was a joke to begin with, but most people didn't know that it was a joke, and then it just got out of hand really fast, and it was just like "WTF...?" \[laughs\]

**Kevin Ball:** \[36:04\] Wait, wait... People were deliberately being mean on the internet?

**Amal Hussein:** Oh, yeah...

**Emma Bosnian:** That never happens.

**Amal Hussein:** Never. Developers are the nicest people. \[laughs\]

**Kevin Ball:** With that, let's take another quick break, and we'll come back and talk a little bit more about some of the wild stuff that's way down still in the stage one and zero.

**Break:** \[36:26\]

**Amal Hussein:** So Jordan, let's talk about date time in JavaScript. Dates, times, timezones - these are things that have been known to break a man...

**Jordan Harland:** Yeah, unfortunately, the JavaScript date object is not great. There are a lot of things about it that are underspecified, meaning browsers do things slightly differently. It's always in local time, so you can't represent a time in a different timezone, and it's really easy to screw up the timezone math as you're trying to make those adjustments... And you can't have a date without a time, you can't have a time without a date.

A date picker I wrote broke one time because we picked midnight as the just placeholder time for the dates. In Brazil, once a year, midnight doesn't exist because their daylight savings time advances at midnight and says 2 AM. So in Brazil, a date picker on Twitter (like Twitter.com) broke because of JavaScript's date object. And this happens all the time.

**Amal Hussein:** \[laughs\] What did Brazil do during Y2K? Were they extra freaked out because they were like "We also have a weird edge case with the way we do time in Brazil..."

**Jordan Harland:** I mean, almost anything you can think of -- there's a great article called "Falsehoods programmers believe about names", and it's like a hundred things that many of us take for granted, that that's the way names work, and in fact, that's not. If someone were to make that list about date times and timezones, it would probably be much, much longer. There's just so many -- almost everything is an edge case. There's really no standard for a lot of this stuff.

Luckily, there's a stage two proposal called Temporal that's attempting to address this... And some of its champions actually are maintainers of Moment.js, which is one of the libraries that has solved this the best in the ecosystem so far.

**Amal Hussein:** Actually, can we take a moment to thank Moment.js, and folks like Maggie Pint from Microsoft, Philipp Dunked from Bloomberg...

**Jordan Harland:** And Matt, yeah...

**Amal Hussein:** And yeah, Matt Johnson... I'm not sure where Matt Johnson works... But Moment.js has totally smoothed over a lot of the headaches that used to be things that everyone had to do on their own, and do imperfectly... So this is kind of like a really great example of web developers taking complexity and abstracting it away into a smooth API, and dealing with the interop issues as well, in addition to the complexities around date time.

\[40:16\] What's fascinating is folks from Moment are like "Okay, cool, we've learned a lot writing Moment. Now let's take Moment and put it in the browser." So this is a perfect example of web developers making the cow paths, innovating on the web with libraries, and then eventually abstracting that behaviour back into the platform, so that we can no longer have to use Moment.

So Moment is now in just full maintenance mode, there are no new features or anything; it still works fine, but the goal is "We're going to have this natively in the browser with Temporal", which we're going to hear about from Jordan in a second...

**Kevin Ball:** Which is really, perfect, because while I love Moment, my bundle size does not.

**Amal Hussein:** Totally. Moment is huge.

**Kevin Ball:** That thing is massive.

**Amal Hussein:** Yeah. I couldn't agree with you more. The other thing - promises are another perfect example of web developers innovating hard on the web, and then coming up with a standard A+ promise kind of spec, and then having that actually be what drove forward the language spec as well.

So web developers innovating freely, without the constraints of the standards world, is something we should never take for granted. We should always have web developers doing crazy things, and creating lots of libraries, and solving lots of problems. Because eventually, one of those is gonna stick, and solve a really hard problem for the web, and then eventually, it'll hopefully be abstracted away into the platform. So they're a really key part of innovation on the platform, and I just don't think we give credit enough to folks who write libraries and solve hard problems for us. I'm done with my soliloquy now... \[laughs\]

**Jordan Harland:** No, it's perfect. And the other great thing is that one of the bigger complaints folks still have about Moment.js beside bundle size, is that it's stateful and mutable; a given moment object.

**Amal Hussein:** What does that mean? Could you break that down?

**Jordan Harland:** Yeah, sure. When you make a Moment object, if you then want to make it be last week, or next year, or something, you have to change that object, just like JavaScript's date object. There's not a clean, easy way to make a new one, or you have to remember to do it. Moment has a.clone method. And what that means is it could be easy to have bugs from accidentally changing an object in one place that you're relying on not being changed in another place. So one of the things that temporal is going to do is not suffer from that problem.

Once you've created a temporal object, there are lots of ways to easily spit off a brand new temporal object that's changed, so you can get a new temporal object that's for last week. But it won't let you change the original object, so it kind of side-steps a lot of that whole class of problems.

**Amal Hussein:** We've been talking a lot about temporal, temporal, temporal... Let's just take a few steps back for our listeners - what is temporal? And then let's talk a little bit about the specifics for the API. What are the enormous goals that they have? I think there are also some opportunities, if I remember.

I was at a TC39 meeting this time last year in Berlin, and if I remember, there were some really cool things that folks from Apple were proposing around modules... You know what I'm talking about, right?

**Jordan Harland:** Built-in modules.

**Amal Hussein:** Built-in modules... And that could potentially actually be something that temporal leveraged... Sorry to get in the weeds, but I think this is -- I'll be quick about this. Basically, built-in modules - there's a proposal out there to have built-in modules, so that JavaScript engines don't have to have every single feature in the language; that they could just kind of do this on-demand thing that we do in JavaScript, where we import something.

So the idea here is like something that does date time - we don't have to load every JavaScript engine with all the date time translations, even for internationalization. The idea is we can just do a just-in-time kind of loading. I thought that was a really cool thing, where temporal actually was like "Hey, let's maybe slow down, because maybe we can release using modules, and stuff like that."

**Jordan Harland:** \[44:20\] Browsers already do that for global. So the built-in modules aren't necessary for that optimization. And then separately, built-in modules has a lot of obstacles, so the temporal proposal decided not to try and install itself, like lock itself on that. So at the moment, it's going to supply a global temporal namespace that contains a couple different types. It's stage two, so the names are changing a little bit... And I don't have them all in my head, but one of them is currently called absolute, and it represents a fixed point in time, unrelated to location or which calendar system you're using.

Then there's another one called the date time, which is like a calendar date, and then a wall clock time, in a specific location, in a specific timezone. And then there's a time object, which is just the wall clock time. So if you need to say "This is a meeting", or "I wake up every day at 7 AM", you don't need a date to represent that, you just need a time; that's the object for that. And similarly, there's a date object, where it's like "My birthday is the same date every year, I don't care what time it is. It's that date."

And then there are a few other types, like there's one called year month and month day. A birthday is actually more of a month day, because it happens every year. A year month could be pretty much anything that happens monthly, and it doesn't matter which day it happens on. If you got paid monthly, you can use year month for that, and so on.

Then there's also a timezone and a calendar object to help manage all the complexity around that stuff, which is also part of the reason why Moment is still large, because of all the timezone and calendar information it has to hold.

So the built-in modules question was we don't want to stick 7-8 new global; we'd rather not have a namespace to hold them, so maybe we can do it as a built-in module. But the performance and functionality for the users is going to be the same either way, so at the moment it's proceeding just as a regular global, like all the other built-in stuff in JavaScript.

**Kevin Ball:** And given its stage two, what do you think the likely timeline is looking like? Because some of us are salivating to get to this stuff, but we know from Amal that we shouldn't use it yet.

**Amal Hussein:** Yes, that's right.

**Jordan Harland:** Right, exactly. Please don't use it yet. Experiment, but don't ship it to the actual web. They just didn't update in the last meeting, and their current plan, as I understand it, is that by the September meeting they are hoping to have it finalized, meaning they're going to get to a point where they stop changing the spec a lot. And then hopefully by the November meeting that will have been enough time to let the designated reviewers for the proposal, as well as the editors, to review it all. And then after it's been reviewed, it will be eligible for stage three, if the committee agrees.

So the optimistic timeline then is that it might get stage three in November... But that requires that there be sufficient review time, that there not be major changes coming out of that, and also that the committee agrees to it at stage three. But yeah, once it's stage three, browsers start shipping it, so...

**Amal Hussein:** \[47:22\] Yeah, super-cool. And this is one of those features that has been in the pipeline probably pretty long...

**Jordan Harland:** Yeah, a number of years.

**Amal Hussein:** A number of years, yeah. It took a while to get this right, and it's nice to see that it's finally getting to a stage of maturity, and a graduation time. I feel like stage two is middle school, and stage three is high school... \[laughs\] Stage four and above is like "I'm done! I'm an adult now!", so it's really nice to see that arc.

Furthermore, I'm friends with some of the folks that are championing it and authoring it, so I'm really happy that this is something that they get to make a dent on, and make a huge difference for the web. Not just in terms of simplifying the API design and abstracting it into the platform, but to kind of go back to Ball's point - we're also saving bytes, and bytes matter, just even from a resource perspective. That's fewer trees that we're burning, or that's less energy that we're using, and it's a big deal.

**Kevin Ball:** Hey, with Moment it's like tens or hundreds of kilobytes, not just bytes.

**Jordan Harland:** Yeah, it takes a lot of complex bundler configuration to bypass that problem.

**Kevin Ball:** Yeah. This has been fun, Jordan. I think we've learned a lot, and we've learned about some of the interesting stuff coming in. We've gotten some on-air proposals and all sorts of fun stuff. I think with that we're going to wrap up for now, but thank you for joining us, Jordan.

**Jordan Harland:** Happy to be here. Thanks for having me.

**Kevin Ball:** Thank you, Amal, thank you, Emma, and we'll catch you next time. Next week, next party. This is Ball, signing out.
