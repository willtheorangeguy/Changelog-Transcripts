**Jerold Santo:** So we're here with Nikita, who's the author of Facade, a free monospaced font with programming ligatures. This is Maintainer Spotlight; we would like to thank Ollie for pointing us to Nikita and Facade... And Ollie said, as a Facade user and repo lurker - aren't we all a repo lurker of somebody's repo...? He said "I've been impressed by Nikita's flexibility and consistently patient conduct on a pretty busy repo. I'd love to hear more about his broader thoughts and perspectives on what seems to be a very popular project. Programming fonts are an interesting collision of niches I have not heard discussed on a podcast", so I agree with that. I don't think we've ever talked specifically about fonts; maybe Font Awesome, something like that... But it's been a while.

**Adam Staravia:** It's been a while, yeah.

**Jerold Santo:** And for Maintainer Spotlight - first, Nikita, thanks for coming on The Changelog with us.

**Nikita Protocol:** Sure. Happy to be here.

**Jerold Santo:** So you live at the intersection of fonts and code, and I'm just curious how you got here and why this was something you wanted to work on.

**Nikita Protocol:** This is an interesting question... Professionally, I am a software engineer, but I've always been interested in design as well, and I've been reading about design, doing some logos, some stuff like that... And inspired from design, I was also naturally interested in fonts. Then there was this idea -- there were already fonts with programming ligatures; it was called Hatchling, but it was aiming at Haskell only, so I figured "Why not create my own font that I like?" and with ligatures that I can use in the language I was working in.

It turned out not to be too hard, and after the initial version there were many other versions, and I got more and more sucked into the world of fonts, how they're built, and what details I've learned... So yeah, I just started, and then I got into fonts; I guess that's how it was.

**Jerold Santo:** It sounds like a rabbit hole you can go a ways down. I've always been on the fringe of fonts, reading people's blogs who were interested in topography. I've never quite known what makes a good font, or why I like a certain one... Adam, you're keen on topography; you're always talking about specific fonts you like, and ones that you don't like... What's your angle at this, Adam?

**Adam Staravia:** I think I'm not keen...

**Jerold Santo:** Oh, you're not? You have some taste about it though. You care.

**Adam Staravia:** \[03:58\] Sure, I have some tastes... I'm not on the fringe or in the know of what's current, less so now, but I think with monospaced in particular - they're unique because they have to serve a certain purpose... Readable, certain size, similar size, they've got to fit into terminal windows, and there are unique properties for monospaced fonts in particular... And you want to put some style in there, but yet, it's a very constrained design pattern to design towards. I like the fact that they're so creative and so diverse, given those constraints.

**Jerold Santo:** Yeah. Things that I've always looked for in a programming font specifically - of course, monospaced is a necessity, because you need to line your code up, right? Indentation, and code alignment - these things are...

**Adam Staravia:** It matters.

**Jerold Santo:** They matter for readability, so you have to have monospaced... So they all do have that. But what I've always looked for in a font for programming is disambiguity. I want something where I know "Is it a zero or an o? Is it an l or a 1?" Not really a big problem if you're reading prose, because your mind can read it, whether it's a zero or an o, and contextually it makes sense. There's no zero in the middle of a word.

**Adam Staravia:** Yeah. It's pretty clear too when you're reading text...

**Jerold Santo:** But in programming there are zeroes in the middle of words, right? A variable name can have a 0 in it, or a 1, and if that's an l or a 1, that's a huge difference. Your code may not compile, or in specific languages maybe it works just fine, but your variable ends up empty, or nil, or something... So those are always things that I look for, and Nikita, you surely have a lot of thoughts having built your own font... We'll talk about ligatures here soon, because I think that's worth focusing on, but what do you think makes a good programming font, or what do you like in fonts in general?

**Nikita Protocol:** Certainly all the things that you mentioned are important... Yeah, mostly it's 0/o, and 1/l, stuff like that. I, l and 1. These are things that must look different in the fonts. But apart from that, I think it's just a matter of taste. At some point, I was looking for a perfect font, but then I found Diamond and built Facade out with it. I liked the aesthetics of it, how the letters look, and the letter shapes themselves... But also, later I discovered maybe there's not a perfect font, and like a desktop wallpaper, you just have to change it once in a while, because it gets boring a little bit.

**Jerold Santo:** Right.

**Nikita Protocol:** There's certainly high-quality fonts, low-quality fonts, that look decent, that look terrible... But from high-quality fonts - yeah, sometimes I just switch things just to make it stay fresh.

**Jerold Santo:** To keep it fresh, yeah. I mean, it definitely is at a certain point an aspect of taste, and our taste changes over time, and we get bored with what we're looking at, for sure. There's a somewhat new trend in programming fonts, especially amongst people who share their screenshots of some code on social networks, which I'm curious what you guys think of this. I'm still not sure where I land, but it's where the comments are like serifed, or curly... Or even in some case the comment is like a completely separate font, and it's... Script, I guess is -- I don't know what the term is; I'm not a font person.

**Adam Staravia:** Really?

**Jerold Santo:** Yeah. So you have the monospaced -- and maybe it's still monospaced, but it's just a completely different style, the comments and then the code. Have you seen that, Nikita? What do you think about that?

