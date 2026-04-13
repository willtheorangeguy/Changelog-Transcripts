**Sub Hinton:** Good day! You are listening to JS Party, a weekly celebration of everything JavaScript. I'm Sub Hinton, I am your host for this episode, and I'm joined by some awesome panellists as well. This week we have a special guest joining us, who I'll introduce in a little bit, but first let's say hi to our regular panellists. First up, we have Nick... What's up, Nick?

**Nick Nisi:** Hey! How's it going?

**Sub Hinton:** Good! And second, we have Alex on the panel also, who from his latest tweet I see was having fun with teaching parrot noises this week. Alex, what's up with that?

**Alex Sexton:** Yeah, my son was in a Mexican restaurant on Cinco de Mayo, doing parrot noises, which are "Khalkha, Khalkha!", which also means poop in Spanish... \[laughter\] It was an interesting experience.

**Sub Hinton:** Alright, so without further ado, our guest this week joining us is Dylan Schliemann. He is the CEO of Site Pen and an open source technology innovator. Dylan is the co-creator of Dojo, which is a popular JavaScript toolkit that revolutionized the way that we thought about building web interfaces.

It's really great to have you on the show, Dylan, to talk about Dojo. Welcome!

**Dylan Schliemann:** Thanks, I'm happy to be here.

**Sub Hinton:** Dojo was started by people such as yourself, Alex Russell, David Schnitzler and others. Can you give us a brief history of how that came about? I think it was released in 2004, is that right?

**Dylan Schliemann:** Yeah, we started the project in 2004. Prior to that, we had another open source project called net Windows, and Alex famously sent out an email I think around April 2004 saying "What would you want from a next-generation DHTML toolkit?" We had a mailing list, and a number of people started responding and talking, and then a couple of months later Alex and myself and David started committing the first bits of code.

Roughly 2005 is when we first shipped a 0.1 release... But at the time we were really just trying to say "Hey, this JavaScript thing is pretty cool. We've worked hard at reinventing things, and it would be nice if we could treat the web as a serious application development environment", which at the time was fairly heretical.

**Alex Sexton:** Was it a mailing list? Wasn't there like an old forum that doesn't exist anymore, something like that?

**Dylan Schliemann:** Well, prior to that there was the WDF DOM forum started by PPK (Peter-Paul Koch), where we would discuss all the flaws of the DOM. That started probably in maybe 2001, and a lot of the people there have led to people who started working on Dojo. So yeah, it even goes back further than that.

\[03:56\] The name Dojo itself was suggested by Leonard Lin, who had a startup at the time. We just had terrible luck with naming; we got a cease and desist back in 2004 from Microsoft, which is kind of funny, because we're such TypeScript fans now, but at the time because we had the word "windows" in the name net Windows, so... We had to change the name on that. It's just a lot of good old history back then, when things were quite different.

**Sub Hinton:** So keeping in mind that there are folks who have entered the front-end development industry just recently, or even just a few years ago, they might be missing context about things like browser incompatibilities and animation challenges and things... Could you give us a little bit more information about the kind of issues that Dojo was solving pre-version 2, that are different to what other JavaScript libraries and frameworks are trying to solve nowadays?

**Dylan Schliemann:** Yeah. I mean, you have to imagine, this is a world where there was no GitHub, there were two browsers - IE5 (or 5.5) and early, early versions of Firefox. Safari hadn't been released yet, or was about to be released. Chrome was still a few years away. GitHub didn't exist... Almost all the modern tooling that we take for granted wasn't there. Firebug had not been released yet, and ES3 was kind of your JavaScript standard.

In many ways, it was like writing software in the dark ages. Your goal was to make something work in both browsers, because there was no mobile web at the time. And the idea that you were going to take this platform that most people kind of laughed and shrugged off as something you sort of treated as a DOM view layer, and that you were going to turn this into a real area where you would write applications was pretty crazy.

Alex and I and David were working at this company called Informatics - they're still around - and they had some pretty exceptional needs at the time; a lot of it would be vector graphics based stuff, large datasets, grids, charts, and all sorts of other advanced features that not only could you not do them with a dated platform, but no one else even really tried at that time.

**Sub Hinton:** So what kind of features in Dojo when it came out became immediately popular?

**Dylan Schliemann:** We were pretty heavily inspired by flex and Allow's approach to widgets, so we created probably the first major component library in JavaScript, ranging from form replacements, to grids and charts, to rich text editing, and so on. Most people I think were attracted to Dojo because of its widget capabilities. Beyond that, we just had a lot of nice improvements to the language.

Dojo 1 had something like 1,400 modules, so it was not a small framework at all. We had a build system, we had an early implementation of promises, we had various async patterns that are now taken for granted, but were not even conceived back then... Just lots of things that made the development of things better, and you can see lots of these things have influenced the standards that we have today.

For example, promises come from deferred, which were an early concept contributed by Alex and another person named Mark Anderson in the Dojo project... As well as another person who worked on a library called cheek at the time.

What else...? You could say Web Components are heavily inspired by Digit. The web has tried to get web components in place forever, but that's obviously been a big change.

A lot of the ES5 and ES6 features around just array operators, bind and just other features like that didn't exist, so libraries like Dojo popularized them.

**Alex Sexton:** Even real-time stuff too, right? Socket’d was Dojo...

**Dylan Schliemann:** \[07:59\] Yeah, Dojo had an early WebSocket implementation, and it had fallbacks to things like Forever Frame techniques, or long polling... Just because we needed real-time no matter what, so we started a project through the Dojo Foundation called Comet, that was basically one of the first open source real-time client server communication protocols as well.

**Alex Sexton:** I think that's why I initially got into Dojo a long time ago. Not that I was every super involved with it, but I think that was the only way you could get any of that done, and the documentation was good, and I had the fallbacks... It was really cool to see real-time.

