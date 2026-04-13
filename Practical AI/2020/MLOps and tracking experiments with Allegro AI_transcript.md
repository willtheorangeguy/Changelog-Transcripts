[0.00 --> 12.20]  When we talk about MLOps, we talk about the ability to move from the data scientist's own machine or laptop to training models at scale on some remote machine cluster.
[12.20 --> 18.26]  We're talking about the ability to orchestrate that and do that within a larger team, not just a single data scientist.
[18.74 --> 21.22]  And we're talking about the ability to automate that process.
[21.62 --> 24.60]  That, in general, is what we talk about when we talk about MLOps.
[24.90 --> 26.18]  How is it different than DevOps?
[26.84 --> 28.04]  Well, it's actually very different.
[31.00 --> 33.90]  Bandwidth for ChangeLog is provided by Fastly.
[34.26 --> 36.16]  Learn more at Fastly.com.
[36.38 --> 39.48]  We move fast and fix things here at ChangeLog because of Rollbar.
[39.60 --> 41.28]  Check them out at Rollbar.com.
[41.54 --> 43.70]  And we're hosted on Linode cloud servers.
[44.06 --> 46.06]  Head to linode.com slash ChangeLog.
[48.68 --> 51.46]  This episode is brought to you by DigitalOcean.
[51.84 --> 52.36]  Droplets.
[52.70 --> 53.48]  Managed Kubernetes.
[53.84 --> 54.68]  Managed databases.
[55.22 --> 55.74]  Spaces.
[56.06 --> 56.92]  Object storage.
[57.22 --> 58.46]  Volume block storage.
[58.46 --> 62.22]  Advanced networking like virtual private clouds and cloud firewalls.
[62.42 --> 68.66]  Developer tooling like the robust API and CLI to make sure you can interact with your infrastructure the way you want to.
[69.08 --> 72.58]  DigitalOcean is designed for developers and built for businesses.
[73.32 --> 79.64]  Join over 150,000 businesses that develop, manage, and scale their applications with DigitalOcean.
[80.06 --> 83.42]  Head to do.co slash ChangeLog to get started with a $100 credit.
[83.42 --> 85.90]  Again, do.co slash ChangeLog.
[85.90 --> 103.28]  Welcome to Practical AI, a weekly podcast that makes artificial intelligence practical, productive, and accessible to everyone.
[103.54 --> 107.66]  This is where conversations around AI, machine learning, and data science happen.
[108.10 --> 112.70]  Join the community and Slack with us around various topics of the show at ChangeLog.com slash community.
[112.70 --> 114.04]  And follow us on Twitter.
[114.20 --> 115.82]  We're at Practical AI FM.
[121.62 --> 125.66]  Welcome to another episode of Practical AI.
[126.08 --> 127.50]  This is Daniel Whitenack.
[127.58 --> 130.74]  I'm a data scientist with SIL International.
[131.34 --> 138.58]  And I'm joined, as always, by my co-host, Chris Benson, who is a principal AI strategist at Lockheed Martin.
[138.80 --> 139.58]  How are you doing, Chris?
[139.58 --> 141.16]  I am doing okay.
[141.38 --> 147.04]  It's summertime here in Georgia, and so it is hot and humid, and so I'm just trying to keep from melting.
[147.64 --> 151.38]  Yeah, not unexpected for where you are, I imagine.
[151.38 --> 152.78]  Happens on a regular basis.
[153.36 --> 154.94]  Hot and humid, not the melting part.
[155.34 --> 155.62]  Yeah.
[155.62 --> 160.38]  So I think I mentioned this a couple times on the podcast, but my wife owns a candle business.
[160.38 --> 176.28]  So there's always this, like, during the summer, you've got to figure out the right shipping and tracking so that you kind of minimize the likelihood of candles melting on people's porch before they actually get into their house if you're sending them to, like, Texas or Arizona or that sort of thing.
[176.46 --> 177.16]  That's a good point.
[177.16 --> 179.10]  Yeah, so it's an interesting thing.
[179.40 --> 186.88]  On another, you know, shipping front, I've got a pile of boxes sitting next to me and a computer case.
[187.14 --> 191.66]  All the components for a computer are here at my house.
[191.72 --> 195.16]  So I'm about to build a first AI workstation of my very own.
[195.30 --> 196.94]  So I'm excited about that.
[197.18 --> 197.74]  Very nice.
[197.74 --> 208.08]  Yeah, it would be fun to have an episode, you know, detailing all of the mishaps that happen along the way as I hopefully don't ruin it, but get this thing running, I'm sure.
[208.30 --> 210.52]  So I'm curious, since you brought it up.
[210.86 --> 219.00]  Yeah, I know in the past when we've talked, we both have typically gone to cloud services, especially for personal things that we're doing at home for our own interests.
[219.44 --> 222.32]  What caused you to decide to go this way this time with a desktop?
[222.32 --> 224.10]  I think it was twofold.
[224.22 --> 236.44]  I think partly it was like I haven't built a computer since I was in college, probably, which would have, I don't know, that's over 13 or 14 years, probably 15 years since I built a computer, maybe.
[236.66 --> 238.88]  I thought it would be fun to just do it again.
[239.08 --> 240.46]  So that's partly just fun.
[240.90 --> 245.42]  But then also I'm getting into a lot more of audio models.
[245.42 --> 252.64]  So speech recognition things and spoken language identification and the data sets associated with those are quite large.
[253.18 --> 264.50]  And so sort of carting those around to various cloud machines and also running models for, you know, maybe days instead of hours starts to get fairly expensive.
[264.80 --> 267.66]  So I think those two things made sense to me.
[268.22 --> 268.84]  Well, good luck with it.
[268.84 --> 275.20]  Yeah, we'll definitely have to get an update from you to share with us all what happened and what went wrong and what went well.
[275.42 --> 276.18]  For sure.
[276.66 --> 283.50]  And today we're going to keep the practical train moving with some more topics that are extremely practical.
[283.78 --> 292.12]  Actually, I had seen what we're going to be talking about today, which is some tools from a company called Allegro AI.
[293.04 --> 296.60]  One of my friends pointed me to that, which I'll mention maybe a little bit later on.
[296.60 --> 310.62]  But I also saw PyTorch mentioned recently that Allegro Trains, which is one of the ML Ops and experiment managing versioning things that we're going to be talking about today, joined the PyTorch ecosystem project.
[311.00 --> 314.42]  And I thought that sounded really exciting, also very practical.
[314.92 --> 320.94]  So today we've got with us Nir Barlev, who is the CEO and co-founder of Allegro AI.
[321.64 --> 322.26]  Welcome, Nir.
[322.60 --> 323.88]  Thank you for having me, guys.
[323.88 --> 324.40]  Yeah.
[324.76 --> 337.58]  Before we jump into all of those exciting things about experiment tracking and versioning and ML Ops and all of that, it'd be great to hear just a little bit about your background and how you got involved in this field.
[338.02 --> 338.42]  Sure.
[338.78 --> 343.64]  You know, I've been in the high tech industry for longer than I care to actually say, probably three decades.
[343.64 --> 351.22]  I started as an engineer, actually, and spent about a decade on large ERP systems and that kind of thing.
[351.32 --> 352.40]  This was way back.
[353.02 --> 362.72]  And then by way of an MBA at Wharton, I joined Google and a decade at Google doing everything from working on the mobile team.
[362.72 --> 381.18]  This was right after Google had bought Android and, you know, before the iPhone went out and to actually helping setting up Google's Tel Aviv R&D center to leading Google's European search advertising product and strategy and a number of other roles.
[381.18 --> 384.36]  My last role, I was a GM of mobile payments.
[384.68 --> 393.28]  And yeah, when I decided to look for something else to do, I joined two folks who are, you know, actually my partners now to basically start Allegro AI.
[393.70 --> 402.26]  The way I came at it is I was looking to do something big that can impact the world and that would involve cutting edge technology.
[402.26 --> 408.90]  I mean, after being at Google and doing everything I did, you know, you don't want to do anything less than that, really.
[409.78 --> 423.24]  Yeah, I was going to say, being at Google, if you're thinking of projects that make an impact, a sort of worldwide impact or innovative, it seems like that sets a pretty good trend for your path forward or a high bar to reach, for sure.
[423.34 --> 423.94]  That's correct.
[424.10 --> 429.98]  So, you know, I don't know if I'll be able to build a company as large as Google, but certainly that's the target you want to put for yourself.
[430.64 --> 430.90]  Yeah.
[432.26 --> 433.48]  Yeah, and it is interesting.
[433.72 --> 455.08]  I mean, it seems and I don't know, maybe you have a perspective on this as a CEO and founder, but it seems like there are a number of really innovative startups in the AI space that are kind of playing at the same level as the major players of, you know, open AI and Google and Microsoft and these at the same level at major research conferences.
[455.08 --> 456.88]  You see kind of startups.
[457.02 --> 460.72]  I'm thinking of like Hugging Face or those sorts of startups that are really right there.
[460.72 --> 464.64]  And it seems like such a huge impact for a small team.
[464.86 --> 478.96]  And so, I don't know, as a CEO, if you think about those things, but it seems really interesting to me that there can be these small, really focused teams that make a very large impact on that level.
[478.96 --> 479.96]  Yeah.
[479.96 --> 480.00]  Yeah.
[480.00 --> 486.04]  So, you know, being a Google, I have to tell you, you know, you kind of think that you can probably do anything, right?
[486.46 --> 498.42]  The reality is that, and I've seen that personally on some of the big projects that I was involved with is that, you know, Google didn't execute as well as a startup or as fast.
[498.90 --> 502.32]  Google ended up, you know, acquiring them for less or even a lot money, right?
[502.32 --> 505.24]  And there are a number of examples for that.
[505.70 --> 510.34]  And as a company grows larger, the targets get bigger, right?
[510.46 --> 514.68]  And so, doing anything requires a very, very high bar.
[514.78 --> 518.70]  I remember at some point, I'm talking about like 2007, I think.
[518.70 --> 525.28]  I remember pitching something to, at the time, it was Susan Wojcicki, who was, at the time, I mean, now she's the CEO of YouTube.
[525.46 --> 528.12]  She was the head of advertising.
[529.00 --> 533.20]  And the bar was, you know, if it's not about $100 million revenue, don't talk to me about it, right?
[533.46 --> 535.72]  And you can imagine this is back in 2007.
[535.86 --> 537.02]  So, imagine today.
[537.58 --> 543.52]  And this gives an opportunity for small companies who are very nimble to identify opportunities.
[543.52 --> 548.24]  There's also a different perspective when you're outside of Google as when you're in.
[549.12 --> 560.72]  Especially, I think, in the B2B space, there are opportunities where, you know, at least Google specifically is still relatively behind companies such as Amazon, for example, or Microsoft, right?
[560.78 --> 564.06]  So, you can identify a small company's niches.
[564.16 --> 567.76]  And if you understand that those are going to grow, then that's opportunity.
[567.76 --> 575.94]  So, kind of curious, as you were at Google, and, you know, how did you come up with this idea for what would become Allegro?
[576.26 --> 580.54]  And so, you're kind of, you had been doing that at Google for a while, moving through your position.
[580.84 --> 583.82]  So, what made you think, I have this idea?
[584.10 --> 586.22]  I'm going to make a major change in my life.
[586.42 --> 590.76]  You know, what gave you the motivation to go off and do a startup, find partners?
[591.06 --> 592.48]  Can you give us a little bit of that backstory?
[592.48 --> 598.06]  So, first of all, I can't really take credit for the original idea behind Allegro AI.
[598.28 --> 600.26]  That's actually one of my partners.
[600.84 --> 611.74]  You know, I guess I can take credit in what we formed out of it and what it became because, obviously, as in any company, especially startups, you know, we change and we adapt quickly to find product market fit.
[611.94 --> 618.82]  So, obviously, the vision as it was set or thought of by my partner needed to improve and get better.
[619.06 --> 620.94]  And, you know, that's something that I was involved in.
[620.94 --> 623.10]  But the original idea was not mine.
[623.48 --> 630.90]  It was more of, for my position, you know, I had felt like I had, you know, I'm in Tel Aviv, Israel.
[631.14 --> 635.30]  And it was about relocating my family back to the U.S.
[635.96 --> 640.44]  And at the time, this was about four years ago, it didn't make sense.
[640.44 --> 645.16]  And coupled with the fact that, you know, I joined Google when it was 3,000 people.
[645.64 --> 649.60]  I think it's about 100,000 now or so, you know, on that kind of scale.
[649.78 --> 651.42]  It's a different company in many ways.
[651.80 --> 654.54]  And I had felt like it was an amazing experience.
[654.54 --> 660.30]  And I learned so much, you know, especially, you know, being at Google in that time of growth.
[660.50 --> 668.28]  But, you know, when I left Google, it was a big company with all the things that we all less like about big companies.
[668.28 --> 674.70]  And I felt like, you know, this was an opportunity to do something different and really go out and try to build something on my own.
[674.70 --> 677.98]  And as I mentioned, I looked for something really big that could change the world.
[678.18 --> 688.42]  And, you know, basically as a potential founder, I started, you know, quote unquote dating people, right, to find partners that we could, you know, come up with something that we'd like to do.
[688.42 --> 692.40]  And through that, quote unquote dating process, I met my current partners.
[693.20 --> 696.98]  And it was, you know, we hit it off, as you'd like to say, really quickly.
[697.66 --> 699.10]  They're amazing guys.
[699.40 --> 703.88]  When you're in a startup and you have partners, you're practically in a Catholic marriage.
[704.70 --> 706.38]  For the time until the exit.
[706.98 --> 712.88]  And so you want to make sure that you have people that you can trust and that they're, you know, great people that you can work with.
[713.28 --> 715.86]  And obviously amazingly capable and talented.
[716.52 --> 718.58]  And I found all of that with them.
[718.58 --> 723.38]  And basically, you know, as I mentioned, one of my partners was the one that, you know, was bringing that idea.
[723.48 --> 724.24]  And it came to him.
[724.78 --> 726.74]  He's a longtime serial entrepreneur.
[727.50 --> 732.28]  He's a very interesting profile where he has both a very, very strong engineering background.
[732.28 --> 735.12]  As well as a data science background.
[735.56 --> 740.94]  So the most prestigious lab today in AI in Israel.
[741.68 --> 745.98]  So it's run by Professor Lear Wolf, who's actually now on Facebook.
[746.60 --> 751.26]  And my co-founder, his name is Moses Goodman, was his first, you know, PhD student.
[751.36 --> 753.88]  Which basically means that they, you know, they set up their lab together.
[753.88 --> 759.04]  And so he's really one of the pioneers of deep learning, machine learning, computer vision in Israel.
[759.44 --> 769.20]  And he basically saw what Allegro really is all about is the fact that we need to bring in engineering methodologies into the AI in the process.
[769.44 --> 769.58]  Right.
[769.78 --> 772.04]  That was not the way that he said it at the time.
[772.04 --> 773.58]  But basically, that's the idea.
[773.70 --> 773.84]  Right.
[773.88 --> 775.92]  How do we actually scale things up?
[775.92 --> 778.66]  And I'm kind of curious on that front.
[778.66 --> 780.30]  And you've stated it well.
[780.44 --> 784.54]  And I think that this has been brought up on our show multiple times from different perspectives.
[784.54 --> 795.62]  So I definitely think it is a theme that's kind of surging through the community that we need to be more rigorous in terms of the engineering we put into our workflows.
[795.62 --> 801.12]  And the AI driven products that we're building and putting out and the tools and all of that sort of thing.
[801.12 --> 819.88]  I was wondering from your perspective, what you see as the challenges to kind of what are the sort of main challenges to getting people on board that are currently in data science and AI positions and kind of convincing them that they need to start doing things differently?
[820.06 --> 821.16]  What are some of those challenges?
[821.42 --> 827.40]  Does it have to do with this kind of variety of backgrounds that people come from that it's not just engineers or is it more than that?
[828.18 --> 829.08]  Yeah, that's a great question.
[829.08 --> 833.32]  And the answer, actually, it's a moving target because our industry, right?
[833.40 --> 840.10]  The one that you guys are talking about and the one that I'm squarely in is rapidly evolving and changing, as we speak, at an amazing rate.
[840.26 --> 843.38]  I've never experienced that kind of rate before in my career.
[844.02 --> 845.86]  So generally say this, right?
[845.94 --> 850.02]  I mean, basically, right, it's a very different paradigm, right?
[850.02 --> 851.54]  It's a scientific paradigm, right?
[851.58 --> 857.32]  And initially, people thought, well, you know, I'll get data scientists or research scientists, and that's what I need, right?
[857.32 --> 858.70]  And then they'll be able to do the job.
[859.40 --> 860.98]  Obviously, we all know that's not enough.
[861.26 --> 867.52]  The thing is that there's still, you know, a core and critical part of a team that needs to build something.
[868.12 --> 875.96]  But data scientists, research scientists have a very different, you know, mindset and outlook, right?
[876.00 --> 877.58]  I mean, they've been trained differently, right?
[877.62 --> 880.06]  I mean, at the end of the day, they're scientists, right?
[880.06 --> 885.56]  And if you actually, you know, take it to the extreme, think of that, you know, mad scientist, nothing is in order.
[886.32 --> 887.24]  You know, everything is hectic.
[887.40 --> 889.94]  It's all about their creativity and finding the solution.
[889.94 --> 892.44]  And there's a lot of truth in that.
[892.54 --> 894.84]  Obviously, that's an extreme exemplification.
[895.16 --> 896.32]  But there's a lot of that.
[896.32 --> 897.44]  And that's changing.
[897.86 --> 905.90]  But we found, you know, throughout the course of the last three years that, you know, data scientists, research scientists have been very much against adopting any tools.
[905.90 --> 907.96]  Because, you know, they came out of university.
[908.48 --> 911.18]  They were focused on, you know, on the science.
[912.12 --> 917.52]  Tooling, they didn't understand the value of tooling, the value of processes.
[918.28 --> 923.24]  In some ways, you might say, you know, maybe even, you know, were a little bit wary, right, of tools.
[924.00 --> 925.80]  And is that going to be good for them or bad for them?
[925.86 --> 930.50]  It wasn't even something that they were exposed to during their curriculum of their training.
[930.50 --> 935.64]  On the flip side, you know, they felt like, you know, I'm a, for example, PhD out of whatever Stanford.
[935.86 --> 937.20]  I mean, I should know everything.
[937.32 --> 943.16]  A lot of times, we saw relatively very junior data scientists leading AI teams.
[943.74 --> 945.04]  Not just in small companies.
[945.56 --> 946.92]  In very large companies, right?
[946.96 --> 952.68]  Because if you're not a Google or Microsoft or Facebook, you're not going to get the cream of the crop.
[953.08 --> 957.84]  And the last thing is, you know, their bosses didn't know what the heck they were doing.
[958.30 --> 960.76]  They didn't even know how to actually measure what they were doing.
[961.36 --> 964.50]  And as I mentioned, they thought that, you know, bringing those people in would be enough.
[965.16 --> 970.36]  And so a lot of that created the situation where, you know, the background of, you know, why do I need tools?
[970.76 --> 972.16]  And a lot of that still exists.
[973.04 --> 987.32]  Now, I think, but, you know, a lot of people who have engineering background of actually sort of doing data science or, you know, ML engineering and data engineering because, you know, because it's new, it's interesting, salaries might be higher, et cetera.
[987.84 --> 992.24]  Companies have realized that they're not seeing productivity out of the data science teams.
[992.76 --> 996.34]  And so that shift has been happening in the last, I guess, year or year and a half.
[996.78 --> 999.20]  We've seen companies integrate, right?
[999.34 --> 1005.14]  Their data scientists and research scientists into a larger product team, right?
[1005.16 --> 1012.48]  That has the engineers and the product leadership, et cetera, DevOps to really, you know, push them to ultimately build a product.
[1012.48 --> 1015.48]  Because it's not about coming out with a research paper, right?
[1015.48 --> 1021.82]  Ultimately, if you're sitting in a company, most of the time it's about building a product or a service.
[1022.76 --> 1038.06]  And so I think now what we've seen is oftentimes a situation where there's a very big underappreciation of what it takes to build a state-of-the-art tool chain to support you.
[1038.06 --> 1045.82]  And I remember talking to someone that was way back in the day, was pushing, you know, SQL databases.
[1046.14 --> 1046.96]  Imagine that, right?
[1047.04 --> 1048.60]  I mean, this is prehistoric times.
[1049.22 --> 1055.14]  And he was telling me how he had trouble pushing that into organizations because they thought they were going to build it themselves.
[1056.00 --> 1059.96]  Obviously, you know, anyone who tried to do that fell flat on their faces.
[1059.96 --> 1061.44]  Same thing here.
[1061.88 --> 1065.24]  And we've had situations, you know, that's changing a lot.
[1065.36 --> 1071.50]  But we've had situations where, you know, a couple of years ago, companies would tell us, what are you talking about?
[1071.52 --> 1072.64]  I can build this in three weeks.
[1073.50 --> 1074.92]  I mean, they believe that, right?
[1075.38 --> 1076.60]  After we showed them what we built.
[1077.04 --> 1085.46]  You know, today, a lot of these companies, because tools didn't necessarily exist or they weren't aware of them or they thought they could build it, you know, have invested internally and built something.
[1085.46 --> 1087.12]  And you know how it is, right?
[1087.14 --> 1088.10]  Not invented here.
[1088.26 --> 1095.46]  And once you've built, like, a small toy, you're enamored with it, especially, you know, but for this sake, I'll say us engineers, right?
[1095.66 --> 1099.20]  I remember as an engineer, I was enamored with some of the things that I built.
[1099.72 --> 1108.70]  And so that's kind of the hurdle that we as an industry that, you know, is building and pushing tools need to try to get around or over.
[1115.46 --> 1145.44]  Thank you.
[1145.46 --> 1149.60]  Join more than 15,000 enthusiastic readers.
[1149.84 --> 1151.96]  It'll cost you exactly zero dollars.
[1152.32 --> 1156.04]  And you can subscribe right now at changelaw.com slash weekly.
[1156.04 --> 1176.00]  So, Nir, I guess as we were starting to get into tools and you were talking about, you know, whether organizations were starting to recognize the need for tools and how did they get productive and measure that productivity.
[1176.38 --> 1183.42]  And that, you know, in a world that, you know, already has things like DevOps and ML engineering and data engineering and such.
[1183.54 --> 1184.92]  We're kind of moving into that area.
[1185.00 --> 1190.14]  I noticed that, you know, kind of front and center on your website, you have this concept of ML ops.
[1190.14 --> 1194.76]  And as you were mentioning DevOps and passing in the tooling before, it really kind of triggered that.
[1194.76 --> 1207.60]  I'm wondering if you can kind of tell us what ML ops means to you in the organization and kind of how does that differentiate itself from DevOps on the software side and other types of ML engineering and data engineering?
[1207.60 --> 1220.24]  Absolutely. So, actually, that's a great question because it actually touches on one point where, you know, ML ops itself as a term is not something that is set already.
[1220.58 --> 1223.76]  And different companies are using it to mean slightly different things.
[1223.76 --> 1227.86]  You know, that's one of the issues, you know, that's one of the issues, again, with our industry.
[1228.02 --> 1230.72]  So, early on, that terminology is not set.
[1231.42 --> 1249.20]  When we talk about ML ops, you know, we talk about the ability to move from the data scientist on machine or laptop, right, to training models at scale on some, right, cluster, right, remote machine cluster.
[1249.20 --> 1256.82]  We're talking about the ability to orchestrate that and do that within, right, a larger team, not just a single data scientist.
[1257.16 --> 1260.08]  And we're talking about the ability to automate that process.
[1260.56 --> 1264.76]  That, I guess, in general, is what we talk about when we talk about ML ops.
[1265.16 --> 1266.64]  How is it different than DevOps?
[1267.92 --> 1269.20]  Well, it's actually very different.
[1269.92 --> 1275.28]  So, I guess, you know, let's define DevOps at a very high level, right?
[1275.28 --> 1302.54]  I mean, basically, the idea behind DevOps is that you want to make sure that a piece of software that usually is already tested, QA'd, and stable, right, that has left development and is now going into production to serve users or, you know, workloads, needs to work at scale and needs to stay up all the time, right?
[1302.54 --> 1305.70]  And you need to make sure that it can sell across many machines, et cetera.
[1305.84 --> 1308.78]  That, at the end of the day, is what DevOps is tasked to do.
[1309.24 --> 1311.60]  And so, basically, what did we say here, right?
[1311.60 --> 1320.52]  We said that there was a single piece of software, that it was tested, and it works, and that you need to take that and you need to scale that up and replicate that, right?
[1320.90 --> 1322.82]  And that happens only in production.
[1323.60 --> 1327.90]  Well, in AI, everything around that is actually different.
[1327.90 --> 1334.06]  So, first of all, as you guys know, right, machine learning, deep learning experiments can be very, very heavy workloads.
[1334.20 --> 1338.10]  I mean, you actually mentioned that yourself when you talk about building your own computer at the beginning, right?
[1338.74 --> 1341.52]  You're going to run things that are going to take hours, right, or even days.
[1342.18 --> 1350.72]  And so, unlike regular software, you need to be able to run stuff on large machines from day one, right, in terms of development.
[1351.44 --> 1352.58]  So, that's one big difference.
[1352.58 --> 1358.16]  The second thing is what you're doing is you're running software that's not tested because you're doing it during development.
[1358.84 --> 1361.48]  The third thing is you're running experiments.
[1361.96 --> 1366.96]  And what you're trying to do, right, obviously, is run a lot of experiments because that's the whole process, right?
[1367.00 --> 1370.28]  You're doing lots of experimentation until you reach your goal.
[1370.28 --> 1377.74]  And so, with experiments, you're basically running pieces of code that are slightly different from each other.
[1378.04 --> 1382.88]  And that's a different thing than running the same piece of code, right, on lots of machines.
[1383.66 --> 1387.24]  And so, basically, this is a very different problem.
[1387.40 --> 1395.54]  How do I, as a data science team, manage my workloads on, you know, clusters of machines?
[1395.54 --> 1407.86]  How do I handle lots of experiments that I need to run from, you know, one or more data scientists or a team of data scientists and do that effectively when we're talking about pieces of code that continually change?
[1408.36 --> 1412.26]  How do I actually take the environment that I built?
[1412.52 --> 1420.48]  Because in AI, again, the piece of code that you're running actually is much more complex on one dimension than a regular software.
[1420.48 --> 1428.96]  Because, really, it's an amalgamation of the model, right, the neural network, for example, right, the code that wraps it with the data, right?
[1429.04 --> 1440.80]  How do I actually take that environment that I built, my research, you know, XReacher, right, and the model that she built and then run it on a remote machine that has a different environment?
[1441.20 --> 1442.80]  And so, all of these are different challenges.
[1443.16 --> 1445.82]  And this is the challenges that we attempt to solve.
[1446.36 --> 1447.90]  And this is what we call ML Ops.
[1448.38 --> 1450.20]  Yeah, that's a really good summary.
[1450.20 --> 1478.72]  I like how you set that up in terms of the comparison to DevOps, because it is kind of maybe a shock for people starting to get into this field where, like you say, from day one, in order to actually make progress on their things, they might have to know about, oh, spinning up this GPU instance in the cloud or, you know, CUDA libraries and running things in a repeatable way.
[1478.72 --> 1487.46]  It seems like a really high barrier for people to overcome, you know, from day one to get things working and also do it in a repeatable way.
[1488.62 --> 1492.58]  Yeah, I also wonder on the, like you're talking about experiments and that sort of thing.
[1492.58 --> 1503.34]  I know one thing that is definitely true of myself and, you know, my wife could confirm is that I'm not very good at remembering what I've done or what needs to be done, right?
[1503.34 --> 1512.38]  But in terms of the experiment tracking side of things, of course, there's like the running of things, which is definitely important.
[1512.50 --> 1514.86]  I think that's what maybe you focus on mostly.
[1514.86 --> 1521.26]  But there's also kind of this weird documentation almost piece of the puzzle.
[1521.42 --> 1532.70]  It's not quite documentation because it's like a very specific type of documentation that's really documenting, like what have I done and what haven't I done and how successful was that?
[1532.78 --> 1540.14]  And it's not really like you want to have a research paper necessarily, especially if you're developing these things as a product or maybe even a trade secret.
[1540.14 --> 1546.20]  But especially if you're on a team, want to have that common understanding of what has been done and hasn't been done.
[1546.46 --> 1552.28]  How soon do you see teams encountering that issue when they start working on this problem?
[1552.28 --> 1561.90]  And what are those kind of essential elements of, I guess, more of the documentation or tracking side of things that need to be in stone somewhere over time?
[1562.30 --> 1562.40]  Yeah.
[1562.98 --> 1569.16]  Well, you know, as you were saying about documenting and how it's not exactly documented, if you come up with a term,
[1569.16 --> 1570.56]  please let me know.
[1573.36 --> 1575.06]  Naming things is the hardest thing.
[1575.24 --> 1575.58]  Exactly.
[1575.90 --> 1576.94]  Doc Ops.
[1578.14 --> 1578.40]  Yeah.
[1579.60 --> 1580.36]  Doc Ops.
[1580.98 --> 1582.20]  That's probably already taken.
[1582.30 --> 1583.14]  That has to be taken.
[1584.82 --> 1586.34]  That's a real issue.
[1586.74 --> 1588.68]  So, you know, that's a real struggle to name it.
[1589.16 --> 1593.08]  So I'll prefix and say, actually, you're saying, you know, we were focusing more on the ML Ops.
[1593.16 --> 1598.64]  Actually, you know, one area where we're pretty unique is that we have a very highly integrated solution
[1598.64 --> 1601.32]  where we think that you can't focus on just one thing.
[1601.44 --> 1606.12]  If you don't have a highly integrated platform that actually takes care of both of the experiment management,
[1606.30 --> 1610.60]  the data management, the versioning, and the ML Ops, you don't have the best scalable solution.
[1610.70 --> 1612.64]  But we can talk about that later if you'd like.
[1613.20 --> 1619.54]  The experiment management part of it, the documentation part of it, when do people realize that they need it?
[1619.54 --> 1627.08]  The answer is actually when someone in the team that usually has some sort of engineering background says, stop, this is crazy.
[1628.10 --> 1628.76]  You know?
[1629.06 --> 1629.46]  Yeah.
[1629.64 --> 1630.86]  That's exactly the point.
[1631.64 --> 1634.68]  I remember Doug, if you're out there, his name was Doug.
[1635.02 --> 1637.38]  He's a great engineer, one of the startups I work with.
[1637.54 --> 1638.66]  He was my wake-up call.
[1638.66 --> 1638.90]  Yeah.
[1641.14 --> 1644.88]  And so, you know, I mean, it could happen with a team of one.
[1645.66 --> 1646.38]  And it can happen.
[1646.48 --> 1647.40]  We've seen it happen.
[1647.80 --> 1653.56]  Well, we've actually seen teams of tens of data scientists that didn't have that, right?
[1653.56 --> 1662.54]  And it really depends if you have that person who realizes that and has the influence and or power to actually say, you know, we need to change this.
[1663.00 --> 1663.10]  Yeah.
[1663.42 --> 1663.66]  Yeah.
[1663.66 --> 1675.72]  And I guess this is something that we've kind of talked about in passing, but that's this interaction between AI developers or data scientists and the rest of an engineering organization.
[1676.04 --> 1682.52]  So maybe a follow-up question to Chris's question about differentiating MLOps and DevOps.
[1683.22 --> 1688.52]  What is the kind of integration point from your perspective between the two worlds?
[1688.52 --> 1701.64]  Because if things eventually end up in a product, right, like I'm importing a model into some API handler in some code that is production product code, there has to be an integration point somewhere.
[1701.92 --> 1705.42]  Where does that exist and what challenges are at that integration point?
[1706.08 --> 1706.76]  That's a great question.
[1706.84 --> 1711.46]  Actually, the integration is something that happens continuously if you're actually running things well.
[1711.90 --> 1713.90]  So it's exactly as I said, right?
[1713.90 --> 1730.20]  I mean, ultimately, what you want to do is you want to take this model, right, that you built to predict something or to solve something and then integrate that into, call it a wrapper or, you know, some larger piece of code that actually carries out the ultimate task of that product.
[1730.58 --> 1742.56]  The thing is, oftentimes, you know, you could test your model a lot, kind of like in a very environment that's kind of clean, but ultimately you're going to want to test it in the field, then you're going to have to have that wrapper.
[1742.56 --> 1766.76]  The other point also is that once you want to get into automation, right, and even if you're still within the data science part, if you want to get into automation and create lots and lots of experiment and you want to maybe you're actually fielding in continuously new data that's coming in, right, let's say you're, you know, you're building an autonomous vehicle and you're getting constantly new videos from your cars driving around.
[1766.76 --> 1773.50]  And you want to actually improve your models based on that, then that also creates an integration point.
[1773.60 --> 1775.98]  So the integration points is on those two levels.
[1776.08 --> 1781.16]  One is, you know, when you have to hand over the code so that it gets wrapped.
[1781.16 --> 1790.58]  And two, when you actually want to integrate those experiments within a larger pipeline that helps improve them.
[1790.96 --> 1800.88]  And there's another point that we actually try to facilitate with our product, which is how can I lower the barrier to entry?
[1801.08 --> 1801.56]  And I'll explain.
[1801.66 --> 1808.04]  Let's say you're a company and you're doing, you're building a solution to, I don't know, let's take computer vision.
[1808.04 --> 1808.48]  It's easy.
[1808.60 --> 1811.98]  I mean, let's say you're rebuilding, you know, something to identify cats, right?
[1812.02 --> 1813.74]  Let's take the ultimate example, right?
[1813.82 --> 1818.88]  But you also need to identify dogs because you're building a pet detector, whatever.
[1819.40 --> 1821.06]  You're speaking right to Chris's heart.
[1821.30 --> 1822.14]  Chris is a animal lover.
[1823.00 --> 1825.10]  I was keeping my mouth shut this time.
[1826.34 --> 1826.80]  Yes, I am.
[1826.96 --> 1828.70]  Daniel can't normally shut me up on that.
[1829.02 --> 1830.26]  So go for it.
[1830.28 --> 1830.58]  Let's hear.
[1830.84 --> 1831.10]  All right.
[1831.16 --> 1836.94]  You know, as data scientists, you understand that if you've built a model and I'm talking about the code now right now, right?
[1836.94 --> 1840.16]  That facilitates object detection for cats.
[1840.72 --> 1852.14]  Well, if you now want to do the same thing for dogs, what you need to do, right, is you need to take that code that you built for the experiment and probably the same neural network.
[1852.38 --> 1860.10]  That is the one that you chose for, you know, identifying objects in whatever scenario and now marry it with a different data set.
[1860.32 --> 1861.00]  That's it.
[1861.00 --> 1864.40]  Why would you necessarily need a data scientist for that?
[1865.42 --> 1866.92]  Why couldn't an engineer do that?
[1868.04 --> 1871.88]  And that's behind a lot of the stuff that we're doing also, right?
[1871.92 --> 1885.04]  The ability to actually have the data scientists work on the core pet detector model and then have engineers facilitate optimizing that for the different objects.
[1885.04 --> 1885.48]  Yeah.
[1885.48 --> 1885.88]  Yeah.
[1886.60 --> 1893.80]  And I think that also actually that example itself illustrates another kind of unique feature of this.
[1894.00 --> 1903.10]  I think you're right in that those later stages could be kind of the popular word, I guess, is democratized to other people within the organization.
[1903.10 --> 1903.46]  Right.
[1903.52 --> 1924.26]  But also, it's still not quite the same as like a normal DevOps in that, like if you're running with a different data set, somehow you need to have a kind of unique tracking that's going on with like what data set was used to train this particular artifact or serialized model, you know, at what time?
[1924.26 --> 1927.04]  Because the code might actually be exactly the same.
[1927.04 --> 1927.54]  Right.
[1927.60 --> 1929.66]  The difference might be in the data.
[1929.92 --> 1930.28]  Exactly.
[1930.62 --> 1931.04]  Exactly.
[1931.04 --> 1931.56]  Yeah.
[1931.56 --> 1931.62]  Yeah.
[1931.74 --> 1942.76]  So I see so many people like develop really sophisticated kind of naming for their files and such, which you'd probably need your own documentation to document that.
[1943.46 --> 1944.90]  What about the data side?
[1944.96 --> 1949.06]  We mostly kind of talked about process and the operations infrastructure.
[1949.28 --> 1951.08]  What about the data side of things?
[1951.78 --> 1955.26]  So the data is the holy grail at the end of the day.
[1955.26 --> 1961.20]  And I think that, you know, obviously experienced and senior data scientists get this, right?
[1961.22 --> 1962.06]  It's all about the data.
[1962.62 --> 1965.48]  Novices are focused more on the models.
[1965.48 --> 1982.44]  But at the end of the day, you know, the difference between a product that meets the threshold of, you know, whatever KPIs you want it to hit and something that doesn't is about your ability to, you know, train it on the right data set.
[1982.44 --> 1983.04]  Right.
[1983.12 --> 1989.10]  And be on top of your data and be able to feed the exact, what we call data view to train that model.
[1989.76 --> 1992.56]  And so iterating on the data, right?
[1992.62 --> 1995.48]  Identifying the skews within the data and handling those, right?
[1995.48 --> 2001.78]  Identifying the holes where you need to add more data or, you know, build synthetic data, right?
[2001.78 --> 2003.18]  Or augmentations around that.
[2003.46 --> 2005.90]  That is the key piece.
[2005.90 --> 2008.92]  And, you know, we talked about this, right?
[2008.96 --> 2009.96]  It's an experiment process.
[2010.14 --> 2013.88]  And so being able to actually version that and track that.
[2014.34 --> 2023.00]  Because as an experiment process, you know, you're going one track and then you realize, you know, what, actually you want to go back to the model I built two months ago and actually take a different direction.
[2023.42 --> 2024.78]  You have to be able to version that.
[2024.88 --> 2028.38]  Or not just the model, you want to be able to version the data set.
[2028.38 --> 2037.42]  I mean, if you have enough experience as a data scientist, you know that you're always going to find data sets that work better for whatever reason.
[2037.52 --> 2038.44]  And you don't even know why.
[2039.20 --> 2039.32]  Right.
[2039.34 --> 2040.08]  You don't know why.
[2040.50 --> 2041.44]  But whatever it did.
[2041.52 --> 2048.50]  I mean, you know, there are so many examples of data sets that are quote unquote wrong because, you know, the metadata on them isn't necessarily correct.
[2048.62 --> 2052.04]  But somehow they produce better results than, you know, data set that's better.
[2052.40 --> 2052.60]  Right.
[2052.64 --> 2055.28]  And so you have to version your data.
[2055.28 --> 2066.90]  You have to version the data, not just the files, but the metadata around that so that you can effectively go through that process and make sure that you're building the best solution that you can.
[2085.28 --> 2089.66]  If you like this show and you aren't listening to the changelog, hey, let's fix that bug.
[2090.10 --> 2093.88]  The changelog is our flagship show and we've been doing it for over a decade.
[2094.56 --> 2098.96]  Adam and I seek out and interview the people who are pushing the world forward with software.
[2098.96 --> 2105.74]  We dive deep into the hacks, the innovations and the leadership required to do what these amazing people do.
[2106.06 --> 2117.60]  One recent example is our conversation with Anders Damsgaard, a climate scientist from Denmark who gave us a peek inside his work and how he scratched a common itch he has when gathering academic research from around the web.
[2118.08 --> 2119.72]  Here's a dorky moment from that episode.
[2120.58 --> 2123.52]  Are you trying to be right or are you trying to solve the world's problems?
[2123.76 --> 2124.14]  Exactly.
[2124.52 --> 2127.10]  If you're a scientist trying to be right, well, then you're right.
[2127.18 --> 2128.56]  It may not actually be the right.
[2128.56 --> 2129.76]  Yeah, exactly.
[2130.10 --> 2133.08]  There's another saying, all models are wrong, but some are useful.
[2133.88 --> 2135.18]  I like that one.
[2135.68 --> 2138.24]  There's another saying, all models are wrong, except for mine.
[2138.38 --> 2138.76]  Mine's correct.
[2140.52 --> 2141.30]  Good one, Jared.
[2142.26 --> 2144.14]  We had a lot of fun with Anders.
[2144.32 --> 2145.34]  He's a fascinating guy.
[2146.02 --> 2150.60]  Continue listening at changelog.com slash podcast slash 378.
[2150.86 --> 2157.60]  Or search for the changelog on your favorite podcast app and find the episode called Open Source Meets Climate Science.
[2158.56 --> 2185.24]  So before we got to the break, you were talking about versioning the data and wanted to kind of let you finish that thought.
[2185.24 --> 2196.68]  And then I actually wanted to also explore kind of how Allegro is moving ML Ops in a practical way, like what you're actually focusing on and how you're implementing ML Ops.
[2196.86 --> 2200.30]  But if you'd finish your thought on data versioning, we'd love to hear it.
[2200.30 --> 2200.94]  Sure.
[2201.30 --> 2206.86]  You know, with respect to data versioning, at the end of the day, you know, we think that that's the, as I mentioned, the holy grail.
[2206.86 --> 2217.34]  So being able to have a set of tools that enables you to effectively manage your data sets and their versions.
[2218.00 --> 2229.10]  And effectively also be able to obfuscate the connection between the code and the data so that we can facilitate, for example, the ability to move from a cat detector to a dog detector.
[2229.10 --> 2230.76]  Because now you're using a different data set.
[2231.24 --> 2240.30]  And again, as a data scientist, you all know that taking one data set with a code and actually switching it to a different data set is not as trivial as one would like it to be.
[2240.30 --> 2245.90]  And so those are some of the goals that we set out about to do with Allegro.
[2246.26 --> 2254.04]  Trains and really the ability to actually switch between the data sets and the code and the models as easy as plug and play.
[2254.44 --> 2255.04]  Yeah.
[2255.22 --> 2261.98]  So what is the kind of, I guess, range of things that Allegro focuses on in its actual offerings?
[2261.98 --> 2271.22]  So I know that there's the Trains project, which was mentioned in that tweet that got me interested, that joined the PyTorch ecosystem project.
[2271.76 --> 2276.74]  So how does that fit into the wider scheme of what Allegro is offering?
[2276.98 --> 2279.68]  And how does a data scientist interact with it, I guess?
[2280.38 --> 2280.50]  Sure.
[2280.50 --> 2299.06]  What we provide is we provide a platform or a tool chain or a set of tools that basically takes care of the experiment process, the MLOps part of it, the ability to actually scale and actually run things effectively, and the data.
[2299.80 --> 2309.62]  And the full platform, which isn't completely available as open source, basically has all these key pieces together, highly, highly integrated.
[2309.62 --> 2327.14]  What we've open sourced or what's available as an open source project is the experiment management part of things, which is all about the documentation we talked about, the ability to document things, version your models, your experiments, your hyperparameters, everything around that, reproduce, compare, etc.
[2327.14 --> 2347.00]  And everything that has to do with the basic MLOps, the ability to actually manage a cluster, whether it's on-prem or on cloud or combination by a team of data scientists and really self-help themselves with orchestration and scheduling, etc.
[2347.00 --> 2376.98]  And automation on top of that.
[2376.98 --> 2386.72]  And obviously, you know, the standard enterprise relevant features like, you know, user management, permissions, managed services, all that stuff.
[2386.72 --> 2395.46]  So I'm curious, as you're kind of describing this, and I appreciated you kind of talking a little bit toward what was open source versus what was the enterprise offering.
[2395.46 --> 2408.14]  As you look at different potential customers out there, and there is a variety of ways they may implement how they are allocating resources for their own MLOps prior to you coming into the picture with them.
[2408.48 --> 2411.20]  You know, some people are strictly cloud-based.
[2411.34 --> 2414.86]  They may be doing, you know, Google or AWS or Azure.
[2414.86 --> 2426.66]  Some people are, or organizations is more specific, maybe buying like a bunch of DGXs from NVIDIA and have a cluster set up locally or some hybrid form.
[2427.20 --> 2431.06]  Which of these scenarios does Allegro fit into?
[2431.32 --> 2434.40]  And if multiple, how does it change how you would implement Allegro?
[2434.40 --> 2441.88]  Actually, you know, we fit into every one of those scenarios, any hybrid scenario that you can think of.
[2442.38 --> 2448.84]  And actually, the more complex your environment is, the more Allegro trains shines.
[2449.52 --> 2450.14]  And I'll explain.
[2450.14 --> 2458.36]  Basically, the way that Allegro trains is set up is you have a server backend that basically manages the processes and records and logs everything.
[2458.36 --> 2472.74]  And then sets up the instructions for, you know, the clients that are basically what the data scientists connect with, as well as the agents that run on the machines that do the actual training.
[2472.74 --> 2478.28]  The system is built that you can set it up on any type of machine for training.
[2478.52 --> 2480.10]  It could be, you know, DGX.
[2480.18 --> 2482.10]  It could be any type of GPU by NVIDIA.
[2482.20 --> 2483.26]  It could actually be CPU.
[2483.98 --> 2485.06]  It doesn't really matter.
[2485.56 --> 2490.50]  It can sit on the cloud, on-prem, any combination, on any cloud that you'd like.
[2491.08 --> 2491.86]  And it all works.
[2491.86 --> 2503.50]  In fact, a significant portion of our customers have a hybrid solution where they have on-prem systems and then they actually burst into the cloud, right?
[2503.52 --> 2507.24]  When they have specific times where they need actually more processing power.
[2507.70 --> 2509.18]  And that becomes really effective for them.
[2509.42 --> 2512.88]  We have other customers that are completely on the cloud, you know, and everything in between.
[2512.88 --> 2528.34]  Why Allegro Trains actually shines the more that you have a more complex environment is because, so on the first level is that the interface to manage these clusters is really, really simple.
[2528.46 --> 2529.44]  You can actually try it out.
[2530.02 --> 2531.64]  We have a demo server up on the web.
[2532.02 --> 2537.42]  The data scientists actually manage queues where they can set up, you know, the machines.
[2537.42 --> 2541.28]  I want one, you know, GPU or I need a cluster of eight GPUs or whatever.
[2541.28 --> 2545.42]  And it's completely invisible to them where those machines sit.
[2547.22 --> 2555.34]  With the enterprise version, we go even further and we provide three layers of software caching and what we call zero data move.
[2555.64 --> 2566.64]  So, if you have a complex system or you have data in multiple locations, you know, we'll make sure the data goes to the right machine to train that's, you know, close by to it.
[2566.64 --> 2570.32]  We'll make sure that there's local caching to it, that it doesn't have to go back again and again.
[2570.32 --> 2574.78]  And so, the data moves as little as it can.
[2575.18 --> 2576.68]  And we can actually, we go even further.
[2576.82 --> 2578.94]  You can actually do federated learning on our platform.
[2579.44 --> 2586.20]  And so, you can actually have data being trained in multiple locations geographically around the world and then combined into a single model.
[2587.02 --> 2587.50]  Really interesting.
[2587.50 --> 2600.12]  And I think you're kind of getting or hinted at some of these things, but just for my own understanding, it sounds like there's the Allegra trains server, which kind of aggregates all of this information.
[2600.12 --> 2606.58]  Does that kind of experiment management is kind of, I guess, maybe the central brain is a way to think of it.
[2606.58 --> 2606.94]  Yep.
[2606.94 --> 2619.46]  In my understanding, like if I'm, let's say, running, let's say I just have a machine, my own machine, and I have some code on it and I want that to be tracked by the Allegra train server.
[2619.46 --> 2630.02]  I think based on what I was reading, you just kind of decorate that code with a certain snippet that connects to the centralized trains server.
[2630.24 --> 2632.62]  Is that kind of the workflow for that scenario?
[2632.76 --> 2633.12]  Exactly.
[2633.66 --> 2633.92]  Okay.
[2633.92 --> 2636.00]  We try to make it as simple as possible.
[2636.18 --> 2637.46]  We dub it automagical.
[2638.12 --> 2639.32]  There's a snippet of code.
[2639.44 --> 2640.78]  It's basically two lines of code.
[2641.38 --> 2644.60]  You put just once in your code and the header basically, and that's it.
[2644.74 --> 2645.14]  You're done.
[2645.36 --> 2646.64]  Everything is in track for you.
[2647.34 --> 2653.84]  And, you know, that you could potentially have the server, the training, and your client be on the same physical machine if you'd like.
[2654.36 --> 2655.08]  It doesn't matter.
[2655.64 --> 2655.86]  Yeah.
[2655.86 --> 2674.58]  Actually, I'll reveal some of my cards now because a little while ago, so I have a friend here close by geographically in Indiana, and we kind of have regular calls to just talk about AI things because, you know, we both work in companies where there's not that many AI type people.
[2674.80 --> 2678.36]  And so we like to share things that we're learning and all that stuff.
[2678.44 --> 2679.46]  His name's Will.
[2679.60 --> 2681.02]  Shout out to Will out there if you're listening.
[2681.02 --> 2687.28]  But I asked him one of the first kind of times we were talking about his workflow and all those things.
[2687.58 --> 2692.96]  We got into this topic of ML Ops and all that, and he's like, oh, I use this Allegro Trains thing.
[2693.10 --> 2693.86]  It's amazing.
[2694.38 --> 2702.06]  And I was just talking to him earlier today, actually, and I was like, hey, I'm going to talk to the Allegro Train, the Allegro AI people later today.
[2702.44 --> 2703.48]  What do you want me to say?
[2703.48 --> 2707.98]  And one of the things he said was it's just for him, it's super easy.
[2707.98 --> 2717.44]  Like you were saying, pretty low barrier to, you know, add this snippet to your code and kind of things happen automagically like you were talking about.
[2717.90 --> 2722.06]  And the other thing he definitely wanted to mention was that the team is super responsive.
[2722.06 --> 2727.86]  And he mentioned raising various things on GitHub and all of that, and the team is very responsive.
[2728.10 --> 2729.04]  So great job.
[2729.22 --> 2732.06]  You've got a very happy user in Will here in Indiana.
[2732.58 --> 2733.70]  Well, thank you, Will.
[2735.78 --> 2736.22]  Awesome.
[2736.22 --> 2739.46]  But yeah, he was kind of telling me about how some of that works.
[2739.64 --> 2741.82]  And then there's also, you mentioned the agents.
[2741.96 --> 2750.06]  The agents, those have to do with kind of the more automated runs that happen across a set of shared resources, or where does that fit in?
[2750.58 --> 2758.14]  So the agents are, if you basically want to run your code on a remote machine, you basically set up an agent on that machine, right?
[2758.16 --> 2760.88]  Whether it's a DGX or a GPU or whatever you have it.
[2760.88 --> 2768.30]  And that agent is tasked with basically, that agent is then associated with certain cues that you create.
[2768.62 --> 2770.86]  It could be associated with either one or more cues.
[2771.12 --> 2777.40]  So it's a little piece of code that sits on any machine that is potentially a target for running your experiments on.
[2777.40 --> 2791.96]  So one of the things I'm curious about, and I meant to ask you this a little bit a while ago when you were touching on it, was some of the motivation that you had for going with an open source business model that builds an enterprise business on top of that.
[2791.96 --> 2796.52]  And did you always know that that was going to be the approach you guys were going to take?
[2796.64 --> 2798.18]  Or did you consider any others?
[2798.36 --> 2800.46]  And how has that model worked out for you?
[2800.98 --> 2803.34]  That's a very revealing question for us.
[2803.60 --> 2813.04]  When we started out, we probably erred on where the market, you know, so I guess one of the things that you do in a startup is, right, you try to time the market.
[2813.04 --> 2821.16]  Which I think I saw, you know, several articles talking about, you know, timing being the number one critical aspect of, you know, startup success.
[2821.42 --> 2824.58]  And actually one of the hardest to hit, right?
[2824.70 --> 2827.02]  And sometimes even VCs call it luck.
[2827.52 --> 2834.62]  But, you know, we were trying to time the market because what we had built initially was around the Holy Grail about the data.
[2834.62 --> 2841.80]  And we basically built a system with the thought in mind of, well, you know, companies are now doing development, but they're going to get to scale.
[2842.12 --> 2845.42]  And they're going to have to be able to manage huge data sets that constantly change.
[2845.48 --> 2846.16]  You have to version that.
[2846.22 --> 2847.16]  You have lots of experiments.
[2847.30 --> 2849.64]  You've got these things running on multiple clusters.
[2849.72 --> 2851.04]  How do you handle all of that?
[2851.42 --> 2855.28]  And so we actually set out to build this really big, robust system.
[2855.28 --> 2863.94]  And then we found out that very few companies were at the stage where they needed this or realized its value.
[2864.62 --> 2868.42]  And so we got back and started thinking, you know, where is the industry now?
[2868.46 --> 2870.34]  And how can we help the industry progress?
[2870.70 --> 2877.06]  And we figured that the right thing to do is to meet the industry where it is, which was, you know, before that scale.
[2877.06 --> 2883.80]  And come up and say, you know, all right, so what are the low-hanging fruit of things that can bring immediate value to data scientists out there?
[2883.80 --> 2885.70]  And that was the first thing was the experiment management.
[2886.10 --> 2891.52]  And then immediately after that, the ML Ops, or at least the ML Ops in its lighter form, right?
[2891.90 --> 2898.90]  Not a, don't think of a huge conglomerate running, you know, hundreds and thousands of experiments, but, you know, even small teams.
[2899.22 --> 2913.02]  And we thought that the best way to do that, to really contribute to community, help spur that along, make that, you know, something that a lot of people can do stuff better in the way we think it would be better and helpful.
[2913.02 --> 2920.02]  And ultimately, obviously, you know, we're a company, we're about making money, but being able to do that was something that we thought was the right thing to do.
[2920.06 --> 2922.18]  That will, you know, be a win-win for everyone.
[2922.36 --> 2923.62]  It'll be a win for the community.
[2923.94 --> 2934.16]  And ultimately, it'll be a win for us because, you know, when, you know, the larger companies that do have money to pay and do feel like they need to get, you know, more, they're going to come back to us.
[2934.16 --> 2935.26]  Yeah, that's great.
[2935.36 --> 2952.16]  And I think as evidenced by, I think, users and also attention and kind of joining in with the PyTorch ecosystem, like in that blog post and other things, I think that that really allows people to, you know, solve a pain point that they really have really, really quickly.
[2952.48 --> 2960.28]  And hopefully it does eventually spur them on to, especially if they're part of larger companies or teams, you know, integrate more with your enterprise systems.
[2960.28 --> 2962.42]  But it's been amazing to talk today.
[2962.80 --> 2966.04]  The topic's very close to what I'm super passionate about.
[2966.14 --> 2967.08]  I think Chris as well.
[2967.18 --> 2973.26]  And part of the reason why we do this podcast is to talk about those practicalities of how people do their AI development.
[2973.54 --> 2975.36]  So really appreciate you joining.
[2975.68 --> 2985.10]  We'll link the demo server and the links to Allegro Trains on GitHub and also your main website, which talks about all of your offerings.
[2985.28 --> 2987.38]  We'll put that in the show notes for sure.
[2987.38 --> 2997.06]  And I encourage people to go there and check out those things and let us know in Slack or on LinkedIn or other places what you think and how you like what they're doing.
[2997.26 --> 2998.78]  But really appreciate you joining, Nir.
[2998.88 --> 3000.52]  It's been a great conversation.
[3001.24 --> 3001.90]  Thank you so much.
[3001.96 --> 3003.04]  I mean, it was a pleasure.
[3003.32 --> 3004.00]  It was fun.
[3004.42 --> 3006.02]  And really, thank you so much for having me.
[3006.02 --> 3012.22]  Have you joined the free Changelog community yet?
[3012.66 --> 3014.00]  I'm not sure what you're waiting for.
[3014.64 --> 3025.78]  You get Changelog news, email notifications of new podcast episodes, access to our community Slack and Practical AI channel where fun and interesting AI discussions take place all the time.
[3025.92 --> 3027.68]  All for the price of a free hot dog.
[3028.04 --> 3030.46]  Check us out at changelog.com slash community.
[3030.62 --> 3031.32]  We'd love to have you.
[3031.88 --> 3034.88]  Practical AI is hosted by Daniel Whitenack and Chris Benson.
[3034.88 --> 3040.18]  It's produced by me, Jared Santo, and our music is provided by the mysterious Breakmaster Cylinder.
[3040.52 --> 3045.60]  We're brought to you by some amazing companies who get it thanks to Fastly, Linode, and Rollbar.
[3046.58 --> 3047.56]  That's all for now.
[3047.90 --> 3049.12]  We'll talk to you again next week.
[3049.12 --> 3079.10]  We'll talk to you again next week.