**Nikita Protocol:** Yeah, yeah. It's implemented as italics, but yeah, there's really curly italics. I think it's Victor Mono and \[unintelligible 00:07:36.19\] There are two fonts like that. I'm not using those... Furthermore, I don't even use italics in my coding at all, and I don't use bold fonts.

\[07:49\] I also have not only tasted for fonts - or an opinion, not only for fonts, but also for colour schemes. I prefer all the text be the same font, the same width, weight... So no bold, no italics, just the same letters over and over, with some colours.

I've seen that italics and bold make actually text harder to read, because you have to switch. When everything is in the same font and the same weight, it's just easier to read for me. So yeah, I am not using those.

**Jerold Santo:** I'm not using them either. I tend to fall in with you.

**Adam Staravia:** Yeah. I can see though for the social network aspect of sharing code like that, too. It's--

**Jerold Santo:** There's a flavour to it, yeah.

**Adam Staravia:** Yeah. I can see why separating and having a distinct style, and potentially even getting -- and maybe that's just a thing for being unique, to make the comments be more stylish... But they definitely stand out.

**Jerold Santo:** Right. It kind of reminds me of the way that TV sets are configured inside department stores, versus inside your house. You go to a store, and you have all these TVs, these large-screen, flat-screen TVs, and the brightness and the saturation are all cranked to the max... Because they're trying to catch your eye, they're trying to stand out. It's actually not the best picture that that TV is capable of, that you would actually want to watch. Like, if you're watching a movie, you would not want those settings. So you take it home, and you have to actually configure it for that environment, and maybe this kind of flare, fantastic, curly comments, with bright colours, is kind of like just catching attention on social media. I'm wondering if people that do that use that day to day, in their regular coding, or if it gets to become too much. Because I sure think it would bother me over time.

**Adam Staravia:** Well, yeah, it'd be distracting. Your eyes would be attracted to the comments more than the code.

**Jerold Santo:** Or you'd have to squint a little bit sometimes to read the comments, because they're curly -- or they're italicized. I keep calling them curly, showing how lame I am. Those kids and their curly comments...

**Adam Staravia:** \[laughs\]

**Nikita Protocol:** I think IntelliJ right now is also experimenting in the latest versions rendering comments in proportional fonts; not monospaced, but proportional... Because it's easier to read, and comments \[unintelligible 00:10:02.00\] and not the code that you change. I'm not sure how useful that is, but there's a lot of design space for experimentation. You can do crazy things, what you want, in which font.

**Jerold Santo:** Yeah, absolutely.

**Adam Staravia:** And you mentioned the word "high-quality" before, and I think the word high-quality comes to play when you say how much time and effort did someone put into the font itself to be represented in all these different scenarios. So you can just go and design a font, or put together a font, and not put a lot of time into it; and it's not so much that it's not high-quality, but if you took all the effort to provide the ligatures, or the unique scenarios where there are contextual opportunities and stuff like that - putting that time into a font or a typeface... And that's even a debate there - is it a font, is it a typeface? But putting the high quality into it is really a craft. A lot of effort and a lot of painstaking time in most cases, by one or many people, to really make sure that this typeface performs well in its designed arena.

**Jerold Santo:** In different environments, yeah. So Adam, you mentioned ligatures, and we haven't talked about that. That's a huge part of Facade, is the ligatures... And I didn't even know what these were a few months ago. I've seen them a few times now; here we are again, and now I get it... I'm not sure if I would want it myself, I haven't tried it yet. Furthermore, I've just installed this morning, and I'm checking it out. Furthermore, I haven't lived with ligatures... But explain what those are to people who aren't familiar with ligatures in your code.

**Nikita Protocol:** Sure. So the idea was that in traditional fonts there were certain letter combinations that was not rendered nicely together. If you have f follow by i, the dot of the i and the edge of the f would overlap, and it doesn't look nice... So they figured out that they will draw this pair separately and replace the combination with specifically drawing pairs that smooth a little bit this overlap. This was in fonts like forever; I think in Metallic fonts this was used as well. It comes from Metallic fonts in real typography. And this was in computers as well, but it only was used for really rare combinations like phi, fl, FFI, stuff like that.

\[12:32\] And then - I don't remember the name, but somebody figured out (the guy who built Hatchling font, I guess) that you can use the same technique, but for programming stuff... And if you think about programming -- not letter combinations, but symbol combinations... Like for example in C or C++ you have dash follow by greater sign, which kind of looks like an arrow, but is not an actual arrow. In some fonts, normally these characters are not even supposed to stay next to each other. So they are not even aligned. So the dash is like minus between numbers, and greater is also supposed to be between numbers. They're not supposed to stay next to each other...

Yeah, so sometimes they look not well together.

So the idea was to find these combinations, the most popular ones, and replace them with the same mechanism, but for example in case of C or C++ arrows, we actually draw an arrow. It's a single glyph that looks like a decent, beautiful arrow.

So that idea that in the places where you're doing ASCII art in your code, like with arrows, or ++, or I don't know... For example in Go you have colon followed by equals, which is assignment operator, stuff like that - we just make them look slightly better together. So it's basically optimizing these combinations for programming. That's what it is.

