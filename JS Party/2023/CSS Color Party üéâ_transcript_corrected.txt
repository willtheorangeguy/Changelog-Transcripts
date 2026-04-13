**Nick Nisi:** Hoy-hoy! Welcome to JS Party. I'm your host this week, Nick Nisi, hello, and I am joined today by Amelia. Amelia, how's it going?

**Amelia Wattenberger:** It's good. I'm very excited about today's episode.

**Nick Nisi:** Yeah, it's going to be a very colourful episode, I think... Speaking of which, we have a special guest, and that is Adam Argyle. Adam, how's it going?

**Adam Argyle:** What's up?! Can I use colourful language? You all have a healthy beep button in there, right?

**Nick Nisi:** Sure. Yeah. I'm sure our --

**Adam Argyle:** I'll keep it cool. \[laughter\]

**Nick Nisi:** It's really exciting to have you back on... I think last time was probably -- was it one of the game shows?

**Adam Argyle:** It was a game show, yeah.

**Nick Nisi:** Yeah. A Feud episode, I think.

**Adam Argyle:** Those are fun and embarrassing. You watch it again, and you're just "Why? Why can't you just say the right answer, dork?" And you're "Well, because I'm at the moment, and it's hard."

**Nick Nisi:** Yeah. \[laughter\]

**Amelia Wattenberger:** Yeah, I still can't get over not being able to name a browser... \[laughs\] It's pretty bad.

**Adam Argyle:** Brains. They fart. What are you going to do...? I don't know... \[laughter\]

**Nick Nisi:** But we're not here to talk about that today. We're here to talk about colour. And there are a lot of wild things that we can do with colour nowadays, with just like pure CSS... I think. I mean, that's what you're going to tell us, right?

**Adam Argyle:** Yeah. Well, and JavaScript. So if you're a JS person that's just like "I love objects, and calling functions, and manipulating data", you're just like "Cool. Do you like colour? Because colour's totally like that." "Oh, colours?!" "No, dude, I'm serious. Like, colours, totally, are a really fun object to play with in JavaScript." Just as much as dates... I don't know if actually dates are fun. Money... There's like these rich -- yeah, this suck. \[laughter\] Colour's way more fun. And it gives you something to see. So as you do all these things, you can show it, and it's not just like dollars went up; you get to see like a colour change, and it's fun. Anyway, yeah.

**Amelia Wattenberger:** I'm sold.

**Nick Nisi:** Yeah. Same. Couldn't have said it better. \[laughter\] So why don't you catch us up on where we're at? Because when I think of colour, there are a couple of things; there is HEX, or RGB, or RGBA are pretty much the main ones that I use... There's also HSL, and SLA, which I've also used... Like, hue, saturation, and something... That's about the extent of my colour knowledge. So can you enlighten me a little more?

**Adam Argyle:** Yeah. And you're not alone. We look at the almanac data and there's like nobody even using HSL. It's just like HEX all day, maybe some RGBA... Which, by the way, RGBA is dead. SLA - dead. It's now just HSL or RGB, and you put a little slash at the end, and you can put your percentage there. You don't have to change the function you're calling any more just to add some alpha, because you all know that was so annoying anyway... Anyway, so --

**Nick Nisi:** Wait, I had no idea. I saw some syntax like that, with like a slash in there, and I'm just like "Why are they dividing in the middle of this?" \[laughter\]

**Adam Argyle:** It's like a classic CSS thing. There are slashes in border radius, there are slashes -- anyway, they're like to denote a break in sort of the parsing... Anyway. Yeah, Amelia, where are you at with colour? I want to know where your baseline is too, and we'll up from there.

**Amelia Wattenberger:** Oh, I'm still using colour names, like pink, sky blue... There's - tomato red is a good one, there's cornflower blue... These are my top hits. That's where I'm most comfortable.

**Adam Argyle:** Those are awesome. Alright, so few fun things about those... So the named colours are really fun to prototype with, and they have a fun attribute; many of them - like deep pink; I really like deep pink, because it's so hot. And if you look on your colour picker, when you put deep pink in there, and you pop it open, the little dot is in the far top right of the colour square, and you're like "Yeah, give me that brightest, most saturated colour..." And that is the brightest hot pink that can be found in SRGB, which is Standard Dynamic Range. So this is "Okay, we'll roll this into --" kind of what we're talking about today is all these colours on the web have been SDR, standard dynamic range, and what we're getting, and what we've gained is HDR colours; high dynamic range. So all these TVs you buy, your iPhones, your laptops - all these things all have millions and billions of colours. And you're like "Right on." But then everything's using them. Like the movies you're watching, the images you're looking at... Take a picture with an iPhone or an Android Pixel, and you look at the colours, and you're like "That sunset is poppin'!" Like, there are definitely some like High Dynamic Range colours coming off that image.

So when you're using these named colours, and HEX, and stuff, you're literally trapped to a tiny portion of what your screen is capable of doing. And so what CSS has done is graduated into the HDR space with a bunch of features that allow you as authors to take your website from an SDR website to an HDR website. And that is a product of excellence thing. This is why Apple was first; they've had Display P3; this is a wide gamut colour range since 2016 in all their products, and it makes sense. You look at an iPad in the App Store, you look at an iPad, in an app, and you're like "The colours on this are beautiful." And they know that; they know that a user can't really articulate why, but they will tell you one looks better than the other.

\[06:09\] So there's an opportunity now for your brand to do this, or your colours, or whatever it is that you're building, to kind of reach into this HDR space. And then there are all sorts of goodies for us to talk about, like colour manipulation, how do you specify colours; there's way more than HSL now, so I'm sorry, it kind of gets more confusing... It goes into gradients, it goes into animations... And we've got all of that stuff to talk about today. So how's that for a high-level little intro?

**Nick Nisi:** I have questions... \[laughter\]

**Amelia Wattenberger:** Yeah, me too.

**Adam Argyle:** Good. I'm here for you.

**Nick Nisi:** So first off, you mentioned all of those named colour values, like - I forgot... Deep pink? Is that the one that you were talking about?

**Adam Argyle:** Yeah.

**Nick Nisi:** Do those map to like the standard six-character RGB values?

**Adam Argyle:** Yep.

**Nick Nisi:** And is there a name for every combination of six-character HEX values?

**Adam Argyle:** Nope. They originally -- I don't remember the year, who cares, but they're basically the box of crayons. Because remember web safe, 256 colours? That's all you had to choose from?

**Nick Nisi:** Yeah.

**Adam Argyle:** A lot of those are from the crayon box. Because that's how creative they were when they were writing the spec. Who cares? Those are good colours. So a lot of those are crayon names. And those are RGB colours -- well, they're RGB colours, and they are inside that space. So yeah, they literally map to an RGB colour, they literally map to a HEX, to an HSL... All of these colour formats that we've been using today, even HWB - they're all in the RGB range. They're in SDR, standard dynamic range colour space colours. So we've had all these ways to reference colours, but they're all from the same pool. And now we have new pools to specify colours from.

**Nick Nisi:** So my 2002 knowledge on those colours was always like "Oh, you shouldn't use those, because deep pink could be this on a Mac, and this other value on a Windows machine..." Is that the case now still, or have they kind of standardized?

**Adam Argyle:** They standardized. So what's cool about RGB, and why RGB has been around for 25–30 years, is it is a common denominator. Basically, it's the most common junk that you can find everywhere. And everybody has united on "This is a healthy baseline." It's not junk, let's be honest; like, it's pretty good. This is why it's survived so long, and we're really only kind of getting nitpicky about bringing them into this HDR colour space. And we were waiting for displays. There wasn't a lot of displays that could even show these colours until five or seven years ago. So we're on this cusp where the capability is there, the math is there even for like downplaying some of these colours... So if I ask for some super-rad new HDR colour on a display that's 20 years old, the display is going to be like "I don't know what to do", but it'll show deep pink. Let's say I asked for "deepest pink", or whatever. Like, go into the crevices of the pool. The browser and the operating system and the display will all work together to go, "Well my colour profile and my capabilities say I can only go here. So I can only reach into this amount of RGB brightness in my little lights that I light up." And you're like "Cool, just give me the maximum pink, I don't really care."

