**Chris Anderson:** *Yo, other NoSQL, your tech is a wreck like an oil spill. You call that web scale? More like toy scale. Your Emma file is a database fail, and your user's going to set sail for the one they can trust. Because if you're serious, then you must be running Couch base*.

**Jerold Santo:** Wow...

**Adam Staravia:** Wow.

**Chris Anderson:** That turned out to be true.

**Jerold Santo:** It turned out to be true. \[laughs\] It's nice when you put together a wrap, and it turns out to be true as well. It's like a bonus.

**Adam Staravia:** Right?! Yeah, I feel like it's been literally 15 years though, since that moment. Almost 15 years, right?

**Chris Anderson:** 15 years of focusing on the same thing in a lot of ways... And what we're doing with Vibes is an outgrowth of that.

**Jerold Santo:** What is that focus, if you could just put a name on it? What are you focusing on?

**Chris Anderson:** Programming is way too hard. It shouldn't be a thing -- like, if you're me, code is never the hard part. And I want it to be that way for everybody.

**Jerold Santo:** And how were you doing that 15 years ago with Couch DB and Couch base?

**Chris Anderson:** Well, my role over there was the Couch App side of the project, which was to make Couch DB into this serverless application runtime you could just drop some JavaScript into and go.

**Jerold Santo:** Did you get that done?

**Chris Anderson:** It was - it kind of still is - responsible for a lot of people who otherwise wouldn't have had infrastructure to support them being able to do things like rural healthcare, or fun apps for their club. A lot of the same things that we're seeing people do with Vibes DIY.

**Jerold Santo:** So for our listener catching up, Chris was first on the show episode 54, back in 2011. Couch DB, which I assume is still extant... You'll have to forgive me, Chris; I'm not out there using it, but... It was a massively popular open source database, businesses formed around it... Damien Katz was the original creator, or was it a group of people? I mean, there's a lot of people on the Wikipedia page, but help us understand the culture there.

**Chris Anderson:** Damian's the guy who Couch DB came to in a dream, essentially. He had been working at Lotus Notes and getting frustrated with the fact that it had to pause the world to do its synchronization... So he invented the data structure that allows the streaming synchronization with fairness.

**Jerold Santo:** And how'd you get involved?

**Chris Anderson:** I started using it to spider the web. This was like early, early on, and I had to teach myself Erlang essentially so I could drop a debug log function in there for myself. Next thing I know, I'm through the whole stack, and never looked back.

**Jerold Santo:** Nice. So what'd you do, reach out to Damian say "Hey, I'd love to help out", or "Let's start a business", how'd that whole thing come together?

**Chris Anderson:** All good things start on IRC.

**Jerold Santo:** \[laughs\] That's a great answer.

**Chris Anderson:** We were hanging out on IRC... I think it was \[unintelligible 00:06:12.00\] who came out to Portland for OSCAN, like we were talking about... We were already buddies from online. And then after that, Damian invited the Brain Trust out to his place in Asheville, North Carolina, where I said "Hey, let's start a company." So my role in that, besides not being scared of the code, was not being scared of the lawyers.

**Jerold Santo:** Tell the story of that company from there. Tell the story. As long or as short as you want it to be.

**Chris Anderson:** So there's a lot that went on, but the thing that really sticks with me is the fact that we kind of accidentally incubated Node.js. We had people like Isaac Schluter and Ryan Dahl hanging around the office, mostly because of Micheal Rogers, rest in peace... And it was that crowd that was just informally writing NPM at the desk next to me... So really fun to be in the presence of greatness for so long, and to be able to incubate things like Pouch DB etc, kind of taking JavaScript to the next level.

**Jerold Santo:** My first exposure to Couch DB was via - now we're name-dropping - a Geoffrey Gooseneck Peep Code on Couch DB. And he made it look so cool. I was just a fledgling Ruby on Rails developer, of course, dipping my toes into the JavaScript ecosystem, and kind of exploring databases at the time, and like wondering... Because Rails made it so easy to kind of switch your database adapter, but nobody's really doing that... But I was interested in the different databases, and Couch DB was so radically different from what I'd been using. And yeah, Geoffrey's voice, which is epic to this day...

**Chris Anderson:** Legend.

**Jerold Santo:** Yeah, a legend. It made Couch DB look like this is where the cool people are coding... And it turns out it was true; I mean, from your story, it's like - yeah, a lot of very talented people are involved in the project.

**Chris Anderson:** \[08:10\] You have to remember 2008-2009, that was the very beginning of the API revolution. The idea that you could put your database behind a REST API. Almost nothing was even JSON yet. So we were all frustrated with XML, we were all writing kind of monolithic servers... And by the time that project kind of matured, even as early as 2011, at least the early adopters were already doing microservices. So really, that was a big sea change right then.

**Jerold Santo:** Mm-hm. Was it good business, too? I mean, you started a business around it. Was the business good? Was it hard? How'd that go?

**Chris Anderson:** It was good and hard, and in some ways, we brought like a cultural cachet that allowed us to, as we discussed on episode 54, merge with Membrane, who had a bunch of really smart people who understood the market and how to drive a startup to success.

So Steve and me, who I learned revenue from over there, is now on the board of Vibes DIY, and helping me do the right things here. It took a while, but they IPO'ed. They IPO'ed about five years after I left...

**Jerold Santo:** Nice.

**Chris Anderson:** ...and I'm always watching it real close.

**Jerold Santo:** So what's your journey from leaving there to Vibes, Vibes. DIY, which is your current thing?

**Chris Anderson:** Well, I bounced around a little bit, checking out other database technologies, worked on Fauna DB, which I still maintain; it has some of the strongest integrity that you can get. Then I went to McKinsey and Company... Kind of a fun story there. Like, you wouldn't think that -- my whole family was like "Really?" But Jason Smith is another legend. He's till there, but he brought me in, and his claim to fame is - well, for Couch, he hosted NPM. So NPM used to have a one-man host, and it was him. And yes. So... Great to have him show me what the real world is like. And what I learned about the real world is you don't get infrastructure, right? Us here in the Silicon Valley culture, where we can boot a virtual machine, or request an S3 bucket and get it - like, that's just an unbelievable luxury. What I learned from this constrained environment of "The client doesn't know what cloud you're going to use until it's too late" is I need to build a database technology that can run anywhere to allow permissionless innovation. So that's the gem of what became Vibes DIY.

I built a deep tech thing, along with Micheal Rogers' team at Protocol Labs, who did a bunch of research on immutable data structures with content addressing. I joined that team for a little while, and saw the potential of it, and built an embedded database that runs in the browser, with end-to-end encryption for multi-user synchronization. And that's what powers Vibes DIY. The database is called Fireproof. Basically, everything I'll talk about today is open source, but if you want to get into Fireproof, there's plenty about it. The thing that it does uniquely is give every operation cryptographic data provenance. It's almost like a mini blockchain in the browser, super-lightweight; no network dependency, just runs right there... But it means that when you do a replication, you know what you've got. There's no questions about what kind of data you're sitting on.

**Jerold Santo:** Let's dive into that. When you say cryptographic data provenance, what do you mean exactly?