**Jerold Santo:** Yeah. And as I browser Facade in my editor here, it turns out you have to also turn on the ligatures explicitly... So I thought I was looking at them and I then wasn't, and then I turned them on inside -- this is VS Code-specific, but there's an actual font ligatures boolean config; in addition to setting Facade as the font, you then can toggle whether you want the ligatures... And with ligatures on, especially in Elixir, one of the combinations that's popular in Elixir code is the pipeline operator, which is the pipe character, followed by greater than character. And it's kind of like an arrow in that sense... I'm sure you're well aware, because it looks like you designed this ligature for that...

**Nikita Protocol:** Yeah. It looks like a triangle, actually.

**Jerold Santo:** It does. It looks like a sideways triangle. So when I turned on font ligatures, all of my |GT; combinations all just switched to an actual triangle; a right-pointing triangle. Hard to describe it in voice, but there you have it. So how many of these are there? Are there like dozens, are there hundreds of these combinations?

**Nikita Protocol:** Yeah, I think there are hundreds. I think Facade has around 100, or 150. Something like that. I have a script that generates them, and I'm trying to remember the numbers; I think it was something like that.

**Jerold Santo:** Sure. Quite a lot.

**Nikita Protocol:** There is a lot, yeah. And regarding your mentioning that you have to turn them on - actually another story here was when we started building fonts like that, it turned out that not every editor was ready for that. Almost nobody supported it, except for web-based editors. So in web typography was designed properly (for web pages) and every editor built on top of Electron was also supporting them.

Then the idea became popular and everybody starting doing them... So right now it's at different levels of support in different editors. Sometimes you have to turn them on, sometimes it's enabled by default... But yeah, it's a thing.

**Jerold Santo:** \[16:19\] Yeah. And worth noting, if this is something that's new to you as a listener - and this was new to me, and I was immediately turned off, because I thought "Are you replacing my text with a Unicode character that represents it?" Because that, I do not want. I do not want to have maybe non-standard - I guess if it's Unicode, it is a standard... But I want to have the actual thing as written. So it's worth noting that the way that you accomplish this is basically a presentation layer thing. You're not replacing the underlying bytes, the characters. You're actually just presenting them. Correct?

**Nikita Protocol:** Yes, that's correct. That's the idea with... This is why it all works so beautifully, because you can see beautiful, Unicode-like -- it's not Unicode-like, but beautiful, specifically drawn shapes in your editor, and your compiler still understands this as plain ASCII characters. So yeah, there's no conflict there; you just see it slightly better than it is in underlying Unicode inside.

**Adam Staravia:** You're going to have a divide there too, right? You're going to have somebody who prefers to literally see two equals signs next to each other, versus an elongated equals sign, or whatever that might look like in its ligature representation. So you might even have somebody who's like a purist, who's like "I want to see the individual characters, and the visual representation doesn't matter to me." And you're going to have some who are like Jerold, who was immediately turned off, because he thought you were replacing, but you're not... And then it really is just a visual. So Jerold, on the Elixir side, is that sideways triangle the visual representation to you -- well, it takes some time, but do you think over time you'd appreciate it?

**Jerold Santo:** I'm not sure yet, because it might take some time... I literally just toggled it on -- and I am kind of a curmudgeon; I'm not unhappy with my fonts, my text scenario, my colours... And I also don't get bored very easily in this way, that maybe others do. Nikita, you mentioned there's boredom, so something fresh -- I've been using Ubuntu Mono at the same size, with the same colour scheme, for probably... Well, maybe I would change colours, but definitely Ubuntu Mono, whenever they announced it, I just used that. I like it, and I just use that.

**Adam Staravia:** A decade.

**Jerold Santo:** And so actually switching away from anything makes me a little bit like "Oh, this is weird..." But I think, looking at these sideways triangles, it's kind of cool. I understand how aesthetically it's kind of more interesting... I know in your README, Nikita, you talk about there's some sort of minor brain wins in terms of cognitive overload with this... Maybe you can explain that from your perspective, of why ligatures are actually like -- just because they're slightly more representative of the glyph, or what?

**Nikita Protocol:** Yeah, so the idea is that if you type two characters to build a single operator, your brain has to sync with as "Okay, I see two characters, but it's actually part of a single thing, a single operator. And then if you just see a triangle, an actual triangle, without any gaps - it's just a single thing, so it's easier for you to like "A-ha. This is a single thing."

I like \[unintelligible 00:19:41.20\] it makes it closer to mathematical notation. If you wrote some equations on a paper, or in a typographically well-set paper, you would use beautiful characters that look the way they're supposed to look. And if you just type in code in ASCII, you're just trying to imitate that, but you have very poor tools, so you cannot build an arrow. It just looks better. It's not a game-changer at all.

**Jerold Santo:** \[20:20\] Right.

**Nikita Protocol:** You will not write better code with it, and I am not advocating that it's a must-have...

**Jerold Santo:** Dang it! I'm looking for wins.

**Nikita Protocol:** It's just nice to have -- I don't know why would you want to look at simpler, not beautiful, broken glyphs, not aligned properly, when you can be looking at the same thing, but rendered much nicer.

**Jerold Santo:** I get it. There's maybe a nice comparison with emoji and emoticons. In the bad old days, when we wanted to emote something, when we wanted to wink at somebody, we'd put a semicolon and then a right brace... Or bracket? A parent. A right parent.

