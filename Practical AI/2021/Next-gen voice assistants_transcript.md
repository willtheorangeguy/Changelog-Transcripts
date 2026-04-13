[0.00 --> 8.80]  I think a lot of people that aren't working in the field would assume that we're going to take a few years and kind of solve all this NLP and related stuff.
[8.80 --> 12.58]  Jan LeCun famously said that he's going to solve NLP in two years.
[12.96 --> 14.52]  How many years ago was that?
[15.08 --> 17.94]  I think like six, seven at this point. He's made great progress.
[18.28 --> 24.92]  Yeah, yeah, no doubt. No, I heard a similar thing. I think it was Eric Schmidt in a tweet. He was like, speech is a solved problem.
[24.92 --> 33.36]  I think Eric Schmidt showed a lot more wisdom than Jan LeCun did there, despite probably less intimate technology, I understand.
[33.66 --> 39.96]  Okay, but I got to ask this now. I'm curious because you said that and I know that it's not a static thing. It's done.
[40.10 --> 44.30]  I know that you're going to continue to make great progress. You've been doing that and you've been telling us about it through this.
[44.30 --> 55.40]  Where is this going and how does larger vision for the problem evolve over time to where you as a young man, a millennial, says this Gen Xer who's significantly older.
[55.80 --> 62.76]  How is this evolving over your lifetime to where you are remaining impassioned about solving this problem in the long term?
[63.04 --> 63.82]  What does that look like?
[66.56 --> 69.26]  Big thanks to our partners, Linode Fastly and Launch Darkly.
[69.26 --> 74.14]  We love Linode. They keep it fast and simple. Check them out at linode.com slash changelog.
[74.30 --> 80.34]  Our bandwidth is provided by Fastly. Learn more at fastly.com and get your feature flags powered by Launch Darkly.
[80.60 --> 82.32]  Get a demo at launchdarkly.com.
[82.84 --> 85.40]  This episode is brought to you by our friends at O'Reilly.
[85.62 --> 91.90]  Many of you know O'Reilly for their animal tech books and their conferences, but you may not know they have an online learning platform as well.
[91.90 --> 96.70]  The platform has all their books, all their videos and all their conference talks.
[97.06 --> 103.14]  Plus, you can learn by doing with live online training courses and virtual conferences, certification practice exams,
[103.14 --> 107.82]  and interactive sandboxes and scenarios to practice coding alongside what you're learning.
[107.82 --> 117.52]  They cover a ton of technology topics, machine learning, AI, programming languages, DevOps, data science, cloud, containers, security,
[117.78 --> 121.76]  and even soft skills like business management and presentation skills.
[121.90 --> 123.68]  You name it, it is all in there.
[123.68 --> 129.18]  If you need to keep your team or yourself up to speed on their tech skills, then check out O'Reilly's online learning platform.
[129.72 --> 133.24]  Learn more and keep your team skills sharp at O'Reilly.com slash changelog.
[133.36 --> 135.64]  Again, O'Reilly.com slash changelog.
[135.64 --> 156.10]  Welcome to Practical AI, a weekly podcast that makes artificial intelligence practical, productive, and accessible to everyone.
[156.44 --> 160.50]  This is where conversations around AI, machine learning, and data science happen.
[160.50 --> 166.88]  Join the community and Slack with us around various topics of the show at changelog.com slash community and follow us on Twitter.
[167.00 --> 168.60]  We are at Practical AI FM.
[174.96 --> 177.88]  Welcome to another episode of Practical AI.
[178.20 --> 179.82]  This is Daniel Whitenack.
[179.94 --> 185.88]  I am a data scientist with SIL International, and I'm joined as always by my co-host, Chris Benson,
[185.88 --> 190.10]  who is a principal emerging technology strategist at Lockheed Martin.
[190.10 --> 191.06]  How are you doing, Chris?
[191.38 --> 192.60]  I am doing just fine.
[192.66 --> 193.32]  How's it going, Daniel?
[193.52 --> 194.26]  It's going great.
[194.36 --> 195.12]  No complaints.
[195.30 --> 204.12]  Took a few days off last week and a short week this week, so I'm rushing to get things done this week, I guess is how it is.
[204.48 --> 210.68]  It's supposed to recharge the batteries and make you feel all refreshed, but you just end up having to do all the same work and get it done faster.
[210.86 --> 211.44]  I get it.
[211.50 --> 217.90]  Yeah, I have known people in my life that do a really good job of front-loading some of that before they leave.
[217.90 --> 221.26]  For some reason, I've never been able to figure that out.
[221.70 --> 222.46]  No, neither have I.
[222.62 --> 224.96]  I think that's like a superpower that people have.
[225.06 --> 226.24]  It's a vacation superpower.
[226.68 --> 227.36]  Yeah, yeah.
[227.44 --> 229.26]  It's not something I've ever acquired, sadly.
[229.50 --> 230.54]  Yeah, maybe someday.
[231.02 --> 231.22]  Yeah.
[231.22 --> 235.60]  I have to go into vacations highly stressed out because of everything that I was trying to get done.
[236.12 --> 238.36]  So I guess that makes the vacation all the more important.
[238.70 --> 239.24]  Maybe so.
[239.42 --> 239.90]  Maybe so.
[240.38 --> 256.50]  Well, one of those things that I'm definitely working on right now and trying to get out the door is a couple changes to some of our internal speech dialogue-related technology, which is part of the reason why I'm really excited today about the topic.
[256.50 --> 262.10]  Because we've got a great guest, the CEO and co-founder of PolyAI, Nikola Merkcic.
[262.52 --> 263.00]  Welcome.
[263.40 --> 264.16]  Thank you for having me.
[264.28 --> 265.00]  It's great to be here.
[265.52 --> 265.78]  Yeah.
[265.96 --> 277.96]  So before we get into all sorts of speech and voice and dialogue-related things, maybe you could just share a little bit of dialogue with us about your background and how you got to do what you're doing now.
[278.24 --> 278.86]  Yeah, for sure.
[279.04 --> 282.16]  So look, I'm the CEO and co-founder of PolyAI.
[282.16 --> 289.62]  I did a PhD with a guy called Steve Young back at Cambridge with my two co-founders, Sean Wen and Eddie Su.
[290.54 --> 298.68]  And, you know, we worked on building dialogue in an academic context for a long time, since 2006 when Steve founded the group.
[298.68 --> 308.70]  And, you know, Steve started working on this stuff back when speech error rates were about 20%, which means that kind of like one in five words that you say would be kind of like misrecognized.
[308.78 --> 313.72]  And typically it would be the one word that you needed to get right to understand what the meaning of the sentence was.
[314.00 --> 314.32]  Of course.
[314.32 --> 327.18]  So, you know, kind of like building a formalism on top that would kind of like let you model the uncertainty, predict all the right things, know when you got something wrong, disambiguate, ask a question, implicitly confirm something.
[327.52 --> 328.58]  It's an art, right?
[328.58 --> 337.68]  And I'm sure we'll talk about all of it, but the squat or the deadlift of, you know, just kind of like doing machine learning and NLP, right?
[337.72 --> 353.84]  Because it involves natural language understanding, dialogue management, response generation, interacting with the external world, its knowledge bases, specific different tasks, all the way into the natural language generation, figuring out what to say in human language again.
[353.84 --> 359.82]  And then producing it again in an audio format, which is, you know, as human sounding as possible.
[359.82 --> 362.42]  So it's a real compound movement and you have to get it all right.
[362.64 --> 364.20]  So it's a really difficult task.
[364.34 --> 365.54]  It's why I got into it.
[365.88 --> 367.52]  It's why I stayed passionate about it.
[367.52 --> 374.10]  And, you know, my whole team is really a group of people who worked on it long before this new hype of conversational AI came about.
[374.50 --> 376.10]  And we worked on it for a while.
[376.26 --> 383.82]  Our previous company also spit out from the University of Cambridge, VocalIQ, was acquired by Apple in 2015 to make C.
[383.84 --> 388.74]  Siri more conversational to give it a bit more of an ability to have a back and forth conversation.
[389.32 --> 395.26]  And that kind of like in academic terms, the multi-turn task oriented dialogue is something we've stayed passionate about.
[395.26 --> 402.74]  And at PolyAI, we're building voice assistants for customer service, helping brands create something that's a superhuman customer experience, right?
[402.76 --> 411.36]  For anything that's short to moderate or even high complexity, putting in automated agents that sound at least as good as your best agents.
[411.36 --> 413.68]  They have answers to all the right questions.
[413.84 --> 419.74]  They're always current, up to date, and they're able to provide a superb level of customer service.
[419.96 --> 424.40]  And if they're not, they hand off to their human colleagues as kind of like supervisors or two agents.
[424.40 --> 433.08]  So you mentioned one thing, like a phrase, multi-turn voice enabled dialogue, I think is what it was.
[433.08 --> 446.86]  So maybe you could just kind of set that in context for some of the, like, what are the categories of sort of dialogue and voice enabled dialogue that are out there?
[446.86 --> 448.98]  Like, probably most people are familiar with Alexa.
[449.52 --> 452.28]  Is that multi-turn voice enabled dialogue?
[452.50 --> 459.12]  What are the sort of categories of things out there that people are doing in terms of interacting via speech?
[459.62 --> 463.00]  Yeah, I mean, there are many ways you can kind of layer out the taxonomy here.
[463.00 --> 473.88]  I think, you know, when you think about Alexa, Google Assistant, Siri, and you ask if they're multi-turn, if you can really have a dialogue, a conversation, as opposed to just have many questions answered.
[474.72 --> 480.36]  The truth is primarily they're single-turn question answering or kind of like simple task execution systems.
[480.50 --> 483.94]  But then again, you know, they're working really hard on making them multi-turn.
[483.94 --> 496.10]  Now, one reason why it's really hard to build a general multi-turn voice assistant for, you know, consumers of all shapes and sizes is that they have very different requirements.
[496.10 --> 497.98]  They're trying to do different things.
[498.12 --> 500.72]  So, like, it's actually a task of enormous complexity.
[500.98 --> 509.34]  When it comes to the things that we do, they're a bit less complex in scope because we build things to help you change your ticket for an upcoming flight.
[509.34 --> 520.06]  Or maybe you're making a reservation for a restaurant or you're trying to debug your router, which stopped working and you're having, like, connectivity issues.
[520.36 --> 523.20]  Or, you know, you're calling your bank and updating your address.
[523.32 --> 524.36]  So, these are all things we do.
[524.86 --> 531.88]  And the one thing that's important about that task-oriented bit of the nomenclature is that it lets you evaluate.
[532.10 --> 535.38]  And when you can evaluate, that means you're doing good science and you can improve.
[535.38 --> 542.84]  Now, evaluating something that does as many things as Siri or Alexa, it's hard, right?
[542.88 --> 543.76]  Because building them is hard.
[543.86 --> 545.28]  Evaluating them is hard.
[545.72 --> 551.12]  Knowing what you should be expecting and where product market fit for them is, it's one hell of a task.
[551.44 --> 551.56]  Yeah.
[551.66 --> 561.42]  So, when you're saying a turn, just to kind of get into some of this jargon, a turn would be, like, you say something to your smart speaker and get a response.
[561.72 --> 562.82]  Is that sort of what you mean?
[562.82 --> 576.28]  And then in your multi-turn, like, if you're trying to debug your router or you're changing your flight ticket or something, that is likely going to take more interactions than a, like, uttering something and getting a response.
[576.38 --> 576.90]  Is that correct?
[577.14 --> 577.56]  For sure.
[577.66 --> 577.94]  For sure.
[577.94 --> 592.76]  So, yeah, I mean, the whole reason we talk about turns is that, for the most part, the dialogue systems today, from kind of like the voice assistants of the large tech giants to automated customer service to chatbots are built on what's known as the turn-taking paradigm, right?
[593.12 --> 600.60]  So, the assumption, and it's a strong one, and it's not something that necessarily holds in human speech, is that you're going to wait for me to finish before you start speaking.
[600.60 --> 607.46]  And the assumption is that you've also absorbed all the information that I've tried to relay over to you before you started speaking.
[607.68 --> 609.90]  Then we're taking turns speaking.
[610.42 --> 617.68]  And, yeah, a multi-turn conversation is kind of like anything that takes more than one turn to achieve a task, right?
[617.68 --> 621.68]  I also have something I actually want to take you back for a minute because you said something interesting.
[622.02 --> 627.46]  I'm curious about your perspective compared to someone like myself who doesn't have your expertise doing this.
[627.46 --> 646.60]  When you were talking about, you know, Alexa and Google Assistant being hard, and you used the word hard associated with that several times, I really couldn't help wonder, as someone who has been doing this as long as you have, you know, starting with those Steve Young days and moving forward to the present, when you say it's hard, I'm kind of curious what you're thinking.
[646.60 --> 651.32]  You know, you're compressing it all into a single word, but how are you thinking about that?
[651.52 --> 653.36]  As you were saying that, I kept wondering that.
[653.74 --> 654.28]  Okay, okay.
[654.38 --> 655.62]  No, that's a really good question.
[655.62 --> 657.40]  I say it's hard because it's enticing.
[657.62 --> 657.92]  It's fun.
[658.00 --> 658.82]  It's a big problem.
[658.92 --> 665.66]  I expect to spend, you know, the rest of my life solving it and to be maybe a small cog in the wheel of how that ends up being solved.
[666.00 --> 678.22]  It's a hard problem on a pure academic level because it's that compound movement of different NLP tasks that all need to work really well, and they need to communicate with each other, which is something that we've not really yet cracked, right?
[678.22 --> 685.02]  So, say, the thing at the center of a dialogue system, language understanding, is not a task that's fully well-defined just yet, right?
[685.02 --> 686.60]  So, say, think of speech recognition.
[686.78 --> 691.72]  In most languages, you say something, there's exactly one way of writing it down.
[691.88 --> 694.14]  But natural language understanding, well, what does it mean?
[694.24 --> 695.46]  How do you choose to interpret it?
[695.74 --> 701.60]  What are the kind of, like, things you're choosing to take away from even, like, an order or something as simple as that, right?
[701.60 --> 705.08]  So, there, a lot is left to the interpretation.
[705.42 --> 712.76]  And that means that it stops really being, you know, a science or even a field of engineering where you have a clear metric to beat.
[713.00 --> 720.24]  Because really, what we've shown over the past 10 years, especially with machine learning, is that you give something a clear evaluation.
[720.24 --> 726.84]  And, you know, the share force and the intellectual power of the people working on it will crush it, right?
[726.84 --> 730.96]  If you, say, think about question answering and the squad data set, right?
[730.96 --> 735.22]  I remember the leaderboard on the Stanford website, I believe.
[735.72 --> 738.80]  And, you know, first, I think, like, the scores were, like, pretty low.
[738.80 --> 745.38]  And then, all of a sudden, like, three, six months in, we got to the point where, like, performance was unbelievable.
[745.72 --> 747.16]  I couldn't believe that it's that good.
[747.34 --> 752.32]  And it's because when you define a clear scope for a problem, we'll build the machinery to solve it, right?
[752.64 --> 757.86]  Now, when it comes to building these voice assistants, we don't know what machinery to build.
[758.20 --> 760.06]  The truth is we've built a lot, right?
[760.14 --> 761.12]  Alexa is manned.
[761.26 --> 764.88]  I like to compare these assistants to aircraft carriers, right?
[764.88 --> 769.88]  And you think about Alexa, 14,000 people, right, building that thing.
[770.44 --> 774.72]  And if you think about the ROI, they're not building it because they're making a ton of money on it.
[774.78 --> 779.58]  They're investing in the future because, well, I mean, Amazon always has the math around it, right?
[779.66 --> 781.22]  And, you know, I hope they're right.
[781.58 --> 786.98]  In any case, it's really good for us because they've actually indirectly funded a big growth in the area.
[787.10 --> 791.66]  They've allowed us to, you know, in turn build a lot of stuff ourselves.
[791.66 --> 793.84]  But we were doing it before they got interested, right?
[793.84 --> 797.18]  And the problem itself is, it's hard.
[797.30 --> 797.42]  Yeah.
[797.48 --> 801.72]  I mean, it's a good word to use because you have to solve a lot of these different problems.
[801.86 --> 808.02]  You have to solve things that are not just in the domain of machine learning, but also like human computer interaction.
[808.28 --> 812.70]  Like the voice user experience is something that academics tend to overlook.
[812.82 --> 814.28]  They don't appreciate that.
[814.28 --> 825.66]  Sometimes just the tone or something like that is much more likely to prolong a conversation and imbue the caller with enough patience and goodwill to go through a conversation, right?
[825.78 --> 830.16]  Equally, people who are very good at user experience don't tend to be mavericks at machine learning.
[830.16 --> 832.82]  And then kind of bringing it all together to build something.
[833.04 --> 835.24]  It takes a lot of different personas, people.
[835.46 --> 837.46]  It's even that is hard.
[837.78 --> 839.56]  So, yeah, I guess that's what I mean.
[839.94 --> 842.26]  You're talking about the human computer interaction.
[842.26 --> 856.50]  And maybe you could speak a little bit to like, I think the way in which people interact with whether that be like a text chat bot or a voice assistant or something is different than how they might interact with another human.
[856.72 --> 865.72]  What are some of those differences in terms of ways that people interact with those systems versus like their friend and meeting them at the coffee shop?
[865.72 --> 866.54]  Oh, for sure.
[866.68 --> 873.24]  I mean, I think that we could spend a lot of time just talking about the differences between voice and chat, right?
[873.32 --> 874.76]  And how people interact there.
[874.76 --> 881.86]  I mean, people will dispense with pleasantries and they'll tend to use shorter sentences when they operate with technology.
[882.20 --> 883.00]  They'll swear more.
[883.56 --> 887.78]  A big chunk of input going into all the large tech companies' assistants are.
[887.78 --> 899.00]  I'm sure you have a huge database now of incredibly explicit and abusive language that people have said to their bot.
[899.28 --> 901.26]  We've maybe got a few colorful examples.
[901.62 --> 912.88]  I can tell you for a fact that we have a lot less, you know, percentage wise than the large tech companies where the number of turns coming into these assistants with profanities can reach double digit percentages.
[913.52 --> 914.96]  Part of it is just human nature.
[914.96 --> 919.70]  Like, what do you do when you can like use a new technology that understands you?
[919.82 --> 921.34]  Well, you swear at it because why not?
[921.46 --> 921.60]  Right.
[921.72 --> 922.80]  Let's see what it does.
[923.40 --> 926.82]  And, you know, I mean, hopefully you've tried it at some point or hopefully.
[926.98 --> 927.96]  I don't know why hopefully.
[928.62 --> 938.58]  But, you know, things like Siri will have really good kind of like, you know, backup mechanisms to be sassy or to tell you off when you've cursed at them.
[938.58 --> 942.62]  Or even when they think you might have, which can happen because speech recognition is not perfect.
[942.62 --> 951.56]  But, yeah, I mean, the other thing that's always interesting with technology is, you know, what do people build first when a new kind of framework comes to mind?
[951.66 --> 954.38]  And I use this in one of our first kind of like investor pitches.
[954.38 --> 965.60]  But at the time, the top four applications with Alexa were things that allowed the system, I think, to read recipes out loud, which is kind of cool.
[966.08 --> 970.42]  And then the remaining three were meowing, farting and barking.
[971.06 --> 971.18]  Right.
[971.18 --> 981.34]  And finally enough, the top revenue grossing app when the iPhone was released was something playing one of those kinds of sounds.
[981.52 --> 982.68]  You can probably guess which one.
[983.22 --> 985.74]  And I guess it's a pattern of how technology evolves.
[985.82 --> 990.32]  But people tend to do these kind of like simple things that are just hacks where they have a bit of fun.
[990.60 --> 992.62]  And then they go and they build like life changing things.
[992.62 --> 1010.88]  This episode is brought to you by our friends at Rudderstack.
[1011.10 --> 1015.60]  And we're calling all data engineers to check out Rudderstack Cloud and start building smart customer data pipelines.
[1016.10 --> 1017.84]  Rudderstack is warehouse first.
[1018.04 --> 1019.02]  No more silos.
[1019.02 --> 1028.52]  Rudderstack builds your customer data lake on your data warehouse, not theirs, enabling all functionality of a CDP with more security and retaining full ownership of your data.
[1028.82 --> 1031.28]  It's open source and API first.
[1031.60 --> 1035.04]  Rudderstack can be easily integrated into your existing development processes.
[1035.60 --> 1038.36]  And because they're open source, you can see all their code.
[1038.56 --> 1041.00]  So you don't have to worry about vendor lock in or black boxes.
[1041.54 --> 1043.12]  And best of all, they have transparent pricing.
[1043.30 --> 1045.56]  Stop paying your CDP a premium to store your data.
[1045.56 --> 1050.92]  Rudderstack is free up to 500,000 events and pricing scales transparently from there.
[1051.40 --> 1053.38]  Learn more and get started at Rudderstack.com.
[1053.64 --> 1055.92]  Again, Rudderstack.com.
[1056.06 --> 1059.62]  That's R-U-D-D-E-R-S-T-A-C-K.com.
[1059.62 --> 1078.36]  So, Nicole, you're talking a little bit about different applications of voice technology, but also the way people interact differently with even chat versus voice.
[1078.36 --> 1088.92]  From your perspective as someone who's really, you know, hands-on working with customers in this space, what makes for a good voice use case?
[1088.92 --> 1098.40]  From my perspective, people maybe don't have a great grasp on yet in terms of like, yeah, we all think voice technology is maybe going to be like a huge thing.
[1098.58 --> 1102.82]  And we can see really cool applications of it and maybe even really useful applications.
[1102.82 --> 1116.98]  But it might be hard for people to visualize, you know, what is a good voice application and what are the benefits of that as compared to, you know, creating a text-based search or creating like other things?
[1116.98 --> 1119.60]  Like when should I be thinking maybe voice?
[1120.20 --> 1126.14]  As you answer that, can you kind of differentiate between voice and chat just for people who aren't intimately familiar with the use cases?
[1126.14 --> 1133.80]  Yeah, for sure. For sure. So, you know, I think that there is a bigger question of like where you want to use voice as an interface to technology.
[1134.52 --> 1140.56]  And then there's just the more narrow question of where you want to use voice or text when dealing with customer service.
[1140.98 --> 1147.86]  Right. And the only other interface you really have other than language are good graphical user interfaces.
[1148.04 --> 1153.42]  Right. So let's say, you know, like smartphone apps and, you know, kind of like the web.
[1153.42 --> 1162.96]  Right. I mean, obviously, the language based ones are better if you're on the move or if you just simply you're not in front of a computer or if you want to do something really quickly.
[1163.18 --> 1168.28]  Now, how the whole like AR, VR space will evolve, it's hard to predict, but we know it's coming.
[1168.80 --> 1178.76]  And there the role of voice in particular is going to be, you know, kind of like much, much larger than what you see when you interact on the web or with mobile.
[1178.76 --> 1183.50]  Mobile, in fact, is the worst one because, you know, you're kind of holding your phone.
[1183.60 --> 1187.88]  It's a bit awkward. You're typically surrounded by people. It's awkward to speak into your phone.
[1188.06 --> 1193.92]  And really, you know, the place where voice on a phone has really been successful is kind of like hands free while driving.
[1194.04 --> 1196.46]  And there Siri gets a tremendous amount of usage.
[1196.94 --> 1205.00]  When you think about the web, I think that's where chat is a natural interface for customer service compared to speaking often.
[1205.00 --> 1210.38]  Because, you know, you might be at work, you might be, you know, speaking to your bank or dealing with something.
[1210.50 --> 1213.80]  And you don't want your colleagues to know that you're actually doing that at work.
[1213.88 --> 1218.54]  So chat is pretty useful or maybe it's early in the morning and you don't want to wake up other members of your household.
[1219.04 --> 1225.88]  But in reality, you know, 60 to 70 percent of all customer service interactions happen over the phone.
[1225.88 --> 1234.74]  Right. And they happen with voice because, you know, in this day and age where you could easily transcribe all this and have all sorts of channels, we're doing this podcast.
[1235.02 --> 1238.12]  Right. Well, while recording it, I see you guys and you see me.
[1238.46 --> 1241.54]  But the end product is just voice because people can consume it anywhere.
[1241.80 --> 1246.64]  It gives them a pretty good feel for kind of like what kind of people we are, how we talk, our style.
[1247.08 --> 1249.24]  A lot of emotion goes through that voice.
[1249.24 --> 1251.34]  And it's also a really high bandwidth channel.
[1251.64 --> 1257.04]  Right. I can probably type a bit faster than I speak, although it depends.
[1257.16 --> 1258.40]  I tend to speak quite fast.
[1259.12 --> 1261.58]  But really, I have a lot more fun when I speak.
[1261.72 --> 1265.04]  And, you know, it lets me kind of express myself a lot more fully.
[1265.46 --> 1271.88]  And, you know, if you think about just the need to capture that channel when it comes to customer service,
[1271.88 --> 1279.44]  when COVID hit, you know, everyone thought big, you know, crisis like these tend to accelerate technology adoption.
[1279.66 --> 1288.80]  Right. And for, you know, close to a decade now, companies have invested in digital transformation in order to push people to digital channels.
[1288.94 --> 1295.00]  Mostly chat, either web chat where they're humans on the other end or kind of like chat with an automated system.
[1295.00 --> 1297.22]  And the hope there was it's cheaper.
[1297.80 --> 1304.78]  Some people, especially those heavily invested in these projects, would tell you that, you know, it's the channel of the future.
[1305.10 --> 1306.80]  Younger people prefer doing it.
[1307.14 --> 1309.02]  Well, look, I mean, I'm a millennial.
[1309.12 --> 1310.62]  I've got a PhD in computer science.
[1310.96 --> 1314.92]  I grew up playing computer games and, you know, like not seeing the sun.
[1315.46 --> 1316.18]  And guess what?
[1316.24 --> 1318.00]  When I need customer service, I like to call.
[1318.22 --> 1320.58]  Right. And like I have a bit of anxiety calling in.
[1320.82 --> 1322.38]  Right. Like most millennials do.
[1322.38 --> 1324.56]  I still prefer to call because it gets the job done.
[1324.56 --> 1331.18]  The alternative is you're typing and then someone responds in four minutes because they're actually speaking to 10 people at the same time.
[1331.70 --> 1333.28]  And it's not really a better experience.
[1333.42 --> 1337.28]  And with COVID, you know, people thought, well, hey, now's the time for chatbots to take over.
[1337.42 --> 1344.72]  They'll go from their 10, 15 percent of the market share, heavily augmented by the fact that you're being forced onto that channel.
[1344.92 --> 1348.02]  And the hope was now it's going to go to like a much higher percentage.
[1348.58 --> 1352.64]  Truth is COVID hit, call center volumes went up.
[1352.64 --> 1356.92]  Now, the stuff went down because of social distancing or mandatory lockdowns.
[1357.26 --> 1359.96]  But really, people kept calling and it's dispelled that myth.
[1360.36 --> 1366.56]  Now, in our case, it's been really great for Poly AI because we build voice based systems for customer service.
[1366.90 --> 1374.46]  And it's been a big boon, especially in getting into those industries that previously might have hesitated to build this kind of futuristic technology.
[1374.46 --> 1376.42]  But it's not going away. Right.
[1376.48 --> 1380.44]  And as time passes, you've got a smart speaker in every part of your house.
[1380.64 --> 1383.04]  At some point, you'll have some kind of wearable.
[1383.16 --> 1384.98]  They'll capture your voice really, really well.
[1385.56 --> 1390.70]  It's going to be really convenient to just say like, oh, hey, turn on my thermometer and order pizza.
[1391.04 --> 1392.52]  I mean, we can talk about these scenarios.
[1392.52 --> 1398.56]  I'm curious, though, as we're about to dive into that next, do me a favor and set some context for me.
[1398.68 --> 1403.50]  For those of us like both of you guys are experts in natural language processing.
[1403.92 --> 1406.68]  I'm one of those interested people, but I'm not an expert like you.
[1406.82 --> 1411.18]  And we've talked about having this multi-turn dialogue and these interactions.
[1411.18 --> 1418.82]  As you're going and solving this for people out there and providing these capabilities that we're all getting excited about,
[1419.26 --> 1425.82]  could you talk a little bit about what it is that you have to be thinking about in that pipeline as you're doing multi-turn?
[1425.96 --> 1431.24]  What are the things that are part of that consideration for those of us who are not as intimately familiar with that?
[1431.60 --> 1432.08]  Okay.
[1432.50 --> 1437.74]  So if you think about kind of like that cycle of building a dialogue system, especially if it's voice based,
[1437.74 --> 1441.16]  the first step in it is speech recognition, right?
[1441.24 --> 1443.90]  Kind of like transcribing what you think the user said.
[1444.18 --> 1448.44]  If you're doing it in the best way possible to maximize performance,
[1448.72 --> 1453.70]  the output of that is not a single sentence, but instead something that is a lot more complicated.
[1454.54 --> 1456.48]  A bit more complicated is an NBEST list.
[1456.72 --> 1459.82]  So kind of like maybe 10 different hypotheses of what you might have said.
[1460.00 --> 1462.30]  So let's say I want to get Serbian food, right?
[1462.34 --> 1463.14]  And I said it fast.
[1463.24 --> 1465.74]  So is it Serbian, Siberian, Syrian?
[1465.88 --> 1466.84]  You're not sure, right?
[1466.84 --> 1468.70]  Or like I want to work for free people, right?
[1469.04 --> 1471.18]  Like did I say three or did I say free?
[1471.68 --> 1472.70]  Well, of course, what?
[1473.18 --> 1477.50]  If we go into just like that technology, the language model there would basically say,
[1477.64 --> 1479.50]  hey, it's more likely that they said three people.
[1480.24 --> 1483.96]  But then again, free people is also something that you tend to see quite often in Texas.
[1484.04 --> 1485.06]  So it's not impossible.
[1485.56 --> 1489.76]  So a good system will tell you, I think it's three people, but it might be free, right?
[1490.10 --> 1493.82]  And equally Serbian, Syrian, a few other hypotheses, right?
[1493.82 --> 1497.18]  So then the next thing that comes is natural language understanding.
[1497.36 --> 1506.64]  Taking what the user said and parsing it and saying like in some ontology that I have previously defined that I need to interact maybe with the external world.
[1506.74 --> 1508.90]  So let's take booking as an example.
[1508.98 --> 1511.72]  If I say, hey, I want to come in with me and my fiance, right?
[1511.72 --> 1514.08]  That actually means two people, right?
[1514.48 --> 1523.04]  And it's not NLP as in like parsing who the entities are because while it could be useful in a composite task of counting up how many people there are in the request,
[1523.14 --> 1527.98]  really what you need to know is that I've initiated a booking request and how many people I've asked for.
[1528.08 --> 1528.86]  And it's two people.
[1528.94 --> 1536.48]  And that's actually a really, really hard thing to do because like actually parsing those words and saying, uh-huh, two people, that's complicated, right?
[1536.48 --> 1547.70]  Then the next thing is like let's turn it into – in very traditional dialogue system literature, this would be called the dialogue act where I've kind of like informed that number of people is two.
[1548.46 --> 1554.16]  And, you know, that would then go off into a dialogue manager that would say like, okay, well, do I have something for two people?
[1554.26 --> 1556.64]  And then what you'd know is, well, like, sorry, when?
[1557.08 --> 1562.16]  And then the system would have to go and say like, well, like, you know, request the time for the booking, right?
[1562.16 --> 1569.38]  Now request time, if you respond like that, you'd sound a bit like – not even like Jarvis, you'd sound like the Terminator or – well, I don't know.
[1569.46 --> 1571.02]  You'd sound like a really bad voice assistant, right?
[1571.16 --> 1571.96]  Request a time.
[1572.30 --> 1573.36]  Yeah, for sure.
[1573.60 --> 1576.58]  So, you know, you need to turn that into like, hey, what time would you like to come in, right?
[1576.62 --> 1577.62]  And then you have to sit.
[1577.82 --> 1581.30]  So that's kind of like natural language generation, another big subfield of NLP.
[1581.92 --> 1586.58]  And then finally, if you want to produce it in audio, you'd have to use a text-to-speech engine, right?
[1587.12 --> 1588.82]  And that would convert it into audio.
[1588.94 --> 1589.80]  You would play it back.
[1589.80 --> 1597.78]  And then the big thing kind of like in understanding everything and having a good conversation would be kind of like the bigger task of dialogue management,
[1597.78 --> 1606.36]  looking at the whole previous set of things that were said and using it to augment the prediction in every subsequent turn.
[1606.48 --> 1610.20]  So let's say I said, you know, you might have thought that I said free people.
[1610.36 --> 1615.26]  But if I repeat free people in the next turn, then that kind of alternative hypothesis is probably true.
[1615.26 --> 1618.00]  And the system should figure it out like, hey, why is he repeating it?
[1618.38 --> 1619.06]  Doesn't sound right.
[1619.06 --> 1620.02]  Let's try that other one.
[1620.12 --> 1621.08]  Did you say three people?
[1621.52 --> 1623.34]  Well, so you can choose to confirm if you're uncertain.
[1623.70 --> 1631.34]  And there, there's a lot of machinery around how you handle that probability distribution, uncertainty, a lot of Bayesian methods that come into play.
[1631.68 --> 1632.60]  It's a pretty serious discipline.
[1632.60 --> 1633.28]  Yeah.
[1633.28 --> 1642.56]  So now if you take that like series of steps that you've laid out, obviously, PolyAI is working in all these areas.
[1642.56 --> 1649.22]  But I was wondering if you could maybe talk about like, where do you feel like you're having to spend most of your time?
[1649.56 --> 1652.04]  There's probably open challenges in each of those areas.
[1652.04 --> 1659.72]  But maybe where's the biggest open challenges in terms of advancing this field along that pipeline of things?
[1659.90 --> 1660.04]  Yeah.
[1660.04 --> 1667.16]  When it comes to kind of like, you know, where we focus, one place where we don't spend a lot of effort is speech recognition.
[1667.16 --> 1672.66]  The speech recognition task itself, because that's one which is pretty well defined, commoditized.
[1672.66 --> 1674.60]  A lot of people are playing there.
[1674.82 --> 1676.20]  A lot of progress has been made.
[1676.46 --> 1678.64]  Big tech companies are pouring in millions.
[1678.80 --> 1683.18]  And that's great for us because we're just getting a better product that we then get to build on.
[1683.28 --> 1683.40]  Right.
[1683.58 --> 1693.74]  So we typically use often several speech recognizers in a single deployment to get that variance out so we can extract the best possible prediction out of all of them.
[1693.84 --> 1697.96]  So the more uncorrelated Google and Amazon are, the better our performance gets.
[1698.42 --> 1699.10]  And we love that.
[1699.14 --> 1700.64]  And we thank them for all their hard work.
[1700.64 --> 1710.68]  Now, when it comes to the piece where we really excel, and this is where we're really, really differentiated from your 1500 chatbot providers that a lot of them claim to do voice.
[1710.76 --> 1715.50]  But their idea of doing voice is, I'll put a speech recognizer and a text-to-speech engine there.
[1715.78 --> 1716.34]  It's going to be great.
[1716.76 --> 1719.64]  This is why they don't have many appealing voice applications out there.
[1720.00 --> 1726.08]  The piece that's really then exciting is what we like to call spoken language understanding as opposed to natural language understanding.
[1726.32 --> 1727.98]  So SLU versus NLU.
[1727.98 --> 1738.16]  And the difference there is you really have to consider the fact that there's a bunch of different speech recognition hypotheses that you can operate over to really figure out what's going on.
[1738.16 --> 1749.58]  The second bit is you also have to look at what happened previously in that conversation to know, again, how to kind of like tilt the outcomes to improve the accuracy.
[1749.76 --> 1758.24]  And then finally, one thing that we do really well, and that's really important, is as the conversation progresses, you can anticipate where the conversation is going to go.
[1758.24 --> 1766.58]  If I've asked you for how many people are coming in, or if I asked you about, you know, like, for example, what our systems can do is parse my name right.
[1766.88 --> 1772.42]  And Nikola Mrkšić will never be a common name in English-speaking environments.
[1772.80 --> 1774.56]  It's a hard name by Serbian standards.
[1774.56 --> 1791.66]  But if you know that, like, say, I told you my phone number and you're authenticating me, then if you inform the speech recognizer that Mrkšić is coming up, well, then they're actually quite likely to parse it correctly, even though it's an impossible collection of syllables in English.
[1791.98 --> 1793.38]  It's very unlikely even in Serbian.
[1793.74 --> 1797.22]  So, but if you know that it's coming, they can kind of wait out for it and be like, ah, that was it.
[1797.58 --> 1797.76]  Right.
[1797.76 --> 1799.18]  So, that's really important.
[1799.32 --> 1803.58]  And that spoken language understanding bit is what lets us do voice really, really well.
[1803.92 --> 1816.54]  Could you also just, for those who are coming along with us, as you talk about spoken language understanding, which may be a new term for some people, could you also just real quickly define, you've kind of talked about some of the qualities of that.
[1816.98 --> 1820.54]  Is there more of a formal definition or is this more of an informal way of addressing it?
[1820.60 --> 1821.42]  I'm just kind of curious.
[1822.12 --> 1823.70]  As you bring people into the terminology.
[1823.70 --> 1827.94]  Yeah, it's a formal research problem and it kind of like touches on different ones.
[1828.08 --> 1846.00]  But if we attempt a formal definition here in a specific dialogue task where we're, say, trying to accomplish something, it is this problem of taking an audio stream and turning it into actionable, parsable, kind of like slot value pairs, typically, or something like that.
[1846.00 --> 1852.42]  So, kind of like slots are things like maybe, say, date or location or number of people.
[1852.58 --> 1852.70]  Right.
[1852.70 --> 1862.26]  So, kind of like extracting that structured information that in the backend, your logic, so not AI, like your pure kind of like business logic knows what to do.
[1862.38 --> 1868.54]  Either it sends a booking request, it sends a query for a specific kind of information or something like that.
[1868.54 --> 1879.94]  So, rather than NLU, which is, you know, again, relatively complex to define when it comes to dialogue, is this, again, idea of extracting the same kind of information from a written sentence.
[1880.52 --> 1885.70]  Now, the thing about a written sentence is that there isn't any noise injected by the speech recognizer.
[1885.70 --> 1904.10]  Whereas in SLU, there's an audio file, which, you know, it's not only about a speech recognizer that may struggle to recognize a particularly complicated word that may be, you know, from a pharmaceutical or, I don't know, a travel domain or something that doesn't come up frequently, or it's a problematic last name.
[1904.22 --> 1906.68]  But really, maybe it's just background noise.
[1906.68 --> 1912.54]  Maybe it's the fact that the accent of the person is not something you're expecting, your model is not very good at it.
[1912.62 --> 1921.86]  Or it could be that, you know, increasingly they're speaking from two rooms away and you're, you know, seven microphones in, and Alexa device are insufficient to capture what they're saying.
[1921.94 --> 1927.44]  But, you know, we're people, our expectations are growing, and we expect that these things will work for us.
[1927.54 --> 1933.14]  And that's what makes the problem fun as well, because it's kind of like, you know, shifting goalposts, right?
[1933.14 --> 1936.60]  Just when we got it to work, when you normally speak on the phone, speak your phone.
[1936.92 --> 1939.24]  Once it works on the speakerphone, there's a baby crying in the background.
[1939.44 --> 1943.22]  And then you're driving, and there's a baby crying in the background, and someone's talking over you, right?
[1943.48 --> 1946.06]  So, and then you might want to switch language, right?
[1946.14 --> 1947.26]  So, it's fun.
[1947.58 --> 1949.06]  Like, it's a hard problem, as I said.
[1960.14 --> 1965.12]  We deserve a better internet, and the Brave team has the recipe for bringing it to us.
[1965.12 --> 1966.26]  Start with Google Chrome.
[1966.50 --> 1970.22]  Keep the extensions, the dev tools, and the rendering engine that make Chrome great.
[1970.40 --> 1971.28]  Rip out the Google bits.
[1971.42 --> 1972.08]  We don't need them.
[1972.40 --> 1974.92]  Mix in ad and tracker blocking by default.
[1975.20 --> 1977.90]  Quick access to the Tor network for true private browsing.
[1978.20 --> 1982.60]  And an opt-in reward system, so you can get paid to view privacy-respecting ads.
[1982.76 --> 1986.54]  Then turn around and use those rewards to support your favorite web creators like us.
[1986.86 --> 1991.46]  Download Brave today using the link in the show notes, and give tipping a try on changelog.com.
[1991.46 --> 1992.10]  Hello!
[2001.52 --> 2007.06]  As you were talking through some of the things about spoken language understanding,
[2007.38 --> 2014.26]  one of the things that you mentioned was things related to, like, specialized jargon, maybe,
[2014.48 --> 2016.22]  or particular accents.
[2016.22 --> 2019.74]  I guess my question is, like, let's say you're onboarding a new client.
[2020.10 --> 2025.10]  They're in a specialized domain, and they're trying to create this, you know, new voice assistant.
[2025.44 --> 2030.88]  At this point, how difficult is it to kind of onboard a person into that?
[2030.96 --> 2033.92]  How much, you know, data do they have to provide?
[2033.92 --> 2041.94]  And, like, how much are you able to sort of transfer things from your other use cases and common data that you have?
[2042.08 --> 2052.46]  Maybe both in terms of, like, restrictions between clients, because I'm sure you can't always share data that you've gathered from certain clients and use it to create things for other clients.
[2052.92 --> 2054.98]  How does that process work at this point?
[2055.04 --> 2058.02]  And how much pre-trained models can you use and that sort of thing?
[2058.02 --> 2059.32]  For sure. For sure.
[2059.72 --> 2066.52]  Well, I mean, I'm sure most of the listeners of this podcast know about the importance of pre-training for deep learning applications, right?
[2066.88 --> 2073.40]  I mean, it's typically, like, you figure out how to pre-train well and then, like, really good things in that subdomain of machine learning follow, right?
[2073.82 --> 2084.78]  So when it comes to natural language understanding, I can tell you, and I can, you know, talk about it for hours, about, you know, collecting data sets of 1,000, 2,000, you know, training examples.
[2084.78 --> 2090.28]  And we did this back at Cambridge. My co-founder, Sean, had this really good data set in a revolutionary paper.
[2090.42 --> 2094.32]  He had one of the first papers on kind of, like, training an end-to-end dialogue system.
[2094.42 --> 2098.60]  And that involved that kind of whole compound movement. It's a really well-cited paper, really good piece of work.
[2099.04 --> 2103.06]  And, you know, for that paper, he collected a data set of 600 training examples.
[2103.20 --> 2107.18]  And then for another paper of mine, I needed a bit more data, so he collected a bit more.
[2107.56 --> 2112.72]  And then I'd go through and annotate. He'd go through and check the annotations. I'd do it again.
[2112.72 --> 2119.48]  And it takes about a collective kind of like one week of work and leaves you with permanent, you know, kind of like mental health problems.
[2121.24 --> 2122.62]  I don't mean to. I don't mean to.
[2122.74 --> 2126.38]  I don't mean to. I joke about mental health. But it is a daunting task. It's no fun at all.
[2126.82 --> 2130.26]  So when we started PolyEye, we were like, this has to stop, right?
[2130.30 --> 2134.56]  We're never going to build amazing things if we're dependent on doing that.
[2134.68 --> 2139.50]  Because bear in mind, like, we're pretty highly qualified for creating this kind of data.
[2139.50 --> 2148.20]  So if it takes two people in the kind of like last stage of their PhD after years of doing this stuff to create that data set, like, that's not scalable.
[2148.20 --> 2164.32]  So what we then started doing was pre-training representation models for dialogues that would kind of like look at billions of conversations, things like Reddit, Quora, Twitter, and learn good representations for a dialogue.
[2164.32 --> 2171.18]  So that if I give you a set of kind of like, you know, turns, like you spoke, I spoke, you spoke, I spoke.
[2171.50 --> 2183.74]  And then I say like, hey, model, use the representation of the dialogue so far and the representation of a potential follow-up to determine whether it's a good follow-up to that conversation.
[2183.74 --> 2186.52]  So we would pre-train in that way.
[2187.02 --> 2192.84]  And if you do it like that, then you get a lot of training data out of things like Reddit, Quora, Twitter.
[2193.16 --> 2198.38]  And Reddit in particular is an incredible resource because people talk about all sorts of things on Reddit, right?
[2198.76 --> 2201.90]  And there are people from all over the world and in different languages as well.
[2202.36 --> 2206.14]  But also just like, let's think about English in all possible different dialects.
[2206.18 --> 2210.04]  You'll see anything phrased and rephrased there in a good way.
[2210.04 --> 2212.74]  And, you know, you can train this thing for a long time.
[2212.82 --> 2225.58]  And this encoder, Convert, that we have built is something that's, you know, in the family of models like BERT or GPT, where really, you know, it's pre-trained on a lot of data.
[2225.74 --> 2228.82]  But unlike those models, it's not really a language model.
[2228.94 --> 2231.12]  It's an encoding model for dialogues, right?
[2231.26 --> 2235.88]  And it's purpose-built and purpose-pre-trained for conversational AI.
[2235.88 --> 2248.42]  So then when you use this model to do things like intent detection, value extraction, all of these tasks that form that big compound movement of dialogue, it's a model that's really powerful, right?
[2248.44 --> 2253.96]  It takes much less data to get to a high level of performance than something being trained from scratch.
[2254.78 --> 2259.50]  And, you know, there's been a lot of benchmarking of this model.
[2259.50 --> 2271.00]  Salesforce recently came out with a study that confirmed that this is the most accurate or rather the best thing to pre-trained with to get the most accurate models with a limited amount of data or any amount of data, really.
[2271.44 --> 2272.88]  So this is really important, right?
[2273.02 --> 2278.50]  And then what we're able to do and what we bring into all of our deployments is this model, right?
[2278.82 --> 2287.32]  And then in all of these deployments, wherever there's not sensitive information, it's just more conversations that are used to subsequently tune that model.
[2287.32 --> 2298.02]  But we don't need to use specific, you know, nitty-gritty details of, you know, I don't know, how you collect British postcodes or how you spell Serbian last names.
[2298.36 --> 2300.22]  Like that stuff is a bit more proprietary.
[2300.58 --> 2304.58]  We have a lot of different technology that's used to counter those specific subproblems.
[2304.58 --> 2310.58]  And the truth is we often have to solve some of these challenges that are a bit separate, often very engineering heavy.
[2310.58 --> 2323.80]  But when it comes to like that data barrier that people think about, like that first step of building a dialogue system, which you need like a lot of data to train, like we need a lot less data because we've already spent years pre-training this thing.
[2323.80 --> 2327.46]  Yeah, this brings me to probably my favorite subject.
[2327.70 --> 2331.30]  Before the interview, I was reading your post about the convert model.
[2331.56 --> 2334.62]  You mentioned that it's pre-trained speech encoder in multiple languages.
[2334.92 --> 2338.68]  So, and I know that multiple languages is something that's emphasized on your website.
[2338.92 --> 2341.88]  And what is your thought process behind that?
[2341.92 --> 2348.06]  And maybe let's say that we're specifically talking about this language model.
[2348.06 --> 2355.80]  How have you gone about setting up that language model such that it enables you to solve problems in multiple languages?
[2356.14 --> 2358.36]  This is a personal academic passion of mine.
[2358.56 --> 2365.54]  So quite a few years ago, now one of my best friends, Ivan Vulic, who is a great multilingual NLP researcher.
[2366.14 --> 2366.86]  He's Croatian.
[2366.96 --> 2367.44]  I'm Serbian.
[2367.70 --> 2372.40]  We met in Beijing over a few years and we were like, well, how do we end up working together later?
[2372.50 --> 2374.58]  He worked on like multilingual NLP.
[2374.86 --> 2375.76]  I worked on dialogues.
[2375.76 --> 2379.42]  We were like, hey, can we like do something multilingual in this context?
[2380.02 --> 2381.46]  And there we got them really interested.
[2381.60 --> 2385.96]  And this was a time where kind of like word level, word vectors were older age.
[2386.06 --> 2389.62]  Things like the word-to-vec model, glove, and all those things.
[2389.98 --> 2392.68]  You know, Mikulov, Pennington, all those guys.
[2393.30 --> 2398.72]  And like this was the first wave of like massively mindlessly data-driven NLP.
[2399.10 --> 2399.28]  Right?
[2399.44 --> 2400.70]  And like I stand for that.
[2400.78 --> 2401.26]  I love that.
[2401.34 --> 2401.52]  Right?
[2401.60 --> 2403.26]  But I also love languages and its nuances.
[2403.44 --> 2403.62]  Right?
[2403.62 --> 2406.20]  So the question is like, well, okay, you train something in English.
[2406.28 --> 2407.56]  How do you port it to another language?
[2407.76 --> 2411.76]  Typically, older school NLP had like this pipeline of things running.
[2411.98 --> 2413.62]  You know, lemmatizers, stematizers.
[2414.48 --> 2416.58]  You know, parsing the sentence structure.
[2417.20 --> 2418.74]  And like that's different in different languages.
[2419.00 --> 2421.32]  Like the, you know, subject, verb, object.
[2421.66 --> 2423.52]  You know, it works differently in different languages.
[2423.86 --> 2428.00]  The morphology murders you in different languages.
[2428.00 --> 2428.30]  Right?
[2428.30 --> 2432.84]  Like if you go from word gender as a thing that exists in some, but not in others.
[2432.84 --> 2434.86]  In one language, word order matters.
[2435.02 --> 2436.46]  In others, you can do whatever the hell you want.
[2436.56 --> 2436.68]  Right?
[2437.22 --> 2439.18]  And I mean, it's really fun.
[2439.42 --> 2439.60]  Right?
[2439.66 --> 2443.28]  But when you think about like then creating a dialogue system that works across all these
[2443.28 --> 2444.62]  languages, it's daunting.
[2444.86 --> 2445.00]  Right?
[2445.30 --> 2448.84]  I mean, you can't just go and translate because a lot of stuff is lost in translation.
[2448.84 --> 2453.88]  And, you know, like just the multi-sense words in one language could translate into something
[2453.88 --> 2455.34]  catastrophically different.
[2455.94 --> 2456.78]  Rhetorical questions.
[2457.58 --> 2457.78]  Yeah.
[2457.84 --> 2458.96]  That's the tip of the iceberg.
[2459.18 --> 2459.24]  Right?
[2459.32 --> 2465.34]  I mean, even mundane things like the word bill might mean something, you know, like an account
[2465.34 --> 2468.60]  or a bill could be the same word in one language, but they're not in others.
[2468.60 --> 2468.82]  Right?
[2468.86 --> 2470.44]  And that's just very confusing.
[2470.60 --> 2472.86]  Like they trigger different actions that both exist.
[2472.86 --> 2479.64]  Now, what we started doing then was training word vector spaces, which would embed complete
[2479.64 --> 2484.58]  vocabularies of different languages into the same high dimensional mathematical representation.
[2484.84 --> 2484.96]  Right?
[2485.36 --> 2494.12]  So words like, I don't know, shion, hund, dog, suka, hound, whatever, hund, they were all like
[2494.12 --> 2496.64]  in this bubble in one place.
[2496.82 --> 2496.90]  Right?
[2496.96 --> 2499.86]  Now, of course, there are problems with this because they're multi-sense words.
[2499.86 --> 2503.64]  But, you know, the multi-sense ones tend to float away in a bit of a different direction.
[2504.26 --> 2508.80]  And then you have machine learning models trained to operate over those mathematical objects
[2508.80 --> 2516.28]  instead of operating over a unitary representation of the word dog in Serbian or in English.
[2516.52 --> 2516.64]  Right?
[2516.98 --> 2523.72]  And if you do that, then the beauty of task-oriented dialogue when it's a specific task is that you
[2523.72 --> 2526.62]  don't need to understand the nuances or the rhetorical questions.
[2526.62 --> 2531.46]  You need to understand that someone asked for a table near the disabled toilet.
[2531.78 --> 2531.92]  Right?
[2532.30 --> 2536.68]  And at that point, the fact that you're just parsing a limited number of intents means that
[2536.68 --> 2539.38]  you're actually able to do it across different languages at once.
[2539.86 --> 2543.48]  And that's like a big thing that we really, really care about.
[2543.56 --> 2549.58]  It's again, a place where pre-training comes to our rescue and where we're then able to do
[2549.58 --> 2551.84]  these things very, very well.
[2551.84 --> 2558.06]  The other thing, again, a big thank you to all the cloud providers for the millions they've
[2558.06 --> 2562.80]  poured into speech recognition research across different languages, because that's not a
[2562.80 --> 2564.36]  thing that we have the budget to do.
[2564.84 --> 2566.10]  And they do it pretty well.
[2566.74 --> 2571.16]  And, you know, that's a piece we don't touch, but it's provided by those companies and everything
[2571.16 --> 2572.08]  else we do at house.
[2572.08 --> 2572.56]  Yeah.
[2572.70 --> 2579.66]  And so then, like, if you have this multidimensional space, which embeds vocabulary from multiple
[2579.66 --> 2586.00]  languages, is the hope then that like when you add, so let's say that you support X number
[2586.00 --> 2590.78]  of languages, but then your next client wants to have a dialogue in a next language.
[2591.30 --> 2594.84]  Maybe that language is related to one of those you already support, but it's different.
[2594.84 --> 2601.78]  Is the hope then to sort of retrain that and add it in or transfer learn from that existing
[2601.78 --> 2606.00]  model, which is faster than training from scratch in a whole new language?
[2606.00 --> 2607.96]  Or how do you approach that situation?
[2608.24 --> 2609.22]  It's a really good question.
[2609.52 --> 2610.86]  You could do either.
[2611.38 --> 2616.16]  The transfer one seems cheaper and easier, but really in our architecture, the best thing
[2616.16 --> 2620.86]  to have is a unified approach that works across all the languages we want to support at once.
[2621.10 --> 2624.44]  So they're really retraining everything makes the most sense.
[2624.44 --> 2628.38]  Now, bear in mind, we have a single model that is kind of like the nuclear reactor of
[2628.38 --> 2628.86]  our system.
[2629.46 --> 2631.20]  So that model needs to be retrained.
[2631.48 --> 2632.72]  And once it's retrained, we're done.
[2632.92 --> 2634.96]  Like that language is in there forever, right?
[2635.48 --> 2641.72]  So on that front, yeah, it's a lot more heavy lifting than like fine tuning a hundred small
[2641.72 --> 2646.56]  models, but it provides this unified thing that will in the long run save us.
[2646.68 --> 2650.82]  This is similar to kind of like what PageRank did to search, right?
[2650.82 --> 2655.00]  They kind of created an algorithm that just indexes an incredibly large matrix, right?
[2655.04 --> 2655.86]  And factorizes it.
[2655.98 --> 2658.18]  But once it does that, well, here you go.
[2658.28 --> 2658.96]  Search forever.
[2659.26 --> 2661.26]  And internet changes, I refactorize the matrix.
[2662.12 --> 2663.22]  And then, you know, I'm done.
[2663.64 --> 2667.96]  Whereas, you know, previously we had like, you know, in older search engines, you'd have
[2667.96 --> 2671.82]  to go to a specific kind of like industry and then you'd search there and there would be
[2671.82 --> 2675.34]  a small kind of keyword based model that would flag the right results.
[2675.62 --> 2678.94]  And I had like specialist statements on what's more relevant.
[2679.26 --> 2681.68]  Whereas now you have a unified approach and it works a lot better.
[2681.80 --> 2683.54]  And we're trying to do the same for language.
[2683.54 --> 2688.54]  So back at the beginning of our conversation, you said something and I've been holding it
[2688.54 --> 2693.22]  onto because I knew it wasn't yet the point where I could ask, you know, you said as we're
[2693.22 --> 2697.68]  getting into the topic and you're introducing it that you expected to spend the rest of your
[2697.68 --> 2699.10]  life working in this area.
[2699.48 --> 2706.42]  That made me as a non-expert in your area really wonder, I think a lot of people that aren't
[2706.42 --> 2711.66]  working in the field would assume that we're going to take a few years and kind of solve
[2711.66 --> 2714.10]  all this NLP and related stuff.
[2714.38 --> 2717.86]  Jan LeCun famously said that he's going to solve NLP in two years.
[2718.30 --> 2719.82]  How many years ago was that?
[2720.14 --> 2721.64]  I think like six, seven at this point.
[2721.82 --> 2723.06]  He's made great progress.
[2723.54 --> 2724.48]  Yeah, yeah, no doubt.
[2724.94 --> 2726.34]  Now, I heard a similar thing.
[2726.40 --> 2728.40]  I think it was Eric Schmidt in a tweet.
[2728.50 --> 2730.22]  He was like, speech is a solved problem.
[2730.22 --> 2736.54]  I think Eric Schmidt showed a lot more wisdom than Jan LeCun did there, despite probably less
[2736.54 --> 2738.92]  intimate technology understanding.
[2739.56 --> 2741.24]  Okay, but I got to ask this now.
[2741.24 --> 2745.32]  I'm curious because you said that and I know that it's not a static thing.
[2745.38 --> 2745.84]  It's done.
[2745.96 --> 2747.84]  I know that you're going to continue to make great progress.
[2747.96 --> 2750.18]  You've been doing that and you've been telling us about it through this.
[2750.36 --> 2756.96]  So I'm fascinated about where is this going and how does the larger vision for the problem
[2756.96 --> 2763.42]  evolve over time to where you as a young man, a millennial, says this Gen Xer who's significantly
[2763.42 --> 2763.92]  older.
[2763.92 --> 2770.30]  How is this evolving over your lifetime to where you are remaining impassioned about solving
[2770.30 --> 2771.90]  this problem in the long term?
[2772.42 --> 2773.20]  What does that look like?
[2773.24 --> 2774.56]  I'm really curious about that.
[2774.64 --> 2776.50]  I've been waiting the whole way through to ask you that.
[2776.78 --> 2777.86]  Wow, that is a tough question.
[2778.08 --> 2781.74]  I think that there are just a lot of tactical things to solve.
[2781.74 --> 2783.86]  So let's say customer service.
[2783.86 --> 2786.60]  It's a challenge that Poly as a company is focused on.
[2786.94 --> 2790.82]  And I think we'll be working on it for a long time because we're really far from having a
[2790.82 --> 2796.00]  voice assistant that you speak with without getting that danger of frustration at the
[2796.00 --> 2798.34]  start when you realize that, oh God, it's automated.
[2798.34 --> 2798.74]  Right.
[2799.06 --> 2801.20]  We want to make that like a non-problem.
[2801.46 --> 2801.56]  Right.
[2801.58 --> 2803.62]  We want people to call in, automate it fine.
[2803.74 --> 2808.16]  The same way that, you know, like you log into a website and you've never seen the format
[2808.16 --> 2809.40]  before, but you figure it out.
[2809.48 --> 2809.64]  Right.
[2810.04 --> 2813.92]  You know, I think there's a lot of work to be put into those things becoming really, really
[2813.92 --> 2814.12]  good.
[2814.20 --> 2815.14]  It's not a small challenge.
[2815.14 --> 2815.38]  Right.
[2815.38 --> 2820.98]  It's going to be an adoption curve that is also partially just about shifting consumer
[2820.98 --> 2821.46]  behavior.
[2821.84 --> 2822.04]  Right.
[2822.52 --> 2825.68]  And voice assistants have done a lot to help there.
[2825.68 --> 2829.32]  They've shifted this into the realm of possible, likely.
[2830.04 --> 2834.22]  And, you know, the new generations, you know, kind of like people younger than any of us
[2834.22 --> 2835.80]  are growing up with these things.
[2835.94 --> 2840.40]  And that I think is really powerful because, you know, we might be the last generation,
[2840.40 --> 2845.86]  which was really, really fluent in, you know, kind of like laptops opening up a terminal,
[2846.46 --> 2848.78]  you know, the heavy intricacies of the web.
[2848.92 --> 2852.80]  Like, why would you do that if it's a lot more accessible with a more natural interface?
[2852.94 --> 2853.10]  Right.
[2853.10 --> 2858.22]  And, you know, I think that people who are heavily reliant on the web might seem in 20
[2858.22 --> 2863.62]  years time to those, well, to younger people like, you know, those guys that are still using
[2863.62 --> 2865.86]  the terminal or, you know, speaking about assembly.
[2866.26 --> 2866.70]  Right.
[2867.12 --> 2871.16]  I know that's the best and the most fortunate analogy, but to kind of like get into the meat
[2871.16 --> 2877.00]  of your question, like, let's say that in 10, 20 years, 10 years, we've got voice assistants
[2877.00 --> 2877.72]  that are everywhere.
[2877.72 --> 2878.04]  Right.
[2878.08 --> 2878.64]  They're endemic.
[2878.64 --> 2880.74]  They're just how you interact with businesses.
[2881.46 --> 2885.92]  You know, they've enabled us as humanity to move away from doing all of those mundane
[2885.92 --> 2886.48]  tasks.
[2887.18 --> 2887.78]  What's next?
[2888.14 --> 2891.44]  Well, I think like just a general interface with technology.
[2891.82 --> 2896.24]  The deeper answer to your question doesn't come without understanding what happens in
[2896.24 --> 2897.04]  AR and VR.
[2897.76 --> 2902.16]  What happens, you know, with things like Neuralink eventually, where like, that's an absolute
[2902.16 --> 2902.86]  necessity.
[2902.86 --> 2903.66]  Right.
[2903.76 --> 2908.28]  Like, I really want that because that's really how we then kind of like transcend humanity.
[2909.10 --> 2912.20]  This technology then becomes a big interface of that.
[2912.36 --> 2912.50]  Right.
[2912.54 --> 2916.12]  Of just like communicating it, of understanding or absorbing all that information.
[2916.64 --> 2922.28]  And then, you know, you could go and fall for, you know, like singularity, consciousness
[2922.28 --> 2922.82]  in AI.
[2923.18 --> 2924.46]  How are you going to communicate with all that?
[2924.60 --> 2925.70]  I don't know where that's going to go.
[2926.04 --> 2930.62]  I'm not super bullish on that, but I know that this problem is going to get deeper and
[2930.62 --> 2930.84]  deeper.
[2930.84 --> 2932.56]  It's a bit like the Dartmouth conference, right?
[2932.98 --> 2936.36]  Where, you know, people sat down for, I think, a summer and they're like, we're going to
[2936.36 --> 2938.08]  crack this, you know, AI thing.
[2938.26 --> 2939.20]  It's like, yeah, right.
[2939.30 --> 2940.66]  You didn't even scratch the surface, right?
[2941.40 --> 2947.24]  So when we get to the point where we have technology, where voice is completely natural,
[2947.66 --> 2951.58]  I think it's really hard to imagine what the world will look like at that point.
[2951.64 --> 2952.18]  It's going to be great.
[2952.28 --> 2953.74]  It's going to be really, really interesting, right?
[2954.16 --> 2954.92]  We're not that close.
[2955.00 --> 2955.74]  There's a lot of work.
[2955.98 --> 2958.16]  I'll be past your age by the time that happens.
[2958.56 --> 2959.86]  You got a ways to go then.
[2960.84 --> 2962.04]  We'll see.
[2962.26 --> 2966.96]  I'm definitely glad to hear that perspective and also just get to hear from your great
[2966.96 --> 2967.82]  work with PolyAI.
[2968.12 --> 2968.36]  Yeah.
[2968.46 --> 2969.26]  It's been a pleasure.
[2969.56 --> 2975.48]  And I know I'll probably annoy you with all sorts of speech related questions as time
[2975.48 --> 2976.06]  goes on.
[2976.14 --> 2978.94]  I'll look forward to seeing what PolyAI does.
[2979.30 --> 2981.50]  But yeah, thank you so much for joining us.
[2981.54 --> 2982.16]  It's been a pleasure.
[2982.16 --> 2983.46]  And thank you for having me.
[2983.54 --> 2984.20]  I've had a lot of fun.
[2984.20 --> 2990.08]  Thank you for listening to Practical AI.
[2990.42 --> 2992.44]  We appreciate your time and your attention.
[2992.44 --> 2997.12]  Follow the show on Apple Podcasts, Spotify, or your favorite podcast app.
[2997.44 --> 2998.98]  Your neural networks will thank you.
[2999.50 --> 3002.68]  We are also on the web at practicalai.fm.
[3002.94 --> 3007.88]  There you'll find recommended episodes, listener favorites, and a free sign up to join the community.
[3007.88 --> 3011.92]  Practical AI is hosted by Chris Benson and Daniel Whitenack.
[3012.10 --> 3015.68]  It's produced by Jared Santo with music by Breakmaster Cylinder.
[3016.08 --> 3019.26]  Thanks again to our sponsors, Fastly, Linode, and LaunchDarkly.
[3019.42 --> 3020.22]  That's our show.
[3020.64 --> 3021.62]  We hope you enjoyed it.
[3021.68 --> 3023.36]  And we'll talk to you again next week.
[3023.36 --> 3053.34]  We'll see you again next week.
