**Kevin Ball:** Lightning talks.

**Jerold Santo:** Let's do it!

**Jake Lundberg:** Yeah, so I just wanted to continue our chat, I guess, on A/B testing.

**Kevin Ball:** Alright, so since this is being recorded, and we may put it out, give us the setup. So A/B testing on the client side...

**Jake Lundberg:** Yeah, so A/B testing uses testing tools like Adobe Target or Optimize to deliver essentially third-party scripts to a site, modify them in some way, and you can control traffic - so some users get the default site, some users get a different experience, and you can measure the impact, rather than just making a change to the site and hoping for the best.

But with Safari making restrictions \[unintelligible 00:03:10.02\] CCPA coming out here January 1st... There are a lot of restrictions coming down. Where do you see the future of A/B testing going?

**Kevin Ball:** It's a great question. I think there are a number of different things inside that question. We were chatting earlier about client-side versus server-side testing... On the client side I see more and more things (broadly, not just A/B testing) moving to first-party scripts. So I see us hopefully getting away from the "load this tech from this site, and this tech from this site" and the bundle that ends up creating all of these nightmarish long download sites, and tracking from 20 different places... Marketing departments love it, it's terrible for consumers, and I think we're finally seeing regulation pushing us in a way that's going to say "Hey, that's not viable anymore."

\[04:03\] So I think for client-side testing we are going to see things moving towards instead of you just drop in a third-party script, you actually have to have an engineer do some work, and you do something that is first-party, so that you have full control over, and is not restricted in the same way. That's probably a negative for marketing departments...

**Jake Lundberg:** I was about to say.

**Kevin Ball:** ...but they're already feeling some of that pain. It's really hard to automatically drag and drop with a single-page app. They're already losing the capabilities, and so this would give us a way to get some of those capabilities back, involving an engineer.

**Jerold Santo:** It sounds like a company would be well-served to provide APIs, easy ways for engineers to build first-party without having to maybe host all the data, or provide their own scaffolding...

**Jake Lundberg:** That's been a huge challenge, not having access to APIs, or there just not being APIs available, and we're scraping pages for limited data. That's been a big challenge.

**Kevin Ball:** Yeah. I think there hasn't been an incentive to build out, for example, libraries there... Because every company wants to own that experience, so they say "Just drop in our script tag and go. Why would we create an open source library for you to control this stuff? It's all hidden behind our proprietary area." If that goes away, suddenly we have much more reason to build out utilities that are going to be helpful.

I suspect you'll also end up seeing proxying type stuff, where maybe you have an API over there, but since you don't want to touch anything that's outside your own domain, you say "Okay, drop this library and put this little proxy in", it'll keep all the user-specific data local and first-party, so you don't have quite as many restrictions about where you're sending things, and you don't have to say "Oh yes, we send your data to X, and Y, and Z." But then you can off-load the data analysis and processing to somewhere else, because -- I mean, with A/B testing you have two big pieces of it. For each individual, you want to assign them something, so that they get a consistent experience, and that is the tracking piece that is increasingly restricted... But then you also have data analysis, which can be anonymized.

You only really need the bulk data to get the analysis piece to understand which is the better solution here or what's doing better. That could be completely anonymized, that could probably stay as third-party services that provide a bunch of value-add there, so long as you can have that layer in the middle that's like "Okay, I'm tracking while you're on the site, so you get a consistent experience, but we're not sending any of your particular data anywhere; we anonymize it, put it in buckets, and send it off somewhere for processing and visualization."

**Jake Lundberg:** Do you foresee adding that additional layer being an additional challenge to accurate analytics tracking? Because there's already an issue with the analytics not necessarily being 100% accurate. Do you see an extra layer adding to that?

**Kevin Ball:** I don't know that it makes it worse than it already is. I mean, especially as you move to a world of single-page apps, or apps that are -- I love the universal JavaScript approach, where you render it server-side, but once it's loaded, it hydrates a single-page app... Those already have tons of problems with accuracy and keeping track of things, and you've already got to have an engineer involved, plugging that stuff in. I don't think it's any worse if what you're plugging in is a library that proxies through your local API, as compared to just dropping in some script tag and then having to use their programming interface to plug it in.

**Jake Lundberg:** Gotcha. Well, thanks guys. I really appreciate it.

**Jerold Santo:** Thanks, Jake.

**Break:** \[07:50\]

**Jerold Santo:** Next up we have Amal Hussein talking about finding your tribe at conferences. Take a listen.

**Break:** \[07:59\]

**Amal Hussein:** Hi, Jerold and Kevin.

**Kevin Ball:** Yo!

**Amal Hussein:** I'm really excited to talk about what I love about going to conferences...

**Kevin Ball:** Oh, yes!

**Jerold Santo:** UUP...! I like this.

**Amal Hussein:** For me, it's an opportunity to find my tribe. I love multi-track conferences especially, because I think you get to find your subtribe... And depending on what talks you're in, which hallway you're outside when talks get out... It's just a great place to catch your tribe, and I love that, I love that about conferences.

**Jerold Santo:** I like that take. I've always been anti-multi-track, because I appreciate a shared experience.

**Amal Hussein:** Oh, yeah. Same here.

**Jerold Santo:** But I like that angle into multi-track - find your subtribe.

**Amal Hussein:** Yeah, yeah. There's a wider tribe, and then there's your subtribe. And I'm with you, there's something about single-track conferences that I think create for richer conversations around everything that we're all experiencing together...

**Jerold Santo:** Yeah, we all saw it, we were all there...

**Amal Hussein:** Yeah. There's power in that. The power of the collective experience.

**Jerold Santo:** Yeah.

**Amal Hussein:** But you know, there's something nice about being in a multi-track conference, because you have an opportunity to connect and break the silos within tech. We're all at All Things Open, and there's a DevOps track, and there's a Blockchain track... Guess who didn't go to any blockchain talks...?

**Jerold Santo:** This guy.

**Amal Hussein:** It's me. I didn't go to any blockchain talks.

**Jerold Santo:** Me neither. You, Ball?

**Kevin Ball:** Nope.

**Amal Hussein:** \#noblockchain. Sorry, everyone.

**Jerold Santo:** \#noblockchain... I think there's like 22 tracks.

**Amal Hussein:** Yeah, there's like 22 tracks, and...

**Jerold Santo:** Holy cow!

**Amal Hussein:** ...so it's an opportunity for me to -- we all have a shared value here, which are we all are proponents of open source software, and we all leverage open technologies, so we all have those shared values... But now I get to meet someone whose maybe doing ops work and get to connect with them, with those shared values. So I think it's a silo-breaking opportunity.

**Kevin Ball:** I feel like I've been finding my sub-sub-sub-tribe... The people who are techy, but also willing to look goofy on camera and dance a little bit.

**Jerold Santo:** Oh yeah, that's a very small group.

**Kevin Ball:** Yeah. There's like five of us.

**Amal Hussein:** A group of one? \[laughs\]

**Kevin Ball:** No, no, no. Tracy is expanding the crowd.

**Amal Hussein:** Yeah, she's expanding that group, she really is.

**Jerold Santo:** Tracy has some TikTok going on. Ball, why don't you tell the people what you've been up to?

**Amal Hussein:** Dancing.

**Kevin Ball:** Um, dancing? I like to dance.

**Amal Hussein:** Did you see him dancing? \[laughter\] ...on TikTok.

**Kevin Ball:** Oh, my goodness.

**Jerold Santo:** Dancing with the TikToks.

**Kevin Ball:** I'd never heard of TikTok. I'd sort of heard of it, but I never understood what it is... But apparently it's the thing for the kids these days. Showing my age.

**Amal Hussein:** Yeah. Which means that no kids are now using TikTok. Once we discover it, it's not cool anymore.

**Jerold Santo:** Right.

**Kevin Ball:** \[unintelligible 00:10:46.29\] kids away.

**Amal Hussein:** Yeah, they're basically like on to the next thing.

**Jerold Santo:** Right.

**Kevin Ball:** They're like, "Oh, this guy's dancing! Kind cool! Oh, he has grey hair. Uh..."

**Amal Hussein:** \[laughs\] Yeah. "Mom, time to get off TikTok."

**Jerold Santo:** I spent a good part of an afternoon on TikTok when I first found it, just trying to figure out what the heck was going on with this thing... And then I uninstalled the app from my phone, and I'm just like "Alright, I get it. I'm moving on with my life."

**Amal Hussein:** It's a rage uninstall. I've done that before, too. Like "I don't understand this. This is really weird UX. Where are all the buttons? Where's my navigation tree?"

**Jerold Santo:** Right. I felt like I'd seen it all, because of all the other remixes and stuff, and there wasn't that many people on it then... So it was like the same thing, and it's funny, funny, funny... And it's like "Cute. Stupid. Funny." Then it starts to be like "Stupid. Stupid. Stupid" and you're like "Uninstall." There's like a downward spiral of my opinion. But I'm sure it's great...

**Amal Hussein:** Yeah, you feel the brain \[unintelligible 00:11:41.00\]

**Kevin Ball:** \[laughs\] I don't know, apparently Tracy likes it.

**Amal Hussein:** I mean, apparently...

**Jerold Santo:** Maybe Ball will be like a TikTok star...

