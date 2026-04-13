**Kevin Ball:** Hello, JS Party people, and welcome to another week of your favourite/my favourite podcast about JavaScript and all things web. I'm Ball, I'm your host this week. Joining me today is one of our newest panellists, Jessica Sachs. Jessica...

**Jessica Sachs:** Hello.

**Kevin Ball:** Excited to have you. I don't know that we've been on a show since she became an official panellist, though we did have one together back a while ago, I think... Jessica did the organizing for this. She set us up with two amazing guests to talk about some of the hot news in the ecosystem today... I'm joined today by Mink Zeke, from I believe the Angular team... Is that right?

**Mink Zeke:** Yeah, I'm working on Angular as well, plus also this effort that we'll be talking about today.

**Kevin Ball:** Yes, Angular and Win. And then we have Latin Rajasthan.

**Latin Rajasthan:** Hello. Yeah, nice to be here.

**Kevin Ball:** Let's start with the two of you maybe introducing yourselves a little bit, your background and how you got into this place that you are today, engaging in the merger of Win and Angular. Mink, do you want to go first?

**Mink Zeke:** Alright, your. So currently, I work on Angular at Google, where I lead the product roadmap and the developer relations. Previously, I was working on a startup that Coursera acquired back in 2018. And actually, back there I was not using Angular at all. We built the entire frontend in React... But I kept contributing to Angular in my spare time, because it's my passion project. So I get to do that full-time now.

**Kevin Ball:** Awesome. And Latin?

**Latin Rajasthan:** Yeah, so I joined Google about 12 years ago now. Initially, I was on a product team; I was actually working on Google Plus, and we started using Win. And it was pretty exciting, very new, a different way of building websites for me at the time. Over the years Win grew in popularity; a lot of large products at Google, like Search, started using Win. However, there were a few products that kind of had picked different stacks. And one of the big ones was YouTube. They had picked a different stack, because they weren't doing server-side rendering, and some of the core value propositions of Win, like reusability, are less appealing if you're not doing server-side rendering.

And so the requirements kind of started changing for Win, and what we realized was applications that are wanting to use Win because it serves, like, it's a proven, scalable product, are now kind of looking a little bit like Angular applications. And then similarly, Angular applications, teams that were using Angular started asking me for features that had more to do with SSR, and so on. And that kind of brought us to this point here, where we're trying to merge the two frameworks instead of just trying to compete and see who can do everything better separately.

**Kevin Ball:** While many of the people on the show are familiar with Angular, or should be, since it's been around a while in the public eye... We've had a couple interviews recently with folks from the Angular team... When this news came out about Win, I and I think probably everyone else out in the world who was not at Google was kind of like "Wait a minute, what is Win?" So can you maybe give us a little bit more of like TL;DR what is Win, and then we can dive into some of the key points?

**Latin Rajasthan:** Yeah, sure. So Win is a web framework which kind of organically evolved from building blocks that already existed at Google about 10 years ago. If you turn back time 10 years ago, and try to remember what Google was doing, it was all about social. Facebook had just completely taken off, and Google was kind of realizing that they don't really have a great social play. YouTube was kind of doing well, but back then YouTube accounts were completely different, and there was really nothing that Google was kind of getting in terms of social graph. So G Plus was one of the largest projects that I've actually ever seen at Google in terms of like a web front end.

Mobile had started taking off around 2008, but working on the website -- like, all features typically started on the web. Very rapidly, G Plus was growing in size to become the largest website ever. And there was a lot of need to break it down systematically into smaller modules, so that you're not loading all the JavaScript just to render the home screen, or something.

\[08:09\] And so this framework, Win, started coming into existence from this idea that if you depend on developers to systematically keep chunking the code, or code splitting, they're eventually going to get it wrong, because either they forget to do it, or they make suboptimal decisions. And so what we need is a framework that systematically chunks the code, and then has a system to load only the code that's required, depending on what is rendered on the page.

**Jessica Sachs:** So Win is a front end framework that was born out of the need to performantly chunk frontend code? That's correct, right?

**Latin Rajasthan:** Yeah. This was one of those foundational kind of inspirations for Win. There's maybe like a couple more, but this is pretty key.

**Jessica Sachs:** And that was because of the just sheer size of Google Plus... Is that about right?

**Latin Rajasthan:** That's right.