**Adam Staravia:** Parenthesis, yeah.

**Jerold Santo:** Yeah. And that would be a winch face. Then emoji came around, and now we have these very nice, very expressive yellow - or whatever your colour of choice -w inky face. The big win in that case is you don't have to turn your head sideways to actually see what you're trying to emote, as the semicolon is necessarily at a 45-degree turn... So that's a win. And I think it's a similar argument here, and there might be similar pushback. I've used the semicolon parent for years, even once emoji were out there. And over time, you just get used to the emoji, and you're like "Yeah, this is just better. Why am I not just switching to that?" And eventually, those pretty much have gone by the wayside. There's still people that put them in certain contexts, especially when emoji is not supported... But it's better, pretty much objectively, to have a more expressive glyph that represents that thing, versus cobbling together a representation.

**Nikita Protocol:** Yeah, I can actually put it another way. In a perfect world, if your language of choice would support Unicode arrows, and you would have a decent way to type them in, also Unicode arrows, you'd probably use those. Nobody would build an arrow from dashes and greater than signs.

**Jerold Santo:** That's right.

**Nikita Protocol:** It's just an approximation, an unfortunate one, but it works; it works easily, effortlessly... So yeah, why not?

**Jerold Santo:** Yeah. We're using the lowest common denominator solution based on the availability of ASCII in different languages or different areas, and then also the fact that you just can't fit all of those glyphs on the keyboard, unless you have specialized keyboards, and we know around the world there are keyboards that are wildly different from the standard QWERTY keyboard, especially for character-based languages, and stuff.

**Adam Staravia:** Yeah. You said the word "if", and there's quite a big if here, on language-specific glyphs. So JavaScript's got some HTML markdown; Java, C\#, Ruby, Go, Swift, we mentioned Elixir, Kotlin, R... So you've taken some time pretty much down the swathe of languages being used today to give them special representation for certain things they're doing inside their syntax... And that's fascinating. And even go beyond that, to do things like \[unintelligible 00:23:17.28\] When you were just mentioning where would you use this, I was thinking it could be super-cool to have these kinds of things whenever you're writing a CLI and something's happening, or you're doing some console stuff, and you have an opportunity, let's say like a module installation with NPM, or something like that. When something's happening, you can do some really cool \[unintelligible 00:23:35.29\] squares, partial boxes, some really cool stuff, really cool art with this type of font typeface, over say Ubuntu Mono, where there's just not that opportunity.

**Jerold Santo:** \[23:51\] Yeah, similar to -- Curl has that new spaceship progress indicator, where it' an ===GT;, and that's the ASCII version of a rocket ship. But if you actually had a font like this, that had accounted for a rocket ship as like a thing, then that could just be translated on the fly into something that looks much more like an actual spaceship, or rocket ship. I'm curious --

**Adam Staravia:** It could be edited even. You can be swapping out characters behind the scenes and it becomes very animation-like.

**Jerold Santo:** Maybe. I was going to ask Nikita about that, because I'm not sure how these things are built. How do you go about achieving this in a font?

**Nikita Protocol:** Actually, the one that you mentioned, with the progress bar, is a really new feature; it was released last month...

**Jerold Santo:** Oh, cool.

**Nikita Protocol:** ... FiraCode version 4. This actually was a tricky one... So the way Facade works, or any other font works - inside the font there is a small programming language that lets you program replacement... And ligatures work through that -- it's basically pattern-matching-like. So for ligatures to just say "If you see -GT;, replace it with this glyph, or with this name." This is simple stuff. But you actually can do more complex stuff, and you can do loops, or stuff like that.

The way it works for long arrows is if you see a dash that is followed by a dash, followed by a dash, you start converting the first dashes into a line, and then this process goes on and on, and it converts them as it goes, and at the end it just puts some ending, like an arrow, or something like that.

So yeah, it's actually a little program inside a font that can do different things; maybe some crazy things... The craziest one for now from Facade is long arrows. You can have arrows of any length, and you can have in the middle also have greater signs, or pipe, or stuff like that; a vertical line...

I think there was also an article a few months back when a guy built -- using the same open type features he built number separators inside the fonts. For example, if you type a long number, like 6 or 9 digits, it will automatically put commas or spaces in between groups of three digits... But it will do it on the font level; it will be purely presentational, just like ligatures are. You can do stuff like that inside the font as well.

**Adam Staravia:** When you sat down and said "I wanna design this font from scratch", how did you begin? What was the first step? What was your blank canvas, what were the constraints you put on yourself? What were some of the key things you were really shooting for? Ligatures - obviously, we've been talking about that, but what were the other aspects that really brought you into play to do this?

**Nikita Protocol:** As you said, when I started, it was just an experiment. There was the Hatchling font, and had ligatures for Haskell. I wanted the same, but with a font that I liked at the moment, which was Fire Mono... And for ligatures - I guess for Clojure, because I was programming Clojure \[unintelligible 00:27:25.19\] maybe. Yeah, so I just took Fire Mono, which had all the letters, so I didn't draw any of the letters, and just added ligatures on top of that. So in a sense, it's just an extension of Fire Mono. That's what I worked with.

**Adam Staravia:** How do you accomplish that then? Are you iterating based on Fire Mono, and you've got the -- like, how a language might have a superset or a subset, or is it like that where you're sort of building on, and you're in tandem with their development of that font?

