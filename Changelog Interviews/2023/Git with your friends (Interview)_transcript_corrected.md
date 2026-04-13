**Jerold Santo:** Recently, we've been overwhelmed by a lot of the crazy, super-cool tools, innovation and just stuff that people have been doing in and around Git, whether it's the Git project itself, or tooling built around it... It feels like there's something new every single week in Changelog News, so we thought we'd get together with our friend, Mat Ryder, who also happens to be a co-host at the Go Time podcast and of Grafana's Big Tent podcast, which is an award-winning podcast...

**Adam Staravia:** Woo-hoo!

**Jerold Santo:** ...and Go Time's an award-worthy podcast...

**Adam Staravia:** Yeah.

**Jerold Santo:** ...and we thought we would just introduce some of these tools and ideas to everyone, and just talk about them. So Mat, thanks for being here.

**Mat Ryder:** Oh, thank you very much. I use Git a lot, so I'm very keen to learn more about this.

**Adam Staravia:** Would you say daily, or weekly?

**Mat Ryder:** It depends if it's every day or every week.

**Adam Staravia:** Okay. Explain.

**Mat Ryder:** Well, if you want to say something happens once a day, you'd say daily. But if it only happens once every seven days, I'd probably opt for weekly.

**Jerold Santo:** The confusing one is bi-weekly.

**Mat Ryder:** Yes.

**Jerold Santo:** Because that can both mean twice a week, and once every other week.

**Adam Staravia:** Two different meanings.

**Jerold Santo:** Who invented that phrase...?

**Mat Ryder:** Yeah... It's not good, is it? We have fortnightly as well, as a term, to mean two weeks.

**Jerold Santo:** I like fortnight. Not the game, but the phrase. The game kind of soiled the phrase, if you ask me, the word... Because now there are two contexts...

**Mat Ryder:** Yeah. Quake did that to me. I used to love quakes, and then...

**Jerold Santo:** \[laughs\] Like earthquakes?

**Adam Staravia:** \[laughs\]

**Jerold Santo:** Quake - what is it, the game?

**Adam Staravia:** It's like the oldest game in the world though, isn't it? It's right up there with --

**Jerold Santo:** Pong.

**Adam Staravia:** Duke Nuke.

**Mat Ryder:** Yeah, we used to play on -- in school we had a LAN party, and Quake 2 was the game we played. And then I used to make levels with my brother using Wordcraft, a 3D World build-a-thing, and it was so much fun...

**Adam Staravia:** Nice.

**Mat Ryder:** ...to be able to like to build levels and then play them with your mates. You just couldn't believe you could do that.

**Adam Staravia:** These LAN parties, did you take a router with you, and did you pick up your entire gigantic tower PC and take it with you? Describe...

**Mat Ryder:** Yeah... Well, luckily, these were in the school library, so...

**Adam Staravia:** Okay.

**Mat Ryder:** Yeah. Because you wouldn't move your computer around back then. It's not like now with your phone. You can't really believe the--

**Adam Staravia:** The internet is your LAN.

**Mat Ryder:** Yeah, exactly.

**Adam Staravia:** The cloud.

**Jerold Santo:** That'd be dangerous, if the whole internet was an all-in-one LAN. Wouldn't we be pretty exposed?

**Adam Staravia:** Well, yeah.

**Jerold Santo:** I mean, NAT's are nice... Again, two contexts for NAT's, especially when you're just saying the word out loud. Let's loop back to Git. How often do you use Git, Mat?

**Mat Ryder:** Daily or weekly.

**Jerold Santo:** \[05:59\] \[laughs\] Well, this is interesting, because you haven't been coding this much lately. This is a change for you.

**Adam Staravia:** Don't out him, Jerold...

**Jerold Santo:** Maybe not recently. Oh, no offence...

**Adam Staravia:** I would ask him for permission first.

**Jerold Santo:** No offence... Is that private information, that you're more of a leader now?

**Mat Ryder:** Well, I'm hoping to get one day promoted back to being an IC, so I can do work again... \[laughter\] Yeah, so I don't use Git -- but honestly, Git was always really complicated to me. And I was "There's so much you can do, and it's really quite complicated." So I tried to always just use the absolute minimum that I could get away with it. That's why I quite liked Git Flow, that used to give you like a workflow where you could -- it'd give you a reason to create a branch, you do your work, and then merge it back in. Yeah, so I would always err on the side of keeping it as simple as possible, because there's so much you can do with Git.

**Adam Staravia:** Yeah.

**Jerold Santo:** Absolutely. And so we're going to talk through some of these tools, and as we go, one of the things that's interesting to me -- obviously, not "Do you use these tools?", because unlikely, because there are so many things, and you like to keep it simple... But having looked at it, seen what it does, thought about it a little bit, like are these things that we, you, me, Adam might adopt, might try? Or is it just a cool kind of triviality that's neat to look at and then move on?

So let's dive into it a little bit... Let's look at the first one, which - it's got that visual aid, it's called Git Heat Map... And this immediately reminded me of like Daisy Disk, or these tools where they search your hard disk, and they show you where the big files are, and they kind of put a map out of wherever the big files are, where most of your storage is across the span of your disk, only this is doing it on your Git repo.

**Mat Ryder:** Is it still file size that it's representing?

**Jerold Santo:** It's based on diff activity. So it's showing you kind of like -- what do you call it? Lines of code that churn a lot, or like the hot files...

**Mat Ryder:** Oh, I see...

**Jerold Santo:** So it's based on the history, and you can also do it to limit to certain users, and stuff, in the history... So the example that is out there in the image that's provided is on Python, which is a project that has a long history of commits... And it's highlighting the files that Guido van Possum changed the most. And so it shows you a layout of that, and like bright red is obviously the hottest, which is configured, and then the Doc folder, and then test and lib... So some of these things are kind of -- I don't know, they're the ones that you would guess. But I wonder if there's actually insights that you'd find, like "Holy cow, this particular file--", which I have found over time in certain repos there are certain files that are the really active ones.

**Mat Ryder:** Yeah.

**Jerold Santo:** And lots of people touching that file. And there are other ones that -- you know, actually, config is kind of surprising to me, but maybe inside Python it's different from what I'm thinking of.

**Mat Ryder:** So you've got two dimensions here, though... You've got the size of the box, and you've also got the colour of how red it is. So do we know what they are? What's the size mean? Versus the -- you know, the colour is obviously the most changed, I guess... But what makes something bigger or smaller? Or is it also just the same thing? It might be, by the look of it.

**Adam Staravia:** Well, it says you can choose the hue that you want the chart to use for highlighting. \[unintelligible 00:09:23.27\] maybe the activity, maybe this is something you can actually fine-tune what it actually is representing... I find tools like this are like "How do you use them? What makes them insightful? Is it an individual using it? Is it an engineering manager sort of looking at, to sort of get--" Because they're less in the code. Maybe you can speak to this, Mat, because you're less into code lately... You're less in the details, and so maybe you use something like this as a way to sort of like grok the bigger picture. Or maybe this is great for a presentation to the Linux Kernel, for example, and you're at LinuxConf. I don't even know if it's a real thing or not, but like, some sort of conference focused on Linux. Like, how fast is Linux moving? What is changing within the Linux Kernel? Who's doing it? Etc.

**Mat Ryder:** \[10:10\] Yeah, I can't imagine the amount of stress that goes in trying to do the presentations at LinuxConf, though... Like, trying to just connect to the projectors with Linux machines... No, thanks.

**Adam Staravia:** Yeah, it's an absolute shame. Well, you have to use the non-free packages or whatnot to do that. So that may be against the rules to the conference, even. Somebody that's like a super free software person, they're like "No way, man. Not going to use it."

**Mat Ryder:** Yeah, I went to FOSDEM recently, and that's obviously open source, and they're kind of allergic to having anything that's not open source focused, of course, there. But one use case I could think for the Git Heat Map is to make sure that you have good test coverage on the things that are changing the most... Because in a way, that's where you need more stability, where you're changing the most. So I feel like a kind of mashup of that and test coverage could be very useful to see "Are we definitely covering these things that we are editing all the time?" maybe.

**Jerold Santo:** Yeah. I can also see it when you're coming to a new project that's existed for a long time, and you're just trying to familiarize yourself with the project, who's working on what, and which files are they working on the most. So I did look up the way that this thing works, and so it's a two-step process. So it basically scans through the entire Git history using git log, and then takes that history and compiles a few database tables, which tracks files, commits, the author, and then the relationships between those things.

And then the second step is taking that database, querying it to create the tree map, and the query is based on both the size of the file, and then the total number of changes to the file. So there are two dimensions. And so the colour, I think, is based on how hot it is, meaning how often it changes, and you can limit that to certain authors, like I said... And then the size of it in the actual tree map is how big the file is, or the folder structure is.

I think I would only use it in that context, if I'm like new to a team, and I have a repo that maybe has years in history, and I want to quickly familiarize myself with it... Running the tests is a good first start, and then maybe just throwing this thing in there... Depending on how long it takes to operate, you can get a tree map real quick.

I know I've also done like CLOCK, count the lines of code... And that will spit out kind of a report on a project of how many lines of code there are in each kind of programming language, like how much HTML there is, how much CSS, how much is Python. And that also helps you familiarize yourself pretty quickly. Other than that, it just looks cool, and so it's probably fun to build...

**Mat Ryder:** So on that then, how do you feel about the fact that it looks cool? Is that a good enough reason for you to have it in? Because to be honest, even if it was just an aesthetic thing, I feel like sometimes that's okay. It's like, "No, this is nice to look at, it's nice to have. We think it's cool. We kind of like it, we feel good about it." Is that a good enough reason, Jerold? Or are you like "No, give me facts!"

**Jerold Santo:** It was good enough for me. I mean, I put it on Changelog News, and I'm like "This thing's cool." Sometimes it's just like, surely this person -- by the way, written by Jonathan Forsythe, so shout out to Jonathan...

**Mat Ryder:** Well done, Jonathan.

**Jerold Santo:** He was probably just scratching his own itch. He probably thought "This doesn't exist. It would be cool." I always do enjoy popping open Daisy Disk, or CleanMyMac X or whatever, and seeing that layout of my system's hard drive, and like where the big files are... And so it's like "Well, can I take that idea and apply it to Git?" It's cool.

**Mat Ryder:** Yeah, it's definitely cool. I also like doing that with Daisy Disk. In fact, I've found lots of big audio files, which were -- when we record these podcasts, we record our own audio locally. So I have lots of audio files of just my side of the conversation. Unfortunately, they also somehow make it into my iTunes, and so sometimes when I'm shuffling music... Like, I might be in the bath, and I've got music on, and then it's playing music, and then it comes to one of these tracks...

**Jerold Santo:** \[14:12\] Right.

**Mat Ryder:** ...and it's just my side of a conversation. And I just have to --

**Jerold Santo:** You could have like the Greatest Hits album with that. Mat Ryder's Greatest Hits...

**Mat Ryder:** Right.

**Jerold Santo:** You know, he just talks to himself, because -- you know, there's this interesting phenomenon now... I don't know if you guys have been out on the streets at all... But when you're out on the streets, people just talk into the air. And when they do it now, you can no longer assume that they have some sort of mental disorder, or a problem. Because a lot of times they actually have like the tiniest little Nearpod in, or something, and they're not just being insane. They're actually just having a conversation on the phone, or something. And it's really strange.

**Mat Ryder:** Yeah, this actually is perfect for me, because I am the person that walks around just saying things out loud... And I don't sometimes think -- like, sometimes, if I'm going to have a difficult conversation, I'll sort of like run it over in my head, and sometimes I'll say it out loud. And I've noticed a couple of times people looking, and then I just like slowly put my hand up to my ear and just say, "Okay, thank you. Bye!" and pretend I was on the phone.

**Jerold Santo:** \[laughs\] That's a pro tip right there.

**Mat Ryder:** Yeah.

**Adam Staravia:** That is a pro tip.

**Jerold Santo:** I like that.

**Adam Staravia:** A little speck of brain science for you... It is totally okay to talk to yourself, even out loud.

**Mat Ryder:** Oh. Thanks.

**Jerold Santo:** In public?

**Adam Staravia:** Yeah, any-- I mean, there's etiquette. I mean, pick your place. But you are not suffering from sort of any mental condition if you talk to yourself. Now, there are certain circumstances where it goes too far, but any normal person who speaks out loud to themselves - it's just a way that you sometimes process your thinking. Everybody's different with how they think, and so you may be a person who thinks out loud, and has to say it out loud to really believe it as fact... And so I'm here to tell you it's okay.