But yeah, there's also media queries to help you handhold this. So let's say you don't want to let the browser and the operating system find something... You can be like "Okay, well, I'll give you a HEX value", and then if it's an HDR-capable display, which is the media query at media dynamic range high, then you can say inside there, "Then bump up those colours, baby. We're going to disco town!", or whatever it is you're trying to do. \[laughter\]

**Amelia Wattenberger:** Okay, here's my biggest question. As a web developer, I have a healthy dose of fear of new things... And I want to know what percent of displays people are using can go to disco town, right? Is this something only 10% of people are going to be able to use, or see?

**Adam Argyle:** \[10:07\] Yes, that's a great question; like, a metric on how common or uncommon are HD displays.

**Amelia Wattenberger:** Yeah.

**Adam Argyle:** This is going to be hard -- this probably depends on your circles... I mean, every iPhone, and every Mac is capable. So there's a percentage value for you already. Many Windows laptops are capable. You can go into the operating system of Windows and say "I want HDR Windows", and Windows will be like "Alright, I'm gonna start using HDR colours where I can", and all those little accent colours you get, they're going to be disco town. I like that we're calling them "disco town" colours. Let's hang on to that. \[laughter\] I was just watching Lego Masters, and someone did like a disco scene, and I guess that's why it's stuck in my head.

But yeah, you're right - a lot of Android phones, just a lot of other devices don't have it. But where you find it's really common is the TVs people buy. It's like they don't even sell SDR TVs anymore. You can only get QHD, super-duper -- and there's like super-high res ones. And then you have liked your Olds, which are different because they can turn off the lights to make black, which is another thing... So a lot of these HDR colours - one aspect of them is how black of a black can you make, and how white of a white can you make? This is like the nits that you'll read. If you go look at a brand-new Mac laptop, and they're going to be like "10000 nits!" And you're like "What do I need? I don't know how many nits do I need." And they're like "Well, you want the most nits, because it's a couple of hundred extra dollars." And you're like "I don't know..." So anyway, that's kind of like some of the factors that are in there. I think it's a lot more common now than we think, and I think that's why the timing is perfect now.

Another weird little niche detail here is that the web has been capable of HDR images and videos for many years, just not from CSS.

**Nick Nisi:** Interesting... So how do you enable it in CSS? It's got to be more than RGB or those HEX colours, right?

**Adam Argyle:** You have to use a new function to specify the colours. You have to ask for a colour from a new pool. And so that's kind of what these colour spaces are - they're new pools, new opportunities, more range, which also means things like gradients have less banding, because... Oh, here's another reason that CSS was kind of slow to this, is a lot of the browser engines were like "Hey, RGB has been really HEX, and it only takes a little bit of memory to hold the values for that. And these new ones - they require double and maybe triple the memory. So we're going to kind of wait on that, because we don't want to double every colour in the whole system." And there's like this fear about how impactful storing just the values of these colours in memory was going to be. And some genius just like a few years ago was like "How about we only double the -- if it's in the new range. Then, if the site doesn't use any HD colours, we don't change the memory." And everyone's like "Why have we never thought of that?" \[laughter\] And all of a sudden it became really viable to just-in-time upgrade colours to a bigger memory allocation if needed. So yeah, types, dude. Types. It was literally a type issue. Oh, also, by the way. Colours -- the types.

**Nick Nisi:** Did you say types?

**Adam Argyle:** I did say types, and dude, all colours in CSS are typed, dude. And they're typed well

**Nick Nisi:** Really...?

**Adam Argyle:** Very intricately typed... It's a typed system from the top to the bottom, and you call functions, you pass parameters - they're all typed. The ins are typed, the outs are typed... It is really cool. So anyway, if you like types, the new colour stuff is very interesting.

**Nick Nisi:** My mind is blown... \[laughter\]

**Amelia Wattenberger:** He's hooked.

**Nick Nisi:** Is it like types in CSS then, or...?

**Adam Argyle:** CSS has always been typed, bro. It's typed, and it's resilient. So it has this like thing where if you put the wrong value into somewhere, CSS doesn't crumble and go, "Oh, no, there's one little wrong thing in my entire application. I can't even do anything", which is what TypeScript does... \[laughter\] Sorry. That's what all typed languages do, really... It's a good reason, I know, but it doesn't have to stop the show. CSS doesn't stop the show. CSS goes "Oh, that's wrong. Yeah, whatever." And just keeps going.

\[14:10\] So you can pass -- for example, you could pass pixels to something that needed a colour type. And it would be like "Alright, well, nice try", and it would just roll on. So that's how they have type validation, is it knows if a length or if a type, and what all -- anyway. So it's all typed; it always has been. It's just sort of lesser known because it's not strict about it.

**Nick Nisi:** Oh. So I don't know how things work in your neck of the woods, but if you put something into CSS, and it's wrong, but it doesn't care, and it just stays there, that is now part of the legacy of the app that I'm working on. Like, nobody goes back and cleans that up.

**Adam Argyle:** Cruft.

**Nick Nisi:** Yes.

**Adam Argyle:** Seriously... I just learned about how many to-dos are in the Google codebase...

**Nick Nisi:** Oh, no.

**Amelia Wattenberger:** Oh, no... \[laughter\]

**Adam Argyle:** It's insane. I was like "Oh, surely it's just a couple of --" No, dude. It's so many to-dos. And you're just like "But those are just left hanging..." Yeah. That's software. We can't get to every edge case in everything, all the time. It's gnarly. Anyway, that's a rant...

**Amelia Wattenberger:** I think to-dos are just -- they're just performance art, right? You leave in there, you're like "I know... I know I'm supposed to do this. I just want you to know that I know." \[laughs\] "I'm not gonna."

**Adam Argyle:** Funny. So yeah, there's a little mind-blown colour stuff. Yeah, where do you want to go next?

**Nick Nisi:** Well, so you mentioned that it's a new function. What does that actually look like to access these new colours?

**Adam Argyle:** Awesome question. Okay, so let's start with the most supported one, or the one that historically has support - it's the colour function. So literally you call colour, you've got two parentheses, and the first parameter is the colour space. And the one that Apple has supported for about six or seven years is the Display P3 colour space. So you say colour, open parenthesis, display dash p3 space, and then you pass three channel amounts. And so it's basically asking for brightness from 0% to 100%, saying "How much power should the display put behind those RGB lights that it's going to light up for this colour?" And you can say 100%, zero, and 100%, or you could say 1, 0, 1... So CSS is very good about understanding a range between zero and one, and zero and 100%. So it's on you as an author to kind of pick how you like to work inside there. And it's as simple as that.

So you say like "background is colour, open parenthesis, Display P3, 101", end parentheses, and you've got yourself super-hot pink, because you maximized the R and the B, and you left the G. I can't believe I did that in my head. Wow, okay. That was pretty good.

**Nick Nisi:** Yeah. \[laughter\] That was going to be my next question - the percentages, was that R, G and B that you're --

**Adam Argyle:** It was R, G and B. So that's another thing. That's why the RGBA function -- yeah, let's just retract a little bit... RGBA was dropped not just because of convenience; because it was really, truly annoying. You're like "I need to add alpha." You're like "Dang, I have to call a different function. It's really annoying." So what they did is they also normalized that all these functions take three channels. HEX is kind of the odd one out here, in that it represents the three channels in like a (well) hexadecimal. And now it's just very blunt. It's like "Here are three channels." And so moving forward, every one of these colour spaces is three channels. And then you have your alpha with the slash, and so it's kind of nice.

