**Mat Ryder:** Hello there, and welcome to this very special new year's edition of Go Time. I'm Mat Ryder. Today we're having a special New Year's fireside chat. And where I'm from, it's traditional this time of year to thank people for all the hard work and all the effort that goes into things they do across the year... And I just want to say thank you to all the wonderful co-hosts of Go Time: Natalie, Angelica, Chris, Ian, Jon, and all the guests that join us. It's such a great show. I love listening to it. And I want to do a special tribute to the editors and the sound technicians. They go above and beyond, I think, every year, and deserve a bit of recognition. Just listen to this fire crackle, at this fireside event. It's just -- you can hear it. It's in HD. Furthermore, it's amazing.

And listen in the distance, birdsong. They're fading as the winter sun sets across the snowy rooftops. You can almost hear water trickling underneath the frozen surface of a stream. So not just water... It's underneath kind of a layer of ice, so it's muffled in some way. Isn't that beautiful? An articulated lorry careens around an icy corner. Three chickens emerge and cross the road without mention, and the camera slowly zooms into a fire around which there are some people having this fireside conversation. I wonder what they can hear... Let's meet the guests, and my co-hosts. Jon Calhoun. Hello, Jon. What can you hear?

**Jon Calhoun:** Hey, Mat? I hear a tea kettle as it begins to boil over the fire. So I pick it up and slowly pour a cup for everyone.

**Mat Ryder:** Oh, that's lovely. We're also joined by Kris Brandon. Hey, Kris. What can you hear?

**Kris Brandon:** I can hear popcorn popping faintly from the kitchen. It smells delicious. And I hear someone with a salt shaker salting an already-made batch. It's going to be pretty good.

**Mat Ryder:** Wow, that sounds great. Yeah, we'll be sharing that popcorn with Ian Lop shire, who's also here. Hello, Ian. What can you hear?

**Ian Lop shire:** Well, it's sunny in Brooklyn... The icicles outside my window are dripping... The subway goes by, and it rumbles the building a bit. Some of the icicles fall free, and crush the sidewalk. You hear a pedestrian yelp in surprise as it falls in front of them...

**Mat Ryder:** Oh, wow. Yeah. And I heard all of those things. Excellent. Well, let's get started then. I just think, this is it. New year, fresh start... I always feel at this time of year that we can really do anything, we can achieve anything. And it's really about January the 10th I realize that's not the case. Life is just as hard as it was. But I remain optimistic. But tell me, what are you excited about? Anything in particular?

**Jon Calhoun:** So I can jump in and say one of the things that I've seen recently, which I think you wanted to talk about later, Mat, is HTMX, which - I haven't gotten to use it, but looking at it was pretty cool.

**Mat Ryder:** Yep.

**Jon Calhoun:** Especially because I always like seeing technology that gives us sort of -- I guess allows us to sort of build more modern things, but also brings it back to like the simpler approach that we're kind of used to, rather than overcomplicating things. I tend to shy away from technology that's really overcomplicating stuff. So for anybody who hasn't seen it, HTMX is like a way of generating HTML on the server side, like you normally would with like a static server side rendered web application, but it allows you to build something that feels a little bit more like a single-page application.

**Mat Ryder:** Yeah. It's funny, because it's we sort of go on this evolution all the time of - that's how it used to be; it used to just generate HTML on the server, and some sites actually still do it like that... I think GitHub, by and large, has this kind of model, where the server generates all the content, and it ships it as one thing, and it just gets rendered on the frontend. And then of course, we started making that frontend richer with JavaScript and more interactive elements, more sort of loading data as you go... And so is HTMX kind of mix of those?

**Jon Calhoun:** From what I've seen, it seems very much to be a mix of that. But it's also interesting, like you said, some sites still do it the old way. But in my mind, I think there's way more sites generating server side HTML than people realize. It's just you don't read about them, because nobody wants to read about technology that's been around working for 10 years; they want to read about what somebody just came up with last week.

**Mat Ryder:** Yeah.

**Ian Lop shire:** Isn't PHP still powering like 60% of the internet? Those are all HTML server side generated...

**Jon Calhoun:** And they work really well. It's just -- it's one of those things that... I don't know, it's easy to get caught up in the "I want the most modern, cool thing." But I really enjoy seeing technology that kind of takes us a step back and like thinks "How can I get back to that simpler approach, while still getting some of the benefits of what we've learned in the last 10 years?"

**Mat Ryder:** I think it's an honourable pursuit, really; the simpler stuff is easier to maintain. You'll get benefits from having stuff simpler. And HTMX has the advantage of -- like, you wouldn't have a JavaScript framework at all running in the browser. So it's still just partial updates, from what I can tell. So you still only ask for bits of HTML, to update bits of the page. But that's kind of done in a declarative way. So you still get that Ajax kind of feel, but it's obviously much easier than writing all that stuff manually.

**Jon Calhoun:** \[06:02\] Alright. Mat, what are you excited about?

**Mat Ryder:** Well, how could we not mention ChatGPT? I mean, I am quite excited about where AI will take us, at least just from the sort of thinking of features and capabilities that could be delivered, and the sort of interactions you have could be so much more natural. It obviously has flaws, but have you tried chatting with it, anyone?

**Jon Calhoun:** I have, yes.

**Mat Ryder:** What did you ask it?

**Jon Calhoun:** I did a couple coding things, like generate a React element or a component that does this, and things like that... And I've spoken to other people who've done things like that... In part because, like you were saying earlier about keeping things simple so you can maintain them, I also see GPT as being a tool that could potentially allow one developer to do kind of the work that multiple developers have done in the past... Or there have been times when people said the full-stack web developer's kind of going away, but I see tools like ChatGPT possibly bringing that back to have one person who sort of maintains a pretty complex application... So I like experimenting with stuff like that to see like "Okay, what all can this do? Can it help me do some stuff, so I don't really have to master React or something else that I want to use?"

**Ian Lop shire:** How do you think it compares to like Copilot? It seems more versatile, but I've not used Copilot yet, so...

**Jon Calhoun:** So I haven't used Copilot that much, because I've been doing a lot of recording for like course type stuff, and I had Copilot on, and I was loving it, but then I went to record and all of a sudden it would give me a block that was like meant to be the entire lesson I was recording... And I'm like "Well, that's not very useful, if it just throws it all up there..." So I'm like "Well, I've got to turn this off for the time being, because it's not useful."

**Mat Ryder:** Can you set spoilers to false?

**Jon Calhoun:** Or it wasn't that it was useful, it was too useful.

**Mat Ryder:** Yeah. I used it. I used Copilot and found it... Furthermore, I don't think it's going to -- well, I don't know about this idea of it replacing people, but when you're writing code that's a bit repetitive, that has a pattern that's predictable... Like sometimes in unit testing, you sometimes end up writing a list of things - it does that stuff very well; it picks example data very well. And so it does -- you can see its kind of carrying a lot of context, but you still have to select from that; you have to choose still what's right and what's wrong. So you are still very much in control of what code goes in.

**Jon Calhoun:** The best way I've seen it described is it can make developers much more productive, but I don't expect my mom to suddenly start building web applications next week. Like, no matter how powerful it is, I think there's always going to be some limitation that you kind of have to have an understanding of what's going on.