**Amal Hussein:** She actually made that joke in her keynote yesterday. She's like "My husband thinks my brain is also shrinking because of it, or something..."

**Kevin Ball:** Yup, exactly. I mean, the fun thing is - it is neat to see people who cross worlds. I love the fact that she's out there, getting people to be uncomfortable... Because as developers, a lot of times we're not very comfortable putting ourselves out there, shaking our body, moving our body a little bit...

**Jerold Santo:** \[12:12\] Especially in the afternoon...

**Amal Hussein:** What body? We have a body? I don't know about that...

**Kevin Ball:** I know, we're just disembodied brains, right?

**Jerold Santo:** In the daylight.

**Kevin Ball:** But no, it turns out that our bodies are important, and if you treat them well, then you can think better and code better... And you goof off and dance a little bit, and then -- I don't know. You find your tribe...?

**Jerold Santo:** 27 seconds, do you want to give any shout-outs?

**Amal Hussein:** Shout-out to the conference organizers and all the keynote speakers and all the speakers. It's a lot of work. I did a talk... Hug your speakers, ladies and gentlemen.

**Kevin Ball:** Show appreciation.

**Jerold Santo:** Hug your speakers.

**Kevin Ball:** Tell them you liked their talk.

**Amal Hussein:** Yes. Tell them thank you.

**Jerold Santo:** Alright, thanks so much for lightning-chatting with us.

**Kevin Ball:** TikTok...

**Break:** \[13:04\]

**Jerold Santo:** Here's Matt Bromberg asking us some hard questions. This guy might have a future in podcasting.

**Break:** \[13:14\]

**Jerold Santo:** We have five minutes on the watch here... It's your show. What do you want to talk about?

**Matt Bromberg:** Oh man, I've always wanted to run the show for you all. Okay, so Jerold, Ball, I was fascinated by one of the keynotes today that talked about full-stack development.

**Jerold Santo:** As was I.

**Kevin Ball:** And the career development challenges that are happening, where there's a consolidation on that end. Can you tell me a little about your personal experiences with breaking into those new boundaries? What do you think is happening there? And then ultimately, how do people that are junior, that are trying to get into this industry - where do they start when it's such a big ball of things going on these days?

**Jerold Santo:** That's multiple questions... Which one should we tackle first?

**Kevin Ball:** Well, I already talked with Matt a little bit about this, so I want to hear what you have to say.

**Jerold Santo:** So where do I fit into the ever-growing front-end...

**Kevin Ball:** Front-end haystack.

**Jerold Santo:** ...the haystack developer? The move of the front-end developer, really the empowerment to a certain degree of the front-end developer to be more full-stack than traditionally we have been - well, I've always considered myself relatively full-stack, because I've worked on teams of one, sometimes two... So when I'm not full-stack, I'm very much the horse image on the slide that Chris Cooper put up, where I have a very immaculate back-end. I never thought I'd say that about myself.

**Matt Bromberg:** Yeah, yeah, an immaculate tail.

**Kevin Ball:** You have a fancy ass.

**Jerold Santo:** I have a fancy ass, and kind of horse face. \[laughter\]

**Matt Bromberg:** This metaphor has gone off the rails, but I hear you... Yeah, so you're better on one end of it...

**Jerold Santo:** I don't know it's feeling pretty apropos at this point. So I've always been at like a 90% stack. Where I lack a little bit in skills is usually in the CSS domain, where I can hold my own, but I do not feel like an expert. So I've always been very proficient at everything else...

**Matt Bromberg:** Right.

**Jerold Santo:** So I don't really know what that means for me... I feel like I'm just doing my thing still. And I was already going to learn the GraphQL, and do the things... So for me, I never consider myself a front-end engineer, just more of an engineer.

**Matt Bromberg:** Awesome. Yeah, and that makes sense for you, in your point. So you, for the next question, Ball - what does it look like for junior engineers, for people that are just coming out of boot camps, just coming out of a degree, and they're pivoting into technology, what does it look like to be in this part of the industry?

**Kevin Ball:** Yeah, I think it's intimidating, because folks see all this stuff going on, and it's changing, and "I've got to do this, and that, and I've got to do a framework, and I've got to do a back-end, and I've got to do GraphQL, and what's this serverless, and all of that...?" Honestly, I think as a junior you should pick one thing and focus.

**Matt Bromberg:** Cool.

**Kevin Ball:** So if you start in React, pick React and get React down. Understand it. Go deep. Try to get as much as you can in that, and really understand it before you start branching out. And I don't even say that within a specialty. So I've talked to folks who were like "Oh, I want to learn React, and I want to learn Vue, and I want to learn Svelte, and I want to learn Angular", and they're trying to learn all these things at once. They have a lot in common; if you go deep on one, you'll be able to branch out really easily later. But if you try to branch out at the beginning, you're going to get overwhelmed and never fully understand what's going on there. So I would say start one place, go deep.

\[16:22\] This actually ends up being played out if you look at published industry career maps. There are a bunch of companies who have published their career maps of "Oh, here's what we expect a junior developer, and here's what we expect a senior developer, and a tech lead", and going on and on and up into architects, what have you... They have this sort of progression, and in the beginning its learn how to learn, and learn one thing deeply. Then as you get up into a senior engineering position, maybe you're 4–5 years in, now you're branching out, and you're saying "Okay, I know my deep thing, and now I need to know the things it's interacting with." And as you get into the industry for more like 8, 9, 10 years, now you should be able to understand all the pieces and how they're fitting together, and go further and further.

But when you're just getting in, learn one thing. Don't be intimidated by all the stuff and feel like you have to do all that. That's hype, that's baloney.

**Matt Bromberg:** I really like that framing, because it's a lot about something that we lose in our current education system, which is about like "Well, know everything to a subpar degree, and then graduate and feel inferior in so many ways", as opposed to what it's like to actually work in this industry, which is enjoyed the path towards mastery, one thing at a time, and build on top of that stack of mastery. Is that what you're seeing, Jerold?

**Jerold Santo:** I agree with that. I think what you find in practice is as you dive into one aspect of the stack, and you get to know that really well, you learn the rest tangentially, osmosis, necessarily, by interacting with folks who happen to know this part really well, or having to interface and connect the Glue Pits together. I didn't go study DNS. Furthermore, I don't know if you guys studied DNS... You just kind of like learn how DNS works. "I've got to put my record in. What's an A record, what's an MX record..." These are things that I just learned because I was running websites, and I wanted the mail to be delivered. But I studied certain things more deeply. So I think you learn the rest because you have to, and I think that's a great way to go.

**Matt Bromberg:** Fantastic. Thank you so much for your time.

**Jerold Santo:** Wood! Five minutes ain't much.

**Matt Bromberg:** No, man. Lightning-talking with three people...

**Break:** \[18:28\]

**Jerold Santo:** Crystal Williams-Brown approached the booth right before I was packing up to tell me about Code The Dream.

**Break:** \[18:42\]

**Jerold Santo:** Crystal, thanks for joining me. What would you like to talk about today?

**Crystal Williams-Brown:** I would like to talk about Code The Dream. It's a nonprofit that offers free programming classes to remove some of the barriers that people face when getting into the tech industry, and also provide some work experience, because that's another barrier for people who just recently have been trained. So they can learn how to make apps for other nonprofits, or socially-conscious businesses.

**Jerold Santo:** Okay, Code The Dream... I like that. What are the barriers that are typically there?

**Crystal Williams-Brown:** The original barrier that they were created to face was part of Uniting NC is helping people with their immigration status, and they discovered these immigrants couldn't get financial assistance to go to school, and they were having some trouble finding work. So two of the people who worked for Uniting NC, Radio and Dan - they both joined together to create Code The Dream, because Radio had studied computer programming in school; he has a computer science degree. So he thought "I can teach them what I know, and at least they'll have that to work with." And you can get by a little easier in the tech industry, especially now, without having a degree, but just having the training.

And then they saw people were having a hard time getting hired, because they didn't have the work experience, so they created Code The Dream Lab, where we can make practice apps, and then make apps for other nonprofits and socially-conscious business.

**Jerold Santo:** \[20:07\] Cool! So how did you get involved?

**Crystal Williams-Brown:** Actually, I was looking for a way to learn programming for free. I was unemployed. I'd struggled with employment for a while, and I actually do have two degrees, but neither one led to any kind of gainful employment... And I was led through the Iron Yard, oddly enough. I reached out to them and I said I couldn't afford their classes, but I really wanted to learn, and they said "Well, Code The Dream has free programming classes. You should look into them", and I was very grateful for that help.

**Jerold Santo:** Awesome. For those listening wondering what those loud noises are in the background - we are in the late afternoon, the last day here at All Things Open, and they're literally closing down shop around us... Crystal, how do people get involved? Who's the right person...? If they wonder "Is Code The Dream for me? Maybe I can get in on the helping side, versus the receiving side." Guide us through that.

**Crystal Williams-Brown:** Well, we have a website that's very helpful in guiding you in whatever direction you want to go... Because we do take in volunteers who teach classes, or they can be a mentor for a student, or you can even come in for a small session where you teach one day, just something that you know that could help out the interns that are currently in the program. And if you want to take classes, they have sessions running throughout the year, and they're in different locations. We're also branching out, so that you can do it remotely. We have some students who are out in Chicago, and then we're going to branch out into more states.

