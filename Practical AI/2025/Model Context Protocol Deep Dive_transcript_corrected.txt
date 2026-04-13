[0.00 → 10.06] Welcome to Practical AI, the podcast that makes artificial intelligence practical, productive,
[10.40 → 11.46] and accessible to all.
[11.46 → 14.48] If you like this show, you will love The Change Log.
[14.70 → 19.52] It's news on Mondays, deep technical interviews on Wednesdays, and on Fridays, an awesome
[19.52 → 21.38] talk show for your weekend enjoyment.
[21.84 → 25.82] Find us by searching for The Change Log wherever you get your podcasts.
[26.32 → 28.36] Thanks to our partners at Fly.io.
[28.36 → 31.10] Launch your AI apps in five minutes or less.
[31.40 → 33.38] Learn how at Fly.io.
[44.08 → 49.14] Welcome to a fully connected episode of the Practical AI podcast.
[49.60 → 55.46] In these episodes where it's just Chris and me without a guest, we try to keep you up to
[55.46 → 61.02] date with a lot of different things that are happening in the AI industry and maybe share
[61.02 → 66.42] some tips and tricks or resources that will help you level up your machine learning and
[66.42 → 67.10] AI game.
[67.68 → 68.60] I'm Daniel Whiten ack.
[68.74 → 75.32] I am CEO of Prediction Guard, and I'm joined as always by my co-host, Chris Benson, who is
[75.32 → 78.52] a principal AI research engineer at Lockheed Martin.
[78.98 → 79.60] How are you doing, Chris?
[79.98 → 81.62] I'm doing perfect today, Daniel.
[81.62 → 83.60] We got some interesting stuff to talk about.
[83.98 → 84.18] Yeah.
[84.40 → 84.62] Yeah.
[84.70 → 87.86] You know, it's been, as always, an interesting season.
[88.14 → 93.76] You know, new model releases, new tooling, new frameworks.
[94.22 → 101.74] Of course, it does seem like 2025 is set to be the year of agentic AI.
[101.74 → 105.42] And it's what a lot of people are talking about.
[106.26 → 109.90] And, you know, of course, it keeps coming up for us.
[110.14 → 116.54] Is agentic AI impacting your world in any way, shape or form?
[117.10 → 120.04] Without giving away any of the stuff I'm not allowed to talk about.
[120.90 → 122.54] Yes, it is.
[122.94 → 124.12] Most definitely.
[124.44 → 124.68] Okay.
[124.68 → 125.12] Okay.
[125.12 → 134.02] So, yeah, I would say in a lot of ways, I see a bit of a pattern developing with our
[134.02 → 139.94] customers where it's kind of like they've done the rag thing.
[139.94 → 142.46] So, like a knowledge-based chatbot.
[142.94 → 149.60] They've done maybe a structured, you know, data interaction, maybe like text to SQL, something
[149.60 → 150.26] like that.
[150.26 → 153.86] Maybe they've created an automation.
[154.64 → 157.30] Like, hey, I'm going to drop this file in here.
[157.54 → 162.94] And these few things will happen, some of which are driven by an LLM.
[163.04 → 166.94] And then something will pop out the other end, or I'll email this person.
[167.44 → 171.24] So, they kind of start developing those individual assistants.
[171.98 → 178.04] And then I see them start to kind of have this light bulb moment of the layer on top of
[178.04 → 183.62] those individual assistants or tools, which I think we could generally call that agentic
[183.62 → 189.38] layer, which is now saying, well, I can interact with unstructured data.
[189.54 → 191.04] I can interact with structured data.
[191.42 → 193.62] I can interact with these automations.
[194.14 → 196.56] Maybe I can interact with other systems via API.
[197.30 → 204.64] How do I start tying those things together in interesting workflows and in various ways?
[204.78 → 205.88] That's sort of what I'm seeing.
[205.88 → 209.80] I don't know if you've seen that pattern as well.
[210.46 → 211.02] I have.
[211.16 → 215.14] And I just want to point out that you and I have been talking about, like, all of these
[215.14 → 216.88] things coming together for a while.
[217.10 → 219.72] We weren't before agentic came out.
[219.80 → 223.18] We weren't saying it was we weren't using the term because that's the term that ended up
[223.18 → 223.32] taking.
[223.68 → 227.06] But we kind of went through, you know, a lot of the generative thing.
[227.24 → 231.98] And we were kind of saying, OK, the next step is for a lot of these different architectures
[231.98 → 232.96] to tie back in.
[232.96 → 234.90] And we're definitely seeing that now.
[235.12 → 236.92] That it is, and it has a name.
[237.34 → 237.44] Yeah.
[237.46 → 238.38] And it has a name.
[238.38 → 240.94] And actually, it has a protocol.
[241.54 → 242.52] It has a protocol.
[242.68 → 242.78] Yeah.
[243.16 → 244.00] Nice segue.
[244.22 → 250.70] Or anyway, it has a developing protocol, which is definitely something I think we want to
[250.70 → 251.74] dig in today.
[251.74 → 257.44] Now that we can kind of we don't have a guest, we can take a step back a minute and just dig
[257.44 → 261.84] in a little bit to model context protocol.
[262.14 → 266.18] So where did you first see this pop up, Chris?
[266.18 → 272.92] Well, when Anthropic did the blog post, you know, and it started, you know, you started
[272.92 → 274.62] seeing it all over the place pretty quickly.
[274.88 → 277.72] So it was only hours after the blog post.
[277.72 → 279.38] And I'm sure it was the same for you.
[279.62 → 284.60] And then all the follow-up, you know, posts and articles have come out about it and everything.
[284.60 → 287.62] But that's yeah, it's it made a splash.
[288.28 → 288.40] Yeah.
[288.40 → 295.68] So technically, this was last, if I'm looking at the announcement date, right, this was last
[295.68 → 299.48] year, November 25th of 2024.
[300.64 → 306.54] Anthropic released an announcement introducing model context protocol.
[307.36 → 310.72] And of course, they wrote a blog post about it.
[310.72 → 318.20] It came from Anthropic, but then also linked to an open project model context protocol,
[318.32 → 320.60] which is just model context protocol at GitHub.
[321.02 → 327.50] There's a website model context protocol dot IO, which kind of talks about the specification
[327.50 → 328.62] and all of that.
[328.78 → 331.76] So there is this kind of origin with Anthropic.
[332.18 → 338.10] But I think from the beginning, Anthropic hope that this would be kind of more of a wide,
[338.10 → 341.06] a widely adopted protocol.
[341.82 → 346.92] And maybe we should talk about kind of the need for this first.
[347.26 → 351.40] We've talked a little bit about tool calling on the show before, Chris.
[351.98 → 357.54] I don't know if I don't know if you remember some of those discussions, but there's very
[357.54 → 358.16] often this.
[358.44 → 364.62] I think we even talked about this cringe moment of people talking about an AI model, you know,
[364.62 → 369.46] renting you a car or something like that and interacting with kayak dot com.
[370.42 → 373.78] Well, the AI model does not do this, right?
[373.94 → 381.48] Something else happens below the hood of that, which I think has been for some time maybe called
[381.48 → 388.58] tool calling or function calling, which is essentially the steps would be the LLM.
[388.58 → 394.94] You would give the LLM context for maybe the schema of the kayak dot com API.
[396.14 → 403.04] You would then ask a query and have the LLM generate the appropriate maybe JSON body to
[403.04 → 405.88] call the kayak dot com API.
[405.88 → 412.44] And then you would just use regular good old-fashioned code, you know, Python requests or
[412.44 → 420.60] what have you to actually execute the API call to the external tool and get a response.
[420.76 → 421.72] Does that flow?
[422.12 → 422.60] Yeah.
[422.88 → 425.52] Generally, you know, am I misspeaking anything?
[425.86 → 427.68] No, no, that's that's my understanding.
[427.68 → 433.72] There's a fair amount of kind of custom code, you know, that people would put in there to
[433.72 → 436.16] to glue those different aspects together.
[436.16 → 439.10] And it varied, it varied among organizations widely.
[439.70 → 439.80] Yeah.
[439.90 → 440.06] Yeah.
[440.06 → 446.30] So that's kind of the guess the stress or the stress point or the need that came about
[446.30 → 456.92] is that everyone saw, OK, maybe it's better if we plug in AI models to external tools rather
[456.92 → 459.44] than having the AI model do everything.
[459.76 → 459.96] Right.
[460.22 → 464.26] So there are certain things that AI models don't do very well.
[464.32 → 468.30] And when I say AI models, I'm kind of defaulting to gen AI models.
[468.30 → 471.52] And let's just zoom in on language models, large language models.
[471.96 → 478.84] They're not going to be your best friend in terms of doing a time series forecast, for
[478.84 → 481.88] example, maybe with a lot of data.
[482.14 → 483.58] But there are tools that do that.
[483.58 → 490.10] So what if I just leverage those tools via API and I could ask my, you know, agent, quote
[490.10 → 496.18] unquote, to give me a time series forecast of X and there's a tool under the hood that
[496.18 → 498.30] interacts with the database, pulls the data.
[498.64 → 503.52] Then there's a tool that makes the time series forecast and boom, you kind of tie these two
[503.52 → 503.90] together.
[503.90 → 510.16] And it looks like your AI system is doing the forecast, but really you're calling these
[510.16 → 511.48] external tools under the hood.
[511.48 → 514.94] The thing is, everybody has different tools.
[515.70 → 517.10] Everybody has different databases.
[517.52 → 519.10] Everybody has different APIs.
[519.38 → 521.14] Every product has different APIs.
[521.60 → 523.84] Everybody has different function code.
[524.64 → 533.32] And so similar, I think, to in the early days of the web, everybody was sort of posting
[533.32 → 539.60] things and creating their own directories of content on the web, their own formats of things.
[539.60 → 546.76] There was no protocol necessarily that everyone followed in terms of their usage of the internet
[546.76 → 547.88] or the web.
[548.06 → 550.88] But then there were protocols that were developed, right?
[550.94 → 551.70] Like HTTP.
[552.48 → 554.94] And now it's common practice.
[554.94 → 557.46] Like I have a web browser, right?
[557.46 → 563.18] And I can go to any website and I expect certain things to be served back to me from the web
[563.18 → 565.44] server that gives me the website.
[565.66 → 571.76] And those things should be in specific formats for my browser to interpret them and me to get
[571.76 → 572.42] the information.
[573.02 → 577.14] And so there's a protocol or a standard in place for each of those web servers.
[577.14 → 586.28] So when I visit Netflix or whatever, it's sending back similarly, let's say, structured or formatted
[586.28 → 594.66] or configured data to me as if I go to amazon.com, and I'm searching for products.
[594.86 → 599.40] This was not the case until recently with these tool calls.
[599.40 → 607.34] So an AI model, everybody was on their own to integrate tools into their AI models using
[607.34 → 614.00] whatever custom code, whatever custom prompts, whatever custom stuff, which means, Chris, if
[614.00 → 621.52] you have created a tool calling agent and I now want to use some of your tools that you've
[621.52 → 629.38] developed and I have my own tool calling agent, I may have to modify my agent to use
[629.40 → 637.02] your tools, or you may have to modify your tools to be compatible with my agentic framework.
[637.20 → 642.54] And that's kind of the situation that we've been in for some time, which I guess is painful,
[643.04 → 643.90] reasonably painful.
[644.56 → 644.88] It is.
[644.98 → 651.02] It's, you know, we've, we've talked about this general idea a number of times across a number
[651.02 → 651.58] of episodes.
[651.88 → 658.18] And it kind of, in my mind, it kind of comes back to that, that notion of the AI field maturing
[658.18 → 658.94] over time.
[659.40 → 663.92] And we've talked a lot about the fact that AI is not a standalone thing.
[664.10 → 669.22] It's in a software ecosystem of, of various capabilities, many of which become standardized.
[669.88 → 675.54] And, and I think this is yet another step of this field that we have been in and that
[675.54 → 680.56] is, you know, raging forward, maturing naturally in the way that it needs to go.
[680.66 → 685.88] You have, you know, now we have a protocol that operates as that standardized glue that we,
[685.88 → 686.70] that can be adopted.
[686.70 → 689.60] And everyone knows what to expect.
[689.70 → 695.20] Just a great analogy with HTTP, as you pointed out in terms of being, you know, you have a
[695.20 → 699.12] standard format, standard serialization, and you can plug right into it.
[699.26 → 702.18] So yeah, this is, this was good news from my standpoint.
[702.18 → 702.98] Yeah.
[702.98 → 708.78] And I think I had a ton of questions about this because it certainly impacts the world that
[708.78 → 709.94] I'm working in directly.
[710.28 → 710.62] Indeed.
[710.84 → 712.96] And it brings up all sorts of questions.
[713.24 → 717.44] So, you know, questions like, well, how do you build an MCP server?
[718.06 → 719.86] Who's creating MCP servers?
[719.86 → 723.24] What kind of model can interact with an MCP server?
[723.60 → 726.12] What, you know, payloads go back and forth?
[726.70 → 732.46] And so, so it may be worth just kind of digging into a couple of those things.
[732.86 → 740.96] So first off, it may be good to dig in a little bit to what kind of how an MCP system operates.
[741.42 → 745.94] And then that may make sense of some of the other things that we talk about in terms of
[745.94 → 748.70] models that can interact with MCP servers.
[748.70 → 753.20] So there's a series of great posts, which we'll link in the show notes.
[753.54 → 757.42] I encourage all of you to, you know, take a look at those mini posts.
[757.58 → 763.90] We'll of course post the main blog post for Anthropic, but also the protocol website,
[764.24 → 765.94] but a few of these blog posts as well.
[766.08 → 769.74] So one of the ones that I found that I really liked was from Phil Schmidt,
[770.32 → 772.30] model context protocol and overview.
[772.64 → 774.54] And this one is, is really useful.
[774.54 → 780.64] And I think it's useful because it helps you form a mental model for the various components
[780.64 → 782.98] and how they interact in one of these systems.
[783.38 → 786.82] So, you know, you might be in your car listening to this.
[786.90 → 790.22] I'll kind of talk through these main components because you might not be looking at the
[790.32 → 795.24] at the article, but they're in, in the system that's using MCP.
[795.24 → 800.26] There are hosts, there are clients, and then there are servers.
[801.28 → 807.60] So the host would be an application that, like the end user application.
[807.76 → 812.34] So let's say this is my code editor and my code editor under the hood somehow is going
[812.34 → 813.48] to use MCP stuff.
[813.48 → 817.06] I'm going to be coding, I'm going to be vibe coding, right?
[817.22 → 822.28] And, you know, ask for various things, and it's going to interact, you know, in the, in the
[822.28 → 826.14] ID somehow and cause things to happen.
[826.38 → 830.64] So that's the that's the host, the sort of end user application.
[831.04 → 839.04] There's a client which lives in, inside the host application, which is an MCP client, meaning
[839.04 → 846.30] this client might be a library, for example, that knows how to do MCP things.
[846.30 → 853.46] Like, like an analogy would be in Python, I can import the request package, which knows
[853.46 → 858.30] how to execute HTTP calls back and forth to web servers.
[858.58 → 864.84] Think about the client, maybe an MCP client as a similar thing that lives within your application
[864.84 → 872.10] and knows how to do this back and forth with MCP servers instead of web servers.
[873.04 → 881.32] And then the servers are those external programs or tools or resources that you reach out to
[881.32 → 882.24] from the client.
[882.80 → 889.86] And those expose, like I say, tools, resources, prompts over this sort of standardized API.
[889.86 → 893.94] So this is, you know, it's a client server architecture.
[894.36 → 897.92] The client lives within the host, which is the end user application.
[898.34 → 904.22] And then there's the server, which you could, you know, think of again as this MCP server.
[904.34 → 910.44] Now we could, we should talk a little bit about, you know, what the MCP server does, but you could
[910.44 → 919.16] think about the client as invoking tools, you know, making requests for resources, making requests
[919.16 → 921.52] for prompts or prompt formats or templates.
[921.52 → 926.30] The MCP server is exposing those tools, resources, and prompts.
[926.56 → 927.88] Does that make, does that make sense, Chris?
[928.24 → 928.76] It does.
[928.88 → 933.98] I mean, it is a essentially it's kind of a new form of middleware in that sense, you know,
[934.04 → 939.14] for, for those who, and I realize that term may not resonate with everybody that's listening,
[939.38 → 946.24] but that's a kind of classical term of that, the notion of connecting different aspects
[946.24 → 952.06] of services and systems together in a way to try to simplify and standardize.
[952.78 → 956.84] And so, you know, I, I, it's, it's a different way of putting, of putting it, but yeah.
[956.96 → 957.08] Yeah.
[957.16 → 957.34] Yeah.
[957.34 → 958.22] I think that's a great way.
[958.28 → 966.52] Even Phil and his, in his blog post has this kind of MCP in the middle as this mediator.
[966.52 → 968.70] So I think that that's a that's a good analogy.
[968.70 → 972.54] And, you know, we mentioned tools, resources, and prompts.
[973.02 → 982.34] So an MCP server, you know, within the specification of the protocol can expose tools, resources,
[982.34 → 983.50] or prompts.
[983.88 → 989.92] So the tools are maybe things like we already talked about with the Kayak API or calling into
[989.92 → 990.54] a database.
[990.54 → 997.22] They are functions that can perform certain actions, like calling a weather API to get
[997.22 → 1002.44] the current weather, or like I mentioned, you know, booking cars, or there's MCP servers
[1002.44 → 1006.14] that will help you perform GitHub actions right on your code base.
[1006.82 → 1010.60] So these are the tools or the functions that are, that are exposed.
[1010.74 → 1013.42] So that's thing one that an MCP server can expose.
[1013.90 → 1020.52] Thing two would be resources, which you could think of as data sets or data sources.
[1020.54 → 1023.80] That, that an LLM can access.
[1024.54 → 1030.86] So, you know, things that you want to expose either as configuration context or data sets
[1030.86 → 1032.84] to the, to the application.
[1033.26 → 1035.26] And then the third would be prompts.
[1035.26 → 1043.10] And these would be kind of predefined templates that the agent can use to operate in an optimal
[1043.10 → 1043.44] way.
[1043.44 → 1050.52] So let's say that you're, let's say that your tools in your MCP server are related to
[1050.54 → 1052.92] kind of question, answer, and knowledge discovery.
[1052.92 → 1059.76] You might have some pre-configured question and answer prompts that the LLM could use that,
[1059.76 → 1065.44] you know, would be optimized for a certain scope of work or something.
[1065.60 → 1067.20] You could think about it like that.
[1067.32 → 1073.18] So these are tools, resources, and prompts that are exposed in the MCP server.
[1073.68 → 1074.52] Does that make sense?
[1075.06 → 1075.44] It does.
[1075.44 → 1080.04] I know in that particular article, you pointed out one of the things that I had really keyed
[1080.04 → 1085.92] in on that, that helped me kind of grok that immediately was that tools are model controlled,
[1086.12 → 1088.92] resources are application controlled, and prompts are user controlled.
[1088.92 → 1092.02] And that was easy enough for me to wrap my mind around quickly.
[1092.60 → 1095.68] So yeah, that's a great explanation from you there.
[1096.20 → 1096.36] Yeah.
[1096.52 → 1097.32] Yeah, definitely.
[1097.32 → 1105.82] So then there's kind of a couple of things that are possible in the interaction between model
[1105.82 → 1109.30] client or MCP client and MCP server.
[1109.76 → 1119.54] One of the things is an application needs to understand how to connect and initialize a
[1119.54 → 1123.82] connection with an MCP server and sort of open that connection.
[1123.82 → 1131.74] That can happen over, you know, standard input output, meaning your server might be running
[1131.74 → 1138.88] locally or, you know, as part of an application, or it may be running remotely, and you could
[1138.88 → 1143.02] interact via server sent events back and forth to the server.
[1143.38 → 1147.60] But then you also need to execute a kind of discovery process.
[1147.60 → 1155.00] I was thinking back to the good old microservices days, Chris, which you may, you know, fondly
[1155.00 → 1156.36] or not fondly recall.
[1156.66 → 1159.28] A bit of both, depending on what I was doing.
[1159.76 → 1166.12] This made me think of microservices sort of discovery things where it's like, hey, what
[1166.12 → 1172.36] services in my big microservices' environment, how do I discover where those are at and what
[1172.36 → 1175.52] domain I connect to them on and those sorts of things?
[1175.98 → 1176.76] What are they?
[1176.76 → 1178.98] So this was a whole topic.
[1179.14 → 1180.86] I guess it maybe still is a whole topic.
[1181.06 → 1190.16] But there's this discovery type of mechanism where you can, in the between the MCP server
[1190.16 → 1196.74] and the MCP client, actually expose kind of a list of tools or a list of prompts or a list
[1196.74 → 1197.40] of resources.
[1197.72 → 1200.44] And those are discoverable to the AI application.
[1200.44 → 1203.16] So it knows what it can do.
[1203.40 → 1204.70] You know, can I book a car?
[1204.70 → 1208.90] Or no, I can't because that's not exposed as part of the MCP service.
[1209.00 → 1214.04] But maybe I can do GitHub related stuff, or maybe I can do, you know, database related
[1214.04 → 1215.64] stuff or whatever that is.
[1216.08 → 1216.72] All right, Chris.
[1216.80 → 1222.12] So we've talked a little bit about MCP clients and MCP servers.
[1222.12 → 1230.26] There's certainly much more that is available to talk about and dig into in the protocol
[1230.26 → 1231.76] itself.
[1232.26 → 1235.02] And, you know, we've scratched a little bit of the surface here.
[1235.10 → 1237.38] We're not going to go through the whole protocol on the podcast.
[1237.38 → 1240.06] Maybe that's a relief to our listeners.
[1240.48 → 1242.60] But there is a whole protocol there.
[1242.60 → 1248.60] I think it would be good to talk, though, about kind of two additional things, which immediately
[1248.60 → 1258.30] popped into my mind when I saw Anthropic releasing MCP and talking about it is, number one, how do
[1258.30 → 1265.18] I create an MCP server, or where do I get access to MCP servers to tie into my own AI system?
[1265.18 → 1270.40] And then secondly, well, what if I don't use Anthropic models?
[1270.66 → 1272.24] Can I use MCP?
[1272.96 → 1278.78] Those were, you know, two immediate questions from my end.
[1279.26 → 1288.00] And I don't know, Chris, if you've seen, you know, there are various GitHub repos that are
[1288.00 → 1293.98] popping up and also examples of various MCP servers.
[1293.98 → 1297.00] Have you seen any that are interesting to you?
[1297.46 → 1303.98] The one that's most interesting to me, because when I'm not focused on, you know, AI with Python
[1303.98 → 1306.66] specifically, I'm very focused on Edge with Rust.
[1307.06 → 1310.62] And there's an official Rust SDK for the model context protocol.
[1310.82 → 1314.00] So that is that's naturally where I gravitated to.
[1314.68 → 1314.86] Yeah.
[1315.00 → 1315.22] Yeah.
[1315.32 → 1317.98] So there's and there's Python implementations.
[1318.78 → 1322.30] I think there's many programming language implementations.
[1322.30 → 1327.48] There's also sort of example servers that are kind of prebuilt.
[1327.76 → 1336.70] I've seen various ones for like Blender, which is a 3D kind of modelling animation type of thing,
[1337.04 → 1337.80] which is open source.
[1337.98 → 1338.58] Yeah, exactly.
[1338.58 → 1346.20] And then Ableton Live, which is a platform that is like a music production platform.
[1346.52 → 1348.04] There are ones for GitHub.
[1348.30 → 1349.38] I already mentioned that.
[1349.58 → 1352.30] Unity, the game development engine.
[1352.80 → 1359.42] There are ones that can control your browser integration with Zapier, all sorts of things.
[1359.42 → 1365.06] So people have already created many, many of these MCP servers.
[1365.28 → 1377.08] And again, when you're creating this MCP server, basically, you just have to create essentially a could think of it like a web server that has various routes on it.
[1377.08 → 1387.12] But these are specific routes that expose specific sorts of things, these tools, resources and prompts over a certain protocol.
[1387.12 → 1394.10] And there is communication back, for example, back and forth of JSON, for example, over servers and events.
[1394.72 → 1397.74] But, you know, again, there's a specific protocol that's followed.
[1398.30 → 1409.40] Now, you can look through all the specific details of the protocol if you want to, say, create a model context protocol server for your tool.
[1409.40 → 1411.68] And I actually wanted to do this.
[1411.82 → 1416.56] So we have an internal tool that we use for doing text to SQL.
[1416.80 → 1418.12] It's very frequent.
[1418.30 → 1422.02] I often call it the kind of dashboard killer app.
[1422.22 → 1426.68] It's like, you know, everyone's created tons of dashboards that no one uses in their life.
[1426.92 → 1432.76] And, you know, wouldn't it be better if you could just connect to your database and ask natural language questions?
[1432.76 → 1442.02] So we have a whole API around this and, you know, you can add your database schema information and all sorts of fun things and do natural language query.
[1442.02 → 1449.70] And so there's like, I don't know, six or seven different endpoints in this kind of simple little API that does structured data interaction.
[1449.92 → 1451.44] So I'm like, OK, cool.
[1452.00 → 1455.14] We've written that with fast API, which is awesome.
[1455.88 → 1457.00] So it's a web server.
[1457.00 → 1470.36] However, it has certain endpoints, right, that allow you to do the SQL generation or allow you to modify database information or allow you to do various elements of this operation.
[1471.04 → 1474.58] And we utilize that as a tool internally via tool calling.
[1474.72 → 1482.34] So I thought, well, what would it take for me to convert that into an MCP server that I could plug into an agent?
[1482.34 → 1489.80] Well, you could kind of do that more or less from scratch, just following the protocol.
[1490.62 → 1494.16] But people have already started coming up with some really great tooling.
[1494.40 → 1497.06] So there's a thing called fast API MCP.
[1497.62 → 1511.80] So if you just search for that, this is a Python framework that essentially works with fast API and basically converts your fast API web server into an MPC server or MCP server.
[1511.80 → 1513.34] And it works.
[1513.34 → 1529.94] So, you know, from my experience, I just added a few lines of code to my fast API endpoint, wrapped my fast API application in this framework and then ran the application, which is, again, this fast API application.
[1529.94 → 1540.24] And that was immediately discoverable as an MCP server, meaning that I could, if I had an AI system, which we'll talk about that bit here in a second.
[1540.24 → 1561.80] If I had an AI system that could interact with MCP servers, my service now, the text to SQL system that we use, would be available to that agent to use as a potential tool that's plugged into, you know, a database that we would connect it to.
[1562.16 → 1562.90] Does that make sense?
[1563.16 → 1563.58] It does.
[1563.72 → 1564.56] That was a good explanation.
[1564.56 → 1564.96] Yeah.
[1565.12 → 1570.94] So I'm sure also, I mean, you mentioned this Rust client that you talked about.
[1571.04 → 1578.38] I imagine a similar thing is possible there with a bunch of convenience functions and that sort of thing.
[1578.50 → 1581.68] I don't know Rust quite as well, but I imagine that's the case.
[1582.22 → 1582.84] It is.
[1582.84 → 1591.62] And it's one of those, I love the fact that MCP is rapidly gaining so much language support off the bat.
[1591.84 → 1594.12] I think you've heard me say this before.
[1594.24 → 1600.70] One of my pet peeves is kind of the Python only nature of a lot of AI.
[1600.86 → 1601.76] At least it starts there.
[1601.76 → 1613.14] And I think I've said in previous episodes, it's a maturity thing when you can get to where you're supporting lots of different approaches to accommodate the diversity that real life tends to throw at us.
[1613.64 → 1614.16] That's good.
[1614.26 → 1617.86] I love, and MCP has shot up that very, very quickly.
[1618.08 → 1629.72] So yeah, in the world that I'm in, you know, playing it, kind of combining MCP as a protocol that works at the edge as well as in the data centre is a big deal for me.
[1629.72 → 1634.00] Yeah, and it does actually work also kind of single node.
[1634.26 → 1637.26] I mean, we've talked about client server, right?
[1637.68 → 1649.54] But you can run an MCP quote server in this sort of embedded way that is discoverable in a desktop application or in a single node application.
[1649.74 → 1657.72] So there's certainly no, so I guess what I mean is if you're using MCP and this is security and authentication related,
[1657.72 → 1663.62] it doesn't mean that you need to connect over the public internet to an MCP server.
[1664.28 → 1671.66] And it doesn't mean that all of that is unauthenticated, or you can't apply security of any type.
[1672.08 → 1676.58] What it does mean is that if you are, for example, in the example that I gave,
[1677.08 → 1682.38] so I've now converted our text to SQL engine into an MCP server.
[1682.38 → 1687.84] I can plug in a database connection to that, connect to a database.
[1688.32 → 1696.28] But depending on how I set up the connection to the database, there could be potential problematic vulnerabilities there.
[1696.60 → 1706.18] And if I don't have any authentication on my MCP server, you know, and I put that on the public internet, anyone could use it.
[1706.18 → 1714.66] So there are two levels of kind of security or authentication or, you know, threat protection that's relevant here.
[1714.78 → 1719.70] One is the actual connection level authentication to the MCP server.
[1719.96 → 1724.10] And the other is, well, I can still create a tool that's vulnerable, right?
[1724.14 → 1726.90] Or has more agency than it should.
[1726.90 → 1727.54] Yeah.
[1728.06 → 1740.84] I think one of the things I love about that call out from you is that, you know, you can be operating on that one physical device and tying various systems together.
[1740.84 → 1756.68] And just like if you take it outside the AI world, and you talk about protocols that we are commonly using, you mentioned HTTP earlier, you know, protocols are really common and things, you know, you may be using all of those other ones that we've been using for years on one device.
[1756.68 → 1760.64] It doesn't mean that there are, by definition, many services in many different remote places.
[1760.78 → 1762.96] It can all be collected there.
[1763.56 → 1774.66] And it still brings value because you still have that standardization and the various vendors, whether they be commercial or open source, can provide interfaces to that to make it easier.
[1774.80 → 1781.08] So it becomes a much more pluggable and yet not tightly integrated, which is a good thing, architecture.
[1781.08 → 1787.28] And I think MCP really gives us that same capability now in this space.
[1787.56 → 1801.04] And so it's, like I said, it really is pushing it up the maturity, you know, up the maturity level from we're all writing custom glue code to now, hey, I'm going to standardize on MCP and away we go.
[1801.04 → 1809.92] Yeah, and I think similar to people can carry over some of their intuitions from working with web servers into this world.
[1810.46 → 1821.06] Like you wouldn't necessarily just download some code from GitHub and expect there to be no vulnerabilities in it when you run that server, you know, locally.
[1821.06 → 1823.26] Same goes with MCP, right?
[1823.44 → 1831.56] You would definitely want to know what you're running, you know, what's included, where you're running it, how authentication is set up, et cetera, et cetera.
[1832.14 → 1840.04] Similarly, if you're connecting to someone else's MCP server, like Chris, you're running one, and I want to connect to it.
[1840.48 → 1848.22] Depending on the use case that I'm working with, I may very much want to know what data does your MCP server have access to?
[1848.22 → 1852.84] How are you logging, caching, storing information, et cetera, et cetera?
[1853.38 → 1854.56] You know, is it multi-tenant?
[1854.64 → 1856.56] Is it single-tenant, et cetera, et cetera?
[1856.78 → 1868.76] So you can bring some of those intuitions that you have from working in the world that we all work in, which involves a lot of, you know, client-server interactions, and bring that into this world.
[1869.34 → 1872.82] Okay, Chris, we've talked about MCP in general.
[1872.82 → 1878.78] We've talked about creating MCP servers or the development of them.
[1879.02 → 1890.42] There's one kind of glaring thing here, which is Anthropic released or announced this model context protocol, and certainly others have picked up on it.
[1890.94 → 1899.44] And you see OpenAI also now supporting MCP, where before they had this kind of their version of tool calling in the API.
[1899.44 → 1908.02] So there's a more general question here, which is, well, I'm using Llama 3.1 or DeepSeek.
[1908.14 → 1911.62] Can I use model context protocol?
[1911.72 → 1926.04] And more generally, like as models proliferate, which they are, and people really think about being model agnostic, meaning they're building systems where they want to switch in and out models.
[1926.04 → 1932.00] Do I have to use Anthropic or now OpenAI to use MCP?
[1932.58 → 1943.42] So the answer to this question, at least as far as, you know, what we've discovered in our own work is, as of now, sort of yes and no.
[1943.84 → 1948.14] But in the future, definitely there will be flexibility to many things.
[1948.14 → 1964.04] So what I mean by that is Anthropic has a kind of head start, in a sense, in the same way that OpenAI has released certain things, you know, like various agent protocols or tool calling or stuff.
[1964.14 → 1967.38] And they had, you know, it was something they released, right?
[1967.42 → 1970.92] Something they had been working towards, and they had maybe an advantage initially.
[1970.92 → 1974.12] So Anthropic obviously has been working towards this.
[1974.60 → 1978.78] Their models, their desktop application, et cetera, supports it well.
[1979.48 → 1984.54] Others are kind of playing a little bit of catch up and that would include kind of open models.
[1984.72 → 1991.58] So if you think about something like a Llama 3.1 or, you know, Quinn 2.5 or whatever model you're using,
[1991.58 → 2002.68] those open models, there's nothing preventing them from generating model context protocol aligned things.
[2003.22 → 2003.40] Agreed.
[2003.50 → 2009.54] But they haven't necessarily been trained as part of their training data set to generate those things.
[2009.54 → 2016.94] Meaning you can have an open model that generates what you need for model context protocol interactions,
[2016.94 → 2029.92] but you're probably going to have to load the prompt of that open model with many, many examples of model context protocol and information about it for it to be able to generate that, which is totally fine.
[2030.06 → 2030.80] You can do that.
[2031.00 → 2036.52] And we've done that internally, and I've talked to others who have and there's blog posts about it, et cetera.
[2036.98 → 2038.54] So there's nothing in that sense.
[2038.60 → 2039.66] That's why I say yes and no.
[2039.72 → 2045.10] There's nothing preventing you from doing this with open models right now or models other than Anthropic.
[2045.10 → 2058.94] You might just have to kind of load that context window with many, many examples that are MCP related and aligned for you to generate consistent output for MCP servers.
[2059.44 → 2063.84] But what will happen similar to what happened with tool calling.
[2064.02 → 2067.70] So if you remember, you know, tool calling was released.
[2068.66 → 2071.22] Everybody, the progression, I kind of see it this way.
[2071.22 → 2075.50] It's like people found out there have been a lot of cases of this.
[2075.60 → 2080.58] People found out that models generally can follow instructions.
[2081.40 → 2092.06] And so at a certain point, people developed prompt formats like Alpaca, Chat ML, et cetera, that had like a generalized form of instruction following.
[2092.06 → 2094.30] And those generally got more standardized.
[2094.76 → 2107.14] And now all training sets, well, not all training sets, but many training sets for kind of the main families of models like LAMA and others include instruction following examples.
[2107.88 → 2110.16] Then people started doing tool calling.
[2110.16 → 2125.76] And then people started developing tool calling specific examples to include in their data sets that they're using for models, including like tool calling formats, which are in kind of like Hermes and other data sets now.
[2126.26 → 2131.42] And so now many models do have tool calling examples in their training data sets.
[2131.72 → 2135.42] Now we're going to have the exact same progression with MCP.
[2135.42 → 2141.14] People can do MCP right now with open models if they kind of perform in a certain way.
[2141.26 → 2151.88] It will become more efficient, though, as MCP examples are then included in training data sets for open and other closed models moving forward.
[2152.06 → 2156.10] So it's kind of now and not yet situation.
[2156.58 → 2157.30] Yeah, I agree.
[2157.50 → 2163.48] I mean, and at the end of the day, there'll be, you know, different organizations will go both ways.
[2163.48 → 2167.02] Some are just going to say, let's adopt MCP outright.
[2167.72 → 2178.38] Others, you know, other like the open AIs, you know, and that that tier of providers, some of them will open source their own approaches to try to compete.
[2178.76 → 2182.60] And the marketplace will, you know, people will try it out.
[2182.60 → 2197.08] And based on, you know, things like, you know, providing examples that make it easy, there'll be a certain amount of kind of all the things competing and probably something will kind of shake out as more popular than the others in the line because this is what we see over and over in software.
[2197.08 → 2211.62] And there'll also be a point where any that are genuine contenders, you'll have servers that support both MCP and all those top contenders with examples of each until it becomes clear kind of what the world is going to go do.
[2211.62 → 2224.50] So I think, yeah, I think Anthropic was smart to do this, and they got a leg up, and they put out a high quality protocol with a lot of great examples and SDKs right off the bat.
[2224.50 → 2230.74] And that was a smart thing to do to try to kind of win the marketplace very early in the game.
[2230.86 → 2232.66] So it'll be interesting to see how that.
[2232.72 → 2254.32] But I think that the key point that I'm trying to make is and that you're making clearly is that the world has changed in that way, in a small way, in terms of, you know, everyone's going to now have to level up into having this kind of AI specific middleware that ties the model into all the resources, the resourcing and tooling and prompting that it needs.
[2254.50 → 2260.64] So, um, I'm, I'm very happy to see it come into place, and we'll see some shake out in the must come.
[2261.12 → 2266.24] Yeah. Yeah. Well, I, um, I definitely am interested to see how things develop.
[2266.34 → 2272.72] There are certainly toolkits of all kinds that are, that are developing, and maybe I can share a couple of those.
[2272.72 → 2275.88] And, and Chris, uh, you could share the, the rest one.
[2275.98 → 2284.02] And I think you had another rest resource that you wanted to share, but, but the ones that I were really was, um, using from the Python world.
[2284.02 → 2296.40] If people want to explore those and, and look at those a little bit more, the one, if you're a fast API user, then I would definitely recommend that you look at fast API dash MCP.
[2296.40 → 2298.78] Yep. Um, that's the framework that I use.
[2298.78 → 2307.74] You can, I am imported, uh, or inserted three lines of code into my, into my fast API app and was up and running.
[2307.74 → 2313.24] Now you may want to kind of modify a few more things than that eventually, but that will get you up and running.
[2313.24 → 2322.20] The, the other thing that was helpful for me is there is actually, um, an MCP inspector application.
[2322.20 → 2332.80] So one of the things like, for example, in fast API, I like is you can spin up your application, and you immediately have API documentation that's in swagger format.
[2332.80 → 2334.42] You can go and look at that.
[2334.42 → 2350.72] Um, well, the MCP inspector can help you check if your, you know, connect to your MCP server, validate which tools are listed, um, execute example interactions, see what's successful, see what's returned from the MCP server, all of those sorts of things.
[2350.72 → 2359.32] So very useful little tool that is actually also linked in the fast API dash MCP documentation as well.
[2359.88 → 2363.70] And, um, Chris, uh, you, you had mentioned, uh, a rust client.
[2363.82 → 2366.04] I'm sure there are a lot of other ones that are out there.
[2366.12 → 2372.92] I am intrigued kind of generally, you know, you, you've been exploring this rust world quite a bit.
[2373.00 → 2376.86] We would love to hear any resources that you've been exploring there.
[2376.96 → 2377.96] People might be interested.
[2378.58 → 2380.28] Yeah, there, there's one that I'll mention.
[2380.28 → 2390.06] And, uh, it's separate from MTV, but it's kind of, it's one that I think is very interesting, uh, for inference at the edge in particular, it's hosted at hugging face.
[2390.06 → 2393.26] It's called candle as in, I think like a candlestick.
[2393.76 → 2400.20] Um, and you can find it, and it is, uh, it advertises itself as a minimal ML framework for rust.
[2400.68 → 2409.88] Um, but it's really caught my attention because as I'm often, you know, advocating for edge context and edge, you know, use cases.
[2409.88 → 2418.42] Uh, where we're getting AI out of the data centre strictly and, and, and doing interesting things out there in the world that may be agentic, maybe physical.
[2418.80 → 2422.12] Um, as we go forward, uh, candle is an interesting thing.
[2422.12 → 2429.18] And, uh, uh, uh, if we're lucky, we might have an episode in some point in the future where we can kind of dive into that in some detail.
[2429.18 → 2439.08] But if you're, if that, if edge, uh, and, and high performance minimalist things are interesting to you in this context, uh, go check out candle at hugging face.
[2439.08 → 2448.76] Yeah. Yeah. Encourage people to do that. All the crust crustaceans out there. Isn't that the, uh, the rust stations.
[2449.56 → 2451.42] That's right. Yeah, exactly.
[2451.42 → 2453.14] It's a crustacean theme though. You're right.
[2453.36 → 2464.00] Yes. Okay, cool. We'll definitely check that out. As I mentioned, we'll share some notes in our, in our show notes with links to all the blog posts.
[2464.00 → 2483.14] We've been talking about the MCP protocol, the Python and rust tooling. So check that out, try it out. Um, start, start making and, and creating your own MCP servers and let us know on, you know, LinkedIn or X or wherever, um, what cool MCP stuff you, you start building.
[2483.52 → 2486.60] And, um, and we'll see you next time. Great talking, Chris.
[2486.82 → 2488.38] Good talking to you. See you next time, Daniel.
[2494.00 → 2516.08] All right. That is our show for this week. If you haven't checked out our change log newsletter, head to changelog.com slash news. There you'll find 29 reasons. Yes. 29 reasons why you should subscribe. I'll tell you reason number 17. You might actually start looking forward to Mondays.
[2516.08 → 2518.96] Sounds like somebody's got a case of the Mondays.
[2518.96 → 2532.88] 28 more reasons are waiting for you at changelog.com slash news. Thanks again to our partners at fly.io to Break master Cylinder for the beats and to you for listening. That is all for now, but we'll talk to you again next time.