If you're used to HSL, there's a new one called LCH, which is kind of almost like the same letters in a new arrangement. It's kind of annoying. And then there's even one called OK LCH, which is superior to LCH, even though it makes it sound marginally better, or marginally \[unintelligible 00:17:43.17\] \[laughter\] Anyway. It's just -- it's like the person that came up with OK LCH was just really humble about it. They could have been like RAD LCH, or like "Doneness LCH", but they were like "Yeah, it's okay." And you're like "Well, you really sold that short, because it's perfect." And the OK LCH colour function - so instead of calling the colour function, like we did earlier, you can just reference the colour space exactly, in a function. You say, OK LCH, just like you did with HSL, open up a parenthesis, pass three channels, and L is your lightness. It gets more technical than that, but you've got an L that's perceptual lightness. This is lightness per your eyes as a human, whereas HSL was lightness in math, which - they're just not the same.

So then you have C and H. C is Chroma, and H is Hue. So your hues are pretty similar, your Chroma is about like how much vibrancy... It's kind of like saturation, but it's a little bit different... So anyway, each of these colour spaces are unique, in that they bring something different to the table. They're like a utility function that you can call to get access to colours in a way that is optimized for one thing over another. So you kind of learn these. But OK LCH is a perfect first place to start, because it both can go into super-wide gamut, HDR colours, but it also has a really, really reliable lightness channel that makes it great for design systems, it makes it great for lightness adjustments, and then colour functions. Like, if you want to manipulate a colour, like darken or lighten something, it has reliable results. So yeah, there's like a little -- so there's how you access the colours; you call these new functions... You either call the colour function and pass a colour space, or you call the colour space itself directly, like OK LCH, or LAB, or LCH.

**Break**: \[19:31\]

**Amelia Wattenberger:** Okay, here's the question I've been wondering since you said the word gradient...

**Adam Argyle:** Yes.

**Amelia Wattenberger:** And I've never thought about this before, but if you defined, say, the start and end colour for a gradient, in a different colour space, will it interpolate differently? Or is it only for the way you're defining those colours?

**Adam Argyle:** This is such a good question. It does interpolate differently.

**Amelia Wattenberger:** Wow...

**Adam Argyle:** This is where we can even pull up a quick little visual. Like, I know you've seen the RGB cube, right? All the colours packed so nicely into a cube. And then imagine you put two little points in there, in a three-dimensional space, and that's your gradient points. And then the cube and your function have to go from one to the next. And it literally goes in a straight line, because that's what math does, right? It goes straight from one colour to the next, which means it's going to go through the middle of the cube, or it's going to go through different parts of the cube that gather the way that the gradient looks at the end. HSL is a cylinder. So again, as you make a gradient in it, you get a different result, because the path that it took, like literally like a journey. You could be like "This is fun. Let's make a metaphor out of this." This is a video game; you've got like a journey, different mountains that you have to cross, and like your little journey person starts here at colour one, and then you have colour two, and depending on the mountain, they take a different path to get there. And as they go, they collect little colours. And then in the end, you get a whole range of the colours that they went through.

**Amelia Wattenberger:** Man, I'd play that.

**Adam Argyle:** Yeah, that kind of sounds cool. Yeah, I agree. And that's colour interpolation. And you can also do this with animation. If you animate from blue to white, it's the same concept. Instead of you seeing one smear of the colour from blue to white, like a gradient does, you see it changed step by step over time. So you only see one state of the colour interpolation over time. And so yeah, each colour space has different results. That's why new gradients use the OKLA colour space by default, because it is optimized for vibrancy, and avoiding the dead zone, which is what RGB has, notoriously. When you go through that middle space, the middle is white, and so you pick up lighter colours on your way; sometimes they look gray, or muddy, and these new colour spaces create gradients that are much more vibrant and don't have the muddy zone, because they're packed different, so that when the little journeyman travels across the mountain, he stays in the bright areas.

**Amelia Wattenberger:** I like that metaphor, or analogy. So you can define a gradient with two different colour spaces. I've never tried it.

**Adam Argyle:** That is correct, you can. Well, it will interpolate in one colour space, but you can put colours from -- this is a great, mind-blowing question... So you've got like colour number one is HEX-something, right? You're like SDR colour. And then the other colour is OK LCH, something turbo-rad-cyan. The browser - there's math in the CSS specs on how to resolve that. And so they're going to get put into a colour space that is big enough that they both can share a position in it, and then they're going to get converted into the colour space that the interpolation happens, and then the interpolation happens. So there's a conversion and then interpolation.

So this is - again, colour gets really, really complex, really fast. I'm going to hope to make this sound as simple as possible throughout this podcast episode, but this is again why it's kind of like working with dates, or working with money. There's a lot that can happen in the math between conversion and interpolation, and perform-- yeah, it's all math. And the end result, you see a colour though.

**Amelia Wattenberger:** I love that. Also -- so you mentioned JavaScript, right? Where does JavaScript come into play here? Or are we only working in CSS here?

**Adam Argyle:** \[23:59\] Yeah, it's good question. CSS has easy access to all these functions. But from JavaScript, you can set colours, you can extract colours... Eventually, there's going to be an object model for it, so that you'll get a rich object back that has the channels already broken out for you into RGB, or LCH, and stuff like that... At which point you'll be able to restructure a colour, "Oh, okay, I will have to move into RCS next", the relative colour syntax, because you literally restructure a colour in CSS, put it back together in one line of code, and then return it to the browser... It's super-rad.

But in JavaScript you could do that now. You could grab a colour off of an element, you could split it by space, and find your channels, reassemble it, put it all back together after some math, and put it back in. There are also a lot of colour libraries to work with. There's many of them. The folks that wrote the specs, Lea Very and Chris Lille have one called Color.js. I use it all the time. And that's very spec-compliant for CSS, and you get this really rich experience working with colour from JavaScript. It's super-fun. And you can make gradients, and various colour spaces... I have all sorts of cool demos I'll share at some point. Oh, here, I think I have CodePen collection of colour stuff. I'll send this to you. And it's a mix of CSS and JavaScript HD colour and colour functions. Here, I'll put this in the JS Party chat.

**Nick Nisi:** We will include that in the show notes as well...

**Adam Argyle:** And yeah, a lot of this stuff is -- there are tons of utility in each colour space; there's utility in knowing the JavaScript ways, and the CSS... Just like normal web development, right? You have like this harmony, and a relationship, and an orchestration that you're going to find the best tool for the job. And these new colour spaces give you better tools for the job. So that's kind of what's nice, is after this podcast you're going to be like "I have new colour tools that help me perform my work better. I like literally learned new functions that give me better results than what I've been working with in the past."

**Amelia Wattenberger:** Yeah, that's awesome. And I love that the fallback is pretty simple, right? I get really nervous with new tech on the web, because I don't know what's going to happen when a browser doesn't have access to it, or doesn't support it.

**Adam Argyle:** Yeah. And that is a good concern. There are a few ways to handle upgrading. So you could progressively enhance; so you've already got an app, it's already got colours, you've got bright blue, bright yellow somewhere in the app... And then you could easily say, @media dynamic range is high; target those custom properties, or whatever, and use OK LCH and bump them up. And now all your yellows and blues are bumped up, safely...

There's actually an additional query that you can put in there... Because there's a difference between the display having the capability, and the browser being able to parse. So you can also put in an ad supports parsing function in there that says, "Hey, do you even understand Display P3? Do you even understand, OK LCH? I don't want to give you this colour unless you can." So you can be really handhold with it, with like two media queries, or you can just do the cascade; you just drop one in the cascade and just be like "Hey, here's the colour one. It's hot pink. And then next one is hot pink in OK LCH." And if the browser doesn't know what OK LCH is, it goes "Cool, I don't know what it is. I'll throw it away. I'll just take the colour I got before then."

