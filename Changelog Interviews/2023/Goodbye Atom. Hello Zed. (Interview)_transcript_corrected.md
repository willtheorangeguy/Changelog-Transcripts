**Jerold Santo:** So on June 9th of last year GitHub officially said farewell to Atom, the beloved text editor...

**Adam Staravia:** Not me. The editor.

**Jerold Santo:** The Atom, not the Adam...

**Adam Staravia:** Atom editor, yes.

**Jerold Santo:** And when I saw that farewell, I immediately thought of Nathan Solo, who we had on the show back in 2017, because Atom was a lot of your work there at GitHub. Welcome back, Nathan.

**Nathan Solo:** Thank you very much. Yeah, I've thought of you guys too over the years, many a time...

**Adam Staravia:** Aww...

**Jerold Santo:** Thank you.

**Nathan Solo:** And I've been relistening to that podcast that we did.

**Jerold Santo:** Oh, nice. How was it?

**Nathan Solo:** It was good. Yeah, I felt like we all did a great job. \[laughter\]

**Jerold Santo:** Excellent. Sometimes I dread going back, especially back to the really older episodes, to hear... Because we think "Oh, no... Those noobs..." Although 2017 wasn't so long ago. We can go back it --

**Adam Staravia:** It wasn't. But we've evolved a lot since then. When I hear that rock intro I know, it's a version of us that's like just in the past, but not terrible, but not our best.

**Nathan Solo:** Your hard rock days...

**Adam Staravia:** Yeah, well, we just had this -- we wanted to come in with a bang. It wasn't necessarily like "Oh, we're into metal", or something like that. It was just like we wanted to sound like "Get amped, get hyped. This is a fun thing."

**Jerold Santo:** Right. But then people told us that we weren't very approachable. Because it's "Is this like a heavy metal --"

**Adam Staravia:** For sure.

**Jerold Santo:** "Is this hardcore? I don't want a hardcore tech podcast." I don't know.

**Adam Staravia:** So then we hired Break master Cylinder, and that's the history basically; that's the long story short.

**Jerold Santo:** Real quick, while we talk about history... Here's ancient history. I don't know if you know this, Nathan, but Adam, I know you know this, because we were just talking about it recently... There's a new movie coming out on Apple TV Plus called Tetris. And it's a fictionalized, dramatized version based on the true story of Tetris, and how it was brought to market. And the main character in that is Hench Rogers, played by some actor; I don't know his name. And it just so happens, when we talk about ancient history, that Adam - not the editor, but Adams Staravia, interviewed Hench Rogers on Founders Talk episode 7, back in 2010. Ancient history. And Adam, you told the Tetris story before it was cool.

**Adam Staravia:** Yeah, man.

**Jerold Santo:** So did you go back and listen to that?

**Adam Staravia:** I haven't, but I remember it very fondly. And that was quite fun, because Hench -- I mean, lets tangent this for just a moment, because...

**Jerold Santo:** Yeah.

**Adam Staravia:** Hench shared the history of like Alexey, and this initial IP issue, and like international law, and being able to sort of get the rights to Tetris, not so much just simply own it, but be able to put it on all these different platforms it's now on today, like the Tetris we all know... Because they worked so hard, they fought so hard to get back what was rightfully theirs. And Hench was a large part of like helping Alexey and the whole process come together, because they were just committed to this game, from the rules, to the gameplay, to the platforms, all that. It was just an interesting story, really.

**Jerold Santo:** So interesting that they made a movie out of it. It's coming out soon, and it's just cool. The main character in this movie, you interviewed him over a decade ago, and got the story. I wonder if they should like to buy the rights from us for this... Can we get some royalty, can we get a royalty check out of this sucker, or what?

**Adam Staravia:** Or at least get a mention at least... "Changelog.fm."

**Jerold Santo:** Yeah, at least get a mention. Or maybe in the credits...

**Adam Staravia:** Yeah. Something.

**Jerold Santo:** Anyway, that's even further back, Nathan, than your 2017 interview. But back then we were talking about Atom... I think VS Code wasn't a thing at that point. I don't remember when VS Code actually came on the scene, but...

**Nathan Solo:** I think it was. Yeah, I think it was.

**Jerold Santo:** Yeah, I think it was probably around, but hadn't taken off... And obviously, GitHub had not been purchased by Microsoft at that time. A lot has changed since then. Atom was very much Chris Wan strath's idea. He had a nice Twitter thread recently kind of telling some of the story of Adam, but you were crucial, and maybe even lead, I think, on the Atom editor inside of GitHub...

**Nathan Solo:** Yeah.

**Jerold Santo:** ...which was groundbreaking in many ways, and paved the way for CS Code, and Electron-based browser tech editors, is that fair to say?

**Nathan Solo:** Yeah, it is. I mean, I remember Chris and Cory, they were a few weeks in at the time I joined, and they had this WebKit, the old WebKit framework that you could pull into Mac apps, to let you kind of drop down into Objective-C... And so Cory had wired up these IO APIs, but one of the challenges we ran into is we didn't have access to the NPM ecosystem. And so from pretty early on, I was on this mission to figure out how to get Node integration, so that we could access all the NPM libraries... And I thought, "Oh, it would be cool if we just had kind of Node smashed into Chrome", because Chrome uses V8...

\[06:02\] We were trying to figure out how to do it, and - I don't know if you want the full story, but we ended up... I think I told the story in the last podcast, of finding Chang, barely able to communicate through this language barrier, but enough to be like "Here's what we want - Node and Chrome having a baby." And that became Electron, and the rest is history.

But yeah, the story of Zed is kind of funny, because having sort of brought about the advent of Electron, we became really frustrated with the limitations of working that way. And that's a big part of why we started on the path that has become Zed.

**Jerold Santo:** Yeah, so we go back to June of last year, when that post came out by GitHub, saying -- although Atom was kind of dead on the vine for a while... The writing was on the wall, it was just like they had to officially... Make it official. And at that time, you tweeted "As Atom's sun sets, Zed's sun is rising. We are not done here." So I love this. This is like a sequel. This is like "Okay, one ends and the next one begins."

**Adam Staravia:** When was his tweet, Jerold?

**Jerold Santo:** "As Atom's sun sets, Zed's sun is rising. We are not done here."

**Adam Staravia:** When was that tweet?

**Jerold Santo:** June of last year.

**Adam Staravia:** Oh, wow. Okay.

**Jerold Santo:** This was right around the -- yes, June 8th, 2022. Right after they announced the farewell. Very, very well played. That was poetic, Nathan. Nice one.

**Nathan Solo:** Thank you. It just came to me...

**Jerold Santo:** And at that point, I'm like "We've got to get you back on the show." And then you're like "Let's do it. But we're not quite ready yet, because - yeah, Zed's sun is rising, but it's just the tip over the horizon there. We're not ready to actually launch this sucker", until now. So here we are. Zed is now out there and available as a beta, and we're excited to talk about this as you're kind of your round two at this text editor game.

**Nathan Solo:** Yeah, that's right. It's great to get an opportunity to do a lot of things right, and learn a lot of lessons from Atom, and carry them forward, into what I think is a much better product, or has the potential to be what I've always been shooting to build, which is sort of the ultimate code editor.

**Adam Staravia:** Can you give us maybe a short version of the mission, and then, kind of the -- did you begin with first principles with this mission? Obviously, you began from zero, right? I'm assuming this at least, because that would make sense. Because before you didn't begin with zero; you began with Electron and the constraints there. Where did you begin here? What's the mission, and where did you begin?

**Nathan Solo:** I mean, the mission's sort of the same as it's always been, which is to build this extremely well-crafted, lightweight, fast, extensible eventually, but not now, but also collaborative tool. I've always believed that one of the key bottlenecks that developers face is just our ability to effectively communicate about code with each other. And there's just so many conversations that I think make sense to have around code.

I came out of Pivotal Labs... That was a culture where we literally sat and coded together for 40 hours a week. I don't really want to work that way anymore, but it really did indoctrinate me into the value of just having conversations about code. And that's always been a big part of my toolkit. But it's always felt like a big gap for me in the tooling that was available. If you want to write a bunch of code by yourself, push it up, and then have a conversation just about the changes you're introducing to main or whatnot, then pull requests work really well. But there are all kinds of conversations that I think could be facilitated around code, that just really aren't. And so that was kind of what I pitched Chris on when I joined GitHub, is this idea of a social code editor.

\[10:01\] The tagline of GitHub was "Social coding", and I just thought we could take it much further. But I think what I didn't necessarily bargain for was just the sheer difficulty of building a good code editor at all, and then taking on the crazy level of extensibility that -- that was really what Chris was excited about more than anything, is just making this thing crazy extensible, like a modern Emacs. And I took that and ran with it as hard as I could as well, creating Electron, and embracing NPM, and all that.

