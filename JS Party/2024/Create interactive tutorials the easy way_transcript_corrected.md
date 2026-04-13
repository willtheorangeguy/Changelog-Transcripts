**Jerold Santo:** Hello, world. I'm Jerold, your internet friend, and I'm joined today by Tomek Stokowski. Welcome to the show.

**Tomek Stokowski:** Hello. Hi, everyone. Hi, Jerold.

**Jerold Santo:** Happy to have you. Founding engineer, Derrel and Desex at Stack Blitz.

**Tomek Stokowski:** Correct.

**Jerold Santo:** We've done a show on Stack Blitz, I think it was a couple of years ago... Recorded May 27th, 2021. This is when Stack Blitz first hit the scene. That episode's called "Running Node Natively in the Browser, with Eric Simons." So a companion of yours, I'm sure.

**Tomek Stokowski:** Oh, yeah. Good friend, too. Yeah. '21 was crazy with web containers.

**Jerold Santo:** Yeah. Long time ago. So Stack Blitz still out there, still doing your thing. Today we're going to talk about Tutorial Kit, which is a Stack Blitz open source joint. But first, catch us up with Stack Blitz, what you all do, what you're up to, and what your work looks like.

**Tomek Stokowski:** Okay. So maybe to recap a couple of years in a couple of sentences... We started up as kind of like an online playground for a couple of specific technologies. We picked the most popular one initially, React, Angular, I think we had Ionic... That was the first three. Then we had a couple of new ones, when Vue started getting popular... But that was all a very custom thing based on System.js. So like with every custom thing, you had to reimplement a lot of logic, update it, and...

**Jerold Santo:** For each new thing, right?

**Tomek Stokowski:** Yeah. And still hit a lot of limitations. So that's when in 2021, I think, after like a good year or more of R&D, we've come up with Web Container. And web containers - a super-high-level overview - they're an in-browser operating system. So imagine like typical elements of OS; file system, network layer, and a couple of typical programs that you might find on OS, like Git and things like that, working on the frontend in your browser.

So of course, we targeted Node specifically, and the idea was to kind of provide everything that Node needs to run normally locally, to run this in the browser. That way, we wouldn't have to make all these bundlers, and custom browser-specific things, especially as the backend in JavaScript became a very common thing to do.

So since 2021, we've been building basically on top of web containers, experimenting with a couple of stuff, both on the editor side, and with the engine itself. So for example, last year we've released an experimental Python support; so you can actually run Python scripts in Stack Blitz right now. There is a starter, you can go to, I think, Vanilla Group in Stack Blitz starters, and there's Python, and I think even WordPress plugin, something like this. We have also some experimental PHP support. So... Interesting stuff around that. Yeah.

**Jerold Santo:** Yeah. And so these web containers, I think, are what are enabling this project, Tutorial Kit. Is this on top of web containers? At least part of it is, right?

**Tomek Stokowski:** \[08:09\] Yes, exactly. It kind of consists of two very cool technologies we can dive into in a second... But I think also an interesting thing is how we got there, because basically, a piece of web containers development was dictated by tutorials, to about two years ago, I think, or even longer. But let's start from the beginning.

So you might have seen -- even if you're not into Svelte, you might have seen a Svelte tutorial. It was basically the primary way for people to learn Svelte since its inception, in like over five years ago. That was created primarily by Rich Harris, who is a great communicator and educator. So he built that, I think, inspired by Knockout, from even more back in the day...

**Jerold Santo:** Knockout.js. I know Knockout, yeah.

**Tomek Stokowski:** Yeah, me too. That was so cool, to remember these things. But anyway, so he built this amazing tutorial. And if you look at any of his talks, actually, YouTube recordings, any demos, he's using that tutorial himself as a starting point even to demo specific parts of the framework. So it's not only for beginners and people who are just onboarding into the technology, but it's also for like an advocate as himself.

