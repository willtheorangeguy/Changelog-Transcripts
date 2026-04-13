[0.00 → 10.06] Welcome to Practical AI, the podcast that makes artificial intelligence practical, productive,
[10.40 → 11.46] and accessible to all.
[11.46 → 14.48] If you like this show, you will love The Change Log.
[14.70 → 19.52] It's news on Mondays, deep technical interviews on Wednesdays, and on Fridays, an awesome
[19.52 → 21.38] talk show for your weekend enjoyment.
[21.84 → 25.82] Find us by searching for The Change Log wherever you get your podcasts.
[26.32 → 28.36] Thanks to our partners at Fly.io.
[28.36 → 31.10] Launch your AI apps in five minutes or less.
[31.40 → 33.38] Learn how at Fly.io.
[44.00 → 47.76] Welcome to another episode of the Practical AI podcast.
[48.18 → 49.92] This is Daniel Whiten ack.
[50.02 → 55.58] I'm CEO at Prediction Guard, and I'm joined as always by my co-host, Chris Benson, who
[55.58 → 58.84] is a Principal AI Research Engineer at Lockheed Martin.
[59.42 → 60.12] How are you doing, Chris?
[60.50 → 62.12] Oh, I'm feeling pretty chipper today.
[62.36 → 65.02] It's a good day to talk about AI.
[65.60 → 66.24] Yeah, yeah.
[66.32 → 73.50] I feel quite chipper as well, especially as we've got our guest today, Scott Meyer, with
[73.50 → 81.82] us, whose founder and CEO at Chip, which you can find at chip.ai, I believe is the link.
[82.10 → 83.36] But yeah, Chip is awesome.
[83.58 → 84.94] Also, Scott is awesome.
[85.32 → 93.42] And also, Scott is along a good friend because he's a fellow member of the Silicon Prairie,
[93.68 → 99.36] not living on the coast, but out here in the middle somewhere where AI is really blossoming,
[99.50 → 100.28] if you didn't know.
[100.28 → 100.74] It is.
[101.78 → 106.54] And it gives an unfair advantage for those of us in non-metro areas, you know, like the
[106.54 → 110.72] ability to leverage AI to have the power of 10 people in a place that doesn't have
[110.72 → 111.76] enough people to do the job.
[111.82 → 112.28] It's perfect.
[112.46 → 114.08] It's a perfect solution.
[114.22 → 116.92] So it's great to be here live from Fargo, just like the movie.
[117.62 → 121.36] It's fantastic to see you all and be heard by all of you listening.
[121.98 → 122.58] Yeah, yeah.
[122.68 → 128.32] Scott, we'll get into all the cool stuff, you know, you're doing with Chip and some of
[128.32 → 129.66] the things you've learned through that.
[129.84 → 135.64] But I'm wondering if, you know, you work in the space of, I guess we might put it like
[135.64 → 139.50] low code, no code, AI assistant builders.
[139.50 → 146.82] So for maybe audience members that aren't as familiar with that space, or maybe they're
[146.82 → 152.78] just kind of wondering what's out there, you know, as of today, could you paint a little
[152.78 → 157.88] bit of a picture for us for kind of what sorts of tools are out there?
[157.96 → 163.02] And then maybe that would kind of motivate some of the unique things that you thought
[163.02 → 167.70] should be out there but weren't, which would maybe kind of highlight some of the things you're
[167.70 → 168.26] doing with Chip.
[168.26 → 169.26] Yeah, no, it's great to be here.
[169.34 → 174.82] I think the staff that blows my mind is that almost 50% of Americans use AI every week,
[174.92 → 180.64] but 7% of businesses use AI, which is obviously a lie because 50% of Americans are using AI
[180.64 → 182.14] every week, and they work at those companies.
[182.64 → 187.66] So what's happening is the businesses aren't, they have no idea what's going on.
[187.72 → 190.94] It's like the early days of cell phones when everyone would come to work with their own
[190.94 → 193.56] cell phone, their own laptop, do whatever they wanted to.
[194.06 → 197.56] And eventually we got to this point where you get a company email, you get company apps,
[197.56 → 199.26] you get like the standard way to do it.
[199.56 → 203.88] I think the risk right now is that, and the opportunity, is those who are willing to have
[203.88 → 206.22] agency and try stuff have unfair advantage, right?
[206.24 → 211.32] So I can go do my work with AI and if my colleagues don't know, and I don't have a culture
[211.32 → 214.14] of sharing, like all of a sudden I'm a super, super human.
[214.44 → 218.22] The number one thing I tell businesses when I meet with them is you should have lunch and
[218.22 → 221.04] learn once a month and just have people say what they're doing.
[221.04 → 226.84] Because just that horizontal sharing of AI practices and ideas is all you need to build
[226.84 → 228.08] a culture of acceptance.
[228.44 → 231.16] And what makes AI so unique is it's not top down.
[231.26 → 235.68] It's not the CIO or CTO saying, I bought this thing, you guys all go use it.
[235.82 → 239.70] It's each individual figuring out how they can use it for their specific tasks.
[240.00 → 245.28] And what I've seen is admin assistants, marketers, interns, right?
[245.28 → 248.24] They're all going to use it differently and often even know better how to use it because
[248.24 → 252.22] they're the ones doing the tasks and that kind of motivated what we built with CHIP,
[252.32 → 255.54] which is how do we just make AI as easy as possible to use?
[255.78 → 258.26] Our, you know, kind of our motto is AI for all.
[258.46 → 262.70] And I think I've spent most of my professional career working on bridging a digital divide
[262.70 → 267.02] because maybe like you, you know, people that work and live alongside me in Fargo aren't
[267.02 → 269.60] always taking advantage of the latest technology, right?
[269.60 → 275.30] And so I kind of feel like it's both a passion and mission to bring what's happening and make
[275.30 → 276.96] it is accessible to those around me.
[276.96 → 281.40] In 2009, I started my first company, and I was trying to tell businesses there's this
[281.40 → 283.24] thing called social media they should use, right?
[283.30 → 285.40] Before there were Facebook pages and Facebook ads.
[285.52 → 289.96] And it feels like that to me again, almost 20 years later, where it's like this amazing
[289.96 → 290.94] power is right here.
[291.16 → 292.78] And the best time to start learning is now.
[293.26 → 298.66] And with tools like CHIP and others that we can talk about, it's actually better now than
[298.66 → 302.36] ever for people who aren't technical because it's not about technical ability.
[302.36 → 304.62] It's about knowledge and agency.
[304.62 → 305.82] And I think we all have that.
[305.96 → 307.50] So happy to give a landscape.
[307.70 → 311.02] I think that already went off track from your question, but hopefully that gives you the
[311.02 → 311.68] starting point.
[311.96 → 312.62] No, that's awesome.
[312.76 → 319.94] What would you say are kind of some of those things that might make AI hard to use?
[320.06 → 323.74] And here, you know, mostly we're talking, of course, we've talked about a lot of things
[323.74 → 328.36] in the show, but mostly we're talking about kind of what typical people would consider
[328.36 → 334.04] AI now, which would be kind of generative AI language models, maybe vision models, ET
[334.04 → 334.28] Peter.
[334.48 → 342.42] So like what can make those difficult to use, or how might people get disillusioned as they're
[342.42 → 343.64] exploring the technology?
[343.64 → 350.40] I'll say almost every excuse people have not to use AI tools is fear.
[350.40 → 352.46] They are scared of a blank page.
[352.54 → 355.26] And this is the same with technology for 20 years.
[355.38 → 356.76] I taught entrepreneurship.
[356.96 → 360.72] I started entrepreneurship centres and all these students with amazing ideas.
[361.28 → 361.82] And you know what?
[362.06 → 365.56] 90% of them didn't do anything because they had to actually go do something.
[365.68 → 365.86] Right.
[365.90 → 368.82] And it's like, you just have to start.
[368.94 → 373.70] And I'm convinced the biggest challenge in AI is change management.
[374.00 → 376.60] It's just getting people to start.
[376.60 → 381.02] And I think this happened when Google first came out, you know, it's a blank screen, blank
[381.02 → 381.92] prompt window.
[382.08 → 384.34] Like, what do I say when I can say anything?
[384.34 → 385.54] It's actually quite intimidating.
[385.88 → 388.84] And so that's the challenge I think with AI is like anything's possible.
[388.90 → 389.52] So where do you start?
[390.12 → 394.12] I tell everybody the best place to start is to create your digital protégé.
[394.52 → 398.14] Like just tell AI what you do and have it help you do those things.
[398.46 → 400.68] AI is great at what you hate.
[401.04 → 404.46] And so find those things that you hate doing or that take a lot of time and start there.
[404.46 → 405.80] You've maybe seen that quote.
[405.88 → 406.50] I really love that.
[406.60 → 413.14] You know, I want AI to do my dishes and laundry so I can do more art and music, not AI to do
[413.14 → 414.96] art and music so I can do more dishes and laundry.
[415.22 → 415.34] Right.
[415.36 → 418.80] So I think we all have dishes and laundry in our day-to-day life.
[418.96 → 424.12] And so let's use AI there first because that'll be the you'll get more motivated to do fewer
[424.12 → 429.40] financial analyses or fewer, I don't know, copy editing because that's kind of annoying
[429.40 → 432.62] than you would like making music because maybe that's fun for you.
[432.62 → 434.22] So start with things that you don't like.
[434.58 → 441.08] One thing I find fascinating about research on AI is actually having knowledge makes you
[441.08 → 443.04] better positioned to use AI.
[443.18 → 446.32] I think about AI as like the rebirth of the Renaissance person.
[446.50 → 451.60] It's like if I want to create a picture on AI that looks like Picasso, but I don't know
[451.60 → 454.80] Picasso's name, it's really hard to describe that, right?
[454.96 → 460.04] If I want to make a blueprint of a Georgian architecture building, like how do I explain that if I don't
[460.04 → 465.36] know what Georgian architecture is? And so whatever area you live in or work in or care about,
[466.00 → 470.94] you have like expertise, right? You can talk about it all day. And that's a great place to
[470.94 → 475.92] start with AI because you can go say those words like, give me, I don't know, a hierarchy of Pokémon
[475.92 → 480.14] characters, and you can name all the things and have it rank order it. Like I have no idea what I would
[480.14 → 485.52] say for that, right? But I can talk all day about saunas and have the AI help me improve my sauna,
[485.52 → 490.52] find new water buckets, look at, you know, different ratios of time in the sauna, like,
[490.58 → 494.46] because I care about that. So find some things that you know about that you're passionate about and
[494.46 → 496.94] start asking AI about it so you can go deeper. I love it.
[497.20 → 501.80] I'm curious, a quick follow-up on that, you know, cause you raised a point that I hadn't really
[501.80 → 506.70] thought about, but I've observed it many, many times and, and you've kind of, you brought it to
[506.70 → 513.42] the surface here with, I see people who are totally comfortable getting on the search engine of their
[513.42 → 518.96] choice and searching topics, and they've been doing that for years. But as soon as they pull up,
[518.96 → 523.68] you know, uh, you know, a chat with a given model, they're really struggling with that.
[523.68 → 528.40] And they're really, that that's a what, you know, like from a, I'm just curious as you've,
[528.46 → 532.84] if you've clearly thought about this quite a lot, what is the difference, and why are people
[532.84 → 539.40] so easy to go to search and yet struggling with, with that model, you know, that has the same text
[539.40 → 540.20] box in front of it?
[540.20 → 544.02] Part of its exposure, right? Just history. But I also think there's something quite vulnerable
[544.02 → 549.70] about AI where it's really a two-way conversation. Search engine is, you know, very much like,
[550.08 → 554.74] like the old card catalogues. You know, I remember my first year of elementary school, I learned card
[554.74 → 558.88] catalogue. And then the next year was told never have to touch that again, but it's the same,
[559.00 → 563.50] that worked the same, right? I'm just going to go find something. But with AI, it's probing back and
[563.50 → 567.46] forth, and actually you can get, you can get pushback and it kind of identifies how you're thinking
[567.46 → 572.32] about things. So I think there's some vulnerability around that. And plenty of like blank page problem
[572.32 → 577.02] of just not knowing where to start. So start by creating a protégé, start by diving into areas you
[577.02 → 581.88] care about. And I always tell people a great framework to get started is what I call the
[581.88 → 587.32] ripe framework. So R-I-P-E. And it's just a way of like four sentences to put into AI to get good
[587.32 → 593.74] answers, which is the role. So like you are an expert, I don't know, copy editor, the instruction,
[593.74 → 599.68] like read through my paper and improve it. Parameters. So make sure it's very concise and
[599.68 → 604.94] don't repeat a lot of the same points and examples. Like here's a paper I wrote before that shows my
[604.94 → 609.58] kind of tone. You know, if you just do those four things, a role instruction parameter example, like
[609.58 → 614.02] you're going to get awesome output that's personalized and much more effective and less
[614.02 → 617.02] robotic than just going there and saying, write me a paper.
[617.56 → 623.12] Yeah. I've had this kind of hypothesis, I guess, going around in my mind. I'm curious,
[623.12 → 629.56] Scott, on your take on this, because you've seen a lot of people now, you're always interacting
[629.56 → 634.98] with people on Discord or wherever, you know, trying to get their assistance to do this or that.
[635.54 → 643.72] What have you found to be kind of the qualities that make up someone who is just really proficient
[643.72 → 653.84] at kind of honing in the instructions, the data integration, the configuration of AI systems?
[654.20 → 663.80] My hypothesis is sort of this is almost like a, I think, if we took a bunch of hostage negotiators
[663.80 → 671.20] and had them log in to AI systems to try to, you know, either get them to do things that they wanted
[671.20 → 676.80] them to do or to jailbreak them. I think they would be like amazing at this because a lot of times it
[676.80 → 683.66] seems to me, you know, not that I feel in danger physically or something, but it's like people can get
[683.66 → 690.16] disillusioned with this. It's like not quite what I want. How do I get you to do what I want you to do?
[690.16 → 697.30] How do I like to warm you up to this idea? So yeah, I'm curious on the qualities that you've seen in
[697.30 → 705.00] terms of people that have become good at configuring these systems, prompting, understanding how to,
[705.00 → 709.60] you know, pull in integrations or when and where to do that. Any thoughts?
[709.92 → 715.78] Yeah. I mean, people who are great at this are kindergarten teachers or parents of three-year-olds.
[716.06 → 717.98] Maybe also hostage negotiators.
[717.98 → 720.24] Also, it's basically the same job title.
[720.96 → 722.76] There's some similarity there, maybe.
[723.18 → 726.92] Yeah. I mean, think about talking, I mean, people, I say an intern, but that's even too,
[726.98 → 731.48] too experienced. Think about talking to my three-year-old Sebastian. If I tell him three
[731.48 → 735.68] things to go do in order, there's no way he's going to get all three of them done, right? Like
[735.68 → 741.36] go to the bathroom, pick out some shoes, grab your snack, go to the car. Like that, that's not
[741.36 → 747.04] happening. I have to be like, go to the bathroom. Good. Now this, right? And now this,
[747.04 → 752.18] it's very step-by-step. And I think what's interesting is there are two models or two types
[752.18 → 756.46] of models emerging in AI. And you guys maybe have your own language for this, but you know,
[756.46 → 761.70] I think about linear models like 4.0, Claude Sonnet 3.5, and we have reasoning models now,
[761.70 → 767.72] like O3, Deep Seek, and now Sonnet 3.7. And it's like the reasoning models actually,
[768.36 → 772.08] that's like talking to an intern who you can give a ton of stuff, and you just let it go.
[772.08 → 777.18] But if you're doing a linear model, that's very much need to do that step-by-step. First do this,
[777.24 → 782.44] then do this, then do this. Because the biggest, I think, frustration people have is that AI too
[782.44 → 788.78] quickly tries to get to an answer before it has all the details and things get lost. And so with Chip,
[788.92 → 793.84] you know, you can prompt your AI tool and then anyone can use it. And so what we've found is like
[793.84 → 800.08] flipping the relationship is really powerful where the AI prompts you to get what it needs and then gives
[800.08 → 804.24] an answer. So you can even, you know, on Chip, you can build this in so you don't have to
[804.24 → 808.44] type it every time. But on any AI tool, you might say like, before you write the paper,
[808.44 → 812.82] before you create the, you know, strategy, before you create the I don't know, the press release,
[813.36 → 817.80] make sure to ask me these three things, right? And force it to get all of that information
[817.80 → 822.16] step-by-step, just like you do with a three-year-old, and then you go to school, and then you write the
[822.16 → 825.60] paper, and then you do the thing, right? So I think that's really fascinating though,
[825.62 → 829.12] seeing that divergence with reasoning, which is like, don't go step-by-step,
[829.12 → 833.88] just give all the context, and it's going to work through it on its own versus the three-year-old
[833.88 → 838.34] linear that's like needs that guidance. So, so yeah, I think, and the end of the day,
[838.40 → 840.30] hostage negotiator and parents, you got this.
[840.30 → 862.56] Well, friends, today's ever-changing AI landscape means your data demands more than the narrow
[862.56 → 869.18] applications and single model solutions that most companies offer. Demo's AI and data products
[869.18 → 877.74] platform is a more robust, all-in-one solution for your data. It's not just ambitious, it's practical
[877.74 → 884.64] and adaptable. So your business can meet those new challenges with ease. With Demo, you and your team
[884.64 → 891.02] can channel AI and data into innovative uses that deliver measurable impact. And their all-in-one
[891.02 → 897.00] platform brings you trustworthy AI results without having to overhaul your entire data infrastructure,
[897.00 → 904.18] secure AI agents that connect, prepare, and automate your workflows, helping you and your team to gain
[904.18 → 910.74] insights, receive alerts, and act with ease through guided apps tailored to your role, and the flexibility
[910.74 → 916.66] to choose which AI models you want to use. Demo goes beyond productivity. It's designed to transform
[916.66 → 923.30] your processes, helping you make smarter and faster decisions that drive real growth, all powered by Demo's
[923.30 → 933.52] trust, flexibility, and their years of expertise in data and AI innovation. Data is hard. Demo is easy. Make smarter
[933.52 → 945.42] decisions and unlock your data's full potential with Demo. Learn more today at AI.domo.com. Again, that's AI.domo.com.
[945.42 → 958.14] So Scott, maybe we'll come back to kind of the tooling itself. Could you maybe kind of circle back and
[958.14 → 964.44] describe some of the maybe people aren't familiar with some of the kinds of tools that are out there,
[964.78 → 971.78] especially, you know, maybe there are programmers that have interacted with APIs that are listening to
[971.78 → 976.74] the show? Maybe there are people that have explored one tool or another. Maybe there's people that
[976.74 → 982.62] haven't explored anything yet. So could you maybe just help us kind of form a mental model for the
[982.62 → 990.16] kinds of AI tools that are out there? And then maybe that would lead into a discussion about kind of some
[990.16 → 996.36] of the things that were really on your mind in terms of needs that weren't being addressed in that
[996.36 → 1000.42] ecosystem. Yeah. I mean, if you, if you want to think of like a simple two by two matrix, I think
[1000.42 → 1006.18] there's a really clear, like vertical versus horizontal and like closed versus open dichotomy.
[1006.46 → 1013.60] So you can think about horizontal tools doing a lot of things across modes, right? So ChatGPT can write,
[1013.70 → 1019.08] it can create images, it can code. It's perfect at all of those. But if you want to just make
[1019.08 → 1024.84] images like mid-journey is probably better, right? It's a vertical image generation tool or Pike is really
[1024.84 → 1030.02] good at video generation, which some of the general horizontal tools aren't as good at. And, you know,
[1030.02 → 1035.18] my sense is like horizontal is going to win, but there's always going to be a need for people who
[1035.18 → 1041.76] want the Maserati of AI, right? If you're only doing code, like you're going to probably be in cursor
[1041.76 → 1047.16] going deep into like using these tools. Whereas someone like me, I'm going to do the vibe coding where
[1047.16 → 1053.28] I can use a tool like lovable or bolt and just try stuff or replete, right? So I think horizontal,
[1053.28 → 1057.14] vertical, and then I think, you know, kind of open close. So there are tools that let you,
[1057.36 → 1060.66] you know, use it on their platform, and you don't necessarily know what's happening. So that would
[1060.66 → 1065.92] be obviously like ChatGPT or Claude. You can't change the kind of rules underpinning it. Also,
[1066.04 → 1069.36] you have to go to their website. You can't brand it. You don't really have much control over the
[1069.36 → 1074.38] privacy. And then more open tools are ones that you could put on your own site. You could add privacy
[1074.38 → 1079.28] into it. You could brand it. So that's what chip is. You know, we want to bring the power of AI tools
[1079.28 → 1085.44] like ChatGPT and Claude to your website, add privacy. So the files stay locally, add your own
[1085.44 → 1090.14] branding. You can see the chat log. So just a lot more control, obviously like prediction guard,
[1090.24 → 1095.22] same thing, right? Where you can bring AI into your own cloud. So a little bit more work,
[1095.28 → 1099.82] obviously with an open tool where you more power, also you get more options. So I think that's kind
[1099.82 → 1104.92] of like the lay of the land. And I think it's just like when you look at the internet broadly,
[1104.92 → 1110.82] like it started with text because that was easy to send across wires and then music because MP3s were
[1110.82 → 1115.40] smaller than video and then video. See the same thing with AI, right? Where it started with text
[1115.40 → 1120.38] and code because that's text heavy, starting to get pretty good images. Now video is still coming,
[1120.48 → 1125.18] not quite there yet, but getting better every day. So I kind of see that evolution happening.
[1125.76 → 1131.20] Yeah. And I think what maybe is a surprise is that people thought the value was in the large
[1131.20 → 1135.56] language models. And I think what's become really clear the last month or two is it's actually going
[1135.56 → 1141.12] to be in the customer relationship and making the stuff easier to use. Deep Seek is the model that
[1141.12 → 1147.76] came out of China a couple of weeks ago. And if I look at what CHIP's cost per API call is, it's gone
[1147.76 → 1154.72] down 90% in 18 months, right? So just think about the value of these large language models becoming
[1154.72 → 1160.58] more commoditized. And then what people are signing up for is like the experience of signing up and
[1160.58 → 1166.42] creating. So I can go to Replit and say, I want an app that, you know, is tracking my to-dos and get
[1166.42 → 1172.12] it in a few minutes. It's all on top of the same power, right? It's all on top of ChatGPT or Claude,
[1172.20 → 1177.82] just like CHIP, you can use any model underneath, but it's that end user experience, which maybe isn't
[1177.82 → 1182.44] so different from the web, right? There are protocols underneath, but you still use the browser that you
[1182.44 → 1187.68] like or the web app you like because of how it works, not necessarily that it uses FTP versus
[1187.68 → 1192.90] something else, right? Could you talk a little bit more about that end user experience, both the
[1192.90 → 1198.76] good and the bad? Because I think, you know, kind of going back to what we were talking about before,
[1199.32 → 1206.00] it's one of those barriers. And, you know, there's a set of people that are totally bought in across a
[1206.00 → 1210.22] bunch of different industries, but there's also a very large segment of the population that
[1210.22 → 1214.78] still really hasn't engaged. You know, they're hearing about it every day in the news and everything,
[1214.78 → 1219.78] but they're just intimidated and haven't done it. So could you talk a little bit about the
[1219.78 → 1222.92] landscape of being on both sides of that barrier for different people?
[1223.24 → 1228.80] I mean, the biggest increase in use that we see with AI is putting it where people already are,
[1228.88 → 1234.80] so they don't have to learn a new interface, right? So if they can engage with AI via a Slack channel
[1234.80 → 1241.32] or via WhatsApp or via text message, like way easier, right? And so I think it's fascinating to see
[1241.32 → 1247.68] there are a lot of amazing UIs out there, but it's still like getting people there. It seems like
[1247.68 → 1252.96] time to value is really important with the tools. So like the faster you can show somebody an outcome,
[1252.96 → 1259.28] and that's, I think, where a lot of the new kind of text to app tools like Lovable and Bolt are
[1259.28 → 1263.80] really exciting for people because they can get something quick, which makes sense. I think that's
[1263.80 → 1268.46] kind of like how all UI is, is like, how do you get someone to the value quickest? I actually think
[1268.46 → 1274.86] like the default UI we are accustomed to with ChatGPT is not great. You know, like for someone
[1274.86 → 1279.50] to come in there and use, you know, it's interesting that ChatGPT was a research project. It was not
[1279.50 → 1285.56] supposed to be a consumer app, and it just became that on accident. And so I think there's a lot of
[1285.56 → 1289.98] improvements to the UI to come to make it easier for people to use. And you see those already coming
[1289.98 → 1296.02] into play where there's pre-built ideas, autofill, you know, connect to data sources. You know,
[1296.02 → 1300.40] the most common way people use Chip is by duplicating an existing app, right? So it's like
[1300.40 → 1305.04] solving that blank page problem is really important, I think, for any AI tool. So the easier you get
[1305.04 → 1312.44] people to motion is key. Yeah. I'm intrigued. You made me think of something. So like for those that
[1312.44 → 1318.00] haven't seen Chip and what Scott and team are building, you can go in and create individual
[1318.00 → 1322.70] assistants that, as Scott mentioned, you can kind of control and configure, make the way you want,
[1322.70 → 1328.18] connect the data sources you want. And often I think in my conversations in the past with Scott,
[1328.26 → 1333.66] I've heard him talk about how people are creating sort of proliferating these, right? You create one
[1333.66 → 1338.40] to do this and like one to do that and one to do this, and you clone this one to do that because it's
[1338.40 → 1346.36] not quite that, which is a different, it's a different paradigm than the sort of like, here's a
[1346.36 → 1351.74] chat interface. This chat interface is going to do everything that we, that we want it to do.
[1351.74 → 1356.86] Could you talk about that, that element of it a little bit and what you've seen there? Because I,
[1357.02 → 1363.86] I also see this on the business side, like when we engage customers, the kind of tendency,
[1363.86 → 1371.22] it seems from my perspective is to say, Hey, how are we going to build like our internal AI,
[1371.60 → 1376.46] right? And get it to do all the things that we want it to do. But it's like a single,
[1376.46 → 1381.74] in their mind, it's a single thing, right? It's like, this is our tool, and it's going to be the
[1381.74 → 1388.48] tool to sort of rule them all. They're thinking very singularly in that way, which definitely does
[1388.48 → 1393.22] not seem to be kind of how people are engaging in the way they're building assistance in your
[1393.22 → 1394.56] tooling. Any thoughts there?
[1395.00 → 1399.92] I mean, I think the high level thought is the concept of software is getting turned on its head
[1399.92 → 1406.90] where software is now an individual sport, not a team sport. You know, you think about if you're
[1406.90 → 1412.86] the CTO, even a few years ago, it's like, I have to do a lot of research by the right thing. Cause
[1412.86 → 1416.80] everyone's going to use this. It has to, has to fit the most use cases. We have to squeeze everything
[1416.80 → 1421.66] we can into one thing. And now it's flipped where every single person can build custom software within,
[1421.80 → 1427.52] you know, we say 60 seconds, right? So you would never build software to, I don't know,
[1427.52 → 1433.10] write a better introduction paragraph to a grant, but now like someone on chip will go build an app
[1433.10 → 1438.02] that just does introductory paragraphs for grant applications because it takes 60 seconds and it
[1438.02 → 1441.84] saves them three minutes every single time. And they do 10 a day. And so it's 30 minutes. And,
[1441.96 → 1447.52] you know, we're seeing the average admin person saving 60 minutes a day on chip going from 90 minutes
[1447.52 → 1453.86] to 30 minutes on admin work because they're building specific apps for their specific tools. So,
[1453.86 → 1458.86] you know, today I was looking at one that was getting IRS status from the IRS website,
[1459.00 → 1463.30] right. And putting it onto a spreadsheet. And it's like, nobody is going to go build a SAS tool that
[1463.30 → 1468.28] just does that. Because the market is, you know, maybe a hundred people or something, but with AI you
[1468.28 → 1475.24] can. And so there's definitely no need to have this like laborious top-down purchase cycle when you can
[1475.24 → 1480.08] say, just try it. Like, does this solve one problem, two problems, five problems, 10 problems? Great.
[1480.08 → 1486.22] Like imagine the power of every single person in your org being a web developer or a coder. Like
[1486.22 → 1491.38] that's what it is now. Right. And so now we don't have to bother our IT people or our developers. They
[1491.38 → 1496.76] can go do like the hard stuff integrating with like with antiquated systems, right? Like getting our
[1496.76 → 1501.66] billing to talk to our web, to talk to this. But for my job, I just have a file and I need to get
[1501.66 → 1505.10] something done. And like, I'm not going to bother our developer, but I'm going to be my own
[1505.10 → 1511.06] developer. And, uh, I don't know, that's a total flip, right? Or now we're not making decisions for
[1511.06 → 1515.92] the org. We're making decisions for Scott and, um, I can just build it myself. So the only limiter
[1515.92 → 1521.34] again is, is agency. Like just go, you have to go do it. Most people still won't, even though the
[1521.34 → 1525.44] tool's right there, but if they can at least try once, it's not as hard as they might think.
[1526.00 → 1530.84] So it's a fascinating point you're making there with it, but it does change that even though you're
[1530.84 → 1536.22] talking about flipping the model over, you know, from kind of catering to the, the business as a
[1536.22 → 1541.52] whole, to being able to cater it to each individual contributor in the business by doing that. I'm
[1541.52 → 1546.82] curious, you know, that, that opens up a lot of possibilities for how you might run the business
[1546.82 → 1553.56] going forward. Do you have any thoughts on like what that does to the business? If assuming lets in a
[1553.62 → 1558.12] in a hypothetical world that you could get your entire workforce to engage in that way,
[1558.12 → 1563.34] what do you think that does for a business and how, how might, if you were the CEO of a business,
[1563.34 → 1568.66] how might you operate in such a way to change that? If you were just, everyone's empowered with
[1568.66 → 1573.42] AI agents that they can make in 60 seconds, what does that do for them? Yeah. And this is, uh,
[1573.42 → 1577.98] what Chip's trying to build. This is really my, or Sinatra, like where we think work is going is
[1577.98 → 1583.68] we need an umbrella of, of, of safety so that our employees can do whatever they want without
[1583.68 → 1588.12] feeling like they're going to break something. Like right now, the fear of messing up is greater
[1588.12 → 1592.40] than the fear of missing out. And so we need to like, get rid of that fear of messing up. So
[1592.40 → 1596.50] I always say, you know, like the FOMO is greater than the FOMO. Like we've got to get rid of the
[1596.50 → 1601.64] FOMO because people aren't taking action because they're scared. And so I think if I'm a company,
[1601.64 → 1606.60] what I'm doing is I have my five to 10 core apps. This is how we work. When you start at Scott Inc,
[1606.98 → 1611.10] you're going to go through the onboarding chatbot. You're going to get the content creator that
[1611.10 → 1615.80] writes everything in our voice. You're going to, you know, get the data analysis. That's going to
[1615.80 → 1620.10] analyze the spreadsheets in the same way. So these are the apps everybody uses. This is company
[1620.10 → 1624.98] standard. This is getting the laptop with prebuilt software. And then underneath that now you can
[1624.98 → 1630.54] duplicate or build your own to how you work, right? So you have this layer of company-wide apps.
[1630.92 → 1635.24] And then I have my Scott apps, and maybe they're only visible to me. And a lot of times I might even
[1635.24 → 1639.74] cross personal and professional potentially, right? Where it's like, here's my workout schedule and my
[1639.74 → 1645.24] agenda builder for work and my, I don't know, grant writer tool. But since it's underneath this
[1645.24 → 1650.14] umbrella, we know that it's going to adhere to privacy. Any personal information will be removed.
[1650.14 → 1654.70] So it doesn't violate any problems. And then the final piece is, yeah, we have the tools, but then
[1654.70 → 1659.98] we need that monthly or biweekly lunch and learn where like, Hey Scott, what did you build this week?
[1660.18 → 1665.18] Oh, cool. Let's just duplicate that one click and now send it to Dan and Dan has similar work or,
[1665.30 → 1668.76] you know, new employee starts. They can look over my shoulder. It already,
[1668.76 → 1672.48] the bots already trained on all the history and knows what to do so they can jump in.
[1673.06 → 1678.00] And, you know, I always, I always say that AI really raises the floor, you know, like every
[1678.00 → 1682.96] new employee could start at average or slightly above average. You still need to raise the ceiling
[1682.96 → 1688.76] yourself, add that special spice, right? Your own ideas, but it's going to make everyone on a whole
[1688.76 → 1694.40] quicker to get to work and higher, I guess, like higher average across the board. And I always tell,
[1694.62 → 1698.42] you know, the framework I always recommend is like the AI sandwich. Like just think about,
[1698.42 → 1704.70] you, the AI interaction starts with you, the human, the bread on top. Then the AI is going to do
[1704.70 → 1708.72] something that's the meat in the middle, but then you still have to be the human on the bottom to
[1708.72 → 1714.66] take that output and to improve it, to share it, to repurpose it. And so I think a lot of new people
[1714.66 → 1719.68] get the bread and the meat, but they forget the bottom piece of bread. And so that'd be like the
[1719.72 → 1724.10] the work I would do as a leader is here's our tools. You can all use it, and you're all going to be
[1724.10 → 1728.16] good. Like you're not going to have spelling mistakes. It won't be wordy. It'll make sense.
[1728.64 → 1733.34] But now how do you get better? And it's going to be like adding your own spice on that last piece
[1733.34 → 1736.62] of bread. So that's what I would do for Scott Inc. So I think home run.
[1737.62 → 1744.68] And part of that too, is like developing the muscle memory. So like for me, for example, the
[1745.10 → 1750.20] you know, we've been going through, through fundraising recently. There's always like
[1750.20 → 1756.98] the same set of questions that come up in, in diligence and in, uh, in, in questions about
[1756.98 → 1764.82] the product and all this. And most of those have been answered like 3 million times now in some form.
[1764.82 → 1771.52] And, you know, now looking back, like, and, you know, we've started to do this actually, but
[1771.52 → 1777.60] really what would be best is if we just had a little chat that had all of that preloaded into it and
[1777.60 → 1782.88] could chat over that. But at the time it's like, Oh, well, I'll just answer this email. That's
[1782.88 → 1789.24] asking these 10 questions. Right. I can bang that out really quick, but that, I guess there's a muscle
[1789.24 → 1795.44] memory thing there. And then there's a there is some barrier to overcome, to configure the system
[1795.44 → 1801.06] for future benefit, right. That you might not see, see there. So I don't know. Yeah. Any,
[1801.64 → 1805.98] any suggestions, even in your own personal life where you've kind of come over?
[1805.98 → 1811.76] I mean, we did, we did the same thing, right? Like we did a raise with chip, and we built a chip chat
[1811.76 → 1816.48] and it was trained on all of our, you know, slides and everything. And people still want to talk to
[1816.48 → 1821.82] you. Like, it doesn't mean that they don't get a human, but it gives them the option. And like,
[1821.88 → 1826.52] you know, the data we're seeing for our users using chip for, for like customer support,
[1826.52 → 1831.48] like a chat bubble sort of use case, 70% of them are not clicking the talk to a human button. Like they
[1831.48 → 1836.28] just want to know what are your opening hours? How much does it cost? Who are you? Like, just give
[1836.28 → 1840.90] me the facts. And as like a busy parent, I get that, right? Like I don't want to make phone calls
[1840.90 → 1845.70] because I know it'll take five to 10 minutes versus a minute if I'm doing it myself. So, so I think
[1845.70 → 1851.40] there's that aspect of like time efficiency, and it is changing habits of like going somewhere else.
[1851.40 → 1857.02] Or like you said, taking core info and putting it into a repository. What we found most helpful is we
[1857.02 → 1862.00] have something called dynamic knowledge sources. So if it's a spreadsheet or a folder on Google Drive
[1862.00 → 1868.26] or one drive, anything that gets added into those places is automatically added into your agent. And
[1868.26 → 1872.94] so I think with businesses, it's important to think about that flow of information and minimizing
[1872.94 → 1879.84] as much like documentation work as you can. So we always put everything into notion or confluence or
[1879.84 → 1887.56] Google sheets or Google Docs, make that your hub that is fed into the AI. So everything that you put
[1887.56 → 1894.22] in that place gets automatically added into your FAQ bot or your, um, you know, marketing assistant bot or
[1894.22 → 1899.48] whatever. So I think that's, that's key is like, you can ask people to do it, but even better is like
[1899.48 → 1904.28] not to require more work or even changing behaviour. Because we know that's the hardest part. So
[1904.28 → 1910.36] maybe it's a BCC email that goes into a spreadsheet that's automated, right. Or, you know, something
[1910.36 → 1914.82] like that. So you can kind of decide, um, the way we do it is we actually look at our chat logs of
[1914.82 → 1920.02] people engaging with chip and find the answers that are going unanswered or don't have a great answer.
[1920.02 → 1924.82] And then we add those things in once a week into our chat so that it improves for the things people
[1924.82 → 1929.06] are asking for rather than trying to solve for hypothetical, um, edge cases. Yeah.
[1929.06 → 1934.90] Well, Scott, we've, we've kind of, uh, we've, we've talked a little bit about chip. I've described it a
[1934.90 → 1940.68] little, a little bit. I'm, I'm wondering maybe for, you know, you've been on this journey of kind of
[1940.68 → 1948.24] trying to build this easy to use AI tool along that journey. Have you found, I'm sure you tried
[1948.24 → 1954.48] various things that did work and didn't work, and certain things have been difficult and certain
[1954.48 → 1961.24] things have been easier as you reflect on that kind of, as a founder of, uh, of an AI company,
[1961.24 → 1967.58] trying to build an AI tool, any things that you'd want to highlight in terms of things that were kind
[1967.58 → 1974.80] of key insights or, or bumps along the road that, that in retrospect, you look at and kind of make
[1974.80 → 1980.86] sense or, or anything like that. Because I think there are a lot in our audience that have, have maybe
[1980.86 → 1987.40] ideas for things out there. Yeah. No, that's amazing. Um, there's so many, I think, um, I'll
[1987.40 → 1992.92] take like a non-obvious one, which are we, we were pretty early on focused on building community. So
[1992.92 → 1998.08] we have over 20 chip chapters around the world, people teaching one another AI, fairly active discord.
[1998.50 → 2005.04] That's been invaluable because those are the people who are bringing back problems and ideas and being
[2005.04 → 2012.06] able to build towards, uh, actual customer questions is, is so important. And a lot of times customers
[2012.06 → 2017.22] don't have time or interest in, you know, giving you feedback, which you need. And so what we've done
[2017.22 → 2022.96] is like every two weeks or so, basically having free workshops to try to educate our users and anybody.
[2023.24 → 2026.92] And that's really built a relationship, I think, where we know these people by name, we know where
[2026.92 → 2030.92] they live, what they do. And, and it makes it a lot easier for them to be like, yo, can you build this
[2030.92 → 2034.16] thing? I need it for a pitch on Friday. And we're like, yeah, for, for you, of course,
[2034.16 → 2038.04] because you're contributing, you know? So it's building that, uh, building relationships and
[2038.04 → 2042.44] it doesn't have to be hundreds, right? This can be dozens of people who love you. And that's how
[2042.44 → 2047.28] you really start is like a strong foundation. So I think that one's non-obvious. Um, I think
[2047.28 → 2052.26] technically something that we found maybe an accident, and we're trying to lean into now is
[2052.26 → 2058.70] riding the wave of other people's innovation. You know, like you can only build so many unique
[2058.70 → 2063.90] pieces, and you need to be on top of other parts of the tech stack. And so, you know, chip is built
[2063.90 → 2070.16] on top of large language models. So as Anthropic and open AI build better models, chip gets better.
[2070.28 → 2074.82] And for a lot of our users, they think chip is doing that because, you know, we are their front
[2074.82 → 2079.12] door to, to AI. And so as the models get better, chip gets better, and their experience gets better.
[2079.24 → 2084.34] We partner with folks like prediction guard who help us provide better privacy and security. Right. And so
[2084.34 → 2089.24] we could go spend six months trying to build that, but now we've lost the whole point of what we're
[2089.24 → 2095.44] doing. Right. And so what is your forte is really important. One thing that has really recently that
[2095.44 → 2100.90] we kind of focused on is, um, Anthropic has a new protocol called, uh, what is it? Model context
[2100.90 → 2107.52] protocol. Um, it's basically an easy way to connect APIs in to AI tools. And so that's another example of
[2107.52 → 2112.32] like, we've been building one-off APIs to all these different tools. And now it's like, wow, there's this
[2112.32 → 2117.56] whole world that's built towards the standard. And if we just tap into that, now we can, again,
[2117.56 → 2122.22] get better, the more the open source community contributes. Um, so I think that's really
[2122.22 → 2127.48] interesting to look out where are the areas that will move quickly that you can ride that wave.
[2127.48 → 2131.52] And then where do you want to be a differentiator, and you can kind of draw your line wherever the
[2131.52 → 2136.46] right places. Um, but probably don't try to draw it on all of them. Like pick the ones you're best at.
[2136.78 → 2140.86] Yeah. I think those are, those are a few. And I think just the power of small teams now, I mean,
[2141.22 → 2147.40] you read that a lot of places, but you know, our CTO Hunter, who is just like a beast with AI coding and
[2147.40 → 2154.64] it's like, I know our output compared to some legacy teams is just vastly greater. And so I
[2154.64 → 2158.40] wouldn't underestimate if you're a solo founder, you got a team, you know, we have a couple of chip
[2158.40 → 2163.40] users. There's a guy named Chuck in Colorado who he's building a million dollar one person agency
[2163.40 → 2168.02] and he's almost there. Right. And it's all built with AI automations, and he's conducting everything.
[2168.74 → 2171.58] There's a lot of potential out there. So I would encourage you when listening, like
[2171.58 → 2176.88] finding a co-founder or a team is really, really hard, but you don't have to wait. Like you can do a lot
[2176.88 → 2182.90] on your own. I'm curious. You, you actually started to, to get in for a second to the next
[2182.90 → 2187.38] question I was going to answer. And that was, you mentioned like privacy and security and,
[2187.38 → 2192.72] and partnering with prediction guard for that. As you're thinking about these, these different
[2192.72 → 2199.14] concerns that weigh in on various industries and, you know, there'll be, you know, legal concerns,
[2199.38 → 2204.42] things like, you know, HIPAA in the medical world. And, and every industry has its own set
[2204.42 → 2209.70] of concerns that are kind of external, but are, are binding the work in those areas.
[2210.12 → 2215.76] And as you are kind of, kind of unleashing people's potential with the work that you're
[2215.76 → 2221.34] doing, this kind of have to find some sort of balance. How are you thinking about the constraints
[2221.34 → 2227.78] versus the unleashing that we talked about and finding a balance so that people are unleashed while
[2227.78 → 2231.88] they're still having to be held to account, you know, by whatever those constraints in their
[2231.88 → 2236.80] industry is. Right. Yeah. I mean, I think regulation is always going to trail the innovation.
[2237.34 → 2243.08] And so I would say as a company, as an individual, like look at yourself first before worrying about
[2243.08 → 2248.78] the regulatory environment. You know, I, I think about privacy pyramid as what we tell our customers,
[2248.78 → 2253.60] like the, the bottom of the pyramid, the first thing you should do is just think about what are
[2253.60 → 2259.02] you are okay sharing and not sharing and just tell people again, like FOMO is greater than FOMO.
[2259.02 → 2263.74] People will not take action if they think they're going to get in trouble, even if it's hypothetical,
[2264.18 → 2268.54] like not real, like, I don't know that fear from elementary school, like sticks with us,
[2268.58 → 2273.70] you know? And, and so the first thing you have to do is remove the fear. And the best way to do that
[2273.70 → 2277.72] is just to say what the rules are. As long as people know the rules, they'll work within them.
[2278.06 → 2281.76] But if they don't know what they are, they're afraid that whatever they do will get them in trouble.
[2281.76 → 2288.02] Right. So, Hey, just don't upload customer, you know, data. Like that's our rule. Great. That's a great
[2288.02 → 2292.44] place to start. Now go do anything else or, you know, no customer data and don't integrate with
[2292.44 → 2297.72] these files. Great. And the second level of the pyramid after, you know, kind of just best
[2297.72 → 2303.84] practices internally, uh, is that going to be like human protection air? I call it, which, you know,
[2303.84 → 2308.62] one thing prediction guard offers as well, which is like encrypting pieces of information that get
[2308.62 → 2313.12] added that shouldn't be right. So if I add an a phone number or, you know, a social security number
[2313.12 → 2316.68] or something like it gets removed for me, because I made a mistake. That's fine. Like we make mistakes,
[2316.74 → 2322.12] but best practices and then cover, cover other people's mistakes up as they make them. And then
[2322.12 → 2326.16] I think the top of the pyramid is where you actually say, you know what, let's put it in our own
[2326.16 → 2331.08] environment. So that way, if we can share whatever we want without having to worry. And, you know,
[2331.08 → 2335.38] that's where you can run an open source, large language model in your own cloud infrastructure,
[2335.38 → 2341.02] whatever you share is in your cloud infrastructure. So, you know, some businesses have to do that. So if you are
[2341.02 → 2345.22] in finance, healthcare, like you're probably going to want to do that anyway, just for regulatory reasons.
[2345.54 → 2348.72] Some people want to do that because they know they're going to be sharing data that might be sensitive.
[2349.34 → 2354.06] But I think for most of us, like to get started, just follow that basic best practice of like,
[2354.60 → 2358.62] think about it before you share it. And if you're working with a team that might make mistakes or
[2358.62 → 2363.82] aren't contractors who aren't following your rules, like add in that second level of like human air protection.
[2364.62 → 2369.66] Scott, as we, as we kind of get near to the end here, I'm wondering if you can maybe
[2369.66 → 2377.94] share just a few standout use cases of maybe things that you've seen people do with chip that have
[2377.94 → 2384.00] either surprised you or stood out in a, in a way like, Oh, I didn't expect people would do this,
[2384.00 → 2391.20] that, you know, or, or things that are like, Oh, I didn't even know, you know, I built the platform,
[2391.44 → 2393.12] but I didn't even know that was possible.
[2393.80 → 2398.42] Every day. That's my favourite part of chip and AI generally is like, we really are building
[2398.42 → 2403.60] the tools, and we don't know how people will use them. And it's so crazy to see what people do with
[2403.60 → 2408.32] it. And I mean, the most common use cases, I would say like, there's kind of five areas that
[2408.32 → 2413.70] people use all the time. It's like operations, marketing sales, I call it company search,
[2413.76 → 2419.36] like finding stuff in your Google Drive, basically. And what's the last one, like data analysis,
[2419.58 → 2423.38] like reviewing financials and things like that. So those are like the most common, but in terms of
[2423.38 → 2428.72] like fun, weird ones, like we had somebody who launched a Canadian tariff checker. And so like,
[2428.76 → 2433.62] as the tariffs on Canada were released, you could actually search any product, and it would source
[2433.62 → 2437.58] like where they were coming from and tell you what the change in price would be. That was like
[2437.58 → 2442.98] totally interesting. Um, one of my favourite use cases, a guy named Tyler Hanson, he's in Sioux Falls,
[2443.10 → 2448.66] South Dakota, and he runs an HVAC company, and he put in all the training manuals for all the
[2448.66 → 2453.50] equipment that they service. So then his technicians are on the, on the ground. And instead
[2453.50 → 2457.46] of having to like to be in the bathroom watching a YouTube video, which I know has happened when my
[2457.46 → 2461.38] HVAC guy comes, right. He's like actually learning how to do the thing that I asked him to do.
[2461.48 → 2466.50] Like they can actually pull up the specific model via their chip chat and get instructions on what to
[2466.50 → 2471.82] do and how to service it and parts. And that one's really fun. There's a contractor out in
[2471.82 → 2476.70] Washington. He uses it to create supply lists. So he just puts in square footage and what people are
[2476.70 → 2481.00] going to build. And then it'll spit out like how much wood he needs, how many nails, like whatever
[2481.00 → 2487.54] else, again, like things I know nothing about a lot of people doing it for like finding HR policies,
[2487.72 → 2493.52] um, finding, let's see, there's a car dealer that's using it to find cars to purchase, like,
[2493.60 → 2499.26] um, to then resell. Right. So like searches through auto trader and, you know, Craigslist and wherever
[2499.26 → 2505.68] else to find vehicles, just so many things. Right. And, uh, every day I'm, I'm encountering new ones
[2505.68 → 2510.22] that are so fascinating. The fun part is we integrate with, you know, APIs and webhooks.
[2510.22 → 2514.42] So really like any tool can get pulled in. And a lot of times chip ends up being a front end
[2514.42 → 2520.46] to an AI tool, uh, that's talking to their software. So chip becomes a way they communicate,
[2520.46 → 2524.82] but then it's pulling their own data. So that's super fun. Personally, I have a Scott bot,
[2524.98 → 2529.32] you know, that's the one I use every single day. And so like, I can write things very quickly and
[2529.32 → 2534.10] remember people that I've talked to. So it can like brings in past conversations. And, um,
[2534.10 → 2539.48] so that helps me quite a bit. So yeah, those are a few random ideas. Uh, I haven't built the
[2539.48 → 2544.86] West Lafayette tour guide yet, but we do have some travel, travel AI tools out there. So I,
[2544.86 → 2549.40] I bet we could do that too. So, uh, very cool. And while you're, while you're building that tour
[2549.40 → 2553.34] guide, I might give you a location or two as well. Okay. There you go. Yeah. That's awesome.
[2553.34 → 2559.78] So really cool use cases there as you like, that's got to get you thinking about like the
[2559.78 → 2565.12] possibilities. So, you know, you, you come at it with your own mindset and the things that you have,
[2565.16 → 2571.28] your, your customers are, are teaching you every day about what the new possibilities and boundaries
[2571.28 → 2577.74] might be. So where does that, where does that take you? Like when you are, are, you know, you're kind
[2577.74 → 2582.78] of done for the work day, your brain's decompressing and, um, but you're still kind of, you know,
[2582.78 → 2586.90] just working on things. What, what are, what's going through your head about like,
[2586.90 → 2591.84] where could things go with this? You know, you, you take what you're driving and, and the
[2591.92 → 2595.12] and the folks you're working with are driving. You're taking what your customers are showing you
[2595.12 → 2599.24] that you never thought about. And that's going to leave you with some pretty cool ideas about what
[2599.24 → 2604.02] the future might hold. But can you share some of those ideas with us? Yeah, I think, I mean, I, I,
[2604.02 → 2609.08] I reflect at the end of the day in a lot of ways, because I have four kids that are 11, nine, seven,
[2609.08 → 2615.68] three. And I just really try to think about like, what does society look like when this is more
[2615.68 → 2620.54] present? And, you know, what does education look like? I spent a lot of my life in education.
[2620.54 → 2626.42] We work with a lot of schools who use it for tutors and advisors. And, you know, what's the
[2626.42 → 2631.24] value of a credential saying, you know, something when the pace of change is like way faster than
[2631.24 → 2638.74] four years. Right. I think ultimately, you know, I, I imagine this technology has to fade away from
[2638.74 → 2644.82] being AI and just being a part of what we use. Um, and it helps us lean into the things that make us
[2644.82 → 2650.16] weird. You know, I think about AI is the world's best cover band, and it needs like the originals
[2650.16 → 2656.08] to cover. And so I think it's really forces us to be more unique as individuals and, and create
[2656.08 → 2661.20] something new rather, you know, we're going to use AI for a lot of the quick answers, and it's going to
[2661.20 → 2665.54] be average. It's going to be the middle of that bell curve and that'll be fine for most work. But
[2665.54 → 2670.54] again, we have to raise the ceiling ourselves. And so I think it makes me feel like I want my kids
[2670.54 → 2676.58] and hopefully myself to like, just get good, perfect at whatever weird, interesting thing
[2676.58 → 2681.90] we care about. Yeah. And I, man, I don't know. I think agency again, like I keep coming back to that,
[2681.90 → 2688.82] but how do you instill a lack, like a fearlessness in people? Because it feels like, first,
[2688.82 → 2694.30] most people aren't aware of the pace of change. And as they become aware of it, it's either I'm scared,
[2694.46 → 2698.48] I'm going to back away, or I'm going to lean into it. And I think we just really need to lean into it.
[2698.48 → 2705.46] And I don't know, I think it's exciting because I'm in Fargo and I couldn't, you know, learn to be
[2705.46 → 2710.78] a nuclear physicist in Fargo. Right. But now I could, like, I can easily go down that path and
[2710.78 → 2716.76] learn what I need to connect with the resources, you know, showcase my work. And this has kind of
[2716.76 → 2722.58] been my dream since my first company in 2009 of like really given, give, giving anyone wherever
[2722.58 → 2727.96] they are a chance to, to build. And AI is just like the next step in that process. And I know a lot of
[2727.96 → 2733.12] people still will find reasons not to, but it's going to be just on that agency piece. Like you
[2733.12 → 2737.50] can. And so I don't know, I think a society where everybody has a chance to build and create is
[2737.50 → 2741.46] incredibly exciting. It's going to be more competitive. You know, everyone around the
[2741.46 → 2747.72] world has equal access to the same models as NASA and, you know, like the defence department,
[2747.84 → 2752.76] like it's kind of wild that you can log into these things for free and have the same power as
[2752.76 → 2757.90] everyone else. So that's an opportunity if you, if you take it, I think I saw there was a recent study,
[2757.92 → 2764.10] um, the world banked it in Nigeria and students who are using ChatGPT as a tutor for six weeks had
[2764.10 → 2770.02] the equivalent of two years of education. And it's just so many of our problems are problems of access.
[2770.02 → 2774.60] And I think a lot of those access problems go away. And then what happens when another,
[2774.60 → 2779.06] you know, 1 billion people come online with education who don't have it now, like that's just
[2779.06 → 2782.30] better for us all. We can come up with really exciting solutions to our problems.
[2782.90 → 2787.68] Well said. Yeah, that's a that's a great way to end. Thanks for, thanks for joining Scott. I
[2787.68 → 2796.14] encourage everyone to go, uh, create your first chip chat on a chip C H I P dot AI, um, and,
[2796.14 → 2801.30] and have some fun, uh, explore those, that weirdness as, as Scott put it. I love that.
[2801.44 → 2803.56] Thanks for joining Scott. It's been great to chat.
[2803.86 → 2804.50] Great to be here guys.
[2809.06 → 2817.86] All right, that is our show for this week. If you haven't checked out our changelog newsletter,
[2817.86 → 2826.42] head to changelog.com slash news. There you'll find 29 reasons. Yes, 29 reasons why you should
[2826.42 → 2832.18] subscribe. I'll tell you reason number 17. You might actually start looking forward to Mondays.
[2832.36 → 2837.30] Sounds like somebody's got a case of the Mondays. 28 more reasons are waiting for you
[2837.30 → 2844.44] at changelog.com slash news. Thanks again to our partners at fly.io to break master cylinder for
[2844.44 → 2849.02] the beats and to you for listening. That is all for now, but we'll talk to you again next time.