**Jerold Santo:** And I don't disagree with that, but I'm here to tell you that when you do it in the public places, that you will look like you're insane. That's all I'm saying.

**Adam Staravia:** Truth. Truth.

**Jerold Santo:** And then you just say "Goodbye!" and you put your finger up your ear, and you look totally normal again. So I learned that today. TIL.

**Adam Staravia:** That is a good pro tip, Mat. One thing I'm noticing is the time to generate the database. Linux is one of the repositories, Python was one of the repositories used... And the commits on these repos are tremendous. I mean, more than a million on Linux, a little over 100,000 on Python, and the time to generate the Git log, the Git log size... And one of the things that Jonathan mentions is wanted features, which I think is pretty cool. Obviously, faster database generations in there, submodule tracking, rendering filters, other things... I think this sort of those things where you're like "Should this be in Git?" Probably not, right? Like, you don't want Git to be muddied with this kind of feature. So this lives in user land, and is this the best one in user land? And if so, how does this kind of thing get support, to not die?

**Jerold Santo:** Great question. I mean, I think it's the only one I've ever seen. I'm not saying it's the only one in user land. Furthermore, I think with typical open source, don't you just have to inspire people to collaborate with you? Like, it has to be interesting or good enough to get that grassroots support of like "Yes, submodule tracking would be amazing. I tried this. My project has submodules, and it completely ignores them, but a lot of the stuff is in there, so I would love to have that. How can I help out?" There's really no other way that these kinds of projects, which really are kind of like scratching an itch, and there's no business around this... Like, this is a small-scoped thing that can really get support, unless you inspire other people to just want more from it, and then they help out.

**Mat Ryder:** Yeah, but look at Daisy Disk. I mean, that's, I think, a paid app, or it has at least paid features, doesn't it?

**Jerold Santo:** Yeah.

**Mat Ryder:** So if there is a real business use case out of something like this, then it does have a potential future.

**Jerold Santo:** Yeah, maybe.

**Mat Ryder:** \[17:53\] But I kind of love that it's play. It's like, we play a lot, and then sometimes there are opportunities that come out of that play. And this is the thing a lot of software teams forget about, I think. They get very serious, and you forget that actually, you've got to be able to be creative, and just try things, and do things because you want to, or you just think it's cool. Just thinking something's cool is a great reason. If someone on one of my teams comes and says, "I've got this idea. I don't know where it fits, or anything, I just think it's cool", that's really compelling for me, especially because they're so motivated to actually do it.

**Jerold Santo:** Right... It's harder than the other way around, you're going to them and saying, "You know what would be cool?" and then you're telling them, and they're "Okay, I'll do it, because Mat wants me to, but..."

**Mat Ryder:** "Sure..."

**Jerold Santo:** But less likely to--

**Mat Ryder:** "Sure, that's cool, granddad..."

**Jerold Santo:** \[laughs\]

**Mat Ryder:** They just think I'm their granddad.

**Jerold Santo:** Right...

**Mat Ryder:** And I haven't even got any kids, so how can I be their granddad? I mean, think...!

**Adam Staravia:** Inquiring minds want to know, Mat. They do want to know.

**Mat Ryder:** Yeah. You can't do it, I think...

**Adam Staravia:** That's a great point though, the play aspect... Because a lot of things happen when you do play. I mean, obviously, your mind is different. It's in a different mode. Sometimes, as you said before -- I may be outing your potential unpopular opinion, and I won't say it... But when you make a plan, it could be too rigid. I'm dropping some hints there...

**Jerold Santo:** He's totally going to say it... \[laughs\] He's going to ruin it.

**Adam Staravia:** I'm not going to ruin it.

**Jerold Santo:** Okay.

**Adam Staravia:** You know, when you play, there's freedom, right? There are no constraints, there are no guardrails, necessarily... It's like, "Where can I go? Where can I explore? What should I do?" And then maybe out if it comes fruits, and maybe that can be a business, if you really wanted it to be... I mean, I think there are examples of large things in our world -- like, Flickr I think was a game at first, before it was like the photo sharing 1.0 version of Instagram, essentially.

**Jerold Santo:** Right. And Slack was supposed to be a communication tool while they built a game.

**Adam Staravia:** See?

**Jerold Santo:** The same teams.

**Adam Staravia:** Yeah, they were just playing.

**Jerold Santo:** Are they ever going to make that game?

**Adam Staravia:** Probably not. It's done.

**Jerold Santo:** Too busy making very successful companies.

**Adam Staravia:** Yeah, they've let it go. But they may play The Sims, which is a good transition to simulating--

**Jerold Santo:** Pooh...

**Adam Staravia:** This has actually sparked my interest, because I was like, I love to have permission to mess up, and Git Sim is the next one - visually simulate Git operations in your own repos. I think that's pretty cool, because you can think of like "What would happen if I branch? What would happen if this happened here? What would happen if I rebase that over here?" And you can sort of like have this fictitious world, this potential future, and just erase it. But isn't that kind of what Git does anyway? But this gives it to you visually. That's the difference.

**Jerold Santo:** Yeah, this visualizes it for you, so you can understand what's going to happen. And also, it's completely safe. With Git, you know that 99% of the time it's in there, right? Like, no Mater what you do. There are circumstances where you can lose data, but most of the time, even if you thought you've lost something, it's in there, because of the way it works. But you have to find out how to get it back, and that's like a huge time sink, and can be very anxiety-ridden, and all that.

**Adam Staravia:** And dangerous. It's like running in production.

**Jerold Santo:** Yeah. But with this, not only does it visualize it for you, which is super-cool, but it also never does it. Right? So it's kind of like a dry run in that way; the author of it did describe why it's better than dry runs, but I've lost the blog post. All I have is the repo at this time...

**Adam Staravia:** I do a lot of Syncing in my network, and in some cases I do deletion through Sync...

**Mat Ryder:** You do a lot of arse-what?

**Adam Staravia:** Syncing. Sync.

**Mat Ryder:** Is that like tattoos on people's backs?

**Adam Staravia:** Sure. Sure, Mat. Sure. \[laughs\] Arse inking...

**Mat Ryder:** Nice.

**Adam Staravia:** Touché.

**Jerold Santo:** Is this a hobby, or are you trying to get a new gig going?

**Adam Staravia:** None of the above. None of the above.

**Mat Ryder:** Can you do me one?

**Adam Staravia:** Let's go with the flag I'm gonna mention here, okay? So when you Sync, especially if you're going to delete, you're moving data to or for, from a place, and it's like "Well, I can use -n and just kind of see what it might do." And it will go and do that whole thing. And that's my favourite thing; especially with that kind of like dangerous tool, you need sort of a simulation zone, so that you can simulate.

**Mat Ryder:** \[22:15\] Yeah. So this is interesting... Could you have this tool, but for real as well?

**Jerold Santo:** Well, once you do the tool, then you do it for real.

**Mat Ryder:** I see.

**Jerold Santo:** Or you mean you want to visualize it as it goes?

**Adam Staravia:** Is your question, Mat, you simulate it, like the results, and just say, "Okay, do it" button?

**Mat Ryder:** Yeah, I guess so.

**Adam Staravia:** Is that what you're saying?

**Mat Ryder:** Yeah. It's like commit. It's like "Yeah, that looks good."

**Adam Staravia:** Yeah. "It looks good. Do it." Yeah.

**Jerold Santo:** Probably it can... So I did find the part where it says, "Why aren't dry runs good enough?" Because Git does have a dry run feature, which is the Sync one that you described there, where it will just tell you what it's going to do. And the author of this, which we should shout out as well...

**Adam Staravia:** Arse inking, Mat...

**Mat Ryder:** Yeah, I can't unheard it now...

**Jerold Santo:** I know...

**Adam Staravia:** I do a lot of R-syncing!

**Jerold Santo:** And then when you plant a flag, I'm picturing a tattoo artist with a flag...

**Adam Staravia:** Arse inking...

**Jerold Santo:** So this tool by Jacob Stomach from the Initial Commit team, which is a team that does Git things... And he writes that there's a dry run flag in Git, which is -n also, so maybe that's a standard, or at least an idiom... It enables you to get some idea of how the command will affect the state of the repository, but he says "These commands can be useful, but not all Git commands have them." So Git has all these sub-commands, and they don't all have dry runs. And he says, "And the purely text-based output can be quite sparse, as is typical of Git's command line interface. Moreover, many people out there are visual learners, and could benefit greatly from a visual approach to simulating the impact of a Git command before running it." So imagine this tool, Git Sim, as if it's a dry run, that has complete coverage of the subcommands and visualizes it for you. This one, I could argue - put it into Git. This is just a better user experience for dry runs, potentially.

**Mat Ryder:** Yeah, this would be very useful, and probably would satisfy some of my fears here, with Git commands just being too complicated, and I don't really have the confidence that I really know what it's going to do... Because it's very abstract, and can be quite surprising, the effects, if you're not really \[unintelligible 00:24:23.15\] with Git... So this would give a level of confidence, for sure. It'd be like "Okay, so you've typed this in. Now, here's a picture. Is this what you meant?" And you're like "No, absolutely not. You've just saved me a lot of embarrassment. Thank you." Or the other way around.

**Adam Staravia:** Yeah. The --animate is a pretty cool flag, too. It animates what's going to happen. Like a presentation. That's pretty cool.

**Mat Ryder:** Yeah. It looks good, too. They have GIFs on the -- I don't know, they might not be GIFs actually, but they have video animations on there. I just don't want to get letters of people saying "That's not a GIF. He doesn't know what a GIF is..."

**Jerold Santo:** At least you pronounced it right...

**Mat Ryder:** Good point.

**Jerold Santo:** So points for that.

**Mat Ryder:** Thanks, Garrett...

**Adam Staravia:** It seems to be a .mp4, just to be clear, Mat...

**Mat Ryder:** Thank you. We have to be a bit pedantic, because I do get letters when I say -- sometimes I'll say something and like just being silly...

**Jerold Santo:** Which ones?

**Mat Ryder:** Oh, there's lots of them, in different orders, depending on what they want to write.

**Jerold Santo:** Okay. Daily, or -- would you say you get those daily, or weekly?

**Mat Ryder:** Yeah, I would. I would say that. I wouldn't say moreover; someone said moreover earlier. Furthermore, I don't think I've ever

said --

**Jerold Santo:** Well, I was reading verbatim from a blog post. So you can take that up with Jacob Stomach. I'll let him know.

**Mat Ryder:** Alright, Jason. Just come here, Jason.

**Adam Staravia:** Jacob.

**Mat Ryder:** Sorry, Jacob.

**Jerold Santo:** Alright, so that sentence had a bug in it... Which leads us to our next tool, Git Bug.

**Mat Ryder:** Oh, these links are brilliant. This is professional.

**Jerold Santo:** Yeah, you're really working with pros here today.

**Mat Ryder:** Yeah...

**Jerold Santo:** \[25:53\] This one - I absolutely love this concept. So Git Bug, written by Michael... Mure. I think that's how you pronounce his name.

**Mat Ryder:** Good name.

**Jerold Santo:** Basically, it's but a bug tracker in Git. It's fully embedded in Git. You only need your Git repo to have a bug tracker. So anywhere your repo goes, the bugs are right there. It works offline, no vendor lock-in, it's fast... I'm just reading his bullet points now. It doesn't delete your project, it integrates with your tooling... So that's what's cool about it, is it bridges over to GitHub issues, to GitLab, whatever they call their issues, to JIRA, if you're in hell already... I mean --

**Adam Staravia:** Oh, boy. \[laughter\] Geez, Jerold...

**Jerold Santo:** Sorry... No love lost for JIRA...

**Adam Staravia:** Say it like you feel it, man. Say it like you feel it.

**Jerold Santo:** Oh, I never liked that tool. I don't know anybody who does...

**Mat Ryder:** I feel sorry for people building it.

**Jerold Santo:** If you do, send Mat a letter.

**Mat Ryder:** Oh, yeah. Please.

**Jerold Santo:** If you love JIRA, let Mat know.

**Mat Ryder:** Send it to Jason, he doesn't exist. I got his name wrong.

**Jerold Santo:** \[laughs\] There you go. But this is really cool. I mean, how do you track your bugs, Mat? I just don't write any. That's kind of the way I do it. But how do you do it?