**Chris Anderson:** So it goes back to Rich Hickey Clojure and the immutable data structures that they were pioneering around the same time we were doing Couch. And what you see in those data structures - as soon as you have an invariant that you're working with immutable backing storage, you have to do everything different, everything new. With Fireproof and the iPod data structures that it uses, that constraint is enforced because the only pointers you're allowed to use are hashes of content. And so everything is addressed by its own hash.

\[12:27\] That means you can only talk about stuff that's already been written. And that means that every time you're doing these B-tree like updates, you're either going to churn data in a real heavy way, with lots of kinds of write amplification that's unnecessary, or you're going to solve these hard, hard problems that the research team over there, people like Alan Shaw and \[unintelligible 00:12:51.17\] worked on, where you have trees that have fascinating properties... So what you need, which is a lot of work to get, is something that is a search tree, like a B-tree, but regardless of if you put all those records in, in one order, or a random order, you still get the same root hash at the end, so your snapshots have stable identifiers. And that means your replication doesn't have to be mechanically the same everywhere. It means you can replicate essentially in an optimized, efficient way, but still end up at the same endpoint.

**Jerold Santo:** So... Fireproof? Firestone? What's it called?

**Chris Anderson:** Fireproof.

**Jerold Santo:** Fireproof - is this your implementation of these concepts, or...?

**Chris Anderson:** It's my essentially making it so easy to use. We talk about technology, especially databases, and one of the phrases people like to say is "a foot gun", right? A foot gun is when if you don't do everything exactly right, it blows up on you.

And the requirement I had for this technology is no foot guns. It's literally designed for the code school dropout.

**Jerold Santo:** Okay. So you can't actually shoot yourself in the foot.

**Chris Anderson:** Right. And that turned out to be the right place to be, because --

**Jerold Santo:** Because we've got a lot of people vibe coding.

**Chris Anderson:** Well, even more than that, I'd say with LLMs and GPTs and all that, we have an infinite supply of code school dropouts.

**Jerold Santo:** Oh, true. Yeah, exactly. They are infinitely supplied... Depending on how much money you have, right? There's another one there; assuming you can afford those tokens. So you're working on Fireproof, you're building this, making it simple for people to build things with it. And then where does Vibes DIY come into the story then?

**Chris Anderson:** So we were going to market with Fireproof after the technology got mature, and there's use cases like black box recorder for self-driving car. Things that are very serious, that are served well by this content-addressed immutable data structure. But there's not very many people who need that, and they don't care how easy it is. That's a different set of problems for them.

When we started to see in our Discord people coming in and saying "I haven't programmed in 15 years, but I built this drum machine along with ChatGPT and your API, and it worked right out of the box", we realized we've got vibe coders.

And so I brought in an old friend of mine, this guy Marcus Estes, who I've known for like 20 years, and he's just a hustler. He makes it happen. He understands where the opportunity is and how to go after it. I've been looking at this vibe coding stuff, thinking "That's fun. That's cute." He realized "No, let's just do this", and we didn't look back. So it's been so much fun.

The big difference, the real difference that matters is my kids, who were so sick of hearing me talk about Merkel CRDTs and all this stuff, now they're grabbing my phone out of my hand.

**Jerold Santo:** You're cool again. "Dad's cool again", you know?

**Chris Anderson:** They just want to make apps. They're like "Dad, can I make an app?"

**Jerold Santo:** "Dad, can I make another Merkel tree?" You know, no one ever says that.

**Chris Anderson:** \[laughs\] Right...?

**Jerold Santo:** \[16:12\] What kind of apps are being built with this thing, or can be?

**Chris Anderson:** Well, I was really inspired -- I was trying to see essentially what's the lowest common denominator that we can address... And the answer to that is I was using ChatGPT Canvas and Claude artifacts and thinking about how for like a Norrie, somebody who doesn't already know their way around the Next.js stack, or deeply understand React and all the tool chain there, those are the best kind of interface and set of metaphors. If you look at those closely, they don't even say Deploy. They say Publish. And so that's the take we've done with Vibes DIY, is when I'm designing a feature, if it's going to require introducing a new concept, don't. Just make it simpler.

And we had this tremendous validation... We just got back from Render ATL. It's a tech conference in Atlanta, where we had a deep line at the booth, crowded up with people who had kind of maybe never even heard of vibe coding, or if they had, they hadn't tried it yet... Or if they had tried it, they thought the existing tools were too complicated... And when we said "Hey, if you make an app, we'll install it on this sticker for you", they would spend the 90 seconds it takes to make an app.

**Adam Staravia:** Wow... What's on the sticker? Is it like a QR code, or an installation kind of thing, or launch it?

**Chris Anderson:** The way we install it in here is with the near field communications chip.

**Adam Staravia:** Okay...

**Chris Anderson:** I actually learned about that at like a Burning Man event, where someone was doing manicures with NFC chips in them.

**Jerold Santo:** Really?

**Chris Anderson:** Yeah, which is super-hot. Like, "Here's my number."

**Jerold Santo:** Right. You can just embed a little bit of information on that chip and then carry it around in your fingernail.

**Chris Anderson:** Yeah.

**Jerold Santo:** That sounds very Burning Man.

**Chris Anderson:** Yeah. You learn a lot. You never know where you're going to learn a lot.

**Jerold Santo:** "Here's your next big idea."

**Chris Anderson:** Right?

**Jerold Santo:** Wow. So if I take the sticker home, how can I use it? Like, I've got this information embedded in it... What do I do?

**Chris Anderson:** You just kind of get it close enough to your phone, and you get one of these little -- and now you can open the URL.

**Jerold Santo:** Okay. So it's similar to a QR code, except for not for the camera, but actually the NFC chip in the phone. Makes sense. That's interesting.

**Chris Anderson:** Right. And for us, it's really this ownership metaphor. Like, code is all in there, over there... Especially if you're not a coder. Like "What am I making? Where is it?" But if I put it in your hand when you walk away from the booth, then you're going to come back with your friend the next day.

**Adam Staravia:** Does that give them access to the code they just created, or vibed? Or does that just give them access to the application they just vibed?

**Chris Anderson:** Well, for us, really our --

**Adam Staravia:** How do they continue development, how do they keep going?

**Chris Anderson:** You're totally right. So most of these people made it on their phone they walked up to the booth with, because it's a mobile-first experience. But if you didn't, if you made it on my phone, or if you made it on the booth laptop, then you still get the sticker, you can still scan it into your phone... And anyone who goes to a vibe can hit the Remix button in the corner and get into the code, or get into the chat and say -- the default remix we have preloaded in our form is "Make it pink." But really, just whatever you want to do to change it.

There's a great story, and we had a lot of fun... I was walking back from lunch in Atlanta, and I said to my phone, I said "I want to take pictures and have you turn all the faces in the pictures into Georgia peaches." And it worked on the first try; sometimes you get lucky... And people thought that was hilarious. So we were showing it off, and then we were sharing a booth with Netlify. They're great friends of ours... And one of the Netlify leaders, Sean, brought his kid. And so she saw what we were doing, and she said "I want to be a cat." \[laughs\]