**Jessica Sachs:** Alright, cool.

**Latin Rajasthan:** And other products at Google, like search, have a similar kind of problem. 10 years ago, search had started adding more and more widgets. Typically, in search, the most interactive thing was the doodle, right? Everyday changes, and you can play around with it, and so on. And then on the results page, it was still a few ad links and 10 blue links. But now, if you go to search, you can't recognize it. It's just like interactive widgets all over the place. Depending on the query, you get a little --

**Jessica Sachs:** You mean like flights and stuff, and like calculator, all those things?

**Latin Rajasthan:** Yes, those little widgets that show up depending on your search. If you search for a restaurant, you can see information about it, and so on.

**Jessica Sachs:** Do you call them widgets internally?

**Latin Rajasthan:** \[laughs\] There are a lot of different names for them. I'm just using widget here, because... Cards also. We some sometimes call them different kinds of --

**Kevin Ball:** Naming, the hardest problem in computer science...

**Jessica Sachs:** I just like to know \[unintelligible 00:09:56.00\] I hear that there are a lot of Wizard of Oz jokes, because it's called

Win. I know that's not technical, but I still like the lore. Speaking of lore, I'm trying to build the timeline... So when was Win created?

**Latin Rajasthan:** I would say around 2014. Yeah.

**Jessica Sachs:** Okay, so Angular came first, and Win came second.

**Mink Zeke:** Yeah. And for different goals also. They were targeting different use cases, I guess. Angular wanted to remove the boilerplate and create a very expressive framework for building web apps, so that it can make developers productive.

**Jessica Sachs:** Where was Angular used at first? Was search first built in Angular, and then cut over to Win? Or what was the migration path between what was there before?

**Mink Zeke:** Yeah, well, there were some other technologies actually, that I'm not familiar with. That was like back in 2010 or so. I think one of the first projects that Angular rebuilt was Google Feedback. I think they reduced the number of source code lines with something crazy like 90% or so after they rewrote it in AngularJS.

Angular existed in a different organization as well... So I guess that's a big difference compared to how the different frameworks team were operating back then, and how we operate right now. We were associated with different products. And currently, we're in an infrastructure team where we can work closely together, and talk to each other easier. Angular was within Google Ads, which is a good position to be in also, because this is one of the biggest revenue streams for the company.

**Kevin Ball:** So some of the things you were talking about in regard to Win made me think about another framework we've had conversations about on the show... So you were talking about sort of the desire to do chunking automatically... And contrasting to many of the web frameworks out there, where you have to work hard to keep it performant, wanting that performance by default. You also mentioned the word reusability. Both of those brought me back to conversations with Misdo Every about Qlik. And before we even get into the technical pieces, I'm really curious, to Jessica's point about the lineage here... Because he was involved with Angular, he was clearly inside Google... Qlik came after he left there, but was he involved with Win at all? Are these concepts and lineage coming together there? Or are these independent attempts at the same problem?

**Latin Rajasthan:** \[12:21\] Yeah, so I actually met Misdo recently, and learned what I'm about to share here. So this is not the first time Win and Angular are trying to merge. It was kind of known that about maybe 2019, when the teams actually kind of organizationally moved really close to each other, and desire was expressed that we're going to try to merge them. And Misdo studied Win very, very deeply at that point, to try to understand if the two frameworks can merge. And he kind of concluded that, at that point, the frameworks were very different, and actually very hard to converge \[unintelligible 00:12:55.28\] was not clear to him. And he shared with me that that was the inception of Qlik; when he was writing those papers to try to understand Win and talk about convergence, that's when the seeds of Qlik were sown in his mind.

**Jessica Sachs:** So where I met Latin and Mink was actually about a month ago at JS Dev -- what is it, Dev World, or what was the conference's name? I'm going to mess it up.

**Mink Zeke:** Yeah, Dev World.

**Jessica Sachs:** Dev World. Thank you. Yeah, that's where I met Latin and Mink. And we spent a lot of time with Shaw and Misdo from Qlik, and reusability was a huge topic. One of the first times it actually clicked for me was talking with Latin, thinking about -- actually, Latin, your talk was the first time that reusability clicked for me. Is that recorded anywhere?

**Mink Zeke:** I got an email today that they're going to share it out. But you have to like log into the Dev World site, or something. I'm not sure.