**Jerold Santo:** Nice.

**Crystal Williams-Brown:** So it doesn't matter if you live in North Carolina or not.

**Jerold Santo:** Okay, you don't have to be in North Carolina... How long has this been going on?

**Crystal Williams-Brown:** It started in 2014, which is funnily enough when I was unemployed.

**Jerold Santo:** Oh, really?

**Crystal Williams-Brown:** So it worked out really well for me.

**Jerold Santo:** So you had free time.

**Crystal Williams-Brown:** Yeah.

**Jerold Santo:** Are you employed now?

**Crystal Williams-Brown:** I am, I'm employed by Code The Dream.

**Jerold Santo:** Tooth...!

**Crystal Williams-Brown:** I'm a full-time developer with them now.

**Jerold Santo:** Very cool, very cool! How many people work there?

**Crystal Williams-Brown:** It grew. It started very small, but a lot of the staff is actually people who have been through the program, and really showed a kind of persistence and eagerness to learn, and also some adeptness at learning... And they gave them more and more responsibilities, and then finally saw if they could bring them on full-time. They like to retain people, and we're trying to make more in-house apps that we can use to raise money for Code The Dream, so that we're not so dependent upon grants, and that allows us to hire more people... So you don't have to worry about looking if you don't wanna look; you can stay.

**Jerold Santo:** You can look, or you can stay, assuming that you guys get that ball rolling. So that's very cool... We have a few seconds left. Any shout-outs you'd like to give, beyond Code The Dream, or maybe to your partners in crime there?

**Crystal Williams-Brown:** Well, I am working on an app called Upstate, that tracks bills in North Carolina and alerts people about anything that's happening to them...

**Jerold Santo:** Cool!

**Crystal Williams-Brown:** And you can sign up for free. You can also view all the actions that are happening on bills for free. It's called Upstate, at app.keepupstate.com.

**Jerold Santo:** App.keepupstate.com. Awesome, Crystal. Well, thanks for joining us!

**Crystal Williams-Brown:** Thank you!

**Break:** \[23:15\] to \[23:57\]

**Jerold Santo:** Okay, here's the live show on stage. Please bare with the audio if you can, because we have a lot of great guests that you will not want to miss. Here we go.

**Break:** \[24:04\]

**Jerold Santo:** Okay, well the sound of those beats means it's time for JS Party. My name is Jerold Santo, thanks for joining us. I'm joined by Kevin Ball. He goes as Ball. Say hi, Ball.

**Kevin Ball:** Hey, I'm Ball! Nice to see you!

**Jerold Santo:** And this is Emma Wedekind.

**Emma Wedekind:** Hi! Can you hear me? I can't hear me.

**Jerold Santo:** We need to get Emma turned up.

**Emma Wedekind:** Is that better? No? Yeah? UUP. I can also just talk louder! Cool.

**Jerold Santo:** And we're ready to go. First up, we did have a -- we primed the pump a little bit... First, I should say this is for everybody to participate in. We were afraid or concerned that perhaps nobody would come up, and we'd have not much of a show... So we did prime the pump and I do have a short list of people that we've contacted before, that we would love to chat with. As we make it through the list, maybe some people don't show up, maybe some people do... We'd love to open it up for everybody to come and talk. And then if we run out of time during this session, we are down on the third floor, booth 72, with the mic all set up, and we will continue the lighting chats there if you don't get a turn here during this session.

The first person we'd like to call up on the stage is Danes Cooper. Danes is happy to join us, but has a flight to catch, so she's going first... And here comes Danes. A round of applause for Danes!

**Emma Wedekind:** Hello!

**Jerold Santo:** Hi! Thank you for joining us. Please have a seat.

**Danes Cooper:** I'm leaving my purse there.

**Jerold Santo:** Okay.

**Danes Cooper:** \[laughs\] You guys have a watch on it, because I'll need it to get on the plane.

**Jerold Santo:** We'll keep an eye on it. So the other thing I didn't say - or maybe I did say it, but I'll say it again - is that this is a community thing, so we wanna talk about anything that you wanna talk about, Danes. We literally prepared nothing... So please give us a topic, and we're happy to shout it out with you.

**Danes Cooper:** Okay. I normally talk about inner source, but after the keynotes today I think it's important to talk about corporate responsibility... Because I was really disturbed by the AWS talk. I was disturbed because there was an implication that OSI-approved licensing is somehow optional... And that is not the case. So I called them out, I called Arun out... And you know what, I'm not saying Arun is a bad guy, but I think when you let your customers decide how you're going to engage with open source, you run the risk of listening to customers that are maybe not so savvy, and think that change is maybe in the air... But it's not clear to me that change needs to happen to open source. I think we got this far because we've made good choices about how to make it last this long. I think we should make changes to the licensing schemes and to the importance of licensing very, very carefully... So that's what I would like to talk about.

**Jerold Santo:** Let's do that. One thing to point out for those that weren't at the keynote this morning, listening to the podcast, is that there was a talk from AWS's Arun Gupta, in which he talked about free credits for open source projects.

**Kevin Ball:** Free credits for open source projects, with a set of criteria... And some of those criteria they put preferably, and in some cases I was like "That's overly restrictive", and in other cases, like the licensing you brought up, I was wondering "That seems a little..."

**Danes Cooper:** It is really dangerous...

**Jerold Santo:** So the point that you'd like to highlight is free credits for open source projects, preferably OSI-approved projects...

**Danes Cooper:** And that "preferably" has to go away.

**Emma Wedekind:** Can you explain OSI?

**Danes Cooper:** Yeah, sure. I worked on the OSI for ten years, so I'm in a good position to talk about it, I think... I think I might have served longer than almost anybody else. But Michael Riemann, local god of open source was on that board with me, too.

\[27:53\] The OSI decides whether licenses are OSD-compliant. OSD is the Open Source Definition. It's ten clauses, it's very straightforward. It's common right now for people to be suggesting changes to open source that would make it better. We actually got a -- a license was submitted this week called the Vaccine License. It has a field of uses restriction that only lets you use this software if you've vaccinated your children. People are suggesting really silly field of use restrictions... But some of them are well-intentioned, like "I wish that big corporations would have to pay", so I want to put a clause on the license that says that that is a field of use restriction; that automatically disqualifies you from OSI approval, because that clause in the OSD says you cannot do field of use restrictions...

We talked about this a lot 20 years ago. Most of us in those days were libertarians, or at least liberal-leaning, and some of us didn't want the software to be used for instance for nuclear power, or for weaponry. But we debated it out and realized that we had to set that aside in order to not create the slippery slope of everybody needs a special carve-out. And all through the history of OSI, licenses that aren't OSD-compliant come from companies that are trying to get a carve-out for their business model, because they don't have a good, strong understanding that open source is not a business model, and they're going to need to change what they do. They can't have their cake and eat it, too. Either they get the halo effect of open source, or they get to say how they want to run their business in ways that open source people would not appreciate. But they can't do both.

We've been fighting that fight forever now. It's really disheartening to see a major venue like AWS, who's trying to convince us that they're serious about open source, use the word "preferable" as though there was any other option if you're actually dealing with open source.

Now, you'd be told that OSI doesn't own that trademark to the term "open source." Nobody owns that trademark, because the trademark office decided that it wasn't trademarkable. But they do own OSI-approved license, which tells you that that license fits within the OSD, therefore it doesn't do anything to harm the open source movement.

Examples of recent things that were problematic - Facebook a few months or a year ago now put a license on React that included an extra patent clause... And Apache said -- a lot of people tried to talk them out of it. They were sure they had to do it to fend off piracy. I said "Look, you've got deep pockets. Your job is to engage those pirates and take them to the mat. Look at Vision is doing. That's what you should be doing as a deep pocket, not trying to write your way around it." But in the meantime Apache is going to say no to that; it's an additional obligation. And as soon as Apache started stripping out React code, they shifted their program. That is how we have been enforcing for the last 20 years. It's not ideal, but it's what we've done.

**Jerold Santo:** Alright, everybody, a round of applause for Danes!

**Kevin Ball:** Speaker number one! \[applause\]

**Jerold Santo:** Alright. We thought that buzzer would be fun. It turns out its kind of rude... \[laughter\] So I apologize for that. I could just hop into the code and change it, but let's not do that. Let's not go there. Okay, is Mo Hampton here? Oh, he's here! A round of applause for Mo! \[applause\] Come on down!

**Emma Wedekind:** I feel like we need the entrance music.

**Jerold Santo:** We probably do.

**Kevin Ball:** We do need entrance music. We'll just beatbox it, right?

**Mo Hampton:** Oh, you don't have entrance music...? That's okay though. I'm okay. I had it in my head.

**Jerold Santo:** Let's play this game - if you had to pick some intro music for yourself, what would you have picked?

**Mo Hampton:** Livin' My Life Like It's Golden, Jill Scott. \[song sample\]

**Jerold Santo:** Alright, Mo, thanks for joining us. Five minutes on the clock, we'd love to chat with you.

**Mo Hampton:** Perfect.

