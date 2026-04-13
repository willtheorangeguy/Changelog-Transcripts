[0.00 → 8.66] Welcome to Practical AI.
[9.34 → 19.54] If you work in artificial intelligence, aspire to, or are curious how AI-related tech is changing the world, this is the show for you.
[20.24 → 24.92] Thank you to our partners at Fly.io, the home of changelog.com.
[24.92 → 32.38] Fly transforms containers into micro VMs that run on their hardware in 30 plus regions on six continents.
[32.80 → 35.44] So you can launch your app near your users.
[35.84 → 37.84] Learn more at Fly.io.
[44.38 → 48.64] Okay, friends, I'm here with Annie Sexton over at Fly.
[48.64 → 51.40] Annie, you know we use Fly here at changelog.
[51.40 → 52.40] We love Fly.
[52.40 → 55.26] Fly, it is such an awesome platform, and we love building on it.
[55.32 → 60.56] But for those who don't know much about Fly, what's special about building on Fly?
[60.80 → 65.62] Fly gives you a lot of flexibility, like a lot of flexibility on multiple fronts.
[66.04 → 71.54] And on top of that, you get, so I've talked a lot about the networking and that's obviously one thing.
[71.70 → 76.64] But there are various data stores that we partner with that are really easy to use.
[77.14 → 80.60] Actually, one of my favourite partners is Tigress.
[80.60 → 84.34] I can't say enough good things about them when it comes to object storage.
[84.54 → 88.70] I've never in my life thought I would have so many opinions about object storage, but I do now.
[88.96 → 96.80] Tigress is a partner of Fly, and it's S3 compatible object storage that basically seems like it's a CDN, but it's not.
[96.88 → 102.30] It's basically object storage that's globally distributed without needing to actually set up a CDN at all.
[102.30 → 105.20] It's like automatically distributed around the world.
[105.52 → 108.84] And it's also incredibly easy to use and set up.
[108.98 → 111.24] Like creating a bucket is literally one command.
[111.48 → 119.86] So it's partners like that I think are this sort of extra icing on top of Fly that really makes it sort of the platform that has everything that you need.
[120.32 → 122.30] So we use Tigress here at Changelog.
[122.42 → 123.86] Are they built on top of Fly?
[124.12 → 127.30] Is this one of those examples of being able to build on Fly?
[127.30 → 132.94] Yeah, so Tigress is built on top of Fly's infrastructure and that's what allows it to be globally distributed.
[133.36 → 141.80] I do have a video on this, but basically the way it works is whenever, like let's say a user uploads an asset to a particular bucket.
[141.94 → 145.86] Well, that gets uploaded directly to the region closest to the user.
[145.94 → 149.94] Whereas with a CDN, there's sort of like a centralized place where assets need to get copied to.
[150.04 → 153.82] And then eventually they get sort of trickled out to all the different global locations.
[153.82 → 158.14] Whereas with Tigress, the moment you upload something, it's available in that region instantly.
[158.58 → 162.08] And then it's eventually cached in all the other regions as well as it's requested.
[162.50 → 166.66] In fact, with Tigress, you don't even have to select which regions things are stored in.
[166.76 → 168.34] You just get these regions for free.
[168.60 → 171.78] And then on top of that, it is so much easier to work with.
[172.02 → 182.70] I feel like the way they manage permissions, the way they handle bucket creation, making things public or private is just so much simpler than other solutions.
[182.70 → 186.92] And the good news is that you don't actually need to change your code if you're already using S3.
[187.06 → 187.96] It's S3 compatible.
[188.16 → 190.86] So like whatever SDK you're using is probably just fine.
[190.90 → 192.40] And all you got to do is update the credentials.
[192.64 → 194.26] So it's super easy.
[194.92 → 195.22] Very cool.
[195.28 → 195.66] Thanks, Annie.
[195.82 → 198.12] So Fly has everything you need.
[198.34 → 204.64] Over 3 million applications, including ours here at Changelog, multiple applications have launched on Fly.
[204.64 → 217.16] Boosted by global anti-cast load balancing, zero configuration private networking, hardware isolation, instant wire guard VPN connections, push button deployments that scale to thousands of instances.
[217.54 → 219.46] It's all there for you right now.
[219.88 → 221.04] Deploy your app in five minutes.
[221.18 → 223.14] Go to fly.io.
[223.52 → 225.50] Again, fly.io.
[225.50 → 225.62] Fly.io.
[225.62 → 226.50] Fly.io.
[226.50 → 227.50] Fly.io.
[234.64 → 239.40] Welcome to another episode of the Practical AI Podcast.
[239.80 → 241.26] This is Daniel Whiten ack.
[241.38 → 247.00] I am CEO at Prediction Guard, where we're building a private Security AI platform.
[247.28 → 253.44] And I'm joined as always by Chris Benson, who is a principal AI research engineer at Lockheed Martin.
[253.70 → 254.40] How are you doing, Chris?
[254.66 → 255.56] Great today, Daniel.
[255.62 → 256.06] How are you?
[256.06 → 274.46] It's a beautiful, beautiful fall day and a good day to take a walk around the block and think about interesting AI things and clear your mind before getting back into some data collaboration, which is what we're going to talk about today.
[274.46 → 277.18] Chris, I don't know if you remember our conversation.
[278.18 → 287.86] It was just me on that one, but with Bing Soon Cha, who talked about broccoli AI, the type of AI that's healthy for organizations.
[288.78 → 298.86] And in that episode, he made a call-out to Angela, which was a big part of his solution that he was developing in a particular vertical.
[298.86 → 315.80] I'm really happy today that we have with us Ben Crenshaw, who is a machine learning engineer at Angela, and also David Bernstein, who is a developer advocate engineer working on building Angela and is still a label at Hugging Face.
[316.06 → 317.12] Welcome, David and Ben.
[317.56 → 317.92] Thank you.
[318.24 → 319.08] Great to be here.
[319.30 → 319.52] Hi.
[320.24 → 320.96] Thanks for having us.
[320.96 → 340.48] Yeah, so like I was saying, I think for some time, maybe if you're coming from a data science perspective, there's been tooling maybe around data that manages, you know, training data sets or evaluation sets or maybe Flops tooling and this sort of thing.
[341.02 → 345.24] And part of that has to do with preparation and curation of data sets.
[345.24 → 361.16] But I found interesting, I mentioned the previous conversation with Bing Soon, he talked a lot about collaborating with his sort of subject-matter experts in his company around the data sets he was creating for text classification.
[361.90 → 363.30] And that's where Angela came up.
[363.30 → 375.74] So I'm wondering if maybe one of you could talk a little bit at a higher level when you're talking about data collaboration in the context of the current kind of AI environment.
[375.94 → 378.06] What does that mean generally?
[378.36 → 386.16] And how would you maybe distinguish that from previous generations of tooling and maybe similar or different ways?
[386.16 → 403.02] So data collaboration, at least from our point of view, is kind of the collaboration between both the domain level experts that really have high domain knowledge, actually know what they're talking about in terms of the data, the inputs and the outputs that the models are supposed to give within their domain.
[403.02 → 408.26] And then you have the data scientists or the AI engineers and this side of the coin that are more technical.
[408.50 → 412.64] They know from a technical point of view what the models expect and what the models should output.
[412.64 → 421.08] And then the collaboration between them is now even higher because nowadays, you can actually prompt other names with natural language.
[421.52 → 427.22] And you actually need to ensure that both the models actually perform well and also the prompts and this kind of things.
[427.58 → 430.18] So the collaboration is even more important nowadays.
[430.84 → 437.16] And that's also still the case for text cat models and this kind of things which we also support within Angela.
[437.16 → 447.70] I guess maybe in the context of let's say there's a new team that's exploring the adoption of AI technology maybe for the first time.
[447.90 → 457.48] Maybe they're not coming from that data science background, the sort of heavy ML ops stuff, but maybe they've been excited by this latest wave of AI technologies.
[457.48 → 472.82] How would you go about helping them understand how their own data, the data that they would maybe collaborate on is relevant to and where that fits into the certain workflow?
[472.82 → 482.48] So yeah, imagine someone may be familiar with what you can do with ChatGPT or pasting in certain documents or other things.
[482.90 → 489.42] And now they're kind of wrestling through how to set up their own domain specific AI workflows in their organization.
[489.90 → 497.50] What would you kind of describe about how their own domain data and how collaborating around that fits into common AI workflows?
[497.50 → 504.70] Yeah, so something that I like to think about a lot around this subject is like machine learning textbooks.
[504.98 → 509.76] And they often talk about modelling a problem as well as building a model, right?
[510.16 → 512.30] There's a famous mama and matter cycle.
[512.76 → 518.14] And in that, when you model a problem, you're basically trying to explain and define the problem.
[518.14 → 525.22] So I have articles and I need to know whether they are a positive or negative rating.
[525.22 → 527.26] And I'm describing that problem.
[527.62 → 533.10] And then I'm going to need to describe that problem to a domain expert or an annotator through guidelines.
[533.92 → 541.44] And when I can describe that problem in such a way that the annotator or the domain expert answers that question clearly enough,
[541.72 → 544.04] then I know that that's a modelled and clear problem.
[544.36 → 546.90] And it's something that I could then take on to build a model around.
[548.32 → 550.04] In simple terms, it makes sense.
[550.04 → 559.12] And so I think when you're going into a new space like Generative AI, and you're trying to understand your business context around these tools,
[559.32 → 564.24] you can start off by modelling the problem in simple terms, by looking at the data and saying,
[564.66 → 566.96] OK, does this label make sense to these articles?
[567.28 → 573.38] If I sort all these articles down by these labels or by this ranking, are these the kinds of things I'm expecting?
[573.38 → 576.00] Starting off at quite low numbers, right?
[576.06 → 579.54] Like single articles and kind of building up to tens of hundreds.
[579.90 → 586.42] And as you do that, you begin to understand and also iterate on the problem and kind of change it and adapt it as you go.
[587.08 → 590.32] And once you've got up to a reasonable scale of the problem, you can then say, all right,
[590.68 → 593.38] this is something that a machine learning model could learn.
[593.38 → 608.28] I guess on that front, maybe one of the big confusions that I've seen floating around these days is the kind of data that's relevant to some of these workflows.
[608.60 → 616.74] So it might be easy for people to think about a labelled data set for a text classification problem, right?
[616.76 → 618.18] Like here's this text coming in.
[618.24 → 621.42] I'm going to label it spam or not spam or in some categories.
[621.42 → 631.26] But I think sometimes a sentiment that I've got very often is, hey, our company has this big file store, right, of documents.
[631.92 → 640.88] And somehow I'm going to, you know, fine tune, quote unquote, generative model with this, just this blob of documents.
[640.88 → 643.86] And then it will perform better for me.
[644.00 → 647.76] And there are two elements of that are kind of mushy.
[647.76 → 651.62] One is like, well, to what end for what task, right?
[651.72 → 652.68] What are you trying to do?
[652.76 → 656.22] And then also how you curate that data then really matters.
[656.48 → 668.92] Is this a sentiment that you all are seeing or how for this latest wave of models, like how would you describe if a company has a bunch of documents, and they're in this situation?
[668.92 → 673.54] They're like, hey, we know we have data, and we know that these models can get better.
[674.32 → 679.04] And maybe we could even create our own private model with our own domain of data.
[679.42 → 688.80] What would you walk them through to explain where to start with that process and how to start curating their data, maybe in a less general way, but towards some end?
[688.80 → 700.42] I think in these scenarios, it's always good to first establish a baseline or a benchmark, because what we often see is that people come to us or come to like the open source space.
[700.52 → 703.08] They say, OK, we really want to fine tune a model.
[703.20 → 710.94] We really want to do like a super extensive rack pipeline with all the bells and whistles included and then kind of start working on these documents.
[710.94 → 715.60] But what we often see is that they don't even have a bench line to actually start with.
[716.18 → 717.70] So that's normally what we recommend.
[717.94 → 725.10] Also, whenever you work with a rack pipeline, ensure that all the documents that you index are actually properly indexed, properly chunked.
[725.24 → 737.10] Whenever you actually execute a pipeline, and you would store these retrieved documents or these based on the question and the queries in RGLR or any other data annotation tool,
[737.10 → 744.16] you can actually have a look at the documents, see if they make sense, see if the retrieval makes sense, but also if the generated output makes sense.
[744.56 → 750.82] And then whenever you have that baseline set up, from there, actually start iterating and kind of making additions to your pipeline.
[750.96 → 755.48] Shall I add re-ranking potentially to the retrieval if the retrieval isn't functioning properly?
[755.90 → 758.32] Shall I add a fine-tuned version of the model?
[758.46 → 764.56] Should I switch from the latest LAMA model of 3 billion to 7 billion or this kind of things?
[764.56 → 772.90] And then from there on, you can actually consider maybe either fine-tuning a model if that's actually needed or fine-tuning one of the retrievers or this kind of things.
[773.54 → 780.88] As you're saying that, as you're speaking from this kind of profound expertise you have, and I think a lot of folks really have trouble just getting started.
[781.22 → 787.94] And you asked some great questions there, but I think some of those are really tough for someone who's just getting into it,
[787.98 → 791.30] like which way to go and some of the selections that you would go with that.
[791.30 → 800.72] But could you talk a little bit about, kind of go back over the same thing, but kind of make up a little workflow that's kind of hands-on on just like you might see this,
[800.98 → 807.22] and this is how I would decide that, just for a moment, just so people can kind of grasp kind of the thought process you're going.
[807.28 → 812.64] Because you kind of described a process, but if you could be a little bit more descriptive about that.
[812.64 → 818.44] But I think when I talk to people, once they get going, they kind of go to the next step and go to the next step and go to the next step.
[818.50 → 823.40] But the first four or five big question marks at the beginning, they don't know which one to handle.
[824.14 → 828.40] I can add some practical steps onto that I've worked with in the past.
[828.58 → 829.86] That'd be fantastic.
[829.86 → 841.34] Yeah, so one thing that you can do that is really straightforward is actually to write down a list of the kinds of questions that you're expecting your system to answer.
[841.86 → 847.64] And you can get that list by speaking to domain experts, or if you are a domain expert, you can write it yourself, right?
[848.44 → 850.76] And it doesn't need to be an extensive, exhaustive list.
[850.82 → 852.80] It can be quite a small starting set.
[852.80 → 864.00] You can then take those questions away and start to look at documents or pools and sections of documents from this lake that you potentially have and associate those documents with those questions.
[864.40 → 871.12] And then start to look if a model can answer those questions with those documents.
[871.12 → 884.58] In fact, by not even building anything, by starting to use, say, Chat TBT or Hugging Chat or any of this kind of interfaces, and just seeing this very, very low, simple benchmark, see, is that feasible?
[885.34 → 891.06] Whilst at the same time, starting to ask yourself, can I, as a domain expert, answer this?
[891.62 → 894.34] And that's kind of where Argyll comes in at the very first step.
[894.34 → 903.58] So you start to put these documents in front of people with those questions, and you start to search through those documents and say to people, can you answer this question?
[903.70 → 909.40] Or here's an answer from a model to this question in a very small setting.
[909.88 → 913.22] And you start to get basic early signals of quality.
[914.14 → 918.14] And from there, you would start to introduce proper retrieval.
[918.38 → 924.02] So you would scale up your doc, you would take all of your documents, say you had 100 documents,
[924.02 → 925.68] associated with your 10 questions.
[926.10 → 934.14] You put all those 100 documents in an index and iterate over your 10 questions and see, okay, are the right documents aligning with the right questions here?
[934.74 → 938.56] Then you start to scale up your documents and make it more and more of a real world situation.
[939.22 → 940.94] You would start to scale up your questions.
[941.44 → 943.88] You could do both of these synthetically.
[943.88 → 949.16] And then if you still started to see positive signals, you could start to scale.
[949.70 → 955.00] And if you start to see negative signals, I'm no longer getting the right documents associated with the right questions.
[955.68 → 961.40] I personally would always start from the simplest levers in a RAG setup.
[961.40 → 966.20] And what I mean there is that you have a number of different things that you can optimize.
[966.74 → 967.90] So you have retrieval.
[968.36 → 970.32] You can optimize it semantically.
[970.90 → 974.16] Or you can optimize it in a rule-based retrieval.
[974.70 → 977.04] You can optimize the generative model.
[977.46 → 978.66] You can optimize the prompt.
[978.66 → 987.48] And the simplest levers are the rule-based retrieval, the word search, and then the semantic search.
[987.74 → 990.06] So I would, first, add a hybrid search.
[990.50 → 994.56] What happens if I make sure that there's an exact match in that document for the word in my query?
[995.04 → 998.20] Does that improve my results?
[998.72 → 1001.36] And then I would just move through that process, basically.
[1001.36 → 1016.10] What's up, friends?
[1016.20 → 1021.68] I'm here with a friend of mine, a good friend of mine, Michael Greenwich, CEO and founder of Works.
[1022.60 → 1031.18] Works is the all-in-one enterprise SSO and a lot more solution for everyone from a brand-new startup to an enterprise.
[1031.36 → 1033.76] And all the AI apps in between.
[1034.22 → 1039.08] So, Michael, when is too early or too late to begin to think about being enterprise-ready?
[1039.48 → 1042.80] It's not just a single point in time where people make this transition.
[1043.14 → 1044.90] It occurs at many steps of the business.
[1045.28 → 1049.94] Enterprise single sign-on, like SAML, auth, you usually don't need that until you have users.
[1050.40 → 1052.14] You're not going to need that when you're getting started.
[1052.52 → 1053.92] And we call it an enterprise feature.
[1054.20 → 1059.42] But I think what you'll find is there are companies, when you sell to like a 50-person company, they might want this.
[1059.70 → 1061.26] Especially if they care about security.
[1061.62 → 1063.06] They might want that capability in it.
[1063.22 → 1066.78] So, it's more of like SMB features even if they're tech-forward.
[1067.16 → 1072.08] At Works, we provide a ton of other stuff that we give away for free for people earlier in their lifecycle.
[1072.30 → 1073.32] We just don't charge you for it.
[1073.54 → 1079.30] So, that Auth Kit stuff I mentioned, that identity service, we give that away for free up to a million users.
[1079.64 → 1081.06] One million users.
[1081.06 → 1086.28] And this competes with Auth0 and other platforms that have much, much lower free plans.
[1086.44 → 1088.64] I'm talking like 10,000, 50,000.
[1088.84 → 1090.04] Like, we give you a million free.
[1090.28 → 1094.70] Because we really want to give developers the best tools and capabilities to build their products faster.
[1095.04 → 1096.52] You know, and to go to market much, much faster.
[1096.82 → 1100.66] And where we charge people money for the service is on these enterprise things.
[1100.66 → 1104.98] If you end up being successful and grow in scale-up market, that's where we monetize.
[1105.08 → 1107.10] And that's also when you're making money as a business.
[1107.42 → 1110.34] So, we really like to align, you know, our incentives across that.
[1110.74 → 1114.28] So, we have people using Auth Kit that are brand-new apps just getting started.
[1114.70 → 1115.90] Companies in Y Combinator.
[1115.90 → 1117.08] Side projects.
[1117.20 → 1118.12] Hackathon things.
[1118.52 → 1120.50] You know, things that are not necessarily commercial focused.
[1120.76 → 1121.48] But could be.
[1121.62 → 1121.92] Someday.
[1122.20 → 1125.16] They're kind of future-proofing their tech stack by using Works.
[1125.70 → 1128.64] On the other side, we have companies much, much later that are huge.
[1128.88 → 1131.40] Who typically don't like us talking about them.
[1131.54 → 1132.38] Their logos, you know.
[1132.66 → 1134.80] Because they're big, big customers.
[1135.34 → 1137.28] But they say, hey, we tried to build this stuff.
[1137.32 → 1138.74] Or we have some existing technology.
[1139.02 → 1140.44] But we're sort of unhappy with it.
[1140.68 → 1142.38] The developer that built it maybe has left.
[1142.38 → 1146.64] I was talking last week with a company that does over a billion in revenue each year.
[1147.02 → 1150.96] And their SKIM connection, the user provisioning, was written last summer by an intern.
[1151.10 → 1152.86] Who's no longer, obviously, at the company.
[1152.98 → 1154.06] And the thing doesn't really work.
[1154.32 → 1155.70] And so, they're looking for a solution for that.
[1155.80 → 1157.62] So, there's a really wide spectrum.
[1157.82 → 1159.78] We'll serve companies that are in a you know.
[1159.92 → 1162.18] Their office is in a coffee shop or their living room.
[1162.24 → 1166.36] All the way through, they have a, you know, their own building in downtown San Francisco or New York or something.
[1166.66 → 1167.60] And it's the same platform.
[1167.86 → 1168.54] Same technology.
[1168.70 → 1170.08] Same tools on both sides.
[1170.08 → 1171.48] The volume is obviously different.
[1171.48 → 1175.60] And sometimes the way we support them from a kind of customer support perspective is a little bit different.
[1175.92 → 1176.58] Their needs are different.
[1176.84 → 1178.60] But same technology, same platform.
[1178.90 → 1179.94] Just like AWS, right?
[1179.98 → 1181.82] You can use AWS and pay them $10 a month.
[1181.90 → 1183.94] You can also pay them $10 million a month.
[1184.30 → 1184.76] Same product.
[1184.96 → 1185.82] Or more, for sure.
[1185.86 → 1186.18] Or more.
[1186.94 → 1192.96] Well, no matter where you're at on your enterprise-ready journey, Works has a solution for you.
[1193.32 → 1199.04] They're trusted by Perplexity, Copy.ai, Loom, Tercel, Indeed, and so many more.
[1199.04 → 1203.08] You can learn more and check them out at WorkOS.com.
[1203.14 → 1206.30] That's W-O-R-K-O-S dot com.
[1206.64 → 1209.12] Again, Works dot com.
[1209.12 → 1238.04] I'm guessing that you all, you know, the fact that you're supporting all of these use cases on top of Angela on the data side makes me think, like you say, there are so many things to optimize in terms of that RAG process.
[1238.04 → 1250.48] But there's also so many AI workflows that are being thought of, whether that be, you know, code generation or assistance or, you know, content generation, information extraction.
[1250.80 → 1252.44] But then you kind of go beyond that.
[1252.78 → 1254.80] David, you mentioned text classification.
[1255.34 → 1257.26] And, of course, there's image use cases.
[1257.26 → 1281.64] So I'm wondering from you all, do the at this point, you know, one of the things Chris and I have talked about on the show a bit is, you know, we're still big proponents and, you know, believe that in enterprises, a lot of times there is a lot of mixing of, you know, rule-based systems and more kind of traditional, I guess, if you want to think about it that way, machine learning and smaller models.
[1281.64 → 1289.66] And then bringing in these larger Gen AI models as kind of orchestrators or, you know, query layer things.
[1289.86 → 1292.20] And that's a story we've been kind of telling.
[1292.34 → 1300.98] But I think it's interesting that we have both of you here in the sense that, like, you really, I'm sure there are certain things that you don't or can't track about what you're doing.
[1300.98 → 1327.52] But just even anecdotally, out of the users that you're supporting on Angela, what have you seen in terms of what is the mix between those, you know, using Angela for this sort of maybe what people would consider traditional data science type of models like text classification or image classification type of things and these maybe newer workflows like RAG and other things.
[1327.52 → 1357.50] How do you see that balance?
[1357.52 → 1357.92] properly.
[1357.92 → 1361.02] We're mostly trained on English text.
[1361.54 → 1363.62] And that was also one of their issues.
[1363.90 → 1377.92] And what they did was actually a huge classification and generation pipeline combining a lot of these techniques where they would initially get an email in that they would classify to a certain category.
[1378.16 → 1384.18] Then based on the category, they would kind of define what kind of email template, what kind of prompt template they would use.
[1384.18 → 1395.50] Then based on the prompt template, they would kind of start generating and composing one of these response emails that you would expect for like a customer query requests coming in for the healthcare insurance companies.
[1395.50 → 1402.88] And then in order to actually ensure that the formatting and phrasing and the German language was applied properly.
[1402.88 → 1407.42] They would then be based on the prompt, they would then be based on the prompt, regenerate the email once more.
[1407.42 → 1411.90] So prompting an LLM to kind of improve the quality of the initial proposed output.
[1412.32 → 1424.42] And then after all of these different steps of classification of retrieval, augmented generation of an initial like generation and a regeneration, they would then end up with their eventual output.
[1424.42 → 1429.42] So what we see is that all of these techniques are normally combined.
[1429.42 → 1443.44] And also a thing that we are strong believers in is that whenever there is a smaller model or an easier approach applicable, why not go for that instead of using one of these huge, large language models.
[1443.80 → 1450.20] So if you can just classify is this relevant or is this not relevant and based on that, actually decide what to do.
[1450.24 → 1451.68] That makes a lot of sense.
[1451.68 → 1476.14] And also one of the interesting things that I've seen one of these open source platforms, Haystack, out there using is also this query classification pipeline where they would classify incoming queries as either a key terminology search, a question query, or actually a phrase for an LLM to actually start prompting an LLM.
[1476.52 → 1480.30] And based on that, actually redirect all of their queries to the correct model.
[1480.30 → 1483.48] And that's also an interesting approach that we've seen.
[1484.14 → 1485.04] Quick follow up on that.
[1485.28 → 1490.48] And it's just something I wanted to draw out because we've drawn it out across some other episodes a bit.
[1490.68 → 1495.12] You were just making a recommendation, kind of go for the smaller model versus the larger model.
[1495.74 → 1499.90] Could you, for people trying to follow and, you know, there's, you know, the divergent mindsets.
[1500.00 → 1504.34] Could you take just a second and say why you would advocate for that?
[1504.42 → 1508.10] What the benefit, what the virtue is in the context of everything else?
[1508.10 → 1513.82] I would say, like, smaller models are generally hostable by yourself.
[1513.96 → 1514.80] So it's more private.
[1515.46 → 1518.10] Smaller models, they are more cost-efficient.
[1518.94 → 1522.72] Smaller models can also be fine-tuned easier to your specific use case.
[1522.72 → 1529.12] So even what we see a lot of people coming to us about is actually fine-tuning LLMs.
[1529.52 → 1539.74] But even the big companies out there with huge amounts of money and resources and dedicated research teams still have, like, difficulties on fine-tuning LLMs.
[1539.74 → 1554.52] So whenever you, instead of, within your retrieval augmented generation pipeline, fine-tune, like, LLM for the generation part, you can actually choose to fine-tune one of these retrieval models that you can actually fine-tune on consumer-grade hardware.
[1554.78 → 1559.88] You can actually fine-tune it very easily on any arbitrary data scientist developer device.
[1559.88 → 1566.48] And then instead of, like, having to deploy anything on one of the cloud providers, you can start with that.
[1566.88 → 1583.78] And in a similar reasoning for a RAC pipeline, whenever you provide an LLM with garbage within such a retrieval augmented generation pipeline, you actually also ensure that there's less relevant content and the output of the LLM is also going to be worse.
[1583.78 → 1589.80] Yeah, I've seen a lot of cases where I think it was Travis Fisher who was on the show.
[1590.04 → 1593.42] He advocated for this hierarchy of how you should approach these problems.
[1594.00 → 1599.06] And there's, like, you know, maybe seven things on his hierarchy that you should try before fine-tuning.
[1599.32 → 1603.28] And I think in a lot of cases I've seen people maybe jump to that.
[1603.50 → 1610.52] They're like, oh, I forget which one of you said this, but, you know, this naive RAG approach didn't get me quite there.
[1610.52 → 1617.38] So now I need to fine-tune when in reality there's sort of a huge number of things in between those two places.
[1617.60 → 1623.18] And you might end up just getting a worse performing model depending on how you go about to fine-tune.
[1623.88 → 1634.34] One of the things, David, you kind of walked through these different, the example of the specific company that had these workflows that involved a variety of different operations,
[1634.34 → 1643.66] which I assume, you know, to Ben, you're mentioning earlier, starting with a test set and that sort of thing and how to think about the tasks.
[1644.06 → 1648.32] I'm wondering if you can specifically now talk just a little bit about Aria.
[1648.74 → 1653.28] Specifically, people might be familiar generally with, like, data annotation.
[1653.28 → 1662.52] They might be familiar, you know, maybe even with how to upload some data to, quote, fine-tune some of these models in an API sense
[1662.52 → 1668.20] or maybe even in a more advanced way with Laura or something like that.
[1668.28 → 1676.08] But could you take a minute and just talk through kind of Aria's approach to data annotation and data collaboration?
[1676.08 → 1681.36] And, like, it's kind of hard on a podcast because we don't have a visual to show for people.
[1681.56 → 1688.78] But as best you can, you know, help people to imagine, you know, if I'm using Aria to do data collaboration,
[1688.78 → 1693.94] what does that look like in terms of what I would set up and who's involved?
[1694.14 → 1695.26] What actions are they doing?
[1695.34 → 1696.06] That sort of thing.
[1696.60 → 1699.12] Aria, there are two sides to it, right?
[1699.12 → 1705.22] So there's a Python SDK, which is intended for the AI and machine learning engineer.
[1705.22 → 1709.82] And there's a UI, which is intended for your domain expert.
[1710.82 → 1718.48] In reality, the engineers often also use the UI and you kind of iterate on that as you would because it gives you a representation of your task.
[1718.96 → 1720.36] But there's these two sides.
[1721.10 → 1722.28] The UI is kind of lightweight.
[1722.72 → 1725.98] It can be deployed in a Docker container or on Hugging Face spaces.
[1726.26 → 1727.42] It's really easy to spin up.
[1727.42 → 1736.64] And the SDK is really about describing a feedback task and describing the kind of information that you want.
[1737.02 → 1740.80] So you use Python classes to construct your data set settings.
[1740.80 → 1747.92] You'll say, OK, my fields are a piece of text, a chat or an image.
[1747.92 → 1751.54] And the questions are text question.
[1751.90 → 1755.72] So like some kind of feedback, a comment, for example, a label question.
[1756.50 → 1763.80] So positive or negative labels, for example, a rating, let's say between one and five or a ranking.
[1764.30 → 1767.30] So example one is better than example two.
[1767.38 → 1769.42] And you can rank a set of examples.
[1769.42 → 1777.68] And with that definition of a feedback task, you can create that on your server, in your UI.
[1777.90 → 1783.28] And then you can push what we call records, your samples, into that data set.
[1783.84 → 1786.32] And then they'll be shown within the UI.
[1787.00 → 1788.90] And your annotator can see all the questions.
[1789.02 → 1791.50] They'll have nice descriptions that were defined in the SDK.
[1792.08 → 1796.58] They can tweak and kind of change those as well if you need in the UI because that's a little bit easier.
[1796.58 → 1799.78] You can distribute the task between a team.
[1799.96 → 1805.98] So you can say, OK, this record will be accepted once we have at least two reviews of it.
[1806.48 → 1809.34] You can say that some questions are required and some aren't.
[1809.54 → 1811.28] And they can skip through some of the questions.
[1812.16 → 1816.70] The UI has loads of keyboard shortcuts with numbers and arrows and returns.
[1816.82 → 1819.00] So you can move through it really fast.
[1819.08 → 1820.16] It's kind of optimized for that.
[1820.56 → 1822.10] And different sort of screen sizes.
[1822.10 → 1827.86] One thing we're starting to see is that as LLMs get perfect at quite long documents,
[1827.96 → 1835.86] some of the stuff that they're dealing with is like a multipage document or a really detailed image and then a chat conversation.
[1836.36 → 1839.86] And then we want like a comment and a ranking question.
[1840.34 → 1842.46] So it's like a lot of information in the screen.
[1842.46 → 1845.50] So the UI kind of scales a bit like an IDE.
[1845.90 → 1849.78] So you can drag it around to give yourself enough width to see all this stuff.
[1850.24 → 1854.26] And then you can move through it in a reasonably efficient way with the keyboard shortcuts and stuff.
[1854.84 → 1855.16] Interesting.
[1855.52 → 1862.22] And what do you see as kind of the backgrounds of the roles of people that are using this tool?
[1862.22 → 1869.56] Because one of the interesting things from my perspective, especially with this kind of latest wave,
[1869.66 → 1876.08] is there's maybe less data scientists, kind of AI people that their background,
[1876.24 → 1881.34] and more software engineers and just non-technical domain experts.
[1881.76 → 1885.76] So how do you kind of think about the roles within that?
[1885.84 → 1888.82] And what are you seeing in terms of who's using the system?
[1888.82 → 1895.28] For us, I think it's, yeah, from the SDK Python side, it's really still developers.
[1896.02 → 1902.68] And then from the UI side, it's like anyone in the team that needs to have some data labelled with domain knowledge.
[1903.32 → 1906.18] Often these are also going to be like the AI experts.
[1906.76 → 1912.22] And one of the cool things is that whenever an AI expert actually sets up a data set,
[1912.28 → 1913.68] besides these fields and questions,
[1913.68 → 1918.86] they can actually come up with some interesting features that they can add on top of the data set.
[1919.30 → 1922.12] They are also able to add like semantic search,
[1922.50 → 1927.18] like attach records or semantic representation of the records to one of the records,
[1927.34 → 1931.60] which actually enables the users within the UI to label way more efficiently.
[1931.92 → 1932.62] So for example,
[1933.26 → 1938.64] if someone sees a very representative example of something that's bad within their data set,
[1938.92 → 1942.14] they can do a semantic search, find the most similar documents,
[1942.14 → 1945.56] and then continue with the labelling on top of that.
[1945.94 → 1949.84] Besides that, you can also, for example, filter based on model certainties.
[1950.22 → 1955.28] So let's say that your model is very uncertain about an initial prediction that you have within your UI.
[1955.50 → 1960.20] And it's fascinating for the domain expert or for the data scientist to go
[1960.20 → 1965.56] and have a look at that specific record or at this range of uncertainties.
[1965.56 → 1974.50] And then based on that, the labelling or like the data curation or whatever you would like to call it becomes way more engaging and way more interesting.
[1975.22 → 1976.18] And on top of that,
[1976.22 → 1983.34] another thing that we are starting to explore is actually using this AI feedback and synthetic data within our JLA as well.
[1983.76 → 1987.04] And that's actually one of the other products that we're working on.
[1987.04 → 1988.66] And it's called this C-label.
[1989.20 → 1996.14] So nowadays, what you can do with LLMs is also actually use LLMs to evaluate questions, for example,
[1996.38 → 1999.72] to evaluate whether something is labelled A, B, or C,
[2000.22 → 2003.10] or whether something is a good or bad response.
[2003.24 → 2007.30] And you see all kinds of tools, open source tools out there.
[2007.30 → 2011.06] And that's also a thing that we are looking at for integrating with the UI,
[2011.46 → 2015.50] where instead of doing this more from a data science SDK perspective,
[2016.12 → 2022.24] users without any technical knowledge would actually be able to tweak these guidelines that Ben highlighted earlier
[2022.24 → 2025.84] and then say, okay, maybe instead of taking this into account,
[2025.94 → 2033.02] you should focus a bit more on the harm that potentially is within your data or the risks that are within your data.
[2033.02 → 2037.86] And then you would be able to prompt an LLM once again to kind of label your data.
[2038.08 → 2041.60] And then you wouldn't directly need the Python SDK anymore.
[2041.88 → 2046.12] I was thinking about, as you were describing that, I work at a large organization,
[2046.46 → 2053.76] and we certainly have a lot of domain experts in the organization I work at that are either non-technical or semi-technical.
[2054.36 → 2058.32] And as users, they will sometimes find it intimidating, you know,
[2058.36 → 2060.82] kind of getting into all this as they're starting a project.
[2060.82 → 2066.98] Could you talk a little bit about what it's like for a non-technical person to sit down with Angela
[2066.98 → 2069.46] and start to work productively?
[2069.62 → 2071.84] What is that experience like for them?
[2072.18 → 2075.22] Because it's one thing, like, the technical people kind of just know.
[2075.32 → 2076.10] They dive into it.
[2076.14 → 2076.94] They're going to use the SDK.
[2077.20 → 2078.36] They've used other SDKs.
[2078.94 → 2082.58] But there can be a bit of hand-holding for people who are not used to that.
[2082.68 → 2087.38] Could you describe the user experience for that non-technical subject-matter expert coming in
[2087.38 → 2094.34] and what labelling is like and just kind of paint a picture of words on what their experience might be like?
[2095.10 → 2095.20] Yeah.
[2095.36 → 2102.98] I mean, one thing I guess I'd start off by saying is that Angela is kind of the latest iteration of a problem
[2102.98 → 2106.38] that has existed for a long time in machine learning and data science, right?
[2106.64 → 2109.10] About collecting feedback from domain experts.
[2109.10 → 2115.54] And it's kind of gone through spreadsheets and various other tools that were substandard
[2115.54 → 2122.18] and terrible user experiences where domain experts were asked for information.
[2122.82 → 2123.98] That information was extracted.
[2124.68 → 2129.22] And then models have been trained really poorly on that information.
[2129.62 → 2133.80] So as a field, we kind of know that it's something that we have to take really seriously.
[2133.80 → 2136.70] And that's kind of what Angela is built on top of, right?
[2136.74 → 2138.88] That's part of our DNA as a product.
[2139.04 → 2144.62] It's like optimizing the feedback process as a user experience problem.
[2145.50 → 2151.74] And so when the user sits down to use Angela, the intention is that all the information
[2151.74 → 2156.34] should be right there in front of them inside their single record view.
[2156.90 → 2161.22] So what that means is they've got a set of guidelines that are edited in Markdown.
[2161.22 → 2167.48] They can contain images, links to various pages or other external documents if they need.
[2167.56 → 2168.96] And they can just kind of scroll through that.
[2169.10 → 2169.50] It's always there.
[2169.66 → 2170.60] It's always available.
[2171.20 → 2173.68] They've then also got like basic metrics.
[2173.68 → 2177.18] So they'll know how many records they've got left, how many they've labelled.
[2177.66 → 2181.04] They can view that kind of team status and see what's going on.
[2181.42 → 2185.34] And then on the left, they have their fields, which they can scroll through.
[2185.48 → 2187.92] And on the right, they'll have a set of questions.
[2187.92 → 2194.02] As I said, they can move through these in keyboard shortcuts, and they can switch the view so that
[2194.02 → 2199.08] they can scroll kind of infinitely, or they can move into a kind of page swiping, which
[2199.08 → 2203.00] yeah, if you're looking at tiny records with like a couple of lines, and you're just
[2203.00 → 2206.04] assigning a symbol label to, you can do that in bulk.
[2206.40 → 2211.82] So as we said, you could use a semantic search, give me all the records that are similar to
[2211.82 → 2213.46] this one, and I'll bulk label those.
[2213.46 → 2217.90] Or you could search for terms inside those records, and you can bulk label those.
[2218.80 → 2221.16] And then once you're finished, you'll know about it.
[2221.68 → 2227.90] And one of the interesting things that I've done personally quite is often sit together with the
[2227.90 → 2233.66] domain experts and their AI engineers to kind of walk them through how to configure our JLA
[2233.66 → 2235.88] most usefully for both of them.
[2236.30 → 2241.58] And then the domain experts come with a lot of things to the table, like I want to see this
[2241.58 → 2242.66] specific representation.
[2242.94 → 2243.94] What if we could do this?
[2244.02 → 2244.96] What if we could do that?
[2245.66 → 2248.34] Then the AI engineers think about like the data side of things.
[2248.50 → 2251.30] Is this possible from our point of view, from our side?
[2251.48 → 2257.24] And then me as a mediator, so to say, can I make the most out of the JLA configuration?
[2257.60 → 2263.38] And that's also how we see this collaboration process going, where domain experts really work
[2263.38 → 2267.64] together also with AI engineers, because AI engineers or machine learning engineers actually
[2267.64 → 2272.96] know what's possible from the data, what it means to get high quality data for fine-tuning
[2272.96 → 2273.28] model.
[2273.58 → 2278.60] Because whenever a domain engineer comes up with something that's useful for them in
[2278.60 → 2283.16] terms of labelling, doesn't mean necessarily that it's actually proper data that's going
[2283.16 → 2286.24] to come out of their in terms of fine-tuning a model.
[2286.24 → 2290.36] And that's also a part of, I guess, the collaboration that we're talking about.
[2305.60 → 2306.54] What's up, friends?
[2306.80 → 2308.44] I've got something exciting to share with you today.
[2308.66 → 2312.78] A sleep technology that's pushing the boundaries of what's possible in our bedrooms.
[2312.78 → 2318.06] Let me introduce you to 8 Sleep and their cutting edge Pod 4 Ultra.
[2318.60 → 2320.38] I haven't gotten mine yet, but it's on its way.
[2320.72 → 2322.18] I'm literally counting the days.
[2322.66 → 2325.18] So what exactly is the Pod 4 Ultra?
[2325.68 → 2330.50] Imagine a high-tech mattress cover that you can easily add to any bed.
[2330.74 → 2332.24] But this isn't just any cover.
[2332.54 → 2337.92] It is packed with sensors, heating and cooling elements, and it's all controlled by sophisticated
[2337.92 → 2339.32] AI algorithms.
[2339.32 → 2345.94] It's like having a sleep lab, a smart thermostat, and a personal sleep coach all rolled into
[2345.94 → 2346.94] a single device.
[2347.14 → 2352.84] It uses a network of sensors to track a wide array of biometrics while you sleep, sleep
[2352.84 → 2357.08] stages, heart rate variability, respiratory rate, temperature, and more.
[2357.34 → 2361.84] It uses precision temperature control to regulate your body's sleep cycles.
[2361.84 → 2368.40] It can cool you down to a chilly 55 degrees Fahrenheit or warm you up to a good, nice solid
[2368.40 → 2370.04] temperature of 110 Fahrenheit.
[2370.34 → 2374.04] And it does this separately for each side of the bed.
[2374.38 → 2378.14] This means you and your partner can have your own ideal sleep temperatures.
[2378.90 → 2385.80] But the really cool part is that the Pod uses AI, and it uses machine learning to learn your
[2385.80 → 2387.20] sleep patterns over time.
[2387.20 → 2391.86] And it uses this data to automatically adjust the temperature of your bed throughout the
[2391.86 → 2393.72] night according to your body's preferences.
[2394.06 → 2399.20] Instead of just giving you some stats, it understands them, and it does something about it.
[2399.58 → 2402.72] Your bed literally gets smarter as you sleep over time.
[2403.12 → 2406.88] And all this functionality is accessible through a comprehensive mobile app.
[2406.98 → 2412.12] You get sleep analytics, trends over time, and you even get a daily sleep fitness score.
[2412.12 → 2414.08] Now, I don't have mine yet.
[2414.24 → 2415.00] It is on its way.
[2415.30 → 2417.06] Thanks to our friends over at 8sleep.
[2417.46 → 2420.44] And I'm literally counting the days I get it because I love this stuff.
[2420.84 → 2424.72] But if you're ready to take your sleep and your recovery to the next level, head over
[2424.72 → 2432.34] to 8sleep.com slash practical AI and use our code practical AI to get 350 bucks off your
[2432.34 → 2434.24] very own Pod 4 Ultra.
[2434.66 → 2436.70] And you can try it free for 30 days.
[2436.96 → 2440.28] I don't think you want to send it back, but you can if you want to.
[2440.28 → 2445.56] They're currently shipping to the US, Canada, United Kingdom, Europe, and Australia.
[2445.98 → 2449.48] Again, 8sleep.com slash practical AI.
[2449.48 → 2474.80] I want to maybe double-click on something that, David, you just said in sort of passing,
[2474.80 → 2476.74] which I think is quite significant.
[2477.06 → 2480.00] And I don't know if some people might have caught it.
[2480.06 → 2484.10] But when you were talking about the still label, you also talked about AI feedback.
[2484.60 → 2486.74] So AI feedback and synthetic data.
[2486.92 → 2489.36] So I'd love to get into those topics a little bit.
[2489.42 → 2492.68] Maybe first coming from the AI feedback side.
[2492.90 → 2498.38] I think this is fascinating because, you know, Ben, you talked about how this is a
[2498.38 → 2504.00] kind of more general problem that people have been looking at in various ways from various
[2504.00 → 2508.94] perspectives for a long time in terms of this data collaboration labelling piece.
[2508.94 → 2516.40] But there is this kind of very interesting element now where we have the ability to utilize these
[2516.40 → 2525.38] very powerful, maybe general purpose instruction following type of models to actually act as
[2525.38 → 2533.86] labels within the system or at least generate, you know, drafts of labels or feedback or even
[2533.86 → 2538.22] preferences and scores and all of those sorts of things.
[2538.22 → 2541.32] So I'm wondering if one of you could speak to that.
[2541.82 → 2548.60] Some people might find this kind of strange that we're kind of giving feedback to AI systems
[2548.60 → 2553.78] with AI systems, which seems circular and maybe like, why would that work?
[2553.86 → 2558.38] Or just sort of maybe that's kind of produces some weird feelings for people.
[2558.38 → 2561.26] But I think it is a significant thing that is happening.
[2561.84 → 2565.96] And so, yeah, either of you would want to kind of dive into that.
[2566.06 → 2568.50] What does it specifically mean in AI feedback?
[2568.74 → 2571.58] How are you seeing that being used most productively?
[2572.24 → 2577.90] So when we create a data set, either manually or with AI feedback or AI generation,
[2577.90 → 2581.64] we have all the information there to understand the problem.
[2581.80 → 2582.68] We have a set of guidelines.
[2583.02 → 2585.28] We have a set of labels, definitions of those labels,
[2585.52 → 2587.54] with documents and definitions of those documents.
[2588.06 → 2591.98] We give those to a manual annotator, or we'll go out and collect those documents
[2591.98 → 2594.44] and we'll give those documents to the manual annotator.
[2594.94 → 2598.14] And we're trying to describe that problem so that the person understands it to create the data.
[2598.68 → 2603.34] We can essentially take all the same resources and give those to an LLM
[2603.34 → 2605.72] and get the LLM to perform the same steps.
[2606.04 → 2607.14] So there are two parts to that.
[2607.14 → 2611.48] There's a generative part where the LLM can generate documents.
[2612.14 → 2617.04] So let's say we've got 100 documents in our data set, but we want 10,000.
[2617.66 → 2623.78] We can say generate a document like this one, but add variation on top of that.
[2624.34 → 2629.74] And we can fan out our data set, our documents from 100 to 10,000.
[2629.74 → 2637.38] We could then take those same documents or a pool of documents from elsewhere, and we could get feedback on that.
[2637.54 → 2640.04] So that could be qualitative feedback.
[2640.44 → 2643.80] Tell me which of these documents are relevant to this task.
[2644.20 → 2650.82] Tell me which of these documents are of a high quality, are concise, are detailed, this kind of attributes.
[2650.82 → 2656.08] So we could filter down our large data set or our generated data set to the best documents.
[2656.72 → 2658.16] We could also add labels.
[2658.16 → 2663.64] So we could say, tell me which of these documents relates to my business use case or not.
[2663.82 → 2664.62] This kind of things.
[2665.08 → 2667.10] Apply topics to these documents.
[2667.10 → 2671.88] And then we can, in doing so, create a classification data set, right, from those labels.
[2672.88 → 2681.88] Or we could, in one example, take a set of documents and use a generative model to generate questions or queries about those documents.
[2682.08 → 2689.42] And we could use that to create a Q&A data set or a retrieval data set where we generate search queries based on documents.
[2689.42 → 2699.38] When you're doing that, and you're generating the data sets with another model, how much do you have to worry about hallucination playing into that?
[2699.48 → 2702.42] It sounds like you have a good process for kind of trying to catch it there.
[2703.20 → 2705.12] But is that a small issue?
[2705.22 → 2706.30] Is that a larger issue?
[2706.56 → 2707.98] Any guidance on that?
[2708.58 → 2710.52] That's one of the main issues, definitely.
[2710.88 → 2712.70] Like, it is probably the main issue.
[2712.70 → 2721.34] And so really, it's about both sides of that process that I described, that generating side and that evaluating side.
[2721.56 → 2728.38] So you get the large language models to do as much as possible to expose hallucination by evaluating themselves.
[2729.12 → 2732.32] And typically, you're getting larger models to evaluate.
[2732.58 → 2736.70] So they're a more performant model, and should hallucinate less.
[2737.16 → 2742.18] The task of identifying hallucinations is not the same as generating a document.
[2742.18 → 2746.10] So typically, LLMs are better at identifying hallucinations and nonsense.
[2746.48 → 2750.14] If you give them the context, then they are not generating it.
[2750.88 → 2758.36] And so you combine that within a pipeline, and then you would take that to a domain expert in a tool like Argyll.
[2758.68 → 2761.50] And so that's really why we have these two tools, right?
[2761.62 → 2762.68] Distalable and Argyll.
[2763.08 → 2768.84] Because kind of without Argyll, Distalable would suffer from a lot of those problems.
[2768.84 → 2769.40] Yeah.
[2769.88 → 2770.40] Yeah.
[2770.52 → 2778.32] And I guess that brings us to the second tool, the Distalable, which I know has some to do with this synthetic data piece as well.
[2778.42 → 2788.68] And I'm really intrigued to hear about this because I also see some of what you have on the documentation about what are people building with Distalable.
[2788.68 → 2797.22] I do note a couple of datasets like the Open Hermes dataset, the Intel Orca DPO dataset.
[2797.46 → 2805.26] These are datasets that have been part of the lineage of models that I've found very, very useful.
[2805.84 → 2812.34] So first off, thanks for building tooling that's created really useful models in my own life.
[2812.34 → 2827.08] But beyond that, yeah, David, do you want to go into a little bit about what Distalable is and maybe even tie into some of those things and how it's proven to be a useful piece of the process in creating some of those models?
[2827.08 → 2844.52] I think, yeah, the idea of Distalable kind of started to have a year ago more or less, or maybe a year ago where we saw these initial new models coming out like Alpaca and Dolly from Databricks, Alpaca from Stanford,
[2844.52 → 2859.26] where there were like datasets being generated with OpenAI frontier models being evaluated with OpenAI frontier models and then published and actually used for fine-tuning one of these models.
[2859.60 → 2863.58] So apparently there were research groups or companies kind of investing time in this.
[2863.96 → 2871.10] But what we also saw is when we would kind of upload these datasets into Agile, actually start looking at the data that there were a lot of flaws within there.
[2871.10 → 2891.78] And then whenever like Ultra Feedback, which is one of these specific papers that really started to scale the synthetic data and AI feedback concept came out, we thought, okay, maybe it's worth to look into like a package that can actually help us facilitate kind of creating datasets that we can then eventually fine tune within Agile.
[2892.22 → 2895.96] And that's when we started to work on the initial version of Distalable.
[2895.96 → 2908.06] So it's kind of like application frameworks like Lama Index or Enchain, if you're familiar with those, but then specifically focused on synthetic data generation and AI feedback.
[2908.44 → 2922.38] So what we try to do is organize everything into this pipeline structure where you have either steps that are about basic data operations, tasks that are about prompt templates or prompting.
[2922.38 → 2934.56] And prompt templates, you can think about either providing feedback, maybe rewriting some initial input that you provide to that prompt template, or maybe like ranking or like generating from scratch or this kind of things.
[2935.34 → 2938.64] And then these tasks are actually executed by LLMs.
[2939.04 → 2944.02] And these are then all like fit together within a pipelining structure.
[2944.02 → 2959.74] The thing for these tasks is that nowadays, we actually look at all the most recent research implementations or most recent research papers, and we try to implement them whenever they come out and are actually relevant for synthetic data generation.
[2959.74 → 2967.92] So you really go from like the kind of finicky prompt engineering, so to say, to well-evaluated prompts that we've implemented.
[2968.74 → 2973.74] And the nice thing about our pipeline structure is also that we run everything asynchronously.
[2974.66 → 2980.40] So there's multiple like LLM executions being done at once, which will really speed up your pipeline.
[2980.94 → 2984.20] And on top of that, we also cache all the intermediary results.
[2984.20 → 2989.00] So as you can imagine, calling the OpenAI API can be quite costly.
[2989.52 → 2994.38] And whenever you run a pipeline, a lot of things can go wrong.
[2994.80 → 3000.10] But whenever you actually rerun our pipelines within the C-label, you actually have these cache results already there.
[3000.18 → 3005.34] So you would avoid kind of incurring additional costs whenever something within the pipeline breaks.
[3005.34 → 3007.10] Yeah, that's awesome.
[3007.30 → 3022.60] And I know that one element of this is the kind of creation of synthetic data for further fine-tuning LLMs to increase performance or maybe to some sort of alignment goal or something like that.
[3022.60 → 3049.90] But also, I know from working with a lot of healthcare companies, manufacturers, others that are more security privacy conscious in my day job, part of the pitch around synthetic data is maybe also creating data sets that might not kind of poison LLMs with a bunch of your own sort of private information.
[3049.90 → 3055.32] That could be sort of exposed as part of an answer that someone prompts the model in some way.
[3055.44 → 3059.34] And this data is embedded in the data set and all of that.
[3059.50 → 3063.34] So, yeah, I would definitely encourage people to check out the still label.
[3063.54 → 3065.62] And you said it's been around for half a year.
[3065.76 → 3070.96] So how have you seen the kind of usage and adoption so far?
[3071.78 → 3077.70] The usage and adoption has been quite, quite good in terms of the number of data sets that have been released.
[3077.70 → 3096.98] So you mentioned the Intel Orca DPO data set, which was an example use case of how we were initially using it, where we had this original data set that had been labelled by Intel employees with references of what would be like the preferred response to a given prompt.
[3096.98 → 3111.10] And we actually used this label to kind of clean that based on prompting LLMs ourselves to reevaluate these chosen rejected pairs within the original data set, filtering out all the ambiguity.
[3111.44 → 3116.18] So sometimes the LLM wouldn't align with the original chosen rejected pair.
[3116.76 → 3125.74] And based on that, we were actually able to scale down the data set by 50%, leading to less training time and also leading to a higher performing model.
[3125.74 → 3137.00] And that was one of the really famous examples that kind of inspired some people within the open source community to actually start looking at this label to start using this label to generate data sets.
[3137.22 → 3145.66] There's some hugging face teams that actually have been generating millions and millions of rows of synthetic data using this label.
[3145.90 → 3150.14] And that's pretty cool to see that people are actually using it at scale.
[3150.14 → 3168.20] And besides that, there's also these smaller companies, so to say, but like LMA, the German consultancy, the German startup that I mentioned before, using it to also rewrite and resynthesize emails within actual production use cases.
[3168.20 → 3198.18] That's really fascinating.
[3198.18 → 3199.76] What's the most important thing that you're using in a few months or maybe a few months or maybe a year or two?
[3199.98 → 3200.58] What are your thoughts?
[3201.30 → 3204.64] I suppose for me, it's about two main things.
[3204.82 → 3206.86] And the first would be modalities.
[3207.48 → 3214.96] So moving out of text and into image and audio and video and also kind of UX environments.
[3215.62 → 3223.52] So that maybe in Argyll, but also in Distal Able, that we can generate synthetic data sets in different modalities and that we can review those.
[3223.52 → 3230.40] And that's a necessity and something that we're already working on, and we've already got features around, but we've got kind of more coming.
[3231.00 → 3234.40] And then the second one, which I suppose is a bit more far-fetched.
[3234.66 → 3240.40] And that's a bit more about kind of tightening the loop between the various applications.
[3240.40 → 3252.14] So between Distal Able, Argyll and the application that you're building so that you can deal with feedback as it's coming from your domain expert that's using your application and potentially Argyll at the same time.
[3252.14 → 3258.14] So we can kind of synthesize on top of that to evaluate that feedback that we're getting and generate based on that feedback.
[3258.74 → 3265.52] So we can add that into Argyll, and then we can respond to that synthetic generation, that synthetic data.
[3266.06 → 3273.02] And then we can use that to train our model, this kind of tight loop between the end user, the application and our feedback.
[3273.02 → 3273.30] Yeah.
[3273.30 → 3273.74] Yeah.
[3273.74 → 3282.66] And for me, it kind of aligns with what you mentioned before, Ben, like the multimodality, smaller, more efficient models, things that can actually run on a device.
[3283.00 → 3293.16] I've been playing around with this app this morning that you can actually load local LLM into, like a smaller IN or LLM model from Meta.
[3293.16 → 3296.74] And it actually runs on an iPhone 13, which is really cool.
[3296.84 → 3297.22] It's private.
[3297.42 → 3298.52] It runs quite quickly.
[3299.08 → 3305.54] And the thing that I've been wanting to play around with is these speech-to-speech models where you can actually have real-time speech-to-speech.
[3305.68 → 3308.06] I'm currently learning Spanish at the moment.
[3308.40 → 3317.26] And one of the difficult things there is not being secure enough to actually talk to people out on the streets and this kind of things.
[3317.26 → 3326.20] So whenever you would be able to kind of practice that at home privately on your device, kind of talk some Spanish into an LLM, get some Spanish back, maybe some corrections in English.
[3326.50 → 3332.02] This kind of scenarios are super cool for me whenever they would be able to come through.
[3333.46 → 3334.92] Yeah, this is may Buenos.
[3335.34 → 3344.26] And yeah, I've been really, really excited to talk to you both and would love to have you both back on the show sometime to update on those things.
[3344.26 → 3358.58] Thank you for what you all are doing, both in terms of tooling and our GLN hugging face more broadly in terms of how you're driving things forward in the community and especially the open source side.
[3358.78 → 3359.76] So thank you both.
[3359.86 → 3364.44] Thank you for taking time to talk with us and hope to talk again soon.
[3365.00 → 3365.74] Yeah, thank you.
[3366.08 → 3367.02] And thanks for having us.
[3367.24 → 3367.58] Thank you.
[3374.26 → 3378.94] All right, that is Practical AI for this week.
[3379.74 → 3380.78] Subscribe now.
[3380.94 → 3385.94] If you haven't already, head to practicalai.fm for all the ways.
[3385.94 → 3392.34] And join our free Slack team where you can hang out with Daniel, Chris, and the entire Changelog community.
[3392.90 → 3397.56] Sign up today at practicalai.fm slash community.
[3397.56 → 3405.08] Thanks again to our partners at fly.io, to our beat freaking residents, Break master Cylinder, and to you for listening.
[3405.44 → 3407.20] We appreciate you spending time with us.
[3407.56 → 3408.74] That's all for now.
[3408.98 → 3410.68] We'll talk to you again next time.
[3410.68 → 3410.74] Bye.
[3410.74 → 3410.80] Bye.
[3410.80 → 3410.88] Bye.
[3410.88 → 3411.80] Bye.
[3411.80 → 3412.80] Bye.
[3412.80 → 3413.80] Bye.
[3413.80 → 3414.80] Bye.
[3414.80 → 3414.88] Bye.
[3414.88 → 3415.80] Bye.
[3415.80 → 3415.88] Bye.
[3415.88 → 3416.88] Bye.
[3416.88 → 3417.88] Bye.
[3417.88 → 3417.92] Bye.
[3417.92 → 3417.94] Bye.
[3417.94 → 3418.02] Bye.
[3418.02 → 3419.02] Bye.
[3419.02 → 3420.02] Bye.
[3420.02 → 3421.02] Bye.
[3421.02 → 3421.52] Bye.
[3421.52 → 3422.02] Bye.
[3422.02 → 3423.02] Bye.
[3423.02 → 3424.02] Bye.
[3424.02 → 3424.06] Bye.
[3424.06 → 3424.08] Bye.
[3424.08 → 3424.12] Bye.
