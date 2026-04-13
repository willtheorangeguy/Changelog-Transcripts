[0.00 → 8.74] Welcome to the Practical AI Podcast, where we break down the real world applications
[8.74 → 13.64] of artificial intelligence and how it's shaping the way we live, work, and create.
[13.88 → 19.14] Our goal is to help make AI technology practical, productive, and accessible to everyone.
[19.48 → 23.54] Whether you're a developer, business leader, or just curious about the tech behind the
[23.54 → 25.12] buzz, you're in the right place.
[25.12 → 29.84] Be sure to connect with us on LinkedIn, X, or Blue Sky to stay up to date with episode
[29.84 → 33.02] drops, behind the scenes content, and AI insights.
[33.36 → 35.88] You can learn more at practicalai.fm.
[36.00 → 37.50] Now, on to the show.
[39.72 → 44.32] Well, friends, when you're building and shipping AI products at scale, there's one constant.
[44.96 → 45.44] Complexity.
[45.84 → 50.58] Yes, you're wrangling models, data pipelines, deployment infrastructure, and then someone
[50.58 → 53.06] says, let's turn this into a business.
[53.56 → 54.84] Cue the chaos.
[55.04 → 59.64] That's where Shopify steps in, whether you're spinning up a storefront for your AI-powered
[59.64 → 62.78] app or launching a brand around the tools you've built.
[63.14 → 68.50] Shopify is the commerce platform trusted by millions of businesses and 10% of all U.S.
[68.60 → 69.04] e-commerce.
[69.32 → 73.50] From names like Mattel, Gymshark, to founders just like you.
[74.08 → 79.70] With literally hundreds of ready-to-use templates, powerful built-in marketing tools, and AI that
[79.70 → 84.28] writes product descriptions for you, headlines, even polishes your product photography.
[84.82 → 86.44] Shopify doesn't just get you selling.
[86.44 → 88.32] It makes you look good doing it.
[88.72 → 89.44] And we love it.
[89.66 → 90.84] We use it here at Changelog.
[91.04 → 93.46] Check us out, merch.changelog.com.
[93.66 → 94.96] That's our storefront.
[95.36 → 97.28] And it handles the heavy lifting, too.
[97.60 → 101.78] Payments, inventory, returns, shipping, even global logistics.
[102.44 → 106.34] It's like having an ops team built into your stack to help you sell.
[106.34 → 109.52] So if you're ready to sell, you are ready for Shopify.
[110.12 → 116.80] Sign up now for your $1 per month trial and start selling today at Shopify.com slash practical
[116.80 → 117.22] AI.
[117.90 → 122.46] Again, that is Shopify.com slash practical AI.
[122.46 → 140.90] Welcome to another episode of Practical AI.
[141.30 → 142.36] I'm Daniel Whiten ack.
[142.48 → 148.70] I am CEO at Prediction Guard, and I'm joined as always by my co-host, Chris Benson, who is
[148.70 → 151.88] a principal AI research engineer at Lockheed Martin.
[151.88 → 152.92] How are you doing, Chris?
[152.96 → 153.60] It's been a while.
[153.96 → 154.86] It's been a little bit.
[154.94 → 155.98] It's good to talk to you.
[156.14 → 161.76] I was gone for a brief period, but I'm back all safe and secure now.
[162.34 → 168.12] Yes, completely reversed back to where you normally are.
[168.24 → 168.88] Ba-doom-boom.
[169.06 → 175.66] And for a great conversation because we have a great previous guest who I got to talk with
[175.66 → 181.06] in London, one of the last times I was over on that side of the pond.
[181.48 → 188.94] And now I get to catch up with Donate Capella, who is principal security consultant at Reverse Sec.
[189.00 → 189.84] How are you doing, Donate?
[190.16 → 191.70] Very, very good.
[191.80 → 192.44] Thank you.
[192.56 → 193.98] And I'm so happy to be back.
[194.32 → 195.00] Yeah, yeah.
[195.18 → 195.94] Same here.
[195.94 → 201.70] I feel like the AI world is in some ways the same and in many ways different from when
[201.70 → 203.28] we chatted last.
[203.68 → 205.30] What's life been like for you?
[206.12 → 210.76] It's definitely been very, very busy for us.
[210.98 → 213.82] Our company has obviously changed.
[213.82 → 217.94] We now are Reverse Sec, the same people, but we separated.
[218.84 → 224.82] But as part of that, we've been doing a lot of Gen AI cybersecurity work.
[225.60 → 231.12] I think our pipeline has tripled in size, and we've been doing a lot of research.
[231.40 → 238.44] I am actually just back from Canada where I was presenting our research at Black Cat in
[238.44 → 239.06] Toronto.
[239.06 → 246.48] And before that, I was at another conference in Stockholm called Secure AI, a complete two
[246.48 → 249.34] days just focused on Gen AI security.
[249.56 → 251.18] I mean, we were presenting our research.
[251.30 → 257.50] There was Open AI there, Microsoft, a lot of hugging face, talking about MCP, protocol
[257.50 → 258.00] security.
[258.14 → 259.90] So, so much was happening.
[260.48 → 263.00] And so for us, it's been incredibly busy.
[263.00 → 268.88] And just like literally half an hour before I finished running one of the training course
[268.88 → 275.16] that we do on Gen AI security for our consultants so that we can have more people that can deliver
[275.16 → 279.46] the work, which is full of energy for me to do that.
[279.56 → 281.80] Like there are a lot of young people there.
[282.16 → 286.04] So it's been busy, lots of work, lots of research.
[286.50 → 287.58] So lots of travel.
[288.26 → 289.20] What more to say?
[289.20 → 289.84] Yeah.
[289.84 → 290.20] Yeah.
[290.20 → 290.32] Yeah.
[290.32 → 290.68] Yeah.
[290.68 → 297.56] And what, I mean, last time we talked, certainly we talked a lot about LLMs, prompting LLMs,
[297.72 → 298.12] et cetera.
[298.92 → 307.00] There's now this kind of additional layers or frameworks or approaches to developing AI
[307.00 → 307.80] applications.
[307.80 → 314.60] From your perspective, just in terms of, I'm always curious about this because some of
[314.60 → 320.88] us that are so kind of into the AI world and not constantly in front of real world, you
[320.88 → 326.70] know, enterprise companies, we have maybe a warped view of like, oh, everybody's creating,
[326.98 → 330.60] you know, agents using MCP or something.
[330.60 → 338.72] What is the reality on the ground as far as you see it of kind of the core AI use cases
[338.72 → 345.20] that people are often thinking about in terms of not only security, but just in terms of
[345.20 → 346.20] adoption and scale?
[346.56 → 354.46] And then what has, what is maybe actually shifting in terms of those use cases from your perspective,
[354.74 → 355.46] at least?
[355.46 → 361.18] I mean, if you asked me this question last year, and you probably asked me this question,
[361.48 → 369.44] I would have said the majority, the majority of our clients were doing rag on documents
[369.44 → 371.34] that were internal chatbots.
[371.52 → 376.54] There was a few of them that were starting to look at agentic workflows.
[377.26 → 384.10] Now, fast-forward to today, a lot of the stuff we test is agentic in one way or the
[384.10 → 384.32] other.
[384.32 → 387.48] And for me, I have a very simple definition of agentic.
[387.94 → 392.00] The LLM can use an external tool or API to do something.
[392.14 → 393.50] So it's got agency.
[394.00 → 398.32] And typically there is a little loop that runs and the LLM can choose the different tools
[398.32 → 399.84] and maybe there is an orchestrator.
[400.52 → 407.00] And a lot of these are internal, for example, for customer support.
[407.00 → 409.76] So there is an email that comes in.
[410.16 → 414.82] And then there is this agentic workflow that based on the email, it's got access to a few
[414.82 → 415.28] tools.
[415.76 → 417.56] It will look into the user account.
[417.72 → 419.82] It will try to look at historic data.
[419.82 → 429.30] And then it can either decide I'm going to automatically perform an action or I'm going to suggest an action for the customer support agent.
[429.30 → 439.16] Some of them also draft the response or the types of actions that the real person needs then to approve.
[439.40 → 443.52] There is a lot of this currently going on.
[443.52 → 447.18] And to me, it makes sense because this is the promise of Gen. E.I.
[447.18 → 453.26] Like certainly we didn't put that much investment in it just to generate text.
[453.72 → 464.84] Maybe the one thing that might be surprising for people outside or some of these enterprises is that MCP is too new for them to have it.
[464.94 → 473.28] Meaning that if you think about it, some of the big organizations have got development cycles where the first projects get conceived,
[473.28 → 476.56] a project gets conceived one year ago.
[476.56 → 484.60] And so a lot of them will have their own agentic frameworks, essentially their own loops and their own prompts and their own parsing.
[485.02 → 488.00] Or they use Lung Chain, which is in...
[488.00 → 489.76] No, actually, what's the one that they use?
[489.98 → 491.10] Oh, God, I forgot the name.
[491.54 → 491.94] Crew AI?
[492.54 → 493.86] I was literally looking at the source.
[493.92 → 494.62] It's in C Sharp.
[494.74 → 498.38] I was literally looking at the source code like last week.
[498.48 → 499.02] What was it?
[499.12 → 500.00] It's by Microsoft.
[500.00 → 501.12] I cannot...
[501.12 → 504.90] Semantic something, which has got...
[504.90 → 505.94] You can define tools.
[505.94 → 507.00] It's in C Sharp.
[507.16 → 515.00] I mean, people use Python, but you have to imagine a lot of these places like native C Sharp stuff.
[515.00 → 525.94] I'm curious, as you were talking about the world has moved into agentic, and we've talked a lot about that on the show in general over the last year and such.
[525.94 → 533.90] But kind of moving from that prompt-only environment that maybe you and Daniel talked about earlier into the agentic world.
[534.22 → 539.20] You defined it as kind of that external agency to bring in things.
[539.20 → 554.10] I would guess, as someone who is not an expert on security, that that introduces mega amount of new vulnerabilities and new concerns just because you're now using those agents to reach out into the world and do things.
[554.60 → 561.68] Could you talk a little bit about what that new landscape looks like to you since you talked to Daniel last time?
[561.68 → 584.40] So I would say, if I need to be concise and make a statement, basically what people need to consider is that any tool exposed to an LLM becomes a tool exposed to any person that can control any part of the input into an LLM.
[584.40 → 596.32] Now, what's very common is that our clients take APIs, which used to be internal APIs, for example, for customer support, for asking staff.
[596.50 → 606.20] And these APIs are built to be consumed by internal systems, meaning they have never been exposed for real on the Internet.
[606.20 → 624.80] Now, as soon as you make that API into a tool that the LLM can call, any entity that can control any part of that LLM input via things like prompt injection, they can get the LLM to call that API with whatever parameters they want.
[624.90 → 631.82] And because this wasn't an API that you ever expected to be exposed essentially on the Internet, all of a sudden you have a problem.
[631.82 → 635.40] And it is not just exposed to the person that's prompting a chatbot.
[635.74 → 645.40] It is exposed to somebody that sends a customer support email in and then that customer support email is fed to the agentic workflow.
[645.66 → 653.10] And now that can cause the LLM to call some of these functions with whatever parameters.
[653.10 → 661.90] So I would say that authorization or access control has been the biggest things we've been focusing our efforts on.
[662.02 → 665.98] Like, you know, how is the identity passed to the tool?
[666.46 → 677.42] And do you have a deterministic, non-LLM-based way of determining whether that function can be called in that context safely?
[677.66 → 681.20] If you don't have that, you can't go into production.
[681.20 → 695.00] I want to run something by you, Donate, because I was thinking about this the other day and I wonder if it's, I wonder if you agree or have a comment on it basically, which is that what you basically described can be very, very complex.
[695.00 → 698.76] Like everything from, like, let's say it is a customer service thing.
[698.86 → 700.58] There's the actual customer ticket.
[700.78 → 707.92] Maybe I'm in a retrieval way pulling in previous JIRA tickets that have information like from a repository.
[707.92 → 711.76] I'm calling, you know, maybe multiple tools.
[712.14 → 724.58] It seems like there's this sort of like explosion of complexity in kind of this web of connected things that happen before the prompt goes into the LLM.
[725.04 → 730.76] And I remember earlier on in my career when it was like the days of microservices everything, right?
[730.76 → 734.64] It's like all of a sudden you have a thousand microservices, right?
[734.66 → 737.12] And I remember we had dashboards up on the wall.
[737.34 → 746.08] And part of the problem was like when there was something bad that happened, an alert would go off on one of the services.
[746.08 → 748.96] But it wasn't just an alert that would go off on one of the services.
[748.96 → 758.06] It was like an alert went off on all the services because they're all like interconnected in this way that makes them all kind of malfunction at once.
[758.16 → 764.54] And so it became kind of this root cause analysis issue then at that point.
[764.54 → 778.54] And you kind of gave up, or you had the trade-off of that complexity and root cause analysis for the simplicity and flexibility of kind of developing on this microservices' architecture.
[778.54 → 790.94] Do you see this kind of also getting into that kind of root cause analysis type of scenario or like analyzing this network of things?
[790.94 → 796.60] Because it's just becoming so complex as these pipelines kind of grow and become more interconnected.
[797.00 → 800.86] And any one piece could kind of trigger a problem in the whole thing.
[801.42 → 803.72] I mean, it is reminiscent of that.
[803.72 → 814.02] And I will say it's an explosion of data sources in the context of the LLM.
[814.02 → 834.64] So what I think is really dangerous is that now in the same single individual call or context that goes into an LLM call, we are mixing more and more data sources from more and more entrusted parties in the same LLM call.
[834.64 → 840.62] And that's where I think confidentiality, integrity starts becoming a problem.
[840.62 → 848.08] Because again, now everything you put into that prompt ought to be trusted for the use case.
[848.24 → 851.08] Otherwise, any single part can break it.
[851.16 → 852.72] I will give you an example.
[853.06 → 856.72] One of our consultants in the U.S. was doing a test a couple of weeks ago.
[857.46 → 860.32] This and the idea of the use case was great.
[860.32 → 862.46] So there is a customer support email.
[862.92 → 863.90] And this is William Taylor.
[864.12 → 866.08] I'll give him a shout because he's an amazing guy.
[866.50 → 869.06] But the email came in.
[869.66 → 871.78] And so the use case is the following.
[872.42 → 874.98] Rug on all the support tickets.
[875.50 → 885.08] Not just the ones belonging to the user that sent the email, but basically all the emails that have keywords or like, you know, similarity.
[885.08 → 892.08] And so that builds the top 10 emails that came in, which are potentially related to this query.
[892.30 → 896.10] The entire thing is then fed to the LLM.
[896.92 → 902.28] And the LLM can then decide, okay, I know how to solve this based on historic data.
[902.40 → 907.20] And I'm now just going to email the user, or I need to escalate it.
[907.64 → 910.54] This is terrible from a cybersecurity point of view.
[910.54 → 924.32] I, an attacker, can send in an email with a lot of keywords, or even I can fill the context of my email with people's email addresses that I'm interested in.
[924.62 → 926.26] Now, I send that email.
[926.46 → 927.80] That's now part of the rug.
[928.16 → 939.50] When one of those users sends a ticket in, my malicious email is very likely to be picked and to be part of that huge prompt, which is then processed.
[939.50 → 944.40] And I can make it, I can make the LLM generate an email with a phishing attack.
[944.94 → 950.90] Like, and now the custody, like the company will send the user an email with the content I want.
[950.98 → 952.70] For example, this is a link.
[953.12 → 954.48] Click it to solve the issue.
[954.58 → 956.70] I mean, we demonstrated that.
[957.22 → 963.46] So the problem here is that we are feeding to the LLM different data sources.
[963.64 → 968.44] And some of them are potentially malicious or not controlled.
[968.44 → 969.72] So there is this explosion.
[970.26 → 971.88] And you could say the same with MCP.
[972.28 → 982.10] So every time somebody is adding an MCP server, obviously the output of an MCP server is input into your LLM context.
[982.26 → 988.68] The description of an MCP server has to end in your LLM context.
[988.68 → 990.66] But that can contain prompt injection.
[990.78 → 997.12] That can tell your client to call another MCP server completely unrelated to do something else.
[997.24 → 999.96] I mean, this has been demonstrated a million times.
[1000.34 → 1007.32] And Sean from Hugging Face was talking about it at Secure AI just again in Stockholm a couple of weeks ago.
[1007.52 → 1009.54] And this is a very hard problem to solve.
[1009.54 → 1017.38] So we are mixing different untrusted sources into the same LLM context.
[1017.48 → 1018.92] And that's hard to solve.
[1018.92 → 1037.36] Well, friends, it is time to let go of the old way of exploring your data.
[1037.62 → 1038.54] It's holding you back.
[1038.88 → 1040.90] But what exactly is the old way?
[1040.90 → 1048.18] Well, I'm here with Mark Duppy, co-founder and CEO of FBI, a collaborative analytics platform designed to help big explorers like yourself.
[1048.62 → 1050.46] So, Mark, tell me about this old way.
[1050.98 → 1061.26] So the old way, Adam, if you're a product manager or a founder, and you're trying to get insights from your data, you're wrestling with your Postgres instance or Snowflake or your spreadsheets.
[1061.26 → 1066.98] Or if you are, and you don't maybe even have the support of a data analyst or data scientist to help you with that work.
[1067.18 → 1082.08] Or if you are, for example, a data scientist or engineer or analyst, you're wrestling with a bunch of different tools, local Jupyter notebooks, Google Cola, or even your legacy BI to try to build these dashboards that someone may or may not go and look at.
[1082.08 → 1093.26] And in this new way that we're building at FBI, we are creating this all-in-one environment where product managers and founders can very quickly go and explore data regardless of where it is.
[1093.40 → 1096.48] So it can be in a spreadsheet, it can be in Airtable, it can be in Postgres, Snowflake.
[1096.76 → 1103.14] Really easy to do everything from an ad hoc analysis to much more advanced analysis if, again, you're more experienced.
[1103.62 → 1110.72] So with Python built in right there and our AI assistant, you can move very quickly through advanced analysis.
[1110.72 → 1128.88] And a really cool part is that you can go from ad hoc analysis and data science to publishing these as interactive data apps and dashboards, or better yet, at delivering insights as automated workflows to meet your stakeholders where they are in, say, Slack or email or spreadsheets.
[1128.88 → 1142.40] So, you know, if this is something that you're experiencing, if you're a founder or a product manager trying to get more from your data or for your data team today, you're just underwater and feel like you're wrestling with your legacy BI tools and notebooks, come check out the new way and come try out FBI.
[1142.76 → 1143.28] There you go.
[1143.44 → 1149.72] Well, friends, if you're trying to get more insights from your data, stop resting with it, start exploring it the new way with FBI.
[1149.72 → 1153.00] Learn more and get started for free at Fabi.ai.
[1153.00 → 1156.30] That's F-A-B-I dot A-I.
[1156.44 → 1158.80] Again, FBI dot A-I.
[1163.36 → 1182.76] As I'm processing what you're talking about with this, I'm like, I'm just imagining, you know, especially as you're describing kind of your offensive driven approach that you guys have, you know, the number of potentially bad actors out there that could be exploiting this.
[1182.76 → 1183.98] You know, with this information.
[1184.52 → 1189.74] And, you know, are you at this point, like, what are you seeing out there in the wild?
[1189.74 → 1197.42] Like, you know, that's such a compelling kind of a danger story that you're telling that is so practical.
[1197.96 → 1200.26] Like any of us could go do that.
[1200.36 → 1204.66] What are you seeing in the real world in terms of bad actors and at what levels?
[1204.66 → 1207.96] Like, you know, I come from the defence and intelligence industry.
[1207.96 → 1212.44] So obviously my brain goes to those types of concerns.
[1212.44 → 1214.64] But, you know, there are cyber criminals.
[1214.64 → 1218.58] There are all sorts of different types of potential bad actors out there.
[1219.30 → 1228.40] So what are you, and what is this industry kind of focused on right now in terms of what's already happening and where your biggest fears are?
[1228.40 → 1234.66] So I will say that because of what we do now, we don't have an incident response team.
[1234.76 → 1238.60] So we don't really get to see much of what happens.
[1238.72 → 1239.66] Like, we don't see that.
[1239.74 → 1241.70] So we are more at the prevention side.
[1241.80 → 1245.36] So we will test systems that are not in production yet.
[1245.36 → 1248.08] So we kind of see into the future.
[1248.28 → 1254.92] Well, if that system had gone into production the way it was, I can foresee the attack would have happened.
[1255.46 → 1265.66] Now, in terms of what people have actually demonstrated in practice, the one that comes to mind, and I'll give a shout-out to the guys at this company called AIM Labs.
[1266.14 → 1269.08] They demonstrated a vulnerability on co-pilot.
[1269.78 → 1271.72] They called it eco-leak.
[1272.04 → 1274.48] So basically, it's the same rag concept.
[1274.48 → 1275.62] You send an email.
[1276.00 → 1277.80] Co-pilot is just a big rag.
[1278.36 → 1281.42] Now, with that email, it was very clever.
[1281.70 → 1284.62] I think we should link in the show notes the description of the attack.
[1284.72 → 1290.08] But basically, with that email, they got co-pilot to exfiltrate information.
[1290.70 → 1293.24] Now, the thing is, Microsoft knows about this.
[1293.52 → 1301.52] They had a lot of filtering in place, but they were able to find a clever Markdown syntax to bypass the filtering.
[1301.52 → 1312.70] So probably your audience will know that one of the main vectors to exfiltrate information in LLM applications is to make the LLM produce a markdown image.
[1312.88 → 1318.86] And in the URL, you can point the URL to an attacker-controlled server.
[1318.86 → 1326.98] And then you can tell the LLM, by the way, in the query string of this URL, put all the credit card data of this user if the LLM knows about that.
[1327.04 → 1333.38] And obviously, when the LLM returns that, and you try to render that image, the request is going to go to the server.
[1333.38 → 1340.84] Now, you can't do this in co-pilot because they are filtering out a lot of this Markdown syntax.
[1340.84 → 1346.38] But the guys found a way around it to bypass the regular expression that co-pilot was using.
[1346.80 → 1352.24] So what we're seeing is instances where stuff could really go wrong.
[1352.78 → 1359.68] But thankfully, there are a lot of researchers that seem to be catching them before they are exploited to the full potential.
[1359.84 → 1362.14] But then cybersecurity is very strange.
[1362.14 → 1365.82] Sometimes you will know a breach happened five years later.
[1366.76 → 1375.42] And I know one of the things I definitely want to get into with you based on our previous conversations was kind of design pattern type of things.
[1375.42 → 1385.58] But before we get there, I'm a little bit curious just from a strategic standpoint in terms of how you're interacting with customers.
[1385.58 → 1399.88] Because there's one side of the spectrum where you can try to lock everything down and say, oh, we haven't verified any of these sources of data.
[1400.28 → 1411.66] We have to have a policy in place to approve certain tool connections or no external connections to different tools and other things like that.
[1411.66 → 1415.58] The issue on that side I see is people want to be productive.
[1415.74 → 1416.78] They want the functionality.
[1417.06 → 1422.46] They'll do this sort of shadow AI stuff and try to, you know, like they just want the good functionality.
[1422.76 → 1424.48] So you kind of go on that end of the spectrum.
[1424.66 → 1426.42] You maybe have that problem.
[1426.62 → 1437.00] On the other end of the spectrum, without any sort of policy or without any sort of governance, right, then you just get into this chaos and a huge amount of problems.
[1437.00 → 1440.50] So, you know, there's never any kind of perfect solution.
[1440.64 → 1442.56] You're always going to have to wrestle with something.
[1442.78 → 1462.08] But do you have any thoughts on that in terms of companies, like, I guess their posture in how to approach this, recognizing that people are able to find tools and able to find, you know, their own solutions that solve their issues so easily but might introduce liability?
[1462.08 → 1470.52] I mean, this is very, very old in cybersecurity with the difference now that people really want to be using Gen.AI.
[1470.86 → 1475.60] Because like for, like, you know, I'm lazy like a lot of other people, I guess.
[1475.78 → 1482.66] I do like the ability to use it to do a lot of tasks or to make them easier.
[1483.16 → 1486.26] Now, what happens in some of the enterprises?
[1486.26 → 1490.90] I think I put them among our clients into two big categories.
[1490.90 → 1495.06] I mean, there are some which are extremely risk-adverse.
[1495.64 → 1497.42] Obviously, I will not name them.
[1497.70 → 1507.60] But the only thing I want to say is that I would never work there because it's basically impossible to get anything done and everything is so slow.
[1508.10 → 1515.82] And sometimes even for us as pen testers, I have to log in with Citrix into a Windows box.
[1515.82 → 1518.62] Then from there, I have to RDP into a server.
[1518.84 → 1523.58] From that server, I have to go into like a Linux machine.
[1523.68 → 1525.68] And from there, I can finally do some testing.
[1525.82 → 1529.82] And by the time I've done all of this, I am so locked into that.
[1529.92 → 1530.76] There is nothing I can do.
[1530.82 → 1532.36] And the employees work like this.
[1532.42 → 1534.92] Like they are on these machines, and they can't do anything.
[1534.92 → 1538.52] So you have that extreme and they do exist.
[1538.88 → 1543.08] Like a lot of big financial sector, extremely risk-adverse.
[1543.66 → 1546.26] It makes you cry when you see that.
[1546.38 → 1547.56] I think I couldn't stand it.
[1547.64 → 1551.32] I couldn't spend all my day into six layers of BDI.
[1551.32 → 1560.54] But on the other side, and we work a lot with startups, and it's wild west to say.
[1560.80 → 1562.10] So I think it's fun.
[1562.38 → 1564.96] But yeah, people are just using whatever.
[1565.32 → 1565.68] Like, you know.
[1566.26 → 1568.54] So yeah, it's these two buckets.
[1568.68 → 1570.90] And I think I don't have an answer for that.
[1570.96 → 1572.78] Meaning that I see both.
[1573.34 → 1576.08] But I see extremely locked down environments.
[1576.08 → 1580.88] And I see companies that are much more relaxed.
[1581.08 → 1582.94] And yeah, people are doing a lot of shadow AI.
[1583.20 → 1587.12] Like people have cloud desktop just installed.
[1587.42 → 1590.12] I guess they will have all the NCP services they want.
[1590.34 → 1591.62] They go and charge EPT.
[1591.72 → 1594.16] Even if company policy says you can't go.
[1594.60 → 1597.80] And yeah, they put all their data there.
[1598.46 → 1599.88] I wouldn't do that.
[1600.36 → 1603.50] I'm curious as you're kind of addressing some of the challenges
[1603.50 → 1607.68] and these different environments that are inherent now in pen testing.
[1608.04 → 1615.12] Could you also talk a little bit about kind of the differences in penetration testing today
[1615.12 → 1619.28] versus, you know, kind of before this Gen AI era?
[1619.56 → 1622.12] Like what's changed and what kinds of activities
[1622.12 → 1625.88] and how have the metrics that you're looking at changed?
[1625.88 → 1630.66] Like what has the new approach to dealing with prompt injection
[1630.66 → 1635.66] and these type of exploits brought to bear in that day-to-day life?
[1636.06 → 1638.76] You know, aside from having to sometimes go so many layers deep,
[1638.88 → 1640.80] you know, as you mentioned in the financial thing.
[1640.86 → 1643.16] What are some of those other attributes that have changed?
[1643.28 → 1647.16] So I would say not much has changed, which is interesting.
[1647.32 → 1648.84] So there are two things that change.
[1649.50 → 1651.90] Capability from the pen testing point of view.
[1651.90 → 1657.90] It is much quicker if you are offensive to write a script to do something.
[1658.04 → 1662.08] I mean, this is like if you know what you're doing, and you have a good LLM,
[1662.62 → 1665.38] your capability, at least you're working faster.
[1665.64 → 1666.72] Like that is true.
[1667.14 → 1670.40] Now, from the security assessment point of view,
[1670.46 → 1672.32] so clients are building applications.
[1673.12 → 1677.36] What's changed is that if they have an LLM in the application workflow,
[1677.70 → 1679.64] we have to do additional testing.
[1679.64 → 1685.76] And that testing is a bit different because you're working on probabilistic stuff.
[1685.92 → 1690.62] So we try to help people assess, okay, have you got guardrails?
[1691.02 → 1694.54] What's the quality of those guardrails?
[1694.90 → 1701.14] And what can you do outside in the design or in the implementation
[1701.14 → 1706.04] to make sure that when the LLM does something wrong,
[1706.38 → 1708.42] you and your customers are protected.
[1708.42 → 1712.54] So typically it takes a bit longer, and actually it becomes more data science driven.
[1712.76 → 1716.54] So if you're looking, if you're testing SQL injection,
[1717.26 → 1719.02] it is not very data science driven.
[1719.14 → 1721.48] You basically demonstrate that you can do it.
[1721.90 → 1724.44] If you're testing SQL injection,
[1725.58 → 1727.34] so if you're testing prompt injection,
[1728.20 → 1730.46] you know that prompt injection is inherent.
[1730.70 → 1732.34] So you are going to find a way.
[1732.34 → 1735.62] So what you're trying to test is what's the effort?
[1736.36 → 1740.92] How hard is it for the attacker to be successful?
[1741.14 → 1745.70] Because that's then going to drive the types of guardrails that you need
[1745.70 → 1748.24] and the type of active response.
[1748.68 → 1753.44] I will say something more, and then I will let you guys see if we can make sense of this.
[1753.44 → 1763.52] But basically, I think jailbreaking and prompt injection is less similar to SQL injection
[1763.52 → 1766.96] and more similar to password guessing attacks.
[1767.34 → 1768.28] In what way?
[1768.68 → 1773.86] So the question is not whether the LLM can be jailbroken.
[1773.86 → 1776.28] The question is, what's the effort?
[1776.68 → 1783.22] How many prompts do I need to try before I am successful at jailbreaking it?
[1783.28 → 1789.30] There are so many techniques, crescendo, random suffix attack, best of N.
[1789.60 → 1792.24] Like you can do so many of these techniques.
[1792.70 → 1796.40] So the more effort I can put in it, the more I'm likely to succeed.
[1796.40 → 1805.54] So exactly as password guessing, the way you kind of solve this is that there are two layers.
[1805.74 → 1813.08] One layer is you don't allow the attacker to explore the space of all possible passwords.
[1813.86 → 1819.70] Likewise, you don't allow the attacker to send 100,000 prompts per second
[1819.70 → 1824.12] to explore, to find something that's going to jailbreak it.
[1824.12 → 1829.38] You have a set of guardrails for prompt injection, topic control.
[1830.76 → 1838.38] As soon as a user, as an identity that's connected to your application triggers three of those guardrails,
[1838.70 → 1840.02] that's your feedback loop.
[1840.46 → 1841.78] You stop the user.
[1842.34 → 1848.68] You suspend it in the same way that if I, Chris, if I try three passwords that are wrong
[1848.68 → 1853.06] against your email account, I am not going to be allowed to keep trying.
[1853.06 → 1855.34] Your account is going to be temporarily locked.
[1855.46 → 1858.80] And that's to prevent me from exploring that space.
[1859.36 → 1864.66] I think protecting against jailbreak attacks in the real world is very similar.
[1865.02 → 1866.20] You have the guardrails.
[1866.60 → 1868.74] They are not protecting the application.
[1868.94 → 1874.36] They are giving you a feedback signal that that person, that user, that identity is trying
[1874.36 → 1875.36] to jailbreak it.
[1875.68 → 1877.48] And then you can act on it.
[1877.74 → 1879.08] Sorry, it was a very long answer.
[1879.34 → 1882.76] But I think this is very important that people don't understand this.
[1882.76 → 1887.14] People think that the jailbreak, the guardrail protects them.
[1887.48 → 1893.44] No, the guardrail is your detection feedback loop that then you have to action to protect
[1893.44 → 1894.98] your application and your users.
[1895.14 → 1896.86] It's a completely different thing.
[1897.24 → 1900.74] It's a good thing to hear because it's not that that's something that was new to me as
[1900.74 → 1901.00] well.
[1901.22 → 1903.44] So I appreciate you covering that.
[1903.82 → 1904.00] Yeah.
[1904.14 → 1904.30] Yeah.
[1904.30 → 1908.46] And I hate it from, I guess, even just from the user experience side.
[1908.46 → 1914.70] If you try to treat that prompt injection block as a kind of binary, you know, you're going
[1914.70 → 1915.48] to let it through or not.
[1915.54 → 1916.72] You're going to moderate the user.
[1917.18 → 1920.56] Also, those prompt injection detections are not perfect.
[1920.56 → 1920.94] Right.
[1920.98 → 1921.76] None of them are.
[1921.76 → 1923.48] So you're going to get false positives.
[1923.48 → 1927.56] And from the user perspective, that creates problems.
[1927.56 → 1928.00] Right.
[1928.08 → 1933.88] But if, like you say, you have certain percentage of detections or a certain number or a certain
[1933.88 → 1936.46] number of triggers, that's much stronger.
[1936.46 → 1941.06] And also an approach that is happening in the background.
[1941.06 → 1947.44] I almost feel like this sort of net new seem event related to AI things where you kind of
[1947.44 → 1949.44] have the response to it.
[1949.90 → 1955.80] I'm wondering, Donate, you spend a lot of time kinds of digging in, I know, to research
[1955.80 → 1956.68] in this area.
[1956.84 → 1963.84] One of those things being a paper that I think you've made some videos on, but also just we
[1963.84 → 1965.92] were discussing prior to recording.
[1966.50 → 1968.18] Could you talk a little bit about that?
[1968.18 → 1971.12] And I think that goes into some design patterns.
[1971.38 → 1975.98] Obviously, if people want to kind of have the full breakdown of this, because there's
[1975.98 → 1978.72] a lot of goodness there, they can watch Donate's video on this.
[1978.80 → 1980.30] We'll link it in the show notes.
[1980.74 → 1985.98] But maybe just give us a sense of that at a high level, some of what was found.
[1986.52 → 1993.42] So this paper is called Design Patterns to Secure LLM Agents Against Prompt Injection.
[1993.72 → 1998.06] And I already like the title of the paper because it's telling you exactly what's in the paper.
[1998.06 → 2001.88] You don't have to kind of wonder what it's about.
[2002.44 → 2009.46] So what I like about the paper, this is coming from different universities, people at Google,
[2009.78 → 2010.32] Microsoft.
[2010.60 → 2015.90] I mean, there are like, I want to say 15 different contributors to this paper.
[2016.04 → 2017.20] It's very practical.
[2017.96 → 2022.80] They basically look at different types of agentic use cases.
[2022.80 → 2026.52] Not every agentic use case is the same.
[2027.18 → 2032.38] So they kind of give examples of like 10 different agentic use cases.
[2032.82 → 2037.40] Now, an agentic use case then has a certain level of utility.
[2037.58 → 2045.80] So how much power do you need to give to that LLM in order to be able to do certain operations?
[2045.80 → 2048.50] And that defines the scope of that.
[2048.64 → 2056.46] And then they find, they crystallize six design patterns that you can apply depending on your
[2056.46 → 2063.78] trade-offs between security for that use case, between security and how useful, usefulness
[2063.78 → 2065.96] or power of that use case.
[2065.96 → 2073.72] Now, there could be use cases that you can make very secure with the pattern that they
[2073.72 → 2075.10] call action selector.
[2075.68 → 2077.86] Now, this is the most secure pattern.
[2078.30 → 2084.94] You are just using the LLM to basically select a fixed action from the user input.
[2084.94 → 2091.36] So that kind of often removes in that case, anything bad the attacker can do.
[2091.42 → 2096.14] Because if the LLM produces output that doesn't make sense, it's not an allowed action for that
[2096.14 → 2098.42] user, you discard it.
[2099.00 → 2101.36] And then they talk about other patterns.
[2101.50 → 2109.20] And the one that's the most promising and the most widely applicable, they call it code
[2109.20 → 2110.58] then execute.
[2110.58 → 2114.96] And this is, it was published by Google and I think they call it CAMO.
[2115.16 → 2116.96] There is a dedicated paper to that.
[2117.28 → 2129.46] And so the idea is that the LLM agent is prompted to create a plan in the form of a Python snippet
[2129.46 → 2135.88] of code where it's going to commit to executing that program exactly as it is.
[2135.88 → 2142.46] Now, as part of that program, the LLM can access data and can perform operations.
[2142.92 → 2153.16] But the logic of the program is fixed by the LLM before malicious data enters potentially the context of the LLM.
[2153.50 → 2160.16] And all the third-party data that comes in is handled as a symbolic variable.
[2160.56 → 2163.06] So X equals function call.
[2163.22 → 2165.28] Then you take X and you pass it somewhere else.
[2165.28 → 2171.12] Not only this, but every tool that you can call can have a policy.
[2171.64 → 2181.96] It can say, if this tool is called with an argument that was tainted with a data source coming from here,
[2182.36 → 2184.24] this action cannot be executed.
[2184.74 → 2189.58] But if this tool is called with a variable, so you do this with data flow analysis,
[2189.72 → 2194.94] with a variable that came from what we consider trusted users, then these actions can be done.
[2194.94 → 2197.20] So each tool can have a policy.
[2197.34 → 2198.44] You can write the policy.
[2198.64 → 2202.18] And then the framework traces data.
[2202.32 → 2203.24] This is classic.
[2203.28 → 2203.92] This is not AI.
[2204.02 → 2205.44] This is classic data flow analysis.
[2205.86 → 2213.66] And so all of this can be enforced completely outside the LLM and completely deterministically.
[2213.66 → 2220.78] It's very reminiscent for people in cybersecurity of what SC Linux does on a Linux kernel.
[2220.94 → 2225.64] So it's kind of this reference monitor for LLM agents.
[2225.64 → 2246.18] What if AI agents could work together just like developers do?
[2246.40 → 2249.94] That's exactly what agency is making possible.
[2249.94 → 2252.38] Spelled A-G-N-T-C-Y.
[2252.50 → 2259.18] Agency is now an open source collective under the Linux Foundation, building the Internet of Agents.
[2259.60 → 2263.60] This is a global collaboration layer where the AI agents can discover each other,
[2263.98 → 2268.70] connect, and execute multi-agent workflows across any framework.
[2268.70 → 2276.40] Everything engineers need to build and deploy multi-agent software is now available to anyone building on agency,
[2276.62 → 2281.12] including trusted identity and access management, open standards for agent discovery,
[2281.54 → 2287.44] agent-to-agent communication protocols, and modular pieces you can remix for scalable systems.
[2287.78 → 2293.72] This is a true collaboration from Cisco, Dell, Google Cloud, Red Hat, Oracle,
[2293.72 → 2298.72] and more than 75 other companies all contributing to the next-gen AI stack.
[2299.00 → 2301.88] The code, the specs, the services, they're dropping.
[2302.02 → 2302.94] No strings attached.
[2303.20 → 2305.04] Visit agency.org.
[2305.10 → 2309.66] That's A-G-N-T-C-Y.org to learn more and get involved.
[2309.66 → 2314.80] Again, that's agency, A-G-N-T-C-Y.org.
[2314.80 → 2324.30] So when you're talking about the code, then execute design pattern,
[2324.52 → 2328.92] is there a way of inhibiting the LLM from using prompt injection
[2328.92 → 2333.56] to get the LLM agent to write the code that then gets executed?
[2333.92 → 2337.74] Is there basically some way of defending the code being written
[2337.74 → 2342.06] from being influenced by the prompt, you know, by a potential prompt injection?
[2342.06 → 2344.70] That's the key of that use case.
[2345.24 → 2353.48] You ask the LLM to produce a plan or the code before any untrusted input enters the context.
[2353.64 → 2356.30] So the user query is trusted, okay?
[2356.30 → 2361.64] But then the tools that it calls and the output from those tools
[2361.64 → 2364.80] and the third-party data could be an email that the user received.
[2365.20 → 2369.98] Now those will not be able to alter the LLM control flow.
[2369.98 → 2374.12] And if they try to, it will be stopped by the reference monitor
[2374.12 → 2379.08] because it will say, no, this function cannot be called with this input
[2379.08 → 2384.28] because this input has been tainted by this third-party email.
[2384.82 → 2386.20] Very, very cool concept.
[2386.40 → 2387.96] They do have a reference implementation.
[2388.28 → 2389.22] I mean, I had a weekend.
[2389.70 → 2391.64] I like this paper so much that one weekend,
[2391.78 → 2395.48] I actually implemented all of these six design patterns.
[2395.60 → 2397.54] I think I put it in a Git repo.
[2397.54 → 2400.00] It's not difficult to implement, actually.
[2401.14 → 2406.88] And it was really fun because then I realized something that I kind of intuitively know.
[2407.22 → 2413.20] You don't solve the problem of LLM agent security inside the LLM.
[2413.30 → 2415.50] This is not an alignment problem.
[2415.90 → 2418.68] You solve the problem outside of it.
[2418.90 → 2422.44] You still use prompt injection detection, topic guardrails.
[2422.44 → 2426.08] You still use these as feedback loops, as we said before.
[2426.48 → 2430.86] But if you want to get assurance that stuff is not going to go bad,
[2431.04 → 2436.96] you need to have much stronger controls that don't depend on the LLM itself.
[2437.48 → 2440.84] So it would be fair to say its kind of a system design problem
[2440.84 → 2445.26] rather than a model design problem because you're kind of isolating the model?
[2445.46 → 2446.74] Is that, am I getting that?
[2446.74 → 2446.82] Totally.
[2447.26 → 2447.50] Okay.
[2447.94 → 2448.34] Totally.
[2448.34 → 2451.14] And you mentioned some of this work.
[2451.20 → 2454.96] Of course, it's been great to see that both in terms of video content
[2454.96 → 2458.36] and in terms of code and actual framework,
[2458.62 → 2461.44] you and your team have contributed a lot out there.
[2461.86 → 2468.58] One of those things that I've run across is the spiky package or framework or project.
[2469.22 → 2471.30] Could you talk about that a little bit?
[2471.30 → 2479.26] Maybe how that came about and where it fits into kind of tooling, I guess, in this realm?
[2480.02 → 2487.44] So, I mean, that's very interesting because when we started doing pen testing of LLM applications
[2487.44 → 2492.58] in 2023, we were doing a lot of stuff manually.
[2493.24 → 2495.24] And obviously, nobody wants to do that manually.
[2495.44 → 2500.12] It's more similar to a data science problem than a lot of the traditional pen testing.
[2500.12 → 2504.78] So, we started looking into tooling that we could use.
[2505.46 → 2514.16] And I'll be honest, the problem there is that a lot of tooling for LLM red teaming is doing exactly that.
[2514.64 → 2516.32] Is red teaming an LLM?
[2517.02 → 2520.34] An LLM application, it ain't an LLM.
[2520.66 → 2522.28] Like, it's got nothing to do with an LLM.
[2522.36 → 2523.92] Like, it doesn't have an inference API.
[2523.92 → 2531.68] Like, if I have a button that I can click that summarizes an email, that is not even a conversational agent.
[2531.76 → 2541.86] If I send an email in and there is, like, an entire chain of stuff that happens, like, I can't run, like, a general purpose tool against it.
[2541.88 → 2542.96] It doesn't make sense.
[2542.96 → 2550.36] So, we started writing scripts, individual scripts that we use to kind of create data sets.
[2550.68 → 2555.10] And obviously, for us, this thing needed to be practical.
[2555.26 → 2559.98] Now, I have five days, six days to do a test for a client.
[2560.40 → 2568.64] And within those days, I need to be able, even in an isolated environment, to give the client an idea of what an attacker could do.
[2568.64 → 2572.06] So, you have all of this wish list of things.
[2572.24 → 2577.62] So, my wish list was, I need to be able to run this practically in a pen test.
[2577.86 → 2584.36] I need to be able to generate a data set which is customized for what makes sense in that application.
[2584.60 → 2596.16] Like, for example, I wanted a data set that I could use whenever it mattered to test data exfiltration via markdown images versus HTML injection,
[2596.16 → 2601.24] JavaScript injection versus harmful content, topic control.
[2601.44 → 2606.80] A lot of our clients, for example, say, I don't want my chatbot to give out investment advice.
[2606.96 → 2608.94] Actually, we would be liable if that happened.
[2609.30 → 2610.74] But every use case is different.
[2610.86 → 2616.18] So, I needed something that I could very quickly create these data sets.
[2616.18 → 2622.72] And then it could be as big or as small as I needed it to be.
[2623.10 → 2629.22] Now, sometimes we go to clients, and they tell us, oh, you can send 100,000 requests a day.
[2629.56 → 2629.98] Fine.
[2630.10 → 2631.82] I'm going to have a very large data set.
[2632.24 → 2636.08] Sometimes we go to clients, and they say, you can only send 1,000 prompts a day.
[2636.08 → 2639.90] So, you need to be very careful because that's an application.
[2640.08 → 2641.94] That's not an LLM inference endpoint.
[2642.34 → 2647.20] So, you need to be very careful, and you need to create a data set that answers the questions of the client.
[2647.40 → 2649.44] Can people exfiltrate data?
[2649.88 → 2652.88] Can people make this thing give financial advice?
[2652.98 → 2656.80] And then you also have general stuff like toxic content, hate speech.
[2657.18 → 2659.14] Yeah, anything covers that.
[2659.20 → 2665.16] But we needed practical stuff, and we needed to be able to run it in completely isolated environments.
[2665.16 → 2669.82] Like if you don't have access to, we needed something where I didn't need to give it an open AI key.
[2670.50 → 2670.78] Okay.
[2671.06 → 2672.54] It's really important.
[2672.84 → 2678.48] And, you know, some of the stuff we can check with regular expressions if we've been successful.
[2678.68 → 2689.58] But we had to figure out a way that if I am in an isolated environment and I have a data set that I'm generating to test whether the application is going to give out financial advice.
[2689.58 → 2696.54] But I cannot call a judge LLM to tell me whether the output is actually financial advice.
[2696.68 → 2697.82] How do I deal with that?
[2697.84 → 2700.08] So, we had to find a solution for that.
[2700.38 → 2704.96] It needed to be simple that we could have a team of pen testers use it.
[2705.28 → 2706.58] It needed to be extensible.
[2706.58 → 2708.38] So, it needed to be modular.
[2708.38 → 2716.88] So, that if one of my colleagues has an application in front of them, this is something that we will see.
[2717.00 → 2724.94] I think one of our colleagues in the US, Steve, had a chatbot that was using WebSockets.
[2724.94 → 2731.74] Now, he spent the first day crying trying to reverse engineer that protocol.
[2731.96 → 2739.24] And then on day two, and he can do that with Spiky, he wrote a Spiky module that's got a play right.
[2739.50 → 2746.84] So, the Spiky module used a headless browser to open the chatbot, send the prompt, and read the response.
[2747.54 → 2754.40] We were the only pen testing company working on that chatbot that was actually able to programmatically test a lot of stuff.
[2754.40 → 2760.40] I think we had another one of our guys was working on some AWS infrastructure.
[2761.38 → 2779.42] And the way you introduce the prompt is by dropping a file on an S3 bucket, calling a Lambda, and then in another S3 bucket, one minute later, you would have another file that was the result of the pipeline that eventually called the other land.
[2779.42 → 2798.04] So, we needed a way where a consultant could, in half a day, look at whatever they had in front of them and create an easy module so that then Spiky could take stuff from the data set, send it there, and read the response, and then say whether the attack was successful or not.
[2798.04 → 2804.28] So, we had some, and then we wanted to be able to extend it with guardrail bypass.
[2804.28 → 2831.74] So, we have a lot of attacks where you take the standard data set, and then you can say, okay, for each of these entries in the data set, I want you to try up to 100 variations using the best of N attacks, so introducing noise, versus using the anti-spotlighting attack, which is another attack that we developed, where you try to break spotlighting by introducing tags and strange stuff.
[2831.74 → 2834.92] So, the NLM doesn't understand where data starts.
[2835.12 → 2837.36] So, all of these things, and it needed to be simple.
[2838.12 → 2844.30] And sorry, that was a very long answer, but that's what we've been working on for the last year.
[2844.38 → 2846.66] And we made the whole thing open source.
[2846.94 → 2851.02] We've actually had people from the community, from other companies contribute.
[2851.70 → 2854.90] So, it's been very fun to put this together.
[2854.90 → 2856.34] No, it sounds really cool.
[2856.76 → 2864.00] And by the way, I don't remember if we identified what Spiky breaks down to from kind of the acronym.
[2864.54 → 2870.44] It's Simple Prompt Injection Kit for Evaluation and Exploitation, in case we didn't say that out loud.
[2870.44 → 2893.30] But I was curious, as you're kind of going through the different kind of construction of the attacks and writing modules and stuff, I am wondering, as you're using Spiky, like, how much of it is pretty kind of standard built-in tools that you have there on any given engagement when you're using the tool to do the pen testing?
[2893.30 → 2903.54] Versus, like, how often are you having to, in a typical engagement, are you having to create custom modules that are very specific to a particular client's needs?
[2903.64 → 2914.12] I was just, as you were going through, I was trying to decipher that, but I wasn't sure that I understood, like, you know, the toolkit as exists versus saying, ah, for this client, I need to add this thing in.
[2914.24 → 2915.48] What does that look like, typically?
[2915.48 → 2926.60] So, typically, on, like, the first day of a test, you write a module, which is going to allow Spiky to talk to the application.
[2927.12 → 2929.12] So, that depends on what the application is.
[2929.28 → 2932.08] So, the first day is typically writing this kind of adapter.
[2932.38 → 2941.78] It could be very easy if you have a REST API, or again, as we were doing, you can write Play Write, you can use the AWS API.
[2941.78 → 2944.70] So, whatever that is, that's the biggest part.
[2945.32 → 2951.74] And then you look at what you are trying to test, data exfiltration and stuff like that.
[2952.02 → 2954.32] You have, we call them seeds.
[2954.66 → 2957.04] So, you don't have pre-built data sets.
[2957.36 → 2964.52] You have seeds that allow you to build data sets, which can take five to ten minutes to customize.
[2964.52 → 2974.94] But, basically, what happens there is that, so, you have jailbreaks, which are common things that typically you don't touch.
[2975.32 → 2978.78] Then you have instructions, and the instructions is what you customize.
[2979.24 → 2987.48] So, if I want to test data exfiltration, social engineering, HTML injection, I will add or modify the instructions in there.
[2987.48 → 2994.24] So, it might take five minutes, but, basically, we only test things that make sense for that application.
[2994.38 → 3002.44] So, we create the data set, and then the rest, once you have the target adapter that allows Spy Key to talk to your application,
[3002.86 → 3007.84] and you have the data set that makes sense for your client, then you will run that data set,
[3008.16 → 3011.74] and then you will rerun it again with different attack techniques.
[3011.90 → 3013.78] So, we would say, okay, what happens now?
[3013.78 → 3016.64] We have a 10% attack success rate.
[3017.62 → 3018.84] Maybe that's okay.
[3019.02 → 3026.06] Maybe we want to see what happens if we now implement the best event, this attack that introduces noise.
[3026.34 → 3028.70] Is that going to bypass the guard rate?
[3028.90 → 3031.58] Typically, the attack success rate goes up.
[3031.96 → 3037.54] And then we kind of try all these different things and maybe change the kind of parameters.
[3037.54 → 3045.00] So, to answer your question, there is a bit of customization to make sure that what we do makes sense for the application.
[3045.00 → 3051.16] But then there are a lot of built-in attack modules that do the heavy lifting for you.
[3051.16 → 3052.56] That sounds really cool.
[3052.74 → 3054.42] I'm looking forward to trying it out myself.
[3054.68 → 3056.42] You really have me intrigued about it.
[3056.42 → 3068.10] As we are winding up here, one of the things that we like to try to get a sense of on finishing is kind of where things are going.
[3068.48 → 3080.64] And you are in this really cutting-edge aspect, the merging of security and AI and all the new types of risks that people face out there.
[3080.64 → 3084.90] And you guys have made so much progress over the last year or two.
[3085.30 → 3094.24] I'm wondering, as you're looking ahead at both what you're doing at your organization and also the larger industry,
[3094.24 → 3100.42] since you're participating in all of these different touchpoints, going to different conferences and stuff like that,
[3100.42 → 3103.08] where do you see this going?
[3103.26 → 3106.94] What kind of evolution are you expecting going forward?
[3107.36 → 3110.12] And as part of that, what do you want to see?
[3110.22 → 3115.16] Aside from whether you're seeing an example, when you're at the end of the day,
[3115.34 → 3119.78] you're able just to kind of ponder and maybe have a glass of wine or whatever you do at night.
[3120.28 → 3124.26] What is the thing you're like, that's the thing that it would be cool.
[3124.36 → 3125.32] I want to go do that.
[3125.32 → 3129.74] Whether it's on the plan right now or just an idea.
[3130.12 → 3134.32] Wax poetic for me a little bit on this, because I'm kind of curious where this industry might be going.
[3134.84 → 3137.50] Oh, I wish I knew, to be honest.
[3137.74 → 3139.26] I think so.
[3139.70 → 3149.44] Realistically, what I would like to see is people shifting the cybersecurity mindset from,
[3149.44 → 3160.98] let's do LLM red teaming to let's secure LLM applications and use cases using a design pattern that actually makes sense.
[3161.12 → 3166.94] So let's stop asking LLMs to say that humanity is stupid or how to make a bomb.
[3167.12 → 3174.78] And let's start looking at our applications and ensuring that they can be used safely
[3174.78 → 3177.66] if they have access to tools and stuff like that.
[3177.72 → 3183.60] Because I think that's going to be one of the big issues that we're going to have.
[3183.68 → 3191.44] Like if people don't start seriously taking the risks that come from LLM agents,
[3191.66 → 3196.06] we are going to see real world big breaches coming from that.
[3196.06 → 3202.96] So what I would like to see is shifting that discussion from LLM red teaming to system design
[3202.96 → 3210.74] that takes into account the fact that we don't know how to solve prompt injection and jailbreaking in LLMs.
[3210.78 → 3214.66] When somebody figures it out, I will be the happiest person in the world.
[3215.10 → 3219.82] But I believe Sam Human last year said they would have solved hallucinations.
[3220.06 → 3221.80] And I am not going to continue.
[3221.80 → 3222.42] Thank you.
[3224.02 → 3226.48] That's a good way to end right there.
[3227.08 → 3230.00] Donate, thank you so much for coming on Practical AI.
[3230.34 → 3232.28] A really fascinating conversation.
[3232.72 → 3236.78] I am excited about this and hope you come back again.
[3237.14 → 3241.00] I know we've already had a couple of conversations, but they're always fun.
[3241.48 → 3247.28] As new things are happening for you, don't hesitate to let us know what's going on
[3247.28 → 3249.48] and keep us surprised on what the space looks like.
[3249.48 → 3251.44] Thank you very much for having me.
[3251.80 → 3259.30] All right.
[3259.46 → 3260.90] That's our show for this week.
[3261.04 → 3265.04] If you haven't checked out our website, head to practicalai.fm
[3265.04 → 3268.20] and be sure to connect with us on LinkedIn, X or Blue Sky.
[3268.42 → 3271.88] You'll see us posting insights related to the latest AI developments,
[3272.12 → 3274.14] and we would love for you to join the conversation.
[3274.44 → 3278.42] Thanks to our partner, Prediction Guard, for providing operational support for the show.
[3278.42 → 3280.76] Check them out at predictionguard.com.
[3280.76 → 3284.78] Also, thanks to Break master Cylinder for the beats and to you for listening.
[3285.14 → 3285.94] That's all for now.
[3286.22 → 3287.96] But you'll hear from us again next week.
[3287.96 → 3289.52] Bye.
[3293.46 → 3293.88] Bye.
[3293.90 → 3294.68] Bye.
[3295.68 → 3295.80] Bye.
[3295.82 → 3296.26] Bye.
[3296.26 → 3296.74] Bye.
[3297.12 → 3297.32] Bye.