**Dylan Schliemann:** Yeah, a lot of these things we just take for granted now, but they were really difficult to do. I remember sitting at OSCAN in Portland I think in a coffee shop with another engineer, and we were trying to figure out how to trick Safari into doing real-time communications through an iframe, and it turned out what you had to do was write to the DOM one kilobyte of white space intermittently, or else Safari would drop the frame connection after 30 seconds. So you would just randomly write white space junk.

Then IE - I think you had to write just any random characters, or maybe it was like 4 bytes of characters had to be written in. Just these really strange hacks you had to get working until WebSockets came to be.

**Sub Hinton:** It's like a weird front-end no-op, I guess, for keeping something alive. That's funny.

**Nick Nisi:** Jerold in the Slack chat says "I'm curious why Dojo has remained so niche all these years, yet is always highly regarded by anyone who has experience with it."

**Dylan Schliemann:** My short answer is I'm a better engineer than I am a marketer. But really, the thing is Dojo 1 was in many ways way ahead of its time, and so people who worked with things like jQuery and Moo Tools looked at us like we were just crazy, like "You guys are these rocket scientists, and I just need to be able to write some HTML with some light JavaScript."

I think John Resign once told me - and I took it as a compliment; I assume it was - that Dojo was like the R&D centre for the JavaScript ecosystem; that we would invent stuff and then everyone else would take good ideas from there and adapt them their own way.

My goal has never really been to say "Hey, we want to own the web." Instead, it's "We want to make a good influence on it and make it better", whether that's through using what we create, or what others create that might be inspired by it.

**Alex Sexton:** Niche is maybe a bit harsh as far as Dojo's usage goes. It was pretty extensive for a long time... I think before Dojo 2, in the last few years, certainly just like jQuery and other frameworks falling off but IBM and a few huge enterprise-level people who needed that large set of documentation support and widgets were using it... So I don't know; it certainly wasn't jQuery-level, but it was pretty popular.

**Dylan Schliemann:** At one point we were used in over 80% of the Fortune 500. It doesn't mean exclusively, just that it was very widespread in its usage.

**Nick Nisi:** I got involved with Dojo probably around 2011 when I started working with it at a startup I was at. That was right around the time of the big synchronous modules to AMD modules change that was happening; it was just a point release in the Dojo world... Can you talk about that a little bit? That seemed to be a huge turning point for the language, and of course, AMD got a lot of adoption in other frameworks as well.

**Dylan Schliemann:** Yeah... So James Burke was an early Dojo contributor when he was working at AOL, and then when he left to go to Mozilla, he found himself in a jQuery world, and he wanted to bring the bits and pieces of Dojo that he liked to the broader ecosystem. So between him and a few other people, the AMD specification kind of came to light. John Hand and Rawly Gill are probably the two others known at that time.

**Alex Sexton:** \[12:09\] I have a line in that spec, just FYI.

**Dylan Schliemann:** Oh, you do? Nice.

**Alex Sexton:** One or two words are mine.

**Dylan Schliemann:** That's awesome.

**Alex Sexton:** Very important contributions.

**Dylan Schliemann:** Absolutely. \[laughs\] And you know, the goal was to come up with a module format that worked asynchronously in browsers without needing a new language syntax, without needing a pre-processor to modify the code before it could run.

What happened is essentially around 2010-2011 that was kind of standardized or finalized. Dojo 1.7 was the first version of Dojo that switched from a more synchronous dojo. Define, dojo. Require style syntax to an AMD structure... And it pretty much revolutionized the way Dojo worked. It improved performance significantly, especially in IE, where it mattered most at the time. In hindsight, we probably should have called that Dojo 2, because so much changed at the time, and pretty much it was a major refactor of the framework, without really changing its capabilities at all.
**Alex Sexton:** If I recall correctly, Dojo didn't actually use Requires though. Didn't you all implement your own loader?