But by the time we just got through learning everything we needed to know to build an excellent editor, and then investing all that time into extensibility, it wasn't until I think after our interview that we really sunk our teeth into "Okay, how can we help people talk about code in this tool?" And I think it was spring of the following year, the year following our podcast - so that was 2017–we decided to build what became Teletype, which was the collaborative coding package for Atom.

And Antonio and I dove into the academic literature, and I had heard a little bit about OT and CRDTs, but didn't know much, and we went from knowing almost nothing to shipping a product in like six months; we were just crazy. I went to Italy, and worked with him for a while, and we just worked so hard on that... And at the end of that I took a step back and was like "We're finally the engineers we need to be to actually build this thing that I've been wanting to build all these years... And we need to start over." \[laughter\]

**Adam Staravia:** Dang...!

**Jerold Santo:** Ouch...!

**Adam Staravia:** That's kind of okay to some degree, right? Like, you kind of build up your skin, you build up your knowledge, but then you realize, everything you've been -- you'd been going the wrong direction, essentially, and you need to begin again.

**Nathan Solo:** Yeah, yeah. And it wasn't necessarily like it was all wrong, or all terrible, but it was also just really clear to me, based on all the battle scars I'd acquired and the experience that I had at that point, that we couldn't get where I wanted to go from where we were. And I didn't want to let it go. So yeah, that's when we started on this project called X-ray. And I called it X-ray because I didn't want to call it Atom 2.0. I didn't really feel that'd be great for the Atom community, and I didn't really have the authority to do that at GitHub. That was always murky; what I did and did not have authority to do was always kind of undefined. We were kind of this little team under the umbrella of this much larger organization...

So we called it X-ray, which is kind of like what you get upon the splitting of the atom. And I remember we decided to do it in Rust, which meant we had to learn Rust, which was no -- I don't know, that was a hell of a learning curve, I'll say that... And yeah, we just started building it, Antonio and I.

We stood in front of the whole Atom team in like January 2018, in Boulder, and I remember giving this presentation about the kind of responsiveness that we really wanted to achieve, that we thought would be what felt amazing in an editor, and all these other architectural details of what we thought made sense. And I don't know - yeah, it was pretty shocking to the team at the time, sitting up there and saying this... But yeah, we started in, and we would -- I remember writing these notes in the repo that were just kind of intended for product managers and people at GitHub, just so that they could maintain awareness of what we were doing. But it was all open source, and at some point, some people found these notes, and we got this little following of people that would just read these random notes I would toss off at the end of each week.

\[14:00\] And yeah, but then... I don't know, we kind of got batted around by different political winds inside of GitHub, and at some point it became clear that there wasn't really an appetite for an Atom 2.0 within the company. I left for the birth of my second daughter, and when I got back, Microsoft had acquired the company, and it was clear that it was really going to happen.

**Adam Staravia:** Oh, wow...

**Nathan Solo:** And so that's what I just switched teams. I worked on web hooks, because at that point GitHub's web hooks were still being delivered by a bunch of like single-threaded Ruby processes, that were like each consuming like 700 legs of RAM, just like blocking sending HTTP requests out... So I went and did that, but in my spare time, Antonio and I started Zed, basically, because I just couldn't -- I couldn't let it go. I tried. There was a period of time after Atom where I'm like "Maybe I should do something else." But every time I'd think of something else to do, I would -- at that point I'd actually switched to Visual Studio Code, because it was a better tool for Rust, and Go etc. and that cursor would be there, blinking, just being like "You aren't done yet. You aren't done yet..." Like mocking me.

**Adam Staravia:** It's the drum.

**Nathan Solo:** Yeah.

**Jerold Santo:** Oh, man...

**Adam Staravia:** Boom... Boom... Boom...!

**Jerold Santo:** The Tell-Tale Heart, or something...

**Nathan Solo:** So I mean, you asked about the mission, and I kind of diverged off in a different direction...

**Adam Staravia:** No, it's good.

**Nathan Solo:** ...but I feel like it's always been the same mission, kind of, which is this lightning-fast, extensible, highly-collaborative tool.

**Adam Staravia:** I'm glad you shared the part of where you were at when GitHub was acquired, because I kind of feel like that's the case here. Every time we have a rubber on the show, it's like, okay, whether you're there now, you're in transition, like Rachel was when she came on the show, or like Nathan's case, he's since left... Where were you when GitHub was acquired? It's sort of my undercurrent of questions. Because then you were so knee-deep into Atom, and obviously, you have this passion for it... And it's interesting even that VS Code was similar in nature in terms of build, because it was also built on Electron early in its day. I don't know the case to this day, but why did it win is a question...

**Jerold Santo:** I think it still is.

**Adam Staravia:** Okay, there you go. So it would make sense... It's like "Well, how did VS Code win?", because obviously, Atom lost, based on the sunset...

**Nathan Solo:** A hundred percent.

**Adam Staravia:** It's just a -- it's an L in that case. But that doesn't mean the work you did was an L. It means that the fight -- and there's a war; it's like browser wars, it's editor wars... I mean, somebody's got to win, somebody's got to lose. I'm not mincing words here.

**Nathan Solo:** Right.

**Adam Staravia:** So you think like, okay, where were you when GitHub was acquired? And then two, "Well, why did VS Code win and Atom lose when you had the same underpinnings?"

**Nathan Solo:** So my understanding of this situation - and it's basically like we created Electron and came up with this innovative model of doing an editor in web technology... And there was this team in Switzerland at Microsoft that was doing Monaco, and doing like Visual Studio Online; like a browser-based version of the editor. That team included like Erich Gamma, who worked on Eclipse etc. But when they saw us doing Electron, and we open sourced Electron, that was this opportunity to like "Oh, we see Atom taking off... Let's sort of take this tech that we're building on the web and fuse it with" what was at the time called Atom Shell. I don't think we'd renamed it to Electron yet. And yeah, that kind of gave them this head-start.

So I think there was a big advantage of coming with some existing tech, some existing experience, and then having us sort of taken all the arrows figuring out how to get Electron done... It was like a pretty good flanking manoeuvre. But then I think a lot of Atom's wounds, honestly, were like self-inflicted on a number of levels. I made some mistakes... And I think one part of it was just never having clear leadership.

\[18:05\] I had been there from the beginning to almost the end. I was the longest-serving member of the team, but I never had any official authority on the team... Yeah, so that was part of it. But there was also just having started the Dark Ages - like, we started in CoffeeScript. It took us too long to switch to JavaScript; we should have gone straight to TypeScript. So just using inferior tools... And it's never the right time to like to take a step back and be like "We should level up our tools. We should pause, do what we need to do to switch, we're going to take a short-term hit, and move forward." We never really pulled the trigger on that, so that was a mistake.

And then we just focused so much on this very broad definition of extensibility, of like "You could come in, run your JavaScript on the main thread, and you could do anything." And I think Microsoft's approach was a lot more conservative, and a lot more focused... But of course, they were coming from the position of working on IDEs, working on the TypeScript's tooling... And so I just think, from their perspective, the language server protocol, and focusing in a more pinpoint way, precision way on the specific types of extensibility that would matter, gave them a big advantage... Because it's hard to maintain all that surface area; it takes a lot of time and energy and resources. And then early decisions we had made that weren't the most performant were sort of sealed in concrete by these API contracts we had made...

So a combination of just like -- yeah, I don't know... I mean, a lot of the things that made Atom exciting were also the things that made it tough to compete, which was just the freedom that people had to do anything. I remember supporting a team at Facebook working on Nuclide; Atom was the basis of all the tooling at Facebook. And that was a much bigger team than our team. It was just like a weird situation, right?

So with Zed, we were determined to do things differently... One thing is had a clear business model, and a clear objective from the beginning, so that we could really start a company that we would aim to be self-sufficient around this tool, that had a clear leadership structure, that sort of me, Max and Antonio, my co-founders and I were clearly in charge of... So that if a decision was made or not made, that was like our responsibility, and there was no doubt about that.

So from a structure perspective, that was one thing. But then I just felt like we had really reached the end of the line on Electron and on JavaScript. Like, if you think about a tool as sophisticated as a code editor, you don't have time to like pause and clean up garbage, or use a language that's just like kicking out garbage constantly, and confined to a single thread, unless you're going through some pretty complex gymnastics to spin up worker threads, that don't have shared memory etc. It's just like -- I don't know, I thought it'd be a push to JavaScript to the absolute limit, and then beyond, doing things like V8 snapshots to start up faster... And just -- crazy. We just were like "We can't do this anymore." So switching to a better language. Rust had hit 1.0. In the meantime, and I'd been following Rust for years, being like "This seems like it could be the right tool to solve the kind of problems we have."

And then there was just like making sure that we had a solid core product, that met a lot of people's needs right out-of-the-box in terms of the languages they wanted to work with, interacting with the language server protocol... Just having all the pieces in place, and fast and polished and dialled in before we even worried about extensibility at all.