So it's a very, very cool concept, a cool tool... But now, if you know anything about Svelte, the most common way of using Svelte is by using SvelteKit right now. And SvelteKit has a very significant backend player. So now we're kind of coming back around to web containers, because it was kind of impossible to build a new tutorial for SvelteKit without having the Node aspect. So Rich Harris reached out to us and asked if there is some way of using web containers outside stackblitz.com.

**Jerold Santo:** Okay.

**Tomek Stokowski:** Yeah. So basically, that was our design partner for creating a web containers API. And now you can use this technology, this engine on your website, building whatever you want to build, if you imagine is you had an OS on your website.

People started building very interesting projects on top of it, like their own code editors and playgrounds... And there's a project that provides you details on any package, something like Bundle phobia, but it's using web containers to actually download the package in the browser, and provide you with the proper information about the structure and what it downloaded.

So the direct inspiration for the web containers API were the tutorials built by Rich Harris, but then it became a very universal tool. And since SvelteKit tutorial was such a big success, people from other teams, from other frameworks, were also inspired by it. And there is now -- I think since the beginning of this year, there is an interactive Angular tutorial. If you go to angular.dev, they have a cool, new documentation and an interactive tutorial, that looks very similar in structure and functionality to SvelteKit. And there's also a very cool tutorial in progress built by Anthony FM from the Next team... You can see in his stream - I think there was like 10 video series; you can find it on YouTube - where he actually built the tutorial app from scratch.

\[12:16\] And again, if you look at it, it takes him a lot of time, a lot of hours, and it's not a trivial app... But you end up with something similar to SvelteKit tutorial, similar to Angular tutorial... So we took a look at this and - it's kind of not something that we usually do anymore as developers, building this same structure from scratch. Usually, we have a framework for everything right now.

**Jerold Santo:** Right.

**Tomek Stokowski:** So that's what gave us the ultimate push to create a framework for building tutorials.

**Jerold Santo:** Cool.

**Tomek Stokowski:** So that's Tutorial Kit in a bit, maybe with a bunch of history on top of it.

**Jerold Santo:** Yeah, the background. Well, that's interesting to know... And if anybody has seen a Svelte tutorial - I haven't seen the Angular one specifically, but they're powerful learning tools. They're interactive... Like you said, these aren't simple apps. There are multiple panes, the panes are interacting, there's code execution going on, there's reflections... All kinds of things that are going on to make that happen. So I love that fewer people need to worry about that in order to get awesome tutorials out into the world, and in the browser, which is so powerful, because there's no curl this, and pipe it to that, and download this, or fire up Docker... It's just like, if you can run it in the browser, that's a huge win. And we've seen a lot of different playgrounds and tutorials moving into the browser, traditionally backend tools... SQLite in the browser via Wasm. There's people putting Postgres in the browser. All these different things. You guys have Node, a full Node environment in the browser... How does the -- just briefly, how does the web containers thing work? Is it similar to WebAssembly? Is it completely different? Are you downloading everything into a browser, like a Docker container, or...?

**Tomek Stokowski:** Yeah, the name might be implying something like this, but it's way -- we have a way easier work, because if you think about it, Node itself is already a wrapper around the browser engine, right? So when you download Node, a ton of what you're downloading is basically kind of a copy, let's say, of your browser. And since we are already running in a browser, we can already use this engine. So it's down to us only to implement the missing parts. So that's why it's way more -- it's actually more performant. It's kind of non-intuitive if you think about it, because we've all used a bunch of native apps, and desktop apps, and browser apps, and very often the native apps are like -- you think of them as faster, or more performant. You don't have a heavy weight, like video editing apps in the browser yet. Maybe you do already, but... It's not something that you think about this way.

But we've heard from a lot of people who are on like low-end machines that they're using Stack Blitz, because they're -- let's say like a traditional setup of VS Code, which is built on top of Electron itself... So you have already one engine, then you have Node, another engine, and then you have the browser. So it kind of sometimes kills the lower-end computers. While in Stack Blitz, we use just one browser. So it's --

**Jerold Santo:** \[15:59\] There's one less browser, because there's no local Node. You don't need local Node. You have like the in-browser --