**Mat Ryder:** In GitHub, as issues. But actually having it in Git - and I assume there's a text file, or something, or some data file where they store this... And what's quite nice about this, I guess, is with a commit, you can also fix the bug, and then that all gets pushed at the same time. And because it's in Git, it's always correct. So if you go back and check out an old branch, you'll see the bugs that exist for the previous commit; you'll see the bugs that existed at that time. So I think that's really clever.

**Jerold Santo:** Yeah, it's super-cool. The way this is built out, it models Git's way of working. It works like Git works, it's just inside your Git repo. It has a CLI, so you interact with it from your CLI, both adding bugs, reading bugs etc. And then it also has this little web UI built in, that you can launch and just run locally, which kind of gives it a GitHub-style issues list, with filters, and open and closed... I'm pretty impressed by this tool, actually. I think Michael did a perfect job with it.

**Adam Staravia:** What about tracking in production, though? How does that happen? Where does it get the reports?

**Jerold Santo:** Oh, error tracking?

**Adam Staravia:** Yeah. Like, is a bug in there? I mean, it's kinda like the same role, isn't it? Bug tracker, error tracker...

**Jerold Santo:** How do you do it, Mat, over there in Grafana?

**Mat Ryder:** Well, I was going to say, if there's an error, or a bug, or whatever, you just open it and I guess commit it, right? It exists at that point in the codebase.

**Jerold Santo:** Well, think about our error tracker, Adam, in Sentry. There's a ton of errors in there, and some of them turn into bugs that we open on GitHub issues. But if every error turned into a bug, then my no bugs command would be way off. Like, there are so many errors, that only -- and thousands of errors can represent the same code deficiency as well.

**Mat Ryder:** Yeah, depending on the scale.

**Adam Staravia:** Well, one important thing that you do though with that is like you track commits to deploys, to errors, and I guess to bugs. And I'm just wondering if you had that full circle, that comprehensive look... Because it seems it can be one-sided, unless it gets that sort of other source of truth, right?

**Jerold Santo:** I'm not following. Say it again in different words.

**Mat Ryder:** It can mean a different thing as well, if you can.

**Jerold Santo:** \[laughs\] At Grafana we have error budgets, actually. So this is a concept that - if anyone's not familiar with it, you really should be, because it's so good.

**Jerold Santo:** Okay.

**Mat Ryder:** It's basically like we're allowed to have a certain amount of errors. And I've worked at a place before where we had a sort of non-technical -- that's the politest way I could say it, is a non-technical CTO... He's an idiot, put simply.

**Jerold Santo:** \[laughs\] And he said "No, there shouldn't be any errors. Like, why are there errors? Why are there bugs? We shouldn't have any bugs, and no errors." Genuinely, that was his position.

**Jerold Santo:** Neither of either. Okay.

**Mat Ryder:** \[29:58\] Yeah. And like, okay, sure; it's almost like you don't really know what you're talking about, frankly, if that's your position. And so in the real world, errors happen all the time, and you're allowed a certain level, a certain budget that you can spend. And that means you can be creative and flexible, and do things, and make mistakes. So you have the flexibility to, within the Los --

**Jerold Santo:** Thresholds... Exactly.

**Mat Ryder:** ...you're allowed to take some risks. Because if you really don't want anything to ever break, ever, you have to do a lot more work, and you can be a lot more free if you're allowed for there to be some errors, as long as you jump on it and fix them when they happen...

**Jerold Santo:** How are those measured? Is it like errors per lines? Or is errors per week? Or how does that play out?

**Mat Ryder:** Yeah, it'd be like failed HTTP requests, depending on what it is. It's like a certain number of those could fail before you consider you've got a problem.

**Jerold Santo:** I see.

**Adam Staravia:** A threshold. Sure.

**Jerold Santo:** That is a cool idea.

**Mat Ryder:** I think the same applies for incidents.

**Jerold Santo:** And it's just realistic, too. It just accounts for reality, and it lets you move forward, while still maintaining it and not letting it get out of hand, which is what you're trying to really fight against, is like all of a sudden --

**Adam Staravia:** Are you seeing g-i-t get out of hand, or g-e-t, get out of hand?

**Jerold Santo:** That's open to interpretation.

**Adam Staravia:** Okay.

**Mat Ryder:** Well, that's the thing - not in my accent, it's not... Because they're very different when I've pronounced those two words. And I think the G-i-t, that project, is a play on words in a US accent. I think it's like get, it's it?

**Jerold Santo:** No.

**Adam Staravia:** Nah.

**Mat Ryder:** Is it not? \[laughter\]

**Jerold Santo:** No, it's Git.

**Adam Staravia:** \[laughs\] It's Git.

**Mat Ryder:** What do you mean?

**Jerold Santo:** No, it's because Linus wanted to make a joke on the term, that it's a tool for gets. Like, isn't get kind of a pejorative over there?

**Mat Ryder:** Yeah. Is that what it was?

**Jerold Santo:** Yeah. He pretty much said that, that it was supposed to be -- I should pull up the quote.

**Mat Ryder:** Oh... I thought it was like in a Texan accent, it was just like someone saying "get".

**Adam Staravia:** Do you want to hear something funny?

**Mat Ryder:** What, your accent?

**Adam Staravia:** I'm a transplant Texan. I wasn't born here. Now, I knew a guy - I still know the guy, but I knew a guy... He was describing the parade going through downtown. And he was telling me that it was going "Dunstan." And I'm serious with you. This was when I first moved here, so I had an excuse... And I was like "What are you talking about? What is Dunstan?" He's like "Dan-tan." He kept saying it. Furthermore, he got louder. "Dan-tan. Dan-tan!" I'm like, "Can you please explain in different words?" And he finally says, "Downtown." \[laughter\]

**Jerold Santo:** "Oh, so you can say it."

**Adam Staravia:** "Finally, you can say downtown..." \[laughter\] Seriously, man... Like, "Dunstan" for like three minutes here, and I'm asking you "What are you talking about?"

**Mat Ryder:** Well, that's amazing.

**Jerold Santo:** Okay, I have the final word here... And this is hilarious, because it shows how small of a world it is. I googled it, or I technically DuckDuckGo-ed it, if that's a thing...

**Mat Ryder:** You Duck Duck Went.

**Jerold Santo:** I went there... And I found how Git got its name. And this article - this historical article is written by none other than Jacob Stomach from Initial Commit?

**Mat Ryder:** What?!

**Jerold Santo:** Yes, he wrote this.

**Mat Ryder:** Jason. He's back.

**Jerold Santo:** He's done all of this history here, and he says "Okay, when Linus Torvalds made his initial commit of Git April 7th 2005, he supplied this message: "Initial revision of "Git, the information manager from hell." That's the subject. And then he provides the deeper cut in the --

**Adam Staravia:** The content.

**Jerold Santo:** Yeah, what do you call it?

**Adam Staravia:** The body.

**Jerold Santo:** The body of the commit message.

**Adam Staravia:** Sure.

**Jerold Santo:** It says "Git, the stupid content tracker. Git - it can mean anything, depending on your mood. One, random three-letter combination that is pronounceable, and not actually used by any common Unix command. The fact that it is a mispronunciation of get may or may not be relevant."

**Mat Ryder:** Hello!

**Jerold Santo:** Well - it may not be relevant, Mat.

**Mat Ryder:** \[33:55\] But it may be...

**Jerold Santo:** "Two. Stupid, contemptible and despicable. Simple. Take your pick from the dictionary of slang. Three. Global Information Tracker." So it could be an acronym. "You're in a good mood, and it actually works for you. Angels sing, and a light suddenly fills the room." And the fourth one - oh, I can't actually say the fourth one. We'll have to bleep it out like crazy.

**Mat Ryder:** Beep!

**Jerold Santo:** You have to look that one up, friends... He says "This is a stupid, but extremely fast directory content manager. It doesn't do a lot, but what it does do is track directory contents efficiently." So there you have it, from the horse's mouth. The slang "git" may or may not be relevant.

**Mat Ryder:** Wow... Okay, good. Thank you.

**Jerold Santo:** Yeah. So thanks for that, Jason.

**Mat Ryder:** Huh... I wonder what "Dunstan" would think of that. \[laughter\]

**Adam Staravia:** Dan-tan

**Mat Ryder:** "Hey, Dan, have you seen Thies? You on' love it!" You know, for example...

**Jerold Santo:** That's pretty good.

**Mat Ryder:** I don't want to insult anyone.

**Adam Staravia:** My other friend - I give you one more...

**Mat Ryder:** Other friend... I like you just admit you've only got two. \[laughter\]

**Adam Staravia:** I said "My other friend." My other friend.

**Jerold Santo:** Wow.

**Adam Staravia:** He also had an experience on his first entry upon Texas. He came from Montana.

**Mat Ryder:** Okay...

**Adam Staravia:** Now Montana is, you know, Montana, as you may know... Now, he drove into town, and there was somebody power-washing something at the gas station. And when he drove over the power wash - do you know what a power washer is, everybody?

**Mat Ryder:** Yeah...

**Jerold Santo:** I do, I think...

**Adam Staravia:** Just confirming.

**Jerold Santo:** I feel like I do, yeah.

**Adam Staravia:** Right? Power washer. He's power-washing whatever it might be. And there's a lot of pressure in that line. And this person drives over the power washer's hose, and the guy yells at him. He says "There's 5,000 PSI there, man. It'll blow up." \[laughter\]

**Jerold Santo:** Dan-tan said this?

**Adam Staravia:** "There's 5000 PSI in there, man... It'll blow up." That's what he said. Like, as if you drove over this pressure washer's hose, because it had such pressure, it would blow up.

**Jerold Santo:** Well, that's a public service announcement, if you ask me...

**Adam Staravia:** Just so you know. Now, it did not blow up. To this day, we laugh at that.

**Mat Ryder:** Yeah. Why is that? I don't get this... You can cut this bit out, but I just want to know, just for my own sanity...

**Adam Staravia:** I'm going to tell you why - because that was the first experience; it wasn't like "Hey, Welcome to Texas." "That's 5000 PSI. It'll blow up." It wasn't "Hello. Welcome. Good to see you. Get your gas here. Come get some snacks inside", or whatever. It was "That's 5000 PSI. It'll blow up!" \[laughter\]

**Jerold Santo:** I'm over here wondering how many times we can get Adam to say that.

**Adam Staravia:** Two more times. Two more times. I will say it on command in the future, too.

**Mat Ryder:** Amazing.

**Adam Staravia:** Just say "Do the bit" and I'll just do it.

**Jerold Santo:** Well, speaking of blowing up - this Git UI project sure is blowing up on the scene...

**Mat Ryder:** What is Git UI?

**Jerold Santo:** Git UI is a blazing fast terminal UI for Git, and it's written in Rust... Which brings me to a sub-topic that I want to ask you about, Mat, soon. But let's talk about Git UI first. Written by a guy whose handle is extrawurst. So he's not just the worst, he's the extra-wurst... But maybe the sausage kind, I don't know.

**Mat Ryder:** Yeah, it looks wurst, doesn't it?

**Jerold Santo:** It's wurst...

**Mat Ryder:** Extra-wurst...

**Adam Staravia:** Wurst...

**Mat Ryder:** "You know, it's like normal wurst, JA, but this is a bit the extra-wurst, so don't worry about it." By the way, I do that German accent to Germans, and they go "What's that?"

**Jerold Santo:** It's just good?

**Mat Ryder:** No. It doesn't sound German to them.

**Jerold Santo:** Oh, it's so bad that they don't even know.

**Mat Ryder:** Yeah. Whereas everyone else is like "Oh, that's a good German accent." So I just think it's not

**Jerold Santo:** I was about to give it a compliment, because I don't know...

**Mat Ryder:** Yeah.

**Jerold Santo:** Okay. Alright, so here's extrawurst's description, or why he made this tool.

**Adam Staravia:** No, you've got to do it right, Jerold. EXTRAMURAL!

**Jerold Santo:** Mat, do you want to read this in the German accent for us?

**Mat Ryder:** Yeah, I'd love to.

**Jerold Santo:** It's in the doc there. The "I do most of my Git work..." That one.

**Mat Ryder:** "I do most of my git work in a terminal, but I frequently found myself using git GUIs for some use-cases like: index, commit, diff, stash, blame and log. Unfortunately, popular Git GUIs all fail on giant repositories or become unresponsive--" I've lost the accent. It went a bit French.