\[22:08\] When the iPhone came out, it did a couple of things. It made calls, and you could browse the web. And it wasn't until a little bit later that they launched extensibility. And so that's the strategy we're taking as well. I mean, I am one of the creators of Atom; obviously, I love extensibility. That's a huge value of life. But Zed, as it comes out in this initial beta launch, really, it's not extensible. That's something we'll add. But we want to make sure that we get that core experience right, so that when we start opening up any of those contracts, which we're going to be much more judicious about, we know that the core is solid, and we don't need to go back and change anything and violate those APIs.

**Jerold Santo:** Well, I think you're spot on there in regard to like the order of precedence of things that you need to get right. I mean, as a user, if I took those three things - performance, extensibility and collaboration - and I said, "Which order do you want them in?", that's the exact order that I want them in. And so many tools -- to this day, I'm a Sublime Text user, because for me, I use Vim in the command line, but for text editing in Sublime Text, because it's just faster; it's faster than VS Code. It's faster than Atom used to be.

I liked the ideas behind Atom, I love the extensibility, and just the whole -- it's web tech, you can hack it yourself. But it was always just a little bit too slow. VS Code feels the same way, especially when I start searching and navigating files. It's just a little bit slower. And so performance for me - it has to be there; like, it has to be there. And then extensibility is awesome, but comes next. And then for me, because I code mostly by myself, collaboration and that kind of stuff is - yes, I could do better. Yes, I'm an outlier, because most people have teams... But not as important.

I'm curious, though... So this X-ray work that you did, one of the things about Zed and this breakthrough performance that it has - according to the website; I've only used it for 15 minutes, and it does feel fast... But it has built like a video game thing, so like you're doing this whole -- because it's like "Well, how do we actually make it fast?" And you could say Rust, but okay... That's not going to get you all the way there. It's going to get you to be faster than v8 maybe in some context... But this 2D rendering GPU thing - ha that come out of your work on X-ray? Is that a brand-new thing you guys built for Zed? So in other words, is it just like a spiritual successor, or is there actually code that you built on this version of Atom 2.0, which was called X-ray, that made it into Zed?

**Nathan Solo:** There's a tiny bit of code. It was all open sourced, so...

**Adam Staravia:** Super-clear there.

**Nathan Solo:** ...nobody sue us... But a tiny bit of code from X-ray involving some of the core data structures around the buffer, the text buffer. I'm not sure if we either made its way in or we derived it based on that knowledge, but most of our approach to UI that we took a X-ray we've discarded, because it didn't work, actually.

So a big thing that Antonio and I did in those first several months, nights and weekends working on Zed was like taking a step back and figuring out, "How do we do a graphical user interface in a language with the constraints that Rust imposes around ownership?" Where kind of everything needs to have one unique owner, and it's very -- you know, once you'd have everything be this directed graph, where everything is downward, a tree structure of ownership. And of course, there's library types like \[unintelligible 00:25:33.18\] and stuff that allow for shared ownership, but every time you introduce one of those, you introduce awkwardness, and the potential for runtime panics, if there's like a double borrow etc.

So like that was the first big problem we needed to solve, is like "How do we do UI?" And so initially, the foundation of GUI, we thought, "Well, maybe what we could do is still have Electron do the rendering for us." Like, just that last little bit. And so the core of Zed was actually -- we tried a couple different approaches. One was embedded into Electron as a library, and then the other was actually running as a separate process... And the views would render JSON, which would then be consumed by React on the frontend, and would render the UI.

\[26:21\] And so we put all this work into the core of the system written in Rust, with painstaking attention to our algorithmic bounds, etc. And then the JSON would get to the JavaScript, and we'd just throw it all away immediately... Starting with parsing that data, and then recalculating styles, reflowing the DOM... Like, no matter what we did, we just couldn't achieve the performance that we wanted, even starting from zero, and doing as much as we could have Rust.

And so at some point we were just like -- I don't know, I was afraid of doing our own UI, honestly, to some extent, because it just seemed daunting. It just didn't even seem like a reasonable thing to try, to me. But at some point, it was just like "Well, there's no point in doing this if it isn't superfast... And this is not fast." And so finally, it was just like "We have to abandon Electron. We have to do the graphics ourselves." And I'd never really done any graphics programming. We played with it a little bit during X-ray, like doing WebGL stuff... So yeah, we started with this Rust crate called Pathfinder, which is - Patrick Walton wrote it; really cool ideas in there about doing like a Bézier curve, 2D rendering on the GPU... But that was too slow. And so finally, we just boiled it down to "Well, what do we actually need to draw? What is a 2d UI?" And it boils down to some rounded corner boxes, with borders, and padding... Drop shadows... We need to get glyphs and icons on the screen... You know, there's like a pretty limited vocabulary that we knew we'd need to have, and so we ended up just like writing our own shader code. And to this day, we have like maybe 600 lines of shader code.

The UI library is pretty large, but in terms of the actual code that needs to run on the GPU, because the primitives involved in a 2d UI are much simpler than a 3D game with photorealistic waterfalls, or whatever... It's actually pretty simple the code we have to run on the GPU. It's all the code around that, that efficiently gets from a mouse click to what happens to pixels on the screen.

A lot of the innovation I think is like code that runs on the CPU, that kind of gets that data into the GPU's memory. But yeah, that was the path of just relentlessly saying, "Until this is fast, we haven't solved the problem, and we're going to do whatever we need to do to get there."

**Break:** \[28:59\] to \[32:17\]

**Adam Staravia:** This GUI thing is a brand-new thing. Is this something you all invented? Can you kind of like --

**Nathan Solo:** Yeah.

**Adam Staravia:** You kind of glazed over and quickly explained it, but give us the deeper notes on GUI?

**Nathan Solo:** Yeah. So GUI is an application framework, a UI framework that we basically created because at the time - what was it, like 2019... I think there were some experimental Rust graphics libraries out there, but none of them that we looked at really solved all the problems we knew we would need to solve, and just from a stylistic perspective if I can't pick up a thing that does the things I need it to do, then I'd rather build it myself, so I really understand it, and I really have control of it, I can map it to my intuition.

So GUI covers just the shell of the app, so interacting with the platform APIs to like to pull up windows etc. We did that ourselves. And then once we have a window open, it's just like a giant right now metal canvas that we're going to render graphics into... But there's also just like "How do you structure the views?" So it's based on data flow, rather than control flow. So what does that mean? Well, Rust's ownership rules are really strict, so we have this kind of global object that owns all the top-level views and models. And then the views and models can kind of interact with this global object via this standard protocol, where you know, say a user clicks - that models as an event, that calls an action on a particular view, and we call that into the view. And then the view can do whatever it wants. And when we call them into the view, we kind of yield the guts of the application to the view. And so if the view wants to emit an event, it says, "Hey, I'd like to emit an event." And then Control Flow returns up to the parent object, and then we move that data to any of the subscribers of that event.

So in a language where ownership is more promiscuous, like JavaScript, you might model an event as like "Oh, on click I'm going to attach this closure here. And inside the closure, I'm going to implicitly capture this, which creates like a cyclic loop. And so when the click event happens, I'm just going to loop through all the event handlers and call them." But in Rust, ownership is one way. That model, of like attaching a click handler that calls a method on you, and creates these cyclic data dependencies - that just doesn't work.

So that's a big part of GUI, is sort of how do you structure the application logic, the models, the views etc. so that you can have these bidirectional interactions which are really common in UIs... Like, I open a modal; then the user clicks the X on the modal? Well, the thing that opened the modal needs to know about that, so it can hide the modal. That creates this bidirectional relationship.

So a big part of GUI is just like a scheme for modelling bidirectional data relationships between these big views and models in the app. And then there's another big piece of it, which is, "Okay, once we have updated the state of a view, how do we represent that view on screen?" So there's this concept of a tree of elements, which is kind of inspired by React, but the difference is that in React you have the virtual DOM, and they're diffing it with the underlying DOM, and then that produces some mutations to this retained mode representation of the state of the UI, and then a bunch of other stuff etc. Like, there's this big chain that occurs... Where instead, anytime any view you update its state, we basically re-render the entire window. So we build this tree of elements, and we do a pass from the top that lays everything down. And this is inspired by Flutter, which we found via the writings of \[unintelligible 00:36:04.16\] Levine.

\[36:07\] So yeah, we do this layout pass-down that says the constraints, how big or small anything can be, then everything passes, it sizes up. So there's one linear layout pass, and then one linear paint that populates this cross-platform scene representation. Then we go straight into GPU memory and draw it.

And so we bypass all this nonsense that occurs on the web. I mean, this model of the web vastly predates the availability of GPUs, and introduces a lot of complexity that's not relevant to the problem we face, of like keystroke to pixels. I get a keystroke, I want pixels on the screen on the next frame. And so yeah, GUI is the system that we built, that kind of aligned with our intuitions, and everything we've learned about doing UI... And I'm sure there are many ways to do it, but this one's ours, and it's worked pretty well for us.

**Jerold Santo:** That sounds like it would be platform-specific.

**Nathan Solo:** It's not.