\[28:04\] Are you drawing the vector versions of all these characters yourself by hand, or did you use some sort of base layer of work and added onto? And is your work tied back to theirs, and has to wait till they iterate so you can iterate and add on...? Are you still connected to the original Fire Mono somehow?

**Nikita Protocol:** Yeah, sure. The first ligatures - yes, I have to draw all the vector forms myself. It helped a little bit that, for example, they already had arrows, Unicode arrows, and I just extended them a little bit; so it's a simple operation. But some of them I had to draw from scratch. So basically you just open a file, which is a set of vector shapes, you add new glyphs, and you have to draw a vector shape for those glyphs. For example, if I want an arrow, I draw an arrow. It usually comes in two weights, so you have to draw it for normal and for bold, and then the software interpolates for all the other weights...

I left the letters from Fire Mono as they are. We fixed a few bugs that they had in Cyrillic, I think, or some rare languages, let's say that... Basically, right now Facade has letters from Fire Mono a while back. Luckily for me, I guess, they're not iterating, they're not changing Fire Mono anymore, so I don't have to keep up. It would be probably pretty hard in there, because if they change metrics or something like that, I will have to adjust all my ligatures, and I have just so many of them, so it would be tricky... But yeah, let's say it has a snapshot of Fire Mono from 4–5 years back, and I am just building on top of that. Every new version of Facade is just more and more ligatures, with sometimes bugs fixed, sometimes new Unicode characters... Sometimes something gets removed, but yeah, it's basically just adding slightly on top.

**Break:** \[30:29\]

**Adam Staravia:** Well, thankfully the source is out there for this stuff, because without it, you'd be starting from scratch... There's a repo out there for Fira Sans, that's got Facade, Fire Mono, Fira Sans in there; some of them kind of dated in terms of their last commits to them... Facade and Fire Mono being four years ago, Fira Sans being two years ago. Thankfully, this is open source, and you can improve upon this work.