**Jerold Santo:** \[20:23\] Remix it. Remix that sucker.

**Chris Anderson:** So basically, a four-year-old turned a peach app into the cat app, and that was a hit... And then we saw what was going on there, and we made this -- we made a caricature app I've got on my laptop here. Here's me as a podcaster.

**Jerold Santo:** Nice...

**Chris Anderson:** And it was also a big hit. People at the conference just all day long building stuff.

**Jerold Santo:** It's just fun. This is the stuff I'm talking about, Adam. Just --

**Adam Staravia:** Total vibes, man. This is the internet, man.

**Jerold Santo:** For joy. It's for the joy of it.

**Chris Anderson:** It totally is for the joy.

**Adam Staravia:** It is.

**Chris Anderson:** And so many people --

**Jerold Santo:** This is like Geocities for the modern era.

**Jerold Santo:** Seriously.

**Chris Anderson:** Yeah. It's like a writeable Geocities, right? View sources back, baby.

**Jerold Santo:** \[laughs\] Yeah. I'm reminded of the old cloud to butt extension. You guys remember that one? Every time the word cloud was on a website, this Chrome extension would replace it with the word butt. I'm not saying this is an idea for a remix, Chris, I'm just saying I'm reminded of it.

**Chris Anderson:** You know if I wouldn't get distracted, we'd just build it right now. \[laughter\]

**Break**: \[21:26\]

**Jerold Santo:** So is the platform the web then? Or how are they -- how are these things running?

**Chris Anderson:** That's the way I think about it. I wanted to build the experience I had early on in the black and white Mac days, with HyperCard... But I realized that when I look around people trying to build similar ambitions, often there's a "do it our way completely or don't" kind of feel. I call that like "They make you wear the socks." With us, the point is there's already so much platform that's done. So we just build React apps, and we're essentially taking the web runtime, which is what a browser can do, and making it as easy to express yourself there, maybe easier than making a TikTok. So if making an app is easier than making a TikTok, now what? And that's the question Vibes DIY is out to answer.

**Jerold Santo:** I love it. I think Adam and I were just talking about this new possibility, specifically in light of Apple allowing local models on phones, and Xcode, and things are getting localized there, where it's like you could build and deploy your own iPhone app. It's just a one-off, just for you; nobody else even has to have it. And there are still platform limitations there with regard to distribution, side loading, and there's lots of stuff. But with the web, it's like "Nah. Just URL, publish that sucker." And that's really awesome.

**Chris Anderson:** Yup.

**Jerold Santo:** So just to nerd out again on the sticker, is the embedded information in the sticker just a URL to where the thing actually runs? Or is there code in there? Or how does that work?

**Chris Anderson:** It's just the URL.

**Jerold Santo:** Yeah, that's what I thought.

**Jerold Santo:** So once you have the URL, we make -- actually, our service layer is so simple. If you look at a lot of the existing vibe coding tools, they're built for professionals, and they're going to mimic a professional output with a full Next.js app. The only thing that the model - which is just a commodity model; we have a switcher. It's actually a great way for AI-interested devs to try out all the different models and get their personalities down. But when you ask Vibes to make something for you, it's only writing app.jsx, and that's it. So our focus is on being fun, done, and alive with AI.

\[26:07\] This last bit means that the apps that you make, get the same API key that we use in your browser to write the code. And you press the Demo data button, and it fills out your to-do list with whatever is plausible. Or it makes an app -- I built this because it takes 90 seconds to make an app, it takes longer to figure out how to use an app. So instead, I just mashed the demo data button, and it shows me what the app would look like if you'd spent some time in it.

**Jerold Santo:** So let's say I mash out a 90-second thing, and it's rad, and we're having fun... Can I then expand/extend/build that sucker out, or I have to remix and start something else?

**Chris Anderson:** That's where one of our core values comes in, is that it has to be real. So the 500 lines of JSX that it's going to write is React code -- it's as good as Claude 4 is going to make it, which means it's not that bad. And the standard library we bring to the table with it means that all these apps are fully functional just in the browser, but then they can be remotely synced via the cloud to other users for collaboration. And that means copy that -- there's a Copy button; you get your 500 lines of code in your clipboard, and you go drop it into anywhere. Maybe into a \[unintelligible 00:27:21.00\] template, or maybe into another vibe coding tool, and say "Hey, expand this." Maybe you turn it into 10 pages, maybe you take 10 vibes and put them into one app... But the sky's the limit. It's really fully malleable software that pros can take and run with, as well as beginners can just use.

**Jerold Santo:** Adam, what do you think of all these sayings he has? He's got like rhyming words, he's got like stickers...

**Adam Staravia:** He's a poet, man.

**Jerold Santo:** This guy's bringing it.

**Adam Staravia:** I'm over here, trying to vibe over here... I think it might be a Safari issue.

**Jerold Santo:** \[laughs\] I thought you might be. That's why I pulled you back in. I can tell when Adam's like testing something out...

**Adam Staravia:** I was vibing over here, and I think I might have hit an issue with Safari, potentially... Because the thing it made me is on a black screen, and so I'm having an issue.

**Chris Anderson:** Well, that's not Safari, that's Claude. I would say you rolled the dice, and...

**Jerold Santo:** You got snake eyes.

**Adam Staravia:** Oh, dang. So it made nothing.

**Chris Anderson:** One in 20 times Claude is like "Oh, I know what you want... You want a black canvas that's like 20 times bigger than your screen." It just does that -- we have work to do, but...

**Adam Staravia:** Yeah, I think that's about it. It's kind of like forever scrolling.

**Jerold Santo:** Well, close the tab, and open a new tab and try again, you know?

**Adam Staravia:** I can share with you my -- it was just intense, man. This is an intense process. I saw it write a bunch of code, I could see all the code, but there's no application to be viewed.

**Chris Anderson:** So basically copy that prompt you did and just make a new one. That's what we learned from vibe coding. Don't go iterate on something unless you're already stoked about it.

**Jerold Santo:** Right.

**Adam Staravia:** Yeah.

**Jerold Santo:** It's just cheaper to throw it all away and start fresh, right?

**Adam Staravia:** Yeah, right? I mean, when it's just spoken word, it's like "Let's try again and just tweak a little bit", you know? That's kind of cool, though.

**Jerold Santo:** That's kind of what I do. Remember with Google searches -- remember when you used to google things? Some people will put in a search, and then they'll read the results, and if there's not the right answer, they'll go to like page two, page three, page four... You know, like an infidel. I just research, right? Like "Oh, my search wasn't good enough." I just research... Now I have the same thing with these LLMs. I just copy a prompt into like four of them, and I'm like "Let's see who's got the best answer", or the fastest, or whatever. Or I can like mentally gunge them into one answer and like pull things from each one... And that's kind of the new research, is this like "Nah, I'm not going to tweak this prompt. I'm just going to try it on more things and see what happens." So yeah, close tab, open new tab, paste prompt and start vibing again.

**Chris Anderson:** Yeah, we're considering seriously doing that for you. We may as well just vibe three of them in parallel and let you pick the best... Although every bit of complexity we add is going to take the simplest user and turn them away.