**Emma Wedekind:** What do you want to talk about?

**Mo Hampton:** \[31:55\] For me, something dear to my hear is just breaking into tech. I've done that transition about three years ago, and I love what I do. There's no other job out there for me. I'm a software engineer right now...

**Jerold Santo:** Awesome.

**Mo Hampton:** ...for Defence. I'm a government contractor... But the thing that I think about a lot is those that have non-traditional CS backgrounds, and that come in. There's some that back from like chemistry, or some people that have something biology that come in, or even people with marketing and advertising. I know it's possible, but I don't know how others feel working with somebody who's non-CS on the team. So I guess I can open that up... Like, how do you guys feel when we come into your space?

**Kevin Ball:** You're one of me. \[laughs\]

**Emma Wedekind:** First, you're not coming into our space. It's all of our space.

**Mo Hampton:** That's true. That's a very non-inclusive word to say.

**Emma Wedekind:** So I think we need to change the paradigm, what it means to become a developer... Because I have a CS degree, and that did put me in advantage, I'm not gonna lie about that; I do feel like that was a privilege. That being said, in terms of the things that I had to learn, I had to work hard to learn those skills, and to see people coming from non-traditional backgrounds - I love working with them. I feel like they bring the vantage point that I have not thought about before. I don't know how to formulate my thoughts right now...

**Kevin Ball:** I 100% agree.

**Mo Hampton:** They give you a different point of view than somebody who's been traditionally through a certain pipeline, and hitting certain classes. They give you a different worldview on things.

**Emma Wedekind:** Yeah, absolutely.

**Kevin Ball:** Yeah. I think it may be slightly harder to break in, but honestly, having a more diverse background gives you an advantage once you're in the game. This may be tooting my own horn, because I'm not a CS background, but I feel like if you go through a CS program - yes, you understand a little bit more of a lot of the fundamental stuff, but you actually don't have that much of a perspective of how the rest of the world works. And if you're coming from another background, especially if you're coming from another professional background - that synergy of skills, of "I understand how this world works, and now I understand the code", that's an incredible advantage, because you can link between those things.

One place where we as coders often fall down is in communication with people outside the software world, but we're building tools for humans. We need to talk to those people.

**Emma Wedekind:** Yeah. I feel like because I went the CS route, I was very tunnel-vision. And when I got to my first job, I did terribly. I thought I was going to quit or get fired, because all I knew was that Bubble sort was worse at runtime than Merge Sort. I didn't understand the practicalities of working in our environment... So people who come from alternative backgrounds to get into this role, I think a) they're used to working harder than we are... Because unfortunately, they feel like they have to prove themselves more, and unfortunately that is the case; I would love to change that. But I also feel like if you come from a bootcamp, you're better prepared practicality-wise to get into development, than a CS background... At least in my experience.

**Mo Hampton:** That's true. That's a good point to bring up. And I was just thinking -- you were saying about people that come from different professional backgrounds... For me, I'm a veteran, so I will look at a problem set differently, and kind of charge forward; I don't know if that's the right way to do things... I'll go head first, and then figure out the collateral damage later, but... It's a different aspect that we all bring to the table, and I hope that people are more open towards it... But sometimes you do feel as if you have to prove yourself more.

**Emma Wedekind:** Right. Well, degrees does not equate to your intelligence. I think IBM just recently started doing apprenticeships -- not apprenticeships, but like trials for bootcamp attendees, where they would bring them in, hire them for a year, and help them grow. So even if you didn't feel like you were prepared, they would try to coach you along and help you. I think what's important is potential and willingness to learn, as opposed to the piece of paper that you would get if you graduated.

**Mo Hampton:** \[36:06\] And I think it's good also because we have -- say for me, I'm stronger probably in my soft skills than I am in my skills of software engineering, but I do have the people that have that background education to bridge that gap. So it's very good as long as we know our skill sets, and we know the gaps. We come together and try to help each other out.

**Emma Wedekind:** Absolutely.

**Mo Hampton:** I'm glad you guys can talk to me about that.

**Kevin Ball:** Oh, yeah. And let's get rid of the word "soft skills." They're human skills. This is how we interact with humans, and that is the end goal of what we're trying to do. We're building things for people.

**Mo Hampton:** Yeah.

**Jerold Santo:** Human skills.

**Mo Hampton:** Oh, it looks like there's ten seconds left, right?

**Jerold Santo:** It does.

**Mo Hampton:** Can I get the outro music then?

**Jerold Santo:** Give a shout-out. Do you have a shout-out you want to give? You have five seconds.

**Mo Hampton:** Oh, shout-out to everybody at All Things Open. You guys are amazing for showing up!

**Jerold Santo:** Let's hear it for Mo!

**Mo Hampton:** Alright, thank you.

**Jerold Santo:** Thank you. Alright... How about Maria Lamar do?

**Emma Wedekind:** Yay!

**Jerold Santo:** There she comes!

**Kevin Ball:** What's your intro music? \[Ball beatboxing\]

**Emma Wedekind:** I'm not singing...

**Kevin Ball:** Not singing?

**Emma Wedekind:** I'm not singing...

**Jerold Santo:** Please don't give Ball intro music.

**Emma Wedekind:** ...nobody wants to hear that.

**Jerold Santo:** Well, when you sit down, you can tell me if I pronounced your name correctly, or you can chide me if I did not. Please, we'd love to call you by name.

**Maria Lamar do:** Maria Lamar do.

**Jerold Santo:** Very good.

**Emma Wedekind:** That's beautiful.

**Jerold Santo:** That is beautiful.

**Maria Lamar do:** Thanks.

**Jerold Santo:** I cannot say that well, but I will do my best. What would you like to talk about today?

**Maria Lamar do:** I'm very passionate about web accessibility and building communities.

**Emma Wedekind:** Yay!

**Jerold Santo:** Okay. Do you want to do both of those? We've got five minutes. Do you want to do accessibility?

**Maria Lamar do:** Accessibility sounds great.

**Jerold Santo:** Okay, very good.

**Emma Wedekind:** What got you into it? What inspired you to...

**Maria Lamar do:** Yeah, so I come from a non-conventional background; I'm actually a behavioural analyst. I provided behavioural therapy for people with developmental disabilities for eight years before I switched into development... And while I was learning how to program, I was so happy when I discovered web accessibility. I was like "Oh yes, this is for me!" After that I just kind of went all-in on web accessibility.

**Emma Wedekind:** I think what's interesting is that we hear web accessibility, and my first thought goes to screen reader compliance, and keyboard navigation, all these things... I also feel like accessibility is broadened to thinking about who's consuming your applications and your websites... So we are in a place of privilege where we have high-speed internet in this country. But if your app is being consumed by people with lower-speed internet, we need to be mindful of that. We shouldn't be shipping all of this really heavy stuff.

So accessibility is not just about what we traditionally think of as accessibility, but also can people access your application from...

**Maria Lamar do:** Right. Like different hardware, or...

**Emma Wedekind:** Yeah, exactly.

**Kevin Ball:** The network speed is a huge one. I have T-Mobile, which is great, because they give you internet access anywhere you go, pretty much. They have 200 countries, or -- there aren't even that many countries, but essentially, anywhere you go, you're going to have internet access, but it's at 2G speeds. And if you ever try to access the websites you're used to accessing from your desktop or your laptop, even over Wi-Fi, at 2G speeds on a phone from somewhere halfway across the world, it is painful. And many of - as Emma highlights - the same practices that are going to make your application accessible to folks here who have assistive software, or things like that, are the same things that are going to make it accessible to folks who have really poor internet connections.

**Maria Lamar do:** Yeah. Even thinking about creating progressive web apps, where you could just launch right off your home screen, and it's just that much easier, once that launched. And even if you don't have great connectivity... So it's very important.

\[39:53\] Playing off of what Mo was saying, coming from a different background really gave me a new perspective, because I already had the experience from all the users who were struggling to interact with these applications... And I just didn't know that a world existed for coding such things. So now coming into it, it's like "Well, I know exactly where all the pain points are" and "What can we do to fix it?"

So I do think that it's super-advantageous to come in with that fresh perspective, and never let your different background be a negative thing. I think it's always a good thing.

**Kevin Ball:** To your point about having seen the users - I wish every developer went and looked at the users of your application and watched them use it.

**Jerold Santo:** Like, stare at them through their window, or what do you mean?

**Kevin Ball:** Bring in folks who have never used your application, but are in your target audience, or who do use your application every day, and just watch them use it... Because your mind will be blown. We have these models of how our stuff works, and other people - normal people out in the world don't have those models. Every time I've ever watched somebody use something I build, I'm flabbergasted. Like, "You do what? You do how?!"

**Jerold Santo:** Yeah. It's humbling, because you realize how much your stuff sucks... \[laughter\] Like, "I thought this was perfect. Then I watched you try to use it, and that's not good. It's not good."

**Emma Wedekind:** We make assumptions that users use our products the way we use them.

**Jerold Santo:** The way we would.

**Maria Lamar do:** Yeah. And we're stuck seeing them every day as we build on them, so to us, it's like "Oh, well, we've definitely improved it, and now it's perfect." Then somebody's coming into it brand new, and it's like "Well, none of these make sense."

