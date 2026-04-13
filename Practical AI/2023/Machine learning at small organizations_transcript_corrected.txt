[0.00 → 4.74] I tend to think of these roles, there's not even a letter that describes this because there's so
[4.74 → 10.78] many, you know, you need to have a relatively shallow but working knowledge of the entire
[10.78 → 17.40] cycle. And so instead of thinking of your role as a data scientist as training models or even
[17.40 → 24.00] producing models, the role of the data scientist is to convert the data into some business value
[24.00 → 26.12] using data science techniques.
[30.00 → 42.94] Welcome to Practical AI, a weekly podcast making artificial intelligence practical, productive,
[43.22 → 48.94] and accessible to everyone. Subscribe now if you haven't already, head to practicalai.fm for all
[48.94 → 55.02] the ways. Special thanks to our partners at Vastly for delivering our shows superfast to wherever you
[55.02 → 62.18] listen, check them out at fastly.com. And to our friends at fly.io, we deploy our app servers close
[62.18 → 66.14] to our users and you can too. Learn more at fly.io.
[72.14 → 79.00] Welcome to another episode of Practical AI. This is Daniel Whiten ack. I'm a data scientist at SIL
[79.00 → 84.62] International. And I'm joined as always by my co-host, Chris Benson, who's a tech strategist at
[84.62 → 88.44] Lockheed Martin. How are you doing, Chris? I'm doing just fine. How are you today, Daniel?
[88.84 → 96.44] I can't complain. It was definitely the first meeting heavy day of the new year for me.
[96.56 → 102.64] Me too. I was really enjoying those like, not everyone knows that I'm back at work. And so I
[102.64 → 109.18] can get stuff done days. So yeah, now everybody knows. But all good things. I'm working on fun stuff.
[109.52 → 113.74] So hey, we're getting to talk AI now for the next few minutes. So we're good.
[113.74 → 121.70] Exactly. Yeah. And I'm really excited to get to have Kirsten Sum with us. She's co-founder and
[121.70 → 125.26] CPO of Storytellers AI. Welcome, Kirsten.
[125.68 → 126.58] Thank you for having me.
[126.88 → 132.88] Yeah, it was great to get to connect with you on Twitter and get you scheduled for the show.
[133.12 → 138.66] One of the things that we were chatting about when I was first talking to you about potential topics
[138.66 → 145.74] for the show was machine learning at small organizations, which I definitely like the idea
[145.74 → 152.18] of like discussing this one because I don't think we've like coherently discussed this on the show
[152.18 → 158.66] in the past and kind of alluded to it at certain points. But also I got my start as a data scientist
[158.66 → 166.84] working at startups at smaller organizations. So I definitely know both like some joys and some pains
[166.84 → 171.86] from trying to like do machine learning or do data science at a smaller organization.
[172.12 → 179.28] What got you started thinking about this topic in particular? And what I understand from storytellers
[179.28 → 183.88] also kind of engaging with a lot of these small organizations in this type of work.
[183.88 → 191.72] So kind of like you, I started in this field in this range of companies from small to large.
[191.88 → 195.98] In particular, one of the things, you know, I'll go a little bit into my background, how I got into
[195.98 → 201.32] data science and why small organizations ended up being my passion. I don't actually have a degree
[201.32 → 207.52] in data science. I have a degree in English is my background. So I came in, I'm sort of a transplant
[207.52 → 213.08] into this field, but I came up through startups. That's how I got into tech was working in startups.
[213.08 → 218.26] And one of the things that you learn at startups, right, is to do kind of the task that's at hand.
[218.32 → 223.20] You just figure out what that task is. You will do it. You make things work. And so I'm so grateful
[223.20 → 228.80] that that's where I started my journey in tech was in startups, because that really is the underpinning
[228.80 → 236.22] of how ML at small organizations works. I ended up going into data science through analytics. I was
[236.22 → 241.86] doing marketing for a long time, got my feet wet and like, oh, wow, if I have data about my marketing
[241.86 → 246.80] campaigns, I can do these things that, you know, if I didn't have the data, I wouldn't be able to be
[246.80 → 253.80] nearly as successful. So I, I, that's where I really found my passion for data. And my first real data
[253.80 → 260.60] science project, I took this marketing process that was a bidding algorithm that was being run out of
[260.60 → 269.02] Excel. And I converted it into a Python script. And that Excel process was taking like 30 hours a week.
[269.02 → 273.50] And with Python, it took eight seconds. It was magical.
[273.86 → 277.26] Talk about return on investment. Yeah, exactly.
[278.88 → 283.22] Exactly. I actually learned Python to do it. It took me two weeks to learn enough Python just to
[283.22 → 290.18] convert this like process into a Python process. And that was like, this is just too fun and too
[290.18 → 296.84] powerful of a tool to not spend all my time doing this stuff. So when I think about that project was
[296.84 → 302.14] actually at a large company, but that large company didn't have a lot of access to data scientists.
[302.14 → 308.78] It was a pretty nascent field at the time. And so my knowing Python being a marketing analyst and
[308.78 → 312.30] just being like, I'm going to roll up my sleeves. I'm going to stand up this process in Python and
[312.30 → 317.58] just do it myself had a huge impact on the business. They actually changed this entire part
[317.58 → 323.50] of the business to be based within those tools because of how much more powerful it was to
[323.50 → 329.80] not have people clicking buttons in Excel for hours a week. So that's where I got really
[329.80 → 335.36] passionate about it. I saw how one person who had these tools could come into an organization
[335.36 → 341.40] and make meaningful change, not just organizationally, but actually for the business itself for growth
[341.40 → 343.66] by using these techniques.
[343.66 → 350.52] And what would you say? So like out of those experiences, because you being a single data
[350.52 → 357.34] scientist in that context, we're able to make a big impact. And so a small organization, I can
[357.34 → 363.32] imagine a lot of small organizations saying things like, well, you know, we're not a big tech company,
[363.32 → 370.14] like we can't support this type of work, or like we're not in a position to do like predictive
[370.14 → 374.90] things, or we're not in a position like we don't have enough data or whatever it is. What are some
[374.90 → 380.38] of those stories that you've heard or cases that you've heard where maybe a company is selling
[380.38 → 385.96] themselves short in terms of the opportunity that's there around data science and machine learning?
[386.56 → 393.70] Yeah, I love that question, because I think it is really selling short, especially now, maybe 10 years
[393.70 → 399.76] ago, I think that those were very valid reasons to not take the step into data science or predictive
[399.76 → 407.40] modelling. Now, the tools are so much better in terms of being able to have, you know, a single
[407.40 → 411.82] person who's making a big impact with these techniques. It's much, much easier, even than
[411.82 → 418.50] when I started to be able to do that. I would say the top reasons that I tend to hear are one,
[419.18 → 425.76] we don't know how to even start in terms of like how to hire someone. That's a big, big barrier,
[426.18 → 429.70] knowing how to evaluate if someone's going to be able to come into your organization,
[429.70 → 435.20] and make an impact is pretty tough. I also hear a lot about not knowing if their data infrastructure
[435.20 → 440.30] is ready or if their data quality is ready. Those are two big questions that are fairly hard to
[440.30 → 445.78] answer. Like, how do you know you're ready? Your data is ready for data science? Do I have enough
[445.78 → 450.34] data? Is it clean enough? Is it stored the right way? Those are all big questions. And then the final
[450.34 → 456.14] one is, I don't know how I would integrate this person into my existing business such that their output
[456.14 → 461.84] gets fed in as an input to all the things that are already running, all of my marketing campaigns,
[462.30 → 466.94] all of my, you know, website analytics, all of that. How do I get this new discipline integrated
[466.94 → 471.82] with all the other technology, especially with small companies having, you know, those people
[471.82 → 475.82] are always stretched very thin. You know, your database administrators stretch very thin,
[475.90 → 480.08] your engineers are stretched very thin. So how can I, you know, do I have the margin to
[480.08 → 481.56] incorporate this new technique?
[481.56 → 486.26] Do you think to that last point that just kind of, you know, FUD, fear, uncertainty, and doubt
[486.26 → 492.76] really kind of play in from a management standpoint? I had a similar experience and I really walked
[492.76 → 498.30] away from that. It was the last small company I worked at, and I just don't think they thought
[498.30 → 503.86] they could do it and they didn't. And I ended up leaving as a result of that. But do you think
[503.86 → 506.98] that's a common situation that small companies run into?
[506.98 → 513.02] I totally do. And to be fair, I think that interestingly, I don't think the data science
[513.02 → 521.20] community is doing a fantastic job at creating literature that is accessible to someone who's
[521.20 → 524.86] in a small business to be able to say, here's how you get started. I think a lot of the literature
[524.86 → 529.06] and data science, we're still really in this experimental phase of like, what new models can
[529.06 → 533.56] we build? How can we push like the state of the art in terms of accuracy and that kind of thing.
[533.56 → 543.06] But the literature really doesn't have an angle for, say, a CEO of a small company that has great
[543.06 → 548.36] analytics, but is actually ready to take the step. There's not that bridge that says, you know,
[548.50 → 553.28] here's how you do it. Here's how you go from an analytics, you know, data driven company to a data
[553.28 → 558.34] science driven company or predictive company. And I think that's right. It's hard to dispel that fear
[558.34 → 563.92] when it feels so mysterious, you know. So that's one of the things I wish that the data science
[563.92 → 569.26] community had more of is non data science facing literature about data science.
[569.58 → 570.22] It's a great point.
[570.60 → 575.20] So I just had this interaction. My wife is an entrepreneur and owns a small business. And
[575.20 → 581.74] we just had the conversation because she just saw Jasper, which is a copywriting,
[581.74 → 589.00] like assistant, like generative language solution that helps you write and that sort of thing.
[589.12 → 594.16] That was the first time like she's, of course, been married to me for quite some time. But it was
[594.16 → 601.16] the first time when she kind of made the connection like, oh, I could have my own people be augmented by
[601.16 → 607.62] this sort of technology in a way that's like, non-threatening or not a lot of work. And she was able
[607.62 → 613.84] to like talk to her team about that. I'm curious, because in that scenario, it's like people that
[613.84 → 622.36] are already inside the company that are kind of now that tooling, sort of like machine learning or NLP
[622.36 → 628.98] tooling is getting more user-friendly and marketed in that way. They're seeing how they can use those
[628.98 → 636.54] tools to advance their business. But then there is a need where like still at her company, like,
[636.54 → 644.72] I help also do kind of some of the forecasting or like other things that really there isn't a great
[644.72 → 649.92] kind of off the shelf tool for, but it also isn't that hard. Like if you know Python, and you're like,
[649.96 → 655.14] you can import like Facebook's profit, you know, then you're like good. And boom, there it is. Okay,
[655.14 → 660.12] I've got it. But it's not the same sort of approachable thing as like a Jasper or something
[660.12 → 665.84] like that. So where do you see kind of moving into the future, like the limits of this, like,
[665.84 → 672.70] kind of low no code, kind of people levelling themselves up versus the things that are going
[672.70 → 678.02] to be really valuable for a data scientist to do in a small organization moving into the future?
[678.34 → 684.12] I love that question, because it reminds me back when I was learning to be an analyst,
[684.44 → 690.16] there was always this idea that eventually BI tools will get good enough, you wouldn't need a BI,
[690.16 → 695.74] right? Like you'd have these like, like Tableau is just a step towards whatever the no code interfaces.
[696.12 → 700.42] And some of these companies would be like, your marketer can just go in an interface and click
[700.42 → 704.18] some buttons, and they'll get a report that really just answers all their questions, no BI needed.
[704.46 → 709.90] And that didn't prove out to be true, right? Like Bis are still like this very important role.
[710.02 → 715.08] But there are these other roles and other tools that can fill some gaps around there. I love
[715.08 → 720.78] the idea of Jasper as this friendly interface to be able to do this particular task of content
[720.78 → 726.68] generation. I think it's a fantastic use case. And also your example of profit, needing someone to
[726.68 → 733.50] come in, use a prebuilt library for doing forecasting in order to get this very simple output that really
[733.50 → 740.72] changes a business's ability to guide itself as that example of that's a hard task to get rid of.
[740.72 → 746.42] And the real core of that, that I see is that data is different from organization to organization.
[746.74 → 751.88] When I was at Amazon, we'd always talk about solve for the constants. That's a constant. Like you go
[751.88 → 756.20] from one business to another, someone's using Stripe, someone's using Square, you know, this person's
[756.20 → 761.26] using Salesforce, this person's using HubSpot. And you have that problem that just multiplies when
[761.26 → 765.16] you look at all of these different technologies that come together to underpin their business.
[765.16 → 771.20] That's where it's like the BI task. You're always going to need someone who's able to reconcile,
[771.50 → 775.48] make sense of the data, and then maybe push it through something that to them is like, oh, this is,
[775.60 → 780.86] this is easy, right? Like training a forecasting model in profit is easy for a data scientist,
[780.86 → 789.18] but it's unreachable for a, you know, a CEO of a company. So that role, I think just like we've seen
[789.18 → 794.34] VI's were always needed. Even when we had all these fantastic low or no code tools for analytics,
[794.34 → 800.84] we still needed VI's that were able to do that heavy lifting of reconciling, of telling the story of
[800.84 → 805.46] creating those interfaces. I think data scientists have that same kind of role. They're always going
[805.46 → 809.98] to need to pull the data together, build that model, explain it to the person, explain how to
[809.98 → 816.06] integrate it. And that role I think is the most fun. If I'm honest, like that's the most fun data
[816.06 → 821.90] science role to me is that particular role. Yeah. I've always really enjoyed that. I've used this
[821.90 → 828.48] analogy with Chris a lot of times that oftentimes I really enjoy this sort of idea that data science
[828.48 → 834.44] is more like cooking than at the like you're at the chalkboard, like doing math problems. So do you
[834.44 → 841.32] have a recipe, but your recipe doesn't quite work the way that the tutorial on medium, like is telling
[841.32 → 848.08] you because you don't have stripe, you have square, but you kind of modify the recipe just enough to
[848.08 → 852.78] make it work for your scenario. And then, you know, you don't have the same ingredients, but you adjust
[852.78 → 858.42] the recipe, and you go from there. I think that's a perfect framework to think about. And I also
[858.42 → 864.22] really enjoy that. It does make me wonder though, for like a data scientist or a machine learning
[864.22 → 870.62] person at a small company, like I could be a machine learning engineer at Google, like on the
[870.62 → 876.34] translate team. And my every day is like translate, right? What I'm thinking about is machine translation.
[876.72 → 883.42] Whereas at a small company, like you said, you're in an environment where you are the data science
[883.42 → 889.64] resource, or there's a few those. How can a data scientist or a machine learning person
[889.64 → 894.48] out at a small company deal with that sort of variability of like one day you're dealing with
[894.48 → 899.52] dash boarding and another day you're dealing with like sales forecasting and that sort of thing.
[899.90 → 905.78] Yeah. It's a fantastic question. I go back to, you know, when we used to talk about T-shaped data
[905.78 → 909.82] scientists, right? Like you're across the top, you need to know a little bit about pretty much
[909.82 → 913.98] everything when everything was a little bit narrower than it is today, but you'd know a little bit
[913.98 → 918.10] across the top, and then you'd have one area. You're, you know, again, translation and the large
[918.10 → 923.50] language, or you're, you're the computer vision. I tend to think of these roles. There's not even a
[923.50 → 928.90] letter that describes this because there's so many, you know, you need to have a relatively shallow,
[928.90 → 935.36] but working knowledge of the entire cycle. And so instead of thinking of your role as a data scientist
[935.36 → 942.78] as training models or even producing models, the role of the data scientist is to convert the data
[942.78 → 949.06] into some business value using data science techniques. And that means having a working
[949.06 → 955.68] understanding of all the elements of the machine learning workflow, like data infrastructure,
[955.90 → 960.86] having a working knowledge of how to stand up a simple database, how to pull data from various
[960.86 → 965.78] sources into that simple database. And then your feature engineering layer, which is really ETL.
[965.90 → 969.46] That's one of the areas I hear a lot of data scientists say like, no, that's not my job, right?
[969.46 → 975.10] Like ETL is actually at a small company, your job, it'll be in a database, but you have to do your
[975.10 → 979.34] own really heavy duty ETL to build your features. Then you've got your training, the thing that
[979.34 → 983.62] everyone kind of gets into data science for, it feels like build training your models. But then
[983.62 → 988.02] afterwards, you also need a simple way of deploying your models and a simple way of monitoring and
[988.02 → 993.26] testing the impact of your models. And so I think about a role at a small company is needed to
[993.26 → 999.34] encompass all of those components, but it doesn't need to be to the level that you would see if you were in a
[999.34 → 1003.20] large company for each of those components. So sometimes people hear that, and they're like,
[1003.26 → 1008.16] wow, that just sounds awful. But the reality is it's because they've seen someone who's specialized
[1008.16 → 1012.32] in Flops, and they're thinking, I have to do that too. And it's like, no, no, no, you don't have to
[1012.32 → 1017.86] do Flops like your Flops peers. You just need to know Flops well enough to where you could deploy
[1017.86 → 1022.48] your own models, have a very simple batch pipeline that you know how to stand up in the technology
[1022.48 → 1027.86] that's available to you at your company. And a very simple, you know, real time, if you can do that,
[1027.86 → 1033.54] a real time, you know, inference pipeline, and those are your recipes, just plug your data into
[1033.54 → 1038.24] those two patterns, and you're good to go. Very rarely do you actually need to come up with a
[1038.24 → 1042.94] whole new way of doing Flops at a small company, you can usually stick to a few simple patterns.
[1042.94 → 1058.52] The changelog is deep discussions in and around the world of software, and it's been going for
[1058.52 → 1062.88] over a decade. We interview hackers like Chris Anderson from 3D Robotics.
[1063.32 → 1067.84] At the time, drones were like predators and global hawks and military industrial,
[1067.84 → 1073.52] they were classified and super, you know, $10 billion things. And we had just built a drone
[1073.52 → 1078.72] with Lego pieces around the dining room table programmed by a nine-year-old. And it's like,
[1078.86 → 1083.96] okay, that should not be possible. You know, it's not, when, when a nine-year-old can do something
[1083.96 → 1089.26] that is classified, that literally export control as ammunition with Lego, with toy pieces,
[1089.78 → 1091.74] it was something important in this world has changed.
[1091.74 → 1094.86] Leaders like Devin Fuel from GitHub.
[1095.42 → 1100.60] In the like 10 to 15-year range or 20-year range, what I would really like is for,
[1100.84 → 1105.46] if you have like three 12-year-olds hanging out and one of them's like, I want to be a firefighter.
[1105.54 → 1109.10] Another one's like, I want to be a lawyer. I want one of them to say that I want to be an open source
[1109.10 → 1109.58] developer.
[1110.20 → 1111.86] And innovators like Amal Hussein.
[1112.40 → 1115.60] I've yet to kind of see applications at scale that don't use multiple languages,
[1115.60 → 1121.68] that don't have just arcane stories behind why this weirdo thing exists, you know?
[1121.74 → 1125.94] Like, all right, when you open this file, you're going to have to turn around three times and tap
[1125.94 → 1127.10] your nose once.
[1129.22 → 1134.40] Like it's just the most hilarious story, you know, but applications are living,
[1134.62 → 1141.72] breathing, they have craft, that's normal. So I want to normalize weirdness because that's just
[1141.72 → 1144.46] how applications evolve over time.
[1144.92 → 1149.94] Welcome to the changelog. Please listen to an episode from our catalogue that interests you
[1149.94 → 1152.56] and subscribe today. We'd love to have you with us.
[1156.22 → 1160.92] I'd like to extend a little bit what we were just talking about and kind of ask,
[1161.20 → 1167.44] we were kind of talking about patterns or recipes if you're in small business, and you addressed a
[1167.44 → 1171.86] little bit about, you know, ML ops and the fact that you don't necessarily need to go to what the
[1171.86 → 1176.94] large company person who specializes entirely. But that does raise the question of there's a lot
[1176.94 → 1183.54] of those tasks to dive into. And so for a person to be successful in the small company environment,
[1183.54 → 1189.94] where they're by necessity forced to be a little bit more generalist and cover a lot more things,
[1189.94 → 1195.12] but maybe not at that depth. What are some of the patterns or other recipes other than ML ops that
[1195.12 → 1201.54] you've identified that like, if you were bringing somebody in new, you would say, focus on that and that
[1201.54 → 1207.00] and your life off the bat will be a lot better than just diving into the deep end without any help.
[1207.10 → 1208.16] What would you tell that person?
[1208.78 → 1214.96] Fantastic question. So one unintuitive thing I would tell folks is build your project or product
[1214.96 → 1222.42] management skills. Having a very strong framework for how you manage a project from end to end is
[1222.42 → 1228.14] pretty much you're going to need that muscle to be quite strong, in particular, because you're going
[1228.14 → 1233.70] to be shepherding sometimes from all the way at the beginning, like data isn't even in a database.
[1233.70 → 1238.66] And you're just talking to the salesperson who has a problem you're trying to solve. And like,
[1238.70 → 1242.70] all right, we're starting from the very beginning from scratch. So having a very strong framework that
[1242.70 → 1250.70] really goes all the way end to end from data, you know, in to data out to your product is critical.
[1250.70 → 1257.00] And a lot of people use crisp DM as sort of their framework for that. I find it's not even quite
[1257.00 → 1263.24] specific enough for as a practitioner to move things from end to end, but that's going to be a
[1263.24 → 1268.64] little variable by company. But I do tend to break it up into these five stages of, you know, having an
[1268.64 → 1275.88] interview format. How do you know that you have gotten the requirements from the person who's going
[1275.88 → 1280.44] to use this such that you have the inputs you need for your model, having a framework for interviews,
[1280.86 → 1286.26] having a simple recipe for standing up a database, or if you need to send up your own database or
[1286.26 → 1292.08] have a very simple architecture for that, that you can plug all of your projects into. So they're sort
[1292.08 → 1297.94] of centralized. The other thing that I really recommend is, well, here's a here's just a side
[1297.94 → 1304.02] note. Almost all problems in this space are tabular. So like it's tabular data. That's what you're
[1304.02 → 1308.50] going to do. And if you've been on Twitter about tabular data, you know, it's gradient boosted trees,
[1308.76 → 1312.86] just use gradient boosted trees. You know, that's your baseline. Don't worry about base lining with
[1312.86 → 1317.28] linear regression or, you know, the simpler models or random forest. Don't worry about that. Just stick
[1317.28 → 1322.10] to a very simple baseline with your gradient boosted trees. You'll probably get a pretty good model out of
[1322.10 → 1327.22] that. And then the last part that I didn't mention in that earlier list that I think is super
[1327.22 → 1333.96] critical is having a very clear base lining process. How do I know when I'm done? And then when
[1333.96 → 1338.42] you're done, put down your pen, you know, don't worry about trying to get to state of the art on
[1338.42 → 1342.80] every problem. Just know what your baseline is. How do I know when I built a model that's actually
[1342.80 → 1346.78] going to improve this business so that I can stop working on this one and work on the next one?
[1346.82 → 1352.22] Because two models will have a much better impact on the business than one perfect model.
[1352.60 → 1359.02] I'm having all sorts of flashbacks to my, my work in various organizations all the time while
[1359.02 → 1366.66] you're talking some, some good and some painful. And I'm thinking about a couple. So like,
[1367.02 → 1373.66] one of my experiences in a like a small startup environment is like getting in this sort of,
[1373.92 → 1379.90] I don't know what to call it. Like you become the replacement for Excel function where like,
[1380.00 → 1385.80] oh, email Daniel can't like, I think he can like to merge two columns together. Right. And then
[1385.80 → 1390.44] like, they send you to like Excel sheets, and you're like, okay, like I can do that in
[1390.44 → 1395.98] like one minute. So you do it, but then you get this increasing number of tasks and, and then you
[1395.98 → 1401.46] just do that all the time. And the second scenario is like, okay, I'm, I'm going to try to build out
[1401.46 → 1407.90] this roadmap and like this project plan, but things like get shaken up all the time in small companies.
[1407.90 → 1414.56] And it's like, okay, I had this plan to like to optimize my pricing model over the next six months using
[1414.56 → 1422.30] like these AB tests or like whatever I was doing. Right. And then the CEO is like, oh, we're, you know,
[1422.38 → 1428.28] like we're not like meeting revenue this month. Like we need to like just change our pricing
[1428.28 → 1435.58] structure entirely. Right. Does that spark anything in your mind in terms of, yeah, like the level at
[1435.58 → 1442.90] which you can do product or project planning within a small company while still managing that sort of
[1442.90 → 1446.94] flexibility and random tasks that, that come up any recommendations there?
[1447.48 → 1452.56] Yeah. It's funny. Because I'll, you sparked a bunch of memories too. I'm doing that. I feel like
[1452.56 → 1457.18] that's a universal experience. Once you know how to use data, people will not let you do anything
[1457.18 → 1463.60] with data. Yeah. Right. I think number one is going back to the idea of solving for a constant.
[1463.78 → 1470.50] That is a constant in small business is that strategy is changing very rapidly. And so building that
[1470.50 → 1478.54] into the way that you approach data science, I think is really important. I find that one thing
[1478.54 → 1485.74] that helps with both of those scenarios is being able to deliver a result that baselines everyone
[1485.74 → 1493.00] about what good data science does for the company. So if a good data scientist is able to build a model
[1493.00 → 1499.08] that increases open rates on emails, 50%, it's much less likely that they'll email you to ask you to merge
[1499.08 → 1505.98] the columns because you're the person who optimizes email open rates, 50%. So that tends to work super
[1505.98 → 1509.48] well, which kind of goes back to the idea of like, you need to have an end-to-end process. You need
[1509.48 → 1515.26] to be able to deliver relatively quickly on a quick timeline and know how to measure your results so
[1515.26 → 1519.58] that when you do start, you know, getting those questions, like, you know what, I'm super busy on
[1519.58 → 1524.86] this pricing model. If you can wait until such and such a time, I'd be happy to. Otherwise, here's a Google
[1524.86 → 1529.62] search, you know, like that kind of not quite as abrupt as that, but here is a tutorial on how to
[1529.62 → 1534.98] merge columns in Excel. And so that I tend to point to in a lot of scenarios as something that solves
[1534.98 → 1543.62] the instability problem in a small business is make sure that you're really focused on results and that
[1543.62 → 1548.88] people know what the results you're driving are. But roadmapping, I think is one of those things I used
[1548.88 → 1554.76] to, as a project manager, hold onto my roadmaps very tightly. But as you learn, even in, you know,
[1554.76 → 1558.56] as working in large companies, we would have those where you're kind of feeling a little whiplash and
[1558.56 → 1564.70] it's like, how do I solve for a changing roadmap? What's, what is, how do I solve for that constant
[1564.70 → 1571.00] and really clear prioritization frameworks tend to really help with that too. Especially if they're
[1571.00 → 1576.58] known way up the chain, like this is the metric I'm trying to optimize for this business. And therefore
[1576.58 → 1582.64] this is what the how it reads into my roadmap and being able to give those cost trade-offs all the way up
[1582.64 → 1585.74] into the management chain tends to be a really effective solution as well.
[1586.08 → 1592.26] I have a follow-up question for you as we talk about process. I love the way that you've kind of worked out
[1592.26 → 1599.14] the end-to-end system, and you have kind of go-to things that you can utilize, and you're kind of simplifying
[1599.14 → 1603.90] and making sure everyone understands what is, is, what the result, how to measure it and stuff like that.
[1603.90 → 1610.48] In so many small businesses, they'll have the data scientist, but they'll also have the software person.
[1610.68 → 1615.62] And then they'll have the infrastructure person or whatever you want to call it, systems or, or whatever.
[1616.16 → 1616.86] DevOps, Doug.
[1617.36 → 1625.90] Yeah, exactly. Or DevOps, Diana, whatever. Just that person is there. And so I like what you're saying about kind of
[1625.90 → 1630.52] going through that system. Where do you bump in either two different ways of looking at it?
[1630.52 → 1635.22] Bump into that person or find a way to integrate and everything is nirvana together.
[1635.48 → 1640.44] How do you navigate that in a small business where their person's like, okay, you're on my toes now?
[1640.70 → 1648.12] Yeah, I love it. I love it because it gets to this skill that I feel like is not talked about a ton
[1648.12 → 1656.28] in data science education, which is how much people are actually the mechanism by which things get done.
[1656.28 → 1663.74] More than any code or any framework, it's people that get things done. And so knowing how to work in an organization
[1663.74 → 1671.62] with folks that have sort of their territory, how do I earn trust with them? How do I think about
[1671.62 → 1677.26] handoffs between the components of this overall system managed by people is, is so important.
[1677.26 → 1686.26] I think one thing that I tend to recommend for data scientists is that earn trust part. How do you break
[1686.26 → 1693.64] down the process of earning trust inside an organization and make that a repeatable thing?
[1694.04 → 1701.30] Overall, just knowing the architecture people-wise of your organization is a task that some care should
[1701.30 → 1705.64] be taken with. Who are the people that are over these various systems? And meeting with them and
[1705.64 → 1712.16] knowing who they are is like baseline. Even then knowing what their goals are, what their blockers
[1712.16 → 1717.40] are, and how your work can actually make their life better is huge. There is a big advantage to
[1717.40 → 1725.22] knowing, hey, software team got this problem where they're meant to optimize this part of the app flow
[1725.22 → 1729.88] and they're struggling with that. Well, actually that's a place where machine learning could come in
[1729.88 → 1734.12] and actually solve part of that problem for them. Can I actually do something that helps them with their
[1734.12 → 1739.52] own KPIs such that I build this trust with this organization? And so it's not like, you know, as much
[1739.52 → 1744.88] as we would like to talk about like code and if it was just faster, if it was just easier, if it was just
[1744.88 → 1751.40] simpler, then we could get data science done. Focusing on that data part and being part of the team is
[1751.40 → 1757.14] actually the skill that stands on its own beyond any technical skill that you develop over your career.
[1757.14 → 1763.74] This is practical AI and I have a very practical question, which I think it is sort of a boring
[1763.74 → 1768.12] question, but I think it actually could be really helpful to people. So like you were talking about
[1768.12 → 1773.54] in part of data science education, machine learning, like we don't talk a lot about this like project
[1773.54 → 1780.68] management side of things. And I'm guessing there's probably even listeners out there, data scientists,
[1780.68 → 1788.86] who maybe they have, let's say it's a data scientist who has like a background in science or something
[1788.86 → 1797.56] or academia. And their idea of project management is like, oh, I have like a notebook with some things
[1797.56 → 1802.48] written down in it. And then on the other end, you have like maybe data scientists coming from like a
[1802.48 → 1807.00] software engineering background and their idea of project management is, okay, I have a JIRA board
[1807.00 → 1812.42] or a sauna, these sorts of tools. And maybe there's, you know, other backgrounds as well.
[1812.72 → 1819.32] I could see like how the notebook isn't going to get you totally to a good place. I could also see
[1819.32 → 1825.50] how some of these other systems like a JIRA or a sauna, it could be overkilled for like managing what
[1825.50 → 1830.82] you need, especially if you're like a solo data scientist working on projects. Do you have any
[1830.82 → 1836.90] recommendations in terms of like some things that are not overwhelming? It doesn't have to be a system,
[1837.00 → 1842.68] or like a product, but like things to look into that can just make your project management
[1842.68 → 1848.92] workflow work for a data science scenario? Yeah, it's a good question. I'll start with,
[1849.14 → 1853.92] I really like Trello. So if we're talking about products, just products generally, like Trello
[1853.92 → 1858.70] is a fantastic place to start. If you are that person that's just like written things down in a
[1858.70 → 1863.54] physical notebook, Trello tends to be like a good step forward in terms of something that's shareable
[1863.54 → 1868.06] and everyone can see it. Not overwhelming. Exactly. It's, it's really great. You can build
[1868.06 → 1871.66] templates in it. And so, you know, like these are the things I need to put together for my,
[1871.76 → 1878.58] you know, data science project. But beside that, the thing that I find is very hard to beat is Google
[1878.58 → 1885.38] Sheets. Google Sheets is a fantastic tool for almost any workflow. Google Sheets is great. Like
[1885.38 → 1890.76] usually when I come into a new organization that doesn't have sort of a project management muscle,
[1890.76 → 1896.18] I start with a spreadsheet because it's so easy to change, so easy to update. It's, you know,
[1896.28 → 1901.76] you can add a new column, remove a column you're not using. It's super, super easy. And you do that
[1901.76 → 1908.36] for like a quarter, like manage 10 projects through a Google Sheet and see what actually is helpful in
[1908.36 → 1913.66] terms of making sure everyone knows when things are due, what the deliverable actually is. How do we
[1913.66 → 1920.16] know we're done? Like what stages does our project go through? Like iterate on those in a Google Sheet for a
[1920.16 → 1924.14] while. And then you'll have this system that really makes sense to everyone because everyone's been
[1924.14 → 1929.22] using it. And then you can level it up with an interface like a Trello if you wanted to. So that is my
[1929.22 → 1934.32] secret to almost every workflow is put a Google Sheet somewhere that's, you know, connecting some pieces
[1934.32 → 1938.64] for a little while. And that's what's going to teach you what you actually need in order to manage that in the
[1938.64 → 1939.02] long term.
[1939.88 → 1946.70] Yeah, that's awesome. I wonder too, like with that, so project management is one thing, but then there's like,
[1946.70 → 1953.14] we're just talking about the people side as well. Communication wise within a small company,
[1953.72 → 1959.10] you know, I've had experiences in the past where I am maybe managing my own thing and I think I'm
[1959.10 → 1965.54] managing it well, but I'm doing that in a silo and I sort of crank on something for like a month
[1965.54 → 1971.84] and then try to lob something over the fence or something like that. So do you have any recommendations
[1971.84 → 1979.62] with regard to that and really kind of developing that empathy and good communication of data science
[1979.62 → 1983.44] within a smaller organization between like key stakeholders?
[1984.00 → 1987.52] It's a fantastic question as well. I love like you're hitting on all the things,
[1987.64 → 1990.06] all the pitfalls of working in a very small organization.
[1990.70 → 1992.70] It's only because I've hit the mind.
[1992.70 → 2002.12] Yeah. The thing that comes to mind with that is really the understanding that success in a project,
[2002.12 → 2008.52] you can do as well as you want in a project. Your product itself can be perfect, but at the end
[2008.52 → 2014.52] of the day, that product won't be able to make it to your end customer without passing through a few
[2014.52 → 2022.36] more hands. And when you really tie your project success, not to the trained model, but to the
[2022.36 → 2028.08] deployed model that is in front of your customer, your end customer, it starts to really raise the
[2028.08 → 2033.42] priority of understanding what happens downstream of the output of your workflow. So the output of our
[2033.42 → 2039.04] workflow is like this trained model, right? Even like a pipeline of inference, an inference pipeline for
[2039.04 → 2044.68] this trained model, that's the output, but that pipeline has to connect somewhere and there's got to be
[2044.68 → 2050.78] someone who's doing that connection. And that is one of the tricks that I use to really raise in my own mind,
[2050.78 → 2057.30] the priority of having good relationships with people up and downstream of me. And so good relationships
[2057.30 → 2062.48] downstream, as you kind of pointed out, regular communication really helps with that. Having a project
[2062.48 → 2066.86] management framework where you've got deadlines, and you're meeting your deadlines, and you're giving
[2066.86 → 2072.02] people regular updates along the way really goes a long way in earning trust in that up and downstream
[2072.02 → 2076.84] relationship with anything like that. When you're, as you've, we've mentioned a couple of times, that
[2076.84 → 2080.50] means that's another task. Like I can imagine someone listening and being like, oh my gosh, not only do I need to
[2080.50 → 2084.20] figure out how to do my pipeline, but I also need to figure out like project management and I need to figure out a
[2084.20 → 2090.84] communication strategy. Making all of those things as light touch as possible is really important. So if you have
[2090.84 → 2096.76] your project management framework in your Google sheet, something as simple as updating that Google sheet,
[2096.92 → 2101.78] copying those rows out, putting it in an email and saying, this is my update for the week. Here's where we are
[2101.78 → 2107.36] really leaning on those like agile frameworks of simple standup. Here's what I did last week. Here's
[2107.36 → 2112.40] what I'll do next week. And here's when I'll be done. Those very simple mechanisms and training yourself
[2112.40 → 2117.92] to make them simple and keep them regular is really, really critical. I have a follow-up, which I'll get
[2117.92 → 2123.44] to in a second, but just something that you said that was really resonating with me is I'm currently,
[2123.44 → 2127.64] though I've spent a lot of years in small companies, I'm currently in a large company,
[2127.64 → 2136.58] but just before we started this conversation, I was in a work meeting. I was with a development team, and I was
[2136.58 → 2143.32] thinking exactly that. I was literally saying, no, no, we need to lighten this up. We're too heavy-handed. I think
[2143.32 → 2149.36] it's one of those small company things that could be used very well in many large companies is don't overdo it.
[2149.62 → 2155.50] Light as well. So I just wanted to say I really resonated with that when you were saying that. You've done a perfect
[2155.50 → 2160.96] job of kind of talking about the need for trust and finding those opportunities and communicating.
[2160.96 → 2167.58] But as we move forward with data science and small organizations, and there are all these opportunities
[2167.58 → 2174.60] for growth of the small organization by really absorbing data science beyond just your role as
[2174.60 → 2181.76] the data scientist, but kind of affecting all the other functions. As you build that baseline of trust
[2181.76 → 2188.26] and you're actively communicating that, how do you approach getting people who aren't thinking about
[2188.26 → 2192.70] the benefits of data in a business context? So they're not doing your job, they're doing their
[2192.70 → 2198.82] job, but there are so many ways that if you kind of get data centric about in a non-technical way that
[2198.82 → 2205.20] you can get benefit from that. How do you bring people along on that journey? Because it's a hard thing to do.
[2205.20 → 2211.50] It takes a very savvy touch to bring people to see something that's not normally their forte,
[2211.74 → 2217.34] that's your forte, but they can benefit tremendously. What are some of the ways of bringing all of those
[2217.34 → 2222.68] other people along in their own right? Yeah. The reason why I like this question so much is
[2222.68 → 2229.66] in a small organization, when you're kind of one of a few data scientists, you have this responsibility
[2229.66 → 2233.24] that you're not just representing your work, you're actually sort of representing the discipline
[2233.24 → 2237.78] within that company. And I think there are a lot of companies going back to like the beginning of
[2237.78 → 2243.34] our conversation that are not doing data science because they maybe like dip their toe in and really
[2243.34 → 2249.14] got burned. And that one project where there was a lot of promise, but it never panned out,
[2249.74 → 2254.86] turn them off of wanting to do data science kind of like for a long time. So these cycles tend to be
[2254.86 → 2259.02] really long. Trust cycles like that tend to be super, super long. Maybe like two or three years later,
[2259.02 → 2263.56] they're like, maybe something's changed in the landscape that would make me want to try it one
[2263.56 → 2270.34] more time. So knowing that is sort of serious. Like when you're the one data scientist, it's kind
[2270.34 → 2275.82] of serious to be like, I not only have to do my work well, I have to convince folks in this
[2275.82 → 2280.32] organization that this discipline can do something for their organization beyond what they're doing
[2280.32 → 2286.14] today. So with that in mind, one of the things that I think is really critical is thinking of yourself
[2286.14 → 2291.96] as not just delivering a product, but educating about what that product is and its benefit,
[2292.36 → 2298.16] which is why having a very strong A-B testing framework, maybe unintuitively, maybe intuitively
[2298.16 → 2303.94] is so important. If you're not familiar with how to deploy something and A-B test it at the same time,
[2304.00 → 2308.78] such that you can describe its impact, that's one of the biggest differentiators I've seen in small
[2308.78 → 2314.24] organizations that really just love their data science team versus like, I don't know why we are doing
[2314.24 → 2320.16] this, right? That's a huge differentiator. Yeah. And so that education point, it's very hard.
[2320.50 → 2327.26] I used to say this quite a bit when I would review resumes. There is a primacy to delivering results.
[2327.88 → 2332.84] Anything else when you're reviewing someone's resume, a lot of times that's the output of kind
[2332.84 → 2338.02] of all the inputs in their resume, what the results have been driven. That can tell you a lot
[2338.02 → 2342.18] about how well do they manage projects? How well do they work in a team? Like all of those things kind
[2342.18 → 2347.14] of ladder up to delivering results. And so when you think about earning trust within a small
[2347.14 → 2353.10] organization, thinking about delivering results as being the output of earning trust, doing your
[2353.10 → 2356.80] work well, you know, training your models well, having good relationships with the people along
[2356.80 → 2361.26] the pipeline, that's what will really point you there. And once an organization sees those results,
[2361.26 → 2365.02] it's actually very tough. You'll have more work on your plate than you'll know what to do it.
[2365.10 → 2371.56] That's what I found. We've talked a lot about challenges related to being a data scientist in a
[2371.56 → 2377.90] small organization or like things that you need to be thinking about. I'm wondering what from your
[2377.90 → 2386.12] perspective, because I've definitely seen some of these things, what advantages does like a small
[2386.12 → 2392.34] machine learning organization or machine learning practitioners in a small organization,
[2393.08 → 2399.84] what advantage do they have compared with machine learning engineers, let's say at a huge tech
[2399.84 → 2406.00] company in terms of what they're able to do. Because I think oftentimes that's not highlighted,
[2406.00 → 2411.90] like some maybe what you can do in that scenario, it's maybe harder to do in a large tech company.
[2412.20 → 2413.54] Have you run across those things?
[2414.26 → 2417.60] Interestingly, that's part of the reason why I like doing it in small companies, because
[2417.60 → 2422.20] when you do data science at a large company, you have to think about things like,
[2422.70 → 2428.24] how do I parallelize the compute for this, so that I can actually get this pipeline to run?
[2428.24 → 2430.62] Three billion users or whatever.
[2431.04 → 2437.56] That's right. So there's this part of the machine learning tech stack that I find the most complex,
[2437.88 → 2442.26] the hardest to understand, the hardest to become expert in, the hardest to deploy,
[2442.80 → 2448.80] are that edge where you have very, very high number of users, an incredibly large amount of data,
[2449.40 → 2454.18] latency requirements that are very stringent, like this inference needs to happen in 300 milliseconds,
[2454.18 → 2459.76] or like everything is off. Those constraints don't tend to happen in small businesses,
[2459.76 → 2464.88] you tend to be looking at tabular data, you tend to be looking at batch inference. And those are
[2464.88 → 2468.60] things that are actually fairly straightforward to learn when you like to sit down, and you look at like,
[2468.66 → 2473.04] what technologies do I have to do batch tabular inference? It's fairly straightforward in most
[2473.04 → 2480.62] platforms. And so I think the advantage is that you actually get this vista of the machine learning
[2480.62 → 2485.40] discipline at a small company that you don't tend to get at a larger organization in a larger team,
[2485.40 → 2491.16] you tend to have a fairly narrow aperture of like, I'm looking at my features have been engineered by my
[2491.16 → 2496.82] data engineering team, I'm then doing some last mile stuff on that data to put it in my model and crane.
[2497.42 → 2503.48] And then I'm handing that model artifact off to my Flops team, and they're doing all the CCD stuff.
[2503.70 → 2509.00] So your aperture is very narrow. And so you tend to not be able to see the innovation that's happening
[2509.00 → 2513.94] in Flops or the innovation that's happening in, you know, data engineering, leading up to your
[2513.94 → 2518.92] model training that I think is fascinating. It's so interesting to do and be a part of.
[2519.38 → 2524.20] So and then you get the chance, like, if it turns out for some people who did modelling for a while,
[2524.28 → 2528.80] that, for instance, that worked for me, they will get a chance to do some of the Flops stuff.
[2528.84 → 2533.66] And like, you know what, I like Flops. That's what I want to do. And so you get the chance to
[2533.66 → 2537.94] actually see these different roles and try them out. And then you could go deep, you could say,
[2537.94 → 2541.98] I'm going to do Flops, and I'm going to be an expert in Flops. That's what I want to spend my
[2541.98 → 2546.74] time on and then go do that at any size organization. So you got me thinking about
[2546.74 → 2550.50] this, because as you're talking about that, and you're really making me think back to my small
[2550.50 → 2555.76] organization time. But I'm also in a large one right now. And as a comment before I ask,
[2556.52 → 2562.50] in large companies, you're often at the mercy of arbitrary decisions of others that may not be
[2562.50 → 2568.62] as informed as you are as the data scientist. And that happens all the time. But you've kind of
[2568.62 → 2572.58] differentiated this kind of different opportunities at the different size companies.
[2573.00 → 2578.62] If someone came, and I was asking you for guidance on like, what kind of company should I target?
[2579.04 → 2584.72] There's a clear set of kind of generalists, but a lot of opportunity at small companies to try
[2584.72 → 2590.48] different things. And then there's this opportunity at large companies that you may have to accept what
[2590.48 → 2596.34] they give you. But within that scope, you can go deep. How would you recommend someone try this or
[2596.34 → 2601.32] that? You know, if someone's looking to you for that mentorship, how do you steer them the right way?
[2601.80 → 2607.92] I think it takes a combination of things to be a data scientist in a small organization.
[2608.64 → 2614.86] I actually tend to recommend that less often than at a more established organization. In particular,
[2614.86 → 2620.92] if folks are coming just out of school, I tend to not recommend looking at smaller companies as their
[2620.92 → 2625.88] first job, particularly if that company is just starting their data science muscle, which usually
[2625.88 → 2630.66] you can find out when you're doing an interview with them. Like, am I employee one or sub 10, you know,
[2630.94 → 2636.60] doing data science at this organization? Usually I'll steer people away from doing those roles if
[2636.60 → 2641.50] they're early in their career, because there's so much about that role that's not taught at, say,
[2641.50 → 2646.52] a university. I tend to find people just out of college don't know how to set up their own data
[2646.52 → 2651.08] science pipeline from end to end, how to interview someone really rigorously to understand how does
[2651.08 → 2656.12] this requirement tell me how accurate this model needs to be, you know, making that translation.
[2656.46 → 2663.32] I tend to recommend sort of mid or larger size companies for a first rule so that you can learn
[2663.32 → 2669.64] from other people that have done this for a little longer and have built this sort of intuitive ways
[2669.64 → 2676.74] of doing data science, you can pick up some of those frameworks from them. But if one, it is a startup
[2676.74 → 2684.88] that is led by a CTO or CPO or CEO that has deep expertise in data science has seen it elsewhere, that
[2684.88 → 2690.56] can be a fantastic opportunity to be mentored by someone really directly. So I tend to sort of put them
[2690.56 → 2695.74] on that spectrum of like, if you're brand new in data science, I tend to recommend a more seasoned
[2695.74 → 2699.62] organization. So you can pick up some of this stuff that simply is learned on the job. Sadly,
[2699.64 → 2704.04] like as much as I wish I could point at like a blog or, you know, a course or something like
[2704.04 → 2708.90] that, that would teach you end to end data science workflows. I actually don't, haven't found one.
[2709.06 → 2714.40] Please send one to me if you have found one, but because that doesn't exist, I tend to say,
[2714.50 → 2718.64] you need to see it. You need to see it and really take that opportunity to learn, not just your,
[2718.74 → 2723.20] your narrow aperture, but really try and observe what the people upstream of you and downstream of you
[2723.20 → 2728.38] are doing so that you know that end to end workflow. And from there, a smaller company can benefit
[2728.38 → 2733.94] from what you've learned at that large organization. As long as you have this desire to really hands-on
[2733.94 → 2738.80] own it ends to end. If your desire is that the person upstream of you is doing a lot of the data
[2738.80 → 2743.84] preparation, please do not go into a small company. If you hope that someone's going to tell the story
[2743.84 → 2747.54] of how good your work is, don't go to a small company. That's going to be your job. But if you
[2747.54 → 2753.10] really love this, like, I want to be the one that takes this whole thing and, and a small company is
[2753.10 → 2755.06] where I would tend to send people.
[2755.58 → 2761.46] That's a great perspective. As we kind of wrap up here and get to the end, I'm just curious, as you look
[2761.46 → 2766.80] forward to the future, that could be something with storytellers and the work that you're doing there,
[2766.80 → 2772.24] or just generally in the industry, what, what's exciting to you and encouraging to you as you look to the
[2772.24 → 2772.52] future?
[2773.04 → 2779.28] I'm most excited as we built this company and seen how much need there is in smaller companies
[2779.28 → 2787.56] for data science techniques and how hard it still is for these companies to find, hire, you know,
[2787.68 → 2794.90] keep data science talent. I'm super excited about the opportunity to show how much data science can
[2794.90 → 2801.06] help a relatively small organization and prove out that case. Like data science really works here.
[2801.06 → 2808.68] And from that, I think that will spark some ideas around, you know, Flops tools tend to really focus
[2808.68 → 2814.74] on enterprise use cases, large teams that are solving very complex problems. I'm excited to see
[2814.74 → 2820.82] tools that are really aimed at solving these constants that small businesses run into lots of
[2820.82 → 2825.40] disparate data that needs to be brought together in order to build these models and deploy them simply
[2825.40 → 2831.76] like a very simple sort of layer for that. I'm super excited about that. Furthermore, I also, as you mentioned,
[2831.86 → 2837.10] Jasper, I'm really excited about how like large language models will play into this idea of deploying
[2837.10 → 2842.22] data science within organizations. Will it make people more familiar with the concept of data science
[2842.22 → 2847.10] to where they're more ready? They're like, I see this value other people are getting. Can I try this
[2847.10 → 2854.72] in my organization? And then lastly, I would say, I'm really excited for how I see the data science
[2854.72 → 2861.10] community generally, maybe starting to pivot away from excellence as being measured as state of the
[2861.10 → 2867.66] art performance towards excellence as being measured as impact within some sort of vertical. Like there's
[2867.66 → 2873.56] so many areas that data science could really, I mean, not to sound like the like Silicon Valley,
[2873.56 → 2878.74] like, like stereotype, but really could make the world a better place, right? You know, you think about
[2878.74 → 2886.56] like how data science can help universities identify when a student needs some sort of service
[2886.56 → 2891.74] in order to help them get their degree. Like that's a very practical thing and something that I haven't
[2891.74 → 2897.68] seen many universities really embrace yet. It's one of those small organizations that still tends to
[2897.68 → 2904.14] have a little reticence around adopting data science techniques. But if we can point towards data science
[2904.14 → 2912.26] outputs, as being driving impact, not just the accuracy of our models, then I think we'll see that
[2912.26 → 2917.12] adoption really start to grow within these smaller organizations.
[2917.70 → 2923.88] That's awesome. Well, thank you so much for joining us, Kirsten. It's been a great conversation. And yeah, I know
[2923.88 → 2930.34] I've got, I've got a lot of tips, I think that I can articulate better now with even with my own team
[2930.34 → 2934.98] after the conversation. So thank you so much for joining us. Thank you. I really appreciate it.
[2943.90 → 2949.04] All right, that is our show for this week. If you dig it, don't forget to subscribe,
[2949.50 → 2954.90] head to practicalai.fm for all the ways. And if practical AI has benefited your life,
[2955.12 → 2960.10] pay it forward by sharing the show with a friend or a colleague. Word of mouth is the number one way
[2960.10 → 2964.72] people find shows like ours. Thanks again to Vastly for fronting our static assets,
[2965.04 → 2969.58] to fly.io for backing our dynamic requests, to Break master Cylinder for the beats,
[2969.82 → 2974.54] and to you for listening. We appreciate you. That's all for now. We'll talk to you again on the next one.
