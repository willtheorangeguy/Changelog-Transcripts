[0.00 → 8.64] Welcome to Practical AI.
[9.20 → 15.96] If you work in artificial intelligence, aspire to, or are curious how AI-related technologies
[15.96 → 18.78] are changing the world, this is the show for you.
[19.20 → 24.36] Thank you to our partners at Vastly for shipping all of our pods superfast to wherever you
[24.36 → 24.66] listen.
[24.92 → 26.76] Check them out at Fastly.com.
[26.76 → 32.02] And to our friends at Fly, deploy your app servers and database close to your users.
[32.44 → 33.70] No ops required.
[34.04 → 36.08] Learn more at fly.io.
[42.88 → 47.32] Welcome to another fully connected episode of Practical AI.
[47.74 → 52.88] In these episodes, Chris and I keep you fully connected with everything that's happening
[52.88 → 54.16] in the AI community.
[54.16 → 59.54] We'll cover some of the latest news, and we'll cover some learning resources that'll help
[59.54 → 61.90] you level up your machine learning game.
[62.18 → 63.08] I'm Daniel Whiten ack.
[63.18 → 68.46] I'm the founder of Prediction Guard, and I'm joined as always by my co-host, Chris Benson,
[68.82 → 71.32] who is a tech strategist at Lockheed Martin.
[71.64 → 72.30] How are you doing, Chris?
[72.48 → 73.78] Doing very well today, Daniel.
[73.84 → 74.30] How are you?
[74.74 → 75.62] I'm doing great.
[75.62 → 83.22] I am uncharacteristically joining this episode from the lobby of a Hampton Inn in Nashville,
[83.36 → 83.68] Tennessee.
[84.42 → 89.20] So if our listeners hear any background noise, they know what that is.
[89.46 → 91.62] But you have a built-in audience right there.
[91.74 → 92.86] A built-in audience.
[92.86 → 102.02] The people in this lobby are unexpectedly learning about AI today, which I'm happy to do.
[102.16 → 102.28] Yeah.
[102.32 → 104.92] Out here visiting a customer on site.
[105.22 → 110.80] And yeah, it's nice to sit back and take a break from that and talk about all the cool
[110.80 → 111.60] stuff going on.
[111.98 → 112.18] Excellent.
[112.18 → 119.12] Well, I'll tell you what, you know, we have had so many questions and about kind of sorting
[119.12 → 123.16] out all the things that have happened the last few months and over the last year.
[123.52 → 128.34] And we've done a couple of episodes where it was trying to kind of clear out like generative
[128.34 → 132.34] AI, what's in it, what LLMs are, how they relate and stuff like that.
[132.86 → 137.68] What do you think about taking a little bit of a deep dive into large language models and
[137.68 → 139.98] kind of all the things that make them up?
[139.98 → 143.32] Because there's a lot of lingo being hurled about these days.
[143.76 → 144.48] Yeah, yeah.
[144.82 → 152.34] I think maybe even outside LLMs, there's this perception that the model, whether it
[152.34 → 159.30] be for image generation or video generation or language generation, that the model is the
[159.30 → 160.10] application.
[160.86 → 167.78] So when you are creating value, the sort of model, whether that be, you know, LLAMA 2 or
[167.78 → 174.60] Stable Diffusion, Excel or whatever, that somehow the model is the application, like it's providing
[174.60 → 177.60] the functionality that your users want.
[178.20 → 180.60] And that's basically a falsehood, I would say.
[181.06 → 187.02] And there's this whole ecosystem of tooling that's developing around this.
[187.20 → 193.32] And one of the things that I sent you recently, which I think does a good job at illustrating
[193.32 → 200.14] some of the various things that are part of this new ecosystem or this new generative AI
[200.14 → 204.32] app stack was created by Andreessen Horowitz.
[204.54 → 208.58] They created a figure that's like emerging LLM app stack.
[208.74 → 210.16] We'll link it in our show notes.
[210.32 → 214.64] I think it goes, though, maybe more generally than LLMs.
[214.64 → 219.30] And that provides maybe a nice framework to talk through some of these things.
[219.46 → 226.32] Now, of course, they're providing their own look at this stack, especially because they're
[226.32 → 230.46] invested in many of the companies that they highlight on the stack.
[230.58 → 235.68] But I think regardless of that, they're trying to help people understand how some of these
[235.68 → 236.54] things fit together.
[236.66 → 237.52] Have you seen this picture?
[237.96 → 238.40] I have.
[238.52 → 241.72] And I appreciated it when you pointed it out a while back there.
[241.72 → 246.30] It definitely is an interesting I haven't seen anything quite like it in terms of putting
[246.30 → 250.50] it together and some things they seem to dive into more than others in the chart.
[250.66 → 253.88] It will be interesting to see how we parse it going forward here.
[254.30 → 254.50] Yeah.
[254.68 → 263.22] And maybe we could just take some of these categories and talk them through in terms of the terminology
[263.22 → 267.78] that's used and how they fit into the overall ecosystem.
[267.78 → 273.24] So, you know, we can take an easy example here, which is one of the things that they call
[273.24 → 274.42] out, which is playground.
[275.06 → 283.70] Now, I think this is probably the place where many people start their generative AI journey,
[283.92 → 284.46] let's say.
[285.00 → 291.84] So they either go to I think within the playground category, there would be like ChatGPT might
[291.84 → 294.84] might fit in that category where you're prompting a model.
[294.84 → 295.62] It's interactive.
[295.62 → 301.56] It's a UI like you can put stuff in and put in a prompt and get an output right now.
[301.76 → 306.12] ChatGPT is maybe a little bit more than that because there's a chat thread and all of that.
[306.54 → 309.10] But there are other playgrounds as well.
[309.28 → 316.50] So you could think of spaces on hugging face that allow you to use Stable Diffusion or allow
[316.50 → 319.20] you to use other types of models.
[319.20 → 326.96] There's other proprietary kind of playgrounds that are either part of a product or are their
[326.96 → 327.80] own products.
[327.94 → 331.12] So OpenAI has their own playground within their platform.
[331.32 → 333.02] You can log in and try out your prompts.
[333.80 → 339.30] There's NAT.dev, which is a cool one that kind of allows you to compare one model to the
[339.30 → 339.56] other.
[339.74 → 345.36] There are other products like I would say something like Quip Drop, which is a tool that lets you
[345.36 → 346.48] use Stable Diffusion.
[347.32 → 348.34] And you can just go there.
[348.64 → 350.94] You can try out prompts for free.
[351.46 → 353.94] You can pay up if you need to use it more.
[354.20 → 355.58] So there's a limit to that.
[355.70 → 358.58] But there are a lot of these playgrounds floating around.
[358.74 → 360.94] And that's often where people start things.
[361.50 → 361.94] It's funny.
[362.24 → 367.26] The playground itself as a category has a lot of subcategories, I think, to it.
[367.64 → 371.22] Because you've already kind of called out kind of the diversity of what you've got.
[371.22 → 375.42] In the cloud providers, for instance, all the big cloud providers have their own playground
[375.42 → 375.98] areas.
[376.36 → 378.22] NVIDIA has a playground area.
[378.68 → 382.20] I think it's almost becoming a ubiquitous notion.
[382.48 → 386.98] And of course, all those playground areas for the commercial entities are focused on their
[386.98 → 388.58] products and services, definitely.
[388.70 → 391.36] But trying to bring some cool factor to it.
[391.64 → 392.02] Yeah.
[392.22 → 396.76] It's almost like a demo or experimentation interface.
[396.76 → 403.24] So if we define this playground category, it's usually, but not always, a browser-based
[403.24 → 410.28] playground or a browser-based interface where you can try to prompt a model and see what
[410.28 → 411.32] the output is like.
[411.40 → 413.38] I think that would kind of generally be true.
[413.84 → 415.86] Maybe there are some caveats to certain ones.
[416.00 → 418.84] Like Midjourney, for example, is a Discord bot.
[419.08 → 421.58] Or there's still a Discord bot that you could use.
[421.66 → 423.16] Maybe that fits into the playground.
[423.16 → 432.86] But generally, these are interactive and useful for experimentation, but not necessarily useful
[432.86 → 435.48] to build an application.
[436.02 → 436.84] Yeah, I agree.
[437.10 → 443.16] And another thing to note about it from a characteristic standpoint is not only is it really, it's not
[443.16 → 445.12] made for you to go build your own thing.
[445.14 → 449.56] It's made for you to try the stuff of whatever organization is doing.
[449.56 → 453.14] But they do it, they provide the resources.
[453.42 → 457.04] So by being in a browser, you don't have to have a GPU on your laptop.
[457.26 → 458.48] You don't have to have resources.
[458.72 → 458.84] Yeah.
[458.92 → 459.10] Yeah.
[459.10 → 462.20] You don't have to have all the things through various means.
[462.20 → 466.60] They set up all that for you on the backend, whether it be just calling a service or whether
[466.60 → 470.00] it is creating a temporary environment through virtualization.
[470.36 → 475.78] But it is a good way to either to test out a new product line or to, or to just get your
[475.78 → 477.06] toes wet a little bit.
[477.06 → 481.40] If you want to try some stuff out, maybe you've been listening to the Practical A podcast for
[481.40 → 484.82] a little while, and you want to, a particular topic grabs you.
[484.94 → 486.38] That would be a good place to go.
[486.84 → 486.96] Yeah.
[487.02 → 492.44] And I think within that same vein, you could transition to talk about this other category,
[492.44 → 500.38] which is not unique to the generative AI app stack, let's call it, but it's still part
[500.38 → 503.38] of the stack, which they have called out app hosting.
[503.38 → 505.90] So that's like very generic, right?
[506.00 → 513.50] So in here would fit things like Tercel, or I would say, you know, generally like the cloud
[513.50 → 514.42] providers, right?
[514.46 → 519.40] And the various ways that you can host things, whether that be on Amazon with ECS or app runner
[519.40 → 525.46] or whatever that is, or in even your own infrastructure, your own on-prem infrastructure, if you host
[525.46 → 525.76] things.
[525.76 → 533.38] Now there are, I would say a number of hosting providers that are kind of cool and trendy
[533.38 → 539.92] and people that are building new AI apps, they seem to gravitate towards like, let's say Tercel
[539.92 → 545.14] and a lot of front-end developers that use Tercel, which I think it's an amazing platform.
[545.28 → 545.74] So cool.
[545.74 → 553.54] That hasn't traditionally been like a data science-y hosting way of doing things, but it represents,
[553.80 → 559.76] I think, this new wave of application developers that are developing applications, integrating
[559.76 → 560.20] AI.
[561.12 → 568.80] And you see some of those now kind of coming into or being exposed in this kind of wider app
[568.80 → 569.18] stack.
[569.52 → 574.48] Which is a good thing because we've talked for a long time, even as we opened this conversation
[574.48 → 576.26] up saying the model is not the app.
[576.76 → 582.02] You know, you have to wrap the model with some goodness to get the value out of it, to be
[582.02 → 582.80] productive with it.
[583.26 → 588.98] And so I personally like the fact that we're seeing the model hosting and the app hosting
[588.98 → 592.48] are starting to merge because I think that's more manageable over time.
[592.62 → 598.10] It's less being in its own special category, and it's more about, okay, every app in the future
[598.10 → 599.32] is going to have models in it.
[599.46 → 601.72] And so, you know, we're accommodating that notion.
[601.90 → 603.32] So I like seeing it go there.
[603.32 → 604.58] I've been waiting for that for a while.
[605.34 → 605.44] Yeah.
[605.54 → 610.78] And to really clarify and define things, you could kind of think about like the playground
[610.78 → 616.60] that we talked about as an app that has been developed by these different people that
[616.60 → 618.86] illustrates some LLM functionality.
[619.16 → 622.12] But it's usually not the app that you're going to build.
[622.30 → 626.94] You're going to build another app that is exposed to your users that uses the functionality.
[626.94 → 631.22] And you'll need to host that either in ways that people have been hosting things for a
[631.22 → 637.24] long time or new interesting patterns that are popping up like things that modal is doing
[637.24 → 643.06] or maybe things that front end developers really like to use like for sale and other things.
[643.16 → 645.48] But there's still that app hosting side.
[646.20 → 651.44] Now, where I think things get interesting is you have the playground, you have the app hosting,
[651.44 → 655.46] but regardless of both of those, what happens under the hood?
[655.46 → 661.36] And this is, I think, where things get quite interesting and where there are a lot of differences
[661.36 → 669.24] in the kind of emerging generative AI stack compared to the maybe more traditional non-AI stack.
[669.24 → 675.88] In the middle of the diagram that we're talking about, this emerging LLM app stack diagram,
[676.14 → 682.68] which I think also is, again, more general, is this layer of orchestration.
[683.32 → 689.80] So I don't know about you, Chris, but I am old enough, I guess, you don't have to be that old,
[689.92 → 697.70] I don't think, to when someone says orchestration, I think of like Kubernetes or like container orchestration.
[697.70 → 705.82] Maybe that's my own bias coming from working in a few microservices-oriented startups and that sort of thing.
[706.22 → 711.40] But this is distinctly not the orchestration that's being called out here.
[711.68 → 716.74] In the generative AI app stack, there's a level of orchestration,
[716.94 → 724.62] which in some of my workshops I've been kind of referring to as almost like a convenience layer.
[724.96 → 727.46] Think about like when you're interacting with a model.
[727.70 → 729.90] Let's give a really concrete example.
[730.00 → 732.54] Let's say I want to do question and answer with an LLM.
[732.98 → 738.66] I need to somehow get a context for answering the question.
[738.98 → 743.00] I need to insert the question in that context into a prompt.
[743.52 → 745.62] And then I need to send that prompt to a model.
[745.78 → 750.34] I need to get the result back and maybe do some like cleanup on it.
[750.34 → 758.04] Like I have some stop tokens, or I want it, you know, to end at a certain punctuation mark or whatever that is.
[758.64 → 759.84] That's all convenience.
[760.38 → 768.98] What I would consider sort of this convenience and what they're calling orchestration around the call to the model.
[768.98 → 784.30] And so this orchestration layer I think has to do with prompt templates, generating prompts, chains of prompts, agents, plugging in data sources like plugins.
[784.68 → 793.16] These are all things that kind of circle around your AI calls, but aren't the AI model.
[793.16 → 797.60] Yeah, I mean, it's the surrounding software, you know, just to simplify a little bit.
[797.70 → 799.12] Yeah, and maybe tooling.
[799.36 → 799.70] Yeah.
[800.12 → 800.90] Orchestration tooling.
[801.08 → 801.22] Yeah.
[801.36 → 801.56] Yeah.
[801.70 → 806.22] It's the stuff you have to wrap the model with to make it usable in a productive sense.
[806.22 → 811.00] And from the moment that I saw that word, that was almost the very first thing that grabbed me.
[811.10 → 815.14] You know, those, you know, little psychological quirk where you kind of notice the thing that sticks out.
[815.52 → 815.66] Yeah.
[815.76 → 826.38] That's the thing that stuck out was they, it's a big bucket that they're calling orchestration, which is a loaded word that can mean a lot of different things depending on what it is you're trying to do.
[826.38 → 831.66] And the examples that they list in that category are all somewhat diverse as well.
[831.94 → 838.76] I think that was the first point where I thought, well, it's a chart with the creator has a, has a bias there.
[839.08 → 849.12] What are some of the ways I'm just curious when we think about this kind of orchestration, as they say, wrapping around and providing the convenience, any ways that you would break that up?
[849.12 → 860.82] Like how you think about it, you mentioned convenience and stuff, but they go from something like Python as a programming language to Lang chain to ChatGPT, all three very distinct kinds of entities.
[861.42 → 861.52] Yeah.
[861.58 → 865.72] I think that you're kind of seeing a number of things happen here.
[865.86 → 869.62] The first one that they call out is Python slash DIY.
[870.12 → 877.32] So you're seeing a lot of roll your own kind of convenience functionality built up around LLMs.
[877.32 → 882.96] But I do think one of the big players here would be like Lang chain and what they're doing.
[883.08 → 891.26] Because if you look again at this kind of layers of what's available there, you have maybe categories that I would call out.
[891.38 → 899.42] If we just take Lang chain as an example, categories that I would call out of this sort of orchestration functionality would be emulating.
[899.72 → 906.74] So this would be like prompt templates, for example, or emulating in terms of chains.
[906.74 → 912.30] So manually setting up a chain of things that can be called in one call.
[912.48 → 916.38] There's also an automation component of it.
[916.38 → 938.08] Maybe this is a way that orchestration kind of fits with the older way the orchestration term is used in like DevOps and other things where some of it could be automation related to with things like agents or something like that, where you have an agent that automates certain functionality.
[938.08 → 950.00] It's not the LLM itself, but it's really automations around calling the LLMs or the other generative AI models to generate an image or what have you.
[950.00 → 955.12] They also kind of have some separate call-outs, you know, for APIs and plugins.
[955.56 → 967.54] And then they have, which we can hit in a moment, they kind of have a collection of the maintenance items, you know, the things to keep the lights on, if you will, logging and caching and things like that.
[967.62 → 969.80] How do you look at that breakdown the way they have it?
[969.80 → 981.52] Yeah, so I think this is where they kind of have the orchestration piece in the middle there as connecting a couple different things.
[981.64 → 987.04] One of those would be what I would consider, I think, more on the data or resource side.
[987.36 → 989.82] And then one is more on the model side.
[990.04 → 992.74] So I think we could split it into those two major categories.
[992.74 → 997.50] So what are you orchestrating when you're orchestrating something with Lang chain or similar?
[998.24 → 1002.16] Well, you're orchestrating connections to resources.
[1002.46 → 1007.40] I'll use the term resources because it might not be data per se.
[1007.68 → 1016.08] It might be like you say, like an API or another platform like Zapier or, you know, Wolfram Alpha, something like that.
[1016.38 → 1019.04] The other side of that is the model side.
[1019.04 → 1025.26] And both the model hosting and some really useful tooling around that.
[1025.50 → 1026.90] But let's start on the resource side.
[1027.00 → 1038.08] So as you mentioned, you might orchestrate things like one of the things that I found both really fun to do and useful is to orchestrate calls into like a Google search.
[1038.34 → 1044.84] So if I want to pull in some context on the fly, then I might want to do a Google search.
[1044.84 → 1046.02] That's a call to an API.
[1046.02 → 1060.00] So that's a resource or a plugin that might be conveniently integrated into your orchestration layer, either via something like Lang chain or via your own DIY code.
[1060.64 → 1072.26] Another side of this would be the actual data and the data pipelines, which are your own data or data that you've gathered or is relevant to your problem.
[1072.26 → 1084.98] So again, if we're thinking about this sort of set of resources that could be orchestrated into your app, maybe you have a set of documentation that you want to generate answers to questions out of.
[1085.36 → 1092.82] Or maybe you have a bunch of images that you want to use to fine tune Stable Diffusion or something like that.
[1092.82 → 1096.70] Having data and integrating it into models isn't new.
[1097.44 → 1109.90] And so the things that are called out in this particular image, like data pipelines, those are also not new and are part of this app stack if you're integrating your own data.
[1109.90 → 1118.08] So things like Databricks or Airflow or Packager or tools to parse data.
[1118.28 → 1128.80] So PDF parsers or unstructured data parsers or image parsers or image resizing or all of that sort of stuff still fits into the data pipelining piece.
[1128.80 → 1147.82] And so you've either got your data coming from APIs, which might be a resource that you're orchestrating, or you've got your data coming from your data sources, which might be traditional data sources of any type from databases to unstructured data.
[1152.82 → 1155.14] This is a changelog news break.
[1155.78 → 1156.80] It's official.
[1156.80 → 1172.54] Well, advancements in computer vision have rendered CAPTCHAs obsolete, as new research shows AI bots are 15% more accurate than humans at picking which images have a bridge or a sign or a bicycle or whatever in them.
[1172.72 → 1182.64] The researchers recruited 1,400 participants to test websites that use CAPTCHA puzzles, which account for 120 of the world's 200 most popular websites.
[1182.64 → 1187.64] The bots' accuracy ranges from 85% to 100%, with the majority above 96%.
[1188.64 → 1197.98] Meanwhile, we mere mortals check in at a pathetic 50% to 85% accuracy, and we answer slower than the robots to add insult to injury.
[1197.98 → 1207.78] I've surmised this for months now, as we've been unable to ward off spam account creations on changelog.com, no matter which shiny new CAPTCHA service we tried.
[1208.38 → 1216.70] There are other efforts in the works besides CAPTCHA in order to differentiate between robots and humans, but so far, the robots are winning.
[1216.70 → 1222.26] You just heard one of our five top stories from Monday's changelog news.
[1222.62 → 1235.02] Subscribe to the podcast to get all the week's top stories and pop your email address in at changelog.com slash news to also receive our free companion email with even more developer news worth your attention.
[1235.44 → 1238.92] Once again, that's changelog.com slash news.
[1238.92 → 1260.16] Well, Chris, part of the data piece or the resource piece that is kind of unique within this new generative AI app stack is the embedding and the vector database piece.
[1260.16 → 1278.68] And I have to say, I've just got to recommend that our listeners, if they haven't listened to our very recent episode about vector databases, because that episode goes into way more depth in terms of what a vector database is and why people are using it.
[1278.68 → 1301.08] But just for a quick recap, part of what you might want to do with generative AI models is found relevant data that's relevant to a user query and somehow orchestrate that into your LLM calls, either for chat or question answering, or maybe even into image generation or video generation.
[1301.08 → 1312.96] In order to find relevant data, what people have found is that they would like to do a vector or an embedding search on their own data to find relevant data.
[1313.16 → 1331.06] And again, you can find out much more about that in our previous episode, but that's called out in this app stack as probably something unique that's developing, which is not just having data pipelines and databases, but having data flow through an embedding model.
[1331.08 → 1336.90] And into a vector database where you're performing semantic searches.
[1337.02 → 1343.70] I mean, at the end of the day, it's a database that's very, it works well for the kind of operation that we're doing here.
[1343.92 → 1353.00] Whereas some of the traditional things that we had been working on for years before, there's kind of a context shifting in terms of how you're handling data, what data is, how it's organized.
[1353.58 → 1355.24] So this makes a lot more sense.
[1355.24 → 1355.80] Yeah.
[1355.80 → 1355.84] Yeah.
[1356.04 → 1367.36] And it should call out here too, part of the stack here, and I'm glad that they called it out in this way in the schematic that we're looking at is the embedding model.
[1367.80 → 1383.20] So a lot of people are talking about these vector databases, but in order to store a vector in a vector database, there is a very relevant component to this stack, which is the actual model that you're using to create embeddings.
[1383.20 → 1385.78] And not all are created equal.
[1386.36 → 1391.24] So think about if you are working on an image problem, right?
[1391.36 → 1400.72] You may use a pre-trained feature extractor type model from hugging face to extract vectors that your images.
[1400.72 → 1403.52] So put an image and get a vector out.
[1403.52 → 1418.66] But if you're working with both image and text, for example, maybe you're going to use something like clip or one of those, a related model that's able to embed both images and text in a similar semantic space.
[1418.66 → 1424.16] But if you're only using text, there's a bunch of, of course, choices.
[1424.84 → 1430.34] And all of those don't perform equally for different types of tasks as well.
[1430.48 → 1440.66] There's, if you search on Hugging Face or just do a Google search for a Hugging Face embeddings leaderboard, there's actually a separate leaderboard.
[1440.66 → 1447.30] So Hugging Face has a leaderboard for open models and how those score in various metrics.
[1447.84 → 1452.48] They also have a leaderboard for embeddings, and you can click through the different tasks.
[1452.56 → 1456.96] So let's say you're doing retrieval tasks, like we're talking about here from a vector database.
[1456.96 → 1467.26] You can see which embeddings perform the best according to a variety of benchmarks in retrieval or in summarization or other things.
[1467.26 → 1474.32] Do you use that a lot when you're putting models and storing them into vector databases and figuring out the embeddings?
[1474.44 → 1477.10] Do you tend to go and see what is going on?
[1477.12 → 1479.96] Because right now there's so much happening in that space.
[1480.06 → 1482.02] Does that make for a good guidepost for you?
[1482.40 → 1483.02] Yeah, yeah.
[1483.16 → 1494.12] And I think what is also useful is looking at those performance metrics, but also at least on the Hugging Face leaderboard and some other leaderboards.
[1494.12 → 1502.92] So if you search for, if you're working with text, one of the major tools for creating these embeddings in a really useful way is called sentence transformers.
[1503.42 → 1512.86] And they have their own table where they have measured and benchmark various embeddings that can be integrated in sentence transformers.
[1512.86 → 1526.96] That's useful, but it's also useful to look at the columns, whether you're looking in the Hugging Face leaderboard or the sentence transformers or wherever you're looking at the size of the embedding and the speed of the embedding.
[1526.96 → 1531.94] Because it was called out when we had our vector database discussion, but only in passing.
[1532.54 → 1536.80] Let's say you want to embed, you know, 200,000 PDFs.
[1537.18 → 1541.70] So I just ran across this use case with some of the work that we're doing.
[1541.70 → 1553.20] And it can take a really, really, really, really long time, depending on how you implement it, to both parse and embed a significant number of PDFs.
[1553.24 → 1558.58] The same would be true for documents or other text or other types of data even.
[1559.10 → 1562.62] And so when you're looking at that, there are two implications here.
[1562.74 → 1566.34] One is how fast am I able to generate these embeddings?
[1566.34 → 1569.86] Do I have to use a GPU, or can I use a CPU?
[1570.44 → 1574.00] Because there's going to be a different speed on GPUs versus CPUs.
[1574.10 → 1576.08] And how big are the embeddings?
[1576.22 → 1594.18] This is another kind of interesting piece, which is if I have got embeddings that are thousand or more in dimension, that's going to take up a lot more room in my database and on disk than embeddings that are 256 or something like that.
[1594.18 → 1602.12] So there's also storage and moving around data implications to how you choose this embedding space.
[1602.24 → 1612.50] So there's a lot of, I think, practical things that maybe people skip over here when they're just doing a prototype with Lang chain and some vector database.
[1612.50 → 1613.46] It's easy.
[1613.68 → 1618.98] But then as soon as you try to put all your data in, it gets much harder.
[1619.68 → 1622.16] You raised a question in my mind, and I'm going to throw it out.
[1622.16 → 1625.30] You may or may not be familiar with what the answer would be.
[1625.80 → 1639.50] But when you're looking at vector databases, and you're looking at all this, you know, the diversity in embedding possibilities here and the fact that that has kind of physical layer consequences, you know, in terms of storage and stuff like that.
[1639.50 → 1653.18] Are we seeing that in vector or other database arenas where they're trying to accommodate this new approach to capturing data in terms of having embeddings the way of vector, you know, with the rise of vector databases?
[1653.18 → 1663.12] It seems that there would be a whole lot of kinds of vendor related research on how you do that, because to your point a moment ago, you're talking about data.
[1663.44 → 1670.70] It's such a volume that poor architecture in terms of what's under the hood could have some pretty big consequences there.
[1670.70 → 1673.14] Yeah, I think that's definitely true.
[1673.34 → 1682.92] And there was a point that was made in one of our last episodes that the vendors for these things are having different priorities that don't always align.
[1683.10 → 1690.08] So some are optimizing for how much data, how quickly you can get a large amount of data in.
[1690.08 → 1693.98] But maybe they're not as optimized for the query speed.
[1694.30 → 1699.64] Some are optimizing for query speed, but it might be really slow to get data in.
[1700.32 → 1703.30] And so that's one piece of it.
[1703.38 → 1713.64] I think another piece of it is how large of an embedding do you need, and how complicated is your retrieval problem, right?
[1713.64 → 1728.10] I would recommend that people do some testing around this, because let's say you have 100,000 documents that are very, very similar one to another or 100,000 images that are very, very similar to one another.
[1728.28 → 1732.52] And the retrieval problem is actually semantically very difficult.
[1732.52 → 1743.90] You might need a larger embedding and more kind of power, even like optimization around the query, like re-ranking and other things to get the data that you need.
[1744.24 → 1753.40] Whereas if you have, you know, 100,000 images, and they're all fairly different, well, maybe you don't need to go to some of those links.
[1753.40 → 1757.62] So, yeah, I think that that's also part of this problem.
[1757.90 → 1772.04] And people are still feeling out the best practices around some of this, partially because it's this kind of new part of the AI stack and partially because things are constantly updating as well.
[1772.18 → 1778.50] So if you use this embedding today, there's a better one tomorrow and vector databases are updating all the time.
[1778.62 → 1781.38] So it's also just a very dynamic time here.
[1781.38 → 1793.94] As we look at the chart here, and there's kind of the three that we referred to earlier that are kind of together, and those are LLM cache, logging slash LLM ops, and validation.
[1794.62 → 1801.82] First, could you kind of describe what's encompassed in each of those and also kind of why are they fit together?
[1801.96 → 1805.36] Why are we seeing those lumped in one category here, one super category?
[1805.36 → 1814.00] Yeah, so if you think about what we've talked about so far, there's this new generative AI stack, whether you're doing images or language or whatever.
[1814.34 → 1819.54] There's an application side, which might just be the playground, or it might be your own application.
[1819.54 → 1826.88] There's a data and resources side, which is what we've talked about with integrating APIs and data sources.
[1827.40 → 1832.22] And then there's like a third arm here, which is the model side.
[1832.38 → 1839.54] And all of those are kind of connected through the orchestration layer, the automation layer, the convenience layer, whatever you want to end up calling that.
[1839.54 → 1844.96] So now we're kind of going to this third arm of the model side.
[1845.72 → 1848.18] And we can come back to it here in a second.
[1848.42 → 1853.26] But one side of this is just hosting the models and having an API around them, which we can come back to.
[1853.40 → 1862.10] But between the model and your orchestration layer, almost as maybe we could call it like model middleware.
[1862.10 → 1864.68] I'll just go ahead, coin that.
[1864.84 → 1869.22] I just coined it on maybe people are already referring to it that way and I didn't coin it.
[1869.34 → 1878.36] But model middleware sits kind of either wrapping around or in between your orchestration layer and your model hosting.
[1878.86 → 1882.78] And these are the things that you're referring to around caching, logging, validation.
[1883.38 → 1891.84] Probably the one that people are most familiar with, if they are familiar with one of these would be the logging layer.
[1892.10 → 1898.18] Which is, again, something that is kind of a DevOps-y infrastructure term.
[1898.18 → 1916.34] But here we might think of very specific type of logging, like model logging, which might be more natively supported in things like weights and biases or clear ML or this other kind of ML ops type of solutions.
[1916.34 → 1929.78] Where you're logging requests that are coming in, prompts that are being provided, response time, GPU usage, all the kind of model related things.
[1930.02 → 1933.76] And you want to put those into, you know, graphs and other things.
[1934.16 → 1937.24] So there may be specific kinds of logging.
[1937.24 → 1942.84] So how quickly on average is my model responding?
[1943.12 → 1948.14] What is the latency between making a prompt or a request and getting a response?
[1948.44 → 1951.66] How much GPU usage is my model using?
[1951.86 → 1954.76] And do I need more replicas of that model?
[1955.10 → 1959.18] These sorts of things can be really helpful as you're putting things into production.
[1959.38 → 1963.20] So that's a first of these middleware layers.
[1963.20 → 1989.34] So Chris, the other middleware layers, I would say, that have been called out, at least in what we're looking at, are validation and caching.
[1989.34 → 1995.16] So I'll talk about caching, and we can talk about validation a little bit, which is close to my heart.
[1995.64 → 2002.72] But caching, let's say that, again, this already happens in a lot of different applications.
[2002.72 → 2005.70] So think about like a general API application.
[2005.70 → 2021.68] If someone makes a request for data in your database, and you retrieve that data, and then the next user asks for the same data in your database, the proper and smart thing to do would not be to do two retrievals, right?
[2021.74 → 2032.30] But to cache that data in the application layer in memory so that you can respond very quickly and reduce the number of times that you're reaching out to your database and things like that.
[2032.30 → 2043.22] I notice in this chart that some of the examples that they put for caching, such as Regis and SQLite and such, are very typical and long-term players in the app dev world.
[2043.50 → 2043.60] Yep.
[2043.74 → 2055.32] So does that beg the question, or at least for me, begging the question that when you're caching, like you're really talking about for the input, here's an output, whether it goes to a model or not.
[2055.32 → 2058.98] Is it really just application data that you're caching at that point?
[2059.68 → 2067.08] So it's caching in that sense, but I think there's maybe implications to it that go beyond kind of normal caching.
[2067.52 → 2077.86] So if you, you know, running AI models is expensive most of the time because you have to run them on some type of specialized hardware, right?
[2077.86 → 2082.72] If I've got a model running on two A100s, right?
[2082.80 → 2086.82] I would rather not have four replicas of that model.
[2087.06 → 2093.18] I would rather just have one if I can, because I don't want to pay for all those GPUs.
[2093.30 → 2097.26] So part of it is really related to cost and performance.
[2097.36 → 2100.42] So it's also for a large model.
[2100.60 → 2103.58] This is mainly for large models, I would say.
[2103.58 → 2120.20] You've got a lot of cost, either because you're running that model on really specialized hardware, or because like if I'm calling out to GPT-4, it's really expensive to do a lot of requests to GPT-4, right?
[2120.20 → 2126.42] So in order to deal with that, if you have a prompt input, you can cache that prompt.
[2126.54 → 2137.52] And if users are asking the same question, I would rather just send them back the same response from GPT-4 or my large Llama 2 70 billion model or whatever it is.
[2137.60 → 2143.98] I'm going to respond to them the same way based on the same or a similar input.
[2143.98 → 2154.12] The other implication to this, which in my mind, it sort of fits into caching, but maybe not in the traditional sense.
[2154.20 → 2160.84] So I normally think of caching as like, oh, I'm going to cache things in memory or locally at the application layer.
[2160.84 → 2178.34] But if you're caching prompts and responses, there's a real opportunity to leverage that data to build your own sort of competitive moat with your specific generative AI application.
[2179.00 → 2181.88] So, for example, like you've got a user base.
[2182.20 → 2184.38] They're prompting all of these sorts of things.
[2184.38 → 2200.06] All of a sudden, if you're saving all of that data and the responses that you're giving, you're essentially starting to form your own domain-specific data set that you could kind of leverage in a very competitive way in kind of two senses.
[2200.30 → 2211.76] One is right now, if you're using a really expensive model to make those responses, maybe you start saving those responses from the really expensive model.
[2211.76 → 2219.20] And you can use that data to fine-tune a smaller model that might be more performant and cost-effective in the long term.
[2219.42 → 2221.28] So it's an operational kind of play.
[2221.80 → 2234.82] The other way is if you're gathering that over time, and you actually have the resources to human label that or give your own human preferences on that or certain annotations on that,
[2234.82 → 2246.46] that now is your own kind of advantage in fine-tuning either one of these generative models or your own internal model for the domain that you're working in.
[2246.80 → 2254.60] So it's caching, but that's almost like a feedback or data curation side of things as well.
[2255.32 → 2259.92] So you mentioned earlier that validation was close to your heart.
[2259.92 → 2267.06] Yeah, so as our users know, I think part of the tooling that I'm building with Prediction Guard would fit into this category.
[2267.34 → 2270.68] It would actually span, I think, more categories.
[2270.68 → 2275.44] It kind of spanned between validation and orchestration and model hosting.
[2275.64 → 2278.20] So there's kind of a little bit of overlap there.
[2278.20 → 2287.26] But this validation layer really has to do with the fact that generative AI models across the board, I think people would say,
[2287.36 → 2294.78] there are a lot of concerns around reliability, privacy, security, compliance, what have you.
[2295.28 → 2301.52] And so there's a rising number of tools that are addressing some or all of those issues.
[2301.52 → 2308.04] So whether it be putting controls on the output of your LLM, again, think about this like a middleware layer.
[2308.58 → 2318.16] My LLM produces something harmful as output, or my generative AI model generates an image that is not fit for my users.
[2318.16 → 2323.10] I want to somehow catch that and correct it if I can, right?
[2323.10 → 2330.88] Or I want to put certain things into my model, but I want to make sure that I'm not putting in either private or sensitive data.
[2331.32 → 2339.30] Or I want to structure the output of my model in a certain way into certain structures or types like JSON or integer or float.
[2339.30 → 2350.74] All of these sorts of things kind of, I personally would break this apart probably into maybe like validation type and structure.
[2351.18 → 2354.56] And then like security related things, because there's a lot here.
[2354.70 → 2358.92] There's validation, which is like, is my output what I want it to be?
[2358.92 → 2369.90] There's security related things, which is, am I okay with putting the current request into my model and or sending the output back to my users?
[2370.12 → 2372.44] And then there's type and structuring things.
[2372.44 → 2378.06] So with images, like is the image upscaled appropriately for my use case?
[2378.06 → 2383.96] Or with text, if I'm putting in something and wanting JSON back, is it actually valid JSON?
[2384.46 → 2388.42] That's more of a structure type checking type of thing.
[2388.42 → 2390.86] So there's a lot in this category.
[2391.08 → 2395.68] And I think you can, you're probably getting the fact that I'm thinking a lot about this.
[2395.88 → 2397.98] And there's a lot here.
[2398.26 → 2408.50] But yeah, other things fitting into this category would, I think, cool one called Rebuff, which is doing kind of checking for prompt injections, for example.
[2408.62 → 2410.96] That's like part of that security side of things.
[2410.96 → 2420.84] There are things like prediction guard and guardrails, guidance outlines now that do type and structure type of things.
[2420.84 → 2434.94] There is also, I would say, a layer of this, which a lot of people are implementing in the kind of roll your own Python DIY way as well, which in prediction guard, we implement some of these.
[2434.94 → 2449.56] But also people are implementing them in their own systems, like self-consistency sampling, like calling a model multiple times and either choosing between the output or merging the output in some interesting way.
[2449.56 → 2452.80] Or things like that, this sort of consistency stuff.
[2452.92 → 2455.72] I think a lot of people are rolling their own too.
[2456.28 → 2458.68] What do you think as we start winding up here?
[2458.76 → 2462.38] What do you think are some of the takeaways from this chart?
[2462.66 → 2468.52] You know, or what brings top of mind things that people as they look at it might benefit from?
[2468.62 → 2469.86] How would you see it in the large?
[2469.86 → 2471.66] Yeah, that's a good question.
[2471.80 → 2482.46] I think one major takeaway, one thing to keep in mind is the model is only a small part of the whole app stack here.
[2482.54 → 2497.04] Similarly to like used to when a thing existed called data science, we would say training a model is only a very small part of the kind of end-to-end data science life cycle of a project.
[2497.46 → 2499.28] There are a lot of other things involved.
[2499.28 → 2507.94] And I think here, you know, you can make a similar conclusion that the tendency is to think of the model as the application, but there's really a lot more involved.
[2508.12 → 2515.44] And there's our friends over at Latent Space would say this is really where AI engineering comes into play.
[2515.58 → 2526.62] This space of AI engineering seems to be developing into a real thing, whether you call it that word or not, it is part of what this is.
[2526.70 → 2528.08] So that's one takeaway.
[2528.08 → 2539.16] I think the other takeaway is maybe just kind of forming this mental model around these three spokes of the stack.
[2539.16 → 2546.46] So you've got your app and app hosting, you've got your data and your resources, and you've got your model and your model middleware.
[2546.96 → 2558.76] And all that kind of middle hub would be some sort of orchestration that you're performing either in a DIY way or with things like Link chain to connect all of those pieces together.
[2558.76 → 2563.80] So you're probably hoarse by now because we've pulled so much information out of you.
[2563.92 → 2567.20] This was a really, perfect dive.
[2567.64 → 2578.00] You know, it's one particular publisher's way of looking at it, but we've never really dived into all the components of the infrastructure of a stack with this kind of.
[2578.00 → 2584.04] And I think most people haven't had a chance to see it yet because so much of this has really arisen in recent months.
[2584.04 → 2592.72] Thanks for kind of wearing half of a guest hat along the way here and taking us through this on this fully connected episode.
[2592.72 → 2599.78] Yeah, and I think in terms of learning about these things, I think people can check out our show notes.
[2599.98 → 2604.62] We'll have a link to the diagram that we've been discussing here.
[2604.86 → 2618.00] I would say learning wise, this helps you organize your thought process, but to really get an intuition around these things, you can look at various examples in this diagram and go to their docs and try out some of that.
[2618.00 → 2624.32] There's a variety of kind of end-to-end examples as well that are pretty typical these days.
[2624.52 → 2632.36] Like in language, if you're doing kind of a chat over your docs' thing, that involves a model and a data layer and an application layer.
[2632.54 → 2641.04] So just building one of these example apps, I think, could give people the kind of learning and that sort of thing that they need.
[2641.66 → 2643.06] But yeah, it's been fun.
[2643.30 → 2646.18] It's always helpful to talk these things out loud with you, Chris.
[2646.18 → 2648.02] So I find it very useful.
[2648.16 → 2649.96] Well, I learn a lot every time we do this.
[2650.00 → 2650.82] So thanks a lot, man.
[2651.16 → 2651.76] Yeah, yeah.
[2651.84 → 2653.16] We'll see you next week.
[2653.24 → 2653.98] See you next week.
[2662.70 → 2664.98] Thank you for listening to Practical AI.
[2665.62 → 2669.30] Your next step is to subscribe now, if you haven't already.
[2669.64 → 2675.78] And if you're a longtime listener of the show, help us reach more people by sharing Practical AI with your friends and colleagues.
[2676.18 → 2681.16] Thanks once again to Vastly and Fly for partnering with us to bring you all Change Talk podcasts.
[2681.76 → 2685.54] Check out what they're up to at Fastly.com and Fly.io.
[2685.94 → 2691.26] And to our Beat Freakin' Residence, Break master Cylinder, for continuously cranking out the best beats in the biz.
[2691.54 → 2692.46] That's all for now.
[2692.74 → 2693.86] We'll talk to you again next time.
[2693.96 → 2694.46] We'll see you next time.
[2694.46 → 2696.02] We'll see you next time.
[2696.02 → 2698.10] We'll see you next time.
[2698.10 → 2706.16] We'll see you next time.
[2706.16 → 2736.14] We'll see you next time.