**Jerold Santo:** Yeah. Is there any real low-hanging fruit of accessibility, or a gripe? Like, "Why does everybody get this wrong...?"

**Maria Lamar do:** Use buttons for buttons, links for links, don't take \[unintelligible 00:41:37.11\] Please, just don't do it.

**Emma Wedekind:** Yes. And if you are going to create custom elements, like custom dropdowns, in instances where you can't use the native semantic HTML elements, you still have to make concerns such that it functions the same way a native input would.

**Maria Lamar do:** Yeah, absolutely. I would always say, whether you're considering accessibility or not, just put your mouse away, try to navigate your entire application with the keyboard only, even if you are not turning on the screen reader. Just go through that basic navigation with your keyboard, and you should be able to access everything. And if you can't, then there's something wrong. So try to figure that out.

**Jerold Santo:** Thanks, Maria. Let's hear it for her! \[applause\]

**Kevin Ball:** Thank you, Maria.

**Jerold Santo:** Did Brian Douglas make it? How about Eva Howe?

**Emma Wedekind:** Yay!

**Jerold Santo:** There she is! Come on down. Let's hear it for her! \[applause\]

**Kevin Ball:** As Eva is walking up, since so many people no-showed, that is an opportunity for everyone here who has a topic they want to talk about... So have that in your head, "What would I talk about if I was on stage?" so when Jerold opens the door, you're up, you're ready.

**Jerold Santo:** Is it Eva or Ava?

**Eva Howe:** It's Eva.

**Jerold Santo:** Eva. Very good. Eva, thanks so much for joining us on stage here. We're happy to hear what you're up to. What you'd like to talk about?

**Eva Howe:** I work for a company called This Dot Labs, and we have an apprentice program where one of our big passion projects is getting more women into tech. Our founder is a woman, we have a lot of women on board... So what we do is we take women who are coming out of bootcamp, and we pair them with a mentor. And then we're a consultancy, so we contract them out together, with the idea being that the woman gets the mentorship that she needs.

We've heard a lot of companies say they don't like to hire junior developers, because they got a deal with the mentorship aspect... So we provide that by pairing them up, and the company gets 40 hours of the junior and 20 hours of the senior. Then at the end of the contract, the company has the ability to hire the woman.

**Emma Wedekind:** That's wonderful.

**Kevin Ball:** That is awesome!

**Jerold Santo:** It sounds very cool. How does it work in terms of if you're interested in getting involved, or...?

**Eva Howe:** You can come by our booth. We have one literally outside this door. Or you can email hi@thisdot.co.

**Emma Wedekind:** \[43:55\] How does the mentorship aspect of that work?

**Eva Howe:** It varies from woman to woman. It depends on the contract too, but the idea is that the mentor is there to help unblock the woman, to check PRs so that she's not crashing anything when she merges... And then also just to help navigate being on the technical team, especially in a sense where she may be the only woman on the team. That gets a little bit more tricky, because a lot of times the senior developer will be male, and that's hard to have that do... But in that case we like to try to plug her into her local community, where she can find more mentors that are female too, even if they're not working on that particular project.

**Emma Wedekind:** What's the biggest challenge that you face with that?

**Eva Howe:** Getting companies to put their money where their mouth is. Everybody is out there talking about diversity, inclusion... I live in Silicon Valley. Everybody knows that 25% of incoming software engineers are women. We've done huge, huge pushes on this, and I get calls, and people are super-excited, and "This is a wonderful program, and we really want to do this!" and I write back, and I get radio silence. So I feel a little bit frustrated in that aspect, that people are very willing to talk about it, but not willing to do anything.

**Emma Wedekind:** Do the women come to your first, and then you match them with a mentor and a company, or do they go to the company...?

**Eva Howe:** So we partner with boot camps all around the country, and we get the women applicants mainly from the boot camps; somewhat through just Twitter outreach and our website... And then the idea is that we -- it's kind of a couple of moving pieces. Obviously, we want to pair the women up with the company in that she has some bases in the technologies that they're using, and that there's a good fit with the mentor. Absolutely, there are personalities there, too... And then fit them with the company. It kind of goes back and forth to make sure that everybody is a good working fit.

**Emma Wedekind:** That's cool.

**Kevin Ball:** I love this idea of an apprenticeship. I feel like this is something that -- I mean, it is definitely important and helpful on the folks coming in from untraditional backgrounds, boot camps, women who are at a disadvantage, other under-represented minorities who are at a disadvantage... Broadly, we as an industry suck at training people. We are terrible... I mean, boot camps have somewhat solved the getting in; I get the first step, and then what? What do I do? Every company I talk to is like "Do you have seniors? Do you have seniors? Do you have senior folks?"

Nobody is training senior folks. Everyone's trying to hire senior folks, but we don't have this pipeline for how do I get from "I just got into the industry" to "I'm able to lead a team, or be a senior" or something like that. So props to you all for doing that. That's great. I think the diversity aspect is a key and important step, but I'd love to see this everywhere.

**Eva Howe:** I completely agree, because I think it's really hard for juniors to get the on-the-job mentorship that they need, and so many companies, for whatever reason, just aren't willing to take that on, and hire juniors. I think a lot of times either their senior engineers are not positioned to do it, they don't want to take the extra financial burden of it... There are a lot of different reasons for it. But in our case, this is a way of us taking that out of the equation.

**Emma Wedekind:** Does that typically bypass the typical whiteboarding interview as well?

**Eva Howe:** Yes.

**Emma Wedekind:** Oh!

**Eva Howe:** We do code exercises, but it's not a whiteboard interview. We're actually a fully remote company, so it'd be a little bit difficult to do a whiteboard interview... And we do other ways of measuring where she is, and what technology she's good at. But no, no whiteboard interviews.

**Emma Wedekind:** I like that.

**Eva Howe:** Thank you. \[laughs\]

**Jerold Santo:** Is it code schools only, or can you be from a different background and still apply?

**Eva Howe:** You can be from whatever background you want to apply. We focus mainly on boot camps, just because that's where the majority of our applicants are from. \[timer alert\]

**Jerold Santo:** Sorry about that.

**Eva Howe:** No worries.

**Jerold Santo:** \[48:02\] Alright, let's hear it for Eva. \[applause\] We talked of Vanessa. Is Vanessa here? There is Vanessa! Come on down...

**Emma Wedekind:** Yay!

**Jerold Santo:** Vanessa Alvarez... Give her a hand. \[applause\]

**Kevin Ball:** Is that the end of your list? Because...

**Jerold Santo:** It is the end of the list...

**Emma Wedekind:** You all better get ready...

**Kevin Ball:** You all be ready.

**Emma Wedekind:** Welcome!

**Vanessa Alvarez:** Hi!

**Jerold Santo:** Hi!

**Vanessa Alvarez:** I was thinking about talking changing careers in the tech industry... But then the other person was talking and had a good idea about whiteboard, and I just wanna heat about what type of interview process you guys do at your current companies. Because I don't like whiteboarding...

**Emma Wedekind:** Oh, no one likes whiteboarding interviews...

**Kevin Ball:** I like whiteboarding interviews as a taker. I hate it as a way to find good people.

**Jerold Santo:** And you would prefer the whiteboard?

**Kevin Ball:** I didn't say I'd prefer it... It's fun. It's fun for me because I love goofing off... So I'll get up with folks, and like -- whiteboarding, you get to... I like whiteboards in general. That's how I brainstorm; that's how I do whatever.

**Jerold Santo:** Just a fan of whiteboards over here...

**Kevin Ball:** I have whiteboards in my office... It's a terrible way to interview people.

**Emma Wedekind:** Yeah.

**Kevin Ball:** It's absolutely terrible.

**Emma Wedekind:** You should have led with that.

**Kevin Ball:** I think it's fun. It's terrible.

**Jerold Santo:** Can you enumerate why it's terrible?

**Kevin Ball:** It's because it's testing completely different things than what you care about for a candidate. Whiteboarding is testing how well do you improvise on the spot, in front of people that you don't know, with a marker in your hand.

**Emma Wedekind:** And communicate.

**Kevin Ball:** And communicate with people you don't know. Communication - that part is actually in my opinion kind of valid, because I think it's important that engineers can communicate...

**Emma Wedekind:** No, that's valid, but in terms of being able to eloquently communicate.

**Kevin Ball:** On the spot, under pressure, in front of people you don't know, oftentimes with folks who are not the kindest of interviewers...

**Emma Wedekind:** Right.

**Kevin Ball:** Yeah, it's setting folks up for failure, unless they're skilled in things that are not actually helpful for their job.

**Emma Wedekind:** Yeah. I had a -- it was a good experience, but it really frustrated me because it was an interview for a UX engineering role, building design systems with React. And two out of the four interviews were about algorithms, so I had to code binary trees on a whiteboard, and find the broken edge... And I'm like "How is this relevant to the job I'm going to be doing?" It's not.

**Jerold Santo:** No.

**Emma Wedekind:** And that is so unfair, to so many candidates... Going back to the whole "What if I'm not from a traditional CS background?" how is that testing anyone's ability to deduce information and problem-solve? To a certain extent it's not.

**Kevin Ball:** What if English isn't my first language?

**Emma Wedekind:** I know. Yeah, exactly.