**Jerold Santo:** It's not, because, as of the beta, it's macOS-only; you are working on other platforms, but it's not. It can work on a GPU, on any common architecture.

**Nathan Solo:** I mean, there's nothing -- so at the moment, we're only on the Mac. And why is that? That's because I am a Mac user, and so when I was working nights and weekends on Zed, that was where I started, on the machine I was on. But we've designed GUI very deliberately to not really be platform-dependent. All the platform-specific pieces are isolated into small interfaces, that should be able to be ported quite readily to other platforms. We haven't done that yet, because we're still really early, and we want to learn as much as we can, and develop the product as much as we can in a focused way... And it kind of just feels like adding another platform is going to add a lot of surface area to maintain, without a lot of new learnings in terms of like the product itself.

And so that's why we're just staying focused on the Mac for now, but it's our intention to really Sun, Linux and Windows prior to dubbing anything 1.0. I think anything called 1.0 would include those things, and I think we're well-positioned to deliver there, as well as on the web.

**Jerold Santo:** As well as on the web. Okay. Taking it back to the web. So when I think about Zed, I try to put myself in your shoes, and I know that you had this cursor staring at you, like blinking, just making you do this... But Zed is being born into a much different landscape than Atom was born into. Very much when Atom was created, there was kind of a dearth of innovation in the space. I mean, TextMate had gone silent, Sublime Text had come in and then kind of, they would release - they still to this day release like once or twice a year, and it's like, they have some builds you can get on... But it was just kind of like not much new. Then you had the hardcore Vim and Emacs people, who are just still using Vim and Emacs to this day, and always will... And Neovim came in at some point and kind of stimulated some innovation in the Vim space... But then VS Code came and really sucked a lot of the air out of the room. I mean, they are the juggernaut now. It seemed like it happened relatively fast. Microsoft put a lot of weight behind that project, and executed very well, as you mentioned some of the things they did.

And so success to them. That's all good. But now here comes Zed... And I'm thinking, like, would I want to compete, in this landscape today, with a brand-new thing? Maybe I would, it sounds like maybe it's a nice challenge, but it also sounds kind of daunting. And then I thought, "Well, the TextMate guys/guy (I don't know how big that team is; I think it's very small), and the Sublime Text people, which there's like three, I think... Like, they're making a good living, right? They are selling licenses for 100 bucks a shot... And you're not going to take over the world, but they can be happy, writing the code they like to, helping their users... And then I see you raising money, and building a team, and I think, "Well, that's not the route Nathan's going." So you're kind of going bigger.

**Nathan Solo:** Right.

**Jerold Santo:** \[40:09\] Maybe help share your mindset around what Zed's trying to become, the landscape, and how you set yourself apart against VS Code now, to carve out your own user base that's big enough to support a growing company with debt, so to speak.

**Nathan Solo:** Yeah, absolutely. Well, we raised equity, for what that's worth, but...

**Jerold Santo:** Okay.

**Nathan Solo:** But I get it.

**Jerold Santo:** No debt. Equity partners who would love their money to come back multiplied.

**Nathan Solo:** Exactly. Yeah. And I don't accept investment without an intention to return on that investment.

**Jerold Santo:** Sure.

**Nathan Solo:** So I definitely would like us to. And quite frankly, I think that code editors in general, the entire space would do well to have a kind of native business model, if that makes sense. Because for all the value that software brings to the world, I think that the front line of where software is written doesn't see enough investment and innovation, because historically I think it's been hard to monetize.

JetBrains is the one company in this space, they're 20 years in, and I think they've managed to gain a foothold with this kind of license-based model. You have these like lifestyles scale businesses like TextMate, or Sublime, that are operating the small teams, or you have kind of the big corporate patron model, which was Atom and VS Code. And I just think that we'd be best served as an industry if we can come up with a business model that's really a flywheel that's generating value and finding a way to capture enough of that value to continue to generate more innovation and really level up this piece of the developer tooling stack. So I think we need it.

In terms of... You bring up -- I don't know that I would want to compete in the landscape, as it looks today. And for me, from a personal, like my personal, deep-down personal motivations to do this, if I saw an editor out there that I was happy to use, and felt like really nailed my definition of the ultimate editor, the perfect editor, then I would not need to compete.

**Adam Staravia:** Okay...

**Nathan Solo:** But just from a personal perspective, it's not like I surveyed the landscape and was like "Let me find a low-hanging fruit to pick." It was much more the perspective of "I've been trying to do this for 10 freakin' years, still haven't managed to do it, and nobody else has either, and so I just have to keep going."

Now, you'll have to talk to our investors for their particular motivations, but I can tell you what I told them, and really believe, in terms of what the market opportunity is today, in terms of - again, I think if I were in this for the money, I probably would have started like a crypto token, or something. That would have been a faster route to riches. But I do think it makes sense to build a business model around this.

And for me, the opportunity is really about how we all communicate around code. I mean, I worked at GitHub for nine years. I love GitHub, but I also don't feel like there's been substantial innovation, since pull requests came out all those many years ago. And I think it made sense at the time to kind of hang this social layer on top of the version control artifacts. I just think we can take it much further. I mean, that's what I pitched Chris on, to kind of get hired at GitHub, and we didn't manage to pull it off... But now I think, based on everything we've learned, we're actually positioned to do that.

\[44:00\] And so what I really want is a world in which having a conversation about any line of code, whether it was written a couple of years ago, or I just wrote it and I haven't even hit Save, is something that just feels like at my fingertips; I can @ mention a teammate, pull them in, and start a conversation, so that conversation is really growing over the entire codebase. Because again, you want to introduce a new feature - that probably interacts with some other layer of the system that you may not understand. Already, you need to start having a conversation. But do you do that on a pull request? You haven't even written one line of code yet. You're just trying to understand what's going on.

And so there's just so many things like that, where it would be a great idea to have a tool that really facilitates interaction around code, and it just doesn't exist. Like, I don't know what we did; we'd like paste code into Slack, or like cap things inside of backticks. You're talking about code that isn't even there, and then it scrolls off the screen, and it's gone forever when someone else comes to the code and has the same exact question that you had. Or are you hopping on a Zoom call and now one person's like dictating through the screen, like "Oh, no, no, no. Okay, open this file; okay, now go to this function..." Whereas already in Zed we've tackled the real-time piece of it.

When we want to just have a conversation about code, we're doing that in Zed. Start up voice, that's not in Zed yet, so we still rely on an external tool to do the voice for us. But then I'll just open up a submenu, invite one of my teammates in, and we're following each other around inside the code, instead of trying to dictate through the screen, like "Go here. That -- take that", because the latency is so high, or whatever. I'm just moving around, and they're following me, and then they're moving around and following me...

I remember, when Mikhail, an engineer on our team - she was like integrating the terminal into Zed; she was interacting with GUI, and there might have been some APIs missing; she wasn't quite sure. So we had a conversation, and I toured her around inside the GUI, which I wrote the majority of, and then I followed her, and she toured me around inside the terminal code, and then I got a sense of what she was trying to do. And then I jumped back into GUI, and we wrote the code, added the methods together that needed to exist for her to accomplish what she was trying to accomplish. Then we hop back into her code, which she knew much better than me, and used those methods. And within an hour, with a quick conversation, we accomplished what over pull requests would have taken a week, I feel like.

And so that's the level of fidelity that we're looking to bring to interaction around code, starting with real time, but not confining ourselves to that. That's, I think, the innovation opportunity; it just so happens that the primo kind of iPhone, Apple vertically-integrated product that delivers that experience in my mind is the tool in which the code is written itself. That you shouldn't be Command+Tabbing out to a browser; that that experience should be tightly integrated directly into the authoring environment, just like it is with Figma, or Google Docs, or these other disciplines, that the place to collaborate and talk about code is where you write it. So we have to build a great code editor. But luckily, I want to do that... So that's our competitive insertion, and that's the business part that we want to build.

If you want to use it by yourself, I want you to do that and do it without paying us a dime for it into the future. And I want to build a business around teams using this tool to be more productive by having a better mind meld with each other and being more effective in our communication. That funds the people that just want to use it by themselves for free, and drives more innovation into the code editor space than has ever been possible, ever been funded.

**Adam Staravia:** As Jerold said, you are up against a daunting task. I mean, VS Code is quite entrenched.

**Nathan Solo:** Oh, yeah.

**Adam Staravia:** \[47:59\] Some of the greatest minds working on it, working in it. We just had a conversation around dev containers which is built right into VS Code. It can be built into Zed as well pretty easily, I'm sure, because it's open source, and the CLI is there, and the APIs are there... But that's a task. The business model seems sound, and we've definitely heard the teams' aspect before. And it's nice that you want to give the editor away, as you said, "for free", to anyone who wants to use it in perpetuity, because you want to build a better code editor; something that when you click a button or push a key, that the very next frame - it's there. And that's that's amazing.

I do want to mention though, because you mentioned Chris's name... Chris, if you're listening, it's been since episode 10. Come back on. Okay?

**Jerold Santo:** Come on, Chris...