**Mat Ryder:** Yeah. Is your mom not into web? She's more like --

**Jon Calhoun:** She's not into web...

**Mat Ryder:** ...backend.

**Jon Calhoun:** She's more of a hardware person.

**Mat Ryder:** Oh, more hardware. Yeah.

**Jon Calhoun:** No, she does not program at all.

**Mat Ryder:** No. Not yet.

**Kris Brandon:** I think with ChatGPT, and also to some degree with Copilot, I think we're getting a little bit better at understanding that we're not building these things to replace people, but more to augment and help people... So this has been a failing of AI in the past, if it's been like "Oh, we're going to replace all of these people, and all these industries will go away", and then it is just like immediately fails the Nazi test, or something like that... And I feel like now we're being much more careful about what these things are meant to do, and we're making them much more effective. So I'm kind of excited to see us kind of move more in that direction as an industry, and start learning from the mistakes we've made in the past.

**Jon Calhoun:** Some of these confused me though, because -- so I have a friend who plays Roblox with her kid, and the one game she was playing was like gas station attendant. Like, you're basically working as a gas station attendant. And I'm just imagining somebody building AI that learns from this to -- like, I don't know, is that really a fun game? It's just so weird to me, but I'm like, I could see somebody building an AI that's like "Let's learn how to be a gas station attendant from all these people." But like you said, all it takes is a couple of kids who -- you know, when they're playing a game, usually you're like "How can I break this, or do something silly?" So it's like, where do you actually get the data to learn from for this stuff?

**Mat Ryder:** Not sure if I'd be happy with the Terminator doing the petrol. I'd just be worried... Also, if it walks around, it probably makes sparks. That's dangerous to have at a petrol station. And then it's always asking about Jon Connor, and it's like "I don't know John Connor. Can you just give me unleaded?"

**Jon Calhoun:** It like forces you to use the least environmentally friendly gas?

**Mat Ryder:** \[10:10\] Yeah, exactly, because it's paid for by Big Oil.

**Jon Calhoun:** It's like "I'm going to kill all these humans..."

**Mat Ryder:** Yeah. \[laughs\] That's a Shell Terminator. "Shell. The best terminators." At some point, we are going to get in legal trouble. Hopefully, we don't kick the year off that way...

**Jon Calhoun:** Do you think Shell is listening to our podcast and giving us grief?

**Mat Ryder:** Yeah, maybe we should just offset that and just say, "Shell, we do a great job." Just do a little nice advert for them as well.

**Kris Brandon:** You never know. Shell could write all of their software in Go.

**Jon Calhoun:** It's possible. That just means we need to say a couple of nice things about their gas... I'm sure they've got some sort of additive they put in it, or something...

**Kris Brandon:** They say it cleans your engine, so...

**Jon Calhoun:** I find it hard to believe that something that's burning gas in your engine is actually cleaning it. It might help a little bit, but...

**Ian Lop shire:** Well, if it does clean your engine, doesn't that mean all that dirt goes out the exhaust, so it pollutes more?

**Mat Ryder:** Yeah. Keep it in your engine, dirty boys and girls... We don't want that in the air and in our lungs. No, but do clean up the air. Actually, that's something I get quite excited about, is innovation in climate technology, more awareness around clean cities, and the London low-- there's a lot of people annoyed, a lot of drivers are annoyed, but they're extending the low-emission zone in London to be a much wider area... So this means you basically pay if you have a car that's pumping poison into people. So yeah, you can still put poison in people, but you're going to have to pay for the pleasure, which is better than it just being free, when they used to just be able to put poison in you for free... So I'm quite excited about new technology, new innovation there, and what could come.

**Jon Calhoun:** A lot of that stuff is definitely intriguing. I guess I'm kind of -- I'm in a weird position where I drive a bigger truck, that burns gas... That's partially out of like necessity. Right now, the F150 electric truck just doesn't work for a lot of the things I want to do... An example is if you want to haul a camper, or if you want to haul a trailer with new equipment, or something on it - it's got very limited range at the moment. So I'm optimistic to see where it can go, especially when you see -- like, didn't Tesla recently release their semi-truck or electric semi-truck? So like seeing that, and it has -- I think it's supposed to have like a 400-mile range, which is fantastic. The problem with like the F150 Lightning is I think the range when you're towing is like 120 miles or 150 miles, and then you have to charge for like an hour, and that's not really going to work that well.

**Mat Ryder:** Yeah.

**Jon Calhoun:** So I'm curious to see where it goes, but I have to refrain myself from getting too excited, because I know it's not going to work for me. I don't want to get excited about something I can't have.

**Mat Ryder:** Why do you need the 400 miles range? Is that just how close the nearest shops are to where you live?

**Jon Calhoun:** It just depends on what you're doing or where you're going. An example is if you've only got 120 miles, that means you can basically get to someplace an hour away and get back without a charge. And sometimes you're going places that don't have electricity to charge while you're there.

**Mat Ryder:** Are you going places that don't have electricity?

**Jon Calhoun:** I am actually going to places like that.

**Mat Ryder:** Wow.

**Jon Calhoun:** I also drive to like North Carolina quite frequently, which is like 360 miles...

**Mat Ryder:** Don't they have electricity there?

**Jon Calhoun:** I mean, they have electricity there... \[laughter\] But I'm not going to get there in one trip, right?

**Mat Ryder:** Yeah, got it.

**Jon Calhoun:** And then the other part of that is like if you go to charge with a trailer on... Because I have a camper; we go camping a lot. And if you try to charge with the trailer on, trying to find a charging station that you can pull into and be like "Hey, let's plug in and take all the stations with my trailer" - like, that's not going to make anybody happy.

**Mat Ryder:** Right...

**Kris Brandon:** I think electric cars are one of those interesting places where it's like, I think we got the innovation slightly wrong by trying to like go all-in, with like "Let's put giant batteries in cars." And I feel like the -- what was it, like the Chevy Bolt, or Volt, whichever one was like the hybrid, but it was like "Oh, we have like a small gas engine, and then we have a bunch of batteries, and the batteries will get you like 60 to 80 miles", or whatever, and then you have the gas engine for if you want to go further - that's like the perfect model for like so many people, and it would have just like limited gas for so many people... It feels like that type of hybrid model would have gotten us further faster. Instead, we're just trying to be like "No, we're going to build things that don't have gas at all", and then it's just very tricky to actually make those things work. I feel like we do that a lot in tech as well, so it's not just like...

**Jon Calhoun:** \[14:20\] Yeah. The one upside though to like going all-in the way they did is I feel like it really forced the infrastructure for charging stations to really quickly come along. So that's an upside to going the way we did. But I agree with you that going with the hybrid approach for a lot of things is a much easier way to get people in, especially when it's like not something drastically new. They can still go to a gas station. It's not like a change of what they're used to. And then there's also all the -- I guess I'm kind of waiting to see what the technology does for things like weed eaters and lawn equipment, essentially... Because we've all probably lived somewhere where you hear people going around running this equipment, and they run like terrible gas, that's like half oil, it' burning into the environment all day long, just burning it up... And I'm sure that's got to contribute a lot to pollution, and that sort of stuff. And those things seem like things that you could pretty easily replace with batteries, where they could have a truck with like a couple extra batteries on there and just swap out at every different job site.