**Vanessa Alvarez:** So what would you suggest the appropriate --

**Jerold Santo:** Yeah, what's better?

**Vanessa Alvarez:** What would be better instead of the whiteboard?

**Emma Wedekind:** I like the take-home exam. I had a really great interview with Gatsby. They gave me three questions, and they said "Answer whichever one you feel comfortable answering." To give options to your candidates is incredible. That whole interview process was seamless. The take-home assessment - first, they were going to pay you for it, which is amazing, because often these companies put you through the wringer within the interviews, and it's unpaid.

**Vanessa Alvarez:** Right.

**Emma Wedekind:** The second piece of that is to do the tasks that you would be doing on the job. a) It's practical. b) You get to see if you even want to do this job in the first place. So I think sticking to practical things that are also manageable - because a lot of us have families and other obligations - we can't give up time to go on-site and give up a full day of work...

**Vanessa Alvarez:** And applying is almost like a full-time job.

**Emma Wedekind:** It is, it is.

**Vanessa Alvarez:** Something interesting that we've been doing in my company - we stopped whiteboarding, and right now what we're doing is basically we have a bunch of functions, and then we tell the person like "Hey, just pretend that we're working together, we're collaborating, just like a normal day, and just tell us what is this function doing." Then we start talking. We want that engagement, and we like that conversation happening... We're testing not so much their technical skills - those too, partly - but more about collaboration. Furthermore, we want to know if this person will reach to us if they have any questions. It has worked for us very well.

**Emma Wedekind:** \[52:27\] It's like less of a test and more of a collaboration.

**Vanessa Alvarez:** Right. So it's like "Did you read and understand this function?" "Yes." "Okay, awesome." And if they get stuck, "What are you thinking about? Tell us." "Oh, this is what's going through my mind." That has worked better, and we have gotten them to be not so nervous, and it has helped us a lot.

**Emma Wedekind:** Yeah. I also think it takes a lot of skill to be a good interviewer.

**Vanessa Alvarez:** Yeah, absolutely. That's another thing, yeah.

**Emma Wedekind:** I was just going to say, as the last point, please don't try to trick your candidates and show who's smarter in the room. That's not a good approach.

**Vanessa Alvarez:** Yeah. \[laughs\]

**Kevin Ball:** The closer you can get to it being "what it's like to actually work here", the better of a tell you're going to be able to get. And you do want to scope that within the bounds of what's possible for that person. My favourite - both as an interviewer and as an interviewee - way to interview someone is to do a scoped, paid project.

**Emma Wedekind:** I love that.

**Vanessa Alvarez:** Yeah, it's great.

**Kevin Ball:** Now, that is not always possible. If you have a full-time job, and you have family obligations, you may not be able to take another project like that. So you need to be accommodating. But the more you can get to "This is exactly what it's actually going to be like working in this environment", the better chance you both have of being able to tell "Is this going to be a good fit?"

**Emma Wedekind:** Yeah.

**Vanessa Alvarez:** Awesome.

**Jerold Santo:** Well, that's our time. Vanessa, thanks so much for sitting down.

**Vanessa Alvarez:** Thank you. \[applause\]

**Jerold Santo:** Okay, audience, if you have a project that you've been working on and you want to tell the world, if you have a passion that you care about, and you'd like to chat with us, if you have a hand, and you'd like to raise it high in the air... A heartbeat...

**Emma Wedekind:** Right there!

**Jerold Santo:** Either one, we'll line them up here.

**Emma Wedekind:** Yay! Awesome! Come on down!

**Jerold Santo:** Let's hear it for the nice man who's running...

**Emma Wedekind:** We need the Price is Right music.

**Jerold Santo:** We do. Come on down...!

**Kevin Ball:** If I knew it, I would sing it.

**Jerold Santo:** Hello! Greetings!

**Emma Wedekind:** Hello!

**Jerold Santo:** Thanks for joining us.

**Clinton Dreisbach:** Hey, guys. I'm Clinton Dreisbach.

**Jerold Santo:** Hey, Clinton. Nice to meet you.

**Clinton Dreisbach:** I keep hearing talking about boot camps up here, and I decided to run up, because I co-founded one, and I teach at one... So I thought it would be interesting to talk.

**Jerold Santo:** Awesome!

**Emma Wedekind:** Tell us about that!

**Clinton Dreisbach:** Yeah, a bunch of my students are here; they're all in the audience, which is awesome. I hope one of them runs up here.

**Kevin Ball:** What's the bootcamp called?

**Clinton Dreisbach:** It's called Momentum. It's local, it's just in Durham, North Carolina. My and a co-founder, Jessica Mitch, we formed it after our former bootcamp closed down... And we knew what we were doing, and loved it, so... Yeah, it's the most fulfilling and awesome thing to get to see new developers go from nothing to full, awesome developers. But yeah, all the problems that people are talking about, with not hiring junior developers - I get to see this up close and personal every day. That's the most disheartening thing, seeing people say "Oh, we only hire senior developers", because the people that I see every day grow as developers are going to be the most amazing developers you've ever met, they're just not quite there yet... But they're getting there. But yeah, it's such a cool thing. I can answer any questions...

**Jerold Santo:** How do we bridge that gap? There's obviously a problem, but there don't seem to be any obvious solutions to that problem.

**Clinton Dreisbach:** The easiest way I've seen so far - and this just takes time - is helping companies learn that hiring junior developers and training them is pretty much the best investment they can have. Our industry people change jobs so quickly... But you bring someone in early, and you help train them, and they become a really loyal, really amazing employee, that knows what's going on there as well as anyone.

**Jerold Santo:** \[55:59\] The risk is that the loyalty doesn't actually stick, because people do move around so much that if I'm going to invest three years in a person, and then they're going to go upgrade to a different job, to me that's a loss.

**Kevin Ball:** Well, I think to both of your points - you have to think about it as an investment. Investments have risks. But if we're willing to put in thousands of dollars to recruiting, we should be willing to put in half of that amount to training the people we already have.

**Clinton Dreisbach:** Yeah, absolutely.

**Jerold Santo:** Good point.

**Kevin Ball:** I mean, frankly, I'd say twice that amount. If it costs you $10,000 to recruit a new senior developer, and you have someone who is already contributing, but you can spend $10,000 to upgrade them to a senior developer - it's a no-brainer.

**Clinton Dreisbach:** Right.

**Jerold Santo:** There's an old saying that I'll butcher, talking about investing in training their engineers - what if we spend all this money training them and then they leave? And then the response is "What if we don't spend it, and then they stay?" They're going to suck forever... No, they won't. They'll still get better, but you can see that point there.

**Clinton Dreisbach:** And the other thing past loyalty is I think there's no better way for your senior developers to get better at being senior developers than to train junior developers. \[unintelligible 00:57:08.21\] if you have no one you're teaching?

People ask me all the time, like "Oh, do you get bored teaching the same thing over and over?" You have no idea. I learn something every single day teaching new developers.

**Jerold Santo:** For sure.

**Clinton Dreisbach:** They ask questions that I would have never thought of, there are new technologies that I have to learn... I've grown as a developer more teaching than I ever did previously, and I think that's going to be true in any company if you have your senior developers actively working to mentor people.

**Emma Wedekind:** What does your curriculum include?

**Clinton Dreisbach:** We do JavaScript and Python, so it's a full-stack curriculum. I tinker all the time with it. So we do JavaScript for the first half of the course, and then Python and Django for the second half of the course.

**Emma Wedekind:** And how long is it?

**Clinton Dreisbach:** It's 12 weeks.

**Emma Wedekind:** Oh, nice.

**Jerold Santo:** Full immersion, or part-time?

**Clinton Dreisbach:** It's full immersion, so it's all day long, 9 to 5, 4 hours of lecture, and who knows how many hours of projects every day. I kind of burn them out a little bit. We try and keep it to 60 hours a week.

**Kevin Ball:** The folks back there know how many hours, and they're going "Uh...!"

**Clinton Dreisbach:** Yeah... So they're getting a break right now, because we got to come out here and see this. But I thought it was so cool to have them immersed in the industry. I love \[unintelligible 00:58:14.23\]

**Jerold Santo:** Absolutely.

**Emma Wedekind:** Also, the fact that you brought them here is super-cool, because -- I didn't get to go to conferences until I was well into my first job, so... That's great.

**Clinton Dreisbach:** Yeah. It's cool.

**Jerold Santo:** So do you feel pressure to constantly be updating that curriculum, especially with how fast the industry moves?

**Clinton Dreisbach:** Yeah. I mean, for multiple reasons. I always want them to have the very best of content... And also, for me and the other instructors - it sharpens our skills to constantly be revisiting what we're doing, making sure we're doing it right. But every class there's stuff that people get stuck on, and I go "Oh, I know a better way to teach that, or a better way to learn that."

Yeah, so... There's some pressure, but it's fun to do. I think teaching is hard, but if you have the bug, you never want to stop doing it.

**Jerold Santo:** How can people apply?

**Clinton Dreisbach:** Well, they can go to momentumlearn.com if they're interested, or you can just find me or anyone else around here.

**Jerold Santo:** Very good.

**Emma Wedekind:** Thank you so much.