**Tomek Stokowski:** Yeah. Kind of like two even, because the editor itself is also using...

**Jerold Santo:** Oh, I see. So VS Code unnecessary.

**Tomek Stokowski:** Yeah.

**Jerold Santo:** So you have just a browser. Three for the price of one.

**Tomek Stokowski:** Yes, exactly. And Wasm, in fact - yes, as you asked, Wasm plays a big part. Actually, that's both the let's say, limitation or like the rules that web containers has to play by... And what is possible in web containers is basically if there is a WASM version of such a specific binary, then we can run it. That's, for example, why the Python support was possible, because there is a WASM version of Python.

And besides that - yeah, we do have to implement some of this stuff on our own. Our Web Container engineers are high-level specialists in like Node spec at this point, because if you've ever seen like a URL parsing spec, you'll know.

**Jerold Santo:** I have. Unfortunately, I have seen a URL parsing spec. \[laughs\]

**Tomek Stokowski:** Yeah, yeah, yeah. So it's funny, because there are some things where actually browser kind of implements it differently than the Node, for example... And then you have to do an exception for this, and... It's interesting - the event loop also is something that we spend like weeks of work on, just this, and like a different version of it to make sure it's airtight.

**Jerold Santo:** Because Node's event loop works differently than the browser V8's event loop works?

**Tomek Stokowski:** Yes.

**Jerold Santo:** Hm... How do you rectify that? \[laughs\] Who knows...?

**Tomek Stokowski:** You'd have to get Dominic Elm, for example, from our team, to have one podcast just on event loop.

**Jerold Santo:** Right? That one section of the codebase that nobody else touches, because it works right now, so let's leave it alone...

**Tomek Stokowski:** You could do it probably maybe on like Halloween, as like a scary episode.

**Jerold Santo:** Yeah, spooky; spooky code sessions. Yeah, I could imagine. Well, the cool thing about Tutorial Kit, as I said earlier, is that anybody now using this tool, which you all have open sourced and made available, can have rich, interactive tutorials for their library, I imagine you could use it for your design system, or your overall UI that you have for your business... You could use it for educational resources, like Rich Harris does, making demos, filming your own stuff... There are tons of different use cases for Tutorial Kit, and most of the heavy lifting, maybe all the heavy lifting, except for the whole "How should I communicate my tutorial?" has been done. The hard work has been done. And because of web containers you can run it, I assume, on or off Stack Blitz, right? Now, you don't need Stack Blitz necessarily to get this done...

**Tomek Stokowski:** Yeah, actually, there's no connection to StackBlitz.com, as in like you don't go to the StackBlitz.com domain. The web containers themselves do request our part, because if you want to download NPM packages, we handle that package management... But not necessarily as well, because we work with several enterprises that have their specific requirements, so you can already imagine what I'm going to say... But working with their own nexuses, their own private packages behind company firewalls, so airtight installations, and things like that. So that's possible as well.

**Break**: \[19:45\]

**Jerold Santo:** So let's imagine that I'm a library author, and I have a new web component that I want to get out there and get used, and I want to set up a tutorial for it. Maybe it's a complicated one, it's a calendaring web component that builds an entire calendar into your browser. Where do I start? What do I do?

**Tomek Stokowski:** So you can probably just YOLO it...

**Jerold Santo:** Just YOLO it? \[laughs\]

**Tomek Stokowski:** I mean, try without reading the manual; you can run NPM create tutorial. So basically, if you didn't know anything, like how to create a tutorial, that's I think the most intuitive thing you could guess.

**Jerold Santo:** That's pretty simple. You don't even need a tutorial on how to build the tutorial. You just NPM create it. And I did read some of the docs... It looks like it's pretty well laid out, in terms of you create this outline format, that's basically like file structure-based, right? There's like a tree of files, and you figure out your tutorial... Maybe there are three parts, and part one has three subsections, which have two things inside of them... Some sort of tree. Like an outline. And then you create files and folders in the style of that outline. Is that as easy as it is?