And there's even another way that you can do this, an even lazier way, which are you just use the new colour functions, and if the browser doesn't understand it - well, you wouldn't get a colour. So that'd be the bummer. But if it does understand it, it will automatically adjust it for the display and the capabilities of the device. So you can be like "I'm just going to use these new colours, and I'll let the browser and the display and the operating system work out how rich it can make this pink, how rich it can make that blue." And so you have all of these options. You have graceful degradation, you have progressive enhancement, you have lazy, "I'm just going to let it be broken on other stuff, if I want..." Yeah, it's all there for you.

**Nick Nisi:** Speaking of broken on other stuff... I was looking up OK LCH in MDN, and it looks like Firefox is the only one that doesn't support it right now.

**Adam Argyle:** Yeah. And that recently merged. They'll have it -- so it's in Nightly, and it'll be in Firefox stable, I think 114, or something like that. I don't remember the exact version, but it's soon.

**Nick Nisi:** \[28:09\] Cool. Nice. So I'm confused... I guess the part that's confusing me a little bit is - you know if you were going to create a news site, and you're creating a design for it... Are you primarily playing within the standard range colours? Or would you have your primary and secondary colours being in this higher dynamic range, with fallbacks into that? When do you use what, and can you rely on -- I'm confused about... You know, if Adam is starting a site, are you primarily still using RGB in a lot of places, or are you dipping into this OK LCH and these new colour functions?

**Adam Argyle:** Super-good question. And I'll answer it in kind of two parts. I just redid my website, nerdy.dev. Have fun, check it out. It does use HDR colours, but it upgrades to them. And so I'm using the approach that I mentioned earlier, with a media query checking to see if the display is capable, and checking to see if it understands the parsing. That way I safely upgrade any vibrant colours.

The syntax highlighting is using HDR colours... Anywhere where you see a nice, bright colour, especially in the dark mode - the dark mode got a lot more treatment for the neons that you can get out of these HDR colours. The other side of this though is - that's Adam doing his own design. Ah, the third person is always so weird. That's me, wearing both hats - a designer hat and a developer hat. And I know what I'm doing. Now, designers though, like on teams that I've always been in, they live in ideal land, right? They always make ideal comps, with ideal layouts, with ideal users... Wow, this user really takes great pictures. Look at that. Look at that profile page. It's amazing." And then you go to the actual app, and you're like "No!! That user's pictures suck." Anyway, so designers are supposed to live in this ideal space, at least in the beginning of the app; who cares. But anyway, they should be using HD colours in my opinion there. The bummer is a lot of the design tools haven't really caught up. It takes, I'd say, 10% or 15% of the designers that I know even know this stuff exists, and their work is better because of it. But it's just not popular, or -- I don't know, we're still catching up. I think people still don't even realize why they bought a UHD TV. They don't even know what they bought. They're like "I bought a new TV." You're like "How many colours does it have?" And they're like "I don't know. A lot." You're like "That's fine." I don't expect everyone to know that. I didn't even really know it before. But I think as designers want product excellence, and they live in the ideal state, they should be using the ideal colours, which again, they manipulate better. Like, you want to make a light variant - it lightens better in OK LCH. It just does. HSL can do funky stuff. And so they'll eventually be working in these, you'll be inheriting them, and the relationship will change, at which point you'll be producing fallbacks at some point; or no fallbacks at all, as we move forward into 2024, and just like everything's HDR, or whatever. But yeah, I feel like I went on to tangents, and I hope I answered your question.

**Nick Nisi:** Yeah, I think so. So in 2024, and beyond, when all of this is fully supported in every browser, and works great, is there a use case for the older colour syntaxes?

**Adam Argyle:** Hmm. I mean, I have friends that work on LCD panels, or like kiosks, or all sorts of interesting niche industry software on weird screens... Now, they's still going to be in SDR land, because RGB is just so ubiquitous in that way. But I think as we look for product excellence, and we want to use the features that someone's got in their hand, like a device that's like HDR-capable, you're going to want to give them that colour quality, it will look and feel different. So yeah, I think just our expectations as users might change a little bit as we get there.

**Amelia Wattenberger:** Well, I have the opposite question to what you've just asked, Nick. So what's like the best case scenario? We use these and colours pop more, gradients interpolate better... What are we getting from this? And also, does it matter evenly across colours? Like, is a pink way deeper than RGB pink, but yellow is kind of the same?

**Adam Argyle:** \[32:20\] Nice. Cool. Okay, two parts. The second part is easier to answer, is that yeah, some of these new colour spaces offer way more blues than they do yellows. For example, yellow is tough. Every colour space has like a tiny amount of yellow to choose from. Whereas blues and greens, and pinks and reds, they just go crazy. Which is also because that's how our eyes are; our eyes are like super-attuned to some of these colours more than others. Any way, it's also the shape of the space, but yes, some hues do offer more than other hues.

The first part of the question though is what is like the main benefit here - it's vibrancy, it's design system consistency... So I have some demos I can share with you where I've defined 15 custom properties in OK LCH, and you can just change the hue, and you get a perfect palette, in any hue that you want. So you don't have to download the Tailwind blue, or you don't have to download you know my library Open Props pink, and you don't have to grab pink and green, or whatever... You don't have to go pick, you just grab 15 props and change the hue. You can also adjust the chroma; so if you want a more vibrant colour palette, you bump up the chroma. If you want it more pas telly, you drop the chroma.

So with 15 props, you literally have hundreds and thousands of colour palettes to choose from, versus the way that we're working today with RGB, where we sort of prefix these 9, or 12, or 15 colours, and then we try to work within that set. We can do the same thing with 15 props, and make it adaptive and dynamic for light, and dark, and all that sort of stuff.

So yeah, you get design systems, vibrancy, manipulation consistency... Oh, and the gradients are better; the gradients do genuinely look better. I don't know if you've seen the tools that -- like, Eric Kennedy has a tool where you go and make a gradient on his tool, and the output... You put two colour stops in, and the output is eight stops. And the reason that he does that is he literally has written an algorithm to avoid the dead zone by hand-holding the gradient, adding additional stops, so that it never goes through the centre. It's like giving the journeyman more positions on the mountain, to avoid the spots that are dangerous. Hey, that actually worked out pretty good... \[laughter\]

**Amelia Wattenberger:** That's sweet.

**Adam Argyle:** So yeah, so you have some of these things. It's going to be smoothness, vibrancy, excellence, consistency, and reliability of manipulation. But it is more confusing, in a way; like, I totally empathize with how heavy this stuff can sound, and that's why I'm -- like, keep asking the basic questions over and over, because everyone who's listening is going to have the same questions, you all. And don't feel bad; this crap is somehow confusing. You're like "Colour is supposed to be simple." And all of a sudden, it's not. And you're like "Well, coding is like that all the time..." But yeah.

**Nick Nisi:** Good. I'm glad you're giving me permission, because I'm going to keep going... \[laughs\] I'm trying to understand... And I'm already terrible at this stuff, but I'm terrible with RGB. And there's just so much more. But a question I had was - so this OK LCH thing, going back to that a little bit... You said that it's defined -- it now works in every browser; Firefox, all of that. And I create a site and use that completely. But then here I am, on a nice, modern Mac, but I'm using a ancient, really cheap display with it, that doesn't support all of that.

**Adam Argyle:** Yeah.

**Nick Nisi:** If I define like some neon blue that's very vibrant, will that get translated into a more muted blue by my display, and still show up as some kind of blue, or what happens there?

**Adam Argyle:** \[35:54\] Yes. So yeah, the display I'm looking at right now, that you all are on, is a poppy SDR display; it's cheap, and whatever. The one I have over here - this is my Mac one. It's very nice. I can literally take a tab from Chrome or Safari and drag it over and watch them go "Book!" and get like downgraded. But here's the thing - just like we were talking about deep pink, or the named system colours, and those are reaching into the furthest corner that's capable in that SDR RGB colour space - that's all the displaying the operating system is going to do. When you ask for a super-rad disco pink, when you bring it onto a monitor that can't do it, the operating system and the browser, they all orchestrate and go "Hey, look, this display can't do that. You've got to downplay it." And it'll automatically downplay it into the best pink that's possible.