**Jerold Santo:** \[38:13\] It did. It also sounds like -- the way you do it sounds very condescending as well, as if the person's like a complete idiot who's saying it.

**Adam Staravia:** Like you're definitely making fun.

**Jerold Santo:** So we should leave that in, but we should back that out and say, "This is totally cool, extrawurst. We don't think that you're the way Mat's portraying you right now."

**Mat Ryder:** No, I'm just doing my German accent, extrawurst.

**Jerold Santo:** That's right.

**Mat Ryder:** There's a stereotype that German people don't have a good sense of humour, and it's one of those that I don't know where it comes from, because every single person I've met from Germany has like an extrawurst kind of sense of humour. Like, it's feel-good.

**Jerold Santo:** I love it. So hopefully, our friends in Germany will appreciate that... But to read it in terms that we can all understand here, he does say that a lot of the Git GUIs fail on giant repos and become unresponsive and unusable, so he built this, it's in the terminal... "Would you use it?" is the question. It's written in Rust? I know, Mat, it's not written in Go... But would you use it anyway? Because a lot of us say, "Hey, I like to keep it simple. I like to stay in my terminal." I'm in the same way. Furthermore, I'm going to shout out one Git GUI here near the end... But mostly, I just use the Git command line, like you do, Mat. But what if you had more at the command line? You don't have to leave your terminal, and it's not going to choke on the Linux repo, for example; would you use this? Because it looks pretty sweet.

**Mat Ryder:** Well, I feel like I need to come out now and tell you that I actually use GitHub Desktop...

**Jerold Santo:** What?! You said you don't use the terminal. \[laughs\]

**Mat Ryder:** No, no, no. I said -- yeah, because it's like really complicated. I avoid complicated stuff. This I like because --

**Jerold Santo:** I must have misheard you.

**Mat Ryder:** Yeah, we can go back and check the recording, mate, if you're calling me a liar.

**Jerold Santo:** Yeah, do that little rewind sound...

**Mat Ryder:** \[rewind sound 00:40:00.18\] Hello! Now I'm back to doing this accent again, so...

**Jerold Santo:** No, no, go back further! Go back further! \[laughter\]

**Mat Ryder:** But what I like about this is it reminds me of early computer interfaces, like really early MS DOS type. I used to do Basic when I was a kid, and stuff... So it has this real retro feel, which I really like. But kudos to writing it in Rust, because I feel like for the times when you really need performance like this, in this sort of case, I think Rust is a great choice.

**Jerold Santo:** Okay. So you're not offended by that.

**Mat Ryder:** No, no.

**Break:** \[40:44\]

**Jerold Santo:** So the sub-topic then... So language support, or languages these tools are written in, and therefore distributed in - we have two in Python. That was the Heat Map and the Git Sim. This Git Bug is written in Go. Git UI, written in Rust. The next one we're going to talk about, if we get to it, Git Branchless, also written in Rust... And that got me thinking --

**Adam Staravia:** I still can't tell if you're saying "get to it" or "git to it." I mean, you're really getting me here.

**Jerold Santo:** If we do it Dunstan...

**Adam Staravia:** Did you see that, Mat? You liked that one, didn't you? You're really getting to me...

**Mat Ryder:** You're really getting to me...

**Adam Staravia:** I'm sorry, I had to pun it out there...

**Jerold Santo:** Fair enough...

**Adam Staravia:** Install I think is all that matters, right? I mean, in the end.

**Jerold Santo:** Well, that's the question. For me, it is. For Mat, I wonder if you're feeling like maybe Rust is starting to eat Go's lunch for command line tools...

**Mat Ryder:** Well, I mean, first, I think - yeah, it's about what's the easiest thing to run. And if it's Python, and I've got some weird, bored Python thing, and I have to fix it or something, then that's a big barrier for me. But if Python is your bread and butter, then I feel like that's okay. I just don't use it enough that I have any confidence in it. So I do like that you get single \[unintelligible 00:43:28.08\]

**Jerold Santo:** Yeah... The Python one gives me pause as well, just because I don't know if it's going to go right.

**Adam Staravia:** Yeah. Can you mention -- you do the talking, Jerold? Can you mention PIP install, your feelings about it?

**Jerold Santo:** Yeah. If its PIP install for me, I just have anxiety... Even though it works most of the time. It's the same way -- and hey, old school Rubbish, but if I see your tool and I see it's written in Ruby, I'm kind of like "Uhm, do I want to mess with this?" And that's how I am with Python as well. Their stories are just fraught.

**Mat Ryder:** Do you not use GitHub then? That's Ruby, ain't I?

**Jerold Santo:** Well, I don't mind the website. I'm talking about a tool that I'm going to install, with dependencies, locally.

**Adam Staravia:** As a dev tool.

**Jerold Santo:** Yeah. I have no problem with Ruby-based things. But if you say gem-install this tool, I'm like "You know what? I don't really trust my Ruby environment over the course of years on my Mac", and I'm the same way with Python. Whereas with Go, and with Rust, it seems - and JavaScript had the same bad story for me, but Demo with TypeScript is showing some new opportunities to have universal binaries, which is cool... I'm just way more likely to say "If you can just grab a binary, drop it in your path and execute it, I will do that 100 times a day." But if your tool says PIP install, or it says gem install, or says NPM install, I'm kind of like "Do I want to mess with this?" That's just my sense. Does that resonate with you guys?

**Adam Staravia:** Especially if you're on Linux proper. Like, if you're on Mac, it's different, because you kind of have to use Homebrew, or PIP, if that's the way you want to go, or maybe vanilla straight-up Ruby, or a binary. But if it's on Linux, it should be in Apt, or whatever your \[unintelligible 00:45:04.05\] Yum, or pick your -- it should be a package. Or you should have to update your registry with whatever package directory you want to use, and apt update, and get that, and install. That's my feelings. I don't like to PIP install anything if I don't have to.

**Mat Ryder:** Yeah, when I get a new computer, which happens more than I can justify, I don't like it when the first time I'm forced to just add all these tools to be able to install stuff. I feel like it's a nice, clean machine, and then I hold off and hold off...

**Jerold Santo:** You're muddying it.

**Mat Ryder:** Yeah. At least if it's a Go binary, I can delete the file, and it's gone, and I know where it is. When I install -- I didn't know what happens when I NPM install something. Sometimes I'll do that in the wrong folder, and then I'll get a Node modules folder on my desktop, which is synced through iCloud... You know what I mean? It could be a can of worms.

**Jerold Santo:** Right.

**Mat Ryder:** So I am, yeah, into that simplicity thing. But if I'm already using that tool chain, if it's a tool for, say, people who are writing Node, then it completely makes sense that it would be written --

**Jerold Santo:** Right.

**Mat Ryder:** \[46:13\] Yeah. If it's a data tool that's going to be used mostly in Python, then I think you also can get away with it, although you still have version issues. But yeah, you can't -- I mean, just a single binary, I love it.

**Jerold Santo:** General-purpose tooling that wants to be used by people that are outside your particular ecosystem, ideally, should be packaged in a way that we can just isolate it, install it, drop it in our path and execute it.

**Mat Ryder:** And delete it. Uninstall easily.

**Jerold Santo:** And delete it without worrying about it just like spreading files all throughout your disk.

**Mat Ryder:** I remember on Windows I used to sometimes -- like, I'd install something, and then I'd be like "Oh, I want to uninstall that", and there's no way obvious way to do it, and you google it, or you DuckDuckGo it, and it's like --

**Jerold Santo:** You went there...

**Mat Ryder:** "Okay, you have to remove these files, then Go and find these files and remove them, then open the registry if you want to remove these values from the registry..."

**Adam Staravia:** Gosh...

**Mat Ryder:** You know, like --

**Jerold Santo:** Yeah, and it scatters its changes throughout your registry, and you're like "I have one global registry and I don't know all the places that it has been changed. Yuck."

**Mat Ryder:** Yeah. You actually had to do occasional just reformat your computer to clean it all, and that used to bother me. And I like on a Mac that applications are mostly contained inside that single \[unintelligible 00:47:22.20\]

**Jerold Santo:** Mostly. But not entirely though, right?

**Mat Ryder:** I know, not entirely. Yeah.

**Adam Staravia:** I think with the M1 there's more change like didn't Homebrew move to the opt directory, I believe...

**Jerold Santo:** Oh, yeah. Yup, Homebrew installs into opt now, versus USR/local. And I can't recall why that was, but that was a new change in order to --

**Adam Staravia:** I'm sure some sort of security enclave reasoning, right?

**Jerold Santo:** Maybe...

**Adam Staravia:** It's just challenging, yeah. I mean, you've got P-lists that spread about, you've got something that might be in my application support folder, or just, it's a -- give me a good, self-contained uninstaller with the thing. Give me the eject button, whether it's an application that I install as a literal Mac app, or a dev tool... Give me an uninstallation flow that respects my system. Because I'm sure you, developer developing it, care about your system, keep it pristine, and with reluctance install new things when it's a new machine, for sure.

**Jerold Santo:** Yeah, I think the only upside of that style is that you do have preferences that persist if you uninstall and then reinstall, or upgrade.

**Mat Ryder:** Yeah, but you don't always want that, do you?

**Jerold Santo:** Exactly. But sometimes you're like "Oh, I actually don't have to redo this. That's nice." It has pleasantly surprised me once or twice, but most of the time I don't want it. I want it to be completely gone.

**Mat Ryder:** Yeah. Sometimes I'll uninstall something because I can't figure out how to change a setting back; and then I uninstall it, and then I reinstall it, and I just remember the settings.

**Jerold Santo:** It's right there. Yeah, it's right there for you. It's waiting for you.

**Mat Ryder:** And I'm like "Where's the registry? Is there a registry?" But I'm on a Mac, so there isn't.

**Adam Staravia:** Another culprit is installing something to.local, in your root directory - or your home I guess - and not removing it, or putting it in like a hidden folder? I mean, obviously, I'm going to do an LL, or L, depending upon what your flavour of --

**Mat Ryder:** How Welsh you are

**Adam Staravia:** ...LS you use... I mean, if you've got an alias or whatnot - which I do, because I use Ohms...

**Jerold Santo:** He doesn't have the time to type L twice.

**Adam Staravia:** Yeah, I don't like, you know--

**Jerold Santo:** Just once. Nobody has time for that.

**Mat Ryder:** Yeah, you're a busy man.

**Adam Staravia:** Why two when you can just do one?

**Mat Ryder:** Good question.

**Jerold Santo:** Alright, so quickly, Mat, respond to my second question, which was "As a gopher, as a representative of the Go community, do you feel like Rust is encroaching on your previously standalone domain of like these command line installable tools?" Like, there's a lot of new tooling, whereas Go was like THE thing for a little while, where it's like "And it's written in Rust." Does that make you feel intimidated or encroached upon?

**Mat Ryder:** \[49:53\] No, no, I remember when Go was becoming that, and I would always say at the time "Write it in whatever you want. Whatever is the right tool for the job." So that attitude - I don't really deviate from that. I don't think Rust will just defeat Go, because it's really hard to learn, and that's the trade-off you make. It's much harder to learn, much harder to write Rust, but the trade-off is you get much more secure, much safer execution... And I guess if it compiles, you've got a high chance it's going to be correct. So there are benefits there. But Go - I don't know if it's just... Like, we'll see how that trends happen. Definitely there'll be trendy sort of things going around, but I don't know. I think they'll coexist, basically, forever, these two.

**Jerold Santo:** Fair enough. I was hoping for a less reasonable and nuanced position, but you know, I can only expect so much...

**Adam Staravia:** So reasonable...

**Mat Ryder:** Okay. Well, in that case, I could get my guitar and do an Anti-Rust song, if you like.

**Jerold Santo:** Okay, I do. Oh, we're in for a treat here... Mat has left his chair, his Mac display is tracking him throughout the room... He's back... He has a guitar.

**Mat Ryder:** The Mac display is annoying, because it follows you around when you move, and you sometimes --

**Jerold Santo:** Yeah, talk about surveillance capitalism, huh?

**Mat Ryder:** Yeah. I'll try and sometimes move out of frame to pick my nose, and then the bloomin' camera follows me and everybody sees it.

**Jerold Santo:** What's the song called? Anti-Rust song, or what?

**Mat Ryder:** Yeah, I don't know... Yeah, I guess that's what it's going to be.

**Adam Staravia:** Let's call it Rust Away.

**Mat Ryder:** Oh, yeah. Okay, yeah. I should just do it. We can always cut this, can't we?