**Kris Brandon:** Yeah. Battery-powered lawn equipment is a really cool space, especially even just like at a human level. Leaf blowers are terrible for your hearing, because they are so loud... And just having ones that don't need to be loud, because it's just like a battery-powered thing would be good from a humanitarian perspective as well.

**Mat Ryder:** Where do you blow the leaves to?

**Jon Calhoun:** It depends on where you live. Where I live, part of your taxes if you live in the boroughs is they actually pay somebody to come around with like a big truck that has -- usually it's like a vacuum that sucks them up and mulches them. So everybody sort of blows them into a big pile next to the road, and then the truck drives up the road and sucks them all up and mulches them.

**Mat Ryder:** That sounds amazing. I'd love to watch that happen. I've never seen anything like that. Put a link to that on YouTube in the show notes, for anyone like me, that would love to see a great big machine sucking up loads of leaves. But I feel like this is sort of ruining autumn though as well. I'd be like "Can you just leave autumn for a few more days?" It's my favourite season.

**Ian Lop shire:** Well, it's fun when everyone has the giant piles of leaves in the front, on the street, you know... It's still kind of nice.

**Mat Ryder:** Oh, you kick through them, or jump in them, have a frolic, that sort of thing...?

**Ian Lop shire:** Why not?

**Mat Ryder:** Yeah.

**Kris Brandon:** So dogs love to like to run through piles of leaves...

**Mat Ryder:** As long as they're just running through piles of things, and not making them. That's the danger. You never know -- you can't just jump in assuming it's going to be a nice -- like a Disney film, a fresh bed of autumn leaves. There could well be spikes in there that someone's put in maliciously, so be careful, kids...

**Jon Calhoun:** My daughter actually did that, I think when she was three...

**Mat Ryder:** What...?

**Jon Calhoun:** We had a pile of leaves, and she had seen a video of like a kid jumping in a really massive pile... And this one wasn't that big, and we thought she was just going to run through it... And she just went and just like dove; like, just fell in... And she came up crying, and I felt so bad. And I'm like, "I did not see that coming."

**Mat Ryder:** Yeah...

**Jon Calhoun:** But she hasn't done it since. So she learned her lesson, I guess.

**Mat Ryder:** Yeah. Well, it's a brutal way to learn. You've got to be careful with Disney films, because I once tried to get loads of little birds to help me get dressed, and it took me longer to get dressed, if anything. It was no help whatsoever. So you've just got to be careful what you believe from those animated documentaries...

So talking about batteries, towards the end of 2022 there was a kind of major breakthrough in fusion energy... And this is something that I'm very excited about, because for the first time, they were able to get out more energy than they put in. So they put a lot of energy in to sort of spark it and initiate it, and there's a tiny bit of fuel, and then that fuel, essentially through the reaction, ends up releasing now more energy. I think 50% more than what was put in. So it's kind of viable. It turns out science has nailed it again. What do you think of this? Are you excited?

**Ian Lop shire:** \[18:02\] I mean, that was only at the reaction level. Right? They didn't generate more energy than they put in. They didn't capture that, right?

**Mat Ryder:** Right. But they got out, they saw that was at least possible for the first time. I guess that was the breakthrough. Right? You sound skeptical, Ian. You're not into this. Furthermore, you don't work for big oil, you don't work for Shell, do you?

**Ian Lop shire:** \[laughs\] Maybe. Maybe. No, I mean, fusion - what do they say, it's always 20 years away? Never 19? I don't know. I think it'd be cool, but definitely skeptical. Furthermore, I think there are a lot of challenges to overcome.

**Mat Ryder:** Yeah, I'm sure that's true... But very brutal view there. So buck your ideas up, science, because Ian so far is not impressed...

**Ian Lop shire:** \[laughs\]

**Mat Ryder:** Jon are you impressed by that, are you excited by this idea of free, clean energy?

**Jon Calhoun:** I mean, I think any free clean energy tech, or even just more efficient energy advancements are interesting to read about; even nuclear stuff, which I feel like the US especially is very anti-nuclear for the most part... But it's interesting to read about...

**Mat Ryder:** Which is weird, because you've produced some of the best superheroes that way. I'm surprised there isn't more support for it.

**Jon Calhoun:** So what you're saying is it's not that people don't want nuclear energy, they just don't want superheroes. They're worried about that.

**Mat Ryder:** They don't want the mutants having special powers, and they can like to see their Wi-Fi, and stuff. That was in one of the shows... One of the shows there, I think it was Heroes, one of the characters somehow could connect to Wi-Fi. So he has to know the HTTP protocols, the TCP protocols... Think of all the stuff he has to know in order to make that work. Smart guy.

**Jon Calhoun:** I'd like to know how he developed this superpower...

**Mat Ryder:** Yeah.

**Jon Calhoun:** Because you'd think that it would have to be ingrained into him, but there's no way he's like mentally thinking, "Oh, we better send this header."

**Mat Ryder:** He was like brought up in a Best Buy, and he was able to learn it from a young age, do you think?

**Jon Calhoun:** You can only tap into HTTP, no HTTPS...?

**Mat Ryder:** \[laughs\] Yeah. Yeah. Well, obviously. Because he can't decrypt stuff like that in his brain, can he? And what does it look like? Oh, I don't know. Anyway...

**Jon Calhoun:** I thought you've got limitations on the guy who can just mentally connect to Wi-Fi.

**Mat Ryder:** Yeah I supposed you can not just connect, but you effectively use it, right? I assume. I don't know.

**Kris Brandon:** I mean, the writers of TV shows never know how any of this technology works, so we can't dig too much into it.

**Mat Ryder:** Yeah... Shame, ain't it?

**Jon Calhoun:** I don't know, Kris; every hacking movie I've seen, they're spot on. You type "launch terminal" or something, and then you're in.

**Mat Ryder:** Yeah.

**Kris Brandon:** You've got to get through the 20 or 50 firewalls that they've got set up, and there's a nice GUI giving you "Oh, you've broken through this--" or "The hackers have gotten through this many firewalls."

**Jon Calhoun:** Yeah. I love how there's also always a progress bar for like cracking the password... It's like "We know at exactly this time we're going to get the right one."

**Mat Ryder:** Yeah, we know which one it is. Yeah, I like that. You have a cube, and the cube has got to be completely full, and then it clicks together one by one as the different sectors are completed... That's also very... They nailed it sometimes, didn't they? Well, so fusion energy, Kris... You've got to be excited about that, haven't you?

**Kris Brandon:** Oh, yes. I'm kind of here just like - nuclear energy is actually like pretty good, and has a lot of the same kind of features, but people are scared of it, because they fear the worst... The same thing with people fearing flying, because they heard about some planes that fell out of the sky. And it's like, yes. And you can probably name most of them, which means it happens basically never.

I was watching some interesting stuff on nuclear fission generation, and people are all scared of like radioactive material, but the video I was watching kind of pointed out that - yeah, there's more radioactive material put into the air every year by mining coal than there is from all the material generated from all the nuclear plants we've ever had. Because there's radioactive stuff all over the place, and mining coal is just doing that, and spewing it into the air in the process.