**Dylan Schliemann:** Yeah... You could use Requires with Dojo 1, but the idea was we wanted multiple implementations. Requires was pretty much intended for the jQuery community. The Dojo loader was also AMD-compliant. John Hand and Brian Cavalier had another one (I'm forgetting the name), but they've done a few as well.

**Nick Nisi:** Cujo, I think.

**Dylan Schliemann:** Yes, Cujo, there you go. And the idea was we wanted multiple implementations because otherwise we wouldn't know if we actually had a good standard to solve different use cases.

**Sub Hinton:** Dojo has been around for a while now... I'm actually interested in the authorship side of things, and what has it been like maintaining something that is so popular for so long?

**Dylan Schliemann:** I think if you look at the history of JavaScript libraries and framework authors, I'm probably the only one of the original bunch that still does this. I don't know why that is. I think it has a huge risk of burning people out. Furthermore, I think if you look at John working on jQuery, or Sam working on prototype, or Valerie on Moo Tools, or the founder of Ext JS, Jack Slocum and whatnot - there was a lot of burnout; a lot of people sort of -- and part of this, philosophically, is I think there are in general people that are perfect at one of three things: starting something new and kind of hacking it together and getting it working. The second type of person is once something is there, and it's clear, really adding to it, and then there is the type of person that loves to maintain things to perfection and will be there until the lights are out. It's pretty rare that you find one person that can sort of last through all three of those lifecycles.

The joke among the people I know is that I'm incredibly stubborn. Dojo has lasted as long as it has because I won't let it die, which is perhaps true, but perhaps kind of funny, as well... I'm not really one who's willing to give up on something or let it go. I'm going to keep it going. Furthermore, I have this real strong sense of duty to our users. If someone has taken the time to learn and adopt Dojo, I don't wanna just say "Oh, I'm bored with that. We're going to shut it off, and you can go figure something else out." So just kind of that sense of "You've made the investment in us, we want to make that to you" is what has really kept me going.

That said, the base of committers and contributors has changed drastically over the years. Almost no one who worked on the original Dojo (0.1) still works on Dojo today... But I think that's okay. I think people's lives and perspectives change, and their focus grows. Alex now is best known pretty much for trying to bring a lot of the goodness from Dojo 1 into the standards bodies through his work at Google.

\[16:10\] I think it's not so much about "Hey, we need to all work on Dojo forever", but how can we make the biggest mark or positive influence on the web?

**Sub Hinton:** That's really insightful. Nick, when did you come to start contributing to Dojo?

**Nick Nisi:** So in 2011 I was working on an app -- my first big challenge with Dojo was converting a 1.4 app to a 1.7 app, which meant completely changing over to AMD and learning that. I did that for a while at this startup; the CTO at that startup, John Christopher, he really was a big fan of Dojo, and grid was this other project that's kind of a grid implementation that's used in the Dojo ecosystem, and that was a really powerful tool for us in the app that we were building at the time.

Then it was from that grid project that I actually became familiar with Site Pen and started looking to them as my next adventure in my career. I've been there pretty much ever since, so for about five years now, contributing to Dojo 1 and Dojo 2, and teaching workshops, and things like that. So I've been really happy to be a part of this community, and I think that there's a lot for really cool ideas that have been improved upon from Dojo 1.

One thing in particular is the Digit system, with its declarative syntax for creating widgets that you can use, and having a whole lifecycle around that. That seems like it's an earlier implementation of what Dylan was saying, like web components, or maybe even like React components. I think that it could maybe be seen as like a building block to get to where we are today, which is really cool.

**Dylan Schliemann:** Yeah, it's fascinating... So the early data grid we had worked with real-time stuff, but it also was one of the first implementations of a virtualized DOM; it supported virtual scrolling, and virtualized rendering of nodes... And if you sort of look at Dojo's grid plus Be spin, which later became the editor that's now part of Amazon, the Cloud 9 editor - these were sort of the two early virtual DOM implementations that React was later crazy enough to say "We should do this for the whole page of your application." So there was a lot of cool inspiration there, but if you think about it, data grids were kind of probably THE reason people chose Dojo 1–we had a really nice, robust data grid, and we've had one for many years... And in the enterprise, every application kind of starts with the data grid.

**Break:** \[19:03\]

**Alex Sexton:** Alright, Dylan, I think we're going to talk a little bit about Dojo 2, but it actually kind of reminds me of a slogan that isn't anywhere near official, but... Wouldn't you say that Dojo 2 is kind of a rehash of something that Dojo 1 already did? \[laughter\] And to that end, explain the misnomer with the "Don't Ask, Don't Tell", and "Dojo Already Did That", DAD.

**Dylan Schliemann:** \[laughs\] That's funny. So I think it was the first ever Scoff, and Peter Higgins was there, and Pete's quite humorous, and pretty much anytime anyone would talk about something, he would quickly remind that Dojo already did that... And it kind of became the official meme of the first couple of Scoffs, that no matter what anyone presented on anything, you could say that Dojo had already done that.

Mostly, I think we had a little bit of a chip on our shoulder and that we did do a lot of great things before others, and the ecosystem is not necessarily great at giving credit for where something comes from... But honestly, that doesn't really matter, but it's just kind of one of those things...

It was funny, just a couple of years ago I finally met Add Osman in person after I think 10 years of talking online... This was before he had moved to San Francisco, so we're in the Google London office, and he pulls out his printouts with the "Dojo Already Did That" signs, and we took photos with it, which was really humorous... So every once in a while, someone just kind of brings that up and gives me a good laugh.

**Sub Hinton:** Alex, you mentioned Dojo 2, and I'm really looking forward to talking about that on this show. So Dojo 2 was just released super-recently, at the beginning of this month, is that right?

**Dylan Schliemann:** That is correct.

**Sub Hinton:** Tell us about this approach that you've had as a result of sort of bumping to a major new version.

**Dylan Schliemann:** Yeah... Really, the thrust of working on Dojo 2 has been over the past year and a half or two years, but I think I first started talking about the idea of Dojo 2 at a conference in 2010; so it's been many years in the planning, and in many ways it's kind of like when you're a musician, and you've had your first successful album, and it's really awesome, and then you don't know what you should do next.

What we realized were a few things. One, whatever we create, we have to support for a long time. Two, we want something to be appreciably better than what we've created before, as well as something that is strong on its own, so not just a rehash of what other people are doing... And something that is very modern and forward-thinking.

Around 2014 we thought we were on a good path, and then we saw that ES6 was finally going to land, and we had also started to take a strong interest in TypeScript, so we pretty much scrapped everything we were doing, took a step back and said "Okay, if we were to start a new framework today, what would we build and how would we build it?" Then we took a few years to iterate on that, and we ended up with something that is sort of core to our beliefs with Dojo, which is that we want to provide a very solid foundation for the enterprise, we want something that's going to scale up or scale down... But we're really aligned with the ecosystem... Whereas Dojo 1 kind of had to build everything in a silo, Dojo 2 can say "You know what, everyone uses Webpack; let's make this work nicely with Webpack", instead of creating our own build system.

We did make a huge bet on TypeScript. While frameworks like Angular use TypeScript, Dojo 2 is pretty much designed assuming that you are a TypeScript engineer, which is a pretty radical departure from what we had done before.

**Alex Sexton:** As far as the ergonomics of using Dojo 2 versus Dojo 1, is it still a similar -- like, there are Digits and there are these things...? I assume it's become more declarative, in like a more virtually DOM-y kind of way, all these types of things have been adopted... What are the main impacts of like day-to-day application development in Dojo 2 versus Dojo 1?

**Dylan Schliemann:** \[24:07\] Dojo 1 was really its own thing. We had our own module system, our own class-like system, our own widget system and so on... And part of that was because back in the day the standards process was not great; it was more black box, things would get thrown over the wall to you, as opposed to today, where it's very much aligned with the ecosystem and there's a lot of open participation.

So Dojo 2 is much different in that it's very focused with standards and common patterns. Yes, we have a widget system, but it's also built on a virtual DOM engine... One that we had originally started with using based on MEAT but that we forked, so we could get a bit more control over how we render widgets. It uses ES modules, we use Typescript, we have a number of core features...

In many ways, what we've tried to do is give you the flexibility of something like React, where you kind of have all of these nice, smaller pieces, but take advantage of the fact that we want a set of things that work together, in not quite as much as, say, Ember takes, where you've got everything designed only to work together, but... The idea is that you've got all these small pieces, like a good routing implementation and a good widget library and a good system for reactive components and so on, but we want them to be able to take advantage of actually being built together consistently and coherently.

**Alex Sexton:** I hear that. I think at any given time at work we're upgrading 10 dependencies in order to be able to upgrade 2 dependencies, in order to be able to upgrade one dependency.

**Dylan Schliemann:** Yeah... Site Pen, the commercial side of what I do - we do a lot of consulting work, whether it's with Dojo or React or Angular or whatever, and we kind of know the pain points of working with various frameworks and solutions, so it kind of frames our reference on "Okay, what would I do if it was just up to me? I'd create something where these pieces work together, and it's not quite as painful to get started or to upgrade."

We've also done a lot of fairly forward-thinking stuff. For example, one area where the virtual DOM paradigm kind of breaks down at times is when you're working with something, and in general, you just need to know something about that particular DOM node... So the typical way is to say "Alright, I'm going to punt on the virtual DOM here, just give me access to the node." That might be for animating an object, changing its dimensions, setting a focus event on it... Or some of the newer API's, like intersection observers and resize observers.

So what we've done is we've provided this pattern called a Meta. What it does is instead of you having to get the DOM node, we provide the properties for those common scenarios, so that you can still work with those behaviours in a reactive manner.

So what makes Dojo 2 pretty interesting to me is we've looked at like hundreds or thousands of little tiny, minor pain points or inconsistencies like that, and really tried to refine them and clean them up and make them feel more consistent.

**Nick Nisi:** Yeah, I think that that's one of the biggest focus points for Dojo 2 - really a focus on making things easier for the developer that's using it; so a big focus on developer ergonomics, with things like that in the Meta project, and other things. You mentioned that we write in TypeScript, where we assume that the users are TypeScript users, as well.

We also write all of our modules with TypeScript's strict type-checking turned all the way on, so that it's keeping us honest, and it's making for the best possible experience for the users of the framework.

**Dylan Schliemann:** Yeah, the TypeScript team jokes that we're stricter than they are, because they're not fully strict in their authoring of TypeScript itself. \[laughter\]

**Alex Sexton:** Doesn't that then leak down into your strictness, though?

**Dylan Schliemann:** \[28:13\] No, no... I'm mostly just kidding. I mean, they're very good engineers, but there are just a few places where they can't be fully strict, but we are. And it is a little more painful, but the goal is to make it, so our end users don't have to suffer for us not getting things just right.

**Alex Sexton:** When you talk about them not being strict - it's in their own parser...? I guess I'm confused how -- if you're checking with their parser, and they're not strict, it seems like it would follow that you have the same... I guess I'm confused.

**Dylan Schliemann:** It's a very meta problem, but... So TypeScript itself is - you know, like, most languages are authored in their own language, so it's one of those interesting meta problems. I just mean that parts of the TypeScript compiler itself are not completely strict, and that's okay... But for us, it's a badge of honour to say "We're fully strict, in that we're going to catch every possible mistake that you might make, that the compiler could enforce."

**Sub Hinton:** So I was taking a look at the Dojo 2 website, and just having a look at the first impression of what is important to you as an author of Dojo, and the Dojo community in general... And one thing that popped out to me that I found unique compared to other modern frameworks is the word "inclusiveness." One of my personal passions is accessibility, so I was really excited to see that that had been brought to the top right on the front page. It talked about how internationalization and accessibility is built into Dojo, and the support of that. In my experience working with other framework, I've seen accessibility teams spin up from the community in order to sort of address some shortcomings for accessibility in other frameworks. That is clearly not a thing for Dojo 2, so can you just tell me a little bit about how internationalization and accessibility became a priority when you were authoring and releasing it?

**Dylan Schliemann:** Sure. So for Dojo 1, we were the first -- okay, so back in like 2005-2006 we were at the first Ajax Experience conference. And we were on a panel, and the question that people kept asking about all this new Ajax stuff was "But is it accessible?" and everyone just kind of hung their heads in shame and said "No. That's an area that's ripe for innovation."

IBM got involved at a very early stage shortly thereafter, and Becky Gibson and her team were part of the ARIA effort and part of making Dojo the first library that supported that standard. So for us, it's just been something we've done forever, and in parallel we also supported internationalization back then, too.

Stepping forward, that's something we're known for - we want what you create to work for all of your users. That might mean ranging from blindness, to foreign languages, to just having better keyboard shortcuts... You know, the full range of "How do you provide a better experience for all of your users?" So fundamentally for this, internationalization was a fairly different beast than accessibility. Internationalization - we leveraged a JS Foundation project called Globalize, and then provided that in a modern reactive manner. Basically, all of your out-of-the-box components that you might author, you can easily hook them into an internationalization system and get all the nice things that Messageformat.js and Globalize give you.

Accessibility is about a few things... First, the components or widgets that we create are accessible out of the box. They comply and conform to the best standards that are out there, and that we've gone through and done that. Sarah Hi gley leads our efforts on Dojo 2 around accessibility.

\[32:11\] Then it's about providing good guidance, good documentation information about how we do that, so that engineers don't just turn around and break accessibility in their own efforts. Then we do also provide some automated testing for the things you can automate. Obviously, you cannot automate everything around accessibility, but there are a few good tools - there's axe, and there's Tenon, and a few others, and our Intern testing tool hooks into those to basically say "Hey, these are mistakes that you might make that could break accessibility." You can automatically test for them in your code base, and at least be notified "Hey, this first passive stuff that you could do to break accessibility, you shouldn't ever do, because the tests will tell you otherwise."

**Sub Hinton:** Why do you think that other JavaScript frameworks or libraries have not really tried to have this built in from day one?

**Dylan Schliemann:** I think - to be nice, but maybe not nice... I mean, a lot of people are impatient, and they just want to get things out the door. Obviously, that's not us, given how many years it really took us to feel like we got Dojo 2 right... And we still don't feel like it's perfect, but we feel like it's solid enough that we can stand behind it. But I think in general people just aren't patient enough to say "Hey, I'm going to solve all of these problems as perfectly as I can before I'm going to thrust them on people."

I've been around the ecosystem long enough that I know that I don't have to push something out first, I don't have to race to get it done and sacrifice the things that matter.

**Alex Sexton:** I think it partially comes from the philosophy of the Dojo team of making a bunch of tools that work together. I do agree with the idea that the virtual DOM implementation, or a component implementation can be separated out and tested separately from a message format implementation or an internationalized component implementation... So splitting those out all seems good as far as code goes. The fact that Dojo already ships everything, all that works together, it kind of makes sense that they might have all these tools that work together, versus someone who's like "Alright..." Like, when React came out, I remember being very underwhelmed; like, this looks cool, it looks fast for the view layer, or the render function of the view layer that I already have in my massive application, right? It just did this one very small thing, and everyone just kind of piecemeal put their own -- you know, for the first six months of React, everyone was just adding it to their backbone applications as the view layer... So I think it is a different approach, for sure.

**Dylan Schliemann:** Yeah, it's definitely a bit more holistic. I think in general accessibility is still challenging, even for HTML-type work, which makes it a bit more abstract for virtual DOM systems... I mean, I think there's a lot of promise and potential with the accessibility object model (AOM) stuff that's being done; it could potentially make this work a lot more smoothly, so that's pretty promising as well.

But yeah, I think if you're designing systems that work well together, you're less likely to introduce things that break your approach. There's the classic example of "Hey, I've pulled 20 widgets from 20 different places, and I don't know if all of them are going to be accessible", whereas if you release a set of widgets together, and you've tested them all for accessibility, you could make the promise that "Hey, we may not be perfect, but we've put serious effort into thinking through these problems and done our best to do that, and then accepting fixes and releasing them quickly where we failed."

**Sub Hinton:** \[36:01\] What kind of things do you think would help with that fragmentation issue that you just mentioned "Well, Dojo is a collection of things that were worked on and that were made to be consistent"? When you have a whole community making lots of different types of components, such as when you can just NPM install a React component, for example, or a Vue component, or an Ember component, how do you think that we could convince the community be more mindful of these things? How do we sort of stop that fragmentation of the different gaps that we see as far as accessibility goes?

**Dylan Schliemann:** One of the challenges we've had as an ecosystem is what I described as the GitHub effect, and GitHub obviously is one of the most amazing things to happen ever to software engineering... But it's also a bit of a curse, in that before GitHub it was actually a challenge to start an open source project; it required effort in actually setting up a project and setting up source control... And today it's so easy - you just create a URL and go to it and start a project... And what it's done is it's reduced the barrier to entry of creating your own framework, rather than the effort to contributing to someone else's. So there's a lot of value in getting people to actually work together and collaborate on things, that gets lost when everyone just kind of does their own thing, in their own way. And obviously, there's a use for both, because you need innovation and creativity, and that only happens when people try and experiment and fail, and eventually find a nice path forward...

But you really do need people to decide "Hey, it's worth the effort to get together and collaborate and come up with something that works together, and is consistent, and has some common standards and guidelines." It's both end user accessibility, but it's also developer accessibility. If I have to learn slightly different APIs for each component I'm using, that's tedious and that's reducing my own experience from getting my work done.

So there's just a lot of need to get people to collaborate and communicate and decide; it's a challenge, and it's one of the things I feel like Dojo was quite good at early on, but I think every project struggles with this. I don't know if I have a good answer for it, so much as if you're aware that the problem is probably human communication, you can maybe look at yourself and say "How can I make this better?"

**Alex Sexton:** It also seems like the projects -- React doesn't need to be building necessarily the internationalization layers or the accessibility rules, since they're not releasing their own widgets... But it seems like they could release a set of standards of like "Here's how we would expect this to be, and here's this certification process" - not a real one, but just like "Here's a thing you can run your thing through; if you run it through this, we'll check for the following things, and then you can add this badge to your GitHub page... Just generally implying via docs and words what would be expected seems like it would go a really long way for at least the most popular widgets to just-- people would PR that.

I think there's a lot we could do, even in the current fragmented system, to standardize more on what's expected for internationalization and accessibility.

**Sub Hinton:** Speaking of components, let's talk about Dojo 2's widgets. I saw in my research that they're designed to be adaptable as like new open web standards are introduced, and they're supposed to be just more forward-thinking than components of the past.

How do you ensure that going forward, and how do you design these different widgets to be adaptable?

**Dylan Schliemann:** So we've taken a few interesting approaches. The first is everything in Dojo 2 is easily imported or exported as a web component, and that's just how it works out of the box. So it's not that Dojo 2 widgets have to be used as web components, but that they easily can be... As well as being able to pull in web components from elsewhere.

\[40:16\] Obviously, this is just the custom elements portion of the web components spec, but we think that's really important because if you can reduce the barrier of entry between frameworks in regard to how components are authored and used, that's really useful. It also is a standard way to say "I'm registering a custom tag that has these properties and these attributes and this behaviour."

Now, web components aren't perfect. There's a challenge in sort of cross-component communication, cross-component data sharing... They're really designed to kind of be standalone. But you take advantage of the standard that's there, and then you figure out how to augment it where you can. That's kind of the foundational piece.

Then what we've done on the styling of components is we've said instead of really focusing on the sort of pre-processor ecosystem that's been in place, let's look at CSS next and use a library called PostCSS. It's sort of what Babel is to JavaScript, it is to CSS. It takes the sort of emerging CSS standards and back-compiles them to CSS that works today. The idea is to really get people aligning the way they author their CSS with the standards that are coming out or that are emerging, rather than sort of jumping into this alternate ecosystem that is useful, but not necessarily aligned with where the web is going.

And then really just looking for features that solve problems that people have had with components over the years. My favourite is probably the intersection observer API. This kind of has two main use cases. One is this sort of infinite scrolling challenge - your Facebook feed, or your Twitter feed, or whatever... And what it does is it basically determines if something is in the view of something else. Then the other use case for it is potentially data grids, or things where you've got large lists, and you need to scroll them. That is potentially a much better way of solving this problem that we've had to solve through large, large blocks of JavaScript code to handle all the use cases that might be possible.

So we just kind of keep following the WING list, TC39 efforts, WHAT, and kind of look for things that feel like they're going to make the web ecosystem better, especially for how HTML, CSS and JavaScript interact together, and then roll them up and keep iterating on that.

We also look for things we can do that make the authoring experience better. For example, we have this system that uses CSS modules and TypeScript together, so that when you're applying a class name to a component, you can only as an author create valid TypeScript if you include a CSS class name that was part of that component's CSS file. And we do that by just importing a TypeScript definition file that is automatically created from each CSS file that's related to each component.
For example, if I'm in my Hello, world widget, I've got a list of CSS class names that can be autocompleted as it's time to style them in my JavaScript code. That might sound like a small thing, but it's just one of those things that saves you five or ten seconds every time you need to figure out which class name to apply to a component, because your IDE is gonna sort of lock you into that list of ones that you've scoped in the context of that component. So really just kind of looking at how all these pieces fit together, where we feel things are going, and just kind of trying to keep that direction going where the web is going in general.

**Break:** \[44:00\]

**Sub Hinton:** So for our last segment today Alex was going to start chatting with Dylan about web standards and foundations, and you just had a few questions for Dylan around that.

**Alex Sexton:** Yeah. So Dylan, you have been involved in much more than Dojo in the past, specifically around standards stuff... One such interaction that I had with you is detailed in a talk that I gave around CSS colours.

**Dylan Schliemann:** \[laughs\]

**Alex Sexton:** I was excited to find out while I was researching the history of CSS colour names that Dylan had many of the same questions that I had doing that research, and unfortunately he had asked them 11 years prior, and never got an answer. So I eventually found that information and replied to WWW style mailing list... But that was in 2001, when CSS 3 was being kind of ratified. I hadn't realized that you had also been that deep into standards that long ago. 2001 is pre-Dojo... Yes?

**Dylan Schliemann:** Oh yeah, definitely a few years before.

**Alex Sexton:** So you were involved in that mailing list for years prior to that, I guess... You had even compiled all the different places that other people were confused about CSS colour names, and linked them in your very informative post... So tell me a little bit about your standards history as well.

**Dylan Schliemann:** Sure. I think it was around '96 when I first really got into JavaScript, so pretty early in the days... And I had read most of the books that were out at the time, and honestly there weren't a lot of other resources available yet about JavaScript, so I started joining the various standards mailing lists, which at the time were the Style List, the DOM List and the JavaScript List, and really just started participating in... I felt like the best way to understand the web platform as a whole was to participate in the standards process. So the time, frankly, it was a bit -- unless you were paying to join the standards body, you really didn't have a say, but you could still participate and figure things out and ask questions.

Standards are mostly a part-time job for a few engineers of each of the browser vendors at the time... But it was really fascinating to me to say, "Okay, how does this really work?", and one of the first things we did at Site Pen is we tried to create something sort of like Google Page Creator... So basically a web-based HTML, CSS and JavaScript editor. But this was back in 2000, so it was a little different from trying to do it in 2010, or something... And one of the things I wanted to do was figure out how to make it easier for someone who had no programming experience try to style a page, which led me down the colour name path. I actually had proposed an alternative way to name colours at the time... There were a lot of cool ideas that didn't go anywhere, but were still interesting to think about.

Today, standards are amazing compared to back then. I mean, they're not perfect, but the open process, the way we handle things on GitHub, and talk through them publicly, and the growth of TC39 and WHAT... I mean, Ian Dickson probably deserves the biggest amount of credit for sort of changing the way we think about the standardization process as a whole.

In the early Dojo 1 days I kind of had the feeling of "Standards are broken. We'll just do whatever we want." But today's standards feel pretty good, so we try to align to them much more closely.

**Alex Sexton:** \[48:03\] Around the same time Dojo was released - I guess a little while after, but... I know I've talked to Alex Russell a little bit about this in the past, but you guys felt pretty strongly about code rights and licenses and licenses and things like that, to the extent where you created a very hands-off, but protective entity, which was I think one of the first foundations that I had known of. Obviously, there was Apache, but it was like pretty early on. So tell me about the history of the Dojo Foundation.

**Dylan Schliemann:** Yeah, so after getting that -- Alex got that cease and desist over the name net Windows; it was pretty clear that we did not want to be the legal entity for a framework... So we talked with some friends - we knew Martin Cooper, who was the vice-president of the Apache Software Foundation, we knew the president of the Python Software Foundation... And we just kind of asked them a lot of questions and realized it wouldn't be that difficult to start a foundation that was focused on JavaScript, so we did. At the time it was called the Dojo Foundation, because we weren't particularly clever with naming things... And for us, it was a huge, important point, which was that the code that's there, people can use; they can trust it's not going to be pulled out away from them, the licensing is not going to change on them.

We said "We're not creating fake, free open source software..." This was a pretty big deal at the time. And also, one company doesn't really control the destiny of a project. The idea was to reduce the barrier to entry for other organizations to contribute and get involved, and I think the foundation is what led early on to companies like AOL and IBM and ESR and Sun and others at the time, to say "We can contribute to this, because you've gone through the effort to make sure that we're not basically contributing to some other company's IP, but instead we're contributing to this shared ecosystem."

**Alex Sexton:** I think that still ends up being an issue today. A lot of the fear and uncertainty and doubt around React has to do with clauses in Facebook's ownership of that code. There were also a few other foundations that emerged... Give me that history, as well.

**Dylan Schliemann:** Yeah, so over the years Dojo had taken on a number of other projects, including one of yours, and then the jQuery Foundation was founded, and it had jQuery and some other projects... And then I think about three years ago Colin Snover introduced Kris and me. Kris Workers was being the president or the director of the jQuery Foundation. He said, "You know, it'd probably be simpler if we just had one foundation that we could manage and take care of, instead of two...", especially since a lot of the projects had strong overlap. So we had Requires and Lodash, which were quite popular in the jQuery community, and vice versa. So we merged, and then sort of rebranded and relaunched just the JS Foundation about two years ago.

Basically, the idea is it's a home that provides support and protection for projects. The idea is not to fund development of projects. That kind of gets into some legal grey area around "Is this an open source foundation or is this a contractor in the middle?" But instead, it's really just focused on providing the support for open source projects around community and legal rights, and support that frankly most open source committers are not perfect at or don't want to think about, so it just kind of gives them the support they need around those areas.

You know, my hope has always been that the foundation would encourage projects to collaborate more, instead of reinventing the wheel. For example, with Dojo 2 we leverage the Pointer Events Polyfill, which is a JS Foundation project. We leverage Globalize, which is another project, we leverage Intern, which is the testing framework that's part of the foundation, and we also use parts of Grunt for our development tooling...

\[52:09\] So the idea is really not to say "Hey, all these projects should become the same", but if they have clear boundaries and API approaches, can they be used together nicely?

**Alex Sexton:** As far as like if I'm a person who maintains an open source library that's not huge, but a lot of people use my calendar implementation, or my something implementation... What do you suggest they do as far as licensing? Obviously, there are very specific licenses they could choose, but suppose like foundations how they manage the same minefield?

**Dylan Schliemann:** It's a challenge, because one of the goals of the foundation is not to become the graveyard for abandoned or ugly toys anymore, right? So it wants to have projects that are thriving and well-supported. So if you're a tiny project, it's hard to say "Hey, I want to join the foundation", but it might make sense to join a project that's part of the foundation, sort of thing.

Licensing is one of those things that everyone has an opinion on, but really there are two types of licenses - there are those that are permissive, and those that are a bit more control-oriented, and they both have their purposes. For example, Linux is the champion of the GPL-style license, and I think it really needs to be... Then most JavaScript libraries or frameworks are more along the lines of either MIT, Apache or BSD license, which are all roughly the same. The Apache license is probably the least ambiguous, though it's the longest, so people tend to choose the MIT, because it's the shortest, so it's less to read... But I think any of those three are viable and reasonable to use.

The goal is you choose a license based on the behaviour you want. The license that Dojo chooses is the BSD or the Apache 2, and we choose that to encourage adoption; we're not trying to control people and force them to contribute back. Obviously, if you have a bug fix, we'd prefer it become part of the framework, rather than you having to maintain a forked version of Dojo forever.

When you choose a license for your project, you very much need to decide what you want your project to be, and try to find a license that's going to lead you in that path.

**Alex Sexton:** One thing that was pretty different when I started working on or committing to Foundation projects was the Committers' Agreement, which is separate from the usage license... And I found that I think that's where a lot of open source projects don't have any corollary to the Foundation projects. So I doubt it's even legal, but a lot of times in my small open source projects I'd say "You can use this under the MIT license, but you can commit to it under the Dojo Committers' Agreement", or whatever. Can you explain more about that?

**Dylan Schliemann:** A contributor license agreement is basically you've contributed some code, and you're saying "I authored this, or whoever paid for this to be authored approves of me contributing this code." The idea is to make sure that we only accept code that we should accept. Now, it's not a legal guarantee that there'll never be a problem, but it's the closest we can get to saying "Hey, we've vetted the source of this code, and it's been contributed as it should be."

For years actually the Dojo Foundation said "Anyone could just follow the rules of the Dojo Foundation and contribute for code, even for their own project, in that way." The JS Foundation works a little differently in that it has basically a CLA bot that when you open a PR, if you haven't committed a PR to that project before, it makes you sign a form real quick in the browser that says "Hey, I know what I'm doing. I can contribute this code and I have the rights to" to streamline the process, but that also means it's kind of limited to the projects that are part of the foundation, because it needs to hook into that system. But again, it's just having a CLA process that says "I agree that the code I can contribute is mine to contribute" is really important.

**Alex Sexton:** \[56:12\] Yeah, I've definitely found that almost tends to be the place where I worry the most about getting code that looks good to me, but actually someone didn't have the rights to actually give it to me. That can be scary.

**Dylan Schliemann:** Absolutely. Just doing everything you can to make sure your users aren't going to be sued for using your project is a good thing, and CLA is one part of that process, where the code you're accepting, the person who has submitted it has at least declared they have the rights to do that, is really powerful.

Before I forget, I obviously forgot one Foundation project, which is a big one for data too, which is Webpack (which I mentioned earlier). Obviously, Sean Larkin and their team are doing really great work on Webpack, and we've had a lot of success with that as well.

**Alex Sexton:** I think Webpack certainly was not the frontrunner; when it came out there was a lot of competition at the time, and then suddenly it just took off, which is cool. When we're talking about standards, we're talking about what standards are you excited about either making it to browsers, or becoming standardized...? What's the cool new stuff?

**Dylan Schliemann:** We're pretty cautious in that we won't really embrace something until it's pretty far along. For example, we got burned a little bit on object. Observe a few years ago, which reached level one, and we had kind of shimmed it and fixed everything we thought was broken with it to make it usable, to then have it discontinued as a standard... So in many ways we look at things, but we don't really probably pay too much attention to them until they're the equivalent of stage three.

Obviously, we're pretty heavily aligned with TypeScript's feature set as well. TypeScript is interesting, because a lot of people will say "We'll just wait for that to become part of the TC39 process, and what a lot of people don't realize is TypeScript can kind of get away with adding features that are around code integrity and authoring because they're all going to be removed at runtime anyway. It's kind of liberating for them to not necessarily have to worry about the features that are going to go into the language, but that are more like developer time tool, language augmentation features.

So I don't know that we're clamouring or waiting for any specific features at the moment, so much as every time we see something cool -- we added Resize Observers just a few weeks before the final release, because there was finally a good shim for it, and native support had finally landed in Chrome, and we were like "Well, we can take advantage of this now."

So it's kind of the "Can you be nimble?" ... but you don't want to be so nimble that you adopt things before they're ready, because then you're going to increase the risk of them being divergent from the standard itself.

**Alex Sexton:** That makes sense. I guess I was trying to get a little bit of your personal excitement, but...

**Dylan Schliemann:** I mean, I have some, but it's like I've had my heart broken so many times, I'm very cautious... \[laughs\] We have a shim for Observables; the equivalent of RxJS Observables, but there's like one small tweak... About two or three years ago it was proposed as a TC39 standard, and as far as we can tell it stalled, because it computes with streams, even though it's fundamentally a lot simpler than to work within streams.

So we have this sitting in Dojo Shim; it's there, you could use it... But we've ended up not really using it ourselves. Instead, what we've done is the things that should be observable in Dojo 2 are just observable by default, so we haven't actually ended up using the API much at all. But when we first thought it was going to be standardized, we had switched to having everything use it, and then it just kind of took its toll.

So it's kind of like we're very excited about a lot of the TC39 proposals around additional async behaviours, and around adding features to the class system, or trying to streamline the way classes work so they don't get abused, and so forth... But until it's like right there, we're just very cautious because we don't want to get burned again.

**Nick Nisi:** \[01:00:16.26\] Dylan, can you enlighten us a little bit about what you see as the future of Dojo 2? Now that we've got the second version release out the door, can you talk a little bit about where we go from here?

**Dylan Schliemann:** Sure. In many ways, getting the .0 release done is kind of the point where you're like "Okay, I think what I've got is good enough and substantial enough that people should start using it", but it doesn't mean it's complete. I would say Dojo 1 was probably four or five years from 1.0 until maybe 1.7 or 1.8 where it felt really complete, from my perspective.

We have a lot we want to do around widgets, we have features we want to add around -- things to add feature parity with Dojo 1 even. I mean, Dojo 1 was so big that there are many things we just haven't tackled yet. We haven't really started down the data grid path for Dojo 2 yet. There are a lot of nice things we want to do around PWAs, we've done a lot of proof of concepts for that, but we don't yet have our PWA tooling in place that kind of makes your application automatically be a PWA.

There are a lot of patterns around data... We have an implementation called Dojo Stores that is your sort of state management store, and it's a little bit (in my opinion) easier to work with than something like Redux... But what we don't yet have been the sort of patterns of "Hey, just hook this up to a RESTful endpoint" or "Hook this up to a WebSocket and get data into my application", some of those ease of use things...

There's a lot to do, and we'd love contributions, but at the same time if you wait until you have everything perfect, then you'll never ship, so you'll have to kind of say "Okay, we've got enough that's substantial here. Now this opens the door for a bunch of other things."

We want to get a nice design system done. Design systems are kind of a way to say "Hey, here's a set of consistent UI patterns and widgets, and how they work together and how you use them..." So just a lot of things like that, really.

**Nick Nisi:** Can I poke more around the PWA topic? What are a couple of quick high-level things that you're thinking about when it comes to PWAs?

**Dylan Schliemann:** One of the goals of Dojo 2 in general is that we want to do things right out of the box. For example, a couple of features I haven't mentioned - I'll get to your question in a second, but let me set the preface for it - is things that are the right way should happen as automatically as possible.

\[01:02:42.24\] For example, we have this build time rendering system that does code splitting and rendering optimization, so what it does is it essentially delivers your initial view optimized as much as possible. Your HTML and CSS for your first view are rendered in line, and the code splitting happens automatically based on what features of your application you need at what point, without you have to write different code to do that... So instead of saying "Hey, how do we enable code splitting?", we just do it for you. Or instead of saying "How do we make that first paint as fast as possible?", we just do that automatically, out of the box.

So the same thing is true with a PWA - instead of saying "Hey, how do I make everything into a PWA?", we say "Okay, how do we set up your manifest file? How do we set up all the different features you might need to have an impressive PWA out of the box?" and provide that as part of the build process, so that every app you create with Dojo 2 would automatically be a PWA, would be the goal.

Now obviously, there's more you can do than that, but at least removing that sort of scaffolding, boilerplate effort up-front is a big win; it's something we've done proof of concepts around, it's something want to land fairly soon, once we kind of sort out exactly how we want to do that.

**Nick Nisi:** And the way we actually do that is kind of -- I don't think we really mentioned it, but we have a robust set of CLI tools that help you get up and running with the Dojo project and sets up the build for you and does everything for you, so you don't have to mess around with a really complex Webpack config or anything like that. You don't even have to realize that it's using Webpack, and then you can build and serve your application in development, and then it'll automatically rebuild on every change, and then also build for production from there.

So the PWA story kind of goes along with that, with "What can we provide from the CLI tooling to make it as simple as possible to take your app and convert it into a PWA, or to deliver it as a PWA.

**Sub Hinton:** That is very cool. I'm very excited to see the future of that as well. So I want to take this moment to thank Dylan so much for coming on JS Party and sharing past, present and futures of Dojo, too.

**Dylan Schliemann:** Thanks for having me, it was a lot of fun.

**Sub Hinton:** Jerold dropped a rap into the JS Party Slack chat, and I see that there's been some encouragement for me to do that rap... So Jerold, this one is for you:

’D to the Plan, Skin to the Mann,

Here comes that Dojo that's going to make you a fan!
Big version 2, who saw it coming?
Two years later going to get you up and running...!"

Thanks for tuning in, everyone. See you next week!