**Jerold Santo:** No...

**Mat Ryder:** \[laughs\]

**Jerold Santo:** It has to go in.

**Mat Ryder:** \[51:42\]

Hey baby, what're your typing in...

I ain't never seen such crazy things...

What the heck is all this going to do...?

I've got some very bad news for you...

We're gonna Rust away...

Gonna Rust away...

You're gonna Rust away... Today.

Rust Away. Mat Ryder.

**Jerold Santo:** Woo-hoo! \[laughs\]

**Adam Staravia:** Can I critique?

**Mat Ryder:** Yeah...

**Jerold Santo:** "Can I critique?" No, you're going to hurt his feelings.

**Mat Ryder:** No, do it, because it wasn't great...

**Adam Staravia:** It won't hurt your feelings. So if there was a version two... Let's say you go away, and you think about sleeping, maybe you sleep a little bit, and you dream, and you think "Well, this is actually a hit song. I could probably do something with this", I would just encourage you to put a little bit more Rust Lang specifics into it.

**Mat Ryder:** Yeah, I don't know enough to do that. I was thinking that. I was going to mainly focus on like --

**Adam Staravia:** You could have mentioned Cargo or anything. I mean, really anything.

**Mat Ryder:** Yeah, but my knowledge is really limited. I was gonna focus on like --

**Jerold Santo:** \[laughs\] It was really -- it was really quite awful, actually.

**Mat Ryder:** Yeah. I was gonna focus on like vulcanizing things, and actually -- you know, to prevent Rust. Like they use painting, and stuff, to protect the metals, so they don't rust.

**Adam Staravia:** Right. Anodized

**Mat Ryder:** Rusting metal, why would you want that? Red iron oxide... There are lots of ideas, but...

**Adam Staravia:** Sure.

**Mat Ryder:** ...yeah, it just didn't happen. I'm sure if Dan-tan had done it, he would have done a much better job, because I know he's particularly good at songs.

**Adam Staravia:** \[53:44\] Dan-tan! So one quick hat nod to the Git UI project is that it seems to be easily installable, regardless of originating language, which is super-awesome. Great song, Mat. Thank you for sharing that with us. It was awesome.

**Jerold Santo:** I was going to hop in and start singing with you, but my skills are a bit rusty, so...

**Adam Staravia:** Ha-ha-ha...

**Jerold Santo:** Sorry about that... Let's move on. Git Branchless. This is our last one of the list here... A high-velocity monorepo scale workflow for Git. This is like a grab bag of utilities. It's a weird name, Git Branchless, because it doesn't have anything to do with branching, really... But it adds a bunch of cool stuff, like Git undo...

**Mat Ryder:** It's a good name then, isn't it, Jerold?

**Jerold Santo:** Like, there's no branching?

**Mat Ryder:** Yeah, it's branch less. And you're like "Oh, I don't know why it's called that. It doesn't have anything to do with branches." But it's called branch less. That's not an impression of --

**Jerold Santo:** Yeah, but why would you name yourself based on what you have nothing to do with? I just feel like it's not the

Way to do it.

**Adam Staravia:** Yeah. Maybe because they're against it, and so they didn't --

**Jerold Santo:** I don't call myself Jerold Rustless because I don't write any Rust...

**Mat Ryder:** Good name though...
**Adam Staravia:** Nice name. I like that.

**Mat Ryder:** It sounds like a cool guy.

**Jerold Santo:** I'll consider it. They call me Jerold "Rustless" Santo.

**Mat Ryder:** That is a cool name.

**Adam Staravia:** Okay.

**Jerold Santo:** That is pretty cool. I might pick that up, actually... Alright, I revoke my argument. The point is, there's lots of cool stuff here. Smart log...

**Adam Staravia:** Git undo, Git restock, Git sync, Git move... Lots of good stuff.

**Jerold Santo:** Written in Rust - so it's not rustless - by Valid Khan, and been out there for a while... But not too much to say about this on the show from me necessarily, except for that it's just a lot of very nice user experience improvements in your command line Git. So if you're not like Mat, using GitHub Desktop, and you're a real dev using the command line, then maybe check out Git Branchless.

**Adam Staravia:** Yeah. In terms of naming - you know, same song, different singer, since we're talking about Rust Away, and Mat's doing some jingles for us, I was thinking Git utilities. I mean, it's a bunch of utilities. Why not like make a standard utility library?

**Jerold Santo:** Right.

**Adam Staravia:** So I googled it, and there is a Git util, but it's not maintained.

**Jerold Santo:** Well, no wonder you didn't name it that.

**Adam Staravia:** It's not maintained, and it's sort of like -- I wouldn't call it dead, but the last commit was two years ago. It's probably either perfect software, or unmaintained. Right?

**Jerold Santo:** It's tough to tell the difference sometimes. I was just talking about this recently, I think on Changelog News, on a post about quitting... What's the difference between quitting and being finished? They're quite a bit different. But with open source, you can't tell, like, "Is this thing unmaintained, or is it actually finished?" Some things are just done. Other things are abandoned, and you've got to find out which is which.

**Mat Ryder:** Yeah, this is always the problem that I have, because people - one of the ways they decide if a project is worth using is they'll look when was the last release... And we're almost at the point where we're just going to do releases regularly for the sake of it, even if nothing changes. And it sort of encourages bloat, it encourages feature bloat as well. When a tool kind of nails it, you don't need to keep going on that. But similarly, software's never finished, and so it's not so simple. But yeah, tough one.

**Adam Staravia:** We almost need like a health meter, or something like that, like built into GitHub, or an external socket; like, they do a lot of security stuff externally from the repository, regardless of its origin, whether it's GitLab, GitHub, or whatever. We almost need like a health meter, or at least a democratized version of it that's like "Okay, this may have had a commit two years ago, but it's still -- it's being used." Like the downloads are still way up, for example, or this release is getting pulled constantly into other things. There has to be a different metric than just simply last commit.

**Jerold Santo:** \[57:49\] GitHub does have that Pulse page, which they've kind of hidden that... But the Pulse, which is kind of that, but it's kind of like what's been going on this project recently... And you can at least go there and see, "Well, there's been 17 new issues and no response." To me, that's probably abandoned, because it's generating issues for people, but not even being responded to... Generally, finished software's at least -- I mean, there's still going to be things that come up over time, but kind of fewer bugs per response... And then there's like PRs merged recently... It'll just show you like what's been going on. It's not exactly health, though; it's more like recent activity, which can be a proxy for health, but not always.

**Adam Staravia:** Well, I have good news for you, Jerold.

**Jerold Santo:** What's that?

**Adam Staravia:** Doneorperfect.com is available. I mean, we can encourage somebody to build a tool called DoneOrPerfect.

**Jerold Santo:** So you've got to pick which one it is?

**Adam Staravia:** Not Under Mifflin Done, or perfect.

**Jerold Santo:** So I don't understand. I guess you're going to mark your project as done, or perfect?

**Adam Staravia:** Well, it just was on the whim here. I'm trying to create a Rust Away song for you, man... Come on, give me a dime.

**Jerold Santo:** \[laughs\]

**Adam Staravia:** No, just some sort of -- I mean, I don't think that the insights tab is that insightful in this regard. So maybe there's something that can be done. Maybe it's a fun project; like Mat said, this is just a fun thing. And then maybe GitHub acquires you, and then next thing you know you're a millionaire or a billionaire, or you've got some stock options in the juggernaut that's called Microsoft, that's just like slaying it out there... You know...

**Jerold Santo:** Alright...

**Adam Staravia:** I don't know...

**Jerold Santo:** That escalated quickly.

**Adam Staravia:** One could dream, right?

**Jerold Santo:** So if you register doneorperfect.com, you're going to be a billionaire with Microsoft's stocks.

**Adam Staravia:** If you execute well, yeah.

**Mat Ryder:** Yeah, probably.

**Adam Staravia:** If you do it. Just do it.

**Jerold Santo:** Alright... Should we hop to unpopular opinions, or should we -- we have more things that we've shared that are Git-related, but we can also just get on with it?

**Adam Staravia:** Maybe a state of Git internally here...

**Jerold Santo:** Okay.

**Adam Staravia:** Like, how do you Get, Jerold? How do you Get, Mat, and Adam, how do you Get? ...speaking to myself.

**Jerold Santo:** Okay.

**Adam Staravia:** Are you a simplicity person, Jerry? I know that you just use terminal.app, not term, or even Fig or...

**Jerold Santo:** Correct.

**Adam Staravia:** ...what else have we had on the show?

**Jerold Santo:** I do use Ash now, versus Bash...

**Adam Staravia:** By force.

**Jerold Santo:** I use it as if it's Bash...

**Mat Ryder:** I can't believe you were having a go at me for using GitHub Desktop, and you just use the basic, the first, the only thing that's already installed when you get your first computer.

**Jerold Santo:** You mean a terminal, like real developers do?

**Mat Ryder:** Oh, I don't subscribe to that...

**Jerold Santo:** \[laughs\] I don't actually either. But...

**Adam Staravia:** He's being funny.

**Jerold Santo:** ... I do use it, and I do use it almost exclusively. Now, I like a Git GUI myself, so I can get graphical... And the one that I prefer...

**Mat Ryder:** \[singing\] "Let's get graphical..."

**Jerold Santo:** ...is called GITC. Now, GITC has been a long, long time project that's gone through multiple forks and abandonments and community pickups, as macOS has changed dramatically over the years. So there was this Rohan -- I think it was Rohan J. had a fork of GITC, that they maintained for a while after the original GITC author didn't want to do it anymore, and then that went unmaintained... And I went searching, actually, for a GUI, specifically for a few things. I like to do staging, and committing, especially like - what do you call it, chunk commits? Specific lines of a file, and like selecting all that... I like to do that in a GUI, and not from the command line, because it's just clunky from the command line. That's the main thing I do inside a GUI. And so GITC was gone for a while; it was just like abandoned, and I was super-sad, I started looking for a new one... And then it got revitalized in the last year or two by the community. This is like the best side of open source, right? People that loved it and wanted to use it picked it back up, and now it's under like the GITC GitHub org even, it's not some user's account... And it's an open source Git GUI for macOS that's under active development once again... Mostly maintenance mode, but I'm happy in maintenance mode, because...

**Mat Ryder:** \[01:02:05.05\] Perfect.

**Jerold Santo:** ...it's a good GUI. And I don't need any new features, honestly. It does what I like, and I like what it does. And so that's what I use - I use the command line for most things - Git log, Git status, simple commits, like git commit -all with the message command line, push and pulls command line... But staging, reviewing - that kind of thing from GITC. So I would highly recommend that for macOS users.

**Adam Staravia:** Let's give it a little shout-out, since you mentioned the fact that this is being maintained. Thank you to -- this is not sponsored, but I am a fan... Mac Stadium. In the footer of the README it says -- oh, that's the license. Never mind. The one before the last, not the very, very end of the README, almost to the end of the README, it says "This project is supported by Mac Stadium open source developer program." And they give them a free Mac Mini for their CI. So they say "Thank you to Mac's team." So I mean, that's super-cool. I think we should do like shout-outs, Jerold, to like those that are supporting open source in some way, shape, or form, just like giving services away, to enable just no new features, but just stability, right? Just keeping the thing alive.

**Mat Ryder:** Well shout-out to me, then. I donated an M1 MacBook to the Whales Project, which is Whales app. You know, you can build desktop apps using JavaScript, and they're great. They feel like native apps, and I wanted to support that project. I don't talk enough about what sort of open source hero I am, frankly...

**Jerold Santo:** \[laughs\]

**Adam Staravia:** Well, that's what we have here, Mat...

**Jerold Santo:** Could you sing yourself a song about yourself, maybe?

**Adam Staravia:** "Mat is a hero in the open source world, yeah, yeah, yeah," That's the chorus.

**Mat Ryder:** Pretty good. Well, I did write Testify, which is Go's big -- that's the testing framework that everyone uses in Go. Well, we had you on the show talking about your stuff. You've got Bit Bar, you've got Bar... Right? So you've got your open source bona fides...

**Mat Ryder:** Yeah, but because I'm so modest... I'm probably the most modest person in the world.

**Adam Staravia:** You seem very modest.

**Mat Ryder:** Yeah. And it's a big weakness, because--

**Jerold Santo:** It's your greatest weakness, actually.

**Mat Ryder:** Yeah, I don't know... I do myself a disservice.