**Tomek Stokowski:** Precisely. That's why I said YOLO it. That's how I like to do it. I like to first try, bump against maybe some issues, and then go back to documentation, which - Tutorial Kit has a really great and up-to-date documentation, which is not always the case with some of the stuff that we've been experimenting with in the past...

**Jerold Santo:** Yeah, it's the open source world, you know...

**Tomek Stokowski:** Yeah, exactly.

**Jerold Santo:** Documentation varies.

**Tomek Stokowski:** Yeah, but what you said about the folder structure - we approach it from a developer experience point of view, with that being the first class citizen. So we also -- I was building a tutorial all the time while we were developing the library, so we hit a lot of these issues very early on, and ironed it out before making it public.

So for example - okay, let's start from the content. You've created a NPM create tutorial. It installed everything, you have the file structure scaffolded... You can go to VS Code and start editing. There is a source folder in that you have content, and first chapter, first lesson, and things like that. Every lesson description is a Markdown file. You can also use MDX if you want to have some custom components... So that's that left pane when you look at any tutorial. And then on the right, you have the code, again, environment. So there is a code editor, a file tree and interactive preview. And to display anything in there, in the Lesson folder you have a Files subfolder, and whatever you put in Files will appear in the interactive part of the tutorial, in the file tree and the editor.

So that sounds like "Okay, the way to go", right? But once you start developing that tutorial and building more and more lessons, you will quickly have a lot of boilerplate to copy between each lesson. So imagine, like, you have a Site project, so you have some Site configuration files, some additional things, a package manager -- sorry, a PKG.Jason... That's pretty much constant. Probably the only thing that the student cares about is something from the source folder. So for that, we have also a special templates' folder. And in the template you put that reusable code that is applied to every lesson. You can also have several templates, and use them on different lessons, different chapters, and things like that.

**Jerold Santo:** Yeah, that's really nice, because we've all felt the pain of having -- I think copy-paste is fine when you're just getting started, and you have a handful of steps, or sections... We've all felt the pain of getting down the road and then realizing we want to change something general about the entire tutorial... And then it's that global find and replace moment where it's like "Do you want to update 27 files?" And it's like "Yes, but I also want to tweak it and see what--" I mean, this is just bad developer experience. So having built in emulating is a huge win. I'm glad you guys did that to get started.

**Tomek Stokowski:** Yeah. So I mentioned that you can have several templates... So now the question is, okay, how does Tutorial Kit know which template to use? So of course, we enter the realm of configuration... And that's another interesting DX question, right?

**Jerold Santo:** \[28:16\] Yeah, for sure.

**Tomek Stokowski:** So for the configuration, you can actually configure on every lesson. There is at this point I think like 15 things you can configure, as in "Do you want to show the preview --" Maybe your tutorial is for a CLI-only tool, so you don't need that preview aspect... Or maybe for a specific lesson there's an intro page, and you don't even need the editor. So you'd want to turn on or off several things.

The other popular setting is if you display like five files, because they're relevant, but the most important file is the file number three on that list, like app.js, and you don't necessarily want to show the index HTML every time, you can define which file should be open by default in the editor. And again, if you imagine that in a bigger tutorial, with like 30 or 40 lessons, setting that one file probably - that might be like one or three files distributed in different lessons - would be tedious. So you can define almost every configuration variable on a lesson, chapter and tutorial level. So you can define it just once for the whole tutorial, and you don't have to set this. So it's kind of like an inheriting of the configuration.

**Jerold Santo:** Yeah, this is a situation where inheritance, even if it's just conceptual inheritance - maybe cascading is a way we can think about it - makes a ton of sense, and is very useful, especially in anything that's tree-structured, it makes a ton of sense to just trickle it down to all your children.

Then let's say "Okay, I got my thing done", and maybe I just procreated it, and then I followed the rabbit trail to all these different Markdown files, and I'm done. I've got my tutorial ready to go. And now I want to share it with the world.

**Tomek Stokowski:** Sure. You won't be sending the localhost URL, of course, anymore...