**Jerold Santo:** \[29:57\] And cost. I mean, that's what Sora does, which is Open AI's video tool. You can pick how many different iterations that you want, and it will make two or four or six. And obviously, you have to have the tokens, and stuff... But especially with creative tools, where it's like "I would like to see four different things", it's just like "Yeah, we'll just crank out four", versus you having to say "Try again, try again, try again."

**Chris Anderson:** The fun part is looking at how much better Claude 4 is than even 3.7. Or if I switch it over to Codex Mini, then I'll get like an app that works great, but isn't showboating at all. Like, GPT models make these lean apps, with no extra stuff... And Claude 4 is going to have your backgrounds, transparency with blur, and \[unintelligible 00:30:41.20\] It's fun to see the personality in there.

**Jerold Santo:** I think Claude 4 - and I don't have any personal reason to say this in terms of like we're not making money by promoting Anthropic... But Claude 4 is just I think good enough now that it's sold me on the entire thing... Whereas up until now I've been very skeptical, because of the results have been so bad. I'm not sure if you guys saw Simon Willison's "The last 12 months of LLM progress as outlined by pelicans riding on bicycles." Did you guys see that post?

**Chris Anderson:** Oh, yeah...

**Jerold Santo:** Because he's such a nerd for every new model that comes out that he tells them all to do the exact same thing, which is to write a code that produces an SVG drawing of a pelican riding on a bicycle. And he documents that, of course, because he documents everything. And he's just showed the progress; he was like "Here's this model, here's that model", all the way down through the last year, and how far they've come and which ones do better. He scores them, and stuff like that. But the progress has been amazing. And Claude 4 - I think we're at a point now where it's like above my threshold of sucking, to where it's like "Let's do it." Like, I want to use them now. I'm not sure what happened between 3.7 and 4.0, but something happened.

**Chris Anderson:** That black screen that you ran into, Adam - the other one that I'm just still trying to teach Claude to never do again... For some reason, it loves to give you buttons with white text on white background.

**Jerold Santo:** Dark patterns. The opposite of dark patterns. Light patterns. Did you get better results this time, Adam, or are you still spinnin'?

**Adam Staravia:** It's still working on it. It's a little slow, for some reason. It's taking its time.

**Jerold Santo:** It's bleeding edge.

**Chris Anderson:** How many lines of code does it want to do?

**Adam Staravia:** At this point it's trying again... So I got two black screens in a row, so I wasn't sure...

**Jerold Santo:** What are you trying to build?

**Adam Staravia:** Okay, so I told this thing "I want to golf with friends. Help me create a tee time and invite folks to it." So "Hey, Jerold, I'm going to golf this Saturday, at this time. You're invited to my tee time." And you can join, kind of thing. So that's -- oh, it finally did something. It's got a golf tee time organizer, I can create a new tee time, I can invite people to it, it seems... It looks like more iteration. Furthermore, it's got some additional features that could be added, which I think is kind of cool... But all in all, quite colourful. It's vibrant. It's got a cool vibe. Furthermore, it's vibing. This is vibing, man.

**Jerold Santo:** This is vibing, man.

**Chris Anderson:** Right?

**Jerold Santo:** So do you guys have a system prompter? I'm not sure if you have some sort of scaffolding in there, that when we write our prompts and put it into vibes, it does more than just that, right?

**Chris Anderson:** The whole thing's open source, so you can go on GitHub on the Vibes DIY org and get into the repo prompts.ts and see what we actually do. But it's fairly simple... I mean, as I was mentioning earlier, I was one of the coauthors on the O'Reilly ChatGPT shortcuts book, and what I learned from that - and the experience continues to pan out... If you talk to the LLM like a person, less technical, more just what you want, you get better answers. So this golf thing is the thing you want to do. There's this great YouTube - we can find it for the show notes - there are two types of vibe coders. And there's the one guy who's all frustrated, with his 4,000-line LLMs text and his feature specification, PRD... And the other guy who's just like "Make GTA. Make GTA six." \[laughter\]

**Jerold Santo:** \[34:13\] And he's having a \[unintelligible 00:34:15.27\] you know?

**Chris Anderson:** Here's my golf tracker... \[laughter\]

**Jerold Santo:** Oh, nice. Did you do that one just now, as Adam was doing one, or is that --

**Chris Anderson:** Yeah, after I heard what he was doing... And I think my prompt was just --

**Adam Staravia:** Let's see your prompt. What is it again? Show it to me?

**Chris Anderson:** I said "golf with friends."

**Jerold Santo:** That's all you said?

**Chris Anderson:** Yup.

**Adam Staravia:** Oh, my gosh... Okay, so how do you share that with me, so I can see it, or play with it, or remix and revive?

**Jerold Santo:** Pass the address into the chat. We have a chat here.

**Chris Anderson:** Right?

**Adam Staravia:** That's how it works?

**Chris Anderson:** So again, we don't deploy. You press the purple button, the big button, and now you publish it, and... I was getting into this a minute ago, I guess I distracted myself... So when it publishes, all it does is take, like, let's say the 475 lines of JSX and put it in a Cloudflare KV associated with the subdomain name. When you go hit that subdomain, we have a static HTML that's essentially the runtime, that's got all the packages in there... And it loads any additional packages via esm.sh. And now you have your app right there... It costs us almost nothing to host, almost nothing to serve, unless that app goes and does some AI calls, in which case that goes against your token quota. So it makes it super-easy for people to write apps that are alive with AI, whether that's... Our benchmark, compared to Simon Willison - he's got the penguins on bicycles; what we have is, for instance, I'll just tell you something in English, and you'll give me a structured to-do list that reflects what I need to do to accomplish that. So I'm always running that when we do an upgrade, or move to a new model... This morning I said "Take my kid to summer camp", and it gave me everything: sunscreen, lunch, all that.

**Jerold Santo:** Alright, I just loaded up Adam's golf tee time organizer app.

**Adam Staravia:** Is it working?

**Jerold Santo:** I mean, it rendered... I don't know if it's actually working. I think it has a white button with white text, as Chris knew it would...

**Adam Staravia:** Something's going wrong here, because I can't get it to load for me.

**Jerold Santo:** But I can create a new tee time...

**Adam Staravia:** Oh, sweet.

**Jerold Santo:** Oh, I see some. Sunnyvale Golf & Club. I can join that round.

**Adam Staravia:** Yeah. Pop your name in there. Boom.

**Jerold Santo:** Okay, I'm joining that round... My name is Jerold, thank you very much... And Confirmed. Jordan Phillips is going, and Jerold is going. So... Where is it storing that information, Chris? Where does the data that I enter in go?