So that's kind of what's nice, is you're reaching really far, and most of the displays won't be able to do even some of the stuff OK LCH can do, but it will do the best it can. And that's kind of one of the fun parts here, is you're asking everybody's device to do the best pink that it can, the best vibrant thing that it's possible, and you just let it adapt to all these scenarios... Just like width of text; just like a lot of our responsive design, and our adaptive design is doing, where we don't nitpick and pixel-perfect everything... The same thing's going to happen with colour, where someone over here is going to have a regular display, someone over here is going to have a super one, and both their displays are doing the best they can with OK LCH.

There's a cool site you can go to, oklch.com. It's made by Evil Martians, the PostCSS folks... Well, they work on PostCSS, and they do lots of other stuff... But it's a very good site. It's also going to immediately be annoying and confusing if you don't do much colour stuff, because you're going to be like "Oh, look, charts that I don't know what they mean." \[laughs\] But at the same time, it gives you a perfect gauge. There's going to be two switches there; one's for P3 and one's for Rec 2020. You should turn on Rec 2020, just to see the additional lines that you get. There's going to be cut-offs. And the cut-offs are going to tell you how dynamic is this colour. And you can choose - you know, reach really far into Rec 2020, and then it'll even show you the fallbacks. So it has that little -- like, in the top left there it'll say "Here's the colour you're building. Here's what that looks like in RGB", and you get like a comparison. And that tool is really nice for seeing how the colour space OK LCH has some quirks; you'll see these curves, and these cuts... And then if you're looking for super-bright, vibrant, you can use their controls to find that peak colour that's in there, and then put it in your code. And it helps you create OK LCH values as like an OK LCH colour picker.

**Nick Nisi:** What is Rec 2020?

**Adam Argyle:** Rec 2020 - yeah, so let's talk about sizes of sports balls. You've got like a baseball, which is your current HEX and SRGB colour size. All the colours that it can do fit inside a baseball. Then you have Display P3. Let's imagine it's like a softball, maybe. Yeah, it's a softball, sure. You get like 40% more colours or something like that, with Display P3. So you literally have a -- you have these two in your hand, and there's literally more colours in the bigger-sized sports ball.

And then you have like a basketball, which is Rec 2020. So Rec 2020 is a recommended -- it's a recommendation, and it was recommended in 2020 for supper... Like, what's the movie theatres we go to that are like crazy-rad? IMAX! Yes, so you've got like IMAX colours. These are the folks that are like real okay. And then - okay, here's another one. Who's the director that did Avatar, and stuff? Yeah, whatever. Okay, anyway. This person's using a camera that's like recording really rad colours. It's a super-rad that's maximum that 2020 could do, right? That's Rec 2020. It's a standard space where all these things that are capturing an intake in colour can put them into a space that everybody agrees on, and then they know what size that is... Which, by the way, RGB, P3 and Rec 2020 are gamuts. And that's why I referenced the size of a ball; like a volume, because you have different volumes of colours.

\[39:55\] But remember, in the gamut of RGB, like the baseball, you have HSL, HEX, HWB, and all these different ways to access colours from the same pool, but in a different shape. This is where things -- this I'm sorry, this stuff gets Tripp... But you have pools of colours, like total number of colours, and that's your gamut, and then the colours space is a shape; and you think about like the RGB cube. The RGB cube is showing you both its shape, and its gamut in one view. But you can separate them; you abstract them into two different types, two different data representations, one just being a totality, and the other one being a shape meant for a purpose.

The HSL cylinder is very handy, because we think about colour in a wheel, you've got that circle, you can just easily change the hue... And as you go down the cylinder, you get darker, and as you go up the cylinder, you get lighter. So it made sense for people to interact with HSL in a very reasonable, humanistic way. They think about a hue, they change the brightness, and then they change the lightness.

And so these new colour spaces like OK LCH operate in the same sort of accessing language, where you still say "I want a hue, and I want some brightness, and I want some lightness to change", but the shape of it is drastically different. So these colour spaces - each shape has a superpower. That's why there's no one true shape right now. There's no one true colour space. And OK LCH just came out like a couple of years ago. It's crazy, literally. So inventions will happen. We are not done with colour. Colour is -- our displays haven't reached what our human eyes can do yet. The code that we write doesn't have access to all this stuff yet; we haven't found the perfect shape that represents the possibility of the gamut, with the handiness of using it... Like, there are problems with OK LCH, even though it's the best one we have; there are issues in it, and people that study it know it. They're trying to solve it. Just like schools of study, trying to fix and create the next best colour space.

It's very computer science, very heavy into math, and three dimensions, and plotting... It's crazy. Furthermore, it's like a totally deep world, that spans media, it spans the movie industry, it spans the photography industry, and now it's in CSS, where we're getting the capabilities that they've had for a number of years.

**Amelia Wattenberger:** That's a whole new world out there. Do you have any tangible explanations for what's changed for monitors? Like the hardware aspect - how are we bumping up the colours that we can represent within our monitors?

**Adam Argyle:** Yeah, that's a good question. One of the best examples is what I was talking about earlier - I think it's UHD, or... No, it's OLED. OLED is more expensive, because - you know how we have black mirror; when your TV is off, it's literally black, and it's like reflectively black. But if you turn it on, and it's broken, it's dark gray. That's not OLED. That's your RGB lights at the lowest setting that they have. But that's not a rich black colour, which means if you're watching Game of Thrones, which - I watch Game of Thrones on my crappy TVs all the time, and I get tons of bad colour. Because they're so dark in a scene, and my screen can't do it, that I see these like bands of gray. When I know the reality is if I was on an OLED display, with a really, really rich amount of dark range in it, I would see richness there, and there would be millions maybe more colours just in the dark area, let alone the light area, where the whites are better because of the nits. Nits come down to the power of the lights. How powerful can these things combine to create a white? There's literally whiter whites. And I know we talk about like painting your home, you're like "Oh, there are 10 whites to choose from when painting a wall." You're like "There are 10 whites?! Come on!" And then you see them all together, and you're like "Oh crap, I see the difference. That's annoying." Same thing happens with the display, and nits; you get more whites, the whites are whiter, and it makes a difference having that darker dark, and the lighter, as well as a bigger gamut of colours. Now you're watching Discovery planet and really getting immersed, right? You're like "Well, the waves are crashing", and it's good stuff. So there's like some background on like the displays and the capabilities that are changing, that are enabling these things to be in our homes and our pockets.

**Nick Nisi:** \[44:13\] So that makes sense for like the blacks and the whites, right? The blacks get -- they can turn the pixels off, effectively, or eliminate or reduce the glare from other pixels close by, maybe... And then the nits for whiteness. But for when it's actually like showing colour, is it still just RGB LEDs that it's putting together?

**Adam Argyle:** Yeah.

**Nick Nisi:** And is there more of them to allow it to --

**Adam Argyle:** That I don't know. I'm assuming more powerful, and then the colour space -- just the math that's built into the hardware is able to do this sub-pixel... It's not sub-pixel, but like floats. You know float values, and -- those might not have been able to be done with older TVs, that didn't have the compute power. And now we have the compute power, so they're doing the float numbers, and so they're getting micro-adjusted in the water, which is why you get possibly a million more blues in between two other blues. It gets really heavy, yeah.

**Amelia Wattenberger:** So the extra colours, are they evenly dispersed throughout the luminance? Do we get brighter colours, or do we get more colours evenly throughout the spectrum?

**Adam Argyle:** Excellent question. So if you think about the gamuts, the gamuts are the totality of colours possible. So if you're in the P3 colour space, there's a certain number of colours that it says "I can do this." So if you're P3 gamut-compliant, that means you can represent everything inside there. And that is -- it's just like flattened out, kind of, and you get this view that doesn't feel very dispersed. It looks very evenly distributed. But when you get into the colour spaces, where you change the shape of something, the shape change can heavily impact how many you have there.