**Jerold Santo:** \[laughs\] So I just expose a port on my laptop, and send it out there?

**Tomek Stokowski:** Yes... \[laughs\] So that's the other piece of the technology... The first being the engine, which is Web Container. The other cool thing - and I think good news for everyone, for every listener that is into a JS ecosystem - it's built on top of Astro. So that kind of answers a lot of questions, if you've ever heard about Astro. But if you haven't, you run the NPM run build command, and that creates a static Astro folder. So it's basically a static site since now, and you can put it on any hosting provider. You can configure a CI to build it, of course, and things like that.

So wherever you can host Astro, wherever you can host an index HTML file, you can host your Tutorial Kit project. So again, you don't have to put it on stackblitz.com, by any means. This can be a part of your documentation site. That's actually the best scenario. That's what we recommend.

**Jerold Santo:** So you're inspired by Svelte and SvelteKit, but you're built with Astro. \[laughs\]

**Tomek Stokowski:** Yeah, true, true.

**Jerold Santo:** Curious...

**Tomek Stokowski:** \[31:47\] Good point. Yeah, I think we were mostly focused on having a very simple code structure, and focused on specific markdown files... So when we looked at what Astro does with projects like Starlight, where this file routing for Markdown and MDX files is a common place... Plus they have a lot of built-in components that are pretty close to what Tutorial Kit does, like documenting code specifically... This all comes with Astro. So that was kind of our main reasoning behind this.

**Jerold Santo:** So once you have your Astro build, you're ready to distribute static files, and you put it up on any host that hosts static files. Are you done at that point? Is there no server-side requirements at all?

**Tomek Stokowski:** There's one thing that you have to set... That's possible on almost every hosting platform. I know GitHub Pages doesn't have this, so that's one exclusion. But for like Tercel, Cloudflare, Netlify, you have to set up specific headers; so these headers are required for web containers to work.

And we have this documented both in web containers documentation, main Stack Blitz documentation, and on tutorialkit.dev, so there's even specific configurations for each of the common hosting providers. But that's the only thing, really.

**Jerold Santo:** Cool.

**Break**: \[33:28\]

**Jerold Santo:** Another thing I noticed which I thought was neat, worth highlighting is that you have available components, React Components to use, that you use to build Tutorial Kit, but they are the different subcomponents of Tutorial Kit... And so if people want just, for instance, the file browser, or the editor window, or like different sections, the different panes, to build into something else that's not a tutorial or whatever, you can grab and go with those, right?

**Tomek Stokowski:** Yes, because -- so obviously, we've built stackblitz.com. In stackblitz.com we've built like the file tree, the false browser, and things like that. Then, when we started doing Tutorial Kit, we've built it again from scratch, and we realized there's a lot of people that are doing this, and it will be useful for folks as well if you want to build like a lightweight editor in your project, in your library; why not use something that we've already -- Tutorial Kit is also open source, so it made sense to make the parts of it easier to consume if you want to rearrange and build your own stuff.

**Jerold Santo:** Well, it looks really cool. It almost looks feature-complete. Is this thing like baked, or are you still cooking it up? Are there more parts to Tutorial Kit coming?

**Tomek Stokowski:** It will never be baked. There's so many... No, no, no. But joking aside, we have a roadmap to 1.0, which is close, which is close. I think within this month, whatever month this comes out in --

**Jerold Santo:** October? The month of October?

**Tomek Stokowski:** Probably October...

**Jerold Santo:** There you go.

**Tomek Stokowski:** Yeah, I think within October we should be on 1.0. But even after that, we have quite a lot of ideas/requests from the early users to add here. But you can certainly build a SvelteKit-like tutorial right now.

Oh, and one additional thing... If you want to start building Tutorial Kit, it's best to do it in VS Code, with a dedicated Tutorial Kit extension. That's something that we've also added based on our initial experiences.

**Jerold Santo:** What does that afford you?