**Chris Anderson:** So all of that stuff goes into Fireproof, which has got that Merkel CRDT. And that means that it just goes in your browser local storage. The way Fireproof works are every database operation is a diff, like in Git. It is end-to-end encrypted and then written to - we use IndexedDB in the browser, because it's real fast with Uint8Arrays... But then asynchronously can be replicated via S3 bucket and WebSocket. So that part works in Fireproof. We're rolling it out in Vibes right now. That means today all Vibes are single player. That's why it's best for this kind of viral AI experiences. But tomorrow, all Vibes have essentially the security model of a Google Doc. So I don't want an end user to have to understand Postgres Row Level Security, or having to do like where clauses to keep from writing bugs... Instead, if you're in the app, you're in the app. Maybe you have write access or read access, but it's as simple as a Google Doc for the sharing. And that means as soon as we activate that feature, then Adam, you could invite Jerold to your app via email, and now you all are both in there, setting up what are you going to bring for lunch to the course.

**Adam Staravia:** It's all on the web platform.

**Chris Anderson:** \[37:58\] Yeah, yeah. None of the people who don't know what code is, who've never deployed anything - they can't depend on any setup. I like to say, if you don't know what an API is, then I'm certainly not going to ask you to do an API key.

**Jerold Santo:** So this thing went Render ATL viral last week, because they already had a fun time making caricatures of themselves... But when's it going to go TikTok viral, or youth viral? Like, it seems like this is set up specifically for 13 to 15-year-olds to find out about it. Just like the six, seven things. I'm not sure if you guys are aware of six, seven, but they're huge on six, seven. And all of a sudden it's like, this thing's screaming.

**Chris Anderson:** Well, I'm pretty sure that my key into that market is you guys. \[laughter\] But really, what we aim to be -- there's a lot of people who use more serious tools for vibe coding, and I'm not going to give a senior developer more control, more options, more details than other incumbents. But what I will do is be exactly the right thing that they're going to turn around and show their friends when they want their less technical friends to start getting into writing code.

**Jerold Santo:** Gotcha.

**Chris Anderson:** So if you've got a buddy who has a dream, or keeps bugging you to build something for them, say "Hey, vibe it up, and I'll take it from there."

**Jerold Santo:** Right. Well, it's very much a GeoCities then, in that sense. Or maybe Glitch. Of course, Glitch recently changed the way Glitch works, but... Similar vibes then, right? Glitch was very much the thing where it's like get people started, learn on it.

**Adam Staravia:** How does versioning work in that multiplayer world?

**Chris Anderson:** So if you look inside the chat that you've been having, you can refine it. You could say "Oh, I didn't mean regular golf. I have these interesting rules of golf I want to bring to the game." Claude will go rewrite the code for that, and now you have a slightly different version of the app. That could be within a single chat session, in which case we're not remixing yet. We're just iterating. But if you go look in that chat, you can click on the older versions of the code, and it brings them up instead. Whichever one is on your screen is the one that gets published when you click Publish. So publish an old version if the new one wasn't as good...

But once it's published, and you go to that URL... You know, when you scan the sticker, and you go to the URL, then you're going to have a Remix button in the corner of the screen. And when you hit that, you've essentially forked. Now, no insult to all the people out there who are kind of like me in this regard, but... I've been forking forever, and what we say to ourselves to make sure we stay on target at Vibes DIY is we say "Forks are for dorks."

**Jerold Santo:** \[laughs\] These guys got a saying for everything. So because you don't like forks, or because you do? I mean, it depends on if you think a dork is a good thing or a bad thing.

**Adam Staravia:** That's right.

**Chris Anderson:** Well, when it's time to get the dorks involved and do the forking. But when you just want to try something and remix, then you don't need all that conceptual baggage.

**Jerold Santo:** Gotcha.

**Chris Anderson:** Just hit the Remix button and go.

**Jerold Santo:** So this is akin to the publish button versus the deployment, right? It's like, remix it, don't fork it, because you're not a dork. You're a Norrie, as you said earlier.

**Chris Anderson:** Yeah. Yeah.

**Jerold Santo:** Well, your audience, and it's not us. It's not us... \[laughs\] Because I'm looking for the fork button over here. I'm like "Excuse me, sir... I would like to fork this."

**Chris Anderson:** Totally. Well, it is us though, because when you go deep on something, it's got that Merkel CRDT, it's made out of standard React components, it's got all the TypeScript annotations you could hope for... And it's ready to go big, if that's what you want to do with it.

**Jerold Santo:** But I imagine sitting on Cloudflare, with an HTML file and some KV backends; big in terms of features and commerce and production big, business big, but not big in terms of scale. I imagine one of these could scale pretty easily in terms of that TikTok viral moment, couldn't it?

**Chris Anderson:** It costs pennies on the dollar compared to anything that requires a VM or any kind of complex state or CPU. When I think of Kubernetes containers, all that, I only want one if I basically want to rent some live RAM.

**Jerold Santo:** Right.

**Chris Anderson:** \[42:13\] And you don't need that. All the live RAM lives in the user agent at the edge.

**Jerold Santo:** Right. So Cloudflare is pretty cool... I mean, just - no further comment. I wonder if you could maybe expand on that. Like, you guys are doing cool stuff because of what Cloudflare is helping you to do, right? It seems like a very interesting platform in that way.

**Chris Anderson:** Our stack is, I guess, native to that way of thinking about things... So not just the publishing flow that goes into a KV, but also the fireproof synchronization is powered by Cloudflare workers, which is a great way to rent some RAM on the cheap if all you need is a list of your currently connected clients. So these -- essentially, the flow is that tiny-encrypted diff, you write it locally, push it up via our API, which you don't have to know about, but it ends up as another record in an R2 bucket... And then an update to the pointer that corresponds to your database. So everyone who's listening to that pointer pulls down the latest. And because it's a CRDT, the merges are resilient.

I was thinking about recovery mechanisms. Say like you lost the pointer, and all you had was the files... It's a valid exercise to just load them all and merge them, and you'll get the same result as if you'd started from the end one.

**Adam Staravia:** Why RAM? Why does it need to be in RAM?

**Chris Anderson:** I mean, it doesn't. We can do it with the S3 bucket only.

**Adam Staravia:** It's cool, right? Because it's cool.

**Chris Anderson:** It's a little faster to keep it on \[unintelligible 00:43:43.19\] And what I mean by in RAM is --

**Adam Staravia:** Is it necessary, though? Or is it just because it's cool?

**Chris Anderson:** It's just because it's faster. So we need essentially a directory, a link to -- okay, let's get technical. The real reason we need any of that is because it's multi-writer safe. And so if you just had like a SQLite and you were trying to do this kind of architecture - which people do, where they put the SQLite segments into an S3 bucket, and then they load them in the browser and query them... That's all good until you need to start writing. And now you're doing some kind of bespoke, you know, take the write-ahead log, and put it in there, and manage kind of conflicts against it and everything... It's not for the faint of heart. Instead, what we do, because of this Merkel CRDT, the merges are handled for you.

So the only thing we need to add to the recipe to make it multi-writer safe is it could be that pointer that points to the most recent file, the diff from which you've got to start to reconstruct - well, it can point to more than one file. So if you're under concurrent load, people can all -- you have 50 people all write on top of the same starting state, without having coordinated each other yet... And now we just have a pointer that's 50-wide. The next read pulls those in, merges and writes back up the single pointer. So that's what we do the performance thing for.