**Nathan Solo:** \[laughs\]

**Adam Staravia:** Chris Wan strath, yeah. Since episode 10 of this podcast, it's been too long. Come back on. And we'll talk about whatever you want. But this is pretty cool. I mean, this is definitely innovation, and I think that's where we want to see things at. It makes sense to start on performance; on the webpage, I think it's /features, if I'm on the right page...

**Nathan Solo:** It's just the main page, probably...

**Adam Staravia:** Sorry, the .dev.

**Nathan Solo:** Yeah.

**Adam Staravia:** "Engineered for performance." You're going to leverage every CPU, every GPU, and the graph there says that Zed performs faster or as fast as Sublime Text, three times as fast as VS Code, and I don't even know Lion, or Lion, or...

**Nathan Solo:** Lion.

**Jerold Santo:** Lion?

**Nathan Solo:** The JetBrains variant of --

**Adam Staravia:** Okay...

**Nathan Solo:** The JetBrains variant targeting Rust and C++.

**Jerold Santo:** Gotcha.

**Nathan Solo:** Just because, I think -- again, we're not even really targeting Java right now. Like, JetBrains can have that, for the time being.

**Adam Staravia:** For the time being... I love it!

**Nathan Solo:** Yeah. That's why we put Lion up there as our point of comparison. Yeah.

**Jerold Santo:** Sure. So let's talk about the name.

**Nathan Solo:** Yeah. Is this a Pulp Fiction reference? Please tell me this is a Pulp Fiction reference.

**Nathan Solo:** The funny thing is - you're going to be surprised; I've never even seen Pulp Fiction.

**Adam Staravia:** Oh, my gosh...

**Jerold Santo:** \[laughs\] Okay...

**Nathan Solo:** So yeah, I should watch it. But anyway. So yeah, someone has since informed me of the Pulp Fiction reference, but... Actually, it was a reference -- I was thinking about names at some point, and I thought back to the Unix editor Ed, which I've always been just fascinated by the history of Unix, and that picture of like Thompson and Ritchie on like a teletype hooked to this PDP 11 that goes to the ceiling, like writing Unix on a freakin' teletype printer. Right? Just like -- that is so mind-blowing to me. And so I love -- yeah, I love kind of computing history, and I was like "Maybe we could name it Ed." And I'm like "Well, Ed still exists though", right?

**Jerold Santo:** Right.
**Nathan Solo:** If you open your terminal right now, and you type ed, it's an editor. I'm not gonna -- it just seems rude to shadow the editor that's still there, that's Ed, that we're trying to be an homage to.

**Jerold Santo:** Right.

**Nathan Solo:** So, I was just thinking "Okay, well, can we name it something similar to Ed?" And Bed doesn't seem like a great name, you know...

**Jerold Santo:** Right. SED is taken, Ted has its talks; there's TED Talks, you don't want to be Ted...

**Nathan Solo:** Exactly. \[laughter\] And I knew I wanted to be short, and so yeah, it just felt like Zed was a pretty good name.

**Jerold Santo:** It's a good name.

**Nathan Solo:** And what I like about it - it's like a word for a letter, and... I like it. It's an homage to Ed, and just like a cool word-for-a-letter... My daughter's name is Zoe, so it's the first letter of her name...

**Jerold Santo:** The first letter of hers, too.

**Nathan Solo:** Yeah.

**Jerold Santo:** I think it's cool. I think you're kind of -- it's like the last Ed. You put the last letter of the alphabet in front of Ed, and it's like Zed. The last Ed.

**Nathan Solo:** Yeah, the last editor... I'm pretty sure this is the last editor I'm going to build...

**Jerold Santo:** \[51:56\] It's at least Nathan's last editor... \[laughter\] It's not THE last editor...

**Nathan Solo:** Swinging for the fences on this one.

**Jerold Santo:** Yeah. So you've raised money, you're swinging for the fences, you're building a team... It looks like you have a decent-sized team. Eight on the website. I'm not sure if that's still accurate, but something around there. And hiring still. Are you building out a team, or you feel good?

**Nathan Solo:** We are definitely hiring, yeah. We're interested in people that know Rust fairly well, fairly proficient in Rust, and... Yeah, the typical ideal startup employee, which is someone that's self-starting and...

**Jerold Santo:** Right.

**Nathan Solo:** Yeah. So if anyone listening to this is interested, excited about the things I'm talking about, we would definitely love to hear you and get help to work on this thing. And next on our radar, and we need to choose the timing right, is also to go open core.

**Jerold Santo:** I was just going to ask you about that.

**Nathan Solo:** That's something that we're not quite ready to do well right now, but I think that's gonna really help us with hiring as well. It's not the only avenue that we want to use, because obviously that narrows your pool to people who are able to work on code in their spare time etc. and we want to be more open than that. But I do think it'll give us a perfect idea of who's excited about this thing, who wants to work on it, and just to get some help. So yeah, we want to go open core; there are some pieces of the system that we think it makes sense to retain proprietary, the parts of the system that we want to charge money for. But we're hoping that can be a pretty small minority of the total code that we've produced, and that the pieces that we don't intend to charge for, we can share more openly. That's good for the community, and also good for us. I'm sure there are so many itches that people that use Zed would look to scratch that aren't even really that big, but there's just a lot of surface area on a tool like this, so... I'm not sure -- I think it's the best route to get help.

**Jerold Santo:** Yeah, this is a similar conversation we had with Zach Lloyd from Warp, and they're building --

**Nathan Solo:** Oh yeah, I worked at Warp for a little bit.

**Jerold Santo:** Oh, really?

**Nathan Solo:** A lot of the tech that they're using is actually derived from our early work on Zed.

**Jerold Santo:** Okay. I mean, there's definitely similarities even inside the model.

**Nathan Solo:** Oh, yeah.

**Jerold Santo:** Yeah. And one of the things that we said to Zach, and he took a lot of thought from there and moved on from there, to think about this as like - the first thing Warp did, and this is back when did the show, and I'm not sure if it still does it, was sign in with GitHub immediately before you can start using it. And I was kind of like "Yeah... It's a terminal, you know?" Like, I get it, it needs to be there for the collab stuff. But the collab stuff wasn't in Warp at the time, just like I'm assuming there's some Collab stuff that's missing from Zed at this time. And I was kind of like "That's a bummer", because you know, this is my terminal; I don't want to necessarily sign in to GitHub to use my terminal, or sign in with GitHub. Sign in to Warp. And so I was kind of trepidations when I saw the invite about Zed of like "Uh-oh... Is it going to be the exact same setup?" And I'm happy to say that I'm using it here without being signed in. There's a Sign-In button in the corner, but not required. So that's a nice touch...

**Nathan Solo:** Because I wouldn't want that...

**Jerold Santo:** Exactly.

**Adam Staravia:** Ha-hah!

**Nathan Solo:** I don't know, it's really important -- I feel like if we can build a compelling business, that needs to be something that people are excited to opt into, if that makes sense. I definitely don't want to like cram anything down anybody's throats.

**Jerold Santo:** Right.

**Nathan Solo:** And I don't think that -- I think that would be counterproductive, and it's just not necessary. So yeah, being legit... And again, the same perspective with telemetry, for example. I know that developers rightfully so are like concerned about their privacy from a principle perspective, and a pragmatic perspective. And so our telemetry - it's opt-in; you go to Help, Show Telemetry, Log, or whatever, and you see exactly the stuff that we're sending.

**Jerold Santo:** Right.

**Nathan Solo:** So just being legit...

**Jerold Santo:** Transparent, yeah.

**Nathan Solo:** Exactly. So yeah, we are trying to build the business. But we're also developers as well, and know what we would want... And so we're trying to be respectful of that.

**Jerold Santo:** \[56:03\] Yeah. Well, I think the open core, the open source aspect, when you get there, helps people with adoption, in regard to those kinds of things. It's like, I'm not hardcore on everything I use has to be open source. Obviously, I'm a Sublime Text user; it's not an open source product.

**Nathan Solo:** Right.

**Jerold Santo:** I prefer that, especially for tools that I want to use for a long time, and for business models that are VC-funded, or equity-raised, and the business model may or may not pan out at the size it needs to in order to thrive... I don't necessarily want to adopt tools that are going to disappear on me. And so open source at least gives you the "Okay, if Zed the company dies, Zed the editor, in some form that I can use, can live on, and somebody can pick up the mantle and run with it." Those kinds of things matter to people, I think. And so I definitely would say that's good intuition.

Now, having everything be open, like you said, can ruin your business model, right? Like, it can make it unsustainable if you don't do it right, so you have to tread carefully with those things.

**Nathan Solo:** Yeah. And for me, I'd like to be as open as possible while being confident that we can build a business... And that's in everyone's interest, I think...

**Adam Staravia:** Yeah.

**Nathan Solo:** ...because ultimately, I think a product like this benefits strongly... Obviously, there are examples of editors that are completely community-funded. I believe the best result is that there's a core team stewarding the product, and channelling the efforts of the entire community around it. VS Code has that; they just happen to have a very large Patreon backing them.