So it's just like, a lot of the fears around nuclear stuff is unfounded, but I feel like nuclear fusion could head down the same path, where people could be really scared of the downsides of like uncontrollable things, whether they can actually happen or not...

\[22:04\] So I feel like we have to figure out how to solve that problem before we can kind of move forward... Because yeah, people like what they already have, even if what we have is already super-dangerous, right? Same thing with like flying, where people are like "I'm going to drive instead", and it's like "You are much more likely to die while driving than die while flying."

**Ian Lop shire:** Driving is terrifying.

**Mat Ryder:** Happy New Year, everybody... Yeah, I kind of know what you mean. I think fusion is a lot -- like, I don't think it can melt down in the same way. I think it has kind of safety properties. But like you say, the facts often don't matter when we get into... You know, I don't want to have a go at the flat Earth people. You do you...

**Kris Brandon:** I mean, it's like, most nuclear plants are designed in a way where they also can't really melt down, but people don't believe that.

**Mat Ryder:** Because it has happened; that's it, I guess. Once it's happened...

**Jon Calhoun:** I could also see the fusion when -- like, doesn't fusion allow us to simulate things that happen in stars?

**Kris Brandon:** Yeah.

**Jon Calhoun:** Or something like that. So I could see people being like "Oh, we're going to have like a star that could essentially explode, and be as hot as the sun", or something. I'm not saying that can't happen. I'm saying I could see people making these weird leaps when they read something.

**Kris Brandon:** Or they'll be like "Hey, you might create a black hole somehow, and destroy the planet."

**Jon Calhoun:** That's exactly what I was thinking.

**Mat Ryder:** Well, that could have happened. That was very unlikely, but when they switched on the CERN particle accelerator that time, there was apparently a tiny chance it could make a black hole and swallow the earth. It just didn't. But you've got to be able to fail.

**Jon Calhoun:** It's like, "We just won't tell anybody. Ask for forgiveness, instead of permission", it's one of those...

**Mat Ryder:** That's it. Don't worry about it. To be honest, Jon, even you just positing what could be made -- like, that's how conspiracy theories start on Go Time. And they get out of hand. We're joking, but I don't think they --

**Kris Brandon:** I mean, in that fusion experiment it got up to (what) 3 million degrees Celsius? That's pretty hot... Like, that could melt some stuff.

**Mat Ryder:** Yeah, we could melt the moon if we wanted to, with that, I reckon.

**Jon Calhoun:** I feel like when you get to a certain temperature, my brain just does not process...

**Mat Ryder:** Yeah. You wouldn't get much thinking done at 3000 degrees, Jon?

**Jon Calhoun:** No, I don't think so.

**Mat Ryder:** Once it gets to 2000, you'd be like "I'm going to step out five minutes, because it's getting a bit..." The thing about this is - so imagine it works, and we have these new power stations that use fusion... It's clean, it's basically limitless... I guess the price of energy becomes negligible, because it's just solved, essentially... So this is the future I'm painting. What are we then excited about? What changes in our lives? And I think transport is probably one area where things are going to change if energy is limitless and free.

**Kris Brandon:** I don't want to burst your bubble, but I don't think energy will ever be free. \[laughs\]

**Mat Ryder:** Oh, they're gonna just keep charging us...?

**Jon Calhoun:** I mean, they definitely have to like pay to like -- there's got to be a network to get energy everywhere. So you've got to have people you pay for that.

**Mat Ryder:** It's fine. It's negligible.

**Jon Calhoun:** I don't know what percentage of the cost of like running an electric company is keeping the power lines up and everything, but...

**Mat Ryder:** Good point. Fine. So maybe you still pay, but I don't know, it's going to be like your phone bill - you get unlimited data, and just do as much electric stuff as you like.

**Ian Lop shire:** I think if fusion happens, and energy is free, I think all of a sudden desalinating water is super-easy, and so many people's lives are saved, just because we can give them clean water...

**Mat Ryder:** That's a great one.

**Ian Lop shire:** That's what I'd be excited about.

**Mat Ryder:** Yeah. There are other health ones I think as well. I would get like loads of fridge freezers, and have them at the Arctic... You know, there are big ones that have ice machines on the front. Jam the front, so that ice constantly is just coming out whenever it's ready, and just leave them running. And get loads of them, like a whole warehouse full, and you're starting to replenish the ice.

**Jon Calhoun:** I literally think there's a startup that is working on big lasers that beam heat into space in the Arctic to cool it back down... Like, the real thing.

**Mat Ryder:** Oh, really? Oh, wow. That's good. A lot of science does get invented on Go Time. I mean, it's jokes to us, but they don't know that.

**Kris Brandon:** \[26:04\] I don't know, I'm going to be contrarian again... Some of our problem isn't even power generation, it's like our electrical infrastructure. We can generate more power than we can actually transmit. I think it was like in Vermont, they wanted to build another -- I think it was a solar farm, and they were basically like "No, because we don't have the transmission lines to do anything with this electricity. It would just go nowhere."

**Jon Calhoun:** I mean, I also think about places like Africa, where there's just no infrastructure -- like, even if we had fusion energy, I don't think it would really help them at this point... So there are a lot of other logistical issues that come into play.

**Mat Ryder:** Yeah, but it's definitely like, a lot of the energy transfer is wasteful, I guess... So we can afford that waste, maybe, for a bit. So it might give us an advantage. I don't know if -- how good is this wireless power thing? Because I feel myself like being like my uncle that's skeptical of new technology now. The idea that as long as a device can just see your phone, it sort of beam forms on it and fires energy at it to charge it.

**Ian Lop shire:** I mean, I don't think we can get past the inverse square law, right? So...

**Mat Ryder:** Go on, tell us about that.

**Ian Lop shire:** I mean, as distance doubles, power decreases by 4x, right? So as you go out...

**Mat Ryder:** Turn it up, though...

**Ian Lop shire:** Well, then if you step close to it, you... \[laughs\]

**Mat Ryder:** Yeah, don't go close to it.

**Jon Calhoun:** Mat's trying to tell everybody it's safe, while he's also just like beaming it, burning anybody who gets near the source...

**Mat Ryder:** Yeah, I think you'd definitely need to put up some signs, and just be like "It is recommended -- diversion this way around the planet. Don't go in this line." But no, do it high up, or underground. I don't know, I can't solve all the problems.

What about drones, though? Drones, I think, could be for transport, when we've got unlimited power. You could order a drone on your app, like a big one, it flies down, it's like a big a car, and you get in it, you can have a couch or a bed, charge your phone, plug that in... And it flies off and just drops you off places.

**Kris Brandon:** Mat, you're coming up with all the ideas... Like, we have good ways of solving these problems already. They're just poorly deployed. There are a lot of logistical problems with drones. That's why drone delivery doesn't exist, because the FAA requires that you can see the drone while you're flying it. And also, a lot of people don't have like backyards and things, where you can land a drone... And also, I don't trust a lot of people; I don't trust drones to just be flying... It's like the same thing with flying cars. We can't deal with cars, people driving in 2D space; you don't want them driving in 3D space.