But - okay, so let's talk about OK LCH. If you're in the red hue, and you go from lightness 100 to lightness 0, this is a superpower of LCH and OK LCH. It's called CHENAB colour spaces; they're perceptually uniform for human vision. They were tested in the '70s, and they got tons of participants to say what was lighter, what was darker, and they arranged the colour space based on how we see, so that it doesn't matter what hue you're in, you do get an even distribution from zero to 100%. This is why it's a powerful space for a design system, is if you want to lighten or darken a colour, you're literally lightening or darkening it based on the way that our eyes perceive colour; the noticeable difference that the human eye can see, not the change in a number, in a mathematical colour space shape, but literally something that 1% will change something visually, 1% to humans. And so that's something special for that colour space. Other colour spaces might not be that way.

I did want to mention one more thing, too... Sometimes it can sound like - when I'm talking about this stuff, like RGB, is somehow not capable, or RGB, like the lights, or just like the colour concept of three channels that way is not good... It's very good. There's colour spaces that use RGB, that are very HDR. There's an Adobe Profit is a very wide gamut RGB-based colour space. And even Rec 2020 has an RGB mode where you can access colours using R, G and B. Because so many of our displays display colour that way; so we can specify how much power to put on each of those lights. But yeah... I don't know, this stuff gets gear.

To bring it back to CSS a little bit, though... Want to chat about like some colour functions? So we'll go beyond colour spaces and gamuts, and kind of chat about like usage, and stuff that you might do inside your application that's handy, and how Sass helped, and how Sass has adapted to the changes in CSS as well?

**Amelia Wattenberger:** Yes, yes. I wanted to ask about this.

**Adam Argyle:** Unless there are more questions, but yeah...

**Amelia Wattenberger:** No, let's do that.

**Adam Argyle:** \[47:58\] Cool. Okay, so in Sass you've had darkened and lighten for a long time. Those were always done in the colour spaces they knew best, which was RGB. They've changed it now. Actually, they didn't change it, but they did -- do you remember when they stopped saying "Use lighten and darken" and they said "Use colour adjust"?

**Amelia Wattenberger:** Didn't get that memo... \[laughs\]

**Adam Argyle:** Yeah, a lot of people didn't get the memo. They gave that memo because people were really realizing that darken and lighten would sometimes give them weird results. And so colour adjust was used to do the same work, with a very similar syntax, but in a better colour space, so that the results weren't so weird.

So now we have CSS, which can -- it can lighten and darken colours. And so there are two different ways to do it. One has great support, and one is on its way. The great support method is the colour mix function. You call the colour mix function, you pass two colours, you can say which colour space to mix them in, and you'll get an output result of them. You can mix a colour with transparency, so to make a colour more or less transparent, you can mix a colour with white, to lighten it, if you want to lighten it in a sort of like mixing fashion... And you can darken things by mixing it with black, or another darker version of the hue. And that's colour mix. It's kind of -- I don't know, a little basic in its way, because it only...

But there's also one called relative colour syntax, which allows you to -- so let's say you have a brand colour that's like #f10 or whatever, right? This is - again, a designer gives you a HEX colour, and you need to do manipulations on it. You can now say "colour" -- we're going to use the colour function, like we were talking about earlier with Display P3... colour, open parenthesis from your HEX colour. And when you say "colour from" -- well, you can even say "OK LCH from", you're going to get back a restructured version of that colour in the colour space that you asked for it. So you could say "HSL from HEX", and you'd get H, S and L back. You could say "OK LCH from HEX", and you would get L, C, H back. And when you get those values, you can use the call function to increase or decrease them, or divide them, or multiply them. So you could double the amount of saturation, you could divide the saturation, you could divide the lightness. You can also just squash it. So you could be like "Hey, I got LCH back. I don't care about L. I want a really dark version of this colour." And so you just set L to 5%, or something like that; now you have a really dark version of that HEX colour.

And so you're getting these new functions that allow you to very, very dynamically build out variants, and derivative colours, and like derive colours from other ones, and build entire systems and entire palettes that are very robust, and consistent. Again, if you're working inside that LCH, or OK LCH space, you're going to get that consistent lightness. So if a user chooses they want the theme to be green, they get a nice, visually-consistent green theme. If they change it to red, they're going to get something that's perceptually the same lightness across the board, just a different hue. And it turns out HSL does not have that power. It has a lot of oddities in terms of lightness.

So yeah, relative colour syntax - often called RCS - and the colour mix function are here to save the day for mixing colours, making variants, and just doing overall colour manipulation inside of CSS.

**Amelia Wattenberger:** What the heck, CSS added all these cool features and I didn't even notice? This is amazing... \[laughs\]

**Nick Nisi:** Yeah. The sad thing too is I'm googling this stuff as you're like saying it, and I'm seeing all these blog posts from 2021, and I'm like "Wow..." I just had no idea.

**Amelia Wattenberger:** "Where have I been...?"

**Adam Argyle:** Don't worry. If anything, everyone is probably in the same seat, sitting in their car, listening to this episode, going "I'll just still use HEX." Well, I have news for you all. This is the best time to ramp up. Skip HSL, skip HWB. Go straight for OK LCH. If you want my recommendation right now, go straight to OK LCH and start playing with it in the browser. Go see the colours that you can get from it; maximize the chroma, change the lightness, and look to see how these things change. And go build a little colour system with it.

I also have convenience things. Open Props has a couple of packs that are OK LCH packs, ready for you to go, where you just import this one line; it's like Open Props from like unpackaged, and you get 15 OK LCH prompts from me that you can then go change the hue and the chroma of, and get entirely new palettes in any hue and any colour that you want. You can start playing with those right away. I'll put those in the show notes, too. It's cool stuff. It's a cool time to start switching -- I think by 2024 we're going to see it well-supported in browsers, and it won't be an issue, and we'll be off to the races with wide gamut colours in our apps.

**Break**: \[52:35\]

**Nick Nisi:** So that's a great segue into the question I wanted to ask, which is like what's the support like for this within design tools? Because when I think of doing this, I usually get like a Figma design from our UX folks, and I have to translate that into the web somehow. And I'm looking at the exact colours they give me, and Figma is usually giving me -- right now it's RGB or HEX colours. So can these be defined in tools like that, or should I go back to them and be like "I'm going to translate this to OK LCH" and watch their faces melt like mine? What's the support like for that?

**Amelia Wattenberger:** Yes, great question. So Photoshop has had lab in it, which is CHENAB colours, kind of like LCH... It's been in there for years. People just don't use it. They're just very accustomed to poking inside the pool of RGB. A lot of designers also pick colours from their -- I'm going to say from their heart. It's like a subjective thing; they're not there doing mathematical computations like we do in code. In code, we're like "I want to know, is it is 5%?" And they're like "It's 5.25% darker" and you're like "I'm going around it. I'm going to round that, because it don't matter. And it makes my code look cleaner if I don't have the sub--"

Anyway, okay, so that was off the topic. Figma does not have support for these, you're right. It's stuck in RGB. It's SDR only. They target multi platforms. They're not just web, they're not just \[unintelligible 00:55:46.01\] I'm in talks with them right now about trying to figure this out. I'm like "Hey, these colours are better. The gradients are better. I know you like product excellence. I know that most of your targets are iOS and Android apps. Those are HDR spaces. And now the web is HDR. You can get HDR across the board now. Make that the common denominator and offer HEX as an export option."