**Jerold Santo:** Right.

**Nathan Solo:** In our case, we needed another plan. So the parts that we'll keep are just the parts where we're not confident that if we open them up, we would be able to build a successful business. That's as simple as it is.

**Adam Staravia:** Yeah. You mentioned charging for teams, and I guess free for individuals, to some degree... Can you speak to the business model? Will it be licenses? Will it be subscription? Will it be -- how will it work in terms of some of the model?

**Nathan Solo:** I mean, we're still -- I think we're a ways away from that, to be real, like, in terms of -- we've just got to get individual people adopting this thing. It's like "Here's a phone", but if you've got nobody to call, it's not very useful. So I think a big part of our effort is just building what other people want to use, and filling in the features people need that aren't maybe there yet, doubling down on the things people are loving...

So in terms of the exact -- yeah, my gut tells me right now it's going to be a subscription-based model similar to GitHub etc. But I reserve the right to do more thinking on that, I guess. So yeah, I'd like to do more thinking. Don't set that in stone... But that's our instinct.

**Adam Staravia:** Well, it's not about setting it in stone, it's just more -- so the reason I asked you that question is kind of twofold. One, I'm curious, but then two, just to talk it out. Because I think if you want the adoption of developers, then you talk about that adaption and how you plan to attract them, on this show. You share where you think you're going to go; not "This is not where we're going to go, but this is where we think we're going to go."

**Nathan Solo:** Right.

**Adam Staravia:** And in a lot of cases, like Jerold mentioned Zach Lloyd, and Warp, and whatnot - that conversation to me... Like, we went back to some of that too with one of his developers that was at All Things Open, and we kind of talked about some of their thoughts around the business model, and the fact that they're not open source... And Jerold and I kind of like really hammered home the last -- I want to say 20 minutes. Like, "Warp's got to be open source. That is THE thing for you to do." Now, obviously, we know open source is one, but how do you do it wisely, in a way that doesn't hamstring your future possible business or not? And that remains to be seen. But I think it's important to talk about those things.

**Nathan Solo:** And we learned a lot from Atom around -- you know, just because you make something open source doesn't mean you're making the most of that community. And so I think that's part of what we're focused on now, is just like first get the freakin' thing out there, and get our ducks in a row so that we're -- I mean, we're not going to do a perfect job, but we're well positioned to do as good a job as we can, like channelling the energy of people that want to participate, and being clear on what kinds of contributions we're interested in and not...

\[01:00:08.16\] And yeah, I mean, really, we may go sooner, but I would really very much like to open source Zed on Zed, meaning use some of the capabilities I'm talking about developing as a part of the open source, the experience of contributing to Zed. Like, you have a question about the code as you're trying to contribute? Being able to engage with us in Zed, on the code.

**Jerold Santo:** That would be cool.

**Nathan Solo:** Because that's really -- our big vision is for Zed to be the future open source. I mean, that's the Grand Slam we're hoping to hit.

**Adam Staravia:** Okay.

**Jerold Santo:** So, okay, I'm starting to see a little bit more of your picture here... Because now all of a sudden who needs GitHub? Open source it on Zed.

**Nathan Solo:** I mean, I don't mean this necessarily like go Git hosting...

**Jerold Santo:** Well, you said where open source is going to be.

**Nathan Solo:** I mean, on a long enough timeframe, yes...

**Jerold Santo:** Okay...

**Nathan Solo:** But yeah, for a while, what I'm more talking about is a lot of the interaction that needs to take place...

**Jerold Santo:** The collaboration part, the social coding.

**Nathan Solo:** Exactly, around open source. I still think there's a role for pull requests, the build gets run, there's this official moment, there may be some conversation that needs to take place on the pull request... I just think there's a lot of conversation right now that isn't happening, that needs to happen. That's the kind of future of open source that I'm really talking about. It's just a new kind of experience that doesn't really yet exist. Because if we were just trying to compete with GitHub, I don't think we'd succeed, and I don't really honestly think that's very interesting. We want to do something new.

**Jerold Santo:** Yeah. Well, the thing is that GitHub is going to be building that future as well from the other direction with VS Code, right?

**Nathan Solo:** Right.

**Jerold Santo:** So you're both going to be going towards a similar space. VS Code is going to become more and more collaborative, more and more real time; all these things that you're building at the same time you are, just from a completely different direction.

**Jerold Santo:** A hundred percent.

**Jerold Santo:** So it'll be interesting to see...

**Nathan Solo:** Yeah, and you know if they get there and execute it really well, and I've built something I'm proud of, and put in a good effort, and I could look back on it and be proud of it, then - you know, I won't love that, but... I can live with that.

**Jerold Santo:** Yeah.

**Nathan Solo:** But my bet is that a small, opinionated team, that's really passionate, and working on this for a long time, and is approaching it with the right tools, and engineering the entire product around the assumptions of the kind of thing we're talking about, has a shot at doing a better job. But we'll see.

**Adam Staravia:** Here's the question I wonder if you've asked, and how much you've bought into it... Because I think we asked you earlier how much have you surveyed the landscape, and you said "I haven't done extensive." I'm paraphrasing.

**Nathan Solo:** Yeah.

**Adam Staravia:** But what is it that makes a developer change their tooling? Specifically, an editor. And Jerold mentioned the list, Emacs, Vim, try hard, often fail, probably to remove that from their hands... Sublime to VS Code - I think that kind of depends on the extensibility. A lot of people move because "Oh, it supports Rust, or it supports Go, or it supports my stack much better etc." Obviously, performance is sort of the necessary core. Will you win only on performance? Probably not. Right?

**Nathan Solo:** Right.

**Adam Staravia:** But what is it that makes a developer change their mind, especially when it comes to changing their editor? What is it? Is it an individual? Is it teams? Because that's part of your business model. And how that question gets answered is "It depends on many, many levels", and that's the easiest for developers, or any question. But that's the question I think you should be asking and figuring out, and having all the various permutations of that answer... Because that's going to guide your directions' product, that's going to guide your directions business model, and how you can actually create value for those people.

**Nathan Solo:** \[01:03:56.27\] Yeah, I mean, I wish I understood the answer to that question in aggregate better than I do... But frankly, the framework that I use is -- like, Linear had an article that put it really well, I think, structuring it in terms of removing blockers and adding enablers, like that's sort of any product. And so for us, removing blockers is just like "Oh, my linter doesn't work", or "I needed a bugger. I don't have a debugger yet." So part of our effort is just like, if somebody does try it, making sure there's something stupid in their way, or just getting things out of their way that are stopping them from being able to use it. But that alone obviously isn't enough. We've got to have these key enablers.

And so for us, what our enablers are performance, that's what we lead with on our main page; uncompromising approach to performance, going to whatever length necessary to make it good. Clean design I think is something I'm really proud of. Just, the editor is really beautiful, and also minimal, fades into the background while you're using it... And that I am really hoping that people are going to resonate with some of the features we have, and some of the features we're adding in terms of better tooling for connecting with their teammates. So right now, those are the compelling things we're focused on.

Obviously, there are new frontiers opening up in AI as well. Integrating Copilot is something that's high on our list, but obviously, it goes much further than that... But at least at the moment, doing further innovation on that front isn't at the top of our list. It's really about connecting you with your teammates. So we're hoping those three things can be compelling for people, but we're going to get into this beta and hear what people have to say, and figure it out as we go.

**Adam Staravia:** I think this team aspect is manageable. So one of the things you say at the very top of your homepage right now is "Zed is a high-performance (we've covered that) multiplayer", which I think is a keyword there, obviously, right?

**Nathan Solo:** Yeah.

**Adam Staravia:** A multiplayer code editor. And so - sure, team. But in open source, like the random out there could be your team. So I think you need to really examine what team is, because it's in air quotes really, because it could literally be your team, if you're an organization or an enterprise leveraging Zed. But if you're an open source maintainer, and you're adopting dev containers, and you've got a code space, or whatever it is, like, that's the world you're sort of going to, because you want that drive-by contribution. I mean, you even have YouTubers out there who are like examining code... What if it was like you're on Twitch, and you were examining stuff, and you were a high-profile influencer out there, or whatever it might be...? And they could be touring, as you said this keyword before, touring someone through X, Y or Z.

Jerold and I have talked about this too before, we're like "Let's have somebody give us--" and we've never done this, Jerold. We should do this at some point. I'm sure we've kind of done it in verbal fashion... But give us a tour through your codebase. This is something I think you've done at least once, Jerold, on YouTube, but something we haven't poured deeply into. But Zed could be the primary differentiator, where - it cannot be easy, in a sense. This multiplayer world, this "team" is something to be examined.