**Kevin Ball:** Well, you've teased me now. I mean, reusability is such a fun and fascinating topic... I would love to hear the Latin explanation.

**Latin Rajasthan:** So I have a somewhat different take than Misdo, maybe. First, I'm really glad that Misdo and Qlik have given us the vocabulary to talk about stuff like this... Because before the word reusability, I would struggle to even explain what's going on. And my hands are waving around, and I'm trying to explain how the event handlers are attached, and... Yeah, which is failing horribly. Everyone's like "I don't understand, why does it matter?" And it's true, it doesn't matter for many, many applications... Because you can just have your users wait a second, right? Maybe they're going to spend a lot of time on your site, like an hour or something. And so if it takes another second for it to hydrate, what's the problem? But every once in a while we'll have this experience on the internet where you're rage-clicking a button and nothing's happening. Like, you got to the site, you could see the button, you are clicking, and nothing's happening. Why isn't it working? And then "Oh, they're loading the JavaScript and hydrating the page. There's no event handler, that's why nothing's happening."

So the simplest kind of way to understand reusability would be "It's fine. Keep doing hydration", like your framework is doing right now. But think about what you can do not drop events after server-side-rendered content is visible, and you're about to hydrate the page. And just try to understand what will you need to do if you had this desire, this goal that you shouldn't drop any events at all. And pulling on that thread kind of starts taking you closer and closer towards reusability. Even if you're thinking you're just going to do hydration, like React, or Vue, or any framework today that does hydration, you could try to add reusability by trying to save those events.

**Kevin Ball:** This reminds me of a pattern that actually I might have first seen in Google Analytics, so I'm wondering the threads here together, where you're loading some third party JavaScript that is capturing events, and before it's loaded, you're pushing events onto an array.

**Jessica Sachs:** Is that the really basic TL;DR?

**Latin Rajasthan:** \[16:00\] I think this is the way to start thinking about it. What you realize quickly afterwards is the amount of time you have to capture those events, and you cannot replay them yet depends on how much JavaScript you load. And then you're like "Okay, I need to load the minimum amount of JavaScript, which then means I need to only load the event handlers that I'm actually about to attach on the page. I don't want to load any event handler that's not yet on the page." So you need to know what was rendered on the page. And then you start trying to optimize that, and then you get a fully reasonable kind of framework.

**Kevin Ball:** Mink, you looked like you were about to jump in on something...

**Mink Zeke:** I was just agreeing with Latin, actually. And I was thinking that what he is describing right now is kind of the path Angular is taking, to an extent, because it can also start loading this code on different levels of granularity. And hydration, hydrating the entire application, and replaying the events will be the least granular one. From there, you can have some partial hydration where you're not loading anything, let's say, and over time, you download only the components that the user is interacting with, but also their parents components, because they might be passing some data to the children. And from there, you can do more optimizations for more fine-grained hydration, and reach reusability.

**Jessica Sachs:** So when people are trying to make sense of what Win and Angular merging means, it's basically the concepts that Win uses coming into Angular, but not the DX... Is that about right?

**Mink Zeke:** And vice versa. Concepts that Angular has, coming to Win. A good example is what Latin started explaining at first, during his introduction around how we discovered that YouTube has similar requirements to what Angular is building, and Win reusing Angular's reactivity was able to deliver on these requirements. Now we're doing something similar the other way around, with reasonability and fine-grained code loading. So I guess we can probably dig deeper into these two topics at a certain point.

**Break**: \[18:06\]

**Kevin Ball:** I'm curious actually the connection between reactivity and reusability, because they both conceptually are mapping a dependency graph; just one's about data, and one's about code.

**Latin Rajasthan:** Yeah. Actually, for a while, Win was attempting to -- like, Win has been trying to improve dev ex for six years now, probably longer... Because one of the biggest challenges with reusability is you have to work with these very fiddly event handlers, that are like declaratively specified as attributes in HTML, but then they're also like in the code somewhere else. So one of our first attempts was to actually create a React style programming model. So what that means is your data is represented as just regular variables, and anytime you want to update the UI, you just rerun the whole template. And then \[unintelligible 00:22:43.12\] is your best friend.