**Mat Ryder:** But there's a whole other D to get into. If you're going to crash, just go into one of the other D's. And plus, it would be from the beginning automated only, so it wouldn't be humans driving them, I think.

**Kris Brandon:** I like that even less... That means software engineers are in charge of making sure this stuff doesn't break, and I...

**Mat Ryder:** Yeah, that's a good point. We don't know what we're doing.

**Jon Calhoun:** I mean, in Mat's defence, drones delivering batteries sounds a lot better than drones delivering missiles.

**Kris Brandon:** Yes.

**Mat Ryder:** Oh, so the drones are delivering -- what, they can just drop on your car and change your battery while you're driving along? That solves your range problem.

**Jon Calhoun:** I didn't know what -- you were talking about having a drone where you get inside and charge your phone... I think it'd be a little more practical to like drop off a battery and leave, but...

**Mat Ryder:** NO, you want to get in it and have that whole experience, and you should be able to like to get in London at like 9pm, and it's going to fly you to Edinburgh overnight. So you just get in... It's like a hotel room. You go to sleep, smooth ride...

**Kris Brandon:** You mean like a sleeper train?

**Mat Ryder:** It's like a sleeper drone, but yeah...

**Kris Brandon:** Now we've somehow wound up in V-tolls, and now we're like "Oh, let's--"

**Mat Ryder:** Yeah. It could go on a train; like, they could fly from your house, or pick you up nearby. Some people have balconies, in the cities... They could just climb out on the balcony and just climb onto it up some steps; do it safely, obviously... Then you're straight on the drone. Off you go. Maybe it could put us on a sleeper train. It's more efficient. But you're just in this capsule that's just like screens. So as far as you're concerned, you could be underground, listen to -- You could be underwater. Listen to this sound. We're underwater now... You can hear that... And I don't know, we've whooshed out of the ocean, and now we're whooshing, and you can hear the wind blowing as we fly through the air... Excellent work there by the sound crew.

**Jon Calhoun:** \[30:15\] So when you said that you believe -- like, for the first of January to like the 10th, you believe you can do anything with your code, or with anything... You weren't joking, were you? \[laughter\]

**Mat Ryder:** Yeah. I felt I could write software for this... Just as an open source project; just mock out the hardware. It's a very common practice.

**Jon Calhoun:** Alright... I think we need like a recap at the end of January, when you're back to realistic mode. You'll be like "No, none of that will work."

**Mat Ryder:** I'm going to be miserable like you, going "No, that's not going to happen. Forget it." I wrote it down, it's supposed to be New Year's.

**Jon Calhoun:** I think we'll see some awesome stuff, I just -- I'm looking at more incremental things, I guess.

**Kris Brandon:** I feel like the way to be successful with your New Year's resolutions is to set sane things, that you can actually achieve.

**Mat Ryder:** Okay, that's a good idea... So let's talk New Year's resolutions then, because I do have one, and that is to read more fiction. I always find, as I get into fiction, I'm just thinking "This isn't true." And then I think "I could be reading something that's true", and I sort of don't really get on with it. Is that sacrilege, Kris?

**Jon Calhoun:** I feel like we just need to like swap then, because I can pretty much only read fiction... I don't know why, just - for whatever reason... When I'm reading, it's more of like a relaxing type thing for me, or shutting my brain off.

**Mat Ryder:** When you say swap...

**Jon Calhoun:** I mean, we both take about 50% of what we're reading and somehow make our brains accept the other person's 50%...

**Mat Ryder:** Yeah. So we're swapping some of our brain then, basically.

**Jon Calhoun:** Yeah, just a little bit. Maybe I'll take your left side, and you'll take my left side...

**Mat Ryder:** There you go. We probably could do that... If only we'd been less safe about our nuclear strategy. We could relax the nuclear safety rules and roll the dice and see what happens. I think you could get some stuff like that. It'd be great.

**Jon Calhoun:** So what do you read now, Mat?

**Mat Ryder:** I read a lot of history bits... I've been reading a lot of management books. They're quite interesting. I've got a book here called "But how do we know?", which takes you from a logic gate, like NAND gates, and then tells you how to make a bit, and then how a processor works... And kind of all the way up to building a computer. There's another one online someone told me about, where you go NAND gates to Tetris, which I think is quite cool. So it's stuff like that, where I feel like I'm learning something. But of course, I'm sure you learn things from fiction...

**Jon Calhoun:** But you're still like -- you're reading for enjoyment. When you say like a management book, to me that doesn't sound like something I'd read for enjoyment. It's more like I'm reading this to better myself.

**Mat Ryder:** Yeah... That's the thing. Like, I need to just be okay with reading something for its own sake, probably. Maybe that's it. I've revealed too much about myself. What's your New Year's resolution?

**Ian Lop shire:** I have a very simple one. I don't want to buy a new iPhone this year. I still have the 13. Furthermore, I want to do the full two years, at least...

**Mat Ryder:** Ambitious goal.

**Ian Lop shire:** I'm going to resist.

**Mat Ryder:** What feature would you not be able to resist? If Tim Cook gets up, and he's like "Nah --" You know, he does it in his voice; I can't do it. It's offensive, probably. What's the feature he announces, and you're like "Right, I'm throwing that New Year's resolution in the bin. I'm having it"?

**Ian Lop shire:** Well, I mean, if it's anything like the last six years, nothing. I feel like smartphones are already --

**Mat Ryder:** Smart enough.

**Ian Lop shire:** I guess it's like "You never have to charge this ever again." It has a fusion power thing in it.

**Mat Ryder:** Yeah. That'd be good. You never have to charge it again, but you might get hot if you stand in certain parts of your house.

**Jon Calhoun:** I'm like hoping an Apple engineer is watching this and somehow emails Ian, and they're like "For $1 you can upgrade." It can't be free, because he's got to actually buy it, but...

**Mat Ryder:** You just want him to fail, essentially.

**Jon Calhoun:** Just to see how committed he is to this.

**Mat Ryder:** Yeah. And Apple --

**Jon Calhoun:** Because it sounds like an easy resolution...

**Ian Lop shire:** Okay, if someone was like "Yes, new iPhone for $1", I would fail. I'm sorry. It would happen.

**Mat Ryder:** \[34:05\] But what if it had little helicopter blades on the back, and you could say like "Phone, come here", and then it's like little helicopter blades come on this -- listen to them now; you can hear them switching on, like a little drone... Up the phone flies, comes over to you, and it lands in your hand, and you never lose your phone again.

**Ian Lop shire:** I think I might pay to get rid of that one, actually.

**Mat Ryder:** You don't want to find your phone.

**Ian Lop shire:** I don't want a phone with spinning blades on it...

**Mat Ryder:** Yeah, be careful. Do be careful around them. They are lethal if you're not careful.

**Ian Lop shire:** You've got to duck out the way...