\[56:09\] There is a plugin that you can get in Figma. Adobe XD does not have wide gamut colours. Pretty much it's exclusively Photoshop right now, and then web tools. There are a bunch of web tools that help you make HD colours. But yeah, I'm very much in the same boat as you are. And like if designers aren't handing these off to developers, it's probably not going to get done, except for those -- there are a lot of folks that spend a lot of time in design systems, managing the colours of their application, and building robust systems. They are going to be stoked on OK LCH, and these colour functions. They're going to get rid of all sorts of stuff, they're going to build it natively into their CSS, and they're going to get awesome results. So less code, better results... But yeah, until designers are handing it off, it's probably going to be a slow ball to get pushed up a hill... So it could be on you to do it.

Honestly, I think a lot of what we're going to see right now is some bottom-up education happening, where developers are like "I've got this new tool, and look at these gradients. They're sick." And the designers could be like "You think your gradients are better than mine? Ohhh! Your gradients ARE better than mine!" \[laughter\] And you'll be like "Um, yeah. Let's talk about it. Let's get these in the app. They look fresh." Anyway... So some of that is going to happen, too. Speaking of gradients... Can I share my tool?

**Nick Nisi:** Yes.

**Adam Argyle:** I want to announce a tool to help people. So I mentioned oklch.com, which is a phenomenal OK LCH colorpicker. I have been working for the past few months to help enable people into getting into these new colour spaces, to learning and seeing what CSS colour can do, and especially seeing the results that you get in CSS gradients. You can now go to gradient.style. And that's where I'm building a very much it looks like a design tool to help you build these new HDR gradients, and see the SDR version fallbacks. I'll generate a fallback gradient for you, and generate the new modern gradient for you. You can change colour spaces, you can do all this stuff. And it's really, really nice, really visual... And you can even drag it across from an SDR monitor to an HDR monitor, and kind of see it that way as well, and just see the change, and start to feel out these colours.

I think there are two main things on that tool that are really fun to do. Well, there are a lot of main things to do, but the first one is use the colorpicker. So if you see a little colour dot - that's when your colour stops - click it, and you'll get the world's first next-gen CSS colorpicker, where it supports every colour space that CSS supports. They're even grouped and tell you if they're HD, or SDR, and stuff like that, which is really nice. And they give you a little control to go play inside there. And it will convert. So if you have a HEX colour, for example, you can paste the HEX colour into the colour \[unintelligible 00:58:39.25\] open up the colour picker, go to OK LCH, it will convert the HEX to OK LCH, and then you can go bump the chroma up and be like "How much brighter can I make this HEX?" You'll like "Oh, crap, that's a lot brighter." And you can do that.

Another fun thing to try on the gradients that are in the bottom left; there are some presets where I've created some things for you to go explore and try on. And then there's a Discord if you want to join and ask questions and learn more about colour spaces, and about CSS colour. In the top right there's a settings cog; click that, and go to think - it's like Help and Feedback, or something like that. That'll pump you out to the Discord to come have conversations in there.

There's also -- just above that is a tips and tricks. You can click that, and I've put a bunch of hints all over the UI to help you learn about what the UI is doing, and help you get you the ball rolling into building a new gradient in these new colour spaces.

Yeah, gradient.style. I'm going to probably be working on it until the end of the year. You can tell some of the stuff's about done. It's in beta, but it's a really strong place to start as we transition as an industry out of SDR - which we've been in for 25 years - into HDR. It's just the future.

**Amelia Wattenberger:** This is so cool. I've just been poking around and not listening to you, but... \[laughter\] If you're listening, you should go check it out. Also, you can set the hue path; you can do like the longest path between two colours, instead of the shortest. That's cool.

**Adam Argyle:** \[01:00:07.13\] Yes. Okay, so this is such a cool -- and it only works for cylindrical colour spaces; HSL is a cylinder. It only works if the hue is an angle. And the way that it works is it's just like Zoolander. Like, literally, RGB has been like Zoolander this whole time. You know Zoolander could only turn right? You'd get to the end of the stage and be like "Oh, wait, I can only turn right."

**Nick Nisi:** Ami-turner

**Adam Argyle:** Not an Ami-turner that's awesome, dude. Now you can tell it to turn the other way. So basically, you would always take the short path, right? It'll always take the short, straight shot, or to always rotate around the clock the fastest way to get to its destination. And now you can say, "Hey, go the long way." And there's been people on Twitter making fun demos of this, where you can say, "Hey, I want a gradient from red to red, and I want you to go the long way." And it literally makes a rainbow, because it took the long way around; it collected every hue, all the way around, 360 degrees. If you open up my colour picker, and you see that little hue strip that shows the rainbow, where you're choosing the hue, that's literally a colour gradient that I've drawn, from red to red, telling it to do the longest hue, or the longer hue interpolation. It'll take a long way. It's so cool.

I used to have to make a gradient with like 12 stops in it to represent all the main hue points, or whatever. And even then it might be a little wrong. Now it's right. It's really cool. Yeah, hue interpolation... That's a new one, too. That's getting deep into the weeds of colour as well, because you've got -- yeah, that's the colour space, offering a feature of an angle rotation. Yeah, it's cool stuff.

**Amelia Wattenberger:** You've blown my mind. This is super-cool.

**Nick Nisi:** Yeah.

**Adam Argyle:** And it's all typed, Nick. It's typed, from top to bottom, dude. Typed. You can't break it. It will only work if you pass in proper length percentages, or lengths and stuff like that. It's good stuff. Or angles... Which means you can pass reds to it and be like -- that's one of my favourite colours to do, is too red. "Oh, yeah, this colour's too red." Dad colour joke...

**Nick Nisi:** This tool is really cool. And I'm looking at the CSS that -- you have the modern gradient, and then a classic gradient for each afterwards... And I was just curious, because I was looking at some other example too, and this English just in the middle of the gradients is blowing my mind. I don't even know how to search for it, but it's like "From zero degrees at centre in OK LCH decreasing." I don't even know -- my brain has shut off.

**Adam Argyle:** No, that's perfect. And if you look at the classic one, it has a lot of the same English in it. One of the differences is the in keyword, which is new with colour spaces. So you have these like definitions about the prelude, or like the first part of your gradient there is about size and position, and now we have the addition of which colour space do you want it in. And that's where those things are coming from. And that's sort of what I wanted my tool to also do. Because if you go to -- I don't know, some other gradient generator online, they don't tell you that there are these keywords. And some of the keywords are rad. Like, to-top-right is responsive, out of the box. Like, if you said 45 degrees, it's not responsive; it'll stay straight, and you can see that in the tool. As you resize the box, you'll see that the degrees stay still. But if you do top-right, it literally takes the first colour and makes sure that it ends perfectly in the bottom-left corner, and that the last colour ends perfectly at the top-right. That's why as you resize the box, the gradient line changes to make sure that in the top-right is the last colour, perfectly ending at the corner's edge.

And then if you go to the radial tool, and you look at things like farthest side, or nearest corner, my tool now visualizes that for you, so you can see what it's doing. It's really rad stuff. So some of these keywords, some of these features that are inside of gradients - they're they've been hidden for years, and I'm hoping this tool unlocks them for people, and they realize that "I can put a gradient in the centre with just a keyword? That's awesome!" And all this stuff.

So I'm hoping it's like multipronged here; it's giving you access to wide-gamut colours, a spec-compliant colorpicker, spec-compliant wide gamut gradients, and then just spec-compliance in general.

\[01:04:13.16\] The tool is facilitating these things for you... In terms of the linear, conic or radials powers, what are its superpowers; including double positions. Did you pull the second percentage on one of those colour stops? It's such a hidden feature of gradients that people don't know exists is double stop. You can have a double-position gradient, and you'll see my tool will split the circle in half, and then you'll have two crescents.

**Nick Nisi:** Yes...

**Amelia Wattenberger:** I was wondering what was going on there... \[laughs\]

**Adam Argyle:** Yeah, Nick's nodding his head. He's like "I see the two crescents." Okay, so you've got like a colour stop that says "Alight, just start to colour here." And then you add another colour stop, and it says "Alright..." "And move it from this colour, to that one, to the other stop." But if you split it, you say "I want this colour stop to span a range, and then transition to the other stop." And it also has superpowers; like, you can set the second one to zero, and it creates a hard stop. So your colour goes up to 10%, and then your second position's at zero, and it will end there. And you can make hard stop gradients really easy by using the double-position syntax.

