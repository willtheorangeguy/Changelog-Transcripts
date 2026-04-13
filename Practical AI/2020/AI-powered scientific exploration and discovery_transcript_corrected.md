[0.00 → 2.58] Bandwidth for Changelog is provided by Vastly.
[2.96 → 4.84] Learn more at Fastly.com.
[5.08 → 8.16] We move fast and fix things here at Changelog because of Rollbar.
[8.30 → 9.98] Check them out at Rollbar.com.
[10.24 → 12.40] And we're hosted on Linde cloud servers.
[12.76 → 14.74] Head to linode.com slash Changelog.
[17.46 → 20.04] This episode is brought to you by DigitalOcean.
[20.38 → 25.14] DigitalOcean's developer cloud makes it simple to launch in the cloud and scale up as you grow.
[25.14 → 36.82] They have an intuitive control panel, predictable pricing, team accounts, worldwide availability with a 99.99 uptime SLA and 24-7, 365 world-class support to back that up.
[37.08 → 42.54] DigitalOcean makes it easy to deploy, scale, store, secure, and monitor your cloud environments.
[42.90 → 46.34] Head to do.co slash Changelog to get started with a $100 credit.
[46.64 → 48.80] Again, do.co slash Changelog.
[55.14 → 65.64] Welcome to Practical AI, a weekly podcast about making artificial intelligence practical, productive, and accessible to everyone.
[66.02 → 70.54] This is where conversations around AI, machine learning, and data science happen.
[71.02 → 75.28] Join the community and snag with us around various topics of the show at changelog.com slash community.
[75.60 → 76.44] Follow us on Twitter.
[76.54 → 78.04] We're at Practical AI FM.
[78.30 → 79.34] And now onto the show.
[79.34 → 87.40] Welcome to another episode of Practical AI.
[88.04 → 98.86] I'm Daniel Whiten ack, a data scientist with SIL International, and I'm joined as always by my co-host Chris Benson, who is a principal AI strategist at Lockheed Martin.
[99.06 → 99.74] How are you doing, Chris?
[99.98 → 100.86] Hey, doing great, Daniel.
[100.92 → 101.56] How's it going today?
[102.18 → 103.16] It's going pretty good.
[103.16 → 110.12] A busy week and lots to work on, which is good and tiring all at the same time, but mostly good.
[110.20 → 110.96] What about on your end?
[111.38 → 111.84] Nothing much.
[111.92 → 113.18] Just the usual work.
[113.38 → 117.88] And we're finally back to some nice weather here in Atlanta, so I'm enjoying that.
[118.36 → 119.04] Cool, cool.
[119.36 → 131.84] I know that in our last Fully Connected episode, one of the things that we talked about was the increase in AI-related publications and also increases in publications on the archive.
[131.84 → 134.80] And I think that's true in general.
[135.18 → 141.08] And I alluded to the fact that we would be talking about that more in a future episode, and that's this episode.
[141.32 → 151.08] So I'm really happy to introduce Doug Raymond, who's joining us from the Allen Institute for AI, where he's the general manager of Semantic Scholar.
[151.32 → 151.82] Welcome, Doug.
[152.34 → 152.94] Thank you.
[153.14 → 155.04] I'm really glad to be here.
[155.76 → 156.92] Yeah, great to have you.
[156.92 → 174.12] Before we jump into Semantic Scholar and all about scientific publications and searching them and all of that stuff, I'd be interested to just hear a little bit about your background and how you ended up at the Allen Institute and working with AI and Semantic Scholar.
[174.84 → 175.62] Yeah, thanks, Daniel.
[175.80 → 184.96] My background is mostly in the product and business of artificial intelligence and machine learning.
[184.96 → 192.18] Before I was at the Allen Institute, I was at Amazon working on the Alexa machine learning platform.
[192.58 → 205.96] And prior to that, I've done a series of startups in the machine learning space and advertising and commodity trading, and then had a five-year stint at Google working on the Google Ads platform.
[205.96 → 208.90] Yeah, that's quite an experience with AI.
[209.48 → 220.10] What stands out to you over the years in terms of how AI or applying AI in the product sense or in an applied way has changed during that time?
[220.10 → 235.76] Well, from my perspective, what's changed is that we've become, as consumers, more conscious about how these models are influencing our lives and replacing various aspects of human cognition.
[235.76 → 244.32] So, when I started out in the advertising space at Google, and this is now close to 15 years ago, we didn't think of it as AI.
[244.58 → 247.62] We thought of it as an efficient way to match supply and demand.
[247.62 → 260.66] But as the models have gotten more sophisticated and more capable, we, as business and product people, are thinking more carefully about how we can actually help users with some problem.
[261.04 → 270.42] And that's where the AI part of the technology becomes super relevant because if you're not solving a problem that a user actually has, it's not really artificial intelligence.
[270.42 → 273.36] It could just be an interesting feature.
[273.36 → 292.18] And on the other side, I think the concerns about how these products and these AI models are using our data and potentially influencing us in unforeseen ways has become a much bigger part of what we think about and the considerations for what we build in the product.
[292.18 → 304.18] So, were some of those considerations as related to how we use AI and think about it, was that what kind of motivated you to join with an organization like the Allen Institute?
[304.32 → 312.48] And maybe for those that aren't familiar, the Allen Institute is kind of a different sort of organization than like a tech company like Google, right?
[312.62 → 316.46] So, could you kind of explain that and how you got involved with them?
[317.02 → 317.46] Absolutely.
[317.46 → 322.52] So, I've been at the Allen Institute for almost two years now.
[322.88 → 327.34] And what motivated me to join was the mission.
[327.88 → 337.32] And we were founded by Microsoft co-founder Paul Allen about five years ago with the mission to build AI for the common good.
[337.68 → 346.34] So, it's a core part of our mission to identify areas where AI can help the public in general.
[346.34 → 349.60] And I found that to be really compelling.
[350.02 → 353.96] I definitely enjoyed startup life and working at Amazon and Google.
[354.18 → 356.06] And those were great experiences.
[356.88 → 364.40] But, you know, my real motivation, I think, to continue my career is to do something that has a positive impact,
[364.40 → 381.12] especially with so much political discord and challenge in the world, especially with respect to the environment and other areas where citizens really need to have the accurate and relevant access to information to make good decisions.
[381.12 → 384.66] And so, that is a part of our mission.
[384.84 → 392.30] And it's something that seemed like a much more impactful use of my time than continuing to work on commercial products.
[392.64 → 392.82] Gotcha.
[393.06 → 401.48] And just out of curiosity, do you have any insight into why Paul Allen wanted to make this investment into AI, especially at the time that he did?
[401.70 → 402.62] Any insight into that?
[403.06 → 403.44] Yes.
[403.44 → 407.12] You know, Paul Allen was a visionary man.
[407.62 → 411.12] He had a variety of passions and interests.
[412.18 → 417.82] And when AI2 was founded, obviously, I joined later.
[418.00 → 431.70] But the story of AI2's founding is related to Paul's interest in how AI could solve really fundamental problems in terms of how people access information.
[431.70 → 445.10] So, one of our first projects at AI2 is a project called Ariosto, which is a project designed to create an AI model that could answer scientific questions in a conversational format.
[445.98 → 454.26] And we recently reached a milestone where Ariosto Project is able to ace the eighth grade New York region science test.
[454.26 → 460.26] And so, the vision that Paul set years before has resulted in an AI that can actually help answer scientific questions.
[460.98 → 463.78] And that project continues and is taking on new challenges.
[464.54 → 474.56] With respect to Semantic Scholar, Paul's vision, and as expressed by our CEO, Ornizioni, was there is so much scientific literature out there.
[474.56 → 483.54] And it's so difficult to access and understand what's relevant that the cure for cancer might be latent in the scientific literature.
[484.20 → 492.50] But with AI tools, potentially, we could make the connections and allow scholars to discover those connections and lead to breakthroughs.
[492.50 → 503.94] So, I'm curious, now that you've kind of got into Semantic Scholar, given the Allen Institute's mission and how it's structured in general, why would it be important?
[504.24 → 517.24] Or why should Allen Institute maybe be the one that kind of provides this assistance in parsing through the scientific literature versus maybe a for-profit organization or something like that?
[517.24 → 523.74] Absolutely. So, I think that Semantic Scholar exists in a unique place.
[523.86 → 530.00] And, of course, there are many tools out there designed to help access the scientific literature.
[530.36 → 538.98] But when you think about broad coverage tools in the sense that they cover all scientific domains and try to solve this discovery problem in a generalized way,
[538.98 → 546.64] there's Google Scholar, there are tools like ResearchGate, and they don't have a really robust business model.
[546.64 → 552.58] So, Google Scholar does continue to release features, but the pace of innovation has been quite slow.
[552.70 → 558.62] And our users always tell us that they want a better discovery experience than what they can find in Google Scholar.
[559.34 → 564.48] And other smaller startups like ResearchGate have the imperative of a business model.
[564.48 → 577.22] So, they tend to be focused on social networking aspects or other ways to generate ad revenue and not really on solving this fundamental discovery problem that basically all scientific disciplines face,
[577.30 → 584.78] which is there is just an information overload in terms of the number of scientific publications that are published each year.
[584.78 → 593.46] And then, I guess, just to add to that on the other dimension, there are a lot of special purpose tools which try to solve a problem in a particular scientific domain.
[593.80 → 600.94] And they tend to be point solutions but aren't well integrated with other domains or the rest of the research lifecycle.
[600.94 → 608.76] And so, we think we're in a relatively unique place where our mission is to have the greatest impact possible on science.
[609.12 → 620.96] And with Paul's backing, we're able to pursue that in a generalized way, which makes me think that we have a great opportunity to have a huge impact on the progress of science overall.
[621.80 → 622.60] That sounds cool.
[622.60 → 630.18] So, I mean, what would you say were the main problems that you were targeting to solve with Semantic Scholar when you started out?
[630.36 → 635.90] And how were you trying to make it different from what was already out there and what people were using?
[636.16 → 640.82] And how did you choose the type of interface that you wanted to kind of realize that in?
[641.30 → 641.94] Yeah, absolutely.
[642.16 → 647.66] So, let me start by talking about the problem that's sort of core to our mission.
[647.66 → 652.70] And we define our problem as information overload in science.
[653.44 → 664.56] And the characteristics of that problem are that as the number of scientists around the world have grown and the number of research institutions and publications have grown,
[664.80 → 674.42] the number of potentially relevant scientific papers for each individual scholar to read has grown at an exponential pace since World War II.
[674.42 → 678.70] So, we're now at 3.5 million new publications each year.
[678.84 → 680.86] It grows about 5% or 6%.
[680.86 → 684.70] Yeah, it grows at 5% or 6% a year.
[685.28 → 688.50] And the number of new journals also grows.
[688.74 → 690.40] It's a proliferation of new publications.
[691.30 → 700.28] And if you're a scholar in a particular domain, your ability to read papers is somewhat static, at least in the short term.
[700.28 → 707.30] So, our research indicates that the average scholar reads approximately 250 papers a year.
[707.52 → 710.80] The time they spend per paper is about 30 to 45 minutes.
[711.44 → 718.30] And that comes out to, you know, up to 15 hours a week just trying to understand what's new or relevant in their domain.
[718.78 → 724.46] And so, they don't really have a good way to read more papers without the help of tools like Semantic Scholar.
[724.46 → 734.86] So, the way that we think of our solution to information overload is if the scholar's attention is fixed, and we want to, at least the amount of time they have is fixed,
[735.24 → 747.02] we want to make it possible for them to overcome information overload by discovering the relevant papers much more easily and with much higher quality in terms of what they decide to read.
[747.02 → 755.70] And then we want to make it easier for them to understand what's interesting and salient to their research in each paper they read.
[756.22 → 760.98] So, while you were talking, I was just kind of contemplating some of the numbers that you mentioned.
[761.14 → 769.38] And at least if I did my calculation right, so 45 minutes per paper, 3.5 million per year,
[769.38 → 776.90] that would take me about 300 years to just read all the papers for a single year.
[777.24 → 778.96] So, obviously, no one's going to do that.
[779.02 → 784.08] You mentioned like, you know, scholars read about, what was it, 250 or something per year?
[784.54 → 784.84] Yes.
[785.30 → 787.24] So, it's called Semantic Scholar.
[787.40 → 796.96] So, is the idea really around like a semantic or a text-centric, like natural text-centric way to search through the literature?
[797.50 → 798.78] Yeah, partially, yes.
[798.78 → 803.28] And if it's okay, I'll take a minute to explain why we're called Semantic Scholar.
[803.52 → 808.20] So, you hit the nail on the head, Daniel, in terms of describing the challenge.
[808.54 → 812.06] 300 years worth of reading every year is obviously untenable.
[812.42 → 820.14] And so, Semantic Scholar, we think of semantics as the science of how do we understand, extract the meaning from the scientific literature.
[820.14 → 837.66] So, when I talked earlier about the evolution of AI throughout my career, Semantic Scholar is an AI application because we're trying to use our AI models and technology to survey and read the papers in advance for you.
[837.66 → 849.62] So, that as a scholar, instead of spending 300 hours reading a bunch of papers, most of which aren't relevant, you can focus on only the papers which are most relevant to your interest at that moment.
[850.24 → 855.04] That's our vision in terms of how AI can solve this problem of information overload.
[855.04 → 861.18] I'm just curious, how do you match up the user who's using Semantic Scholar with that process?
[861.46 → 865.14] How do you know what is the right research and how to present it to them?
[865.14 → 873.98] Absolutely. So, we think of our product as having kind of three core attributes that help the user find the relevant science.
[874.80 → 886.50] And at a high level, and I can go into more detail in terms of how we use AI in each of these areas, one thing that we've done is create a very rich knowledge graph that represents all of scientific literature.
[886.50 → 900.60] So, through mapping all the papers and citations and indexing full-text PDF of the scientific literature created a very rich representation of science at this point, over 180 million scientific papers.
[901.02 → 910.92] The second aspect of that, which is, I think, more related to your question around how does a scholar use us to find the relevant literature, is our discovery experience.
[910.92 → 918.10] And so, a semantic scholar is, the initial experience is pretty much like traditional search engine.
[918.58 → 936.94] However, because we've extracted the semantics from all the underlying literature, and it's in a structured knowledge graph format, it's much easier for the scholar to define their interest in terms of this area of science from these journals in this state range and have a comprehensive representation,
[936.94 → 957.08] not only of what papers meet that interest, but all the other extracted information that we build with our models, such as the influence of the paper, how that paper has been discussed in social media, the associated data sets and GitHub repositories that are used in that research.
[957.08 → 970.68] So, we try to create a very rich representation of not only what's in that scholar's scope of interest, but within each paper, you know, what are the points that would allow them to understand, is this paper relevant?
[970.84 → 975.20] What is new and interesting about my area of interest that's expressed in this paper?
[987.08 → 991.78] Hello there, this is Jared Santo, Managing Editor here at Changelog.
[992.02 → 996.90] The fact that you're listening to this means you are actively investing in your future in this industry.
[997.52 → 999.72] Things move fast and keeping up is hard work.
[1000.08 → 1003.60] Help us help you stay relevant by subscribing to Changelog Weekly.
[1003.98 → 1012.10] We track, log, and contextualize what's happening in software throughout the week and deliver it directly to your inbox on Sunday mornings.
[1012.10 → 1019.98] Head to Changelog.com slash weekly to browse the archives, subscribe, and push the easy button on your continuing education.
[1020.58 → 1021.82] That's all from me.
[1022.02 → 1024.96] Once again, that's Changelog.com slash weekly.
[1024.96 → 1054.94] Changelog.com slash weekly.
[1054.96 → 1058.24] So there's this sort of knowledge graph that you mentioned.
[1058.48 → 1061.14] And then there's the search and discovery.
[1061.66 → 1065.94] I don't know if it's right to call it like recommendation or notification type of stuff.
[1066.22 → 1079.10] I was wondering, there's kind of, at least I'm aware that there's some work going on pretty widely around using AI to generate or automatically build knowledge bases or knowledge graphs.
[1079.10 → 1086.84] So I'm wondering if that's one place where you're utilizing AI to kind of extract this and kind of automatically build the knowledge graph.
[1086.96 → 1093.92] But then it sounds like maybe there are other opportunities for AI usage on the user interactivity side.
[1094.00 → 1105.38] And I was wondering how much effort you're kind of placing in those two areas and where you think the main benefits, at least in this application, are for AI, at least that you've leveraged so far.
[1105.38 → 1110.64] Sure. So it's true that we do use models to build our knowledge graph.
[1110.90 → 1114.34] And there are some efforts going on there to increase the quality and coverage of it.
[1114.34 → 1128.82] In terms of what are the areas that we think are most exciting to us from a research standpoint, we're focused on this discovery experience in terms of how do we help you identify what's new and relevant.
[1128.98 → 1143.00] And we have several research efforts in terms of creating a personalized representation of what's new, of creating explanations or recommendations that are actionable in terms of how we explain to you why we've recommended particular papers.
[1143.00 → 1148.82] And we have a number of other research areas there that I'd love to talk about that I think are quite exciting.
[1149.48 → 1151.90] Yeah, definitely. I'd love to hear more about those.
[1152.02 → 1158.40] I know specifically because I've used Semantic Scholar, and maybe you can describe this a little bit more and how it fits into some of those discovery things.
[1158.56 → 1168.66] But as you're searching things, you can, I believe, tag certain content and create sort of tagged collections of content that you're looking for and organizing.
[1169.04 → 1171.76] And does that fit into this sort of discovery model?
[1171.76 → 1180.70] It does. I think, you know, we have a library where we enable our users to organize and tag their research.
[1180.90 → 1190.60] And so I think that's part of how we help them use it in their work and have a greater impact in their work with the research they've found through Semantic Scholar.
[1190.60 → 1201.74] There's also a lot of work we've done to help you identify out of the thousands of new papers published each day, which of those are relevant to me, which of those are worth reading.
[1202.06 → 1204.40] That's another area of research for us.
[1204.40 → 1213.16] So is that fit more within a sort of traditional recommender system sort of thing or in what ways are those being generated?
[1213.28 → 1219.66] And one of the things that's going through my mind, too, is it seems like there's these giant benefits to this sort of approach.
[1219.66 → 1236.60] But then also, if you're kind of amplifying certain signals within the scientific community, you kind of have to be pretty right on with those because you could kind of like you said, the cure for cancer could still be sitting somewhere below this sort of amplified signals.
[1236.60 → 1240.72] Yes. So maybe I could talk about how do we recommend papers.
[1241.04 → 1263.66] So I think if I understand your point, Daniel, there's a phenomenon in science where which I would describe as, you know, the rich get richer, which is if you have an institutional backing, if you're publishing your papers in prestigious journals, and you're generating a lot of citations, that citation count can be used as a proxy for quality.
[1263.66 → 1269.66] And those scholars who don't have the institutional backing, don't have as many citations, their research will get overlooked.
[1270.06 → 1274.38] And I think we are very conscious of that phenomenon.
[1275.10 → 1282.64] And it is one of the challenges we hope to overcome with our approach to discovery and recommending papers.
[1283.30 → 1286.12] So I could go a little bit more into that.
[1286.26 → 1287.44] Yeah, that'd be fantastic if you would.
[1287.90 → 1288.62] Yeah, absolutely.
[1288.62 → 1294.96] So I think in the semantic scholar experience, we do use citation count as an interesting piece of metadata.
[1295.22 → 1309.30] But from our perspective, one of the challenges with the growth of the scientific literature is that there are great scholars out there and great science being done in places where they aren't in a prestigious conference or prestigious institution or published in a prestigious journal.
[1309.30 → 1313.54] And so, therefore, they may be overlooked if that's the only thing you're looking at.
[1314.14 → 1324.88] So, for us, we really think a lot about how can you discover science that's relevant before it has a rich citation history or science that's relevant without a citation history.
[1325.10 → 1333.04] And so, one of the big efforts that we've made is trying to understand the relevance of papers at a very fundamental level.
[1333.04 → 1336.86] And that starts with us at the language model level.
[1337.24 → 1342.80] And I think, perhaps in a previous podcast, you talked about some of our work on different language models.
[1343.04 → 1352.10] At AI2, we develop a language model called ELMO, which was subsequently developed further into a model called BERT through Google.
[1352.10 → 1362.46] We have created a pre-trained language model called CYBER, which is trained on 3 billion words from a host of scientific documents.
[1362.66 → 1375.76] So, it is particularly good for trying to understand what a paper is about in a way that a model trained on Wikipedia or other texts would not be quite as good at.
[1375.76 → 1386.32] And we've used that scientific language model, which we call CYBER, to build a host of discovery experiences that helps scholars find relevant papers,
[1386.44 → 1392.50] even if the citation count doesn't necessarily indicate that that paper is highly regarded.
[1393.10 → 1398.10] So, one of the things we've done with that is created a personalized feed of papers.
[1398.28 → 1403.14] It's sort of a Spotify for research, if you will, which is available in Semantic Scholar now.
[1403.14 → 1413.62] And the idea there is that if we use this language model and create a neural network to understand the similarity of papers,
[1414.50 → 1419.08] we then allow the user to indicate what they like and what they don't like.
[1419.54 → 1427.16] And through that process, in a few clicks, they can create a highly relevant feed of research papers that's tuned exactly to their personal interests
[1427.16 → 1432.46] in a way that you could never do it with a search engine or just looking at citation counts.
[1432.46 → 1435.80] And how do you make that available to the user?
[1435.96 → 1439.78] How are they able to actually kind of specify what their interests are?
[1440.42 → 1440.90] Certainly.
[1441.14 → 1449.46] So, the way the product works is you go to Semantic Scholar, you select papers that you believe are relevant to you,
[1449.62 → 1456.22] and you can use the traditional search interface to do that or just type in the title of the paper you already have high regard for,
[1456.22 → 1460.78] and then we'll automatically generate recommendations of related works.
[1460.78 → 1471.20] And by indicating, I like this paper, I don't like this paper, you can tune that feed in real time to be highly relevant to your interests.
[1471.20 → 1475.74] So, you're only seeing papers that are directly relevant to the interest you're pursuing.
[1475.74 → 1487.26] I'm curious, in this process, like how long approximately or how many papers do I have to go through and kind of tag before I start seeing some of this benefit?
[1487.26 → 1492.50] And I guess also on that front, is this amplified like between users?
[1492.62 → 1500.82] So, I guess there's like personalization at the user level, but there's also in science, there are communities of people that are working together and collaborations.
[1500.82 → 1505.02] And does that fit into the recommendation at all?
[1505.06 → 1506.86] Or is it mostly at the language model level?
[1507.26 → 1511.76] Yeah, at this point, it's really at the language model and what that individual user has indicated.
[1512.08 → 1519.08] I think what you described is very interested in terms of how do we build recommenders that service a community.
[1519.08 → 1533.84] But what we've done so far is created a model that looks at the paper similarity based on cyber, a model trained on scientific text, and then tune it so that scholars can get papers that are relevant to their interest.
[1533.84 → 1538.06] In terms of your initial question, how many papers does it take?
[1538.06 → 1546.72] What we find is that most of our users are able to get a highly relevant feed by rating between three and five papers.
[1546.94 → 1550.64] Depending on how generalized or specific your interest is, it could take more.
[1550.84 → 1558.84] So, if you have a very specific narrow interest, you might need to rate more papers before your feed becomes highly, highly relevant.
[1559.16 → 1565.84] But in most cases, it takes a minute or two to identify three to five papers that match your interest.
[1565.84 → 1579.90] So, I'm also curious, because when I'm thinking about this sort of similarity matching with a language model, I'm kind of thinking about it like, oh, you perform, you know, you provide input data to this language model.
[1580.02 → 1581.74] You get out some representation.
[1582.00 → 1584.84] Maybe you compare distances or something like that.
[1584.86 → 1591.44] But it's not really related to, in my mind, the sort of graph structured data that you mentioned before.
[1591.44 → 1593.70] Are those both utilized?
[1593.94 → 1598.44] And is the graph stuff mostly utilized for, like, just search?
[1598.58 → 1607.70] Like, you type in a query, and then you get entities out of that and match those entities to entities in the graph versus, like, the language model is utilized mostly for recommendation?
[1608.12 → 1609.94] Or is there any interplay between those?
[1610.34 → 1610.84] There is.
[1610.90 → 1615.48] So, to be clear, the graph structure is kind of our core data structure.
[1615.48 → 1624.36] So, when you search Semantic Scholar, you're essentially trying to identify, you know, a vector within this knowledge graph that's within your scope of interest.
[1625.16 → 1631.64] For the recommendation experience, the adaptive recommendations I was describing, we do use the graph information.
[1631.82 → 1639.62] But what we do is use a citation graph of these different papers as a feature in that similarity model.
[1639.62 → 1651.20] So, understanding what papers have cited each other helps determine, you know, how close they are in that similarity space based on what the user has indicated is of interest to them.
[1651.94 → 1652.04] Gotcha.
[1652.24 → 1654.06] So, it's kind of like the language.
[1654.36 → 1661.04] Am I correct in saying, like, the language model would give you a sort of learned representation of a paper?
[1661.04 → 1670.52] And then you're matching that in terms of distance in some space and using a feature from the graph, like the citations, like you're mentioning, to further refine that?
[1670.74 → 1672.68] Or is it different from that?
[1673.04 → 1675.24] I think that's pretty close, yes.
[1675.38 → 1679.40] In the sense that, you know, the language model is just how we understand what the paper is about.
[1679.40 → 1689.64] In terms of understanding how similar one paper is to another, the language model, the Cyber is one aspect of understanding, okay, here's a vector that represents the meaning of this paper.
[1690.20 → 1701.26] But similarity is also indicated by citation graph, a neural model that we built to map those papers in some vector space to understand how similar they are.
[1701.26 → 1711.70] And then the aspect that makes this a personalized experience is the user being able to indicate what papers are of interest and are not of interest.
[1711.80 → 1717.14] And that becomes an input to the model to define what papers should be presented.
[1731.26 → 1735.20] This episode is brought to you by Brave.
[1735.58 → 1737.40] We deserve a better internet.
[1737.72 → 1741.06] That's why the team behind Brave reimagined what a browser could be.
[1741.56 → 1743.50] Brave is like Chrome, the good parts.
[1743.80 → 1745.42] Even your extensions will just work.
[1745.66 → 1752.94] It has built-in ad and tracker blocking, easy anonymization with the Tor network, earn tokens while you browse, and use them to tip your favourite creators.
[1753.32 → 1754.90] And did I mention it's lightning fast?
[1755.24 → 1757.84] Turns out the web is superfast when you remove all the cruft.
[1757.84 → 1762.88] Download Brave today using the link in the show notes and give tipping a try on changelog.com.
[1774.56 → 1786.16] So I'm curious, as we were kind of talking through the ins and outs of discoverability in Semantic Scholar and also the, you know, how things are working under the hood.
[1786.16 → 1799.50] I got to thinking, like, given that you've processed so many scientific papers, are there any efforts within Semantic Scholar to sort of analyze in a more exploratory way the scientific community as a whole?
[1799.50 → 1812.00] Like, I'm guessing that, you know, from this knowledge graph, you're able to maybe extract collaborations and other things that might be sort of under-described in a general search interface.
[1812.00 → 1820.60] If you're just searching on a journal or something like that, where you're kind of representing more about a paper than is known.
[1820.60 → 1829.38] So I don't know, have you explored anything like that in terms of, you know, exploring what collaborations exist and how to represent those?
[1829.46 → 1836.84] And maybe I was thinking of, like, duplicate or highly related work in terms of, like, reviewing new work and that sort of thing.
[1836.94 → 1838.14] Are there any efforts like that?
[1838.58 → 1840.92] Yes, that is an interest of ours.
[1840.92 → 1843.90] And I could, a few efforts come to mind.
[1844.10 → 1856.18] So one thing that we've done recently is use our summary of authors as a way to help conference organizers disambiguate reviewers.
[1856.18 → 1871.44] So this is a problem in academic conferences where, if many papers are being submitted, you need to select the people who will review those papers to decide whether they will be accepted at the conference in an optimal way.
[1871.98 → 1883.18] And you can imagine how that problem becomes exponentially more difficult as the number of papers submitted increases exponentially year over year.
[1883.18 → 1893.54] So that is the submissions to conferences in computer science have grown multiple fold just in the last five or 10 years in fast-growing areas of AI.
[1893.92 → 1902.78] So one partnership we did in the fall was with ACL, which is a large conference that's going to be based in Seattle this year.
[1902.78 → 1922.46] And they used the Semantic Scholar Knowledge Graph to help disambiguate reviewers from the papers that are being submitted for review because you don't want someone that you've co-authored with or, you know, someone who's potentially, you know, on your same faculty to be reviewing your paper for conference because it creates conflicts of interest.
[1922.74 → 1924.36] That's an example of a recent application.
[1924.84 → 1930.42] I could talk about the other uses of Semantic Scholar in terms of understanding science overall.
[1930.68 → 1931.24] Oh, please do.
[1931.34 → 1931.88] That would be good.
[1931.88 → 1933.92] I was actually going to ask something very similar to that.
[1934.04 → 1935.06] Oh, absolutely.
[1935.06 → 1949.44] So because we've created this rich representation of science, it allows us to do what we would describe as meta research in terms of the trends in science and what potential opportunities or challenges are emerging.
[1949.74 → 1960.42] So we've published articles about the growth of open access publishing, about gender, the trends in gender equality and computer science publishing,
[1960.42 → 1966.42] looked at biomedical research and identified areas of bias in clinical studies.
[1966.42 → 1980.00] And in each of these cases, because we've created this rich and structured representation of science, we're able to do research on orders of magnitude larger data sets than any previous research.
[1980.00 → 2000.88] So do you have any, I'm just kind of curious, you just started to go there, but my mind's kind of wondering on different possible use cases of that, you know, because you're really in your, your structured graph, you're kind of capturing the shape of science, if you will, you know, based on the papers and the citations and kind of where it's flowing and where it's not flowing a little bit.
[2000.88 → 2004.66] Do you have some ideas when you're talking about that kind of meta analysis?
[2005.02 → 2009.78] Any thoughts on different use cases where you guys have thought that that would be particularly useful?
[2010.38 → 2010.74] Yes.
[2011.10 → 2024.78] So we've already published a number of studies where we've identified areas of bias or potential insights of social impact, for instance, gender equality and computer science.
[2024.78 → 2037.80] I think in the future, we'd like to do more of these studies and focus them on areas where we can identify opportunities to increase the impact of science overall.
[2037.80 → 2059.84] So a big area of interest for us is climate change research in terms of what's being funded, where are the areas that are either over-served or underserved, and how can we surface that information in a way that helps scholars, but also potentially policymakers or politicians invest in the areas that can have the greatest impact.
[2059.84 → 2080.40] I'm curious as well, as you've done this sort of work, and you've obviously processed a lot, so there's a lot there already, but I was wondering if there are certain areas of science or areas of research that are harder to probe in terms with this approach than others.
[2080.40 → 2107.56] So I'm thinking I work with a bunch of linguists at my organization, and I found that there's all of this sort of archived systems that are really hard to access and search and all of those things, but that's where a lot of the linguistic research is, and it's all sort of documented in really odd and conflicting ways in terms of what languages it applies to and all these things.
[2107.56 → 2125.96] So I was wondering if there are systems like that or areas of science that have proved harder to integrate with this sort of approach, and what sort of ways you're approaching the diversity of how science is represented for different areas.
[2126.48 → 2135.42] Yeah, you know, I would say that there are definitely opportunities to increase our coverage in certain areas of science.
[2135.42 → 2147.64] At the highest level, we are optimistic that our generalized approach seems to work pretty well across all domains of science that we cover.
[2147.64 → 2165.76] There are definitely issues that you alluded to in terms of older publications where we may not be able to get access to a PDF or the data that allows us to figure out how to integrate it under knowledge graph is hard to come by.
[2166.12 → 2171.14] But I wouldn't say that there's sort of an obvious major problem to overcome.
[2171.14 → 2179.88] There are a lot of smaller problems to overcome, which we kind of address in our planning based on how much impact we think we can have for our scholars.
[2180.96 → 2200.90] Yeah, and I guess that there are various considerations in terms of how actively or active and rapidly developing areas of science are and, you know, how they maybe apply to certain things that the Allen Institute is also interested in, like climate change and that sort of thing.
[2200.90 → 2205.02] Yeah, I mean, I guess you have to you have to start somewhere and put your efforts somewhere.
[2205.36 → 2212.72] But I think probably just assuming that you can get a PDF covers a large majority of cases.
[2212.72 → 2213.50] Is that right?
[2214.02 → 2214.36] Yes.
[2214.46 → 2226.40] And a lot of our effort is focused on partnerships with the major academic publishers on integration with some of the major preprint servers like Archive and Open Access Journals.
[2226.40 → 2235.38] And so if we get a high quality PDF, in most cases, we're able to fully index that content and make it discoverable to our users.
[2235.72 → 2243.26] You know, there are other challenges in terms of quality of extraction and how our models work to fully extract the content from different fields of science.
[2243.26 → 2253.76] But they tend to be, you know, fairly minor to the challenge of just getting access to the science and making it possible for scholars to discover it.
[2253.76 → 2272.66] Awesome. Well, I was curious, in addition to the Semantic Scholar product and the discovery tool, I think if I'm not mistaken, some of what has happened within Semantic Scholar has been open sourced in terms of things that people can use.
[2272.66 → 2278.78] So are things like pre-trained models and maybe tools, I think there's like a PDF parsing tool.
[2278.96 → 2279.44] Is that right?
[2279.86 → 2291.06] What's come out of Semantic Scholar in terms of open source things that maybe others can build on as they're thinking more about science and PDF parsing and those sorts of things?
[2291.44 → 2291.78] Absolutely.
[2291.78 → 2304.52] I think that's a great illustration of what makes AI2 and the Allen Institute for AI and Semantic Scholar special is that our mission is to have a positive impact on society at large.
[2305.08 → 2311.52] And so most of the things that we build that we think are valuable and unique are available as open source projects.
[2311.52 → 2322.52] So our knowledge graph, the aspects of it that we can release that are not restricted by the various agreements we have with publishers, is something we release as a public resource for the research community.
[2322.52 → 2329.18] This language model, Cyber that I mentioned earlier, is available on GitHub.
[2329.68 → 2333.02] And so we try to make it possible for others to build on our work.
[2333.18 → 2344.40] In addition to that, we have a public API where other projects can access Semantic Scholar features and our knowledge graph to further science in their own way.
[2344.40 → 2359.92] So I guess as we wind up and kind of bringing it back to a very practical side of things, I'm kind of curious as users, maybe they've heard the episode here, and they decide to try it out and get into some of the features we've been talking about.
[2360.14 → 2367.06] What should they be expecting on your roadmap ahead in the relatively near term over the next few years?
[2367.06 → 2376.50] You know, where do you expect to grow the product so that they can kind of take advantage of some of the things we've talked about as you've talked about these big problems that you're trying to tackle and expanding that?
[2376.84 → 2377.12] Absolutely.
[2377.62 → 2381.36] Our vision is to be a solution for information overload.
[2381.70 → 2392.04] So we'd like scholars to come back to us whenever they're trying to understand what the scientific literature says about some issue that is of interest to them.
[2392.04 → 2414.74] And so a lot of our work in the upcoming year and beyond is around making that discovery experience higher quality, adding new models and new AI-driven features that allow you to understand the highlights of a paper, to understand the intent, and to get a summary of it in a very succinct and high-quality way.
[2414.74 → 2421.78] And by doing that, we hope that we can make every semantic scholar user higher impact in their work.
[2421.88 → 2429.10] They'll be able to spend, if they still want to spend 15 hours a week, they can do that, but it'll be much higher quality of reading.
[2429.30 → 2434.96] If they want to spend less time so they can focus on other aspects of their work, we hope to enable that too.
[2434.96 → 2447.58] And so our research is really designed to make information overload a problem of the past and allow scholars to focus on what they can do best, which is delving into new unknown areas of science and creating breakthroughs.
[2448.02 → 2448.06] Awesome.
[2448.26 → 2457.74] Well, I'm excited about that future and definitely, you know, I'm excited about Semantic Scholar and a lot of the things that the Allen Institute for AI is doing.
[2457.74 → 2463.78] I know we had Joel Ruse on a previous episode talking about Allen NLP, which I've used personally.
[2463.98 → 2476.24] And, so thank you so much for working on Semantic Scholar, but also, you know, pass along our thanks to the Allen Institute for all the great work that they're doing and the contributions to the community.
[2476.74 → 2485.28] I think it's a really great thing to see so many efforts that have made contributions, practical contributions that people can use.
[2485.28 → 2488.84] So, yeah, thank you so much, and thank you for taking time to join us.
[2489.56 → 2489.64] Excellent.
[2489.80 → 2490.30] Thank you, Daniel.
[2490.40 → 2491.10] Thank you, Chris.
[2491.20 → 2491.74] It was a pleasure.
[2492.02 → 2492.38] Thank you.
[2494.86 → 2495.32] All right.
[2495.36 → 2497.98] Thank you for tuning into this episode of Practical AI.
[2498.26 → 2499.72] If you enjoyed the show, do us a favour.
[2499.84 → 2500.42] Go on iTunes.
[2500.54 → 2501.24] Give us a rating.
[2501.48 → 2503.36] Go in your podcast app and favourite it.
[2503.48 → 2506.18] If you are on Twitter or social network, share a link with a friend.
[2506.26 → 2508.62] Whatever you got to do, share the show with a friend if you enjoyed it.
[2508.92 → 2511.58] And bandwidth for change log is provided by Vastly.
[2511.58 → 2513.12] Learn more at fastly.com.
[2513.12 → 2516.54] And we catch our errors before our users do here at Change Log because of Rollbar.
[2516.80 → 2519.12] Check them out at rollbar.com slash change log.
[2519.24 → 2521.96] And we're hosted on Linde cloud servers.
[2522.30 → 2523.92] Head to linode.com slash change log.
[2524.02 → 2524.46] Check them out.
[2524.54 → 2525.36] Support this show.
[2525.78 → 2528.98] This episode is hosted by Daniel Whiten ack and Chris Benson.
[2529.40 → 2531.48] The music is by Break master Cylinder.
[2531.86 → 2535.30] And you can find more shows just like this at changelog.com.
[2535.38 → 2537.44] When you go there, pop in your email address.
[2537.44 → 2543.76] Get our weekly email keeping you up to date with the news and podcasts for developers in your inbox every single week.
[2544.00 → 2544.92] Thanks for tuning in.
[2545.08 → 2545.82] We'll see you next week.