**Adam Staravia:** So this M1 MacBook Pro - it's being used by someone to maintain Whales, I assume? Are they sharing it and mailing it around?

**Mat Ryder:** I love the idea of that, but no, they -- someone has it, and they use it to...

**Jerold Santo:** Like a CI?

**Mat Ryder:** No, no, they're using it to actually test... Because you're building desktop apps, and so M1 was very different, and they wanted to... Yeah, there was work to do there.

**Adam Staravia:** That's true. That's a great point, too. I mean, when you do platform-specific development, and you don't have the latest rev of Apple Silicon, you need that, and maybe don't have the cash to shell out, or want to, because this is just a fun thing to you. You need supporters. That's cool.

**Jerold Santo:** Right.

**Mat Ryder:** Yeah. And of course, you can sponsor a lot of projects now on GitHub... So I recommend that. And I don't think enough companies do that. If you're a company, and you use some open source project, and you can sponsor it, I feel like you just should. We should make that more normal, really... Especially if you make money off that project, directly or indirectly.

**Adam Staravia:** For sure. Well, again, MacStadium.com. Shout-out to them. Super-cool.

**Mat Ryder:** Super-cool.

**Adam Staravia:** So you're a pretty simplistic Git user then, Jerold. You mainly stay command line only, except for visual specifics.

**Jerold Santo:** Yeah. Keep it simple, you know...

**Mat Ryder:** You're a simplistic Git. That's what he just said to you. I love that.

**Jerold Santo:** \[laughs\] And I owned it. I do agree. Clip it.

**Adam Staravia:** Well, I paused. Simplistic Git user.

**Mat Ryder:** Yeah, you did pause. And that's where we'll do the cut.

**Adam Staravia:** Yeah, I had to do that.

**Mat Ryder:** Yeah.

**Jerold Santo:** Just remember that I had to describe to you guys what Git meant earlier in this show, so... I'm not sure which one of us is simplistic. But...

**Adam Staravia:** Well, that's just because you CDU better than we do. Or DDG.

**Jerold Santo:** \[01:06:06.23\] \[laughs\] I thought you'd at least go DDW, I duck-duck-went faster than you guys... \[laughter\]

**Adam Staravia:** Alright, Mat, your turn... How do you Get? How do you Get?

**Mat Ryder:** I like to keep it simple. I'm a simple Git. If it's complicated, if it's like "Oh, there's a conflict in this file", I'm like "Forget it. I'm out." I just put in my letter of resignation. \[laughter\] No. Yeah, I tend to use GitHub Desktop as much as I can, and then I'll go into the command line if I have to, if things aren't working for me. I'm not one of these -- like, some people like Jerold a couple of times hinted at being like "I'm not a proper dev, because I use desktop apps", and stuff like that. And I know, Jerold, you're joking... But I still have a song for you.

**Jerold Santo:** Well, I'm also serious... No. Oh, you have a song for me? Uh-oh, look what I did... Look what I did...

**Adam Staravia:** Gosh... Two songs in one show. Is this possible?

**Mat Ryder:** Don't say that, because hopefully the first one gets cut.

**Adam Staravia:** No, it's not getting cut. What's the title of this song?

**Mat Ryder:** Keyboard Wizard.

**Adam Staravia:** Keyboard Wizard. Okay, good.

**Jerold Santo:** Ooh...

**Adam Staravia:** I feel like Howard Stern. Pause one second... Howard Stern does a great job of having awesome artists on his show to do like renditions of their song in a live version. I feel like Howard Stern right now. Like, what's your song title? Okay, go ahead. Go, go.

**Jerold Santo:** All we need is an awesome artist, and then we will be him.

**Mat Ryder:** Well, meanwhile, you've got me.

"I don't care what you wear,
I don't care if you swear...

It doesn't mean that much to me...

You can do what you need, do as you please...

You'll hear no argument from me...

Except "What's your IDE?"

Your IDE, please... I want to know so I can see...

Are you a VS Coder like me,

Or are you one of those keyboard wizards that you see...?

Oh, speaking of which...

I'm a keyboard wizard, I need no mouse...

Get that trackpad away for me...

I know combinations that'll rock your foundations,

I dare ya, screen-share with me...

Screen-share with me...
Screen share with me...

I want to know so I can see...

Are you a keyboard wizard? I need no mouse...

A trackpad is just a rectangle as far as I'm concerned...

Because I'm a keyboard wizard...

**Jerold Santo:** Wood! That one's a keeper.

**Mat Ryder:** Yeah, that's a keeper. That one I actually did right.

**Jerold Santo:** That's a good one.

**Mat Ryder:** Thank you. But also, very serious point there, which is, you know, let people just use whatever tools they want. Don't make us feel bad because we can't get out of Vim, just because we can't quit Vim...

**Jerold Santo:** Well, that leads me to a serious question, though... As a VS Code user, have you done any of the -- Because VS Code has a bunch of Git stuff built into it? Have you tried any of that stuff? Do you like it? Or are you just like "I'm happy with the GitHub Desktop, I don't care"?

**Mat Ryder:** Actually, yeah, for the simple -- just like stashing, committing changes, I'll just use that in the IDE, because it's right there exactly. And then if it's a little bit more complicated, I'll open GitHub Desktop, and then if I can't do that, I'll phone up one of my smart friends like Jerold and ask him "What do I type in to make this fix, please?"

**Adam Staravia:** Debatable...

**Mat Ryder:** Yeah.

**Adam Staravia:** \[01:09:49.02\] Hostinger Tutorials mentions that GitHub Desktop -- it specifically says... If your remote repository is on GitHub, they say "This tool will be the most useful for you." So, I mean, that's a large tribe, right? I mean, a lot of people have software there. But I do agree that at some point you graduate; it's like "Well, certain things can be done via the command line. I'm here... Why eject and go somewhere else?" Certain things should be done. If you're in VS Code, why not use some of the visual aids inside VS Code? I do that. I might add a file to a commit that I'm staging up and whatnot, and type the message in, and along I go. Why go to a full-on GitHub Desktop experience? Well, maybe you're visualizing, or you're doing something with issues, or maybe there's a PR going on, and it's a bit more complicated and a bit more GitHub-specific.

**Mat Ryder:** Yeah.

**Adam Staravia:** It makes sense.

**Mat Ryder:** Yeah, it does. Use whatever tools you like.

**Adam Staravia:** So, for me, thank you for asking...

**Mat Ryder:** Adam, what's your favourite ever song? \[laughs\]

**Jerold Santo:** Favourite ever song?

**Mat Ryder:** Yeah, you're going to have to pick.

**Adam Staravia:** Okay... Well, I'm going to go to your side of the pond. I might say something from the Beatles. I'd probably pick from Yesterday... Actually, I'm a big fan of the movie Yesterday. Have you ever seen this movie?

**Mat Ryder:** Yeah. What a great premise.

**Adam Staravia:** Amazing, amazing movie. But it's a great song, too. So I'm a Beatles fan.

**Mat Ryder:** The premise of Yesterday is this guy just discovers that the Beatles never existed, and so no one knows them... But he knows all the songs, and he's like a songwriter. So he just pretends he writes the Beatles songs...

**Adam Staravia:** That's right.

**Mat Ryder:** ...and then they're all hits, and he becomes a super-famous chap. Yeah... I love that. I also love the Beatles very much. Furthermore, I have an original Sergeant Pepper's album in mono, which is good... Furthermore, I just listen to it in one ear, because you might as well... And yeah, it's just beautiful. Paul McCartney, I think - probably one of our greatest ever songwriters... You know, just amazing.

**Adam Staravia:** Phenomenal, phenomenal artist. So yeah, my answer is that. I mean, I think the Beatles is on my list of top artists, top songs. Like, if I had to pick a song on replay forever, I would say don't. But if I had to, if it was by force, absolute force...

**Mat Ryder:** Hang on, what's the situation?

**Adam Staravia:** I don't know, I don't want to speculate, but it's probably terrible...

**Jerold Santo:** Gun to your head, or...?

**Mat Ryder:** They've got your kids?

**Jerold Santo:** Ooh... The phone calls come from inside the house?

**Adam Staravia:** Come on now... Do you want to do a Liam Neeson situation here? You want to go there, Mat?

**Jerold Santo:** \[laughs\] Oh, Mat loves Liam Neeson. He does the Liam Neeson.

**Mat Ryder:** \[in Liam Neeson voice\] "I don't care who you are... I want you to listen to the same song on repeat forever... Or I will find you!" "Yesterday! No Mercy!"

**Jerold Santo:** \[laughs\] Oh, gosh... You played into that brilliantly. Mat, I knew you had a Liam Neeson up your sleeve, and so you were just waiting for an opportunity there.

**Adam Staravia:** I figured you could do that.

**Mat Ryder:** Yeah. I can't wait for someone to mention Jack Sparrow. \[laughs\]

**Jerold Santo:** I think we've drained Mat of all of his talent on this one episode. I mean, do you have other bits? We know you have Jack Sparrow, but... I mean, you've pretty much done --

**Mat Ryder:** Yeah, the German character, Hans...

**Jerold Santo:** The German character... \[laughs\]

**Adam Staravia:** Speaking of other modern famous singer/songwriter - Ed Sheeran. Can you do an Ed Sheeran version? You also sing a lot, too... Do you like the guy?

**Mat Ryder:** I think he's a great songwriter, actually. So yeah, I think he's good. But no, I can't -- I mean, does he have a distinctive voice? I mean, he does singing, but...

**Adam Staravia:** Yeah, for sure.

**Mat Ryder:** ...but talking, I don't know. I could do Beatles though, if you like... I can do every Beatles.

**Adam Staravia:** Okay, sure.

**Mat Ryder:** They're all different.

**Adam Staravia:** Ringo. You can do Ringo?

**Mat Ryder:** Of course I can do Ringo. He's very bouncy when he talks, you know... That's Ringo. And he sounds like he doesn't know what he's saying... But he does, you know. And Paul McCartney is a bit like that too, bounces around, but

He's a bit more upbeat, and also, he seems to know what he's doing... John Lennon was always very wiry in his voice, you know, when he talks. So it's very different. And then you've got George, who's my favourite, because George doesn't really sound like he's all there, but \[unintelligible 01:14:01.09\] here comes the sun, you know? Did you know that?

**Jerold Santo:** Right... Pretty good.

**Mat Ryder:** \[starts playing the guitar\]

**Adam Staravia:** Oh, gosh...

**Jerold Santo:** \[01:14:14.02\] \[laughs\] Look what you've done, Adam... You've opened up this can of worms. You can't put the worms back in the can. I love it.

**Mat Ryder:** Can you actually get cans of worms? Like, can you buy them?

**Jerold Santo:** Oh, of course.

**Mat Ryder:** For fishing, or something. Or just eating.

**Adam Staravia:** For sure. You can literally get them, and you can figuratively get the version that's a simulation, or not really the can of worms. You could buy the one for kid like the prop.

**Mat Ryder:** Oh yeah, when a big snake flies out when you open it.

**Jerold Santo:** Right, and it pops out...

**Mat Ryder:** That's one worm though in it. I wouldn't say -- I'd say that's a can of worm.

**Jerold Santo:** Well, you buy more than one, and it's cans of worm.

**Mat Ryder:** Yeah, it's like attorneys general.

**Jerold Santo:** Exactly.

**Mat Ryder:** \[laughs\] I've got one pick that I'd like to also bring up, that I learned about at FOSDEM...

**Jerold Santo:** Oh yeah, please do.

**Mat Ryder:** And this I think is very cool... It's at reviewpad.com. And this is like smarter PRs and rules around PRs. So in a lot of my projects I like to have it such that PR goes up, and then we automatically run all the tests and everything, and only if all those tests pass... And they can be backend unit tests, they can be integration tests sometimes, they can be frontend tests, end-to-end tests... Whatever it is that gives you the confidence to release to production, you can gate the PR on that, so that it doesn't go into main. So your main is never broken, your main branch.

Well, that can be sometimes a little bit too strict, and Review Pad lets you actually create some more nuanced rules around this. So you can say, for example, "Markdown files, just let them go straight to main." You can say "In this case, I want to I want to push to main, but I still want someone to review this at some point." So it's like still in there, it's low-risk, so you want to progress, and later someone can check it.

You can say things like "For all Go files, you want to make sure the entire test suite runs", because it's quick, so it's no big harm... But you can even do things like for new starters, for like different groups of people, you might say "New starters, everything should run for them, but the more senior people have slightly more relaxed rules, and they're allowed to push without all the checks happening."