**Kris Brandon:** I feel like I used to be someone that would upgrade my phone every year, and then somewhere along the path I just stopped. I guess it was like with the iPhone 10. Like, I got the iPhone 10, and then I wasn't interested in upgrading. And then I was like "Okay, now this thing is slow, very slow, and it's annoying." So then I got like a 12, and that's where I am now. I'm just kind of like -- I don't know, I was like "Oh, the 13th... Meh." The 14 came out, I was like "Meh..." I'm like "Okay, maybe when the 15 comes out." Maybe I'll be on this like every three-year upgrade cycle sort of thing.

**Ian Lop shire:** I objectively know it does nothing new, nothing better. There's no reason to buy it. But I still want it. Apple's done a good job advertising to me over the years.

**Mat Ryder:** Yeah.

**Jon Calhoun:** I don't think it's just phones that pull that off though. There are a lot of things where people want the new one, even if it's not significantly improved.

**Mat Ryder:** Yeah. I'm guilty of that a bit... But I also do that thing, try and resist it... And two years is what I also try and do. Because I used to do that exact same thing, every year. Because there'd always be someone to hand it down to, in the family, people. So it was always kind of an excuse, really. I can get the new phone, and then someone else gets a phone, and I could turn that into a good thing in my brain... Instead of a bad thing. But yeah, I try not to.

**Jon Calhoun:** It's not as bad in that sense. My mom's always done that; like, my sister gets a new phone, my mom takes her old phone, and then they do something with the old one. But in that case, my mom's running like four years behind, my sister every two years, or something... So it's not like terrible, but -- and I get how that makes it easier to rationalize.

**Mat Ryder:** Yeah. No, but it's good. You're doing some good. Ian's rummaging around in the background there...

**Ian Lop shire:** I was going to try to find my stack of old iPhones, but...

**Mat Ryder:** He's got them all, like a computer museum. Wow.

**Jon Calhoun:** So Ian is definitely not handing them down.

**Ian Lop shire:** Well, some of them are broken, you know?

**Mat Ryder:** Yeah... Oh, what happened to that one?

**Ian Lop shire:** I have no idea. I probably dropped it. I'm not a case person, so...

**Mat Ryder:** Who wouldn't drop it if you had the little blades on the back? Because it would just notice, with the accelerometers, that it's falling, and then spins up the little chopper... Tiny Chopper it's called.

**Kris Brandon:** I hope no one's around, so it doesn't like to chop your finger off, or something.

**Mat Ryder:** Well, if they're around, they'd catch the phone...

**Kris Brandon:** Yeah, that's not how that works...

**Mat Ryder:** Well, yeah. If they're not good, then maybe they deserve a little blade in the hand, just as a reminder.

**Kris Brandon:** Have you never like fumbled your phone, trying to like to catch it, and it still falls?

**Mat Ryder:** But I think you'd get used to it. You'd be like "I've dropped my phone. Everyone step back! Get back! I've dropped my phone!" The first version is not going to be as good, so it's going to be a bit more dangerous; the blades will probably be enormous as well... So bear that in mind, for the first version. Mapping it.

**Kris Brandon:** Apple's trying to get rid of the SIM card slot, and the charger. They're like "We need more space in the phone."

**Mat Ryder:** Yeah, for these blades.

**Kris Brandon:** They're going to put blades...?

**Mat Ryder:** What do you think they're clearing out the space for? You'd hope battery, but not so far... Actually, that's one thing when you get a new device like that - the battery just seems like it lasts forever. Those first few weeks, when you're not used to it, and it probably just is peak performance. They just last forever. When I got my last phone, it was like two days that I hadn't charged it, and it was still fine. You wouldn't believe it.

**Jon Calhoun:** Do you have all your apps installed?

**Mat Ryder:** \[37:57\] No, you can't use it; it drains the battery. You can't use it at all if you want it to last two days.

**Jon Calhoun:** Whenever you get a new phone, do you transfer all your apps over, or do you like start fresh and install them as you need them?

**Mat Ryder:** I start fresh, because I used to love setting up devices, because it was so nostalgic for me. I'd get like a computer for Christmas maybe, and then I had to learn it, and had to just spend hours setting it up, and figuring out what it could do, and the workbench, or the desktop software, whatever... And it's kind of like that same thing for iPhones for a while. And then now I'm just like "No, I don't want the hassle now." It's the first time I felt like it's -- I'm sort of getting old, because I've lost that little bit...

**Jon Calhoun:** I feel like I'm getting old when I don't do updates for stuff all the time, because I'm like "I just need to get work done. I don't care about updates anymore." When I was young, I did like every update as soon as I could.

**Mat Ryder:** Yeah.

**Kris Brandon:** I've gone so far on the other end of the adoption scale now, with especially OS updates... I'm so terrible with -- like, I'm still running iOS 15. Some of my computers are still running the older macOS'ES... I'm just like "Meh..."

**Mat Ryder:** What, Mountain Lion? Are you still running Mountain Lion?

**Kris Brandon:** Not that old...

**Jon Calhoun:** I feel like the hard part for me is like the minute you -- like, every time you do an update, and it hurts your productivity, or you spend half a day trying to fix something because of the update... Like, when you're younger, you kind of go through, and it's like "Whatever..." But then you hit a certain point where you've just done it so many times that you're just like "I don't want to waste that time. I've got kids and other stuff I need to focus on. This is not something I want to spend a day doing."

**Kris Brandon:** Yeah.

**Ian Lop shire:** Yeah, it took me a full week when we all upgraded to M1 Max, just to get everything running. It was a nightmare.

**Break:** \[39:36\]

**Jon Calhoun:** I still don't have an M1 Mac. When you were talking about upgrading, that was the one that almost got me, and then I thought about it, and I'm like "The few things that this would speed up aren't things that I can't just do overnight, like video processing, or something. I can just do it overnight and come back the next day, and it really doesn't make a difference."

**Mat Ryder:** Yeah.

**Ian Lop shire:** I think Go compiles a little bit faster, I don't know...

**Kris Brandon:** \[41:45\] I mean, I don't care about any of the compiling or anything. The thing I like about the M1 and the M2 Max is that they have instant awake. So you just open it and it's just on. What I hated about Intel MacBooks is that you hadn't turned it on in a couple of days, like over the weekend, and you open it, and then it just takes like 10 minutes before it's like "Okay, I'm gonna work now." And the fans come on, and they're blowing all this heat out, and it's killing your battery... It's just an unpleasant experience. But with the Apple Silicon, you just kind of open the thing, and it's like "Oh, hello. You can use me now." I feel like that's a huge productivity boost.

**Mat Ryder:** Yes, I agree.

**Jon Calhoun:** I'd love to actually track that.

**Kris Brandon:** It's real.

**Jon Calhoun:** To log how much time you gain through the year. I mean, it's possible you could.

**Mat Ryder:** No, I mean, literally, like opening apps... I mean, you still fall foul to standard -- like, an app will sometimes just give you the beach ball of death, and then you're spinning for a while... You're not immune from that. But in general, when stuff is working... Opening the Mail app opens at the same speed as if it was already open, but the window was hidden, and you're just bringing the window to the front; it's that quick. And I don't know, that's worth something. Just that -- I don't know, it just feels fast. I mean, it is fast.

**Kris Brandon:** It would have been more useful while I still worked in an office, but also the display engine being so much better, where you can just plug your computer into a dock, and then the displays just work, and there's not that flickering nonsense that happens, where it's just trying to figure out how to actually display on all these different screens...