**Jerold Santo:** So in your mind or in your heart, is Fireproof the thing, and Vibes DIY is a thing to demonstrate the thing? Or is Vibes DIY the thing that Fireproof let you build?

**Chris Anderson:** I feel like I'm in the Millennium Falcon and I just like mashed the gas, you know?

**Jerold Santo:** \[laughs\]

**Chris Anderson:** So it's a little bit of both, but it's its super-aligned. Fireproof is for the kind of people who like to fork stuff, and Vibes is for the kind of people who --

**Jerold Santo:** And Vibes is for remixers.

**Chris Anderson:** ...don't want to be bothered with all that. It's just done.

**Jerold Santo:** Okay. Do you think you're going to have to pick a certain point, or like focus, or do you have infinite bandwidth to just like mash that Millennial Falcon - what's it called? Warp speed? No, they don't call it warp speed. What do they call it in Star Wars? I'm blanking.

**Chris Anderson:** The hyperdrive?

**Jerold Santo:** Yeah, the hyperdrive. Go to hyper speed.

**Chris Anderson:** So we are focused 100% on Vibes.

**Jerold Santo:** Okay.

**Chris Anderson:** \[46:04\] And in a lot of ways, it's because Fireproof is basically done. I mean, it is never the case with a database, but it's not like it needs new features. It's just about hardening it, and continuing to release it. So in that world now, Vibes gets cool new features. A fun new feature we get to add - this is lightweight stuff. Like I said, I don't want people to have to know what an API is, much less an API key. So... Bake that YouTube API key in there. It's not in there yet, but this allows you to say "Hey, I want to turn my playlist into a YouTube screen", and it just works already. Same thing for Spotify, or any other of this kind of mass market media APIs. There's no reason that you as a Vibe coder should have to know about any of that to use it.

**Adam Staravia:** Have we talked about money yet?

**Jerold Santo:** No.

**Adam Staravia:** How do you make money?

**Jerold Santo:** No.

**Adam Staravia:** Let's talk about that.

**Jerold Santo:** Let's talk about it.

**Adam Staravia:** Does it matter at this point? Or is it just for the vibes?

**Chris Anderson:** It matters that we don't get it wrong... And then the more we think about it, the more excited we get. So if you look at what it would take to build something with a vibe coding tool and a database backend - those are both kind of like maybe just to get started; table stakes, $25 a month, $25 a month - that's $50 a month right there. We do an all-in-one bundle at $5 a month. And that's because all we need is that R2 bucket. It's not costing us a whole Kubernetes container to keep your Postgres instance running. It makes pennies on the dollar for us. And then the real cost becomes those tokens, that either your app consumes when it's generating cool caricature images, or parsing your to-do list, as well as the tokens that you use when you write an app.

$5 a month gets you started. If you want to go over that, there's a meter which is competitively priced. And then where we see this going in the long run is almost like this YouTube-style model, where, say -- first, think about a corporate case.

Think about some big marketing agency that builds like "See our product in your house. Replace the Statue of Liberty with our product", whatever it is. "Take a photo, put us in there." You get 100,000 views on that from your email list... You're probably writing us a check for $20,000 or something on the tokens it consumes. But if you're some kid who figures out a cool way to scan your house and turn it into a video game level, you don't have that kind of money. But your app costs just as much to run, and it goes just as viral. So in that world, there's a little bit of a freemium. Somebody comes along, uses the app - they can generate a simple level or a couple of images. But then they're going to get through their set of free vibes tokens... If they like what they're experiencing, then now they're subscribing for $5 a month. So we're not just selling it to developers, we're selling it to people who want to make cool caricatures of themselves in their dream job, or whatever it is that these end user apps do. So now if you're that kid who made a cool video game, and you don't have any money, but you get us 50,000 signups, then my goal is to write you a check, like YouTube.

**Jerold Santo:** Does that "Turn your house into a video game" level thing exist? Because I want that.

**Chris Anderson:** No, somebody's got to make it. I mean, why wouldn't it exist?

**Jerold Santo:** That's such a good idea.

**Chris Anderson:** Right? Gaussian splat is cheap now, running on the phone.

**Adam Staravia:** How would you do that though? Would you just walk around your house just like taking a video, and uploading it?

**Jerold Santo:** I don't know.

**Chris Anderson:** We like to say that the best we can hope to do -- you know, we're kind of grizzled, old vets of the industry. The best we can do is invent the electric guitar. It's up for the kids to invent rock and roll.

**Jerold Santo:** That's like the best non-answer ever, right? He's like "You guys figure it out."

**Adam Staravia:** Alright...

**Jerold Santo:** Yeah.

**Chris Anderson:** \[49:51\] I mean, we've got roadmap features that expand. So everything I've talked about is really just the browser runtime. It can do a lot. It's underutilized, especially for people who really haven't pushed it to its limits yet. But roadmap features are something we learned from the Couch DB ecosystem. Essentially, Fireproof is the Couch DB model running in the browser. And one of the things that you see a lot of -- the way NPM was powered, all those packages stored in Couch DB, and then when someone uploads a new one or makes a change to some metadata or whatever, there's just an event reactor subscribed to the database feed that can then go do some heavy lift, or send an email, or update some analytics package somewhere.

Same thing, just -- if you wanted to today, you could stand up a Cloudflare worker that subscribes to that golf database. And when somebody puts in a new tee time, you could get a push notification. Our roadmap brings that to the masses by making it, so there's just a backend.js that we also let the model write.

**Adam Staravia:** Yeah. See, I wouldn't have even thought about that, I guess... It'd be helpful I there's a guide. "Here's the next step you can take." They mention different features that can come, but not what you mentioned there, which is like push notifications. That'd be kind of cool.

**Chris Anderson:** Right. And there's no end to that kind of stuff. And we really -- essentially, if I think about the job you're hiring that backend.js to do, it's the stuff that's essentially hiding API secrets. You can't just publish the way that you send your emails, your Postmark key to the world. You can't put it in the browser, but you could put it on the backend, and then the backend's job is just to forward those messages.

**Adam Staravia:** What happens when it's successful? What is a year, two years from now -- like, how does this change things? What is vibes.DIY a year and a half from now?

**Chris Anderson:** Well, now that it's easier to make an app than a TikTok, we picture people swiping right on the good apps, and long-pressing to launch it, and having essentially their phone blow up in their hand when their app gets popular. So the same thing you see with an Instagram, or a TikTok or a YouTube, where it's really about the excitement you get from coding. That's what I saw in Atlanta.

When I was first starting coding, the coolest thing in the world was just to change one line in your HTML and then hit Refresh and there it is. So educating people how that feels, and then letting them share that with their friends... I think what we see is that coding becomes something that is cool.

**Adam Staravia:** How do you deal with the potential of scams, or just like security issues in that unfettered world where it's like "Yeah, check out my vibe app", and it's cool, but like what happens when it's a scam?

**Chris Anderson:** There's thankfully a bunch of prior art. Essentially, for us dev tool builders it's a little bit of alien land, but if you've done social media before, it's that playbook. So we've done some of the basic things already... For instance, there's no way to publish to a fire hose. It's not like just everything's all showing up. We moderate the stuff that goes out on the homepage. That doesn't mean you can't share something. So if you start building honey pots, then now we have a different moderation challenge. It's not new, it's just new to do it with HTML instead of video, or images.