**Jerold Santo:** Thank you so much! \[applause\]

**Emma Wedekind:** Come on down...

**Jerold Santo:** Come on down... To Chinatown.

**Emma Wedekind:** Well, I was singing the theme earlier, but no one seemed to understand it.

**Jerold Santo:** That's what we're going to do. For our next lightning chat session we're going to get the theme song to play as you come down.

**Emma Wedekind:** Yes.

**Jerold Santo:** Hi, what's your name.

**Henri Helvetica:** Good afternoon. My name is Henri. Henry in French.

**Jerold Santo:** Okay, Henri.

**Kevin Ball:** Bienvenu!

**Henri Helvetica:** Merci been! Is that all you have? \[laughter\] I'm waiting, I'm like "Yeah... And? And...?"

**Jerold Santo:** You've reached the end of what he has.

**Kevin Ball:** \[unintelligible 00:59:49.22\]

**Emma Wedekind:** You actually speak French.

**Henri Helvetica:** Oui, LE Français est ma Lange maternally. I just said "French is my mother tongue."

**Emma Wedekind:** Of habits-tu?

**Henri Helvetica:** \[59:57\] JE suit Canadian et j'habit à Toronto.

**Emma Wedekind:** I have no idea what you've just said. \[laughter\]

**Henri Helvetica:** I said "I'm Canadian and I live in Toronto."

**Emma Wedekind:** Oh, wonderful.

**Jerold Santo:** Okay, very cool.

**Henri Helvetica:** I mean, is this a translation podcast?

**Jerold Santo:** It's going to have to be.

**Kevin Ball:** We can go to Spanish, we can go to German...

**Henri Helvetica:** Okay, un position, un mosquito...

**Kevin Ball:** Puerto hangar Español is quires, Pero...

**Henri Helvetica:** Alright, let's go... I mean, we just flipped the podcast. Okay, so we started? Oh, man, we've just started.

**Jerold Santo:** We're wasting your time here. What do you want to talk about?

**Henri Helvetica:** Okay, so I tend to hang out in the web performance space... So I was like "Oh man, I think people are going to be bored", but I'm here to talk about something that's being worked on right now, which is the JPEG Excel, so kind of new format.

**Jerold Santo:** Okay...

**Henri Helvetica:** For all the web developers out there, images are a huge problem on the web... In fact, actually, for the person who talked about accessibility - the number two issue in accessibility is through images, which is alt text. So images are a problem through and through.

With the JPEG Excel, basically what's going to happen is -- well, essentially what happened... Let me back-track a couple of years ago... Is my time up?

**Kevin Ball:** No, that's the light going crazy... Just keep going.