**Nikita Protocol:** \[31:48\] Yeah, so the biggest luck for me was that it was open source; it was Open Font License, so anybody can build modifications and distribute them freely. The original work on Fira Sans was done by Ralph du Carrots, or something like that (I'm not sure how to pronounce the name) and Erik Spiekermann. They built it for Firefox mobile operating system. I think it was called Firefox OS, or something like that... So it was supposed to be the default font on Firefox OS. But then Firefox OS didn't happen, but the font already was built, and it was openly distributed, and it had monospaced, and I was lucky just to have it.

After that, they tried to update it, I think twice. They built -- I think the Fira Sans that you mentioned from two years ago was the first attempt; then they formed a different company and rebranded it as Virago. It's basically Fira Sans, but updated again. So the Virago is recently newly updated. Fire Mono wasn't really updated since 4–5 years back. It doesn't get new versions anymore.

They released though at some point a version called Facade, which is just Fire Mono with different line height. Not ligatures, nothing at all. They just chose this name, for some reason. I don't know. I don't think anybody uses that, and I think Facade was already very popular by then. Furthermore, I asked them to change it, and they don't seem to respond... So yeah, I don't think it matters much.

**Adam Staravia:** I'm not sure how popular Wikipedia is for people looking for the history on this, but I assume it might be to some degree popular, because we use Wikipedia for history, in some cases... So I would say -- that's where I was confused, because I saw a Facade mentioned in the Fira Sans Wikipedia page. It didn't seem like it was referencing anything in particular, because it didn't link to the proper place. Where I went didn't have anything representing Facade. However, we're obviously talking about Facade here today, so maybe do an edit on the Wikipedia page and point to yours, so we can have some clarity out there for anybody looking.

**Nikita Protocol:** Yeah, maybe. Yeah. That sounds good. But in terms of Google search, I think Facade is fine. I think it all leads to the proper GitHub page, my GitHub page. Also, on Google Fonts there's Facade and Fire Mono, and Facade is my Facade, not that version, so...

**Adam Staravia:** Oh, nice.

**Nikita Protocol:** So it's all fine, yeah.

**Jerold Santo:** Is that something that you submit to, or did they come to you and say "Can we put this on Google Fonts?" How did that work out?

**Nikita Protocol:** I think I submitted, or somebody from Facade community submitted it. There is actually a little story there... So when I started Facade, I had -- like, in Fira Sans and Fire Mono license they have a phrase that "We license the name Fira Sans and Fire Mono." I'm like "Okay, I will just name mine Facade." And it was fine for a while. Then they changed the license Fire prefix, and "All fonts with Fire are ours." I'm like "Oh, no! What do I do?" And because of that -- a few years they didn't want to take Facade to Google Fonts, because this question was questionable... And it was really hard to contact anybody from Firefox or from box Type, even just to look at that. They didn't want -- they're like "We don't have time to look at it."

**Jerold Santo:** Right.

**Nikita Protocol:** After a while everything got cleared up. They changed the license again, so... After that, Google Fonts was happy to take my font. They actually also do some drop on it. It's not like I submit my font to them. Actually, a guy came to my repository, wrote a bunch of scripts that build font properly, and stuff like that... And only after that, they host some version. I think it's also not the versions that I distribute, it's the versions they built from my source.

**Jerold Santo:** Interesting.

**Adam Staravia:** \[36:17\] That's an interesting question though, Jerold, because I was thinking earlier, if the barrier to entry -- like he'd mentioned, he's a programmer primarily, but curious about design, and in particular fonts and typography... And the next question is adoption. So if he puts them out there, you've got to define all these installation instructions, and this and that... But if you're using Google Fonts - and that's pretty common - you can use that for desktop AND the web.

So it can be, in many ways, access to a large population of people who are font-curious and they want to try things out... So the way you get adoption is by having distribution. I'm thinking "How do you get distributed?" Well, it sounds kind of backwards though, because it seems that they should be working more closely with you to ensure that your desires for it are fulfilled through Google Fonts... And it seems like they're not exactly collaborating with you, they're just sort of using your source and doing their own thing with your stuff, which is totally fine - license and legally, and whatever...

**Nikita Protocol:** No, no, no. Maybe I put it wrong. They did come and do a bunch of fixes and cleanups, as a pull request, and I merged everything in Facade source... So it's all in there. But they also contributed build scripts, and -- yeah, I don't know... I just didn't have them. I went into the Glyphs App and clicked Export, and got a file from it...

**Jerold Santo:** Yeah, they automate it.

**Nikita Protocol:** ...they change it to command line... It's all fine. We talked, and we closed a couple of issues... There was communication.

**Adam Staravia:** Gotcha, okay. I misheard then. So when you say "they", do you mean somebody that represents Google Fonts? People that manage their library etc.?

**Nikita Protocol:** Yes, I think there was a person, a guy who was communicating with me. So yeah, I worked with them. I'm just trying to remember -- I think that he was called Steven \[unintelligible 00:38:14.00\] or something like that. If it's wrong, I'm sorry. But yeah, it was a collaboration.

**Adam Staravia:** Well, I was just trying to figure out how that happened, because it's like -- if somebody else out there is like you, what can they expect, how does it work...?

**Nikita Protocol:** I think if you want to initiate that, you can leave a request or issue in the Google Fonts repo, and then from that you will know what to do; they will tell you what to do. He also mentioned distribution, and I'm not sure that Google Fonts is that perfect for distribution... Because there are lots of fonts, and I doubt that just by putting your font on Google Fonts - which is useful, but it will not change everything. It's not like getting on the frontage of Hacker News, or something like that. Not at all.

**Adam Staravia:** Well, maybe not. The installation process is pretty straightforward though. So once you get the critical mass, and you get the awareness, the next step, which is usage - they've lowered the barrier to that at least, so I don't have to think too hard if I'm using Google Fonts for desktop or whatever, and it gets a little easier, saying "Just install."

**Jerold Santo:** Yeah, certainly. That's a cool open source success story. I know you're building on top of some open source... Of course, there's always copyright and legal things that happen here or there, and licensing, but it seems like everything's pretty much -- it shook out and been good. What about managing an open source community and project around a font? Is it different from managing open source around a codebase? I know you have some open source Clojure libraries, too... Does it feel like that, does it feel different? Is it actively developed? It sounds like you're working on the next version, so... I would tend to think a font - you design it, and it's done, but I guess if you're adding ligatures all the time, you could just do it till the end of time. Does it feel like a coding project, or does it feel like a different thing altogether?

**Nikita Protocol:** \[40:15\] Yeah, it certainly feels the same. There are a couple of differences. For one, it's really hard to take pull requests on the font, because the way a font is built - at least Facade - it's built in proprietary software, Glyphs App, which I think is kind of standard for font builders. There is Font Lab and there is Glyphs App; I think those are the two most popular programs. They're both very expensive, so you would not buy them just to change a letter in a font and submit a pull request... Because of that, I have to do most of the changes myself. So it's mostly issues, and people request and I just implement them myself. So that's different.

I would like to accept pull requests, but I think because you have to buy this program to design a font, and also because I'm not sure how well the font file itself will work with changes/patches, as you can do with source code. I think it's not well-optimized for patches. It's text format, but I think it's not well optimized.

I've initially used JSON; it might be slightly better... Yes, there are some questionable things inside. I've looked inside the Glyphs App format, and there are some questionable things... As a software engineer, yeah.

Other than that, it's also my most popular project, so I get much more requests for that than for anything else... But yeah, that's expected, I guess, because of the popularity. At some point I found out that the only way to keep up with it is just as you get some request, you have to deal with it immediately, otherwise it'll pile up, and you'll find yourself under a huge pile of requests that you have never taken time to answer... So now every day if I see a new issue I reply immediately. It might be "This sounds good" or "I will not implement that", or just two words, just to get feedback to people immediately.

**Adam Staravia:** What's your process though on issues then? Because you've got 686 closed, 238 open... Which seems like a lot. So what makes you open or close an issue? How do you handle issues?

**Nikita Protocol:** Sometimes you need to explain something to a person, sometimes you have to just redirect them, because many bugs are actually bugs in editors, or terminals, or in syntax highlighting... But people come to me with them and I have to explain how it works.

For feature requests, they just build up, and at some point - right now I do it every month - I just pick some that are certainly easy to implement, and I sit down for a day or two, implementing them, and then releasing a new version of Facade.

**Adam Staravia:** What makes you leave the issues open? Do you just leave them open because there's more conversation to happen? And what makes you click the Close button? When the issue is solved, or you've responded accurately, and you don't expect any more communication? What makes you keep this amount of issues open? Why is that number so large?

**Nikita Protocol:** Yeah--

**Adam Staravia:** Obviously, it's not your day job, so I'm not grilling you why you're not doing your job, I'm just trying to figure out - what is it that makes these issues stay open for you? What's your philosophy on keeping them open?

**Nikita Protocol:** \[43:59\] Yeah, if the issue is not resolved, like if I am certain I will never implement it, I close it because it won't implement. If I do implement it, I close it because it's done... But if I am uncertain, if there's pros and cons, I just leave it open. I don't see a problem with lots of open issues. Okay, maybe at some point I will have time and come back and take another look; maybe something changes.

I think in the last release I closed some issues from four years ago, or something like that... It's still possible. I don't mind open issues and I don't see a problem with them... I know with some repositories - especially in big companies, I think - old issues get closed automatically. Furthermore, I don't do that, because I don't see the point. It doesn't become less relevant because nobody took a look at it for a year. It's probably still an unsolved problem.

**Adam Staravia:** Gotcha.

**Jerold Santo:** Could you estimate the number of hours you've put into this project?

**Nikita Protocol:** No... \[laughter\]

**Adam Staravia:** Thousands, hundreds?

**Jerold Santo:** Orders of magnitude? Is it 100 hours, is it 1,000? Is it 10,000 hours?

**Nikita Protocol:** No, I would say a hundred. A hundred sounds like something realistic. It's a very thin layer on top of my day job, so it's like a day a month, or something like that... But it's been going for a while. I don't know how old it is - like five years? Or six years? It's pretty long now.

**Jerold Santo:** Do you ever just want to put up the "Not Maintained" sign on the README and just say "I'm done with this?" or are you still enjoying it? Do you get a lot of value out of it personally?

**Nikita Protocol:** Yeah, I still enjoy it. The issues just keep coming, so... Yeah, I don't want to close it. Actually, it's unusual for font projects... Usually, fonts get done, and not change afterwards. Most of the fonts never change after their release... So yeah, I guess it's unusual. But then, as a software project, it's not unusual; it's typical. Software projects usually are never done, so... Yeah.

**Jerold Santo:** And is that because you're adding ligatures?

**Nikita Protocol:** Yeah, mostly because I'm adding ligatures. There are requests from people, like "I think this might be a good idea." Most of the time it is -- or I don't know, half of the time it is, half of the time it's not... Sometimes they just come with the idea... In some languages there are certainly sequences of glyphs that are operators, but they just have no idea how to draw them, especially from Scala or R \[unintelligible 00:46:54.08\] How do you draw that so it makes sense? I don't know...

**Jerold Santo:** Right.

**Nikita Protocol:** There is no ligature for that. I would love to put it, I just don't know how to draw it.

**Adam Staravia:** If we estimate eight hours as a day of work, and you put in roughly a day per month, and you've been doing it for five years, that's around 500 yours.

**Nikita Protocol:** 500. Wow.

**Adam Staravia:** Yeah. If we base it on those numbers there. If that's accurate, then we've got about 500 hours into this project.

**Nikita Protocol:** Okay. Interesting.

**Adam Staravia:** Plus the mind space... Which is a lot; if you've got a day job, and other activities, and things that you're interested in, it's a lot to handle. And the reason why we did this show is not so much to say "Oh, let's quantify your effort", but more like, you know, there's a lot that goes into producing open source, that goes into maintaining open source, to lead a community, to do something like this with a labour of love... And it's less about quantifying that and more about being clear with how much effort it takes to be committed as you are and others are to open source.

**Jerold Santo:** \[48:06\] Have you had a lot of support? I notice you have a Patreon, I see you have some supporters, you're trying to get to a certain amount of money to help you work on these things... And I would say you've had some modest success there, but I'm curious how you would view that.

**Nikita Protocol:** Yeah, I think it's pretty successful. Patreon certainly helps a lot, especially the money for the license, for Glyphs App...

**Jerold Santo:** Is that an annual license, or a one-time purchase?

**Nikita Protocol:** I think it is one-time. I'm not sure. I just bought it actually because -- the first year when I started Facade, I asked the author of the Glyphs App if we can provide me with a license, and he did... Yeah, and I used it for a couple of years, the free license; that certainly had to be renewed each year. But then I set up a Patreon, and it didn't seem fair, so I just paid for the license from the Patreon money. I forgot the rest of the question...

**Jerold Santo:** I was asking about how you feel like the Patreon support is going, and if you're well-supported...

**Nikita Protocol:** I think for the amount of work that I am doing it's pretty generous.

**Jerold Santo:** Nice.

**Nikita Protocol:** I also have other open source which I would love to do more, like Clojure stuff. It's currently under the same Patreon. Maybe I should split it up at some point. Sometimes it annoys people that donate for Facade and get Clojure instead, or donate for Clojure and get Facade instead... I guess it's not entirely fair.

But yeah, I would certainly love to do more at this point. The full-time working on open source is a dream that I have, but it's not possible with the current amount of support. But it's certainly helping, yeah.

And I think that Facade is probably the most popular font with ligatures for programming. It also warms my heart every time I see Facade in the wild. For example, it's a conference and somebody puts up slides, and they use Facade, and somebody knows about it... It still feels strange, but it's a good feeling.

**Adam Staravia:** What's the skew when it comes to your support? I know you've got GitHub Sponsors going on, which is really on the Ton sky, not so much your repositories, which - that's how it's designed... Or it could be organizational-based. You've got Patreon, you've got PayPal... Of the three that are available, at least when you go to GitHub, and you're on Facade, which one is the most popular? Which one do you prefer? What's the percentages across the three?

**Nikita Protocol:** Patreon is certainly the biggest one. It might be because it was set up the first, and when I announced it, most of the people went there. The GitHub is probably ten times smaller, and PayPal is -- I don't know; it's 2-3 times smaller than GitHub. And also, PayPal a one-time thing, and GitHub and Patreon is every month.

**Adam Staravia:** \[51:12\] When it comes to this opportunity to sponsor you as an individual, what is it that makes you like or dislike certain feature sets from them? What do you like most about GitHub Sponsors? Obviously, PayPal is not being used very much... What's the skew between the two in terms of your preference, in terms of how they do things, and represent you as an individual creator etc?

**Nikita Protocol:** I would say that the idea of Patreon is the best, because you can have posts, you have extra material, and stuff like that. You can hide something for Patreon's only, stuff like that. All the features.

On GitHub Sponsors I don't think you can do that. You just give money and forget about it. You don't get \[unintelligible 00:51:57.22\] So in terms of Patreon, it's probably the best. I don't like the UI of Patreon; I think it's terrible. Everything is of the wrong size, and you can never find anything, stuff like that... It's hard to write a post, and stuff like that. But conceptually, the idea is better, certainly.

**Adam Staravia:** Yeah.

**Nikita Protocol:** I'm not sure how well it works for software projects, because maybe GitHub is better for software projects; or the same, at least... Because you see, Patreon is more for people who provide something tangible, that you can share. And a software project, especially in open source, is just a software project; what do you put on the Patreon page? Backstage videos of coding, or what? I don't know.

**Adam Staravia:** Yeah.

**Nikita Protocol:** It's just the code, and the code is already on GitHub. You get the code.

**Jerold Santo:** Right. So if you could one-for-one replace your current software engineer salary - exact same salary, but now you're full-time open source, would you make that deal?

**Nikita Protocol:** Yeah, absolutely.

**Jerold Santo:** And what would materially change about your life, having switched over to full-time open source? Have you thought through that?

**Nikita Protocol:** What do you mean materially?

**Jerold Santo:** Practically. Like your day-to-day, or your life... What would change about your life, having the same income but having this different career?

**Nikita Protocol:** I think that I will just become more calm, because I would work on things that I think are important... So it gives you bigger peace of mind, let's say. When you work for an employer, you're doing somebody else's ideas, and you have to also -- yeah, basically that. Also, I think I work better on things that I deeply believe in, and I'm more invested, and I work better... So yeah, it's just the way I feel that I work.

**Adam Staravia:** Well, it's out there on GitHub, you can check it out - Facade. It is amazing. I like it; I think it's got a great flair to it, especially if you really appreciate the ligatures. If you're someone who really wants that visual aspect to it, or if you're going to do a console UI, or you have some of these unique ideas... Nikita is certainly dedicated towards; he mentioned he's passionate about it, and if you want to support it, you can. All the avenues are there; the links are in the show notes, so check that out.

Nikita, thank you so much for your dedication to this interesting font for programmers to use, and for your commitment to open source. Thanks for coming on the show.

**Nikita Protocol:** Thank you for having me.

**Outro:** \[54:54\]

**Jerold Santo:** Boom goes the dynamite! You're off the Changelog Hot seat. I'm going to leave these ligatures on for a few days. I want to commit to a week of just leaving it as it is configured right now, and then I'll send you guys a tweet or a text or an email and let you know what I think after a week... Because maybe I'll just turn out loving it, and I'll become your next big advocate. Who knows. Or maybe I'll hate it and turn it off. I don't know.

**Nikita Protocol:** You certainly should give it a go... And also, another thing that I learned to experiment with fonts is the first impression is usually wrong. You have to give it at least a week; otherwise -- you cannot judge your first impression. And it happened for me with a couple of ones that I installed, looked at them, and said "No. This cannot possibly work", and then at some point I just tried them for a week and I had a completely different feeling. I could accept that I just didn't understand at the first glance... So yeah, certainly give it a go.

**Jerold Santo:** I think that's probably true. I think most of the time I do the initial hot take and move on, or move back... Like "Meh..." I'm happy with Ubuntu Mono and I just go back right away. It's kind of like "Do you want to go live in this new place?" It's like, "Well, if I stayed there for a week, I would have a much better idea, versus just walking through it." So I'm going to let it stick.

I think the ligatures is the biggest change. The fonts - there are differences, but they're mostly stylistic. Ligatures -- I was even typing the pipe and the carrot, and I'd delete the carrot and see what happens... The switch from \[unintelligible 00:57:40.26\] So that's a different thing that I'm not used to. But I'm definitely going to let it live, because maybe I'll end up being a ligature person after this, who knows.
