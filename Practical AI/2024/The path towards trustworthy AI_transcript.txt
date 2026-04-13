[0.00 --> 7.28]  Welcome to Practical AI.
[7.70 --> 15.00]  If you work in artificial intelligence, aspire to, or are curious how AI-related tech is
[15.00 --> 17.72]  changing the world, this is the show for you.
[18.06 --> 20.66]  Thank you to our partners at Fly.io.
[21.14 --> 26.86]  Fly transforms containers into micro VMs that run on their hardware in 30 plus regions on
[26.86 --> 30.72]  six continents, so you can launch your app near your users.
[31.28 --> 33.24]  Learn more at Fly.io.
[35.60 --> 41.04]  Okay, friends, I'm here with a new friend of ours over at Timescale Avthar Suwathan.
[41.46 --> 44.80]  So Avthar, help me understand what exactly is Timescale?
[45.02 --> 46.58]  So Timescale is a Postgres company.
[47.06 --> 52.34]  We build tools in the cloud and in the open source ecosystem that allow developers to do
[52.34 --> 53.22]  more with Postgres.
[53.22 --> 57.74]  So using it for things like time series, analytics, and more recently, AI applications
[57.74 --> 59.40]  like RAG and Search and Agents.
[59.66 --> 65.62]  Okay, if our listeners were trying to get started with Postgres, Timescale, AI application development,
[66.16 --> 66.80]  what would you tell them?
[67.14 --> 67.80]  What's a good roadmap?
[68.12 --> 73.12]  If you're a developer out there, you're either getting tasked with building an AI application,
[73.32 --> 76.84]  or you're interested and you're seeing all the innovation going on in the space and want
[76.84 --> 77.78]  to get involved yourself.
[77.78 --> 84.28]  And the good news is that any developer today can become an AI engineer using tools that
[84.28 --> 85.36]  they already know and love.
[85.62 --> 90.30]  And so the work that we've been doing at Timescale with the PGAI project is allowing developers
[90.30 --> 95.52]  to build AI applications with the tools and with the database that they already know, and
[95.52 --> 96.40]  that being Postgres.
[96.70 --> 100.82]  What this means is that you can actually level up your career, you can build new interesting
[100.82 --> 105.70]  projects, you can add more skills without learning a whole new set of technologies.
[105.70 --> 111.58]  And the best part is it's all open source, both PGAI and PG Vector Scale are open source.
[111.72 --> 116.12]  You can go and spin it up on your local machine via Docker, follow one of the tutorials on the
[116.12 --> 121.84]  Timescale blog, build these cutting edge applications like RAG and Search without having to learn 10
[121.84 --> 126.56]  different new technologies and just using Postgres in the SQL query language that you will probably
[126.56 --> 128.02]  already know and are familiar with.
[128.34 --> 129.40]  So yeah, that's it.
[129.46 --> 130.22]  Get started today.
[130.44 --> 131.96]  It's a PGAI project.
[131.96 --> 137.38]  And just go to any of the Timescale GitHub repos, either the PGAI one or the PG Vector Scale
[137.38 --> 143.00]  one and follow one of the tutorials to get started with becoming an AI engineer just using Postgres.
[143.48 --> 150.32]  Okay, just use Postgres and just use Postgres to get started with AI development, build RAG,
[150.54 --> 152.22]  search AI agents.
[152.22 --> 153.60]  And it's all open source.
[153.60 --> 163.04]  Go to timescale.com slash AI, play with PGAI, play with PG Vector Scale, all locally on your desktop.
[163.20 --> 164.08]  It's open source.
[164.48 --> 167.76]  Once again, timescale.com slash AI.
[182.22 --> 188.18]  Welcome to another episode of the Practical AI Podcast.
[188.74 --> 190.22]  I am Chris Benson.
[190.50 --> 195.60]  I am a Principal AI Research Engineer at Lockheed Martin.
[196.26 --> 202.36]  And unfortunately, my co-host Daniel is not with us today, but it is my pleasure to introduce
[202.36 --> 208.92]  Elham Tabasi, who is the Chief AI Advisor at NIST, which is the National Institute of Standards
[208.92 --> 209.72]  and Technology.
[210.28 --> 211.32]  Welcome to the show, Elham.
[211.32 --> 212.50]  Thanks for having me.
[212.90 --> 220.96]  You guys are doing so much in this area in terms of AI and kind of setting the stage.
[221.44 --> 225.86]  And I was wondering, for those of us in the audience who may not be familiar with NIST,
[225.92 --> 231.80]  if you could kind of start out with just telling us a little bit about NIST, what you do both
[231.80 --> 238.92]  in AI and maybe outside to give a little context and give us a little intro into what NIST is
[238.92 --> 241.38]  doing in AI and your role in that.
[241.64 --> 242.36]  Yeah, happy to.
[243.30 --> 249.10]  NIST, our National Institute of Standards and Technology, is a non-regulatory agency under
[249.10 --> 250.34]  the Department of Commerce.
[251.26 --> 255.78]  NIST was established in 1902, and our mission has not changed since then.
[256.42 --> 260.86]  NIST's mission is to advance U.S. innovation and industrial competitiveness.
[260.86 --> 266.62]  At NIST, we have a very broad portfolio of research, from building the most accurate atomic clock
[266.62 --> 270.32]  to modeling the behavior of the wildfire.
[270.32 --> 275.46]  But most importantly, we have a long tradition of cultivating trust in technology.
[275.90 --> 280.42]  We do that by advancing measurement science and standards, measurement science and standards
[280.42 --> 286.56]  that makes technology more reliable, secure, private, fair, in other words, more trustworthy.
[286.92 --> 289.50]  And that's exactly what we are doing in the space of AI.
[289.50 --> 295.86]  As I mentioned, NIST was established in 1901 to fix the standards of weights and measures.
[296.68 --> 303.48]  Our predecessors created and advanced standards to measure basic things such as length, mass,
[303.84 --> 309.68]  temperature, I don't know, time, light, electricity, all those that were essential for technological
[309.68 --> 313.50]  innovation and competitiveness at the turn of the 20th century.
[313.98 --> 318.18]  We are following the same course, working with and engaging the whole community
[318.18 --> 324.76]  in figuring out proper standards and measurement science for advanced technologies of our time,
[325.16 --> 327.06]  which is artificial intelligence.
[327.56 --> 332.98]  And the way we do it is exactly, or maybe an improved version of what we have been doing
[332.98 --> 334.88]  in the past century or so.
[335.72 --> 341.92]  NIST's day-to-day work is focused on helping industry develop valid, scientifically, rigor methods.
[342.86 --> 346.92]  And one thing that I want to emphasize is that we do this through multi-stakeholder,
[346.92 --> 348.72]  open, transparent collaborations.
[349.48 --> 354.90]  While we have a lot of really good experts and expertise at NIST, we also know that we
[354.90 --> 356.16]  don't have all of the answer.
[356.72 --> 363.00]  And it's really important and vital for us to foster a consensus and buying across our
[363.00 --> 364.08]  stakeholder community.
[364.74 --> 368.14]  So what we do is that we listen and we engage.
[368.40 --> 369.60]  We get the input.
[369.82 --> 371.04]  We distill them down.
[371.04 --> 377.70]  We develop a path for measurement to build up or bolster the scientific underpinning.
[377.96 --> 385.42]  And then we develop tools, guidelines, frameworks, metrics, standards, et cetera, to support industry
[385.42 --> 386.82]  and technology.
[386.82 --> 392.36]  And we have done that for development of the AI risk management framework.
[392.62 --> 395.34]  We have done that for quantum computing, for cybersecurity.
[396.08 --> 403.22]  And we are continuing doing that for improving methods and measures for risk management and
[403.22 --> 404.60]  trustworthiness of AI systems.
[405.34 --> 407.20]  That's a great introduction.
[407.76 --> 408.68]  I'm curious.
[409.02 --> 412.34]  You talked about a couple of things about collaboration.
[412.34 --> 412.62]  collaboration.
[413.22 --> 420.84]  You seem to be right at the center, kind of, you know, sort of an interface between government
[420.84 --> 425.92]  interests in these technologies and the issues around them and industry.
[426.20 --> 431.00]  And I know you work with a number of different organizations as, you know, that NIST does in
[431.00 --> 432.84]  these different things that you've talked about.
[432.94 --> 435.78]  And you specifically called out trust.
[435.90 --> 440.48]  I was wondering if you could talk a little bit about kind of how those different collaborations
[440.48 --> 447.50]  work, how trust in technology can evolve, and how does NIST go about that process of starting
[447.50 --> 451.02]  to, you know, in AI and in other adjacent technologies?
[451.02 --> 454.98]  How does it go about that process that it's been doing for so long?
[455.34 --> 456.52]  Yeah, thank you for that question.
[456.64 --> 464.32]  As I said, it's sort of, I think, the magic sauce for us to do stakeholder engagements, to
[464.32 --> 472.54]  work with the community and ask for their inputs, leverage the knowledge of the community and build
[472.54 --> 474.90]  on the really good works that the community has done.
[475.52 --> 481.64]  And by working with all of the experts, strengthen the scientific underpinning, building the right
[481.64 --> 486.94]  technical building blocks that are needed for development of scientifically valid guidelines
[486.94 --> 487.92]  and standards.
[487.92 --> 494.90]  In terms of the engagements, particularly in the space of the AI, we all know that AI is
[494.90 --> 503.60]  a multidisciplinary and in order to understand the concept of the trust, what make AI systems
[503.60 --> 505.64]  trustworthy and what constitute trust.
[506.10 --> 510.68]  That was one of the main questions as we were developing the AI risk management framework.
[511.52 --> 517.26]  And in the engagements that we were doing with the community, early on, we recognized that
[517.26 --> 524.28]  as much as we need the input from the community that developed the technology, this is the
[524.28 --> 528.34]  community with expertise in math, statistics, computer science.
[528.94 --> 533.16]  We also need input from the community that studied the impact of the technology.
[533.52 --> 538.36]  That's economists, sociologists, psychologists, cognitive scientists.
[538.90 --> 544.18]  And we need to bring all of them together because AI systems are more than just data, compute
[544.18 --> 544.76]  and algorithm.
[544.76 --> 550.84]  They are a complex interactions of data, compute and algorithm with the human, with the environment,
[551.06 --> 555.48]  with the human that operates this, with the human that can impact, be impacted by the
[555.48 --> 555.88]  systems.
[556.48 --> 564.56]  So that engagements with a very broad set of actors in the community bring different expertise
[564.56 --> 567.42]  and backgrounds became really important.
[568.20 --> 572.16]  In the answer your questions about the trust and what constitute the trust.
[572.16 --> 576.96]  As I said, that was one of the important and central questions in development of the AI RMF.
[577.64 --> 584.00]  The AI RMF or the AI risk management framework, very briefly, it was directed by a congressional
[584.00 --> 584.48]  mandate.
[584.90 --> 590.52]  And it's a voluntary framework for managing the risk of AI in a flexible, structured and measurable
[590.52 --> 590.98]  way.
[590.98 --> 597.32]  It was, as we do with anything else, developed in close collaborations with the AI community
[597.32 --> 604.42]  and engaging diverse groups of different backgrounds, expertise and perspective to particularly get
[604.42 --> 608.60]  in and focus and hone on the concept of trust and trustworthiness.
[608.60 --> 616.40]  So on the side of the trust, what makes us AI systems trustworthy, when we started the process, there have been
[616.40 --> 623.12]  very good high-level value-based documents that talk about AI systems to be non-discriminatory,
[623.36 --> 623.66]  ethical.
[624.56 --> 629.44]  And there has been a lot of different other papers and publications.
[629.44 --> 636.40]  Basically, there were many different views about what makes an AI technology, AI systems trustworthy.
[637.04 --> 641.56]  And these views were not all aligned and on the same page.
[642.10 --> 649.72]  So it's not a property that can be defined with perfect rigor, but based on the collaborations and engagements and
[649.72 --> 655.32]  consultations that we did with the community, we understood that there are well-established key
[655.32 --> 657.04]  characteristics of trustworthy systems.
[657.04 --> 664.12]  With the help and consultation with the community in the AI RMF describes trustworthy AI systems as those
[664.12 --> 671.70]  that are valid and reliable, accountable and transparent, safe, secure and resilient, explainable and
[671.70 --> 676.80]  interpretable, privacy enhanced, and firm with harmful bias managed.
[677.04 --> 678.64]  It takes it a step further.
[678.92 --> 685.70]  And for each of these characteristics, provide a sort of a definition or bring the community on a shared
[685.70 --> 689.16]  understanding with expectation from each of these characteristics.
[689.56 --> 696.82]  And also talks about how these characteristics interrelate and trade-offs involved in decisions about
[696.82 --> 703.50]  how safe is safe, how private is private, or how to enhance interpretability or transparency,
[704.16 --> 710.82]  while at the same time, for example, preserving the privacy or ensuring the security and resilience of the AI systems.
[710.82 --> 716.76]  I'm curious, and as we go, we'll certainly dive into those topics.
[716.90 --> 725.36]  But one of the things around trust is folks like us who are in this industry and are living and working
[725.36 --> 733.56]  in and around and developing AI every day, these are kind of work topics that we're going through.
[733.56 --> 740.20]  And the guidance that NIST provides is invaluable, especially being part of that process of developing.
[740.34 --> 749.08]  And as you described, but I would, before we surge into all that, there is so many people out there that are not in this line of work as we are.
[749.08 --> 756.78]  And there are those that are, you know, curious about how they see it in the news every day and they see, you know,
[756.78 --> 760.16]  they're trying to understand what are these technologies that we're working on.
[760.28 --> 766.88]  And many people in the audience for this podcast are what we would describe as kind of AI curious as opposed to just, you know,
[766.90 --> 772.44]  we have practitioners, but we also have AI curious people who are trying to understand how it fits into them.
[772.44 --> 783.26]  And I was wondering if you'd take a moment and kind of talk about the context of trust and AI for those of us who are not in this industry in a direct way like that.
[783.38 --> 791.30]  And, you know, like how does NIST try to frame it for the larger population or is it more for practitioners?
[791.50 --> 793.08]  How do you see that for the larger world?
[793.60 --> 795.54]  Yeah, thanks for that question.
[795.70 --> 799.52]  So let me try to answer that with an example.
[799.52 --> 805.80]  We are seeing enormous advancements in the AI technology.
[806.60 --> 811.38]  Just in the past year, we saw a lot of, you know, release of the powerful models.
[811.38 --> 826.50]  We are also seeing that these technology, this AI systems are being incorporated into a lot of the functions of the society and the way we do our work.
[826.50 --> 835.44]  I want to explain the concept of the trust in an examples in use of the AI systems in health domain.
[836.12 --> 843.04]  When we go, you know, for medical imaging, I'm coming from the computer vision.
[843.48 --> 847.22]  That's where my training was and that's where they feel they feel comfortable.
[847.22 --> 856.38]  So when we do a medical imaging, imagine some sort of imaging of the brain and the question is, is it a tumor there or not?
[856.88 --> 863.14]  So an algorithm can go and be employed to help the physicians to make that decision.
[863.36 --> 872.36]  So first for that systems, for that algorithm, we wanted to be talking about the AI RMF, trustworthiness characteristics.
[872.36 --> 874.60]  We wanted to be valid and reliable.
[874.84 --> 878.82]  We want to make sure that it has some certain level of the accuracy.
[879.54 --> 888.68]  So the false positive and false negative is low because there is going to be, you know, you don't want to scare a patient saying that, yes, there was a tumor when it was, there was none.
[889.18 --> 890.04]  Or vice versa.
[890.22 --> 895.28]  A tumor is because of the errors of the systems is being, is going unrecognized.
[895.28 --> 898.72]  So we want the systems functions, functions as intended.
[898.90 --> 901.04]  We want it to be valid and results being reliable.
[901.44 --> 916.94]  On top of that, we also wanted the systems to be secure and resilient because if it's not, and if the systems get hacked, there's a lot of the personal informations that can get in the hand of non-friendly users.
[917.56 --> 921.00]  Talking about that, we want the systems to be privacy enhanced.
[921.00 --> 929.98]  We have heard, read that particularly the large language models, they have the tendency to memorize the training data.
[930.64 --> 941.30]  Even before the large language model, there were papers that showed that with certain level of expertise, the training data can be inferred from AI systems.
[941.30 --> 953.26]  So if the system has been trained on real patient data, we don't want to have any hole that can give, you know, access to those private informations.
[954.06 --> 955.72]  Explainability and interpretability.
[955.94 --> 966.04]  So if it comes and say that, yes, there is a tumor, we expect it to give some reasoning, some sort of explanations of why decide that there is a tumor.
[966.04 --> 983.08]  And then there is a lot of no one sense there too, because that explanations, if it's being given to a physician versus a technician versus the patient, it's going to be different level of the technicality and different level of the informations being shared.
[983.68 --> 986.62]  And of course, we want it to be fair.
[986.62 --> 995.08]  We don't want AI systems that has been more accurate for certain demographics versus others.
[995.32 --> 998.36]  You know, this usually happens if the training data is uneven.
[999.04 --> 1006.32]  So all of this, at the end, we want to build the confidence in this, that this technology works.
[1006.32 --> 1020.56]  And the results, predictions, recommendations that the system is providing for better decision making in this case, analyzing a scanning of the brain to see if there was any tumor was there or not.
[1020.96 --> 1026.80]  So all of these things are with the end goal of AI technology has a lot of promises.
[1027.04 --> 1028.48]  They are very powerful tools.
[1028.48 --> 1042.88]  They can transform the way we work for better, but make sure that at the same time, it uplifts all of us and we get the maximum benefits while minimizing the negative consequences of the technology.
[1058.48 --> 1061.18]  What's up, friends?
[1061.34 --> 1065.06]  I'm here in the breaks with David Hsu, founder and CEO of Retool.
[1065.50 --> 1069.98]  So David, Retool has definitely cornered the market on internal tool software development.
[1070.40 --> 1071.08]  But zoom out for me.
[1071.12 --> 1072.00]  What's the big idea?
[1072.16 --> 1073.24]  Why did you start Retool?
[1073.38 --> 1075.96]  What is the big idea with internal software?
[1076.46 --> 1080.92]  Yeah, so Retool started at this point seven years ago.
[1080.92 --> 1090.36]  And when we started Retool, the core idea was that internal software is a giant, giant category that no one really thinks about.
[1090.78 --> 1100.58]  And what's surprising to most people is that internal software represents something like 50 to 60 percent of all the code written in the world, which might sound pretty surprising.
[1100.84 --> 1108.18]  But if you think about it, most of us in Silicon Valley, we work at software companies, whether it's like an Airbnb, a Google, a Meta.
[1108.18 --> 1111.04]  These are all companies that are software companies selling software.
[1111.40 --> 1114.30]  And so most engineers in these companies are working on external facing software.
[1114.64 --> 1121.20]  But if you think about most software engineers in the world, most software engineers in the world actually don't work at these software companies.
[1121.42 --> 1122.34]  There's not that many of them.
[1122.40 --> 1123.48]  There's maybe 10, 20 of them.
[1123.68 --> 1124.36]  Big ones, at least.
[1124.70 --> 1127.46]  Most of the companies in the world are actually non-software companies.
[1127.72 --> 1132.96]  So if you think about a company like an LVMH, for example, like a Coca-Cola, for example, like a Zara.
[1133.32 --> 1134.88]  Zara is not selling any software.
[1135.10 --> 1137.04]  They actually have a lot of software engineers, actually.
[1137.04 --> 1141.90]  And all their software engineers, all they do day in and day out is basically build internal software.
[1142.10 --> 1144.04]  So that's, I think, one reason we started to retool.
[1144.32 --> 1150.78]  The second reason we started to retool is if you look at all this internal software that people are building, it is remarkably similar.
[1151.16 --> 1156.90]  So if you take a look at, you know, like a Zara, for example, versus Coca-Cola, two very different companies, obviously.
[1157.16 --> 1158.82]  One a clothing company, one a beverage company.
[1159.04 --> 1165.54]  But if you actually look at the software they're building internally to go run their operations, it is remarkably similar.
[1165.54 --> 1175.24]  It's basically forms, buttons, tables, all these sort of pretty common building blocks, basically, that come together in different ways.
[1175.50 --> 1182.34]  But then if you think about, you know, not just the UI, but also what's the logic behind a lot of this stuff, they're pretty much just hitting API endpoints, hitting databases.
[1182.34 --> 1185.14]  You care about authentication, you care about authorization.
[1185.54 --> 1188.74]  These are sort of a lot of common building blocks, if you will, to internal tools.
[1189.04 --> 1193.34]  And so for us, the insight was, wow, internal software is a ginormous category.
[1193.62 --> 1195.14]  And it's all so similar.
[1195.48 --> 1196.92]  And developers hate building it.
[1197.10 --> 1202.76]  And so could we create a sort of higher level framework, if you will, for building all this software?
[1202.90 --> 1203.96]  And that would be really cool.
[1204.42 --> 1205.12]  That would be really cool.
[1205.12 --> 1205.68]  Okay.
[1206.04 --> 1211.62]  So listeners, Retool is built for everyone, built for enterprise, built for scale, built for developers.
[1211.84 --> 1212.30]  And that's you.
[1212.56 --> 1218.32]  And if you found yourself nodding your head to what David was saying, then check out Retool at retool.com slash changelog.
[1218.48 --> 1220.48]  It's the fastest way to build internal software.
[1220.92 --> 1223.28]  Do yourself a favor, get a demo or start for free today.
[1223.56 --> 1226.76]  Again, retool.com slash changelog.
[1226.76 --> 1256.20]  So I know in the early part of 2023, NIST issued the AI risk management framework
[1256.20 --> 1257.40]  that we've been talking about.
[1257.40 --> 1263.06]  But a few months later on, or almost exactly a year ago, as we're talking in late October,
[1263.64 --> 1269.16]  the White House issued its executive order on the safe, secure, and trustworthy development
[1269.16 --> 1271.42]  and use of artificial intelligence.
[1271.42 --> 1280.78]  So I was wanting to understand that how the issue of the executive order might have either
[1280.78 --> 1286.40]  altered or accelerated or changed any of the work that NIST was already doing.
[1286.50 --> 1291.42]  You guys were already very much involved in artificial intelligence through the framework
[1291.42 --> 1292.68]  and other activities.
[1293.14 --> 1297.22]  Could you describe the impact of the executive order on the work you were doing?
[1297.62 --> 1298.06]  Absolutely.
[1298.48 --> 1304.54]  In answering your question, if I can just go back from the release of the AI RMF in January
[1304.54 --> 1310.80]  2023 to release of the executive order, end of October, October 30th, 2023.
[1311.76 --> 1315.10]  So the AI RMF was released January 2023.
[1316.04 --> 1319.88]  In March of that year, we released the AI Resource Center.
[1319.88 --> 1325.18]  This is a one-stop shop of knowledge, data tools for AI risk management.
[1325.62 --> 1332.34]  It houses AI RMF, its playbook in an interactive, searchable, filterable manner.
[1332.34 --> 1336.86]  And by the way, the AI Resource Center is definitely a work in progress,
[1336.86 --> 1341.90]  and we want to keep adding to that and adding more additional capabilities,
[1342.34 --> 1345.12]  things such as standards hub, repository for metrics.
[1345.58 --> 1348.56]  We want it to be really a one-stop shop of all of the informations,
[1348.56 --> 1353.12]  but also a place for engagements across the different experts.
[1353.12 --> 1358.00]  In June of 2023, just give a little bit of context,
[1358.42 --> 1365.08]  the CHAT GPT-3 was released in November 2022, a month or so before release of AI RMF,
[1365.16 --> 1369.30]  and CHAT GPT-4 was released in February or beginning of the March,
[1369.38 --> 1374.00]  a month after release of the AI RMF.
[1374.00 --> 1380.22]  So in response to all of these new development and advancement technology,
[1380.78 --> 1385.68]  we put together a generative AI public working group
[1385.68 --> 1391.58]  where more than 2,000 volunteers help us study and understand the risk of the generative AI.
[1392.58 --> 1398.72]  And then in October, as you said, we received our latest assignment,
[1398.92 --> 1401.78]  Executive Order on Safe, Secure, and Trustworthy AI.
[1401.78 --> 1406.88]  This executive order really builds on the foundation works that we have been doing,
[1407.04 --> 1412.08]  from the AI RMF to Playbook to Resource Center to Generative AI Public Working Group,
[1412.64 --> 1416.16]  and supercharge our effort to cultivate trust in AI,
[1416.70 --> 1421.62]  mostly by giving us some tight timelines of the things to deliver.
[1422.56 --> 1426.82]  The EU specifically directed NIST to develop evaluations,
[1427.22 --> 1429.78]  redeeming safety and cybersecurity guidelines,
[1429.78 --> 1433.54]  facilitate development of consensus-based standards,
[1434.04 --> 1437.62]  and provide testing environment for evaluations of AI systems.
[1438.22 --> 1441.70]  All of these guidelines infrastructures,
[1441.98 --> 1443.30]  true to the nature of NIST,
[1443.38 --> 1447.76]  will be a voluntary resource for use by the AI community
[1447.76 --> 1452.40]  to support trustworthy development and responsible use of AI.
[1452.40 --> 1459.10]  We approach delivering on the EO the same way that we do all of our work going to the community.
[1459.34 --> 1462.76]  We put a request for information out to receive input.
[1462.88 --> 1464.48]  Based on the input that we received,
[1464.62 --> 1468.42]  we put draft document out for public comment.
[1468.58 --> 1470.26]  Based on the comments that we received,
[1470.26 --> 1483.22]  we developed the final documents that we were very pleased that all of them were released by the deadline of July 26 that the EO had given us.
[1484.26 --> 1487.30]  Quickly, a quick overview of the things that we put out.
[1487.30 --> 1493.74]  One of them was a document on a profile of AI RMF for generative AI.
[1494.46 --> 1495.86]  The document number is,
[1496.02 --> 1498.30]  at NIST we like to refer to everything with a number.
[1498.94 --> 1502.18]  So that document is a NIST AI 600-1.
[1502.68 --> 1504.40]  It's a cross-sectoral profile,
[1504.56 --> 1507.26]  companion resource to the AI risk management framework.
[1507.26 --> 1514.16]  Based on the input that we had and discussions that we had on the generative AI public working group,
[1514.94 --> 1518.58]  responses to the RFI and inputs that we have received.
[1518.86 --> 1521.70]  I think one main contribution of that document,
[1522.34 --> 1523.88]  if I want to summarize it,
[1524.26 --> 1532.08]  is its description of the risks that are novel or exasperated by generative AI technologies.
[1532.08 --> 1539.04]  These risks span from CBRN information capabilities,
[1539.44 --> 1548.48]  eased access to synthesis of materially nefarious informations that can lead to design capabilities for CBRN,
[1549.06 --> 1555.20]  confabulation, dangerous, violent, hateful content, data privacy risks,
[1556.08 --> 1557.52]  let me remember the rest,
[1557.52 --> 1561.40]  environmental impact, bias, human AI configuration,
[1561.70 --> 1563.84]  information integrity, information security,
[1564.66 --> 1565.80]  intellectual property,
[1566.66 --> 1568.72]  degrading or abusive content,
[1569.28 --> 1572.90]  and the concept of the value chain and component integration.
[1573.72 --> 1574.74]  With the generative AI,
[1574.86 --> 1576.20]  we are moving from the binary,
[1576.70 --> 1578.72]  the deployer, developer,
[1579.34 --> 1583.20]  kind of a actors and dynamics.
[1583.20 --> 1587.04]  And now we are having upstream of the third party components,
[1587.20 --> 1588.44]  including data,
[1589.02 --> 1592.00]  that are part of this value chain.
[1592.50 --> 1598.90]  So one of the things that we're working in continuing that work is to work with the community
[1598.90 --> 1602.88]  to get a better understanding of the technology stack,
[1603.32 --> 1604.90]  of AI stack, if you will,
[1605.20 --> 1605.94]  for AI,
[1606.18 --> 1611.14]  understand the role of the different AI actors involved there,
[1611.14 --> 1614.24]  so we can do a better risk management.
[1615.00 --> 1616.40]  As you're talking about that,
[1616.84 --> 1619.04]  could you describe a little bit,
[1619.40 --> 1621.60]  and this is just a question in my mind,
[1621.84 --> 1626.44]  like when we're talking about AI as risks,
[1626.74 --> 1628.40]  as a set of risks,
[1628.58 --> 1633.14]  and we talk about kind of that effort to create trust in technology,
[1634.82 --> 1636.78]  how do you tie those together?
[1636.78 --> 1638.34]  In this process,
[1639.26 --> 1640.74]  you've identified these risks,
[1640.80 --> 1642.16]  and you just enumerated those,
[1642.60 --> 1649.32]  and with the purpose of ultimately kind of helping people get to a point of trust
[1649.32 --> 1652.68]  and being able to implement the technologies productively,
[1653.20 --> 1658.38]  how do you approach getting to trust through mitigation of risk?
[1658.78 --> 1659.08]  Does that,
[1659.48 --> 1661.50]  I'm not sure if the question makes sense or not.
[1661.74 --> 1662.68]  It certainly makes sense.
[1662.68 --> 1666.36]  I'll try to answer the way I understood this.
[1667.32 --> 1671.16]  So AI systems are not inherently bad or risky,
[1671.48 --> 1677.84]  and it's often the context that determines if a negative impact will occur,
[1678.08 --> 1680.16]  and also what are the risks.
[1680.54 --> 1687.28]  So an example that I usually use is that if I use face recognition to unlock my phone
[1687.28 --> 1692.76]  versus face recognition as in the airport that now our faces are boarding pass to get on the plane,
[1693.64 --> 1696.82]  or face recognition in the context of the law enforcement,
[1697.52 --> 1698.70]  it's the same technology,
[1698.98 --> 1700.34]  but in the different context,
[1700.78 --> 1706.92]  there is different risks and different level of the assurances that we want to have
[1706.92 --> 1710.12]  for the systems to work in a trustworthy manner.
[1710.12 --> 1718.58]  So what we have been trying to do as part of our work in approaching trust and trustworthy AI,
[1719.08 --> 1721.42]  the first one was to unpack the concept,
[1722.16 --> 1728.28]  try to get into the characteristics that make a system trustworthy.
[1729.08 --> 1733.50]  That helps to answer the question of what to measure.
[1733.50 --> 1735.98]  If I want to know if it's trustworthy or not,
[1736.06 --> 1737.54]  what are the measurements I need to do?
[1737.94 --> 1740.38]  So I listed the seven characteristics,
[1740.70 --> 1743.10]  one valid and reliable, safe, secure, et cetera.
[1743.66 --> 1747.92]  So that gives a more of a systemic approach and structural approach
[1747.92 --> 1750.22]  to what are the dimensions,
[1750.54 --> 1755.34]  what are the characteristics that together can make a system trustworthy.
[1756.06 --> 1758.14]  And by the way, AIRMF talk about this,
[1758.28 --> 1762.32]  that not each of them by itself make a system trustworthy.
[1762.32 --> 1766.18]  You can have a system that is very secure,
[1766.34 --> 1768.04]  but not valid or accurate.
[1768.40 --> 1770.04]  So that's not going to be trustworthy.
[1770.32 --> 1772.42]  And a system that's 100% accurate,
[1772.42 --> 1774.48]  but not secure is also not trustworthy.
[1775.06 --> 1776.86]  So that gives, again,
[1776.98 --> 1779.90]  more structured approach on what to measure.
[1780.40 --> 1785.66]  Then the next step is how to measure methods and metrics for the measurement.
[1786.34 --> 1792.10]  Those type of measurement gives an information about limits and capabilities of the systems.
[1792.10 --> 1793.96]  The type of the risk that can occur,
[1794.12 --> 1796.90]  the magnitude of the impact if those risks occur.
[1798.12 --> 1800.18]  And then based on this information,
[1800.58 --> 1804.42]  then we can come up with mitigations and management of the risks.
[1804.54 --> 1811.68]  So AIRMF, its recommendations is really categorized in the four functions of govern,
[1812.24 --> 1813.96]  map, measure, and manage.
[1813.96 --> 1820.32]  The govern is giving recommendations on procedures and processes,
[1820.70 --> 1826.46]  roles and responsibilities that we want to have in an organization to do effective risk management.
[1826.86 --> 1827.96]  So what is the accountability line?
[1828.64 --> 1830.42]  What are the role and responsibility involved?
[1831.04 --> 1837.46]  The map functions provides recommendations on understanding the context of the use,
[1837.60 --> 1839.88]  you know, going back to that examples of the face recognition,
[1839.88 --> 1844.18]  understanding the environment that AI systems are being operating there,
[1844.32 --> 1847.52]  understanding the community that can be impacted by that,
[1847.98 --> 1850.86]  identify the risks in this particular context,
[1851.08 --> 1853.38]  understanding the laws, regulations,
[1853.38 --> 1857.34]  and policy that are effective in this context of use.
[1858.16 --> 1862.72]  The measure functions provides recommendations on the how to measure.
[1862.72 --> 1865.60]  So for all of the risks identified in the map measure,
[1866.10 --> 1870.16]  provides quantitative or qualitative recommendations on how to measure them,
[1870.22 --> 1876.32]  how to take into account the trade-off between all of those trustworthiness characteristics.
[1876.32 --> 1883.24]  And all of this information is being used during the managing the risk part that can,
[1883.60 --> 1890.74]  the recommendations can go from safeguards and mitigations that can put in place to mitigate risk,
[1890.74 --> 1897.06]  to sometimes we cannot just mitigate risk and the risk should either be accepted or transferred,
[1897.36 --> 1901.98]  or the systems is too risky that it should not be developed or deployed.
[1902.32 --> 1905.42]  So that is how the process in AIRM.
[1914.62 --> 1918.20]  There's a lot of your personal data out there on the internet, and you know this,
[1918.20 --> 1921.18]  anyone can see this stuff. There's more than you think though.
[1921.28 --> 1925.48]  Your name, your contact info, your social security number, your home address,
[1925.88 --> 1928.12]  your various addresses, your past addresses.
[1928.56 --> 1932.88]  There's even information about your family members, maybe even the name of your cat.
[1933.34 --> 1936.90]  This is all being compiled by data brokers and is being sold.
[1937.22 --> 1940.46]  Now these data brokers, they make a profit off your data, obviously.
[1940.82 --> 1941.38]  So they do it.
[1941.58 --> 1945.96]  Your data is a commodity and anyone on the web can buy your private details.
[1945.96 --> 1948.28]  They can identity theft you. They can fish you.
[1948.40 --> 1950.08]  They can attempt to fish you.
[1950.18 --> 1951.18]  They can harass you.
[1951.40 --> 1952.68]  They can send you unwanted spam.
[1952.76 --> 1953.96]  They can call you nonstop.
[1954.78 --> 1956.32]  And this is something I get lots.
[1956.84 --> 1960.40]  But now you're able to protect your privacy online with Delete Me.
[1960.76 --> 1964.50]  As a person who exists publicly for some time now,
[1964.72 --> 1968.26]  especially someone who shares their opinions online quite frequently,
[1968.70 --> 1972.32]  I'm aware, hyper aware of safety and security.
[1972.32 --> 1978.38]  And I take it seriously and it's easier than ever to find personal information about anyone online, really.
[1978.76 --> 1984.20]  All this data is just hanging out on the internet and can have actual consequences in the real world.
[1984.50 --> 1987.24]  That's why I was excited about finding this recent solution.
[1987.66 --> 1989.42]  And as sponsor of this show, Delete Me.
[1989.80 --> 1995.06]  Delete Me is a subscription service that removes your personal information from hundreds of data brokers online.
[1995.50 --> 1998.96]  When you sign up, you can provide Delete Me with exactly what information you want deleted.
[1998.96 --> 2001.00]  And their experts take it from there.
[2001.36 --> 2006.12]  They send you regular personalized privacy reports showing what information they found on the internet about you,
[2006.32 --> 2008.74]  where they found it, and what they removed.
[2009.16 --> 2011.86]  And Delete Me isn't just a one-time service.
[2012.38 --> 2015.22]  They are always working for you, constantly monitoring,
[2015.84 --> 2019.80]  constantly removing your personal information that you don't want on the internet.
[2019.80 --> 2024.42]  And to put it simply, Delete Me does all the hard work of wiping your data,
[2024.76 --> 2026.00]  your family's personal information,
[2026.00 --> 2029.74]  and all these things you don't want out there from those data brokers' websites.
[2030.32 --> 2034.76]  Now, the next step is to take control of your personal data and keep it private forever
[2034.76 --> 2036.40]  by signing up for Delete Me.
[2036.66 --> 2041.24]  Now, at a special discount rate for our listeners, of course, this is awesome,
[2041.24 --> 2048.62]  Get 20% off your Delete Me plan by texting PRACTICAL to 64000.
[2049.66 --> 2054.74]  Again, text the word PRACTICAL to 64000.
[2055.74 --> 2059.56]  And of course, you may know this already, but message and data rates may apply.
[2059.86 --> 2061.60]  Check the terms, all that good stuff.
[2061.86 --> 2068.42]  Once again, text the word PRACTICAL to 64000 and get 20% off Delete Me.
[2068.86 --> 2069.10]  Enjoy.
[2069.10 --> 2069.16]  Enjoy.
[2071.24 --> 2071.74]  Enjoy.
[2084.68 --> 2091.44]  So, that was very useful for me in terms of trying to frame and understand, you know,
[2091.48 --> 2095.10]  what you're relaying here in terms of govern, map, measure, manage.
[2095.10 --> 2101.66]  And you talked about something a moment ago that was really interesting in the sense of
[2101.66 --> 2106.98]  you have these characteristics, you know, that you're trying to measure toward trustworthy,
[2107.24 --> 2112.02]  but it's not just one and it's not just, you know, a black or white issue.
[2112.14 --> 2119.54]  You have a collection of them and they vary across different types of use cases, it sounds like.
[2119.54 --> 2122.96]  So, you kind of have a, you know, characteristic profiles in a sense.
[2123.56 --> 2131.12]  How do you think about, if you are out there as a consumer of the guidance that you're providing from NIST,
[2131.76 --> 2139.28]  maybe you're in a small company that's doing some work in AI and you're trying to implement the guidance from NIST
[2139.28 --> 2147.26]  and you're kind of evaluating your own profile of characteristics through that govern, map, measure, manage process.
[2147.74 --> 2149.42]  How does one frame that?
[2149.48 --> 2152.56]  If you're kind of just getting into this and trying to implement the guidance,
[2152.72 --> 2158.60]  could you talk a little bit about how an organization that maybe had not done this before
[2158.60 --> 2164.40]  might go about implementing a particular, you know, whatever their use case is?
[2164.66 --> 2167.88]  And, you know, how do they get started in the process?
[2168.14 --> 2169.42]  What's your recommendation there?
[2169.42 --> 2176.92]  The first thing I will say is that you don't need to implement all of the recommendations in the AI RMF
[2176.92 --> 2179.74]  to have a complete risk management.
[2180.42 --> 2187.20]  So, our recommendation is that start by looking at and reading the AI RMF.
[2187.20 --> 2188.86]  It's not a very long document.
[2189.20 --> 2189.78]  I forgot.
[2190.00 --> 2192.46]  I think it's about between 30 to 35 pages.
[2192.70 --> 2197.02]  So, get a kind of a holistic understanding of this.
[2197.20 --> 2205.56]  And then check out the playbook in the AI Resource Center where for each of the recommendations,
[2205.76 --> 2209.24]  AI RMF is in high level for functions.
[2209.80 --> 2213.34]  Each function is divided into categories and then subcategories.
[2213.34 --> 2220.52]  So, in a sort of a granular approach, we give recommendations on what to do for the govern.
[2220.80 --> 2226.04]  And then for each of those recommendations, get into a little bit more granular recommendations.
[2226.66 --> 2232.98]  The playbook for each of the subcategories, which is about, I think, 70 subcategories in the AI RMF,
[2232.98 --> 2244.38]  provides recommendations on suggested actions and informative documents that you can go read and get more information.
[2244.78 --> 2252.96]  And also suggestions about transparency and documentations for implementation of that subcategory.
[2252.96 --> 2264.58]  So, we often suggest that get a better understanding of the AI RMF, spend some time in the playbook to get a better understanding of the type of the things that can be done.
[2264.96 --> 2280.38]  And then, based on the use case, based on exactly what you want to do, start by simple, small number of recommendations in the AI RMF and start implementing that.
[2280.38 --> 2286.10]  Govern or map functions are useful starting points.
[2286.80 --> 2293.10]  Govern provides recommendations about the setup that you need for a successful risk management.
[2293.28 --> 2301.88]  So, it can give you ideas or an organization's ideas about the resources that's needed, the teams that needed to do this,
[2301.92 --> 2307.80]  so they can align it with their own resources and the teams that they have.
[2307.80 --> 2319.36]  And the map functions, as we discussed, gives recommendations of a better understanding of the context, getting answers to what needs to be measured.
[2319.90 --> 2327.96]  I will also add that the functions govern, map, measure, manage, there is no order on doing that.
[2328.14 --> 2331.14]  It depends on the use case, depends on what needs to be done.
[2331.56 --> 2334.68]  The starting point can be recommendations of any of the functions.
[2334.68 --> 2352.96]  We usually recommend start with govern and map, and then start with as few number of the subcategories or recommendations that the resources and the expertise of the entity allows for their implementations,
[2353.32 --> 2356.66]  of course, prioritize in terms of their own risk management.
[2356.66 --> 2367.88]  And then the last thing I'll also add is also be mindful that the risk management is not a one-time practice that we just do at once.
[2367.88 --> 2369.90]  And you say, okay, I'm done with my risk management.
[2370.46 --> 2373.82]  AI systems, you know, there's data drift, model drift.
[2374.78 --> 2380.88]  These newer models can change based on the interactions with the users, with the environment.
[2380.88 --> 2385.44]  So we suggest a continual monitoring and risk management.
[2385.70 --> 2395.78]  So I think one of the recommendations in the map or govern is to come up with a cadence of repeating the assessments of the risks.
[2396.68 --> 2399.16]  So that would be my recommendations.
[2399.58 --> 2402.70]  Another thing that I would say is that I mentioned the AIRC.
[2402.86 --> 2403.94]  I mentioned the playbook.
[2403.94 --> 2408.28]  We also, in the AIRMF, talk about profile.
[2408.88 --> 2419.94]  So I keep emphasizing the context of the use and mentioning that the importance of the context in AI system deployment, development, and the risk management.
[2420.46 --> 2426.42]  At the same time, AIRMF, by design, is trying to be sector agnostic and technology agnostic.
[2426.42 --> 2437.16]  We try to kind of come up with the foundations, the common set of the practices that's needed to be aware of and are suggested for risk management.
[2437.42 --> 2443.66]  But we also have a section on AI profile and recommendations on building verticals.
[2443.66 --> 2460.08]  These profiles are instantiations of the AIRMF for a particular use case or domain of use or technology domain so that each of the subcategories can be slanted or be aligned with that use case.
[2460.22 --> 2466.82]  So there can be a profile of AIRMF for the example that I used, medical image recognition.
[2467.50 --> 2471.88]  There, you can imagine a profile of AIRMF for financial sectors.
[2471.88 --> 2475.02]  That's something that we have been asked to work with the community on.
[2475.44 --> 2482.48]  That was a very long intro to say that there are a couple of profiles posted on the AI Resource Center.
[2483.34 --> 2489.36]  One is the one that Department of Labor did for inclusive hiring.
[2489.96 --> 2495.62]  Another one that Department of State did for human rights in AI.
[2495.62 --> 2504.56]  So that can give some sort of a window to or idea about where the organizations can start.
[2504.76 --> 2512.98]  In addition to the profile, we have also posted a few use cases and we will post more use cases.
[2513.18 --> 2522.62]  And that is how different organizations are using AIRMF that can hopefully be more practical examples of how to use AIRMF.
[2522.62 --> 2527.60]  That's a fantastic set of suggestions right there.
[2528.70 --> 2532.08]  And I'd actually like to kind of ask a follow-up to that.
[2532.22 --> 2538.84]  And as a prelude to my follow-up, if I'm understanding, kind of go to the AIRMF, read that core document.
[2539.22 --> 2540.08]  It's not very long.
[2540.14 --> 2540.96]  It's very consumable.
[2541.52 --> 2542.50]  Go to the playbook.
[2542.82 --> 2543.62]  Look at the subcategories.
[2544.28 --> 2546.20]  I believe you said there were about 70 of them.
[2546.20 --> 2551.34]  You know, it has suggested actions and references to other docs in that.
[2551.52 --> 2560.88]  And then start to bite off kind of simple, small chunks in terms of how you're going to approach the functions that you mentioned, starting kind of with govern and map.
[2561.02 --> 2564.92]  And then kind of how to put together resources and teams.
[2564.92 --> 2573.28]  And then kind of cycling back with a cadence of repeated assessments that are also specific to the vertical that you're in.
[2573.38 --> 2577.36]  And as you're doing that, it's feeling really practical from my step.
[2577.50 --> 2580.26]  You know, we're practical AI, so that appeals to us.
[2580.26 --> 2586.72]  I'd like to ask, are there now or do you expect kind of tooling?
[2587.08 --> 2595.08]  You know, like if you look outside of AI, kind of the software industry at large is kind of a predecessor to that.
[2595.28 --> 2609.10]  As standards and workflows and kind of best practices arose in software development at large, lots of tooling arose around how to do, you know, agile methodology and you name it.
[2609.10 --> 2611.48]  There are many different approaches to software development.
[2612.10 --> 2627.30]  Are you expecting tooling or do you have any thinking around what kind of tooling might help AI development teams that as they're building these teams and their resources so that they can be productive over time?
[2627.82 --> 2630.28]  How are you seeing that evolve going forward?
[2630.28 --> 2638.78]  Or do you think that there'll be a cottage industry kind of forming around this the way we've seen in software and other areas where there's a lot of tool support?
[2639.26 --> 2642.30]  Yes, we have already started seeing some of that.
[2642.62 --> 2649.46]  So there are entities that are putting tools for implementation of the IRMF and dashboards and all this.
[2650.34 --> 2654.04]  They have developed those tools and they are having it on their websites.
[2654.04 --> 2660.38]  If I can just go back and thank you for your excellent summary of my very long, windy answers.
[2661.18 --> 2662.26]  No, it's very good.
[2662.34 --> 2663.38]  I'm learning a lot here.
[2663.92 --> 2670.96]  And I ask your listeners to, I think, start with the AI Resource Center.
[2671.20 --> 2675.94]  The URL is airc.nist.gov.
[2676.68 --> 2682.18]  AIRMF is there and Playbook in an interactive, filterable way is there.
[2682.18 --> 2692.94]  So if their businesses is only, you know, they are developers, they can go and first filter all of the, you know, from the 70 recommendations, anything that is only applicable to the developers.
[2692.94 --> 2695.44]  So they're not overwhelmed with all of that.
[2695.44 --> 2709.72]  Or if they're only care about deployment and the issue of the bias for the deployment, they can go and say, you know, filter from the AI actors for the deployers and from the characteristics from the bias.
[2709.90 --> 2712.60]  And that gives them, that saves them sometimes.
[2712.60 --> 2721.00]  So that is the, where they get information from our website and some hints about, you know, kind of, we have it in more filterable way.
[2721.58 --> 2727.08]  And yes, there has already started entities that are putting more tooling in.
[2727.08 --> 2733.96]  And with the 600-1, that was the cross-sectoral profile of the AIRMF for the generative AI.
[2734.98 --> 2742.34]  The work that we're doing with the community, we are focusing on, we use the word operationalization.
[2742.54 --> 2747.14]  So what are the tools that are needed for operationalizing and implementing AIRMF?
[2747.14 --> 2756.40]  And going back and emphasizing the community engagements and the role that the input from the community plays in all of these things.
[2756.84 --> 2763.20]  Some of the tools can be developed by us, but the majority of the tools are being developed by the community and shared by the community.
[2763.20 --> 2765.40]  And we hope that we see more of that.
[2765.98 --> 2766.62]  I hope so, too.
[2766.74 --> 2767.72]  It's fascinating.
[2767.72 --> 2776.36]  I love the framework that you've given us here that is, you know, can be applied in so many different verticals and so many different ways.
[2776.54 --> 2779.86]  And yet is flexible in its guidance that way.
[2779.96 --> 2791.80]  As we wind up here and we have seen so much advancement in the development of AI, both as a technology and as the industries around it.
[2791.80 --> 2803.14]  And as you are kind of sitting there in the nerve center of kind of where this guidance and these standards come together, bridging both government and industry.
[2803.62 --> 2816.04]  As you look forward, what are some of the things when you're, you know, not in a particular meeting and you're just kind of winding down and you're kind of thinking creatively about where things are going.
[2816.04 --> 2826.04]  What are some of your thoughts about the future of this, both for NIST's role and for the industry and the technology at large, where we're going?
[2826.22 --> 2829.42]  Because it's just, you know, it's going at such a rate.
[2829.56 --> 2841.32]  It's so fast and it's fascinating and is, you know, changing the face of business, changing the face of how we are as humans and stuff in terms of the tools and, you know, that are available to us.
[2841.32 --> 2847.98]  I really love your insights into where you think all of this is going in the days and years ahead.
[2847.98 --> 2867.68]  I think what, and for me, the end goal, for me, what I'm hoping to see a lot of that is to use this powerful technology in the way, as a sort of a scientific discovery tool, in the way that we are doing the science and discoveries there.
[2867.68 --> 2885.68]  I think that is where we are going to see a lot of really advancements into precision medicine, individualized educations, you know, climate change, anything that's going to make life a lot better for all of us.
[2885.68 --> 2895.80]  I have to say this, that I, you know, my heart was worn by seeing Nobel Prizes for things such as AlphaFold.
[2896.04 --> 2900.12]  I keep saying for a long time that, you know, that needs a lot more recognitions.
[2900.64 --> 2906.16]  But really, all of the recognition that AI got through those prizes.
[2906.16 --> 2916.20]  But I'm also very aware of very important things that NIST can do and the community needs to do.
[2916.74 --> 2922.66]  I think we all agree that there is a lot that we don't know about how these models work.
[2923.08 --> 2924.60]  And we ought to do something about it.
[2924.66 --> 2929.84]  We need to have a better understanding of how these models work, their capability and limits.
[2929.84 --> 2934.76]  That get me to the important topic of evaluations and testing.
[2935.44 --> 2943.70]  We talk about it at the beginning of this podcast that it's important to unpack the concept of the trust into the things that needs to be measured.
[2944.08 --> 2949.46]  But at the end of the day, we need to have reliable measurements for assurance that the systems are trustworthy.
[2950.34 --> 2959.12]  At NIST, we are, as a measurement science agency, we are the big fan of this quote from Lord Kelvin that if you cannot measure it, you cannot improve it.
[2959.12 --> 2971.86]  So if you want to improve the trustworthiness and the reliability of the systems, we need to have a good handle on how to test them and how to evaluate for reliability, for validity, for the trustworthiness characteristics.
[2972.64 --> 2976.38]  And our knowledge on how to test AI systems is very limited.
[2976.62 --> 2978.80]  We need better evaluations, as we can see.
[2979.76 --> 2981.06]  Benchmarks are too easy.
[2981.42 --> 2983.34]  They get saturated very quickly.
[2983.62 --> 2986.76]  We need to have a better understanding of how they work.
[2986.76 --> 2995.48]  That gets to the assurance that can build trust into the technology and give users, everybody, confidence that the systems works.
[2996.28 --> 3010.38]  And the third item that I put in, once we have built that knowledge base, once we have a good scientific foundations, when we have true-dead research and the work with the community, we have built the technical building blocks.
[3010.38 --> 3025.78]  Let's develop clear, understandable, technically robust standards that can help with global improbability of AI evaluations, AI assurance, and AI governance.
[3026.62 --> 3027.06]  Fantastic.
[3027.40 --> 3031.74]  Well, Elham Tabasi, thank you so much for coming on the Practical AI Podcast.
[3031.74 --> 3036.90]  It was very, very instructive in terms of how to frame this.
[3037.20 --> 3043.52]  Certainly, information that I'm going to be using going forward and really appreciate you taking time to talk with us today.
[3043.94 --> 3050.00]  I appreciate the opportunity to be here and talk and really enjoy the conversation.
[3050.18 --> 3050.42]  Thanks.
[3050.42 --> 3058.80]  All right.
[3059.08 --> 3061.58]  That is Practical AI for this week.
[3062.38 --> 3063.42]  Subscribe now.
[3063.58 --> 3068.58]  If you haven't already, head to practicalai.fm for all the ways.
[3068.58 --> 3074.98]  And join our free Slack team where you can hang out with Daniel, Chris, and the entire ChangeLog community.
[3075.54 --> 3080.18]  Sign up today at practicalai.fm slash community.
[3080.42 --> 3087.72]  Thanks again to our partners at fly.io, to our Beat Freaking Residents, Breakmaster Cylinder, and to you for listening.
[3088.08 --> 3089.84]  We appreciate you spending time with us.
[3090.20 --> 3091.38]  That's all for now.
[3091.62 --> 3093.30]  We'll talk to you again next time.
[3098.58 --> 3100.58]  Breakmaster Cylinder