**Adam Staravia:** Yeah. I just wonder... It's one of those things where you don't want to have to deal with it, but you do... And it's early, because trust will be everything to get to the TikTok stage of sharing, and virality, or whatever... It's going to be something you can trust, or has to be. And if you can't trust it, then it's like -- it's a today problem, basically. Like, at launch.

**Chris Anderson:** \[53:49\] Yeah. So if you look at the history of using Mechanical Turk to moderate profile images, and having to do two of three thumbs down, and all that - so much cheaper, so much easier to do that with a model now. Just let Claude tell you whether it's not any good, you know?

**Adam Staravia:** There you go.

**Chris Anderson:** And then on top of that, we aren't going to run into these problems to -- it's sort of blunted. We don't give you the ability to go into the editor and type. It wouldn't be hard for us to, but we figure that that's the point you should copy and paste it somewhere else. And Claude's not going to write something out of the box that's going to be extremely concerning. We just use the Open AI image gen. It makes our job easier. Eventually, we'll want to value-engineer all that stuff, but that comes with scale.

**Adam Staravia:** Solve it with more AI. That's interesting. Right...? All problems get easier with AI...

**Chris Anderson:** Well, AI makes new problems faster, then it makes the other ones easier, but hopefully we've isolated ourselves from that with this one file app JSX thing. And don't underestimate the power of the single-origin policy. The web browser kind of already worked out a lot of this stuff.

**Jerold Santo:** So if this thing takes off - I mean, now's the time to get in there and really be the vibe Diver in chief, right? The people that were early on YouTube, the people that were early to TikTok, they had a much better time... Is there actual virality built into it? Can I build an audience? Can I distribute? Is there a distribution channel? I know you all are just getting started, so the network effects probably aren't there yet, but are the tools to build an audience for my apps in the product?

**Chris Anderson:** So if we're talking 90 seconds from prompt to app, on the cases where it works, probably another 90 seconds to be like "Is this app any good?" and then hit Publish. And now it's on a URL, so we go wherever URLs go. But the built-in features around like a newsfeed, and a For You page, and all that... These are the things I'm super-excited to build.

We're growing the team right now. People who want to do that should probably talk to me about it, but it's definitely... It's a kind of interesting green field, because so much of the design language is already worked out. It's not like we have to decide what an algorithmic feed even is. Furthermore, it's more just about making it for -- basically, we're bringing a new media object to the world.

**Jerold Santo:** Right.

**Chris Anderson:** And the same thing you do with a video, you do with this. And we even have plans -- for instance, the same Jason Smith I mentioned earlier, he used to host NPM. I talked to him about it yesterday, and he said "Hey, I've been working on some video gen stuff. I think you could --" Like, we have this demo data button that fills the app up with data for you... You could also do a video tour button. You just click one button, and it takes your face, lip syncs, puts it on TikTok, "Here's my app."

**Jerold Santo:** Right. That's cool. So what kind of engineers or people are you looking for?

**Chris Anderson:** Really right now if you go use Vibes, you're totally allowed to roast it, because I am a React developer, I guess, but I'm also a CEO... And it's like 75% CEO code right now. So we've got --

**Jerold Santo:** C-level code. \[laughter\] I like that.

**Chris Anderson:** So if you're just like absolutely cracked, and the person hire is -- you know, when somebody is kind of like new enough to a stack where they're like dangerously enthusiastic about getting everything right... If you're senior enough, you're going to see my flubs and be frustrated, but at the right part of your skills curve, you're going to be just like chew up fixing that stuff, and get it into best practices.

**Jerold Santo:** Every level of CEO code is like an opportunity for the right person, you know?

**Chris Anderson:** Yup.

**Adam Staravia:** I just got like WordPress vibes, in a way. Like, positively. When I was looking at this golf friends thing I got built out here, it's like Kubrick. Like K2 was to WordPress. Very -- every app has a certain style, kind of thing to it. I kind of feel like it's a good thing.

**Jerold Santo:** Is there a shared -- is that on purpose, Chris? Is there a shared design aesthetic, or something?

**Chris Anderson:** \[57:59\] Well, we made the choice to differentiate ourselves from everybody else. We're not using Shadow... And that's not because it's not great. We just want to be different. We want to be more lightweight. Furthermore, we want to have a little bit more variance and let Claude or whoever express themselves a little more in there. So the way we prompt the design language is -- actually, my co-founder Marcus I mentioned earlier just did a bunch of research, like art history type research around like, you know, "We don't want synth wave. That's played out" etc.

We've found -- there was a design school in Italy in the eighties that came up with a style they called Memphis. And so we tell it to make Memphis... So we described Memphis a little bit, and it does a pretty good job of that. That's all user editable. So if you go into the settings page right now, you can just type in your own style prompt. You could switch it to synth wave. You can switch it to synth wave and DeepSeek. And then if you run it on DeepSeek now, you probably have to generate the app 10 times before you get a working one, but... \[laughter\]

**Jerold Santo:** Certainly a good playground for testing out these models, and comparing them to each other. Probably better than my copy-paste prompt into like four things is actually making -- probably better than Simon Willison's pelicans on bikes, is like make the same app against all these different models.

**Adam Staravia:** That's cool. I see the style prompt now. It's pretty cool, you can just like swap that out, make it whatever you want. That's so cool.

**Jerold Santo:** It's your own.

**Adam Staravia:** Yeah.

**Chris Anderson:** Right. Or if you really want to go deep, just hit up our GitHub, fork the whole thing - you know who you are - and fix up my React.

**Jerold Santo:** Yeah, I was going to ask you that... Like, how much of this can you run? How much of this is just completely "if I had enough gumption, I could get it running on my own Cloudflare account"?

**Chris Anderson:** So... Kind of yes. What we have set up is even for - if you're going in via the GitHub, it deploys to our end point, and it uses our login system... And that means that you could have projects -- basically, we want you to be able to be a Vibes DIY user, go run a fork, maybe your fork is like internal for your work or something, but not have to do the whole heavy lift of the full stack. The fork will just run against our backend. If you want to get even heavier than that - yeah, now you can start to code up the backend... But that's a senior engineer task.

**Jerold Santo:** How do you keep up with your underlying technologies in terms of what you're generating, or what you're telling Claude to use? Because those things are also moving targets.

**Chris Anderson:** I have more work to do there. There are models that aren't represented yet. I would love to get \[unintelligible 01:00:27.09\] personally when I'm in Windsurf... And so, there are some things we can do to keep up. We essentially need like a cultural ambassador to LLM land to keep us up.

**Jerold Santo:** What about to Next.js land? Is that a fast enough moving target? I guess you're always generating a new one, so it doesn't matter so much.

**Chris Anderson:** Right. And we're just doing that one file. I chose to do app.jsx instead of app.TSX, mostly because it's one less thing the model can hallucinate wrong. Now, if you wanted it to be TSX, I'm pretty sure Windsurf can fix that for you in a single pass.