**Nathan Solo:** Yeah. And we use the term "multiplayer" very deliberately, because our vision for how people collaborate is a lot more like a video game. Like, we've built the UI like a video game, but we kind of want how people work together to feel like a video game as well, where you're kind of inhabiting, with all the other participants, this world, and you could travel over to someone's working copy, and you're just there, and they're there as well. And you kind of don't care what server the dungeon's on, right? You're in this shared illusion that you're occupying the same reality. And so that's - yeah, this multiplayer environment where people just feel a lot more present and accessible; the interaction feels higher bandwidth, is something that we're going for, where it's not just like an avatar \[unintelligible 01:08:07.26\]

**Jerold Santo:** \[01:08:10.27\] Right. Well, I'm not going to say the M word, but I will say that at some point, Nathan, you might need to rewrite your 2D engine and make it a 3D engine.

**Nathan Solo:** Hah! Yeah, I thought about that. I mean, it's funny, Antonio -- on our site we have this graphic where you see the 2D thing, and then it kind of --

**Jerold Santo:** Yeah, and it turns...

**Nathan Solo:** ...turns down, and rotates, and everything... All the different Z indexes kind of blow out...

**Jerold Santo:** Right.

**Nathan Solo:** And Antonio actually had to wire some code through, because all the Z indexes were sort of fixed, and the perspective transform on the geometry was just like a top-down, and so he added a little code to make it be able to rotate, and do all that stuff, and I thought, "Ha, it would be cool at some point..."

And like another cool thing we haven't even scratched the surface of is like animations. Like, another great thing about Zed is because of the way we've architected it, we can redraw the window anytime anything changes. We do have an idea for sort of reducing the hit area, only filling part of the frame buffer during partial redraws, and stuff... But already, the power efficiency difference... You know, you can sit on a laptop, coding in Zed, for just -- especially one of these new M1s, or M2s, just all day long. It's already so power-efficient. But we haven't done that part yet.

**Jerold Santo:** Right.

**Nathan Solo:** But anyway, we can, 120 frames a second, in burst mode or whatever, run animations. And so I just thought it would be so cool to have parallax effects when you change focus, or something... Or just do some interesting things that are video game-like.

**Jerold Santo:** I would really lean into that, honestly. I would take advantage of the one thing that Electron's probably never going to be able to do, and that you guys are built to do... Because think about it like -- this is what made Snapchat so interesting at first; their filters -- and it's all by definition superficial stuff, right? But it's cool, fun, crazy stuff, that makes it interesting, and people say "What editor are you using?" All of a sudden you have a TikTok where -- I remember there's this VS Code thing where it's like a firework that would happen... And it was cool, and people shared it around. But it's kind of dorky and low-res, and slow, pixelated...

**Nathan Solo:** Right.

**Jerold Santo:** And if you could do really cool stuff, Minority Report style, inside of Zed, just because you can... You know, kind of like how the Teslas can dance, or whatever, just because they're like "Why not make the thing dance? Because that would be cool."

**Nathan Solo:** Right.

**Jerold Santo:** It actually might have some nice network effects, to where people are like "Oh, just go download Zed. You can have it on your computer, too." "Okay, why not?" And then they get there, they're like "Oh, this editor is actually pretty nice. Maybe I'll keep using it." So I think that'd be fun and interesting.

**Nathan Solo:** Yeah, I had that same conversation with myself, kind of, just a few weeks ago, of like "God, that seems kind of frivolous doing something like that", even though I'm like "Well, wouldn't it be cool?"

**Jerold Santo:** Right.

**Nathan Solo:** And yeah, because of how Zed is built, nobody else can really quite do it the way that we can. So yeah... And we've done a lot that is of substance. Another really cool feature we have is this idea of a multi-buffer. So if you run like a project-wide search in Zed, the initial experience is a lot like running a project-wide search in Sublime, where you get this buffer full of the little excerpts. Or at least the last time I ran it. It may have changed since then. But in Zed, you could put your cursor in each of these little excerpts, and just edit. You could have like a multi-cursor edit that like spans across multiple files, and like edit everything at once and hit Save. Or when you're looking at the Rust compiler errors, you see every error in the entire project presented in one buffer, and you could put your cursor at the top of the screen, if you're collaborating with somebody they can put their cursor at the bottom, and you just walk, fixing the errors... Because a lot of times it's a simple thing, and you could just fix it right there. Obviously, you could jump into the whole file to get more context, but you can start at one end, and you meet in the middle. We do that all the time.

\[01:12:13.22\] So anyway, what I'm trying to say is I think there's a lot of investment we've done that's of substantial substance. I mean, that's all we focused on. But it wouldn't be the worst thing to do something cool and fun as well.

**Jerold Santo:** Totally.

**Adam Staravia:** Are you even thinking, Jerold, the Git visual, the one we just covered with, since you mentioned the Mat Ryder show with -- the codename show that we won't mention the codename of... But like the visual sort of like simulation of what might happen if you simulate a Git change, like we talked about? Did you think of something like that even?

**Jerold Santo:** Yeah, that could be a for-instance; that could be built-in, or something. But I was more thinking of even less useful things, that are just rad. So this reminds me -- I know Elon Musk is unpopular, but when the Cybertruck first came out, he did a drive-thru with Jay Leno. Did you guys see this? Where Jay Leno drove the Cybertruck for the first time?

**Nathan Solo:** I didn't see it.

**Jerold Santo:** Okay. So there's a quick clip, you can go watch it on the internet somewhere. And Jay Leno is driving it. He's asking Elon Musk questions. They're driving further. And he's like "This car is bulletproof, isn't it?" And Elon says, "Yeah, it is." And then Jay Leno is like "Why would you want your truck to be bulletproof?" And Elon Musk says, "[Because it's badass](https://www.youtube.com/watch?v=25ZuKkbHdqM&t=173s)." And it was kind of the best answer, you know? It's like, "Okay... Why does Zed do that?" It's like, "Well, because it's awesome!" Isn't that cool? And then turn it back off and keep coding, or whatever.

**Adam Staravia:** Yeah.

**Jerold Santo:** So I think there's value, even though it seems like "Why...?" "Well, because maybe it's badass", and maybe that's what gets people interested.

**Nathan Solo:** And the spirit of fun is just something that's --

**Adam Staravia:** For sure.

**Nathan Solo:** I don't know, that was how GitHub have always felt in the early days. It was just this spirit of fun...

**Jerold Santo:** Totally.

**Nathan Solo:** Tom's motto, "Optimize for happiness. So that's really something I'd like to carry forward. I mean, we're a different crew than those guys were... But yeah, making things fun.

**Jerold Santo:** It's the hacker spirit. A lot of it is just the hacker spirit. Like, we do it because we can, and because we love it, and because "Look how cool this is that I can do this." I don't know, I would lean into that.

**Nathan Solo:** Thanks.

**Adam Staravia:** Let's say folks are listening to this show, and they're like "Man, I have got to take the next step."

**Jerold Santo:** I hear it's bulletproof. Zed is bulletproof? \[laughter\]

**Adam Staravia:** I hear it's bulletproof... Your early innings, you're still trying to win the minds and hearts, and you're even early on that, by your own admission... So set the expectation for someone listening to this show, going right now to Zed.dev, trying it out for the first time. What's the expectation? What are you trying to do? What should they do?

**Nathan Solo:** I mean, download it, give it a try... But in terms of the expectation, of what you should expect to experience, we've been building Zed in Zed For about a year. Zed is written in Rust. I freakin' love using Zed to write Rust, on Zed, just the way that we present the diagnostics... So you should expect a pretty solid experience if you're writing Rust, first and foremost. And I've got -- I haven't written a ton of TypeScript in it, but our website's written in TypeScript, and it's quite good there, and we've gotten good reports for that experience.

So we've got an integrated terminal, I'm really proud of our UI, it's very minimalist, out of your way... And the performance - you should experience it as best-in-class. We've got a feedback widget built into the tool, and if that isn't the case, please let us know, because that's one of our top priorities. So you should expect a very sleek, well-designed editor, that stays out of your way, with very good language server integration for the languages that we support, which is -- God, I don't want to rattle them off; we'll list the languages we support in our docs. But Rust, TypeScript, Go, C and C++, Ruby, Python... I'm sure I'm missing some. Elixir... And - yeah, for the languages that we support, it's fast, it's clean... You should enjoy it.

\[01:16:20.26\] We don't have a debugger yet, so if that's super-important to you, then you may need to wait. And we'll keep blogging as we fill these gaps. And we really want to get people's feedback. We read it all. We've also been experimenting with using AI to just like help us ingest all the feedback. So we have like a community repo where people can open issues and engage with us that way... And there's just like a fire and forget launch us feedback, right inside the tool, that you can just basically type as much or as little as you want, and just shoot at us, and we'll be reading it all.

And... Yeah. So again, I love using Zed. Does it do everything that all the other editors do yet? No. I mean, it's still in beta; there's still a ways to go. But I don't know, I don't ever want to use any other editor. And for me, the reason is just the performance is really addictive. I didn't know, when we were investing all this energy into like making it really, really fast, how I'd feel about it. I just had this instinct, like "Let's just do whatever it takes. Let's make it insanely fast." But I don't know... Just that feeling of it never getting in your way, there never being sand in the gears. Just like, you type a key and it just tears away like tissue paper. It's not putting up any resistance to your thought stream... Yeah, once I got used to that, like, I didn't want to do anything else. So I put up with not having a debugger, because I want that.