And this approach kind of did work to improve the dev ex, but then we kind of keep running into these performance challenges. And with Signals reactivity, like actual real reactivity, where you're doing the tracking of the data dependencies, like you're making the graph, like you said, you're able to tell more precisely what is the data that the component depends on, and that makes it easier to leave some information about those data dependencies. Because it's not just the events that you care about. If you haven't hydrated a component, but its data changes because you hydrated a different component - the usual example is like a shopping cart, or something - then you want to know that "Oh, the cost data changed. I need to hydrate the shopping cart. I need to update it."

**Kevin Ball:** Yeah, so you have intersecting dependency graphs.

**Latin Rajasthan:** Right. And so you need to know two things. You need to know what the data was, and then you need to know what is the chunk that you need to load in order to "hydrate" that thing. And hydration - I'm kind of using the word loosely here. It's not necessary that you need to attach event handlers to that shopping cart; you actually just need to load the update path, and update the shopping cart, because the user added something to it, and so I need to increment that number by one.

**Jessica Sachs:** That's really granular. That's incredibly granular.

**Latin Rajasthan:** Yeah. And that's kind of what Qlik is trying to do. It has a different upgrade path, and the optimizer just splits everything up into like many, many small pieces.

**Mink Zeke:** Yeah. And this I guess sets also some constraints on how you can use data, and how you can manipulate the DOM as well. You can't just do document.querySelectorAll() and find a random element and update it when something happens. Or you can't just update a random data property that is not wrapped inside a signal, because the framework wouldn't know about this, and wouldn't be able to properly hydrate the page, or resume the page.

**Jessica Sachs:** So will Angular users notice a difference in restrictions that they're able -- they're able to like opt in to reusability, or what changes will Angular users see in the developer experience?

**Mink Zeke:** Yeah, great question. So I guess it will change over time, but at first we will not just change Angular and make it entirely resumable, because we're going to break all the developers out there. They'll have to rewrite their applications, and we definitely don't want that. So we're introducing certain primitives; we have deferrable views right now... This just sounds fancy, this keyword, and a block that you can wrap certain part of your templates into, and it will lazily load it.

So we're adding some extra semantics on top of this when you do server-side rendering, and we're reusing some of the primitives that Win uses in order to achieve this reusability called \[unintelligible 00:25:40.14\] JS Action, which handles events at a top level, and from there, based on an identifier, can figure out which codes to load from where.

So just by adding additional, let's say, abstractions and functionality, over time we'll be able to get you closer to reusability, to where it makes sense also, by providing you a good developer experience. We will decide at certain point if we would like to flip the switch and make this the default behaviour or not, but I would say we are many years away from this, and we're currently going gradually on this path of adding reusability concepts on top of the framework.

**Kevin Ball:** \[26:18\] So a question related to that... And I do love the kind of opt-in migration path that Angular has landed on. I think it is -- we've talked about it before, but it sets a perfect standard, and it makes sense given the audience of Angular being so much in the enterprise; people who can't just drop everything on a dime, where that backwards-compatibility is super-important. But is there like a critical -- so something like reusability, it feels like... I'm wondering if there's a critical mass you need to hit too before you start to see the benefits? Or do you see it immediately, just on whatever component you have opted in for it on?

**Mink Zeke:** Yeah, so in Angular later this year we're going to introduce partial hydration, which is bringing us one step closer. And you'd immediately see the benefits there, because you'll already be loading half of your application, let's say. Or actually, at first, you will not be loading any JavaScript; you'll be only loading this small library, Js Action, that is a couple of kilobytes. And from there, you would cut, let's say, by half the JavaScript that you need for the page, depending on how you structure your component tree. So yeah, getting immediate benefits there.

And at a certain point, as you can imagine, we might be able to get 80% of the benefits with 20% of the effort. So we will decide from there whether it's worth really like optimizing for the remaining 20%. Or we can just enable these remaining 20% for some applications that really need this high performance, and keep Angular simpler for everyone else.

**Kevin Ball:** So that does put Angular though from the opposite perspective of like the Win or Qlik mindset of "Fast by default", right? Because there I think the idea, if I understood it, was developers are not going to keep up with this stuff. They're focused on shipping, whatever, they're focused on shipping, it's going to be slow. And Qlik and Win say "You know what, we'll take care of that for you. We'll break everything apart, we'll go very fine-grained, and it will work fast by default." So how can you absorb that into Angular while maintaining the stability that you have?