And even individual functions... You could mark a function in code as critical, and if anything inside that changes, then it makes sure that all the tests will run, and that whole pipeline executes before it's allowed to merge. I think this is the next level, the next generation of PRs; this is something that -- I mean, I don't know who owns this... This is something that I would expect to have in GitHub, at some point. This is perfect. I haven't used it yet, but I do intend to. What do you think of that Review Pad?

**Jerold Santo:** I like all the words that you've just said about it. It's brand new to me, it sounds really cool... A glowing review from you, which does mean a lot to me, so I'll definitely look closer at it... But I think that --

**Mat Ryder:** It's too late to start being nice to me now, Jerold...

**Jerold Santo:** Well, no one's listening anymore. We lost them at "Here comes the sun." \[laughs\] But yeah, I mean, definitely we'll check it out. I think that PRs as they stand leave a lot of things on the table, and we know there are lots of teams building things like this in order to flesh out and improve the code review process. We had a show last year on Graphite, which is Stack Diffs, which plays in the same ballpark as this, but it's not exactly the same; they're not tackling it the exact same way. And I know a lot of people are enthusiastic about that. Christopher Miller, skull on JS Party actually gave an unsolicited Graphite shout-out in his Pro Tip Time, because he's been using that, and he has been loving that... So that's another tool that maybe we'll just link to. But that's my thoughts on the matter. I have never seen this before this afternoon, so I have to check out more of how it does what it does... But yeah.

**Adam Staravia:** \[01:18:05.07\] It makes sense. I mean, it's almost as if this can even be similar to the way you have infrastructure as code. It's almost like to main as code. I don't know, just like something that says "We have to have a gate on this process." And like you had said, there are certain things that can go through, more nuanced rules... And that totally makes sense. A one-size-fits-all Git push to main does not always fit. So I can see how this makes sense.

The thing I think I question though is less the tool itself, and more like Steve Jobs said about Dropbox - is this just a feature, or is it a product, or a company? I wonder if, in some cases, this is a great standup of a feature that should just be GitHub proper, if that's what the majority uses.

**Mat Ryder:** Interesting. I mean, I wonder if their strategy is like an acquisition thing. And sometimes that's a great strategy to have.

**Adam Staravia:** You've done it a couple of times, right?

**Mat Ryder:** Yeah.

**Adam Staravia:** I mean, it's a good -- I don't if that's been your strategy, but you've done it...

**Mat Ryder:** Yeah, three times.

**Adam Staravia:** Thrice...

**Mat Ryder:** Yeah, but they weren't features. I mean, actually, I think solving one problem and doing it really well is worth doing. And yeah, maybe you'd struggle to build a business around it. I don't know.

**Adam Staravia:** Yeah. Well, that's the hard part... It's like, "Here's this thing, it's great, it's useful", but man, it died because there's no company. It's just a feature.

**Mat Ryder:** Yeah, so that's why we have to sponsor open source if we want to keep it alive. We can't just expect it to keep going. We have to normalize that more. Furthermore, we've got to do more of it. It's hard to justify sometimes, but it's important.

**Adam Staravia:** I think it's certainly becoming more normalized, but I think as it becomes normalized, it becomes the paradox of choice. It's like "Well, there's so much open source, there's so much usefulness... I can't possibly give to it all, so I either do nothing, or I just don't know where to put it, and I am just guilty. I feel guilty."

**Mat Ryder:** Yeah, so that's interesting... I wonder if we could get like a heat map of usefulness of your dependencies, actually. How often is that code executed?

**Adam Staravia:** Yeah. I would say a Git heat map sounds pretty cool, honestly.

**Mat Ryder:** Yeah. Well, we can do it with observability tools. If you've got tracing, and you've got observability running in your code, you will have insights into the code paths, and stuff; you probably could gather some stats on the most useful bits.

**Adam Staravia:** That might just layer on the guilt though, honestly.

**Mat Ryder:** Why don't you just pay for the project then, if you're feeling guilty?

**Adam Staravia:** Well, I mean, it's not me, Mat. It's somebody else, of course. No, I mean, I think that --

**Mat Ryder:** It's Dan-tan!

**Adam Staravia:** Dan-tan... \[laughs\] He's back again.

**Mat Ryder:** Dan, pay for your project!

**Adam Staravia:** The point you're making is great, though; we should support open source more. I always want to see more clarification on the how. GitHub Sponsors is one answer, but it's an avenue. It's not like what. The what becomes infinitely harder to define if you don't examine the open source that's useful to you. And then sometimes it might be corporate sponsors, and it may actually be open source, but it's a company who's backing you. Well, are you going to support that thing? Well, maybe... You know, you might use it as a support, but they're already a company; just buy the things that support them to make it. There's no wrong way to support open source.

**Mat Ryder:** I like all the words that you've just said.

**Adam Staravia:** Well, thank you.

**Mat Ryder:** I don't agree with your point...

**Jerold Santo:** That's quite a compliment.

**Mat Ryder:** Well, that was a very -- yeah, Jerold, by the way, just for future reference, if someone's describing something, and you like all those words, I feel like you like the thing. I think it's safe to say, "Yeah, I like that."

**Jerold Santo:** "Okay, I'll check it out."

**Mat Ryder:** Yeah, check it out. You will like it.

**Jerold Santo:** I just don't want to give you too much credit. I don't like to give you exactly what you're looking for, because you beg for it so much. Well, let's close up with a lightning round. This has been a fun conversation, a long one, way more singing than expected, or hoped for...

**Adam Staravia:** Or desired...

**Jerold Santo:** ...or appreciated...

**Mat Ryder:** A lot less than I expected. I'm really here to do songs, and there's been a lot of talking about Git. \[laughter\] We've spent a lot of time in between tracks, talking about Git.

**Adam Staravia:** Way too much...!

**Jerold Santo:** \[01:22:15.27\] \[laughs\] That's funny. Yeah. We should have changed the premise to like "Mat sings a song, interspersed with Git conversations."

**Mat Ryder:** Great. You'd go to that gig, wouldn't you?

**Jerold Santo:** Well, you have one more chance here, because we're going to do a lightning round of your brainchild on Go Time, Unpopular Opinions... And surely, you can strum us out the theme song for the jingle for Unpopular Opinions... Can you not? Otherwise, we'll have to splice it...

**Mat Ryder:** It's hard.

**Jerold Santo:** We can splice it right here.

**Mat Ryder:** Yeah, splice it, yeah. \[starts playing the guitar\]

**Adam Staravia:** Gosh... We're back to this again?

**Jerold Santo:** What's the alternative? \[laughter\]

**Mat Ryder:** Yeah, yeah, splice it in.

**Jerold Santo:** We'll splice it.

**Jingle:** \[01:22:59.20\]

**Jerold Santo:** So for those who don't listen to Go Time, Unpopular Opinions is a regular segment where people share opinions that they think or hope or expect to be unpopular with the listening audience... And then we put those opinions out on the social mediae to see if it's actually unpopular or not. Now, what we've found over time is that most unpopular opinions are actually popular when it comes polling time. But there's been a few people who have been somewhat unpopular, and a few who've managed to be incredibly unpopular with their opinions. I'm actually in the top five most unpopular opinions of all time...

**Mat Ryder:** What was it?

**Jerold Santo:** That JS Party is a better podcast than Go Time.

**Mat Ryder:** Aw... I feel bad for JS Party.

**Jerold Santo:** ...which was unpopular, of course, with the Go audience... But we're going to do a lightning round real quick. So Adam, passing to you... First one. Do you have an unpopular opinion you'd like to share?

**Adam Staravia:** I think my unpopular opinions I don't have any unpopular opinions. I tried so hard to think about something that is unpopular, and all I could think about is popular things.

**Mat Ryder:** Like what?

**Adam Staravia:** Well, I think if you're struggling to get something done consistently that you want to do, my unpopular opinion is that you should learn to habit-stack. It's a superpower.

**Jerold Santo:** Habit-stacking is a superpower.

**Adam Staravia:** That's right.

**Jerold Santo:** Tell us more.

**Adam Staravia:** But that's kind of a popular opinion if you know about habit-stacking.

**Jerold Santo:** Right.

**Adam Staravia:** Like, if you learn the inner secrets of this dark secret, basically... So you have habits, right? Let's say you make coffee. This is my example for me, a really simple example. I make coffee once a day when I'm at work at least, maybe twice, and I wear glasses, like you, Mat. I wear glasses. And as a glasses' wearer, you must be upset or get upset when they're dirty.

**Mat Ryder:** Yeah. I get furious.

**Adam Staravia:** Especially upset if you have to have a special microfiber cloth to clean them, because you can't just use your shirt.

**Mat Ryder:** Ugh!

**Adam Staravia:** Your glasses would smudge, right?

**Mat Ryder:** Yeah... Aright! I hate dirty glasses!

**Adam Staravia:** Now that I have a point of empathy, you can understand what I'm saying. So my feeling is if I'm going to have dirty glasses all day, that's upsetting. Can't do that. Well, I will forget; I get busy... You know, I don't have this cloth in my pocket all the time... I'm gonna habit-stack. I'm going to make coffee and leave my cleaning cloth when I have time. There are steps between the coffee making, right?

**Jerold Santo:** I see...

**Adam Staravia:** You brew the coffee, you wait for the coffee to brew, you pour it, you drink it.

**Jerold Santo:** You stack this habit with a habit you're already doing.

**Adam Staravia:** Right. So you stack a habit near another habit that you do consistently... And then you do it.

**Jerold Santo:** Right. Okay...

**Adam Staravia:** It's a superpower. If you learn to do that in different ways, let's say more productively... Let's say - I don't know, whenever you're running tests, and you've got a minute or two, and you have like three emails you can rapid-fire off, then you could do them. Stack up a habit of like you need to return these emails, but you've got that minute, minute-and-a-half, or maybe you've got a couple Slack messages stacking up, or something that can happen in that three minutes. Stack a habit of good communication could be the habit. And the way you execute is a few simple emails, maybe a returned Slack message, maybe it's a PR review, or a one-liner, or whatever it might be... Maybe a quick chat with ChatGPT... Who knows? I mean, just do something. Yeah.

**Jerold Santo:** \[01:26:24.09\] Is this just multitasking, or is this more than multitasking? Because it sounds like you're just talking about multitasking. Because am I in the habit of --

**Adam Staravia:** Well, I think in that case --- no, no, no. Well, because -- well, in that case it might be blurred. But in my case, I'm like, I do have a habit, and so I stack certain habits around that thing. So not only am I doing those other things, but now I think "Okay, when I make coffee, neurologically, I'm thinking "I've got to clean my glasses", because right here's the thing, and I just do it." So it's a habit that forms around other habits.

**Jerold Santo:** Now, I don't wear glasses, but I would think --

**Mat Ryder:** Show-off...

**Jerold Santo:** ...what about like when you realize they're dirty? Maybe you do it then.

**Adam Staravia:** Well, the point is that you don't always have that cleaning cloth.

**Jerold Santo:** Oh, I got you.

**Adam Staravia:** You know, unless you carry this cleaning cloth with you everywhere. And I just don't.

**Jerold Santo:** So like if I'm deploying my code, I can floss my teeth.

**Adam Staravia:** Well, I mean, Jerold, pick your habit. If you've got issues with flossing, then maybe. Maybe.

**Mat Ryder:** Yeah, but I'm kind of liking this. I wonder if it also works with bad habits... Because like if maybe you're a nose picker.

**Adam Staravia:** Sure. Des tack. You could stack things.

**Jerold Santo:** I'll have a cigarette.

**Mat Ryder:** No, I don't mean so that you can do bad habits, Jerold. That's mad.

**Jerold Santo:** Every time you pick your nose, have a cigarette. \[laughter\]

**Mat Ryder:** That would work though...

**Adam Staravia:** Sure.

**Jerold Santo:** Yeah, it works with bad habits, too. I think it does.

**Adam Staravia:** Yeah, that's redirection. So if I understand you correctly, maybe you have a bad habit, and you don't want to do it... And so when you think about the bad habit, you do a healthy habit.

**Mat Ryder:** I like the bad habits though.

**Adam Staravia:** Replace it with --

**Mat Ryder:** No, I'm thinking I do a bad habit, like don't brush my teeth... And while I'm not brushing my teeth, I can also be not wearing deodorant, for example. So it's like cascades...