**Henri Helvetica:** Okay, a couple of years ago, to celebrate the 25th anniversary of the JPEG, the Joint Photographic Experts Group put out a CFP, because JPEG is a format that's kind of always being worked on... So they receive seven submissions, and two are picked. Basically, they're trying to see how we can go about and improvement the JPEG as a format. Essentially, what happened is two were selected. To take the best of both - one is the (I'm going to pronounce it improperly) FIF, which is the Free Universal Image Format, which was being developed by Cloudinary, and the second was PICK, which was another format that was being experimented with by the people at Google.

So the two - the best of both - are going to be used to make the way to this new format, which is going to be called the JPEG Excel.

**Kevin Ball:** And what are the advantages of JPEG Excel?

**Henri Helvetica:** Essentially, with any recent format you're going to get some improved encoding, for sure... But things like responsive web design has been a huge burden on the web, simply because a lot of people just do not get it right, so you end up having a lot of data waste being sent down the pipe to users... And actually by corporations as well, because you get that wrong - that's a service that you have to pump the resources down.

That, and obviously, you're going to have animation, which is also a bit of an issue on the web, because a lot of people do fall back to the grossly oversized GIF... \[laughter\] Yes, I said GIF. And so that encoding is going to be improved... Obviously, we're going to have alpha channels, we're going to have adaptive compression, so essentially parts of the images are going to be compressed a little better than the others, the ones that need it anyhow...

And obviously, it's most likely going to be mostly lossy, but with the best encoding possible at the time... So you have this sort of like CIASI-lossless thing going on.

**Emma Wedekind:** Those are a lot of words that I don't know that much about, but I'm intrigued.

**Henri Helvetica:** Okay, well -- I mean, there's information online, for sure, if you go to (I believe) jpeg.org, but at the end of the day I think most people know images, and most web developers certainly need to work with images. You talked about having constricted data, or...

**Jerold Santo:** Constrained, yeah...

**Henri Helvetica:** ...networks and whatnot...

**Kevin Ball:** One hundred percent.

**Henri Helvetica:** Exactly. If you don't handle images properly, this is where you're going to feel it the most.

**Emma Wedekind:** Your question is probably more pertinent than mine \[unintelligible 01:04:11.16\]

**Jerold Santo:** \[01:04:13.15\] You're wasting his time.

**Henri Helvetica:** Yeah, yeah. All of you. \[laughter\]

**Kevin Ball:** So the question I had, actually - you brought up accessibility...

**Henri Helvetica:** Yes.

**Kevin Ball:** And one of the things that I have seen bandied around is embedding some of that alternate text in the images, so that it's not dependent on the web developer, and it can actually be encoded. Is that something that's included in this?

**Henri Helvetica:** That's actually separate. It's funny you should say that, because I'm preparing a project talk on that... There is a push towards automation of alt text. This is completely separate, but Instagram/Facebook has been doing it for a while. Chrome, in Canary, as an experiment - you can actually get that done right now, as we speak... It's behind a flag, but again, that has less to do with performance, unfortunately.

**Kevin Ball:** Yeah. That feels like something where machine learning image recognition...

**Henri Helvetica:** Oh, it's happening.

**Kevin Ball:** ...is going to be super-powerful and helpful.

**Henri Helvetica:** It's happening as we speak.

**Jerold Santo:** Thanks, man.

**Emma Wedekind:** Thank you so much.

**Jerold Santo:** We appreciate it.

**Kevin Ball:** Awesome, thank you. \[applause\]

\[intro song sample\]

**Jerold Santo:** Come on down... \[unintelligible 01:05:22.06\] We have a few more slots after this one if you'd like. If you're interested, come close, so we have less awkward stalling. Hello! What's your name and what would you like to talk about?

**Jill Burns:** Hi, my name is Jill Burns, and first, I love your podcast.

**Jerold Santo:** Well, thank you.

**Jill Burns:** Great to meet you guys.

**Jerold Santo:** We appreciate that.

**Jill Burns:** I wanted to just mention that I came into coding years ago, but re-entered recently \[unintelligible 01:05:48.23\] I had 18 years as a computer programmer/software engineer...

**Jerold Santo:** Wow.

**Jill Burns:** ...took ten years off, raised kids...

**Kevin Ball:** Full-time job...

**Jill Burns:** Yeah... And moved three times. And then came back in as a software developer again. So the senior -- we had an apprenticeship, I had a mentor which was crucial to the program... But I think it's another way to bring women in, that have had experience... And you know, we've done our learning at one point...

**Jerold Santo:** Right, right...

**Jill Burns:** ...and then just have the opportunity. I'm so excited to be back in the field, actually.

**Jerold Santo:** That's beautiful. What's changed the most from your first time to now?

**Jill Burns:** I think that the database work, for me.

**Jerold Santo:** It's way easier now? Way harder? Way different?

**Jill Burns:** I mean, relational databases into the NoSQL was probably my biggest leap. When I left, I was doing Java and web services, and now it's Node.js, cloud and NoSQL, so... A couple of different jumps. But I started in the mainframe, so going from Fortran in high school, Pascal in college... \[unintelligible 01:07:18.21\]

**Kevin Ball:** Alright, history... I was in scientific computing back in the day.

**Jill Burns:** There you go... \[laughs\]

**Jerold Santo:** What hasn't changed then? You come back, and you're like "What's the same?"

**Jill Burns:** Exactly. I've seen it change a number of times.

**Jerold Santo:** But what hasn't changed? Oh, you're saying everything has changed...

**Kevin Ball:** Has everything not changed?

**Jerold Santo:** I get it.

**Jill Burns:** What hasn't changed...

**Jerold Santo:** Truly there are some constants... Change is the only constant, right?

**Kevin Ball:** Jerold gives me this look, like "You're going to back me up here, right?"

**Jerold Santo:** I just blew up his mind. Did your mind explode?

**Jill Burns:** \[laughs\] I'm not sure if there are any constants... I mean, there are a lot of similarities; I will say there are a lot of similarities. But the basis of who I'm working with is getting a lot more diverse than historically. I draw on a lot of my knowledge from other programming languages and databases...

**Emma Wedekind:** \[01:08:09.26\] How did you get up to speed when you came back in?

**Jill Burns:** Well, you know what - I attended conferences like this. While I was out I did attend conferences. I listened to podcasts...

**Jerold Santo:** Excellent.

**Jill Burns:** ...and I did online training when I could, because it was still a full-time job raising kids.

**Kevin Ball:** Yes.

**Jill Burns:** So yeah, that was it. And then when I started, it was a 12-week apprenticeship, with the option of - on both sides - being hired or not at the end. So that was my 12-week of "Okay, here's your project."

**Kevin Ball:** Yeah, that is the best way...

**Jill Burns:** You've got a few weeks \[unintelligible 01:08:47.15\] code...

**Kevin Ball:** If you can make that happen... I mean, if I'm looking for a job, that's my favourite way to interview, because it's how you learn what this place is going to be like to work with. Because folks will put on their happy face when they're interviewing you, and you work with them for a while, and you discover it is a cesspit. Or other folks, who are not super-jazzed at interviews and don't do it very well, but then you work there, and it's the best place ever.

**Emma Wedekind:** That's how Europe does it. When I moved to Germany, they were like "Oh, you're on probation for six months", and I was like "What do you mean?" And they're like "No, it's a standard." Everyone who generally joins, they're on probation for six months. At the end, either party can walk away. That's a good amount of time to get your...

**Jill Burns:** To know.

**Emma Wedekind:** Yeah. We should standardize that.

**Jerold Santo:** It's kind of a cool idea.

**Kevin Ball:** We absolutely should.

**Jill Burns:** And I did the three-question take-home interview, so... \[unintelligible 01:09:36.17\]

**Jerold Santo:** Oh, you liked that.

**Jill Burns:** Yeah, I got the three questions...

**Kevin Ball:** I think the both sides is key, too.

**Emma Wedekind:** Yes!

**Kevin Ball:** If it's instituted as a company power play, it's terrible. Like "Oh, we're going to be watching you for this first 3 months, or 6 months, and then we decide..."

**Jerold Santo:** "Probation" is a weird word for me.

**Emma Wedekind:** Yeah...

**Kevin Ball:** But if you come in with it saying like -- I do it as a consultant, I do it if I'm looking for a job... Like, "I want to do a test run, and I want to figure out, by working with you, is this a good place or not?" And it's my decision to walk away. And yeah, you could decide if you want me to go too, but you won't. It's my decision.

**Jerold Santo:** "But you won't..." \[laughter\] That confidence... Yeah, there you go.

**Emma Wedekind:** That's awesome.

**Jerold Santo:** Awesome.

**Jill Burns:** That's it.

**Emma Wedekind:** Yay!

**Jerold Santo:** Jill, thanks so much for joining us, thanks for listening to the show, and welcome back to the community after all those years.

**Emma Wedekind:** Yeah, welcome back. \[applause\]

**Jerold Santo:** Okay, I did see another hand poke up, and then it dropped immediately. I'm hoping that hand will go back up again... Oh, here it is right here.

**Kevin Ball:** Yes, yes, yes...

**Emma Wedekind:** Yay. I can't sing anymore.

**Jerold Santo:** Oh... Pointing fingers... Go Emma, sing! Alright, here she comes!

**Kevin Ball:** I think she raised her hand first, but if not \[unintelligible 01:10:45.13\]

**Emma Wedekind:** \[laughs\]

**Jerold Santo:** \[unintelligible 01:10:47.22\] I like that. Hello!

**Wannabe Sick:** Hi!

**Jerold Santo:** What's your name?

**Wannabe Sick:** Wannabe Sick.

**Jerold Santo:** Wannabe. Nice to meet you, Wannabe.

**Wannabe Sick:** Nice to meet you!

**Jerold Santo:** Thanks for coming up on stage with us. What would you like to talk about?

**Wannabe Sick:** I wanted to answer Vanessa's question about whiteboarding - alternatives to whiteboarding...

**Emma Wedekind:** Yay!

**Jerold Santo:** Okay, awesome.

**Wannabe Sick:** ...and what other companies are doing.

**Jerold Santo:** Yeah.

**Wannabe Sick:** I guess, briefly, my background is graphic design. I went to school for design. There are a lot of people I know who are making that jump from design into development. It's kind of natural, right? You're already on the computer...

**Emma Wedekind:** Tangential spaces.

**Wannabe Sick:** Exactly. People are going to ask you to do a little HTML here and there, and next thing you know, you're full-on in development.

**Emma Wedekind:** \[unintelligible 01:11:24.22\]

**Wannabe Sick:** Yes. \[laughter\] So I actually took a career break, and I came back and found out everything changed, and had to quickly get up to speed on how to code... And I end up doing a lot of job hunting... And one of the places that I interviewed at was Red Ventures, and they had a booth here at ATO last year. I met a guy who remembered my name, and when they came out looking for someone to hire, they reached out to me and said "We really liked you. We don't really have a role in particular, but we'd like to talk with you."

\[01:12:06.13\] So they brought me in to do one of those "meet ten people for six hours", it was one of those big interviews... I did have to do whiteboarding, but I sat on a panel for a couple of hours, and they just asked like "Explain what are you good at" and "Why are you here?", and just really try to get an understanding of where my strengths are, and my interests... And then they were able to manipulate the interview to see exactly how I would fit in.

So I did do a whiteboard, I really sucked at it, but they were like "We don't expect you to be good. We know you're going to be sweatin', and we just want to hear how you think. You did well, even though you feel like you did poorly."

**Jerold Santo:** Yeah.

**Wannabe Sick:** So they were very interested, and... I did end up passing on that opportunity, and recently I got employed at another company called Med Think, and then I did another career jump... So I'll be starting at IBM.

**Emma Wedekind:** Yay! Congrats!

**Jerold Santo:** Congratulations.

**Wannabe Sick:** Thanks! Yeah, it's been a long journey.

**Emma Wedekind:** Do you know what team, or what area of focus?

**Wannabe Sick:** Under the cognitive applications as the larger department, and then I'll be doing front-end development for them.

**Emma Wedekind:** Cool! Awesome! What do you think of that interview?

**Wannabe Sick:** It was so cool... It was very cool. At first, I thought -- I'd applied a couple of times before, and I failed, and I was like "I'm not going to do this again... I'm just so tired." But a recruiter found me on LinkedIn, and it was a take-home application. What was cool was that they didn't have a particular goal. They basically gave you a very open-ended task, and they wanted to see how you thought, all the way from the wireframe, UX/UI strategy, into development.

To me, it felt like a personal pet project, so I already went in not having that pressure... And I just went to town on it. I threw in all my XD skills, and my wireframe \[unintelligible 01:14:04.13\] UX, and then into my front-end development, and then even tried to do a little back-end with some Express, which... You know, I was afraid I wasn't going to get it. But when I had the chance to come in and just tell the team - because you have to sit with two or three developers - I got to explain my whole process, and what I was thinking, and why I did it, and just go through all the things that I was really strong about, all the things that I was pretty good in...

And then I think they also kind of stepped back and thought "Okay, she's pretty good with this, but probably not as strong here..." But I didn't feel that pressure. No binary tree searches -- because I have gone through that. That was ridiculous. Fibonacci... I am a designer first, and then developer, so I can draw you a tree, but I \[unintelligible 01:14:52.01\] \[laughter\]

**Kevin Ball:** \[01:14:55.11\] I feel like one of the things that you're highlighting here is this should not be -- if you're looking at your hiring process as an employer, this should not be a judging process. This is dating. I don't go on a date -- I mean, I haven't been on a date in 20 years, but I don't go on a date and be like "Alright, you're 7 out of 10 on this, and a 9 out of 10 on that..." It's looking for compatibility, it's looking for like "Are you the type of person that I want to work with? Are you going to fit well in our team?"

**Wannabe Sick:** Right. And I think that's probably how you can retain talent. Because if I'm coming in knowing I'm going to be looked on, like they're expecting me to do well at what I'm doing well already, then you're just gonna start from a point where you're going to excel. So that's how I feel... I'm pretty excited.

**Emma Wedekind:** \[unintelligible 01:15:38.29\]

**Wannabe Sick:** 13 seconds left...

**Jerold Santo:** Do you want to give a shout-out?

**Wannabe Sick:** To...?

**Jerold Santo:** Anybody you like.

**Wannabe Sick:** My son. I'm going to do a talk tomorrow, and he's going to be here. He's three, and we're going to do a talk about bringing minority children into STEM.

**Emma Wedekind:** I love that!

**Kevin Ball:** Awesome!

**Jerold Santo:** When and where is that talk?

**Emma Wedekind:** Yay! Everyone go watch your talk tomorrow! \[laughter\]

**Jerold Santo:** Yeah.

**Wannabe Sick:** It's room 205, at 11:45 AM.

**Jerold Santo:** Okay. You heard it here.

**Kevin Ball:** \[unintelligible 01:16:02.27\] \[applause\]

**Emma Wedekind:** Thank you so much!

**Jerold Santo:** Okay, that is our time. That being said, if you have a lighting chat you would like to perform -- or is it a performance? I don't know; if you'd like to chat with us, we will be down in the main floor, booth 72. We're mic'ed up, we're ready to continue these conversations, we'll get the timer going, and everything. Any final words from my esteemed colleagues up here?

**Emma Wedekind:** I just want to say thank you to everyone that came up here and put themselves on the spot. I think it sparked some fascinating conversations.

**Jerold Santo:** Ball.

**Kevin Ball:** You all rock! But I want more dancing.

**Jerold Santo:** We all rock... But more dancing. Okay, that's our show, that's JS Party. Thanks for joining us, and we'll see you next week, I probably should see. That's weird though... We'll see you next time! \[applause\]