I also in my tool have transition hints. And those are the sliders in between colour stops, which allow you to tell it how to transition between the two; which of the two colours is more dominant in the interpolation from one to the other. And then I visualize that on the gradient tool. You can see the little arrow thing, and you can drag it and see how it changes the gradients. So it's like, there's been hidden superpowers in here. It's like, specialists have only known, and I'm like "No, people need this. They need this in their hand", and so I started building a tool to put all this into one, and help folks out.

**Nick Nisi:** This is awesome. It's like those videos of people doing elaborate tie-dye patterns, where they're folding things in very specific ways, and then putting the dye on in very specific ways, and then they get some amazing pattern at the end, and they hang it up... I was watching one of those on Reddit recently, and so...

**Adam Argyle:** Sounds mesmerizing... \[laughs\]

**Amelia Wattenberger:** It does. \[laughter\]

**Adam Argyle:** That's kind of everything -- I mean, yeah, I mentioned Open Props; I have some stuff in there, too. So if you want to start in this like next-gen colour stuff, there's some good starter packs for you there. They're in beta right now. There's no Firefox support, so I'm not -- and I'm just playing with this idea, but I really like the way that it's headed right now, where you just import this one set of 15 custom properties, and then you can just change them however you want, and then you get any colour palette, of any hue, perfectly from light to dark, at any amount of vibrancy that you want. So no longer will you visit a website and be like "I've got 12 colours to choose from. I can choose jungle, or grape, or lemon..." That's gone. You're just gonna pull in 15 props and be like "No, hue 210. That's our brand hue. And now I've got an entire palette that's perfectly perceptually linear lightness", and you go nuts. That's really cool.

**Nick Nisi:** This is such a cool tool.

**Amelia Wattenberger:** He's just moving the sliders back and forth... \[laughs\]

**Nick Nisi:** I also love that it's encoding it into the URL too, so you can share what you create as well.

**Adam Argyle:** Yeah, you can definitely -- yeah, paste it into the chat. Let's see what you made, yo. The monstrosity...

**Nick Nisi:** Yeah, I was going to say - challenge; gradient. Style and share with us on the socials what you come up with.

**Adam Argyle:** Totally. I'm excited to see him. And I had fun naming all of them. I've got like Soundwave... Oh, here, there's one in the HD examples called Solid. Click that one. Did you know a gradient can take just one stop, and still be valid? You have to use the double position syntax, because you can say "Hey, I want this colour to span from zero to 100%." And now it's a single colour stop gradient that goes all the way across the canvas. A lot of people would reach for a background colour to do this, and you don't have to. So if you do a multi-layered gradient, you can put solid colours in there that way. This tool visualizes it for you, which I think is unique.

**Amelia Wattenberger:** \[01:08:04.02\] Yeah, this is the best kind of learning environment, where you're just kind of figuring things out as you go.

**Adam Argyle:** Yeah. Here, I'll share that one in the chat there. I tried some compression algorithms on the URL too, so I could fit more colour stops in there, using Base-64, and some other things... But I liked the readability that you have right now. You can kind of parse the URL... And it doesn't look tricky. You're not going to get sent a URL that's like "If I click this, what's going to happen?" \[laughter\] "I see some obfuscated data; that makes me feel uneasy." So it's not obfuscated... But anyway.

**Nick Nisi:** It might as well be straight CSS for me, at this point...

**Adam Argyle:** Yes. SvelteKit has been awesome on this tool. I already liked Svelte, but man, it's been phenomenal... And then it is TypeScript, but I use a very light amount of TypeScript. I'm like, "I just kind of understand my code." I don't want to go nuts with types, because it's just a slippery slope for me. Like, "Oh, I'll just type this parameter. Oh, I'll just type its return type. Oh, I'll just--" And then all of a sudden I'm like "Ohhh, what did I do?! My function was already working. There were no bugs. What am I doing? Like, I'm hardening it." You're like "Yeah, I guess..." I need tests though. I do need to write unit tests, and stuff. Furthermore, I don't have those yet.

**Nick Nisi:** Well, you have types. That's a good start.

**Amelia Wattenberger:** That's all you need.

**Adam Argyle:** Light types. I'm a light typer these days. I've been to the dark side of heavy typing, and I'm like "No, I'm a light typer."

**Nick Nisi:** Yeah. There's a balance, for sure. It's like that "Not now! Someone's wrong on the internet." Not now, there's a type that's slightly incorrect...

**Amelia Wattenberger:** \[laughs\] Somebody put "any" in my codebase...

**Nick Nisi:** Yeah... \[laughs\]

**Adam Argyle:** Well, y'all feel like you understand STR verse HDR now, and you're like "I've got some new functions to go try"? Yeah, what's remaining in your mind, other than like -- it's just a very tangible thing. Your eyes need to see it, your fingers are going to change numbers in these colour functions, and you're going to see the results... And that's definitely the next step, is to go play. So yeah, hopefully this playground is good for that.

**Nick Nisi:** Yeah, definitely it is. It gives you good ideas on how to do these things. My mind is empty at this point, trying to make sense of this... But I definitely see the value of these new colour values. It's just when to, or how to practically apply them is still like the difficult part for me. And it mostly comes down to -- if I receive a HEX colour from my UX team, I'm probably going to use that still. So the tooling needs to come around, but... Yeah, totally. It's really cool.

**Adam Argyle:** Yeah. I'll share my site in the chat there, just because -- yeah, you'll open it up, and you'll be like "Nothing here really looks HD." But it's me being the designer in like a subtle way; like, the background colour is not black, it is very dark, rich, cool gray. And if you open up the colorpicker...

Oh, Chrome DevTools has cool features for this, too. So does Safari, by the way. If you're debugging this in the browser, the Chrome DevTools colorpicker is updated now. You'll see a cut-off where Display P3 is, kind of like you saw on the oklch.com. You can convert in that tool between colour spaces... But it's really nice to visualize, when you're like "This colour doesn't feel that bright." And then when you go see, and you drag the thing down into the RGB colour, and you're like "Oh, okay." Like, when I see it downgraded, I definitely feel that, but you might not get that sense immediately that it's somehow special... But I don't know, this is one of those things. That's why Apple has had it for so long before everyone else; they knew that that subtlety couldn't be articulated by many, but that they would feel it and see its excellence. And hopefully, that's what you see on my site, too. Like, if you look at my code snippets on any of my blog posts, you'll be like "Wow, those colours are really neon." That's because I'm definitely pushing those to Display P3 maximum. That's fun stuff.

**Nick Nisi:** I did notice that, and I want a Vim colour scheme based on that now...

**Adam Argyle:** So yeah, how long until VS Code has HD colour support, and all of our colour themes now have better dark colours, richer dark colours, whiter whites, and more vibrant neons for all of our highlighting? I'm serious. We're all going to switch to colour themes that are HDR.

**Nick Nisi:** That's going to be amazing. Well, cool. Yeah, we will have all of these links in the show notes, including gradient. Style, which you heard about here first. Go share your amazing gradients on the socials, and with Adam, and join the Discord. Adam, anything else you want to add?

**Adam Argyle:** No... You all's show is so good. I really appreciate you having me on, and continue to make amazing content. Don't stop this. You all rock. I really appreciate it.

**Nick Nisi:** It's just because of amazing guests like you, so thank you for coming on. And Amelia, do you want to add anything else?

**Amelia Wattenberger:** No, I'm stoked to try this stuff out.

**Nick Nisi:** Same. Yes. I can't wait. I'm going to share a couple of gradients and see how they compare. Cool. Well, thank you so much for coming on, and we will catch you next time.

**Adam Argyle:** See you around.