**Mink Zeke:** Yeah, this is the beginning of the journey, what I'm talking about right now. And fast by default also comes with certain constraints and implications on developer experience, that we are not 100% sure that are worth it at this point. So that's why the Win and the Angular team are working together in order to figure out what is kind of the optimal solution in there; how we can get the best from developer experience and performance, and still achieve incredible performance for 80% of the use cases, and provide a path forward for the people who really are seeking the same performance as Google search, let's say, to do the extra steps and get there.

**Jessica Sachs:** So fast by default... Is that what you're calling it internally? The general principle of the thought leadership behind how Win is built... Did that make sense? It didn't make sense. Neither of you are answering immediately...

**Latin Rajasthan:** We don't quite say that, but one of the key focus areas for Angular this year is actually fast from the start. And so that is trying to capture, you know, SSR is important, we're going to focus on SSR, but at the same time, after SSR, if you just do a hydration, that's going to kill your performance, and so you need to also work on partial hydration. We need to start thinking about streaming, as like SSR streaming, and so on.

**Jessica Sachs:** So those are your priorities right now, is SSR streaming, and then eventually reusability.

**Latin Rajasthan:** Yeah.

**Mink Zeke:** \[30:02\] I have one - maybe a little bit of a hot take also... I would say that performance - it still needs to be a priority. Even if you get a very highly optimized framework that is focused on performance, you can still make your application slow.

**Kevin Ball:** I'm very good at that.

**Mink Zeke:** Yeah. Developers might need to try a little harder to make their application slow, but we just see in the HTTP archive the more adoption certain frameworks get, the slower the applications get over time as well. So it's unfortunate, but still, I'm very confident that we're on the right path to overall make the web faster.

**Kevin Ball:** It's really easy to make your application slow. Just throw an LLM in there. That's what we're all doing these days, right?

**Jessica Sachs:** Chatbots... You said HTTP archive. Can you describe the relationship between how you -- talk to me? HTTP archive... Where does that sit in your research pipeline?

**Mink Zeke:** Yeah, HTTP Archive Open Dataset, which has the top many thousands of websites out there, and there is a crawling that happens I think about once a month - they measure the performance of each one of these targets, and also what technologies are they using on the page. And we are definitely -- well, we are using it in many different ways. We're first curious to see what are the top performance challenges that websites are facing, and figure out on what we should be focused on.

There is another team at Google called Aurora. Aurora also joined us for our session at Dev World \[unintelligible 00:31:36.16\] They're constantly looking at HTTP Archive and trying to figure out different patterns and how they can optimize the web overall, all the different frameworks. So that's one way... Another way is - on Angular we're overall measuring the impact of the performance improvements that we're making by looking at the HTTP Archive very often. It's not very -- HTTP Archive is good for certain things, for example measuring performance, but it also is biased towards specifically landing pages, which doesn't necessarily represent the whole framework community too well. A lot of frameworks are being used for dashboards, let's say, and they will not be present in there. Specifically for load time performance, this is where the HTTP Archive comes really handy.

**Kevin Ball:** And logged out pages, too. Even if it's not just landing pages, you're not getting somebody's private dashboard in there...

**Mink Zeke:** Yeah, yeah.

**Jessica Sachs:** That makes sense. So Latin, for YouTube and stuff like that, the performance metrics aren't as great. HTTP Archive isn't as helpful for you...

**Latin Rajasthan:** Yeah. So since Win is also a very proprietary and internal framework, we have access to the same product analytics and experimentation, information and data that the product teams have access to. And yeah, and Google has a pretty sophisticated experimentation framework, so we're able to make a change, have a control group, and compare that. And even if we do it for 1% of all users, that's millions of users. And so we get pretty good data by doing those kinds of experiments.

**Jessica Sachs:** Do you regularly do performance-only optimization experiments? Like, do you set a feature flag, and you're like "Did changing this action in this way give us performance gains?"

**Latin Rajasthan:** Yes. We're always doing stuff like that. And sometimes it's like just trying to shave a few kilobytes. Actually, that's probably a huge improvement off of the initial render pack on like the search results page, for example. In fact, if there's something that can actually save us a few kilobytes, it's worth spending a year or two years trying to actually get that, make sure it works, and ramp it up for everybody.

**Kevin Ball:** Man, you all live in a very different world... I mean, it makes sense, right? The scale that you're talking about Google, both in terms of access to data, but then if you save a few kilobytes on YouTube, how many petabytes is that per week, right?