**Jerold Santo:** Sure. But why? I guess by then you copy-pasted it, so it's yours anyway, right? Do what you want.

**Chris Anderson:** Exactly. Yeah, the JSX is all about the simplicity, and then the -- it really allows anybody to get in there, edit these apps, and bring them to any backend. When you do eject, it runs through those same APIs. Again, you can move them over. I don't know if there'd be a good reason, but there's a world in which, especially when we spin up the user pays mode for like image gen AI usage by the app, you might just pull our NPM modules directly into whatever environment and use those, because that lets you ship apps without having to worry about the cost of the LLM.

**Jerold Santo:** Say that again. I don't think I tracked it.

**Chris Anderson:** \[01:01:52.12\] So built into these NPM modules that's part of our standard library is that when you run out of your free tokens, it pops up the login window. And after you log in, and you get another batch of free tokens, you run out of those, it asks for your credit card. If all you care about is going viral and the thing that's holding you back are that going viral is going to cost you $50,000 in ChatGPT fees when people start using your prompts in production - well, do it on Vibes or do it with the Vibes NPM modules, and you'll get the same benefit that we'll handle it for you. And if you get enough usage, then you can be looking at creator payouts.

**Jerold Santo:** Yeah, that actually scales really well. I guess that's what you're referring back to the YouTube model, where basically as an app creator, I'm bringing you token use by way of people using my app, and you being Vibes DIY is making money off of every one of those people who decides to put down some cash in order to use the app some more. And so you're now talking payouts to me for bringing you guys additional customers. That's an interesting model.

**Chris Anderson:** A real kind of eye on the prize... You know, Couch did well, but I also learned firsthand what it's like to get whooped by MongoDB. \[laughter\]

**Jerold Santo:** How did that feel?

**Chris Anderson:** At the time, I wrote that rap about other NoSQL, right? You could tell how it felt. But now I appreciate what they did; they understood that the real answer to taking the market is to be on the ground floor when people are writing apps without permission in the enterprise. And so we're probably a decent choice for say you're running a veterinarian clinic, and your customer management system doesn't keep track of what the dog's favourite treats are... Vibe up a treat tracker... And on down the line the cryptographic causal consistency that's enforced by Fireproof means that you could use this for regulated supply chain. Maybe your cannabis dispensary needs to keep track of some stuff, because someone with a badge is going to come knocking... And Vibes has got the underlying infrastructure to make that safe. So after we make coding cool, we have a lot of bandwidth to go and make this system scale for serious use cases.

**Jerold Santo:** Do you think your brand scales that way?

**Chris Anderson:** We'll find out, but I kind of think so.

**Jerold Santo:** Here's a sub-brand: Serious Vibes.

**Chris Anderson:** Totally. Yeah, we talk about gray mode... \[laughs\]

**Jerold Santo:** Gray mode? There you go. Yeah.

**Chris Anderson:** There's a lot we can do there. There's a whole --

**Jerold Santo:** It's cool stuff.

**Chris Anderson:** ...like, if you wanted to fork the core thing and make it work with, say, not React... Like, I've got nothing against Vue. I've got nothing against Solid.js. All these things are excellent technologies. We chose React because it's the one that's going to give you the deepest training set. But being able to take the wrapper and deploy a Vue app or a React app to our Cloudflare endpoint - it's not going to change things. From an infrastructure standpoint, it's ready to go.

**Jerold Santo:** Alright, dorks, get out there and fork away... For the normal people, get out there and remix somebody else's golf tee time tracker...

**Adam Staravia:** Hm.

**Jerold Santo:** Adams has already published it.

**Adam Staravia:** And improve my vibes. My vibes were not so vibe.

**Chris Anderson:** Get your friends into coding. Get some -- make an image generator that no one would have expected, and make it go viral on your Facebook.

**Adam Staravia:** I've got a phrase for you. Ready for this?

**Chris Anderson:** I love phrases.

**Adam Staravia:** Vibe with friends.

**Chris Anderson:** Vibe with friends. That's right.

**Jerold Santo:** There you go.

**Chris Anderson:** \[01:05:54.24\] And that's coming -- I mean, that's just an easy on switch... Some of the folks we've been talking to are most excited about that this chat interface where you're talking to the LLM, and it's writing a code for you - that's multi-user. As soon as we flip on the same sharing mechanism that allows Adam to invite Jerold to the golf app, you can also invite Jerold to be the coder on the golf app, and you all can be in the chat together.

**Jerold Santo:** Now you really are vibing with friends.

**Adam Staravia:** There you go.

**Jerold Santo:** Awesome, Chris. Anything else that you expected us to ask you that we haven't asked you, or that you can't wait to tell us about before we let you go?

**Chris Anderson:** You all did a great job. I just can't wait to see what you vibe up.

**Jerold Santo:** I'm going to vibe some stuff. I'm going to get my kids vibing... This is going to be fun. Vibes.DIY, if we haven't said it enough times on the pod. That's your URL.

**Adam Staravia:** Vibes.DIY.

**Jerold Santo:** There you go. Tell your friends. Get your kids, get your nieces and nephews - if you're of age similar to ours - out there and do it yourself. I mean, I'm going to throw a few things at this. I think the image gen, like the caricature stuff - do you have a gallery of where... Because sometimes one idea just strikes. You've got to have something to start with, and you're like "Oh, I can just change that", like the remix thing. Do you have a gallery out there?

**Chris Anderson:** We moderate the stuff that shows up on the homepage. So we essentially have a carousel. Every time you hit refresh on the homepage, you'll get some new choices.

**Jerold Santo:** Gotcha.

**Chris Anderson:** There are some ones that illustrate how you do real things. If you have in your mind, as many of us dorks have, a mental list of APIs that have cores and don't require an API key, I've got for instance a vibe on there that is using Algeria's hacker news search to just bring you the vibe code news. So go remix that. Any API that's got that kind of access control - super-easy to use. And then, as I said, with this backend support coming soon, you'll be able to drop your own API keys in.

**Jerold Santo:** And what's the best way to get in touch with the creators of this, yourself, your team, your community? Is there ways that you can say "Hey, I'd love support for this, that, or the other thing" and you guys don't have it yet? Feedback, or a Discord, or a Zulip, or anything.

**Chris Anderson:** It's in the Discord, and the Discord is linked from our About page.

**Jerold Santo:** Alright. Go forth and vibe code with friends... Especially once that multiplayer feature gets toggled on. Let us know, Chris, when that's out there, because we'll definitely give it another shot, and probably another shout-out, as Adam and I could vibe code together. I could be changing his design as he's trying to add features. That'd be fun.

**Chris Anderson:** I'm looking forward to the day when your guests are on here with things they made in Vibes DIY.

**Jerold Santo:** That'll be amazing. That will be full circle, won't it?

**Adam Staravia:** That's what I'm trying to talk about. That's cool stuff. That's the way it's got to be done. I can't wait! I'm vibing. Furthermore, I'm vibing.

**Chris Anderson:** Thanks, Adam. Thanks, Jerold. Super-excited to be here. And yeah, remember, everything we do is open source, so you're invited.