**Mat Ryder:** Yeah.

**Kris Brandon:** I wasted so much -- especially when it would just break, and I'd have to like to restart my whole computer... I wasted so many hours of my life trying to dock or undock my MacBook. And that's just kind of like not a thing anymore.

**Mat Ryder:** Yeah.

**Kris Brandon:** But if you never have to undock your Mac, that doesn't really matter; it's not going to be an advantage to you.

**Jon Calhoun:** I also don't think I've ever heard the fans on this thing. I used to spin up Docker, and it would jet engine for a good ten minutes. And now nothing.

**Mat Ryder:** Yeah. And the battery life. That's the thing; it's not just that it does things faster, even if you can't notice it's quicker. You will notice that -- I did video editing one day, I was doing video editing, and like multiple renders, I was doing like docs stuff, email, Slack... Slack, and it still had like 70% battery at the end of the day.

**Jon Calhoun:** So I can run four Electron apps now.

**Mat Ryder:** \[laughs\]

**Kris Brandon:** And seven Chrome tabs. It would be great.

**Jon Calhoun:** Starting to feel like this is an intervention like Jon you cannot keep using that Intel Mac. It's not okay.

**Kris Brandon:** I mean, if you're doing like video and audio editing... I remember watching the reviews, and it was like "Oh yeah, we did this compile. It was faster, which was cool, but it used 3% battery on the MacBook on the M1, and it used like 80% or 90% battery on the Intel." So it's like "Okay, well that's different."

So I think like those are the things too, where it's like I can actually continue using my computer while it's doing other things, or still have battery life after I do this long compile, or this long render, or whatever export.

Also, if you're using Pro Res, the M1 Max and M1 Pro are just kind of like - you just hit Play, you don't have to render. If I was still doing video editing, that would be so beautiful.

**Mat Ryder:** Yeah, same for Logic Pro. I use that music editing software, and that used to be -- well, I also have this ridiculous machine that's... I shouldn't have really done it, because I spend the most time in email... But it's just unlimited as far as like -- I don't have time to record that many tracks when making a song... So it's like, it's beat me now; I don't need that much. I can render songs, and be rendering a video at the same time... Like, you can just really push it and it does kind of a cracking job.

**Kris Brandon:** And you can run ten Docker containers.

**Mat Ryder:** Yeah, can run Docker, and a Slack, and a couple of tabs...

**Jon Calhoun:** That's just far too many Docker containers...

**Kris Brandon:** I mean, if you're Kubernetes on top of Docker, you could get a--

**Jon Calhoun:** Alright, we can move away from Apple. I hope they're sending sponsorship money at this point.

**Mat Ryder:** Yeah. They should at least sell Ian that iPhone for $1, after all this talk... Does anyone want to, just for balance, say something horrible about Apple? Chris, you live in a litigious country...

**Kris Brandon:** \[46:10\] I'm not mad at Apple right now. I don't have anything bad to say about them.

**Jon Calhoun:** You can just be like "That darn 30%", then move on.

**Ian Lop shire:** That mouse you have to flip upside down to charge, or that pencil that you lollipop with an iPad...

**Kris Brandon:** I mean, they do have some stupid designs... I think when it comes to that 30% thing, I'm madder at the industry and people that I am at Apple, and I feel like that's a hot take. Maybe that's an unpopular opinion. But when the iPhone first came out, and Steve Jobs was like "We're gonna use html5 for everything", and everybody was like "No, go f yourself. You're going to build us an app store, and then give us native apps", and then they did, and then 10 years later, everybody's like "Hey, why are you charging so much money for this thing that we forced you to build and put a lot of money into? That's not fair. We want something that's open." And it's just like "You could have had it, if you had just all worked together and tried... But you didn't want to. So you can now like sleep in the bed that you made. Thank you."

**Mat Ryder:** Yeah, you tell them. People don't like that take.

**Jon Calhoun:** I mean, in their defence, a lot of the people complaining now probably weren't involved in the original decisions.

**Kris Brandon:** Yeah, but that's not how -- you've got to pay for the mistakes of the past. That's what we've all got to do. That's just life.

**Jon Calhoun:** Just those guys who are about to retire, they're like "No, no, no... You go ahead and build something. I'll let some other sucker deal with it."

**Kris Brandon:** Yeah. I mean, that's how like generational wealth works. If it works for wealth, it should work for the bad things, too. It can't only be the good." That'd be like saying, "Okay, well, we can't borrow any code from the past, because the people in the past wrote it." Like, if we get to inherit their code, we also get to inherit the other decisions that they made.

**Mat Ryder:** Yeah.

**Kris Brandon:** And some of those decisions were bad ones, like not using html5 to build apps. Because we got there, right? If you look at browser API's now, they can do like most of the things that you want to do in a native app; they're still kind of not as advanced as we'd like, but they're getting there. You can do like Bluetooth integration, you can do file storage, you can do a lot of stuff. So it's possible to get there, but everybody was just like "No, we want what we like."

**Ian Lop shire:** And then we get Electron apps, and...

**Jon Calhoun:** I think what I like best about that is there's literally mobile apps that can do everything perfectly. Reddit is an example. But they'll pop up a big thing, and it's like "Would you like to go to the app though?" And you're like "No, just let me see this Reddit page in my browser."

**Kris Brandon:** Yeah. When they invented deep links, I was like "Okay, this has gone too far. You're just reinventing browsers... What are you doing?"

**Mat Ryder:** Yeah, that reminds me, Kris, what you're saying... In the UK, we have the Royal Mint, and we have the national debt. And this is a very kind of interesting example of "You can't have the good and not the bad." The Royals, cheeky. We've got a new king though; I don't want to say anything wrong, because I think legally he can just cut my head off, if he wants to. So that's still an old law that applies. So fingers crossed that doesn't happen.

**Jon Calhoun:** He's got to make an example of somebody.

**Kris Brandon:** Yeah, this is why we got rid of monarchs. Now we just have whatever we have in this country.

**Jon Calhoun:** Kris is like "Look at how much better it's been over the last eight years."

**Mat Ryder:** Yeah, but at least you chose your lunatic...

**Jon Calhoun:** I had to go back far enough.

**Mat Ryder:** At least you chose your lunatic.

**Kris Brandon:** I mean, comparatively, the UK is not the shining example to pick as the -- the much better than the US. They've had a little bit of trouble there, just like we have.

**Mat Ryder:** Yeah. A little bit...

**Kris Brandon:** Canada seems to be doing alright, right? Like, they don't --

**Mat Ryder:** Yeah, what's going on there?

**Jon Calhoun:** Doesn't Canada have some sort of relationship with the Queen though?

**Mat Ryder:** Yeah.

**Kris Brandon:** I mean, they're still like a Commonwealth country, so yeah, they still have a monarch... So now they technically have a king...

**Mat Ryder:** Yeah. I don't know if he's allowed to cut their heads off, but you know, fingers crossed, just for the equality of it. I don't wish any ill of Canadians, but if he can slice my head off with no trouble, I sure as heck hope he can also slice your heads off I don't care how polite you are.