Everybody has different values, and it's a vector, what people put their weight on... So this is my set, but if that's something that sounds compelling to you, I would love for you to give it a try, and give us your feedback.

**Adam Staravia:** There's something to be said about fast tooling. Fast tooling is fun to use... My dog's barking in the background, for whatever reason. Who knows why he just decided right now to bark... Whatever, Rex... That's his name. Fast tooling is so fun to use, obviously. Right? I mean, when you have a fast tool, you're like "I want to use that thing--" Shut up, dog... More often! \[laughs\] Gosh! Get out of here, Rex. Stop barking. But that's so cool.

Hey, one -- I was thinking about the conjoined triangles of success, because I can't get through a podcast without mentioning Silicon Valley... Do you have -- and it's a shtick in this one here... It says "The conjoined triangles of success...!" Anyway. Do you have a mission for success? I've got to imagine, while we mentioned the W and the L earlier in terms of Atom, you got the L there, your effort wasn't an L obviously, but the effort... It's sunsetted.

**Nathan Solo:** Yeah. But I would also call, like -- what I'll say though about the Atom thing... Sorry to interject.

**Adam Staravia:** That's okay. Please do.

**Nathan Solo:** I view it as an incomplete success personally, in the sense that what was an L is, from my perspective, I ended up never feeling like it truly realized my vision.

**Adam Staravia:** Yeah.

**Nathan Solo:** But on the other hand, there were kinds of 2 million people writing software in the thing...

**Adam Staravia:** For sure.

**Nathan Solo:** ...a month for a while there. So it's it like, it did have utility for a time. Anyway.

**Adam Staravia:** I'll take that. I appreciate you saying that. I'm not saying that to say it was an L. And I agree. It was just --

**Jerold Santo:** You said it was an L, Adam. You called it an L.

**Adam Staravia:** It was the basis for my next point...

**Nathan Solo:** Sorry...

**Jerold Santo:** \[laughs\]

**Adam Staravia:** But I do agree. No, I love that. Please do. I mean, I'm not trying to like to belittle anything whatsoever.

**Nathan Solo:** But it fell short. It fell short of what we wanted it to do.

**Jerold Santo:** It could have been more, yeah.

**Adam Staravia:** \[01:19:51.28\] I think an incomplete is probably a better -- so it's like, did you fail the test? No, you got an incomplete, because you couldn't complete the mission. You even said that you didn't have the authority to sort of direct its direction, so you were sort of hamstrung. But the point I'm trying to make is, to be successful, this mission of success, if that is a thing for you, what is the first thing you're going to go after? I assume, since Sublime Text is the second one on the list in terms of who you compare yourself to performance-wise, which is the hallmark that you've talked about, and we've talked about here, multiplayer is obviously the next best thing, of course... But is your current mission to win the hearts and minds of Sublime Text users?

**Nathan Solo:** I mean, that's a perfect way of framing it... And I'll have to give it some thought; I hadn't thought about it through that lens, but I think that does make a lot of sense. I think we're well positioned to do that, but perhaps not entirely there. I mean, the challenge we face is you just look for 100 miles in any direction, and there's \*beep\* to do. So what do we do first? And I think that's a fascinating way of framing it.

**Adam Staravia:** It's like dominoes, right? Like, one topples, as they go, for obvious reasons, because of gravity, and kinetic energy, and all that cool stuff... But what's your first domino, right? You've got to take somebody out. So there's got to be -- that's why I mentioned the W and the L. To get a W you have to cause somebody else to have an L...

**Nathan Solo:** Build momentum.

**Adam Staravia:** Gosh, this analysis is just the worst. I'm not trying to hurt people's feelings.

**Jerold Santo:** Yeah, you have to get \[unintelligible 01:21:21.07\] because you can't attack everywhere at once, like you said, Nathan...

**Adam Staravia:** Right.

**Jerold Santo:** ...there's just so many things. I think it makes sense, because Sublime Text users - as one, I'm more likely to try out Zed because of the performance than I would be to try out some flashy new Electron thing, because of the non-performance. For instance, I've already chosen Sublime Text, even though I know VS Code has way more features that everybody loves... But for me, that's something that's the most important. And so if I'm using Zed, I'm like "Wow, this is silky smooth, even better than Sublime." Now I'm starting to consider sticking around. But then the second question, I'm like "Okay, but what about all my custom stuff that I do?", that you don't realize in the first 15 minutes, but you realize in the first eight hours of using a tool... So I'll be emailing Nathan tomorrow and say, "Hey, you know what would be cool? If Zed did this."

I think it'd be extensibility is going to be a big thing that Sublime Text has going for it. There's a large community of things that have been built for it, and it even inherited a bunch of stuff from Sublime Text with the theming, and stuff. It has a bit of pretty big beachhead there.

**Nathan Solo:** Yeah.

**Jerold Santo:** And I know that's on your list, extensibility, and multiplayer. So certain camps are gonna care about certain things more. I think Sublime Text people will care about speed and extensibility, much like Vim and Emacs people will. VS Code has extensibility, too. I mean, there are so many stinkin' extensions for VS Code...

**Adam Staravia:** Yes...

**Nathan Solo:** I'd say that's their biggest \[unintelligible 01:22:48.28\] It's just the long tail of all the extensions that have been built for them.

**Jerold Santo:** Yeah. And the thing that VS Code also has, which - Atom had this; it was just the batteries-included aspect. Like, it comes out of the box ready to use. Zed seems to have some of that going for it.
The thing about Vim - and I'm a longtime Vim user - is Vim people and Emacs people, they love to configure the crap out of it... Because you kind of have to. Like, it's going to come out of the box, and you're like "This experience needs some help. I'm going to help it."

**Nathan Solo:** It's an editor kit.

**Jerold Santo:** It is. And I got tired of that. Like, I would love to just hit the thing in my doc and have it launch, and then have it be usable, and then I can extend it from there...

**Adam Staravia:** For sure.

**Jerold Santo:** ...which VS Code has going for it, and I think Atom had that going for it. I think Sublime Text does as well. And I've not used any of the JetBrains stuff.

**Nathan Solo:** But it took us some time even on Atom to do that, because we were so focused on the extensibility over almost everything else.

**Jerold Santo:** Right.

**Nathan Solo:** So I don't know, Atom did have some batteries included, but not enough. So that's kind of still what we're focused on, getting enough of those batteries included to feel like we've really got the core in place before tackling extensibility. So we're still figuring it out. I think getting it out there and letting people try it and give us feedback will be very informative.

**Jerold Santo:** Well, we're rooting for you. I always root for the little guy.

**Nathan Solo:** Thanks.

**Jerold Santo:** I love David over Goliath. I think you have definitely a great start. You have the experience. I love how fast this thing feels in my hands.

**Adam Staravia:** And the history.

**Jerold Santo:** And you have the history.

**Adam Staravia:** You're new, but you're not new.

**Jerold Santo:** That's right. But you've got a big battle ahead of you, and we'll be rooting for you.

**Nathan Solo:** Yeah, we've been fighting this fight for a very, very long time, so... I mean, I don't really view it as a fight. Like, we're just trying to do our thing, and do something that matters, and do something we love, and make an impact. But I get it; at a given moment, a developer's not really using two code editors, they're using one.

**Jerold Santo:** That's right.

**Nathan Solo:** And there's a finite number of developers. So to that extent, it is a fight. But yeah, hopefully this resonates, the vision I put out resonates with people, and will give us a try, and stay tuned to what we're doing and what we're trying to do.

**Adam Staravia:** Very cool. Alright, you all... Zed.dev. Code at the speed of thought, high performance, multiplayer, extensibility, whiz bang features that don't even matter, potentially, because Jerold recommends them...

**Jerold Santo:** That's right. Coming soon. \[laughter\]

**Nathan Solo:** The extensibility piece...

**Adam Staravia:** Yeah. Well, it's on the mission plan, so there you go.

**Nathan Solo:** Exactly.

**Jerold Santo:** That's right.

**Adam Staravia:** That's part of the promise. I think if you go there for that, and you like what you have there, then you know where the promise is going. So Zed.dev... Nathan, it's been awesome having you. Is there anything we didn't ask you? Is there anything that's left unsaid?

**Nathan Solo:** Probably, but... Yeah, I think we're pretty good. \[laughs\]

**Adam Staravia:** Okay.

**Jerold Santo:** \[laughs\] We appreciate you coming back on the show.

**Adam Staravia:** Until next time. We'll have you back again.

**Nathan Solo:** Yeah. I appreciate you having me.

**Adam Staravia:** Yeah. Awesome.

**Nathan Solo:** Cheers, guys.

**Jerold Santo:** Cheers.