**Jerold Santo:** \[laughs\]

**Adam Staravia:** No, that's not how it works, Mat.

**Mat Ryder:** No, you want to do -- the second one should be positive.

**Adam Staravia:** Well, I mean, it would work if you cancelled it out. Let's say you did a bad habit, and you're like "Well, since I'm bad here, I should be good over here."

**Mat Ryder:** Yeah, that's what I was thinking. I was trying to do that, and I thought deodorant

**Adam Staravia:** Yeah. Like actually double up on deodorant, or something like that.

**Jerold Santo:** Alright. Well, this one was going to be unpopular with me. I think it's a terrible idea. I think habit stacking is the worst. \[laughs\] It sounds awful. Let's go to you, Mat. Do you have an unpopular opinion?

**Mat Ryder:** Yes, I do. Yeah, I think when we're building software, we very often focus on the wrong things. I just think we're constantly doing this; we don't focus on what's important. I mean, really, you've got to solve a problem for somebody. That's what you've got to do. And we are sometimes so far away from that, it's so abstracted from that, because of process, or just organization, or whatever it is, that we're doing the work kind of in isolation, and not in the context of where it actually ends up.
In small tools, in small projects that don't happen too much. And especially if you're scratching your own itch, then that's a great way for this to not happen... But when you get into bigger orgs, understanding why you're doing something is so important, and everybody needs to know that; everyone needs to understand that. It can't just belong to just some people, and they decide what everyone else is doing.

So I think we often focus on the wrong things, and we're just building the wrong things. And usually, sometimes it's nice to just do a cool project, and I would never want to take that away from anybody. But if you're just doing cool, complicated stuff because you love it, or it's satisfying to do, and it's a hard problem, and you're solving it, then that's one thing. But you can maybe -- if you can solve a problem for somebody with a script, or just something much simpler, if there's even just a tool already that kind of solves the problem... Yeah, I feel like we don't enough - especially because we're there to build software... We should remember there are other things in our tool belt, and try and just focus on solving the problem and do whatever it takes to solve a problem for a person. And try and know who the person is; try and meet them if you can. If it's not you. Try and meet the person. So that's my unpopular opinion.

**Jerold Santo:** \[01:30:25.06\] This just sounds like good advice, man. This isn't like unpopular opinions. Like, I agree with everything you say there. Who's going to disagree with that?

**Adam Staravia:** Well, you agree with how you execute. What you may not agree with is that where -- you said we're doing it all wrong, basically, or something like that. We're focused on the wrong things...

**Mat Ryder:** I think most people are doing it wrong.

**Adam Staravia:** Most people.

**Mat Ryder:** I think like 90% of us are building software wrong, because we aren't obsessed with that. It needs a sound bite, doesn't it?

**Jerold Santo:** Okay, that's a little stronger way of saying it. There's your sound bite. Okay.

**Adam Staravia:** Well, I agree with connection, and the meeting the people that you're solving the problem for. That's key. You should do that, for sure.

**Jerold Santo:** Here's an actual unpopular opinion, now that we've heard your guys' lame ones. Here's a real unpopular opinion. And I know this is going to be unpopular, because I've said it before, and people haven't liked it.

**Mat Ryder:** Oh.

**Jerold Santo:** So I'm going to say it again...

**Mat Ryder:** Here we go...

**Jerold Santo:** ...and see if people like it. Automagically - you know, the word automagically... That's a dumb word. We shouldn't use it. I don't like that word at all. To me, it says "I have no idea of how this works. Thankfully, nobody else does either. And I'm hoping the fact that nobody knows how it works is good enough to impress everybody." So you ask somebody, "How does that work?" and they say, "Well, it's automagical." And we're supposed to all be like "Oh, okay, it's automagical! Yay!" and then move on. No, it means you don't actually know. If you knew, you'd just explain how it worked. Because when you know how software works, it's not magic, is it?

**Mat Ryder:** No. But, counterpoint - it means you don't have to know how it works. You can just use it. It works. And you don't have to know.

**Jerold Santo:** Oh, you know what else means that? It's automatic. We already have a word for that. "It just works automatically." "Oh, okay. It just does it automatically." Why do we have to pull magic into it?

**Adam Staravia:** I don't know about that, Jerold... Nah. Let's push back a little bit.

**Jerold Santo:** Neither one of you agree with me... I'm telling you, this is an unpopular opinion.

**Mat Ryder:** Yeah, this could be...

**Adam Staravia:** Haha! Okay...

**Jerold Santo:** Because you guys don't like this.

**Adam Staravia:** Message received. Got it. So, "automagically" describes a process that's too complex, whereas automatically is just -- there's no complexity in there. The "magically" with "auto" makes the thing that you don't know how it works, that's too complex - you explain to it that way. "Automatically" doesn't simply describe something that's automagical, that's too complex, and you don't know how it works.

**Jerold Santo:** I disagree. \[laughter\]

**Adam Staravia:** "I disagree..."

**Jerold Santo:** That explanation was not automagical enough. It's just a spin. It's a bad spin on something that could be explained...

**Adam Staravia:** Do you believe in magic?

**Jerold Santo:** What kind of magic? Sleight of hand?

**Adam Staravia:** Well, do you believe in magic?

**Jerold Santo:** Are you gonna break into a song here?

**Adam Staravia:** No...

**Jerold Santo:** Um, I believe in sleight of hand. Like, in magic tricks, yeah.

**Mat Ryder:** You can't believe in sleight of hand.

**Jerold Santo:** Well, that's why I don't understand the question "Do I believe in magic?"

**Mat Ryder:** Is there a group out there like the flat-partners that are just like "No, we deny sleight of hand." If anything, they believe in magic, don't they? Because they think it's not sleight of hand.

**Jerold Santo:** Right.

**Adam Staravia:** That's right.

**Jerold Santo:** I just don't understand the question then.

**Adam Staravia:** Well, I was gonna break into a song, but you've ruined it...

**Jerold Santo:** \[laughs\] Well, I did everybody a service there...

**Adam Staravia:** But if you can somewhat agree that magic exists to some degree, like things happen that are very complex, that we don't know how they work... I mean, not literal magic, but like a version of things happening...

**Jerold Santo:** Okay. Do I believe in the unexplainable? Absolutely.

**Adam Staravia:** Okay, so that's a version of magic.

**Jerold Santo:** Do I believe that there's software that's completely unexplainable? Well, it shouldn't be. If you know your systems... Maybe it means "I don't want to explain it to you."

**Adam Staravia:** What is the context of this word being used that you loathe?

**Jerold Santo:** Engineers say it all the time.

**Adam Staravia:** \[01:34:02.12\] Who says it?

**Jerold Santo:** Engineers. And we put it on our marketing... Like, "And then it automagically just works." And you're like "Nah, this is marketing lingo. You're spinning me, and I don't like it." It's a dumb word.

**Adam Staravia:** Gotcha. I don't like to spin, okay? Don't spin me.

**Jerold Santo:** \[laughs\]

**Adam Staravia:** There was actually a book about Spin Selling. I grew up in sales; my origination into professionalism was in sales, and there's a book called Spin Selling. Look it up.

**Mat Ryder:** You can tell you're in sales, because you just said "My origination into professionalism."

**Jerold Santo:** \[laughs\] Yeah, that's some spin right there...

**Mat Ryder:** Try "My first job was in sales." \[laughter\]

**Jerold Santo:** Yeah. That was an automagical saying. That's funny. Yeah, I know -- Mat, I'm sure you've said it. I used to say it as well when I was a younger person... A lot of people love that term, automagical, and I've just gone sour on it. So it's unpopular. It's not a popular opinion.

**Adam Staravia:** I just didn't know it was that popular of a word.

**Jerold Santo:** Alright, listener, let us know it. Do you agree? There are three opinions here. Which one is the worst? Which one is the wurst? \[laughter\]

**Adam Staravia:** The wurst!

**Jerold Santo:** It's going to be mine. It's going to be mine.

**Adam Staravia:** Can we clarify that was not -- Mat, you were making fun, weren't you? Weren't you making fun?

**Jerold Santo:** No, that's his standard German accent.

**Adam Staravia:** That was just you're being funny doing an accent, right?

**Mat Ryder:** Yeah... What do you mean?

**Adam Staravia:** Okay, good. I just wanted to clarify that. \[unintelligible 01:35:22.04\] wanted to clarify that, because... For a little while there it just sat so wrong with me.

**Mat Ryder:** Oh, I'm sorry.

**Adam Staravia:** And I almost said something. I almost stopped the show.

**Mat Ryder:** You should if you feel like that. Absolutely. I mean, I celebrate different accents. I really love them, and so yeah, impersonating accents is like a fun hobby...

**Adam Staravia:** I was so close, man... My white towel was like --

**Jerold Santo:** Were you going to throw in the white towel?

**Adam Staravia:** You know, it was so close...

**Mat Ryder:** No one has a go at Liam Neeson on my watch... \[laughter\] Hang on, though... Hang on. It's okay to do a British accent, isn't it? Everyone does a British accent.

**Jerold Santo:** I don't... I can't.

**Mat Ryder:** Like, you have Jerold because I've heard you do it.

**Jerold Santo:** \[laughs\] I try not to, because I'm not good at it.

**Mat Ryder:** We like it.

**Jerold Santo:** No, I think accents are all in good fun. I think just the length of the read...

**Adam Staravia:** Well, as you went on, it became more and more caricature.

**Jerold Santo:** Well... I think we made it clear that it was in good fun. If not--

**Adam Staravia:** So I'm joking about ending the show, as you may know. I don't know if you knew that. I was kidding around about stopping the show. Nah, I wasn't going to stop the show. I was just being funny.

**Mat Ryder:** But it's a nice point, actually. It's a nice point. Because if somebody felt insulted by that, I'd be devastated, genuinely.

**Adam Staravia:** Right. Yeah, I wanted to clarify that. We were not trying to be insulting.

**Mat Ryder:** No, we were not trying to be. It's just natural talent.

**Jerold Santo:** It's just who he is. How and when do we end this?

**Mat Ryder:** Never?

**Jerold Santo:** I'm thinking like five minutes ago, probably... \[laughs\]

**Adam Staravia:** Probably... When I tried to say goodbye. "Goodbye!" I don't know.

**Jerold Santo:** Thanks, Mat...
**Adam Staravia:** It's over now...
**Jerold Santo:** Thanks for joining us for your final episode.

**Adam Staravia:** Well, you know what we could do, Jerold? We can play that song, "It's closing time." Tell me you remember this.

**Jerold Santo:** Hm... Semitonic.

**Mat Ryder:** Yes, Semitonic?

**Jerold Santo:** Of course.

**Mat Ryder:** I saw them live.

**Jerold Santo:** You don't have to go home, but you can't stay here.

**Adam Staravia:** Right. They were playing that song for us...

**Jerold Santo:** Oh, yeah...

**Adam Staravia:** ...when we were trying to do Beyond Code the first season, in that bar... We're like "We're trying to wrap up the last two interviews here. Come on, people."

**Jerold Santo:** Yeah. So we were at an after party at a conference, Mat... And this was a Keep Ruby Weird maybe?

**Adam Staravia:** Keep Ruby Weird yeah.

**Jerold Santo:** Keep Ruby Weird.

**Adam Staravia:** 2014.

**Jerold Santo:** At the after party, the DJ turned on Closing Time at 9:30. The party ended at 10. So you know, naturally, what you do then if you're a terrible DJ is you loop it. So he started looping Closing Time at 9:30 at it played literally for half an hour...

**Mat Ryder:** Maybe someone had his kids...

**Jerold Santo:** Are you trying to do Liam Neeson again? \[laughs\]

**Mat Ryder:** Maybe someone had his kids, yeah. \[laughter\]

**Jerold Santo:** Anyway... We couldn't even record our video show, because Closing Time was too loud in the background.

**Mat Ryder:** Ahh...

**Adam Staravia:** It was terrible.

**Mat Ryder:** That's so rude.

**Adam Staravia:** Oh, my gosh...

**Mat Ryder:** \[playing the guitar\]

"Closing time...

Open all the doors and let you--"

Yeah, I don't know it.

**Jerold Santo:** "You don't have to go home, but you can't stay here." I only remember that part.

**Mat Ryder:** \[playing the guitar\]

"Closing time...

Turn on the lights on every boy, every girl..."

\[original song 01:38:22.03\] Closing time... You don't have to go home, but you can't stay here...