**Tomek Stokowski:** Alright, so when we started working on our first tutorials, we realized that even traversing that file structure, the folder structure for lessons and everything, even though it's like as minimal as possible, it's still quite a lot of jumping around. So the first thing that Tutorial Kit gives you is an outline, and it displays your tutorial outline in the side panel. And when you click it, you jump directly to the Markdown description of a given lesson... Plus the specific part of the file tree is also activated, focused, so you don't have to look for specific folders, changes to folders, and things like that. So traversing is the first thing.

Then creating a lesson... Again, for each lesson, even if it's like we use the templates, we use the configuration on the top level, you still, for every lesson, have to create a content MD file and the Files folder, every time. So why not just right-click, add new lesson, name the lesson. So lesson creation, removing lessons... In the future we want also like a drag and drop to rearrange the lesson order if you want to do so...

And finally, last but not least is - I mentioned there's over a dozen of configuration options, and these options are set in the Front matter of your Markdown file. And if you've worked with Front matter, you probably know that it's not like TypeScript, to say the least, right?

**Jerold Santo:** Yeah, you can just typo something and silently fail.

**Tomek Stokowski:** Yes. Yes. So... Not anymore. Thanks to the extension, we've implemented language service something... I didn't do it.

**Jerold Santo:** Language service protocol?

**Tomek Stokowski:** Yes, yes. I was only a consumer for this one. But yeah, thanks to this you have auto-completion, errors, squiggles, if the types or whatever are wrong... So yeah, that's the big one.

**Jerold Santo:** \[40:17\] There you are, doing developer experience again.

**Tomek Stokowski:** Yeah. \[laughs\] Yeah, exactly. But actually, just to give additional props - in parallel, the Astro team worked out a very similar solution. So I don't remember if this is specifically for Starlight, or generally for Astro. I think it might be for Astro collections. So if you have Astro collections, their extension also can do this as well. So we're kind of coming out of the dark ages of Front matter.

**Jerold Santo:** So are you all using this inside of Stack Blitz? Are you scratching an itch, or are you just providing something for the community? What's the motivation? I know that Rich Harris asked about it, but that's not usually good enough for most people to go and dedicate a bunch of resources to some software... It's a pretty good reason...

**Tomek Stokowski:** Yeah, it's a mix of a lot of these things, actually. I think there is, funnily enough, for a company that moves this fast, and we have a lot of high-priority things that are -- actually, there are some secrets that will be announced on this Vietcong. So that will be after this podcast.

**Jerold Santo:** Coming up soon, Vietcong? Okay.

**Tomek Stokowski:** Yes. And it's something entirely different from Tutorial Kit. But there is, I think, a big need in us... The first five people in Stack Blitz, if I remember correctly, were all educators. So we all started by doing this. And the initial idea behind Stack Blitz was to give people a tool so they don't have to set up all these things locally, and can just start learning the freaking React, right?

So there is a sense of mission behind it, but now that we have it, we also scratch our itch. So there is a tutorial on the using Web Container API, on using Stack Blitz SDK... I do a lot of general browser CSS tips, a lot on Twitter and such... So I've built some CSS tutorials as well... Yeah, but it's also, I think, a very cool showcase of what Web Container is capable of. So yeah, once we got the idea, we just couldn't do it.

**Jerold Santo:** Love it. Well, there is a demo tutorial out there - speaking of CSS - which walks you through some of the basic functionality of Tutorial Kit as you style up some forms. So I went through that one this morning, and just got a lay of the land... Very familiar. I'm not sure if I've gone through specifically Svelte's tutorial, but I like that there's becoming kind of this pattern or trend of how these things flow. And honestly, now that Tutorial Kit exists, it may have the bootstrap effect. The bootstrap effect was a downside, because we want to have unique and different experiences on our websites... But you go to our websites, and they all look like a bootstrap site, with different colour scheme applied, and a different logo... And that's not great when you're trying to stand out from the crowd. But when you're trying to make a tutorial that's familiar for folks, actually having it uniform in the way it presents - and of course, you can theme and style these - is actually a big win, because I immediately understood "Here's the text on the left, here's the interactive part on the right, and the lower right is the terminal. Here's your output." It was all very CodePen-ish. I don't know who started this trend... Maybe it was Svelte. But it feels like a CodePen or a JS Fiddle, with additional instruction... And I like that. I like how it's uniform. And I think as more people build these out, it's going to be a win for the cognitive load. I mean, we've already got to learn so much stuff, right? There's so much to learn. Don't make me learn how to use your tutorial.