**Latin Rajasthan:** \[34:09\] Yeah. So the biggest thing that we were probably learning over the last two years is how different these two products are. They're almost at like the two ends of a diameter which represents like all possible. On one hand you have a product that just wants to get the user off as soon as possible, like show your search result, find the result, and you're gone. Right? And on the other end, you come there, you kind of sit in, you kick your legs up and spend an hour watching YouTube, or more. Completely different products, that care about completely different things.

So the one or two kilobytes example I gave was for search, because it matters -- instead of taking like 200 milliseconds, you can get it done in like 150, that's a huge deal. But for YouTube, that matters a little less. That doesn't mean you just load as much JavaScript as you want, but at the same time, other things are important, like contention. Like, if you load a lot of JavaScript, and now the browser is spending time dealing with that, it's not spending time initializing the video player, and running the video. So it still matters, but for different reasons.

**Kevin Ball:** I kind of love that direction, actually. So if somebody is building a new application, what would you sort of try -- and we'll frame it within Win and Angular land maybe, but I think this is applicable to anyone choosing a framework, and most of us don't have the luxury of being able to choose Win, unless you all are going to open source it... Silence. Okay...

**Mink Zeke:** Well, yes... In the long run...

**Latin Rajasthan:** \[unintelligible 00:35:37.02\] Angular, yeah...

**Jessica Sachs:** We're open sourcing... Yeah.

**Jessica Sachs:** How long?

**Mink Zeke:** Well, it depends on what the target is. But overall, everything will be happening gradually over the next years. Yeah.

**Latin Rajasthan:** So here's how to think about it... We aren't trying to just converge by like explaining concepts to each other, and then recreating those concepts. Like, that would be possible, and that would actually be great as well, but you'd still have two copies. We're converging by actually sharing code. So when we say YouTube is using Signals, we literally mean the Signals code that's in the Angular repository is running on YouTube.com, and the mobile website, and so on. When we say Angular is using Js Action, eventually that would mean that it's the actual same library, the same event dispatch library that's running on Google.com. And we're not maintaining two copies of the code. And so when you take that kind of approach to convergence, it's very real, and you have to do it slowly... Because every step of the way you're kind of touching code that's in production. And it's hard to move that stuff.

**Jessica Sachs:** So you're putting each change of pulling Angular in behind a feature flag, basically, internally, slowly, slowly, slowly, checking those metrics, seeing if you're shaving 50 milliseconds off from load time...

**Mink Zeke:** And also at the same time trying to make this happen without breaking anyone... It's not trivial. It's how we want it to be at the same time; we want everyone to be able to take advantage of these features gradually, incrementally. And it's opt-in at first.

**Break**: \[37:12\]

**Kevin Ball:** So coming back real quickly to Latin's point about optimizing for very different things... If someone's making a decision, is the view that no matter what you're optimizing for, eventually Angular plus Win, whatever this merge thing, Similar, that will be your solution, and it's maybe configuration that changes what you're optimizing for? Or is there still going to be some set of decisions about what's the right framework for the problem?

**Latin Rajasthan:** I think we will end up -- if Win and Angular convert... So it's Wing, by the way...

**Kevin Ball:** I like Similar better, but okay... Wing.

**Jessica Sachs:** No, I like Wing. Wing is nice, it's short, NG is still capitalized the same way...

**Kevin Ball:** That's true. That's true. Okay.

**Latin Rajasthan:** So I think it'll have the capabilities of handling all kinds of applications... But ultimately, if you don't kind of understand your business well, you can always use it in a wrong way, and then you feel like the framework's letting you down. So there's not going to be any framework that's going to somehow save you from having to deeply understand the business need first. Like, what is the kind of page you're building. And if you change your mind about what is the kind of page you're building, it's going to impact you. So you have to be very intentional about the different parts of your site, and try to understand "Oh, this is a page where most of my users are just going to come in, check some status, and leave. So it should be SSR, it should be really fast." And "This is a page where users are going to come in and pour over the data for many minutes, or half an hour, and there's a lot of complex UI here", and so you need a different kind of approach to building that. We will certainly have a framework that will let you make that kind of choice, but you could still get it wrong, and the framework is not a silver bullet.

