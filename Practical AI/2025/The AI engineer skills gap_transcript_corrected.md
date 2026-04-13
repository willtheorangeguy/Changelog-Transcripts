[0.00 → 8.74] Welcome to the Practical AI Podcast, where we break down the real-world applications
[8.74 → 13.64] of artificial intelligence and how it's shaping the way we live, work, and create.
[13.88 → 19.14] Our goal is to help make AI technology practical, productive, and accessible to everyone.
[19.48 → 23.54] Whether you're a developer, business leader, or just curious about the tech behind the
[23.54 → 25.12] buzz, you're in the right place.
[25.12 → 29.84] Be sure to connect with us on LinkedIn, X, or Blue Sky to stay up to date with episode
[29.84 → 33.02] drops, behind-the-scenes content, and AI insights.
[33.36 → 35.88] You can learn more at practicalai.fm.
[36.18 → 37.50] Now, on to the show.
[47.88 → 51.44] Welcome to another episode of the Practical AI Podcast.
[51.44 → 53.32] This is Daniel Whitelaw.
[53.48 → 58.78] I am CEO at Prediction Guard, and I'm joined, as always, by my co-host, Chris Benson, who
[58.78 → 61.66] is a Principal AI Research Engineer at Lockheed Martin.
[61.90 → 62.58] How are you doing, Chris?
[62.98 → 64.38] Hey, doing very well today, Daniel.
[64.42 → 64.94] How's it going?
[65.30 → 70.74] It's going really well, because I have a close friend joining us on the podcast today and
[70.74 → 72.12] a previous guest.
[72.28 → 77.62] We went through the Intel Ignite Accelerator program together in different companies.
[77.62 → 84.42] And yeah, just really excited to have with us Rain Mohammadi with us, who is an adjunct
[84.42 → 90.36] professor at Northeastern University and also Lead Principal AI Engineer at basest.
[90.66 → 91.54] Welcome, Rain.
[91.82 → 93.14] It's good to see you again.
[93.56 → 94.34] Yeah, thanks, Dan.
[94.68 → 95.12] Yeah, Chris.
[95.16 → 96.54] It's always great to be back.
[96.80 → 97.68] Yeah, yeah.
[97.68 → 101.06] I've been excited to talk through these things.
[101.22 → 107.82] And even before the show, obviously, you're kind of living in two worlds.
[107.82 → 112.60] You're living in the industry world, and you're living in the academic world.
[112.60 → 117.42] And you've kind of been living in those two worlds for quite some time, which is interesting
[117.42 → 126.12] because you have a perspective on how, for example, data scientists or AI people or machine
[126.12 → 132.42] learning people are being trained and what those people are actually doing in industry,
[132.42 → 138.14] which I find really intriguing, especially because so much has changed.
[138.14 → 147.20] I guess maybe that's a good initial question is, is my perception right that the role of
[147.20 → 155.36] an AI person or a data scientist or a machine learning person in industry, like that, the day-to-day
[155.36 → 163.94] life of that person has really changed dramatically over the past even few years.
[163.94 → 168.30] And I'm curious if the academic side has kept up with that.
[168.96 → 169.14] Yeah.
[169.32 → 170.80] So I think that's an interesting question.
[171.00 → 175.80] I think we need to break it down into multiple sections.
[176.66 → 180.96] Because, I mean, let's just start first, do a quick review of what has happened.
[180.96 → 186.54] You know, because we're talking about the complete transformation of the AI and data science
[186.54 → 187.16] job market.
[187.40 → 194.02] You know, I mean, if you remember, and it was about like a decade ago back in 2012, our
[194.02 → 198.44] business review, they call data science is the sexiest job of 21st century.
[198.68 → 198.86] Yeah.
[198.90 → 200.36] That's why I got into it.
[200.74 → 203.52] Obviously, that describes what I want it to be.
[203.52 → 209.84] And if you think about it, that one phrase, it kicked off a massive gold rush.
[210.02 → 210.96] Everyone wanted it.
[211.14 → 214.30] Universities were spinning up the new master programs overnight.
[214.86 → 217.14] And the promise was pretty simple.
[217.44 → 223.10] Get a degree and learn a little bit of machine learning, and you're insensitive employable.
[224.06 → 226.62] That promise feels like almost like a myth now.
[226.62 → 231.54] I mean, if you talk with any new graduate today, especially someone looking for their
[231.54 → 234.84] first role, the feeling is totally different.
[234.94 → 235.36] It's brutal.
[235.48 → 236.76] The market is absolutely brutal.
[237.06 → 238.98] We see job posting for entry level.
[239.26 → 242.84] You know, that job requires about three years of experience.
[243.18 → 244.26] The demand has changed.
[244.62 → 245.82] It's shifted fundamentally.
[246.04 → 250.38] It's not about what do you know about it from the textbook anymore.
[250.52 → 252.06] It's about what can you build?
[252.06 → 256.98] Can you deploy and maintain a real, like a scalable AI system?
[257.26 → 259.70] It's kind of like that's the new currency of hiring.
[259.98 → 268.44] I think one time, Chris, I don't know if this was us that came up with this discussion,
[268.44 → 274.48] but I remember quite a while ago we talked about kind of like full stack data scientists
[274.48 → 276.10] or something like that.
[276.10 → 282.44] The idea being like you could figure out what kind of modelling you needed to do.
[282.98 → 289.00] You could do the prototyping and POC, but you could also like to deploy something to actual
[289.00 → 291.36] cloud environments or something like that.
[291.48 → 297.94] I mean, that seems like quite a tall order, Rain, because you're basically saying like,
[297.94 → 305.88] be a software, like a proficient software engineer, but also be an infrastructure person.
[306.10 → 311.12] And also, and there's this, I don't know, I've heard a lot of people say there's not really
[311.12 → 314.08] like a full stack engineer doesn't really exist.
[314.74 → 321.10] So yeah, is it, I guess from that perspective, how much of what a data scientist or machine
[321.10 → 327.48] learning or AI person fits into those different buckets at this point, whether it's software
[327.48 → 333.06] engineering or infrastructure work or actual like knowledge of differential equations or
[333.06 → 334.28] statistics or something?
[334.96 → 336.30] I think that's also a great point.
[336.38 → 340.88] So if you think about back to data science job, the idea of data science job was that
[340.88 → 345.38] your job is kind of done once you got a good score in the notebook.
[345.66 → 350.88] You know, that the classic, my model has 95% accuracy on the test data, and you're good,
[350.88 → 352.20] you pass it to someone else.
[352.92 → 360.06] And then if you remember, I think it's around 2020s with this, some resources like Google
[360.06 → 366.56] Cloud Rules of Flops, you know, it laid out this new realities that successful ML needs
[366.56 → 368.80] a home suit of real engineering escapes.
[370.04 → 376.02] The things like containerization with Docker, CCD pipeline automation, monitoring, and you
[376.02 → 380.66] know, you have to know if that your model actually works in the real life.
[380.66 → 381.88] And then you need to monitor it.
[381.90 → 385.16] And after you deploy it, you need to basically look for the drifts, you know.
[385.60 → 389.58] So industry made it really clear that job wasn't just build a model anymore.
[389.58 → 391.94] It's kind of like you need to own the pipeline.
[393.12 → 398.26] So, and then if you think about it, all of a sudden the analysts or data scientists went
[398.26 → 403.82] from just being a simple analyst to be on engineers who build and maintain the intelligent
[403.82 → 404.50] systems.
[404.50 → 412.58] And so just as that engineering bar was being raised by Flops, along comes the second, maybe
[412.58 → 415.34] even bigger tidal wave, you know, the generative AI.
[415.88 → 423.18] And that becomes like around 2023 explosion that you can see in the Stanford AI index basically
[423.18 → 426.34] dimension that this was not just a cool new tool.
[426.68 → 428.34] This was an automation event.
[428.34 → 433.96] You know, I immediately attacked the entry point in the field that they could do those
[433.96 → 434.70] jobs basically.
[435.34 → 439.78] You know, it's kind of sort of this shift was drastic from the data scientists to Flops
[439.78 → 441.76] engineers and all of a sudden AI basically.
[442.30 → 447.46] In addition to that, there's so much more diversity in, you know, as we were talking a moment ago
[447.46 → 451.48] about the notion of the full stack engineer, especially at the entry level, trying to fit into
[451.48 → 456.52] this and the notion of like what is full stack is changing fairly rapidly.
[456.68 → 458.36] There are a lot of different options out there.
[458.82 → 464.30] And not only do you have to try with that entry level student have to try to fit in to
[464.30 → 469.40] the notion of what, you know, an organization is looking for, but there's all these variations
[469.40 → 470.66] on that.
[470.66 → 475.76] And if they're not in the right variation of what that organization is looking for in terms
[475.76 → 480.74] of this abundance of skills that are required for that given position, they're still out of
[480.74 → 481.02] luck.
[481.20 → 486.88] I mean, it's really a crap shoot for students today in terms of trying to find the right
[486.88 → 493.82] fit and represent their own ability to fit to the organization that's looking to hire.
[495.04 → 498.56] I'm really glad that I'm not out there in the job market in that way right now.
[498.64 → 499.38] It would be brutal.
[499.70 → 500.18] Yeah.
[500.52 → 502.20] So I think that's true.
[502.36 → 507.80] It's like, if you think about it, as this AI wave comes in and this series of automation
[507.80 → 512.02] tasks, basically, AI made certain things simpler.
[512.68 → 517.06] Those are like the types of tasks, like a bullet per task that you always used to give to the
[517.06 → 518.02] new hire, basically.
[518.24 → 519.80] You know, it's kind of like the groundwork.
[520.78 → 527.48] And for someone who's an early hire, recent graduate, those type of job work kind of like
[527.48 → 529.10] the first step on the ladder.
[529.28 → 534.34] How to, for example, you write a complex SQL query to get the data, make simple Python,
[534.34 → 536.80] and get your hand dirty with the company's data.
[536.96 → 537.86] You learn about it.
[537.90 → 539.62] And also, you show your skills, you know.
[540.76 → 542.94] But now, it's no longer like that.
[542.98 → 548.22] So you need to basically find the correct fit, what they exactly want, what they want to build.
[548.28 → 549.90] So I show that I can build that.
[550.18 → 557.64] And there was this study from OpenAI and University of Pennsylvania that they look at this task
[557.64 → 562.84] exposure to large language model and the takeaway that they had was pretty simple.
[563.20 → 569.84] Any repeatable task that used to be given to juniors, I highly want to bring to AI, basically,
[570.10 → 570.66] and innovations.
[571.14 → 575.68] So if a junior analyst used to take all this afternoon, write the SQL queries and make the
[575.68 → 578.56] dashboard, now AI can just write it with a great prompt, right?
[578.56 → 586.12] So, basically, the economic case for hiring a big group of, you know, attorneys and have
[586.12 → 589.20] them to do the work and has evaporated.
[589.32 → 591.14] You know, there's kind of like a change.
[591.20 → 598.04] For example, I used to hire lots of interns to basically help with the development and speed
[598.04 → 598.94] up the process.
[599.38 → 604.20] And since AI shift, to be honest, I just use AI for all of those tasks.
[604.20 → 608.30] You know, so this has been this big change.
[608.46 → 613.84] And of course, you know, we are seeing this shift in hiring strategy kind of everywhere
[613.84 → 616.38] in big tech or even in startups.
[616.62 → 621.30] They're just stop hiring for potential, and they are starting hiring for proven capabilities.
[621.98 → 624.44] It's kind of like the paradigm has changed.
[624.74 → 629.54] New companies these days basically afford to bring in 50 juniors or spend a couple of years
[629.54 → 630.32] to train them.
[630.32 → 636.30] You know, they'd rather to hire five or maybe 10 people that already have built or developed
[636.30 → 638.32] some complete system from day one.
[638.62 → 643.60] So, it's kind of like, if you think about it, that new entry-level jobs is technically
[643.60 → 647.04] what we would call mid-level engineers a couple of years back.
[647.46 → 648.98] You know, this shift is terrible.
[649.56 → 654.38] And with this kind of with this new bar, it's not like that, you know, you don't need knowledge.
[654.38 → 659.38] So, all this, you know, deep statistical knowledge, heightened skills, they're all essential.
[659.70 → 663.40] But they are just, at this point, they are kind of prerequisites.
[663.92 → 665.08] They are the ticket to the game.
[665.18 → 666.52] They are not how to win it.
[666.74 → 668.12] You know, it's kind of, it has here.
[668.20 → 670.00] You need to prove that you can build.
[670.34 → 672.14] The company wants what you build.
[672.30 → 674.28] And then, you know, you go for hiring.
[674.28 → 681.18] I'm wondering, because that bar has been raised, like you say, the kind of mid-level positions
[681.18 → 686.88] that we used to call mid-level or maybe the entry-level ones now, how does that change?
[687.10 → 694.14] Because, I mean, maybe this is a negative view that I'm about to give, but I'm very pro,
[694.42 → 695.62] you know, higher education.
[695.62 → 701.68] But I also think, like, even whether you look at computer science or data science sort of
[701.68 → 708.60] education, a lot of that does not, even before the recent shift that you talk about, it didn't
[708.60 → 714.12] always connect to what you were actually going to do in your day-to-day work, right?
[714.28 → 720.16] So, now not only does it not connect to that entry-level kind of day-to-day work, but does
[720.16 → 729.84] it now even increase that divide where, like, how could we possibly train people to come
[729.84 → 732.94] in as mid-level kind of data science folks?
[733.02 → 739.50] Because I think if I'm interpreting what you're saying correctly, it's not that AI is making
[739.50 → 744.96] data scientists no longer relevant or AI or machine learning people no longer relevant.
[745.10 → 746.00] It's still very relevant.
[746.00 → 752.04] It's just the stuff that entry-level data scientists or machine learning people used
[752.04 → 756.62] to do and kind of, you know, level up on, that's no longer available.
[756.76 → 758.60] So, where are they going to do that?
[758.68 → 764.92] And is it even reasonable for us to think that universities could help get them up to that
[764.92 → 765.78] level, I guess?
[766.20 → 769.66] Yeah, I think, so I would answer to that question in two sections.
[769.80 → 774.62] I think one part is about where is academia stands right now?
[774.62 → 779.50] And then the second part would be talking about the industry versus academia right now.
[779.80 → 782.64] So, let's just start with where does academia stands?
[782.86 → 788.02] You know if you think about it, and I kind of call this, I don't want to be negative,
[788.22 → 790.90] I call it educational bottleneck, you know?
[791.22 → 795.50] And to be clear, the first thing is that, you know, the faculties that we have in CS, ML,
[795.58 → 797.22] data science department, they are all brilliant.
[797.22 → 801.92] You know, they are like world-class at teaching the fundamentals, the math, theory, history,
[802.12 → 805.78] the research, that foundation is non-negotiable.
[806.00 → 806.68] You need it.
[806.84 → 809.52] But the curriculums often just stop there.
[809.72 → 811.66] And it used to be also kind of like that.
[811.76 → 817.00] And you stop at the theory and leaves basically this huge gap between what the student learns
[817.00 → 820.52] and what employees actually need for them to do on the first day.
[820.52 → 824.76] As an example, you know, a student might spend the whole semester learning about the math
[824.76 → 830.20] and all sorts of like optimization, back-replication techniques, stuff like that, which is necessary.
[830.44 → 835.74] But as soon as they graduate, they basically see this job market that wants them to deploy
[835.74 → 839.88] on the Kubernetes, or they know how to work with all different cloud resources, you know?
[840.16 → 846.78] So, they know exactly how the engine works, but they actually never try to drive a car into traffic.
[846.78 → 855.16] And, you know, there was this new post by Andrew Engine recently that he argued this urgent shift in education.
[855.32 → 856.76] I'm going to paraphrase what he said.
[856.84 → 860.04] He said, knowledge is great, but skills are greater.
[860.32 → 867.78] Meaning that in the field that's moving this fast, you have to teach the practical skills to get the work done.
[868.00 → 875.58] You know, you need to basically give the capacity to get meaningful work done by having a proper knowledge and proper training.
[875.58 → 879.40] So, this is exactly what the job market is selecting for now.
[879.88 → 883.54] So, that's the view that I have on education at the moment.
[884.50 → 892.90] And the second part that we can basically talk about is like a comparison between where is industry versus academia.
[892.90 → 901.42] And there is a perfect study by MIT, a recent study basically that the stats are staggering.
[901.64 → 913.28] They say that right now about 70% of the AI PhDs are just skipping academia and go to job market, go to basically industry directly.
[913.28 → 917.42] And that's a huge brain drain for the universities, you know.
[917.88 → 929.24] And the second is that, which is the real clear risk, and I'm sure you know about this, like 96% of the major state-of-art systems comes from industry labs, not from universities anymore.
[929.82 → 932.14] So, a university is already falling behind.
[932.14 → 937.40] And then companies like Google, Meta, OpenAI, they are the one that's defining the frontier now.
[937.72 → 938.80] They are building the tools.
[938.90 → 940.24] They are setting their standards.
[940.90 → 943.24] And that's the absolute core of the bottleneck.
[943.62 → 946.86] Academy curriculums moves on a cycle of years.
[947.64 → 952.30] Getting a new course approved, like updating a textbook, it's a slow.
[952.30 → 963.36] By the time a university approves one new course to be, like let's say, for example, LLM application course to be added to curriculums, the tools have already changed three times, you know.
[963.52 → 969.18] So, the entire framework is really different because, you know, it took a while.
[969.42 → 975.00] And that has happened to me also, like I developed a course and take years to get approval to teach that course.
[975.06 → 980.42] And then you need to go back and update everything that you were planning to teach because, you know, the industry has changed already.
[982.30 → 990.74] Well, friends, when you're building and shipping AI products at scale, there's one constant.
[991.40 → 991.84] Complexity.
[992.26 → 995.94] Yes, you're wrangling models, data pipelines, deployment infrastructure.
[996.42 → 999.48] And then someone says, let's turn this into a business.
[1000.00 → 1001.24] Cue the chaos.
[1001.44 → 1009.18] That's where Shopify steps in, whether you're spinning up a storefront for your AI-powered app or launching a brand around the tools you built.
[1009.18 → 1015.46] Shopify is the commerce platform trusted by millions of businesses and 10% of all U.S. e-commerce.
[1015.76 → 1019.92] From names like Mattel, Gymshark to founders just like you.
[1020.46 → 1030.68] With literally hundreds of ready-to-use templates, powerful built-in marketing tools and AI that writes product descriptions for you, headlines, even polishes your product photography.
[1031.24 → 1032.86] Shopify doesn't just get you selling.
[1033.10 → 1034.72] It makes you look good doing it.
[1035.12 → 1035.86] And we love it.
[1036.06 → 1037.26] We use it here at Changelog.
[1037.26 → 1039.88] Check us out, merch.changelog.com.
[1040.08 → 1041.38] That's our storefront.
[1041.84 → 1043.70] And it handles the heavy lifting too.
[1044.02 → 1048.20] Payments, inventory, returns, shipping, even global logistics.
[1048.84 → 1052.76] It's like having an ops team built into your stack to help you sell.
[1053.10 → 1055.92] So if you're ready to sell, you are ready for Shopify.
[1056.54 → 1063.66] Sign up now for your $1 per month trial and start selling today at Shopify.com slash practical AI.
[1063.66 → 1068.88] Again, that is Shopify.com slash practical AI.
[1068.88 → 1083.50] So, Rain, I love how you highlighted this kind of divide between academia, industry, like what that is in reality.
[1083.50 → 1090.98] And anecdotally, I remember actually last year or maybe a year and a half ago.
[1091.12 → 1092.26] I live by Purdue University.
[1092.26 → 1093.96] I was like walking through campus.
[1094.88 → 1100.16] And they were just finishing their – they had this new building, right?
[1100.16 → 1104.78] And so this was 20, whatever, 2024, right?
[1105.22 → 1108.44] And it said like Hall of Data Science, right?
[1108.94 → 1117.44] And I thought – my immediate thought in my mind is like in 2017, you could have created a Hall of Data Science.
[1117.70 → 1119.58] Now you need a Hall of AI.
[1119.82 → 1122.06] Like you're building the wrong Hall.
[1122.52 → 1126.94] To their credit, I think they actually – so I just looked this up while we were talking.
[1126.94 → 1129.90] I mean, they did rename it Hall of Data Science and AI.
[1130.16 → 1133.98] So to their credit, they at least caught up with the name.
[1133.98 → 1139.90] But yeah, I guess like obviously you're an educator.
[1140.88 → 1150.48] And so you see that there is value in trying to have these formal – formal education serves a purpose
[1150.48 → 1155.40] and is different from maybe on-the-job training.
[1155.40 → 1166.92] What do you think – or have you seen examples where these sorts of practical skills are built up in an academic environment
[1166.92 → 1174.68] rather than just kind of the theory or the knowledge as you were kind of drawing the distinction there?
[1174.68 → 1181.38] Yeah, so actually that's something that we have been doing for almost the last three years.
[1181.70 → 1189.02] So I basically developed this course, this FLOPS course at Northeastern University almost three years ago that we have been ongoing.
[1189.50 → 1190.76] So the idea was this.
[1191.26 → 1193.28] This is like about three, four years ago.
[1193.38 → 1198.12] I was this hiring manager and I used to do lots of interviews for our team.
[1198.12 → 1208.58] And I always basically interviewed smart, motivated, good school basically candidates, but most of them struggled with the same thing.
[1208.70 → 1212.10] They understood the theory, but they couldn't build anything.
[1212.28 → 1213.30] They couldn't ship anything.
[1214.16 → 1220.30] And that's when it clicked for me that, okay, if the industry – I personally as someone who was in the industry and academy –
[1220.30 → 1225.42] expect these students or these basically candidates to build a real system from day one.
[1225.42 → 1228.80] And then I know in the industry we don't teach them that.
[1228.96 → 1230.28] Could we do something about it?
[1230.54 → 1232.74] So I started working on this course.
[1232.82 → 1241.10] I built this FLOPS course that every semester right now we have about 150, 270 students within one class, like a huge classroom.
[1241.90 → 1248.02] And instead of just learning the concept, they start by choosing a domain that they actually care about.
[1248.10 → 1251.36] Healthcare, finance, sport, robotic, and whatnot.
[1251.36 → 1257.60] Then, as a team, they spend the entire semester on building one real product.
[1258.12 → 1260.48] And this real product is not just homework assignment.
[1260.64 → 1261.52] It's not a toy example.
[1261.68 → 1266.06] It's a real working system with deadlines, milestones, deliverable.
[1266.54 → 1270.06] Just like a real – like an actual ML and software team.
[1270.06 → 1280.12] And the best part of that is we wrap up the semester – the way that we wrap up the semester is that the students basically present their product at our FLOPS Expo,
[1280.78 → 1286.54] which is a full industry partner event we have been holding over the last, I think, two years now.
[1287.08 → 1290.28] This year, for example, we partnered with Google.
[1290.28 → 1299.92] So we are hosting in two weeks, December 12th at Google Main Campus in Boston, and where our students are pretty hyped to come there.
[1300.04 → 1301.14] But they will basically what they do.
[1301.22 → 1305.46] They show, they demo the actual product that they have built.
[1306.62 → 1309.00] And so the whole course is simple.
[1309.42 → 1311.46] You don't just learn ML anymore.
[1311.62 → 1313.50] We teach you how to build with it.
[1313.50 → 1321.34] And the idea for me was to give the students this hands-on experience that companies are looking for right now.
[1321.60 → 1328.28] And honestly, watching the students go from, I have never deployed anything before, to me and my team, we built a real product this semester.
[1328.46 → 1330.10] That's kind of like the best part for me.
[1330.10 → 1344.42] One, at least, hypothesis that I have here, which I would love your opinion on, Rain, is on one side, you have highlighted how this kind of gap is widening, even,
[1344.80 → 1350.46] like between the theory and where you need to come into a job, like at a mid-level.
[1350.46 → 1364.92] At the same time, this revolution of Gen.AI has been happening, which in some ways, to your point, some of those things are the things that are being automated by AI.
[1365.10 → 1379.76] But it's also enabling maybe this younger generation of software engineers, AI people, to actually perform at a higher level out of the gate, but in a different way.
[1379.76 → 1398.70] So not like, there's kind of a burden on maybe us as prior generation data scientists and machine learning people to understand that students and new hires need to, from the start, be doing their data science work differently.
[1398.70 → 1409.82] So just by way of anecdote, we were talking about this a little bit before the show, that my wife owns an e-commerce business, Black Friday, Cyber Monday just happened.
[1410.94 → 1422.64] I, you know, day-to-day in my company, you know, I'm not doing as much kind of hands-on work on the product as I was given my role as CEO.
[1422.64 → 1425.40] But it was like, it was nice to go back.
[1425.64 → 1427.94] So for like four days, I helped them during the sale.
[1428.08 → 1440.18] And I just sat in a room doing like customer lifetime modelling and like updated forecasts for 2026 and looking at churn and analyzing like customer journey and all this stuff.
[1440.18 → 1457.26] And number one, it was a ton of fun, but I was kind of coming at it from that perspective and kind of reentering some of those things that maybe I hadn't done as much for a little while, or even, you know, maybe since the previous year when I helped them with forecasting.
[1457.26 → 1469.18] Like I was able to get tons of that done so quickly because I was having AI honestly write most of the code for me.
[1469.32 → 1476.32] The thing though was I still had to play the data scientist to get from like point A to point B.
[1476.32 → 1490.14] There was no way that like I could have just said to any AI system like, hey, I want like write a three sentence prompt and get out all the, you know, lifetime modelling and forecasting and all of this stuff.
[1490.28 → 1503.86] I still had to play that kind of data science orchestrator and know what the things were, know what, you know, modelling techniques were relevant, know maybe what trade-offs were and other things.
[1503.86 → 1527.20] So do you think on the one hand, it's maybe depressing that the academic kind of industry gap is widening, but on the other hand, maybe there's, am I right that there's an opportunity to actually like lean in for, for these students in terms of different ways of their, of working to like to get to a higher level faster?
[1527.20 → 1537.68] I'm not sure about the higher, getting to the higher level faster part, but just, I saw a new talk recently by Neil Ahoyen over at Google.
[1538.22 → 1541.12] And he made a great point that about this data science job.
[1541.22 → 1548.90] And basically was saying that the data science job is, it's not gone, but AI is just forcing them to change dramatically.
[1548.90 → 1556.22] It's, it's no longer is about analyzing the data or building certain, you know, certain of dashboards and stuff like that.
[1556.22 → 1562.42] As we say, you can just window the knowledge, just prompt it properly and just having the data and just build that quickly.
[1562.98 → 1574.00] You know, so there are certain, certain types of tasks that he used to do for try to climb the ladder to learn more and more, but that they are not the same anymore.
[1574.00 → 1581.62] And the expectation is not for you also to do the same task because, you know, if this company is hiring you, probably these days they want more.
[1582.36 → 1600.18] But I think it is a really great point that for hiring managers or for someone that's, when you hire someone on your team or have someone new juniors on your team, you need to also account for helping them to like mentoring them properly to be sure that they can evolve and learn.
[1600.18 → 1611.42] Otherwise, we basically take this cognitive ability from them because they even want, if you just ask everyone to just build, build, and they just use AI, they don't, they're never going to learn basically how to build.
[1611.48 → 1616.60] So we take that cognitive ability away from them to just build new, faster products.
[1616.90 → 1630.06] Yeah, I think you're really onto something there in terms of, you know, like one of the things that, that I have done for the last few years is, is I'm a capstone sponsor for capstone projects at Georgia Tech.
[1630.18 → 1632.16] In the, in the College of Computing.
[1632.16 → 1637.68] And so, as, and I'm doing that from my nonprofit role as opposed to my day job.
[1637.82 → 1644.94] And so, when I work with different teams there, I think one of the challenges is they're kind of bringing what they know.
[1645.46 → 1652.54] You know, certainly Gen AI capabilities have helped them, you know, step up a little bit along the way in terms of figuring it out.
[1652.54 → 1666.40] I think the areas that I've noticed that they're still struggling, the students are, there's, you know, going back to, to Dan being a data scientist over the weekend instead of a CEO at that moment, is he's bringing all that business knowledge.
[1666.40 → 1673.58] You know, years and years and years of business knowledge and understanding about what's really needed in that.
[1673.94 → 1684.20] And I think that's, you know, that's one of those things that is, is part of the struggle with junior level is, is there's the kind of concept of I've learned tools in university.
[1684.20 → 1689.70] And I'm trying to bring them to bear, and they're not always the right tools for the organization they've joined.
[1690.00 → 1701.42] And they don't necessarily know how to combine that with all the other, all the other tie-ins that that organization may need that were not necessarily something accommodated in their, in their academic development.
[1701.42 → 1712.72] And so, you know, that's kind of exacerbated by the fact that now with Gen AI kind of replacing a lot of those junior roles coming in and, and, you know, how do you, how do you ramp up?
[1713.60 → 1725.26] It does seem to your point, like things are actually getting like, even though we have new amazing tools in, in the form of Gen AI capabilities, it seems like things are getting harder to bridge that gap.
[1725.26 → 1738.86] And, and I'm not sure how you do that because it's a combination of both kind of the, the experience of being in the real world along with fast moving, you know, a fast moving technical landscape to navigate.
[1739.10 → 1745.46] Are you seeing that from your side with students and, and how are you tackling some of those, those subtleties that are there?
[1745.96 → 1747.08] Yeah, actually definitely.
[1747.08 → 1753.60] So two weeks ago, I sent out a survey to my students and I asked them basically to take a couple of questions.
[1753.60 → 1756.62] And I specifically did it for our talk.
[1757.24 → 1760.98] And so as part of the survey, basically, there were some questions.
[1761.16 → 1771.08] And one question was, which is 60% basically of the, of the students, they say that they are taking online courses on top of what they are taking in the school.
[1771.62 → 1780.22] And another question, 82% of the students say that they're participating in hackathons in order to learn how to quickly to build.
[1780.22 → 1795.48] And about 46% of the time they are attending workshops, you know, so they are building their own parallel curriculums through side project, open source contributions or certification to AWS Google, you know, and that's exactly it.
[1795.58 → 1798.22] You know, the portfolio kind of has become a new credential.
[1798.98 → 1800.36] It's no longer about your grades.
[1800.50 → 1802.26] It's like about what you have as a portfolio.
[1802.26 → 1811.76] And this is also important for us to kind of like a dose of reality that this self-learning path isn't easy and isn't equitable.
[1812.06 → 1815.68] You know, it takes tons of time and costs lots of money.
[1816.22 → 1823.44] And if you want to practice building a real production grade system, working with a cloud service that always costs money, you know, as those commercials.
[1823.44 → 1835.26] And how many students, like if you think about the students already paying a thousand intuitions, they cannot also afford thousands of dollars per month for cloud computing, you know, to practice.
[1835.36 → 1836.74] So it's kind of like a huge change.
[1836.80 → 1838.48] It creates this resource divide.
[1838.80 → 1842.74] And at this point, I think the bar isn't just higher.
[1842.90 → 1847.60] It's kind of also financially more expensive for the students to learn.
[1847.60 → 1852.96] And right now, for example, shout out to our friends at Google.
[1853.30 → 1861.48] You know, they give us lots of credits for our Flops course every semester because our students, they can't otherwise build anything in the real world.
[1861.82 → 1866.94] And I personally reach out to lots of providers in the industry.
[1867.28 → 1868.32] And I say, hey, you know what?
[1868.42 → 1870.98] We train these students to use your tools.
[1871.22 → 1875.04] Give us some cloud credits so they can basically learn and build a phone.
[1875.04 → 1878.44] But yeah, that's my take on that.
[1879.42 → 1896.54] Well, Rain, I am kind of intrigued because, well, on the one side, you're thinking very in an innovative way about how to bring this kind of skill or reducing the skill gap, being creative in the academic setting to get people these skills.
[1896.68 → 1900.78] But also, you know, you're a practicing AI engineer.
[1900.78 → 1904.10] What have you seen kind of personally?
[1904.40 → 1907.96] Because you're already operating at a higher level.
[1908.92 → 1925.74] Are there also changes, any like significant changes that you've noticed in your day-to-day work over the kind of past few years that have caused you to think about your day-to-day tasks differently?
[1925.74 → 1943.56] Like more so than the entry-level type of folks, but actually ways that you're fundamentally thinking about your workflows or how you're doing this kind of higher, maybe higher skill or higher level kind of data science AI stuff.
[1943.64 → 1946.14] I'm wondering if anything stands out for you.
[1946.66 → 1947.14] Yeah, definitely.
[1947.36 → 1949.90] I mean, I personally have been part of this shift.
[1949.90 → 1952.58] I started my career as a data scientist.
[1953.44 → 1958.48] Then, like in 2018, I started as an ML engineer, and it just went up.
[1958.76 → 1961.26] Then, last year, I started as an AI engineer.
[1961.56 → 1964.46] So, I also have been part of this change myself.
[1964.48 → 1965.84] Data, ML, AI.
[1966.22 → 1966.60] Exactly.
[1966.76 → 1967.70] The same pattern.
[1968.52 → 1971.96] And for me, when I look at them, they are kind of similar.
[1971.96 → 1977.44] If you put the data science aside, because that was kind of like there was no production.
[1977.56 → 1979.70] There were lots of research, especially around it.
[1979.90 → 1982.98] But when you go to ML and AI, just the terminology is different.
[1983.10 → 1984.58] They're technically kind of similar.
[1984.84 → 1995.24] I think that the main difference that I personally felt is that I need to, in my day-to-day work, to work a lot with LLMs because it's a requirement for certain things.
[1995.24 → 2009.12] I work a lot with larger models, which requires you to have a better understanding on, you know, it's kind of like a GPU optimization, how to break your models and basically ensure that they're optimal, basically.
[2009.12 → 2015.28] And those changes, you know, it wasn't something that you do maybe a couple of years ago.
[2015.90 → 2023.70] So, I ended up personally trying to read a lot, you know, spend summer, just read different books to learn, to advance my own career.
[2023.92 → 2026.18] And I always talk about this with my students.
[2026.18 → 2028.96] When I learn something new, I bring it to the class.
[2029.20 → 2032.70] I was like, okay, I was recently basically reading about this.
[2032.92 → 2033.98] And this was fascinating.
[2034.10 → 2034.88] This is the link.
[2035.04 → 2038.04] And maybe I sometimes give them a small lecture also on it.
[2038.04 → 2043.46] But I think, yeah, so it's like the change is there for everyone, not just for a junior.
[2043.74 → 2046.90] It's like it doesn't matter if you're a principal or a junior technically.
[2047.28 → 2056.56] But who's getting, being more impacted, I think that's the part that's kind of like unfair, you know, to the juniors technically or recent graduates.
[2056.56 → 2069.00] I'm curious to extend this out a little bit, you know, as we kind of went from the challenge of juniors and Dan introduced, you know, the challenge of kind of us, you know, as people who are past that point in their life.
[2069.00 → 2078.98] But, like, we have fast coming, you know, fast changes are coming even more in the sense of, like, we're hitting that point where physical AI is really on the rise now.
[2079.36 → 2084.42] You know, not just in certain industries as it has been historically, but in many industries.
[2084.42 → 2087.40] It's, you know, it's exploding outward at this point.
[2087.54 → 2095.68] And we all have challenges in terms of incorporating these new realities into what we're doing and how we're going to learn about it.
[2095.68 → 2107.64] What does that imply at the university level when you're getting back to students, and they're already, you know, you're already trying to bridge the gap into the corporate world or the startup world or wherever they're going to be productive.
[2107.88 → 2114.28] But you also have this explosion in terms of the places that AI is touching in new and different ways.
[2114.36 → 2125.00] What are what are the implications on the curriculum and on the burden that professors have to try to get their students ready for that next thing, which is steam rolling over us already?
[2125.00 → 2126.52] I think it depends.
[2126.70 → 2131.56] So let me just I know some other schools are doing that, but I'm going to speak with respect to Nurses.
[2131.64 → 2140.02] For example, Nurses Curry College of Computer Science, they as of this year, basically 2026, they are updating their curriculums finally.
[2140.24 → 2144.48] So they and not everything is going to be a small shift, but gradual, basically.
[2144.48 → 2150.74] So they are introducing some more practical courses into the curriculums.
[2150.74 → 2161.62] And also, for example, they are weaving their ethics directly into the coding part of the curriculums, you know, but this is going to be kind of like a slower shift on the curriculum side.
[2161.62 → 2174.18] But on the other end, from the teaching perspective, you know, and this is like kind of like AI is kind of like a double-edged sword at this point, because students, you know, they all use AI.
[2174.36 → 2175.62] They are using degenerative AI.
[2175.62 → 2178.06] So they basically, which is great.
[2178.38 → 2184.14] I would tell my students, you know, use it, but don't lose to it, you know, kind of like you need to use it, don't lose it.
[2184.14 → 2195.36] So it's kind of like you need to be sure that you can learn, move faster with this type of thing, not to just give away all the autonomy and you just basically, you just use them for everything.
[2196.22 → 2206.86] And so and then from the other end, from the teacher's perspective, it's kind of difficult because when you give, for example, homework or labs to students, it's just especially coding.
[2206.96 → 2209.38] I'm not talking about writing an essay, like coding perspective.
[2209.38 → 2217.46] You don't know, you can't even tell that if they wrote the code or not, everyone returned great codes these days, you know, and then there's the homework.
[2217.92 → 2230.10] And there's no way for you to just say that, like, it's written by AI or not, you know, they're really smart to fucking how to change the temperature to ensure that the result is not being detected.
[2230.10 → 2241.90] So, so, so, so again, this is like kind of like a double-edged sword, but also from the other end is like, because there are lots of information, lots of changes in the market, in the industry, in the domain.
[2241.90 → 2246.58] And every day, like every day, like every day you read the news, there's a new article, there's something coming out.
[2247.14 → 2251.32] And it's hard for basically academia to keep up with that.
[2251.44 → 2259.74] You know, it's like a new academy is falling far behind the industry, and it's going to go into this, this gap is going to just expand the way that it is.
[2259.74 → 2266.26] And I think at some point, industry need to help academia.
[2266.84 → 2270.10] It shouldn't be just academy need to keep up with the industry.
[2270.52 → 2276.34] If the industry needs new talent to come later, you need to step forward.
[2276.56 → 2278.22] And I say that, okay, you know, let me also help them.
[2278.30 → 2279.42] Let me start some program.
[2279.52 → 2282.20] Let me participate in some of the courses that they have, you know?
[2282.48 → 2288.34] So otherwise it's kind of like a chasing a ball, like an academy just constantly trying to keep up.
[2288.34 → 2290.00] And that's not going to win.
[2290.44 → 2290.92] That's fair.
[2291.08 → 2298.04] And I think that's a good notion that I think industry really needs to consider as investments back.
[2298.16 → 2298.88] I agree.
[2299.02 → 2301.72] I think it's been largely a one-way street there.
[2302.20 → 2308.82] I would like to flip a little bit the timeline around to the students that are coming in.
[2308.94 → 2310.62] And I'm asking this selfishly.
[2310.72 → 2314.66] I have a 13-year-old daughter in eighth grade.
[2314.66 → 2321.16] She is, we have been applying to magnet schools and things like that and getting her ready for her high school experience.
[2321.94 → 2324.50] And she has never been someone interested in AI.
[2324.66 → 2326.28] That was dad's thing and all that.
[2326.40 → 2335.12] But as she has started looking at what she wants to do, she's starting to recognize that whatever that is, AI will impact her significantly going forward.
[2335.12 → 2341.92] So it's not just the kids that are focused on technology at this point, but all the kids.
[2342.08 → 2351.16] And as she does that, and they're entering into high school, what advice do you have for what high schools need to do before they come to you?
[2351.26 → 2359.70] Before you're getting those students, and you're trying to prepare them for industry and a career and moving through their lives, you have students coming to you.
[2359.70 → 2372.82] What would you like to see from high schools in terms of how they prepare these kids to be better or more ready to come into your care as a professor so that you can do the thing that you do?
[2373.28 → 2373.42] Yeah.
[2373.54 → 2374.98] So I think that's a great point.
[2375.56 → 2378.04] And there are already two shifts.
[2378.18 → 2386.12] I have been spoken by neighbours, similar question that, hey, my kids, should they go back, go to college for computer science anymore?
[2386.26 → 2387.54] Should they study this anymore?
[2387.54 → 2393.98] And I think the answer is that, yes, you know, there will be shifts in the market.
[2394.10 → 2395.88] And it's not just computer science.
[2395.98 → 2396.82] It's not just AI.
[2397.16 → 2398.94] AI is going to impact so many things.
[2399.42 → 2402.72] Some areas like it's slower, but some areas much faster.
[2403.32 → 2409.48] And at some point, all of us basically become somehow we need to learn how to work with AI.
[2409.48 → 2420.66] And I think it's perfect if from high school you understand the concept, not maybe the math, the theory behind AI, but just to learn, okay, in general, how does AI work?
[2420.70 → 2424.60] There are lots of AI capabilities that you don't even need the math behind them.
[2424.66 → 2429.36] You can just build a system just by knowing how to put the components together.
[2429.36 → 2438.90] So if they could, like from high school, go to part of the workshops or participate in some sort of like a training stuff, build something simple.
[2439.34 → 2445.22] You know, that automatically opens lots of doors, like a thinking process for you for the future.
[2445.38 → 2453.26] As you go to like after high school, and you want to go basically to universities, and you learn in different courses, different concepts, you're like, oh, I know.
[2453.26 → 2455.20] Maybe I can build something around this.
[2455.60 → 2458.94] You know, I always think that everyone can be an entrepreneur, you know.
[2459.26 → 2463.72] It's kind of like as long as they have the correct mindset and the energy for it.
[2463.72 → 2473.78] So if they already have been trained from high school, and they have not trained in a bigger way, just kind of this easier way of training, like teaching,
[2474.56 → 2482.88] they could potentially advance more in university in compared to students that they just want to learn during the university.
[2483.26 → 2492.50] Well, I know that we've talked a lot about kind of lot of perspectives, both from the industry side, from the academic side.
[2492.70 → 2501.94] I think all of us on the call, though, are generally excited about kind of certain parts of the ecosystem, the way that they're developing.
[2501.94 → 2515.86] From that side of things, as we get closer to the end here, Rain, what as you look at the ecosystem, because you're, again, you have multiple views of this ecosystem from the industry side, from the academic side.
[2515.86 → 2521.50] What's most exciting for you as you're kind of entering into this next year?
[2521.50 → 2529.50] And maybe it's something like, oh, I can't wait personally to, you know, have the time on a weekend to explore this.
[2530.34 → 2533.14] Or maybe it's something you're you're already getting into.
[2533.14 → 2534.48] But yeah, definitely.
[2534.66 → 2539.26] Actually, I recently purchased the Ritchie Mini.
[2540.28 → 2542.28] Yeah, yeah, yeah.
[2542.36 → 2543.40] The robot, right?
[2543.46 → 2546.60] The little it's kind of a desktop type robot.
[2547.20 → 2547.64] Yeah.
[2547.78 → 2552.62] So it's I'm, so I'm pretty excited and waiting for that to be delivered.
[2552.72 → 2555.66] I think it's the delivery is going to be early January, hopefully.
[2556.12 → 2556.70] Finger crossed.
[2556.70 → 2563.36] And I'm pretty excited to work with that and build some capabilities I have in mind.
[2564.44 → 2571.70] And when I think about all these changes, like if you would put me back a couple of years ago, I would have never gone for robotic.
[2571.98 → 2573.24] I'm like, ah, no, you know what?
[2573.26 → 2573.92] It's not my time.
[2574.34 → 2582.28] But now with this AI change, and I already went through the, you know, contents of Hugging Face, which is, these guys are great.
[2582.28 → 2585.58] But reading it through the documentation, I was like, wow, that's pretty straightforward.
[2585.58 → 2592.44] So think about how much AI or change the field that I can easily go buy a robot, like a small robot.
[2592.54 → 2594.40] And I'm planning already ahead of time.
[2594.64 → 2595.68] You also have this simulator.
[2595.86 → 2597.76] So you don't need to wait for it to deliver.
[2597.92 → 2602.28] You build ahead of time the apps and simulate it that it will work on the robot.
[2602.42 → 2604.08] So when the robot comes, you deploy it.
[2604.38 → 2609.34] So that's my go-to, like what I'm excited for in 2026.
[2610.00 → 2611.14] Yeah, it's kind of crazy.
[2611.14 → 2625.06] I feel like when we started in this field, it was like hard enough to get the dependencies installed for TensorFlow and just be able to run any model.
[2625.46 → 2628.14] Just like that in and of itself was like...
[2629.52 → 2631.38] Are you trying to give us PTSD?
[2631.92 → 2633.18] Is that the goal here?
[2633.18 → 2636.58] I mean, TensorFlow and CUBA.
[2637.32 → 2637.86] Yes.
[2638.74 → 2639.08] Yeah.
[2639.28 → 2643.18] It's like, regardless, that was the hardest problem.
[2643.30 → 2649.86] And now you can like to have a whole digital twin of a robot and like do all that.
[2650.04 → 2651.54] It is pretty spectacular.
[2652.44 → 2652.60] Yeah.
[2652.90 → 2655.12] Well, I'm also excited for that.
[2655.20 → 2658.80] I think we do have one coming here to our offices as well.
[2658.92 → 2661.90] So I'm excited to see what that's like.
[2661.90 → 2669.78] I've never done any robotics, really, other than maybe those like what are those Lego robotics sort of things.
[2670.06 → 2673.76] But yeah, excited to see where things are going.
[2673.94 → 2675.86] Thanks for sharing some of your insights with us, Rain.
[2676.00 → 2683.94] It's been a real pleasure and hope to have you on the show a third time to let us know how the robotics went.
[2684.24 → 2685.30] Yeah, I appreciate that.
[2685.36 → 2686.44] Thanks for having me again.
[2686.86 → 2688.02] And it was great.
[2688.02 → 2688.14] Thank you.
[2691.90 → 2695.90] All right.
[2696.06 → 2697.48] That's our show for this week.
[2697.90 → 2704.80] If you haven't checked out our website, head to practicalai.fm and be sure to connect with us on LinkedIn, X or Blue Sky.
[2705.02 → 2708.36] You'll see us posting insights related to the latest AI developments.
[2708.80 → 2710.74] And we would love for you to join the conversation.
[2711.20 → 2715.00] Thanks to our partner, Prediction Guard, for providing operational support for the show.
[2715.34 → 2717.34] Check them out at predictionguard.com.
[2717.34 → 2721.36] Also, thanks to Break master Cylinder for the beats and to you for listening.
[2721.74 → 2722.52] That's all for now.
[2722.84 → 2724.54] But you'll hear from us again next week.