**Tomek Stokowski:** \[44:30\] Yeah, fair point. That's a great point. One metaphor or mental model that I have for this is Storybook also, if you think about it. Before Storybook, usually you would build some workbench privately to work on a component faster... But it usually wouldn't get published. And once Storybook came to be seen, now every component library has a Storybook project. And they -- yeah, they look the same, pretty much, plus/minus some plugins...

**Jerold Santo:** Yeah.

**Tomek Stokowski:** Speaking of, we also have quite extensive steaming capabilities, so you can change things around... But in the same structure, which I think - as you said, it's a good thing.

**Jerold Santo:** That is a good thing. Well, the website is tutorialkit.dev. Check it out. Open source, free to use... There's really no reason not to give it a try if you have to build a tutorial for whatever your use case, whether you're at work, trying to help your colleagues understand the thing that you built for them, or you're trying to educate the next group of awesome web devs out there.

Tomek, anything else that we didn't cover on this topic before we call it a show?

**Tomek Stokowski:** I can mention maybe some implementations of some people who have already built tutorials with that.

**Jerold Santo:** Oh yeah, for sure.

**Tomek Stokowski:** So one of our engineers that is building Tutorial Kit - he's currently leading the effort, the open source part of it. His name is Ari Period. He built a Site plugin tutorial. So if you've used Site, you've probably used some plugin, and you might have wondered how to build plugins... So now you can do a tutorial and actually learn that. So there is a tutorial-vite-plugin.pages.dev. So it's on Cloudflare, so pages.dev, tutorial-site-plugin.

And I think the biggest one -- because as I think you've mentioned before, coming up with the actual content is now the only remaining challenge.

**Jerold Santo:** Yeah, it's still the hard part, but it's the only hard part.

**Tomek Stokowski:** Exactly. So it's interesting now, because unlike most other, I think, tools in that space, we've introduced Tutorial Kit first like two months ago, and there are still not so many baked tutorials...

**Jerold Santo:** Sure.

**Tomek Stokowski:** ...because people are still working on the content. So I'm always looking for the biggest one, the most developed one. And I think the one that I've seen is learn.remult.dev. So yeah, it's quite an extensive one. But there's several in progress as well. There's nextpatterns.dev... That's looking promising, especially considering how big Next is.

Also, if you're interested in what tutorial does or do not do, visit our GitHub repository. We have both issues and discussions that are quite dynamic. You can ask questions, you can share your projects, and we will showcase it on Stack Blitz as well.

**Jerold Santo:** Yeah, that is awesome. It'd be cool to get together a list. I'm sure you're going to be collecting them. Send me the links to all those things for the show notes, so people can click through easily to those existing tutorials. And to our listener, if you create a tutorial using Tutorial Kit, let Tomek and the team know about it. They would love to know about it.

It looks like you have a pretty active GitHub, six open pull requests, 39 issues, so people are participating and talking about it, even though you're not at 1.0 quite yet. So it's new, it's ready to be used, and they're continuing to advance it... So that's all good stuff. That's all good stuff.

Well, thanks so much for coming on the show, telling all of us about this very awesome tool you all built. Hopefully, people get out there and figure out their content, get some tutorials posted.

**Tomek Stokowski:** Yeah, there's one less reason not to write, so...

**Jerold Santo:** That's right, one last reason. Unfortunately, now we have no more excuses as to why we haven't finished that stinking tutorial yet, except for it's hard to write words down. Alright, well, on behalf of Tomek Stokowski and the Stack Blitz team, the Tutorial Kit team, I'm Jerold, this is JS Party, and we'll talk to you all on the next one.