**Mink Zeke:** Yeah. Great point here. Yeah, I'm also thinking, it's not obvious always whether you need SSR all the time, or CSR; there's different hosting requirements as well. And I know there has been a push for SSR in certain communities, but also your monthly bill will be higher this way. And you may not need it all the time. So that's one of the things where we're thinking SSR will be probably the default that we move forward with, but there is going to be a way for you to opt out of it if you want to just have static hosting.

**Jessica Sachs:** That's super-important to mention. I know the dashboard crowd is pro-CSR in general... So a question - I kind of wanted to go deeper, Ball, into thinking critically about your performance. Can you talk a little bit, Latin or Mink, about Lighthouse, and the nice green 100 bubble, and when you should or shouldn't care about that, depending on what you're optimizing for?

**Mink Zeke:** \[44:21\] I'll say just the business, whatever the business cares about. It's a dashboard. 100 out of 100 might not be the most important thing, especially if you're accessing over like Ethernet. If you're building an ecommerce platform, or ecommerce website, I'd say that 100 out of 100 is probably critical. But there are other bubbles on there, on Lighthouse, around accessibility, that are also just equally important in a lot of cases.

**Latin Rajasthan:** I don't have much to add to that. You have to look at your business metrics as well, and just focusing on one particular metric will probably be a bad idea, if you do it for the long term.

**Kevin Ball:** I'm curious if you can sort of sketch out the space here. So we've talked about kind of two ends of the spectrum, right? Somebody who's coming in and making a snap decision, whether it's ecommerce, or they're coming to search, they want something as quick as possible and bouncing off... And we've talked about kind of the very long - you're either sitting and watching a video on YouTube, or you're really exploring a bunch of stuff in a dashboard where that initial load time might not be that important, because you're going to spend 45 minutes or an hour there. And that seems like two ends of one dimension. Are there other dimensions that you think about, or that you would recommend application developers thinking about?

**Latin Rajasthan:** I think Mink brought up a perfect one with accessibility. I think you have to think about the kinds of users you want to reach out to. So that really is something you have to consciously be aware of, in addition to the time people are spending. Anything else?

**Mink Zeke:** Yup, security. Security, I'll say, is another one. I'll say both accessibility and security are probably things that you'd like to optimize for all the time. And we've \[unintelligible 00:46:04.03\] when I open Twitter, I just see people focused on the performance bubble in Lighthouse... Which is fun, but also its accessibility would not make your application usable by a lot of people, which might be even more critical than performance. But yeah, performance is definitely another important topic, and is also critical for a lot of people, without stable network access also; not being able to make your application accessible for them.

Yeah, I can't think of anything else actually, any other spectrums, or any other dimensions that's we're --

**Kevin Ball:** You almost alluded to one there, in network stability. There's the ability to function in some form or another without internet; the whole like local-first, or something in that domain, where maybe you can load it asynchronously with this inconsistent network, but then once you've got it loaded, you're able to interact there.

**Mink Zeke:** Yeah, good point. Latin is working with the Workspace team very often. I was surprised by how well their products worked when we travelled for dev world. I didn't have network access, and made some last-minute changes in our deck, and everything ended up working out, magically.

**Latin Rajasthan:** That actually reminds me of maybe another spectrum... And that spectrum is consistency. So what I mean by that is, if you're making a product like a spreadsheet, and there's a lot of complex formulas and ways to calculate things, you're likely reaching out to your users on multiple platforms, and so you want the stuff to work the same way on Android, on iOS and web. And so you kind of have to make that decision of do you want the same code running everywhere? Or do you want to target one of those platforms, and then the others can catch up in your business?

\[48:00\] And so Workspaces actually does run the same code everywhere. So there's a lot of like technology that technology choice is there, but then imagine writing your web code using Kotlin, or something like that... Or any one of these cross-platform tools. So that's kind of important to mention as well; you make that choice, like "Oh, I'm going to be platform-native everywhere, so I'm just going to make my app N times." Or "I'm not doing that. I'm making my app once", and I think Jess is pretty familiar with this area.

**Jessica Sachs:** Yeah, I work at Ionic, we do cross-platform. Write once, run anywhere... Gosh, I can't believe I said that. I'm sorry, to everybody listening... Latin, is that public? Did I miss the what?

**Latin Rajasthan:** What?