**Kris Brandon:** Yeah... I don't know if a king can actually slice your head off.

**Mat Ryder:** Well, this is it; you don't want to find out, do you?

**Kris Brandon:** I mean, that could be the thing in the US, because we have presidents that said they could shoot people on Fifth Ave, and they wouldn't get arrested.

**Mat Ryder:** Yeah. Well, there we go.

**Kris Brandon:** Have we talked about Go at all in this episode? I feel like--

**Mat Ryder:** Oh yeah, I forgot about that.

**Kris Brandon:** This is NGO Time.

**Mat Ryder:** Is there anything in Go that we're looking forward to? This is kind of a New Year's chat...

**Jon Calhoun:** \[50:18\] I mean, when we talked about HTMX it was kind of related, because you can use it with Go... In my mind, there's a

a little bit of a benefit there.

**Mat Ryder:** So you think we've fulfilled our contractual obligation.

**Jon Calhoun:** So we can pretend like we had some Go in there...

**Mat Ryder:** Cool, yeah.

**Kris Brandon:** I know it's not new, but I've been looking at code that uses some generics... Specifically some code around atomics; and I'm like "I don't hate this as much as I thought I would." But I think that's because it's being used properly. I think if it was being used in a mass way, I'd be very upset about it.

**Mat Ryder:** Is this the pointer type? The atomic pointer that's typed with generics?

**Kris Brandon:** I think so... I don't know. Well, I think it's like in part of Tail scale's codebase, where we just have a sync package that has these nice typed atomic values, so you don't have to do typecasting when you get the value. It's just very nice. I'm just like "I like this. This is pleasant."

**Jon Calhoun:** I mean, generics were 2022, so I think it's a good time to look back and... They released in 2022, right? Am I losing it?

**Mat Ryder:** Good question. We should check that. I'm sure the internet will tell us.

**Kris Brandon:** It was 1.18, right?

**Jon Calhoun:** That has to have been this last year.

**Kris Brandon:** Beginning of 2022?

**Mat Ryder:** Really? Yeah. Wow, okay... And I think there's only one example in the standard library of generics being used, and it is that generic pointer in the atomic package. So you can say the atomic package lets you protect things concurrently, so you can kind of update, you can do operations and guarantee that only one go routine is going to change that memory at a time. So you can have that sort of safety there.

And then the pointer thing lets you basically point to any object, and you specify the type, and then you've just got the sort of type safety; you can't then put the wrong type of thing in that pointer that would be otherwise possible to do. So I think that's it. It's nice to see those cases where it's used well, and sort of surface them, and I feel like that's something we could do in this new year; we could do an episode on looking back at generics. Where have we seen it used, where have we not seen it used very well, and see what lessons there are?

**Ian Lop shire:** There are a couple of proposals in right now that I'm also excited about. I don't know if it's actually a proposal or just like a discussion about the built-in iterators... I don't know if you've all read that.

**Mat Ryder:** Yeah. Do you wanna just describe it briefly?

**Ian Lop shire:** It's been a while. Basically, they're talking about adding - so we can use the range operator kind of natively for custom iterators. I think it also changes the loop dynamic, so that the variables are redeclared every time inside the loop. So you know that var, where you have to say like i=i, or define the variable again. That'll go away... Which I know is one of the big things that causes issues... So that's exciting as well.

**Mat Ryder:** Yeah.

**Ian Lop shire:** I don't know, can someone else explain the iterator thing better?

**Jon Calhoun:** I haven't read the like post, but based on what you're saying, that sounds like what I would expect when you say there's like an iterator proposal. It's just something so you can make your own type, and you can do like a for thing in range, or arrange loop, essentially, over it.

**Ian Lop shire:** Yeah, exactly. And they're defining kind of two types. Like a push and a pull iterator. I couldn't tell you the fine details, but it covers all the use cases in the standard library right now, which I think is pretty cool.

**Mat Ryder:** \[53:30\] Well, we'll try and dig that out and put a link in the show notes for anyone interested in the iterators. One of the things I like about the way that it works today is there's nothing magic going on when you arrange over something; because you can only arrange over those native types, those built-in types, so you know what's happening. Whereas as soon as you have your own iterator, you could be doing expensive operations in there, and that would be hidden. For example, if you're iterating over some data, and once you reach the end of the page, or as you're approaching the end of the page, it fires off another request to get the next page - how is that surfaced, and how do you handle failures in that code? I think that's one of the challenges that people will have. There must be some kind of error handling in this API, I guess.

**Ian Lop shire:** Yeah, I think the function can return an error... Which is interesting. I agree that it's a little bit weird that it's using the range operator to do things like that... But I think it outweighs -- like, there's so many different ways things do iteration now, and I think it's unclear all the times how it works. I think there's a swath of errors or programming mistakes that we can just eliminate.

**Mat Ryder:** Yeah.

**Jon Calhoun:** I would imagine part of this stems from the fact that most other languages have a way to say for, thing, like treatable thing... And like because of that, when they come to Go from another language, it's not like -- historically, when I first started programming, I swear that type of syntax wasn't common. A for loop with an i=0, it;length, and i++ was like the way you iterated over stuff. And then as more languages have introduced this, I feel like it's kind of tricky in the sense that people switching from another language just aren't used to that syntax... So what is clear and readable to me might not be clear and readable to somebody who learned to program in like the last couple of years.

**Mat Ryder:** Yeah, you're right; the higher-level languages have let you do this for a while. And again, when it's used properly, it's kind of perfect. The cases we do have to watch out for is where it gets abused, or where we ended up hiding things that are happening. But I think as long as we're careful, then yeah, I'm all for it.

**Jon Calhoun:** Going back to Go stuff, I think one of the things this year that kind of excited to me was I think it was the first year that Go Modules didn't basically lead to a big issue of some sort, or confused me at some point... Which - I feel like Go Modules came out a long time ago, but I feel like there's always been little things here and there, or like the Go tooling has changed gradually over time... And this, for whatever reason, felt like the first year we're like, it just worked smoothly most of the year.

**Ian Lop shire:** I 100%. Agree with that. This is the year we upgraded, and after one attempt, that failed miserably.

**Kris Brandon:** Yeah, I feel like this is why I wanted to Go Modules to be in 2019. Just, the tooling is there... I think that's the thing that happens; like, all the tooling has come together finally. The language server is robust enough now that it can handle most of the things that it needs to handle, we've figured out all the kinks... I hope this does become like a lesson for not just like the Go community, but other communities, so making sure that you're tooling and everything is there, and you haven't like just baked the idea and put it out there...

Yeah, I'm excited that modules finally just feels like a boring technology. It's just kind of like "It's there. You use it. It works. You don't have problems. Yay!"

**Mat Ryder:** Nice. Well, on that high note, I think it's time to end this lovely fireside New Year's special episode of Go Time. Thank you so much. I really enjoyed that. It was nice to hang out. I hope you have and had nice holidays, and got to have a nice break there... Pleasure to chat. Ian, Jon, Kris, until next time. Thank you. Goodbye. You can say goodbye, and then I'll play the music if you like...

**Ian Lop shire:** Bye!

**Jon Calhoun:** Bye, everybody.

**Mat Ryder:** Bye!