**Jessica Sachs:** Google's code sharing between JavaScript and Kotlin and Swift... Is that public, the compiler?

**Latin Rajasthan:** No, I gave an example. Kotlin was an example. The actual code sharing we do inside is very complex, and a lot of it is proprietary. The tech is not open source. But Kotlin is one of the open source tools we do have at Google. The other one being \[unintelligible 00:49:04.22\] Flutter. It lets you write everywhere. So this is Google, we have a couple of options for everything, right...?

**Jessica Sachs:** "This is Google..."

**Kevin Ball:** Yes...

**Jessica Sachs:** I think that's a meme? Isn't that a meme? "This is Google..." I don't know if that's a public meme...

**Kevin Ball:** I think on the positive and on the negative, right? There's so many -- the tech geek in me would absolutely love to work inside of Google. And then I also know so many people working there, and the dysfunction sometimes is also there... So I don't know.

So we've talked a little bit about the timeline for this. It's kind of a long timeline, not super-well defined, you're exploring things... If people want to get involved in this, and they are not inside of Google, is there a route for them to do so?

**Mink Zeke:** Yeah, we're posting regular updates, and also a lot of pull requests are landing... I mean, not a lot, but there are a couple of pull requests maybe a year that will be landing, with the primitives that we're sharing across both frameworks. So that's one way. There might be more ways later this year, but... Yeah, that's what we have for now.

**Kevin Ball:** Okay. So essentially, get involved with Angular to see the inside scoop of what's coming in from Win.

**Mink Zeke:** Yeah. And contributing to some of these primitive packages. They're inside literally Primitives directory in the Angular repository. Your code could be running -- if you make a contribution there, your code might be running on YouTube.com by the end of the day.

**Jessica Sachs:** End of the day...!

**Latin Rajasthan:** \[50:38\] Yeah. It depends on the time... But yeah, we try to do daily releases in a lot of our large apps as well, and yeah, it's certainly possible. Anything that ends up in primitives is actually going to be running in production in Google as well. And so that's like a great way to try to -- it's understand what is one way to do this, and also know that any changes you make there are impacting a lot of users.

**Jessica Sachs:** If somebody doesn't feel comfortable contributing publicly on GitHub at that point, they're not there yet in their open source journey, will there be a set of best practices that you publish for Angular developers, soon to be Wing developers, eventually Wing developers?

**Mink Zeke:** Yeah, overall, not specifically contributing to the Angular community, but I guess in a broader sense, there could be many different ways. My very first pull request to Angular was just adding one missing brace in the documentation, and it took me five hours to open this pull request, because I was thinking "How could these people from Google make a mistake?" I was so nervous; it took me literally many hours. Documentation is a great example, or just looking at the code and writing a blog post about it, or learning community inside your company, just talking to your colleagues about these shared primitives and how you can use them in your framework of choice even. All of this is just different alternatives for how people can get involved.

**Kevin Ball:** Awesome. Well, I think with that we're probably at a good place to wrap this up. Any last words, Mink or Latin, that you want to share about Angular, Win and the Wing future?

**Latin Rajasthan:** Yes, so this is super-exciting for all of us, and we're really looking forward to continuing to share more primitives this way, and very excited to get feedback from the community. We want to be just generally helpful to all web developers out there. We're trying to now have these discussions about getting Signals into JavaScript itself, and see whether it's something that makes sense for all frameworks... And so yeah, come talk to us, engage with Angular, and looking forward to it.

**Mink Zeke:** Yeah. We'll be posting more updates in May, with version 18, and after that we'll be slowly rolling out partial hydration. So those are some upcoming updates.

**Kevin Ball:** Alright. Jess, any last thoughts?

**Jessica Sachs:** He mentioned the Signals repo. I got excited. We can't go into it, we don't have time, but I hope that we get to talk about it on this show sometime soon.

**Kevin Ball:** Is there a public Signals repo?

**Jessica Sachs:** It just released. Latin, Mink, both of you have been involved in it, if I understand correctly.

**Kevin Ball:** Alright. Well, let's at least put that in the show notes for people who want to follow up, and maybe we can do a future deep dive. Alright. Well, with that, I think we have just about run this into the ground. Mink, Latin, thank you for joining us today. Just lovely to have a show with you as an official JS Party panellist. And with that, that is JS Party. I'm Ball, signing out. Take care, see you all next week.
