[0.00 → 6.04] Welcome to Practical AI.
[6.60 → 16.18] If you work in artificial intelligence, aspire to, or are curious how AI-related technologies are changing the world, this is the show for you.
[16.70 → 22.08] Thank you to our partners at Vastly for shipping all of our pods superfast to wherever you listen.
[22.36 → 24.18] Check them out at Fastly.com.
[24.18 → 29.44] And to our friends at Fly, deploy your app servers and database close to your users.
[29.84 → 31.10] No ops required.
[31.44 → 33.46] Learn more at fly.io.
[42.72 → 43.80] What's up, friends?
[43.80 → 57.74] I'm here with Vijay Raji, CEO and founder of Stat sig, where they help thousands of companies from startups to Fortune 500s to ship faster and smarter with a unified platform for feature flags, experimentation, and analytics.
[58.44 → 61.12] So Vijay, what's the inception story of Stat sig?
[61.18 → 62.12] Why did you build this?
[62.46 → 64.88] Yeah, so Stat sig started about two and a half years ago.
[64.88 → 73.40] And before that, I was at Facebook for 10 years, where I saw firsthand the set of tools that people or engineers inside Facebook had access to.
[73.70 → 82.26] And this breadth and depth of the tools that actually led to the formation of the canonical engineering culture that Facebook is famous for.
[82.26 → 100.52] And that also got me thinking about, like, you know, how do you distill all of that and bring it out to everyone if every company wants to, like, build that kind of engineering culture of building and shipping things really fast, using data to make data-informed decisions, and then also inform to, like, what do you need to go invest in next?
[100.80 → 103.66] And all of that was, like, fascinating, was really, really powerful.
[104.00 → 107.68] So, so much so that I decided to quit Facebook and start this company.
[107.68 → 117.54] Yeah, so in the last two and a half years, we've been building those tools that are helping engineers today to build and ship new features and then roll them out.
[117.84 → 121.02] And as they're rolling it out, also understand the impact of those features.
[121.18 → 122.10] Does it have bugs?
[122.26 → 125.90] Does it impact your customers in the way that you expected it?
[126.04 → 128.36] Or are there some side effects, unintended side effects?
[128.68 → 131.38] And knowing those things help you make your product better.
[131.38 → 144.30] It's somewhat common now to hear this train of thought where an engineer, developer was at one of the big companies, Facebook, Google, Airbnb, you name it, and they get used to certain tooling on the inside.
[144.40 → 156.36] They get used to certain workflows, certain developer culture, certain ways of doing things, tooling, of course, and then they leave, and they miss everything they had while at that company.
[156.36 → 160.26] And they go, and they start their own company like you did.
[160.26 → 161.64] What are your thoughts on that?
[161.68 → 169.70] What are your thoughts on that kind of tech being on the inside of the big companies and those of us out here, not in those companies, without that tooling?
[170.14 → 177.90] In order to get the same level of sophistication of tools that companies like Facebook, Google, Airbnb, and Uber have, you need to invest quite a bit.
[177.98 → 182.40] You need to take some of your best engineers and then go have them go build tools like this.
[182.84 → 186.16] And not every company has the luxury to go do that, right?
[186.24 → 187.76] Because it's a pretty large investment.
[187.76 → 208.86] And so the fact that the sophistication of those tools inside these companies have advanced so much and that's like left behind most of the other companies and the tooling that they get access to, that's exactly the opportunity that I was like, okay, well, we need to bring those sophistication outside, so everybody can be benefiting from these.
[208.86 → 214.00] Okay, the next step is to go to statsig.com slash change law.
[214.10 → 224.28] They're offering our fans free white glove onboarding, including migration support, in addition to 5 million free events per month.
[224.50 → 225.24] That's massive.
[225.72 → 229.70] Test drive stat sig today at statsig.com slash change law.
[229.76 → 234.28] That's S-T-A-T-S-I-G.com slash change law.
[234.28 → 235.76] The link is in the show notes.
[235.76 → 254.82] Welcome to another episode of Practical AI.
[255.16 → 256.70] This is Daniel Whiten ack.
[256.80 → 264.22] I'm the founder at Prediction Guard, and I'm joined as always by my co-host, Chris Benson, who is a tech strategist at Lockheed Martin.
[264.58 → 265.26] How are you doing, Chris?
[265.26 → 266.86] Doing well today, Daniel.
[266.92 → 267.34] How are you?
[267.66 → 268.70] I can't complain.
[269.04 → 277.18] It's like these two weeks in the Midwest in the United States that I enjoy each year when it's like between hot and really, freezing.
[277.74 → 280.56] And so, yeah, I'm really I'm excited about that.
[280.74 → 282.60] And yeah, just cranking away.
[282.60 → 297.04] I'll be at the Intel Innovation Conference next week, which is going to be a fun experience to see some of what they're doing in the AI space and talk to them about some of some of the stuff we've been trying on Intel hardware.
[297.04 → 299.68] So, yeah, it's a lot of good stuff coming up.
[300.18 → 301.20] I'm really excited.
[301.32 → 308.54] Actually, it was through that Intel community that I met Dominic from Ask UI, which is our guest today.
[308.76 → 309.84] So welcome, Dominic.
[309.84 → 310.92] It's great to have you here.
[311.16 → 312.50] Hey, thanks, Don.
[312.50 → 312.62] Thanks, Don.
[313.06 → 314.00] To have you here.
[314.00 → 314.52] Yeah.
[314.74 → 316.26] Well, Ask UI.
[316.88 → 327.62] Could you tell us a little bit about first, maybe just what is it about UI that Ask UI is concerned with?
[327.62 → 333.02] And how did you get to start thinking about UI and automation?
[333.52 → 336.46] Maybe a little bit back on what are we doing?
[336.98 → 342.60] We try to free humans from being robots.
[343.10 → 344.28] What does it mean in particular?
[345.32 → 357.60] Not only you have repetitive tasks on user interfaces and what we are trying to do to bridge the gap between you have to be the programmer versus you can describe the user.
[357.62 → 360.20] And then you can describe in natural language what you want to do.
[360.32 → 362.04] So your intention, what you want to automate.
[362.58 → 369.24] For example, if you want to log in in your Facebook, then you can say with us, please click the login button.
[369.40 → 384.18] Please fill out this and this credential with natural language, which allows also non-technical guys to automate user interface and lower the border, which you can automate or start to automate things.
[384.18 → 387.18] And the second question was a little bit about...
[387.70 → 391.14] Why did you start caring about this problem?
[391.56 → 393.30] Why, why, why, why I start caring?
[393.48 → 395.52] A little bit of background about this.
[395.98 → 398.62] Previously, my background is a software developer.
[398.62 → 404.80] I was working previously at Siemens before I found it with Jonas, my co-founder of ASCII.
[405.64 → 417.06] So there, what I was doing there, I was on the plant automation system where we had to test everything because our systems have to run 365 days a year.
[417.44 → 419.60] So everything should be tested well enough.
[419.74 → 423.88] So we were standing a lot of inside the testing level and test everything through.
[423.88 → 427.58] So then I switched also a little bit to the department, the same thing.
[427.86 → 431.88] You have to test, you have to stand directly on to test the application.
[431.88 → 439.78] And then I was moving to a new organization, which tries to modernize or bring the agility within Siemens.
[440.12 → 444.76] I learned a lot about Scrum agility, bring all the new stuff, tools.
[444.76 → 455.14] But I had also the problem because Selenium and other tools couldn't solve the pain to write unit tests, the user interface tests in a way.
[455.52 → 458.82] And then I was thinking, hey, can we not solve this with AI?
[459.00 → 463.58] Because AI can understand visual information and can understand initial information.
[464.06 → 466.08] So I thought, hey, can we not combine this?
[466.22 → 468.42] And all of this, the journey started.
[468.42 → 475.26] This might be a completely ignorant question, but I just want it for my own context as well.
[475.42 → 483.44] Now, in my background as a data scientist, I've participated many times in the fun activity of web scraping.
[484.28 → 494.34] And through that, I know like, oh, there are a lot of ways in which web data or UI data might be exposed.
[494.34 → 500.38] So could you talk a little bit about like how, what does the data look like?
[500.46 → 514.02] Like, what does the problem look like as you're trying to get an AI model to interact or use an AI model or natural language input to an AI model to then interact with either a UI or a web page,
[514.08 → 519.94] especially when a lot of those things can be quite varied in terms of how they're built?
[520.26 → 523.72] Is it more of a visual thing or is it something else?
[524.34 → 526.20] Yeah, the rear on the visual part.
[526.66 → 536.58] For example, when you're talking about Selenium, Selenium is only working with web interfaces, and you cannot use this, for example, on Android and so on.
[536.92 → 540.06] What we are doing, we're doing really a screenshot of the system.
[540.70 → 542.86] So it means we can take a screenshot of the application.
[542.98 → 546.40] We can take a screenshot directly of the operating system.
[546.40 → 551.62] And then our AI model, what we trained, can detect the user interfaces.
[551.84 → 558.98] It means we're detecting buttons, we're detecting text, we're detecting text fields, we're detecting checkboxes, we're detecting icons.
[558.98 → 566.52] And so we have already trained a model which can understand the visual representations of user interfaces.
[567.00 → 571.96] And then we connected our natural language part to it to match the intention.
[572.16 → 572.70] What do you have?
[572.70 → 578.68] For example, click on the lock-in button to the real lock-in button on the user interface, and then we are moving them out there.
[579.26 → 590.06] So this is a little bit different from the concept versus I connect directly to the application and then try to scrape the source code of the application to get my information.
[590.82 → 592.82] Maybe this is the best way to differentiate.
[592.82 → 597.10] So you're kind of starting with a screenshot instead of doing web scraping.
[597.52 → 597.76] Correct.
[597.98 → 601.82] And then just doing classification on the screenshot itself to do that?
[602.00 → 602.20] Correct.
[602.46 → 608.26] So we have object detection model in place, which really detects the screenshot and detect all the elements on it.
[608.54 → 617.00] As a quick follow-up, when you do the classification and identify what you have in the screenshot, how do you tie that in with the tests desired?
[617.54 → 620.24] So you have a collection of tests that you're trying to automate.
[620.24 → 625.06] How are you tying, like, I got a screenshot, I have a button, I have a text field.
[625.40 → 628.06] How does that tie into a particular unit test or something?
[628.56 → 636.90] Currently, we have our Text Script application, which you can download, which is also available as an RSI NPM package, which you can use.
[637.54 → 643.92] And with this, you can directly start, install it, and then generate a standard test.
[643.92 → 657.40] And then you have, for example, the JEST test block or Java JUnit test block, where you then can write, ask your eye dot click dot with text dot so on.
[657.74 → 659.08] And the background, what happens?
[659.62 → 668.92] We have a controller then installed on your local system, which connects to the operating system, takes a screenshot and also have the ability to control the mouse.
[668.92 → 675.74] Move the mouse, then we're taking the screenshot, we are connecting the instruction, the click on button, for example.
[676.20 → 681.00] Send this to our inference backend, then we get the result back, and then we're moving the mouse there.
[681.00 → 692.18] And with this single steps, as you would do it in Selenium, you can then write your workflows or tests to automate every operating system.
[692.40 → 700.88] We are currently running on Windows, on Mac, and on iOS, especially for a legacy application and the Windows environment.
[701.28 → 705.24] We can test also these applications that we are not limited to web.
[705.96 → 707.64] Did this answer the question?
[707.92 → 708.76] It does, it does.
[708.82 → 709.14] Thank you.
[709.14 → 709.68] I appreciate that.
[709.86 → 710.70] It was a good explanation.
[711.00 → 721.66] So you obviously had a certain perspective of when you came to this problem because you had worked at Siemens, you had thought about this sort of automation.
[721.80 → 732.12] I'm wondering, as you've developed this technology and seen others that might have had this need or experienced this pain,
[732.66 → 740.20] what is the sort of range of things that you're seeing people either do or want to do with this kind of automation technology
[740.20 → 749.96] that might fit the use case, sometimes fit the use case that you had in mind initially, but sometimes might be a sort of new things that you didn't think about previously?
[749.96 → 766.46] I think currently, because we are using AI technology and with AI technology, you are a little bit more flexible what you can describe because you can learn it based on data and have not to explicitly describe it, which things you want to do.
[766.46 → 796.46] 00
[796.46 → 801.74] please, as normally normal workers will do with this,
[802.00 → 805.50] which are copying, for example, the PDF or information
[805.50 → 808.08] from the PDF over to another formula.
[808.62 → 811.50] And what you can do then with our technology is to say,
[811.58 → 815.30] hey, please automatically copy all the information over,
[815.42 → 817.44] which you see on the left side to the right side.
[817.44 → 821.38] This is where we think where the technology will go
[821.38 → 825.92] so that you can have not defined the matching of the files,
[826.28 → 829.46] everything, when you then connect also large language models,
[829.58 → 832.90] which have the ability to understand the language a little bit better
[832.90 → 836.84] or a little bit closer as we could, as humans can define it,
[837.10 → 838.44] then you can build such systems.
[839.32 → 840.32] Yeah, that's fascinating.
[840.50 → 845.78] I'm thinking of even like in, I had a friend that works in the offices,
[845.78 → 849.16] same office building that we're in here, and he stopped by
[849.16 → 850.14] and we were talking today.
[850.32 → 854.94] He takes screenshots of his work as he goes along in the day,
[854.94 → 856.42] like every so often.
[856.42 → 860.76] And he does this because he wants, like, he can't always remember
[860.76 → 864.48] like all the things that he was doing throughout the day.
[864.62 → 868.10] And so he takes these screenshots as a sort of historical record
[868.10 → 871.78] of like the various interfaces and what he was doing and such.
[871.88 → 875.70] So I had that in my mind as you were talking through all of these things.
[875.70 → 877.86] I'm like, hey, this would be really cool for him.
[877.86 → 882.66] He could, you know, potentially query certain things about his day
[882.66 → 887.64] and these interfaces and what he did and like create potential automations
[887.64 → 889.28] off of those.
[889.54 → 893.22] This is also a use case where we're thinking to be a recorder
[893.22 → 896.72] in the background, but then collecting repetitive tasks.
[896.92 → 901.18] And then say, for example, hey, we have now detected you have done this
[901.18 → 903.06] over the last week five times.
[903.38 → 904.68] Should we automate this for you?
[904.68 → 908.46] For example, yeah, there are also cases where the technology can go
[908.46 → 912.86] because we have the understanding of human interfaces and there was a lot
[912.86 → 916.24] of engineering stuff around this then can build such nice systems.
[916.24 → 921.44] That seems like an automation, like automation and AI seems to like scare
[921.44 → 926.30] people for some maybe justified reasons, some unjustified, or I don't know
[926.30 → 926.92] what's justified.
[927.22 → 932.28] But that's like an automation that like, why wouldn't I want that to save
[932.28 → 933.24] myself some time?
[933.34 → 936.28] I would love to automate some of my repetitive tasks.
[936.90 → 940.14] So one of the things I'm wondering is you're having looked at your website is
[940.14 → 943.68] you talk about like all the different platforms, you know, you get web apps
[943.68 → 945.02] and enterprise apps and everything.
[945.22 → 949.96] Are you able to take the same approach across the different platforms that
[949.96 → 951.26] you're targeting for that?
[951.60 → 954.68] And is that what makes it so flexible by doing screenshots and stuff?
[954.74 → 955.80] Is that what does it?
[955.80 → 960.84] Or do you have, how do you break down the challenge of getting from, you know,
[960.92 → 964.74] addressing one platform in your initial and then starting to spread out across
[964.74 → 965.72] the other platforms?
[966.26 → 970.78] From the other, the main technology is accessing the screenshot from the
[970.78 → 972.66] operating system and to controlling it.
[973.18 → 977.44] I think you, if you have tried to do it, there are a lot of open source software
[977.44 → 979.50] already available, which can do this.
[979.50 → 983.64] If you have such technology accessible, then you can take the screenshot.
[984.12 → 989.22] For example, we have Android support where we can take the screenshot, and it's the
[989.22 → 993.42] same model, and it's the same technology behind them as we are using this on the
[993.42 → 996.76] Windows operating system or on the Linux operating system.
[997.28 → 1001.22] And we have a general model which can solve all the tasks.
[1001.22 → 1010.04] So, Dominic, I'm already thinking of a lot of use cases that maybe I might want to automate
[1010.04 → 1012.04] and interact with the system.
[1012.52 → 1018.34] One of the things we were chatting about, like prior to actually hitting the record button
[1018.34 → 1027.08] on this episode was maybe the unique approach that Ask UI has taken in terms of more of a software
[1027.08 → 1034.50] engineering approach to understanding how this machine learning and AI systems work and utilizing
[1034.50 → 1040.26] them in a in this sort of like more practical software engineering approach to this.
[1040.34 → 1044.56] I'm wondering if you could talk about that in a little bit more detail and how you've
[1044.56 → 1049.92] approached these problems that you think is maybe unique or at least represents your perspective
[1049.92 → 1051.98] on how to build systems like this.
[1051.98 → 1052.62] Yeah.
[1052.62 → 1062.32] First, what I see or what we saw already in the past, the research area has built a lot of models,
[1062.80 → 1066.34] has released them on the public, but then it stopped it.
[1066.46 → 1070.76] After you have published your paper, you have no interest anymore to bring this to production.
[1071.50 → 1078.88] What we also see in that currently beginning from the 2020s, that a lot of new applications are coming,
[1078.88 → 1084.12] which try to solve this, to formalize this as software patterns.
[1084.28 → 1088.20] As I know it at the beginning, I started with the machine learning, and I was wondering,
[1088.70 → 1094.66] are there no software patterns like metric pattern, like trainer pattern, like other kinds of pattern
[1094.66 → 1097.70] which you can reuse and which you can communicate in a better way?
[1098.26 → 1100.72] Why are we the good at software development nowadays?
[1100.84 → 1106.16] It's because we have standardized the patterns which we use and used them everywhere.
[1106.16 → 1112.16] So this is what I was where we're always searching a little bit and also the tooling.
[1112.92 → 1116.86] And how did we approach this from the machine learning?
[1117.22 → 1119.40] We have different teams a little bit.
[1120.38 → 1125.38] The first thing, what we have done, we have built an application which used directly our model.
[1125.74 → 1130.16] And we used to plug in the best of the first model, which we can produce.
[1130.16 → 1137.12] And we started with our model, which has only five images for object detection,
[1137.24 → 1140.68] for detecting this five images training data set, which is not a lot.
[1141.64 → 1145.16] So, but we've done this to prove that this end-to-end possible.
[1145.62 → 1147.56] And we mocked a lot of things away.
[1147.94 → 1151.80] And then we go on out to the customers and say, hey, can you work with this?
[1151.88 → 1158.54] And they complained, yeah, it's nice, but your modular object detection model don't work so good.
[1158.54 → 1163.06] So what we've done in the next one, we collected more data, trained the better model.
[1163.34 → 1165.82] Then we go on to the customer access now enough.
[1165.96 → 1171.70] And then they were, okay, it's going the direction, but we could only support one application at the beginning.
[1172.54 → 1178.06] And then we had to relate it based on this and tries to connect all our things together.
[1178.74 → 1180.18] What does this mean on the other side?
[1180.48 → 1187.12] We started directly to taking, going out to the customer and then increasing everything.
[1187.12 → 1194.40] And now we are making, because this was hard at the beginning, because I mentioned already that in 2020,
[1194.64 → 1201.02] all the tools, PyTorch Lightning and Metaflow, and so everything came up, which you could reuse.
[1201.38 → 1208.30] And now we are migrating more and more to the data pipeline and trying to bring everything to the customer
[1208.30 → 1210.56] so that they can also train by themselves.
[1210.56 → 1217.14] But this is our software engineering approach where I say, hey, bring everything to the customer and let the customer complain.
[1217.90 → 1220.20] Then you're doing the next iteration steps.
[1220.46 → 1221.50] This is the last note.
[1221.92 → 1226.14] So as a follow-up, I want to ask you to kind of flip-flop what you just covered a little bit.
[1226.40 → 1229.28] And what's it like to engage from the customer's perspective?
[1229.34 → 1232.14] Because you're kind of taking it from your perspective, and we take it over.
[1232.14 → 1237.86] So if you're a customer, and you start to use Ask UI and deploy it, what does that picture look like?
[1237.90 → 1242.98] What does the customer go through as they start deploying or start utilizing the service?
[1243.50 → 1244.30] What he's doing, too?
[1244.78 → 1248.32] There's also a little bit of history, but what is this now?
[1248.40 → 1253.30] You're going now to our website, then log in with your credentials,
[1253.94 → 1260.14] and then you can directly upload your first screenshot and then simulate on this.
[1260.14 → 1265.90] So do a simulation directly on the screenshot so that you see the aha effect.
[1266.58 → 1271.76] And then the next step, what you want to do, if you have created your workflow a little bit,
[1271.80 → 1273.00] then you want to automate this.
[1273.52 → 1278.54] And you then schedule this, for example, in a Docker container in the background we have already.
[1279.18 → 1282.30] Also, if you're in the web environment.
[1282.30 → 1288.08] And then after time, you get the result, and you're happy that you have automated with really easy things
[1288.08 → 1290.90] and workflow.
[1291.54 → 1299.72] And what we are now doing is to reduce also the hurdle that you have to learn less as now,
[1299.84 → 1302.36] because this is the thing.
[1302.70 → 1307.76] We're trying to bring all problems from the user perspective away.
[1307.76 → 1312.76] The user has a really easy life to create automations, to maintain automations,
[1312.76 → 1317.30] and to schedule all the stuff, set up all the testing environments,
[1317.64 → 1320.70] because it's not only the automation part what you're interested in.
[1320.72 → 1325.00] You're also interested in where can you schedule it and all the broadening.
[1325.44 → 1326.90] How can you connect data and so on?
[1326.98 → 1329.26] This is what we are doing, what we are currently doing.
[1329.26 → 1330.48] That's awesome.
[1330.84 → 1338.78] I want to propose what I think is probably a bad idea, but I want to get your reaction to it.
[1338.78 → 1345.18] So I'm wondering, there's this way now that you've enabled people to automate their interactions
[1345.18 → 1346.66] with various UIs.
[1346.96 → 1354.26] And there are plenty of cases where I don't really care to interact with a UI,
[1354.58 → 1356.98] but I do need to accomplish a task.
[1356.98 → 1365.36] But I also, for example, one of these that I struggle with all the time is AWS and its interface,
[1366.06 → 1371.00] which is just like you can do everything, but it's super hard to understand how to do anything.
[1371.46 → 1373.06] Is there an opportunity?
[1373.74 → 1378.18] Let's say, and again, I think this is probably from the start a bad idea,
[1378.32 → 1386.48] but let's say I just gave some sort of agent tied in to ask UI my credit card information and whatever.
[1386.48 → 1396.64] And just said, hey, I want you to create an AWS account and spin up this infrastructure and do this.
[1396.86 → 1400.62] And then when you're done, give me the URL so I can access my,
[1400.98 → 1405.42] like here's the GitHub repo, tell me when it's ready, and here's my URL.
[1405.78 → 1409.80] Now, I imagine that would also need to tie into other external knowledge,
[1409.80 → 1412.82] like the documentation from AWS or something.
[1413.10 → 1418.34] But is this type of scenario anything that you've been talking about internally
[1418.34 → 1421.42] or see as things that might come about in the future?
[1421.54 → 1424.88] As soon as you start automating things around UIs,
[1425.52 → 1428.20] there's the one side of it, which I think we've talked about a lot,
[1428.30 → 1432.22] which is automating the things you've already done with UIs.
[1432.22 → 1437.48] But what if you want to do things with UIs that you haven't done yet,
[1437.64 → 1439.52] but don't really care to learn how to do?
[1439.94 → 1443.24] This is also our plan to do this to leverage that.
[1443.30 → 1446.48] We already played a little bit around with large language models,
[1446.96 → 1449.84] giving all the documentation to do this,
[1450.06 → 1453.78] and also tries to translate, for example, Google documentation
[1453.78 → 1456.16] and create out of this Ask UI step.
[1456.48 → 1458.12] This was working quite good.
[1458.12 → 1461.22] And the direction will go there.
[1461.70 → 1463.62] So in the future, we can do this.
[1464.02 → 1465.58] So there was another part.
[1465.64 → 1466.92] This was the attention base.
[1467.32 → 1469.34] Please create me an ET2 instance,
[1469.50 → 1470.94] and here are my credit card information.
[1471.04 → 1472.10] This was the intention.
[1472.78 → 1473.58] Please do this.
[1474.02 → 1474.76] You can do this.
[1474.90 → 1477.62] But the main problem with this is humans,
[1478.16 → 1481.82] if you talk also to your colleague or to someone from another nation and so on,
[1482.16 → 1483.90] you will always have communication hurdles.
[1483.90 → 1487.60] So you have always to have the tiny steps in between
[1487.60 → 1490.34] where you then can correct a little bit up.
[1490.62 → 1491.32] This is one thing.
[1491.62 → 1495.24] The other thing is, are we trustful for credit card information?
[1495.86 → 1497.08] For this, I have to say,
[1497.98 → 1500.76] you're submitting also in GitHub or GitLab,
[1501.28 → 1505.76] your security tokens to your AWS access.
[1506.12 → 1508.38] So there are standards already in place,
[1508.42 → 1510.92] which are also validated, which can do this.
[1511.02 → 1512.60] And this is what we have to follow.
[1512.60 → 1515.20] We have also business, also enterprise customers,
[1515.20 → 1516.96] which wants to have the standards.
[1517.24 → 1519.30] So we have to be compliant with the standards.
[1519.98 → 1521.86] So from our side, it's no problem.
[1522.00 → 1522.80] You can trust us.
[1523.72 → 1526.18] But on the other way, you have also the possibility,
[1526.46 → 1529.92] because it's nice to create the tests online,
[1530.50 → 1533.30] download everything and execute this locally on your machine
[1533.30 → 1535.50] without any access on our side.
[1535.92 → 1538.04] You can also hide all the information,
[1538.58 → 1540.36] all the secrets, I would say,
[1540.36 → 1542.82] on your device and have the guarantee
[1542.82 → 1545.74] that they are not leaked on anything.
[1545.74 → 1549.14] Yeah, that was another thing I was going to ask is like,
[1549.62 → 1552.20] hey, if I'm going to a site,
[1552.76 → 1554.66] like let's just say, I'll give an example
[1554.66 → 1557.28] because I love the product and what they're doing.
[1557.78 → 1560.14] So Chris, you remember we had Josh from Kochi
[1560.14 → 1562.76] on talking about their voice studio and all that.
[1562.84 → 1564.14] I've been using that recently.
[1564.38 → 1567.14] You go in, you can input your text,
[1567.46 → 1570.04] like a sentence and synthesize a voice.
[1570.04 → 1573.58] And then you can change like the language or something
[1573.58 → 1575.84] and then like go through, export the file.
[1575.96 → 1579.66] So there's like, there's not just a UI interaction here.
[1579.66 → 1582.16] There's like input data and output data
[1582.16 → 1584.00] that might include things like passwords.
[1584.34 → 1585.98] It might also include things like,
[1586.08 → 1588.80] hey, I generated a file with this UI.
[1589.00 → 1590.66] Like, where does that go?
[1590.72 → 1592.60] Like a quick download or something?
[1592.66 → 1593.04] I don't know.
[1593.36 → 1595.08] What's the best practices around
[1595.08 → 1596.92] as you're automating these things?
[1596.92 → 1600.22] How should a customer think about these like inputs and outputs?
[1600.62 → 1603.98] And how do you handle those in terms of what you're building?
[1604.82 → 1607.46] I would forward this question to
[1607.46 → 1610.92] how are you normally doing integration tests or end-to-end tests?
[1610.98 → 1612.64] You have always the same data there.
[1613.24 → 1615.68] So first, to recommend customers,
[1615.90 → 1620.26] try to use always synthetic or generated data.
[1620.58 → 1622.66] Don't leak production data to it
[1622.66 → 1623.58] because it's security.
[1623.92 → 1625.62] This is the first thing.
[1625.62 → 1629.00] What do you learn when you start automating and testing?
[1629.18 → 1630.24] Don't use production data.
[1631.08 → 1631.96] And then the other thing,
[1632.40 → 1634.80] you have to apply security standards.
[1635.30 → 1637.94] So there are environment variables or secret files
[1637.94 → 1639.72] which you can inject to it,
[1640.10 → 1641.90] go with it, do it,
[1642.22 → 1644.12] use our security function
[1644.12 → 1647.28] that you're not sending to us anything
[1647.28 → 1648.74] what's related to it.
[1649.14 → 1651.50] And this is what I could recommend to the customer.
[1652.08 → 1652.98] I'm curious.
[1653.14 → 1654.86] We've been talking about testing for a while
[1654.86 → 1657.56] and most of the use cases have been unit tests.
[1657.70 → 1659.02] Are there any other types of testing
[1659.02 → 1660.98] like integration testing that you're able to do?
[1661.46 → 1663.34] Is there a workflow for those kinds of things?
[1663.34 → 1666.88] Or is this really focused on kind of the screenshot itself
[1666.88 → 1668.92] and everyone stands alone?
[1669.04 → 1670.34] Is there any way to tie them together?
[1670.34 → 1671.34] Yeah.
[1671.34 → 1671.44] Yeah.
[1671.54 → 1673.18] You can tie them together.
[1673.18 → 1674.72] What we are,
[1674.76 → 1676.16] we are only a library
[1676.16 → 1677.84] which you can use in TypeScript.
[1678.08 → 1678.60] In the future,
[1678.82 → 1681.06] we will also support Python and other languages
[1681.06 → 1683.46] to make this technology also available.
[1684.08 → 1687.00] But you can also combine this with Selenium
[1687.00 → 1688.04] or some other techniques.
[1688.22 → 1690.62] You can connect to a Congo database,
[1690.96 → 1691.96] getting the data out,
[1692.46 → 1695.44] processing this in terms to other systems and so on.
[1695.44 → 1696.08] Yeah.
[1696.08 → 1698.36] We are really flexible in this race
[1698.36 → 1700.44] because our main concept,
[1700.68 → 1702.76] this is maybe also another thing
[1702.76 → 1704.78] that's unique on our side.
[1705.12 → 1707.74] We are thinking that automation
[1707.74 → 1709.20] or user interface automation
[1709.20 → 1711.66] as a low-code user interface automation
[1711.66 → 1713.14] is to a certain level nice
[1713.14 → 1716.86] because it can give the ability to other people.
[1717.14 → 1718.38] But on a certain point,
[1718.62 → 1719.68] we are reaching the limit.
[1719.68 → 1720.62] And for this,
[1720.72 → 1721.32] you need developers
[1721.32 → 1725.20] to build some nice stuff to automate
[1725.20 → 1726.74] or to connect, for example,
[1726.80 → 1727.34] to MongoDB
[1727.34 → 1729.56] or some other sort of stuff.
[1730.02 → 1730.74] In this case,
[1731.06 → 1733.16] you can always have the possibility
[1733.16 → 1736.00] to go from our low-code view
[1736.00 → 1737.40] to our code view
[1737.40 → 1738.92] and insert directly code.
[1739.18 → 1740.10] So there's no problem.
[1740.28 → 1740.98] You can do this.
[1741.46 → 1743.56] And you can also install other libraries.
[1743.56 → 1751.38] This is a Changelog News Break.
[1752.00 → 1753.40] Page Find looks pretty cool.
[1753.74 → 1756.06] It's a fully static search library
[1756.06 → 1758.18] that aims to perform well on large sites
[1758.18 → 1760.84] while using as little of your user's bandwidth
[1760.84 → 1761.74] as possible
[1761.74 → 1763.84] and without hosting any infrastructure.
[1764.54 → 1766.90] It runs after your static site generator
[1766.90 → 1769.46] like Hugo, Eleventh, Astro, etc.
[1770.04 → 1771.94] and generates a static search bundle
[1771.94 → 1773.28] to add to your built files.
[1773.66 → 1775.86] It then exposes a JavaScript search API
[1775.86 → 1777.82] that can be used anywhere on your site.
[1778.34 → 1778.60] Quote,
[1778.68 → 1779.70] The goal of Page Find
[1779.70 → 1780.44] is that websites
[1780.44 → 1782.26] with tens of thousands of pages
[1782.26 → 1783.30] should be searchable
[1783.30 → 1784.48] by someone in their browser
[1784.48 → 1785.36] while consuming
[1785.36 → 1787.06] as little bandwidth as possible.
[1788.06 → 1789.34] Page Find's search index
[1789.34 → 1790.46] is split into chunks
[1790.46 → 1792.00] so that searching in the browser
[1792.00 → 1793.36] only ever needs to load
[1793.36 → 1795.42] a small subset of the search index.
[1795.92 → 1797.66] Page Find can run a full-text search
[1797.66 → 1799.16] on a 10,000-page site
[1799.16 → 1800.30] with a total network payload
[1800.30 → 1801.50] under 300 kilobytes,
[1801.70 → 1803.50] including the Page Find library itself.
[1804.00 → 1804.66] For most sites,
[1804.90 → 1806.50] this will be closer to 100 kilobytes.
[1806.94 → 1807.38] End quote.
[1807.78 → 1808.96] I'd love to see a comparison.
[1809.44 → 1810.54] Link me up if you know of one.
[1810.66 → 1811.68] But my guess is that
[1811.68 → 1813.36] this could easily replace Algeria
[1813.36 → 1814.90] on lots of open-source docs
[1814.90 → 1815.84] and websites.
[1816.34 → 1817.60] One less service to depend on.
[1817.86 → 1818.54] Why not, right?
[1818.54 → 1822.20] You just heard one of our five top stories
[1822.20 → 1824.04] from Monday's Changelog News.
[1824.42 → 1825.64] Subscribe to the podcast
[1825.64 → 1827.58] to get all the week's top stories
[1827.58 → 1829.28] and pop your email address in
[1829.28 → 1831.14] at changelog.com slash news
[1831.14 → 1833.60] to also receive our free companion email
[1833.60 → 1835.84] with even more developer news
[1835.84 → 1836.82] worth your attention.
[1837.26 → 1837.88] Once again,
[1838.06 → 1840.70] that's changelog.com slash news.
[1840.70 → 1848.00] I always like to ask guests
[1848.00 → 1850.02] who have really manifested
[1850.02 → 1851.38] some new idea
[1851.38 → 1853.64] that's really driven fundamentally
[1853.64 → 1856.40] by AI and machine learning
[1856.40 → 1857.32] this question.
[1857.52 → 1857.96] And that's,
[1858.32 → 1858.46] you know,
[1858.50 → 1861.22] as you are building out this product,
[1861.48 → 1863.50] what challenges did you find
[1863.50 → 1864.54] in using,
[1864.98 → 1866.26] you already eluded this
[1866.26 → 1867.90] a little bit with like,
[1868.02 → 1868.20] oh,
[1868.48 → 1869.48] researchers release
[1869.48 → 1870.66] like all of these models
[1870.66 → 1872.86] and then like what happens after that?
[1872.94 → 1874.50] They're not really supported
[1874.50 → 1875.94] or maybe they die off
[1875.94 → 1876.74] or other things.
[1876.92 → 1878.28] So what specifically
[1878.28 → 1880.52] were the kind of machine learning
[1880.52 → 1881.68] or AI challenges
[1881.68 → 1883.96] that you faced
[1883.96 → 1885.18] as you were trying
[1885.18 → 1886.14] to make this work?
[1886.20 → 1887.10] You eluded a little bit
[1887.10 → 1888.48] to the data side of things
[1888.48 → 1890.34] and kind of adding data over time,
[1890.34 → 1891.34] but I imagine there's
[1891.34 → 1893.10] much, much more than that.
[1893.46 → 1895.54] So what are some of those things
[1895.54 → 1896.38] that stand out,
[1896.50 → 1897.86] just practical things
[1897.86 → 1898.78] that you faced
[1898.78 → 1899.86] in trying to apply
[1899.86 → 1900.60] this technology
[1900.60 → 1902.10] to a real world
[1902.10 → 1903.40] automation problem?
[1903.96 → 1904.10] Yeah,
[1904.22 → 1905.64] maybe to start at the beginning,
[1905.96 → 1906.38] previously,
[1906.64 → 1908.26] I was a software engineer.
[1908.40 → 1909.14] I had no clue
[1909.14 → 1910.10] about machine learning.
[1910.80 → 1911.60] I get a little bit
[1911.60 → 1912.60] theoretical knowledge,
[1912.76 → 1914.32] but theoretical is nice,
[1914.44 → 1915.06] but in practice,
[1915.14 → 1916.08] it's completely different.
[1916.82 → 1918.88] So I had no clue
[1918.88 → 1919.76] that, for example,
[1920.40 → 1921.88] if you adapt the learning rates,
[1921.88 → 1923.26] you can bring your model
[1923.26 → 1924.16] to convergence.
[1924.16 → 1926.18] And such things
[1926.18 → 1927.44] I struggled at the beginning
[1927.44 → 1929.36] with also how you connect
[1929.36 → 1930.68] the layers at the beginning
[1930.68 → 1932.50] to make everything work.
[1932.86 → 1934.06] But then you've solved
[1934.06 → 1934.70] this problem.
[1935.18 → 1935.98] Then the next step
[1935.98 → 1936.96] where you start to struggle
[1936.96 → 1939.30] is making the experiments
[1939.30 → 1941.12] visible so that you generate
[1941.12 → 1941.82] the right metrics,
[1941.90 → 1942.38] that you see,
[1942.48 → 1943.26] that you understand
[1943.26 → 1944.22] what you're learning
[1944.22 → 1945.26] or what you're not learning.
[1945.66 → 1946.50] Then when you have solved
[1946.50 → 1947.74] this challenge for yourself,
[1947.82 → 1948.90] so you have tried out
[1948.90 → 1949.76] a tensor board,
[1950.32 → 1951.28] you have the next challenge
[1951.28 → 1954.46] to go to how can I manage the data?
[1954.56 → 1955.60] How can I increase the data?
[1955.96 → 1957.56] How can I version the data?
[1958.20 → 1959.10] So, and then you came
[1959.10 → 1959.64] in the challenge,
[1959.88 → 1960.90] how can you do
[1960.90 → 1962.60] repeatable experiments
[1962.60 → 1963.38] that you can say,
[1963.46 → 1964.32] hey, you have done
[1964.32 → 1965.90] now progress step by step.
[1966.40 → 1966.98] And for this,
[1967.10 → 1967.76] you have to then
[1967.76 → 1969.14] to search a lot
[1969.14 → 1971.40] about what tools
[1971.40 → 1972.06] are out there,
[1972.16 → 1973.08] which tools are good,
[1973.24 → 1974.84] you need to know
[1974.84 → 1975.46] a feeling.
[1976.06 → 1977.02] Then the next step
[1977.02 → 1978.46] is you've figured out
[1978.46 → 1979.34] that you have messed
[1979.34 → 1979.96] everything up
[1979.96 → 1980.40] and your code
[1980.40 → 1982.62] is totally out there.
[1982.96 → 1984.16] So you have to think
[1984.16 → 1984.74] a little bit out
[1984.74 → 1986.24] how can I structure the code?
[1986.68 → 1987.90] This is what I mentioned
[1987.90 → 1989.12] previously with patterns.
[1989.70 → 1990.24] So you're looking
[1990.24 → 1991.54] in other repositories
[1991.54 → 1992.42] how other developers
[1992.42 → 1993.44] have structured the code
[1993.44 → 1995.34] that it's more maintainable
[1995.34 → 1996.30] and more reusable.
[1997.30 → 1998.32] So in Cavalry view
[1998.32 → 1999.66] and then you're coming across,
[1999.74 → 2000.14] for example,
[2000.26 → 2000.84] PyTorch-like,
[2001.00 → 2001.80] which would I say,
[2001.90 → 2002.36] which are doing
[2002.36 → 2003.08] this really great
[2003.08 → 2005.02] to build up models
[2005.02 → 2006.40] in a modular way.
[2007.30 → 2008.44] And then you're
[2008.44 → 2009.44] not only one developer,
[2009.56 → 2010.46] then you're two developers,
[2010.76 → 2011.74] two machine learnings,
[2011.76 → 2012.20] the researcher,
[2012.34 → 2013.12] then you have to communicate
[2013.12 → 2013.64] in a way.
[2013.74 → 2015.62] So you have to exchange data.
[2015.96 → 2017.64] So then the thing is
[2017.64 → 2018.42] you're starting to
[2018.42 → 2020.04] copy and paste data
[2020.04 → 2021.16] and send it over Slack
[2021.16 → 2021.78] or some stuff.
[2021.86 → 2022.46] Then you have to say,
[2022.54 → 2023.86] hey, it's totally stupid
[2023.86 → 2024.48] what we are doing.
[2024.58 → 2025.66] We need the data platform.
[2026.20 → 2026.92] And then with you
[2026.92 → 2028.52] going through step by step,
[2029.10 → 2029.88] you have reached
[2029.88 → 2031.06] the complete expertise
[2031.06 → 2031.52] that you say,
[2031.58 → 2032.94] hey, now we need
[2032.94 → 2033.84] a complete data storage.
[2034.00 → 2035.04] We need a metric system.
[2035.04 → 2037.14] There's how we exchange data
[2037.14 → 2038.02] between the teams.
[2038.36 → 2038.92] This is a way
[2038.92 → 2039.98] how we label data.
[2040.52 → 2041.56] So for example,
[2041.64 → 2042.72] also the other challenge
[2042.72 → 2043.96] is not only exchanging data,
[2044.04 → 2044.58] getting data.
[2044.82 → 2045.96] This is also the challenge
[2045.96 → 2047.32] labelling goods data.
[2047.50 → 2048.10] Then you're looking
[2048.10 → 2049.00] at the labelling tools.
[2049.58 → 2050.70] So then you figure out,
[2050.82 → 2050.90] yeah,
[2050.94 → 2051.86] labelling tools are nice
[2051.86 → 2052.88] for standard use cases,
[2052.88 → 2053.64] but sometimes,
[2053.90 → 2054.94] especially in our case,
[2055.36 → 2055.92] because we have
[2055.92 → 2057.00] five different models
[2057.00 → 2058.18] which are chained together
[2058.18 → 2059.00] nicely,
[2059.40 → 2060.04] that you have labelled
[2060.04 → 2061.46] different kinds of data
[2061.46 → 2062.56] for different models.
[2062.56 → 2064.56] because these model types
[2064.56 → 2065.82] are fitting perfectly
[2065.82 → 2066.86] for this use case.
[2067.44 → 2068.22] So you are then
[2068.22 → 2069.64] thinking about
[2069.64 → 2071.22] how you can improve
[2071.22 → 2072.04] the labelling process.
[2072.34 → 2073.42] So now we are building
[2073.42 → 2074.70] a new labelling tool
[2074.70 → 2075.68] based on Streamlet
[2075.68 → 2077.22] so that we can easily
[2077.22 → 2077.84] connect,
[2077.98 → 2078.38] for example,
[2078.46 → 2079.56] our inference part
[2079.56 → 2080.90] that we can do
[2080.90 → 2082.00] a little bit preloading,
[2082.10 → 2083.34] then can automate stuff
[2083.34 → 2084.92] and to improve everything.
[2085.26 → 2085.28] So,
[2085.90 → 2087.48] and then at the beginning,
[2087.48 → 2088.10] you remember
[2088.10 → 2089.14] that you talked once
[2089.14 → 2090.06] with some guy
[2090.06 → 2090.82] which always said
[2090.82 → 2092.14] if you do machine learning,
[2092.32 → 2093.16] you will end up
[2093.16 → 2093.82] to building
[2093.82 → 2094.56] a labelling tool
[2094.56 → 2095.42] where we now reach.
[2096.80 → 2097.50] You've reached
[2097.50 → 2098.08] the pinnacle.
[2099.70 → 2100.82] But it's a journey
[2100.82 → 2101.80] and I think
[2101.80 → 2102.44] when somebody
[2102.44 → 2103.50] would now ask me
[2103.50 → 2104.16] how to start,
[2104.22 → 2104.72] I would answer
[2104.72 → 2105.60] completely different
[2105.60 → 2106.80] in a completely
[2106.80 → 2107.44] different way.
[2107.68 → 2109.54] So that's literally
[2109.54 → 2110.16] what I was about
[2110.16 → 2110.70] to ask you
[2110.70 → 2111.30] because that was
[2111.30 → 2112.46] a fantastic journey
[2112.46 → 2113.62] that you just took us on
[2113.62 → 2116.26] about all the practicalities
[2116.26 → 2116.74] and, you know,
[2117.14 → 2117.62] that, you know,
[2117.64 → 2118.74] you solve one problem
[2118.74 → 2119.50] and you hit the next
[2119.50 → 2120.18] and you hit the next
[2120.18 → 2120.92] and you hit the next
[2120.92 → 2123.08] and you just describe
[2123.08 → 2124.26] coming in
[2124.26 → 2126.32] completely new
[2126.32 → 2127.04] to this
[2127.04 → 2128.14] and taking it
[2128.14 → 2128.92] all the way
[2128.92 → 2129.86] to being very,
[2129.94 → 2130.94] very productive
[2130.94 → 2132.52] and all the practicalities.
[2132.92 → 2133.02] So,
[2133.38 → 2134.16] that's actually
[2134.16 → 2135.18] what I want to ask you
[2135.18 → 2135.56] is you said
[2135.56 → 2136.22] I wouldn't do it
[2136.22 → 2136.70] the same way.
[2136.74 → 2137.52] I'd like to know
[2137.52 → 2138.90] there is
[2138.90 → 2140.46] at least one person
[2140.46 → 2141.24] out there right now
[2141.24 → 2142.08] if not many
[2142.08 → 2143.44] that are thinking
[2143.44 → 2143.96] about AI.
[2144.36 → 2145.10] They may have dabbled
[2145.10 → 2145.46] in it.
[2145.68 → 2145.96] Maybe,
[2146.28 → 2146.82] maybe not.
[2147.14 → 2147.94] They have an idea
[2147.94 → 2148.76] for a startup.
[2149.28 → 2150.46] They're listening to you
[2150.46 → 2151.10] and they're going
[2151.10 → 2152.48] that's the guy
[2152.48 → 2153.12] you know,
[2153.20 → 2154.24] who started doing this
[2154.24 → 2155.42] but I have my own idea.
[2155.84 → 2156.82] What would you tell them?
[2156.92 → 2157.08] Like,
[2157.12 → 2157.98] how do you get started,
[2158.08 → 2158.44] you know,
[2158.56 → 2159.58] to get going?
[2160.12 → 2161.54] Because this is a daunting
[2161.54 → 2162.78] field to break into.
[2163.22 → 2163.82] You mean only
[2163.82 → 2164.96] the machine learning part
[2164.96 → 2165.98] or to start a startup
[2165.98 → 2166.78] based on machine?
[2167.78 → 2168.90] Mostly the machine learning.
[2169.00 → 2169.10] Like,
[2169.16 → 2170.24] how did you learn?
[2170.30 → 2171.30] It's a skill set.
[2171.64 → 2172.50] It takes the time
[2172.50 → 2173.08] to digest
[2173.08 → 2174.26] and it's constantly evolving.
[2174.66 → 2175.86] How did you digest
[2175.86 → 2176.74] that skill set
[2176.74 → 2177.82] so that you could be productive?
[2178.58 → 2178.82] Okay.
[2179.72 → 2180.58] First,
[2180.72 → 2181.96] what I would recommend
[2181.96 → 2184.12] directly introduce
[2184.12 → 2184.82] tools
[2184.82 → 2185.94] which support you.
[2186.54 → 2187.62] Use directly
[2187.62 → 2188.34] hugging phase.
[2188.48 → 2189.20] Try to build
[2189.20 → 2190.14] models based
[2190.14 → 2190.86] on hugging phase
[2190.86 → 2191.92] so that you have libraries
[2191.92 → 2192.58] or based on
[2192.58 → 2193.38] PyTorch Lightning
[2193.38 → 2194.66] because they're
[2194.66 → 2195.66] giving things
[2195.66 → 2196.22] for free,
[2196.86 → 2197.80] I would always say.
[2197.92 → 2198.76] Then the other thing
[2198.76 → 2200.12] I would directly introduce
[2200.12 → 2201.28] version control system
[2201.28 → 2201.82] for data.
[2202.38 → 2202.66] Beginning,
[2202.82 → 2203.56] I would recommend
[2203.56 → 2204.58] we are currently
[2204.58 → 2205.32] using Dilemma.
[2205.32 → 2206.32] I would now recommend
[2206.32 → 2208.24] DVC at the beginning
[2208.24 → 2209.30] and then
[2209.30 → 2211.20] try to find,
[2211.34 → 2212.32] especially for the
[2212.32 → 2213.26] machine learning part,
[2213.94 → 2214.54] try to find
[2214.54 → 2215.16] one researcher
[2215.16 → 2216.20] and one software engineer
[2216.20 → 2217.12] and bring them together
[2217.12 → 2218.14] and let them communicate
[2218.14 → 2219.52] because then you get
[2219.52 → 2220.74] the efficiency
[2220.74 → 2222.20] from software engineers
[2222.20 → 2222.72] or especially
[2222.72 → 2223.70] cloud software engineers
[2223.70 → 2224.92] and you get the
[2224.92 → 2226.38] research knowledge
[2226.38 → 2227.30] and bring them together
[2227.30 → 2228.64] so they can
[2228.64 → 2230.34] learn from each other
[2230.34 → 2231.54] to exchange ideas
[2231.54 → 2232.60] how to do this
[2232.60 → 2233.54] in the software manner
[2233.54 → 2235.32] and how to do research.
[2235.82 → 2236.48] And this,
[2236.66 → 2238.48] when I would start again,
[2238.60 → 2239.68] I would now say,
[2239.80 → 2239.98] hey,
[2240.48 → 2241.74] here you have one team,
[2242.26 → 2242.80] two people,
[2243.10 → 2243.90] one software guy,
[2244.14 → 2245.04] which DevOps background,
[2245.50 → 2247.00] also the software development
[2247.00 → 2247.92] and DevOps background
[2247.92 → 2248.52] a little bit
[2248.52 → 2250.14] and then bring a
[2250.14 → 2251.12] machine learning
[2251.12 → 2252.02] researcher to it
[2252.02 → 2253.54] and then I think
[2253.54 → 2254.60] they would benefit
[2254.60 → 2255.08] the best.
[2255.50 → 2255.60] Yeah.
[2255.60 → 2257.66] And you talked a little bit
[2257.66 → 2259.64] about your journey
[2259.64 → 2261.14] in terms of
[2261.14 → 2262.36] the technical side
[2262.36 → 2263.02] and learning about
[2263.02 → 2263.70] these tools
[2263.70 → 2265.22] and also the kind of
[2265.22 → 2266.78] bringing on more people
[2266.78 → 2267.46] side.
[2267.64 → 2269.54] As you look forward
[2269.54 → 2272.18] to the next steps
[2272.18 → 2272.72] in the roadmap,
[2272.92 → 2274.22] I love it how you publish
[2274.22 → 2274.94] your roadmap
[2274.94 → 2275.74] on your site,
[2275.84 → 2276.88] which is really cool.
[2277.04 → 2278.22] As you look forward
[2278.22 → 2279.10] to the future
[2279.10 → 2280.46] of that roadmap,
[2281.18 → 2282.16] what do you feel like
[2282.16 → 2283.30] are the challenges
[2283.30 → 2284.30] that you're facing
[2284.30 → 2285.16] right now
[2285.16 → 2286.00] as someone
[2286.00 → 2286.90] who is,
[2287.44 → 2288.34] does it have to do
[2288.34 → 2288.56] with,
[2288.70 → 2288.82] oh,
[2288.90 → 2289.64] now what do I do
[2289.64 → 2290.18] with all these
[2290.18 → 2291.46] generative AI stuff
[2291.46 → 2292.24] and how does that
[2292.24 → 2293.90] factor into our product
[2293.90 → 2295.06] or does it have to do
[2295.06 → 2296.48] with how do we make
[2296.48 → 2297.86] these models better
[2297.86 → 2298.84] and support a wider
[2298.84 → 2299.96] set of use cases
[2299.96 → 2301.14] or is it,
[2301.14 → 2302.08] is it a combination
[2302.08 → 2302.78] or something
[2302.78 → 2303.56] completely different?
[2304.26 → 2305.12] I would say more,
[2305.46 → 2306.46] it's not more about
[2306.46 → 2307.58] the technical challenge,
[2308.16 → 2308.92] what you could solve
[2308.92 → 2310.00] because technical challenges
[2310.00 → 2310.62] you can solve
[2310.62 → 2311.16] with a little
[2311.16 → 2312.22] with knowledge
[2312.22 → 2313.40] and a little bit of research.
[2314.14 → 2314.72] So normally
[2314.72 → 2316.40] if it's not physically
[2316.40 → 2317.16] impossible,
[2317.42 → 2318.04] you can solve
[2318.04 → 2318.60] those things
[2318.60 → 2319.50] with a certain tongue.
[2319.96 → 2320.84] This is normally
[2320.84 → 2322.18] a normal problem.
[2322.58 → 2323.20] The main problem
[2323.20 → 2324.36] is what I see
[2324.36 → 2327.12] is to speed up
[2327.12 → 2327.70] the development
[2327.70 → 2328.66] process itself
[2328.66 → 2330.86] so that the right
[2330.86 → 2332.32] things are researched,
[2332.46 → 2333.12] the right things
[2333.12 → 2334.42] are designed
[2334.42 → 2335.46] and the right things
[2335.46 → 2336.72] are started
[2336.72 → 2337.32] to develop
[2337.32 → 2338.16] so that you're
[2338.16 → 2339.00] bringing more
[2339.00 → 2339.64] the focus
[2339.64 → 2340.52] on one topic
[2340.52 → 2341.56] and if you have
[2341.56 → 2342.82] a lot of people
[2342.82 → 2343.54] in your company
[2343.54 → 2345.02] or a lot of,
[2345.08 → 2345.50] I would say,
[2345.54 → 2346.10] interfaces,
[2346.86 → 2347.94] then you have
[2347.94 → 2348.66] to bring them
[2348.66 → 2350.12] one common
[2350.12 → 2350.74] understanding
[2350.74 → 2351.68] what you want
[2351.68 → 2352.18] to achieve,
[2352.44 → 2353.04] how you want
[2353.04 → 2353.48] to work,
[2353.80 → 2354.34] how you want
[2354.34 → 2355.18] to define
[2355.18 → 2355.66] requirement.
[2356.10 → 2356.44] This is,
[2356.56 → 2356.90] I would say,
[2356.96 → 2358.42] currently the main
[2358.42 → 2359.04] challenge when I
[2359.04 → 2359.64] would say so
[2359.64 → 2360.80] and then from
[2360.80 → 2361.24] the technical
[2361.24 → 2361.76] challenge,
[2362.22 → 2363.18] we have to talk
[2363.18 → 2363.80] to customers,
[2364.04 → 2364.78] get the feedback,
[2365.04 → 2365.56] build the staff
[2365.56 → 2366.18] as quick as
[2366.18 → 2366.56] possible
[2366.56 → 2367.80] and iterate
[2367.80 → 2369.24] in terms of
[2369.24 → 2370.26] what the business
[2370.26 → 2371.06] wants to have.
[2371.82 → 2372.94] So as we kind
[2372.94 → 2374.14] of wind up here,
[2374.40 → 2375.22] and this is
[2375.22 → 2375.96] pretty typical,
[2376.08 → 2377.58] we love to get
[2377.58 → 2378.46] kind of the benefit
[2378.46 → 2379.28] of your insight,
[2379.38 → 2380.10] not only for these
[2380.10 → 2381.40] short-term practicalities,
[2381.60 → 2382.58] but a little bit
[2382.58 → 2383.42] of the dreaming
[2383.42 → 2384.50] and as you're,
[2384.94 → 2386.30] as you are kind
[2386.30 → 2386.48] of,
[2386.66 → 2388.02] you've come this far
[2388.02 → 2388.62] in this journey
[2388.62 → 2389.46] that you've described
[2389.46 → 2391.22] and you now have
[2391.22 → 2392.36] this capability
[2392.36 → 2393.40] that didn't exist
[2393.40 → 2394.12] as an entrepreneur,
[2394.12 → 2395.58] as you're looking
[2395.58 → 2396.24] at the future,
[2396.56 → 2397.72] what are the ideas
[2397.72 → 2399.02] that may be
[2399.02 → 2399.54] speculative,
[2399.80 → 2400.36] it doesn't have
[2400.36 → 2400.94] to be based
[2400.94 → 2401.98] in the realities
[2401.98 → 2402.60] of what we have
[2402.60 → 2402.88] today,
[2403.32 → 2403.68] where do you want
[2403.68 → 2404.48] to go with this?
[2404.56 → 2404.68] Like,
[2404.72 → 2405.36] what do you envision
[2405.36 → 2405.92] building,
[2406.10 → 2406.56] you know,
[2406.60 → 2407.24] over the next
[2407.24 → 2408.26] couple of years,
[2408.48 → 2408.76] you know,
[2409.02 → 2410.18] you can pick the horizon,
[2410.32 → 2410.70] two years,
[2410.80 → 2411.14] five years,
[2411.22 → 2411.90] whatever you think,
[2412.42 → 2413.14] so when you lay
[2413.14 → 2413.72] in bed at night,
[2413.76 → 2414.06] you're like,
[2414.16 → 2414.78] that's the place
[2414.78 → 2415.78] I'm going eventually.
[2416.02 → 2416.80] What does that look like?
[2417.36 → 2418.50] Maybe to look a little
[2418.50 → 2419.50] bit back in the history,
[2419.62 → 2420.32] how this project
[2420.32 → 2420.76] started,
[2420.76 → 2421.70] I think I haven't
[2421.70 → 2423.18] told this before.
[2423.82 → 2425.24] When I was also
[2425.24 → 2425.82] at Siemens,
[2425.82 → 2426.74] then I also do,
[2426.94 → 2427.26] I've done my
[2427.26 → 2427.76] master's thesis
[2427.76 → 2428.68] about visual question
[2428.68 → 2429.04] answering,
[2429.24 → 2430.06] which should solve
[2430.06 → 2430.86] the tasks
[2430.86 → 2431.50] that we are doing
[2431.50 → 2432.20] now in separate
[2432.20 → 2433.52] tasks as an
[2433.52 → 2434.14] end-to-end task.
[2434.64 → 2434.76] So,
[2435.28 → 2436.80] what my dream is,
[2436.92 → 2438.72] is to take the
[2438.72 → 2440.14] now available
[2440.14 → 2440.80] technology,
[2440.94 → 2441.94] large language models,
[2442.36 → 2443.60] including the
[2443.60 → 2444.32] visual part
[2444.32 → 2445.06] and the natural
[2445.06 → 2445.38] part,
[2445.48 → 2446.28] combine everything
[2446.28 → 2447.88] so that we can
[2447.88 → 2449.24] teach or bring
[2449.24 → 2450.22] every kind of
[2450.22 → 2451.04] data inside the
[2451.04 → 2451.24] model.
[2451.74 → 2452.66] What does this mean,
[2452.74 → 2453.60] every kind of data?
[2453.60 → 2454.24] So,
[2454.32 → 2455.76] this means we get,
[2456.00 → 2456.64] for example,
[2457.14 → 2458.32] manuals for
[2458.32 → 2459.16] software,
[2459.54 → 2459.94] which says,
[2460.08 → 2460.20] hey,
[2460.28 → 2460.76] please click on
[2460.76 → 2461.20] this button.
[2461.34 → 2461.46] So,
[2461.54 → 2462.40] then the person
[2462.40 → 2463.06] coming to you
[2463.06 → 2463.28] and say,
[2463.36 → 2463.46] hey,
[2464.00 → 2464.70] please create
[2464.70 → 2465.26] me an account
[2465.26 → 2466.24] in this one.
[2466.38 → 2466.86] You give this
[2466.86 → 2467.36] a manual,
[2467.76 → 2468.20] and then it
[2468.20 → 2468.50] does it
[2468.50 → 2469.06] completely
[2469.06 → 2469.60] automatically
[2469.60 → 2470.52] without any
[2470.52 → 2471.24] kinds of
[2471.24 → 2471.54] learning,
[2471.62 → 2472.60] because it's
[2472.60 → 2473.66] learned how to
[2473.66 → 2474.20] interact with
[2474.20 → 2475.62] you're operating
[2475.62 → 2476.04] system.
[2476.60 → 2477.12] This is one
[2477.12 → 2478.20] thing where we
[2478.20 → 2478.90] want to go
[2478.90 → 2479.72] to bring
[2479.72 → 2480.46] nowadays
[2480.46 → 2482.04] technology in
[2482.04 → 2483.12] to make it
[2483.12 → 2483.86] accessible for
[2483.86 → 2484.68] the users,
[2485.10 → 2485.60] and also
[2485.60 → 2487.26] that everyone,
[2487.42 → 2488.30] really everyone
[2488.30 → 2489.00] can use it,
[2489.06 → 2489.52] also your
[2489.52 → 2489.86] grandma.
[2491.78 → 2492.58] That's great.
[2492.70 → 2493.80] I am excited
[2493.80 → 2494.98] to see some
[2494.98 → 2495.74] of those things
[2495.74 → 2496.34] come down the
[2496.34 → 2496.58] line,
[2496.66 → 2497.10] and I think
[2497.10 → 2497.50] one of the
[2497.50 → 2497.88] things I've
[2497.88 → 2498.40] enjoyed about
[2498.40 → 2499.24] this conversation
[2499.24 → 2500.58] is that you
[2500.58 → 2501.60] brought a lot
[2501.60 → 2503.18] of the sort
[2503.18 → 2503.72] of positive
[2503.72 → 2504.54] side of
[2504.54 → 2505.08] automation
[2505.08 → 2505.94] that is
[2505.94 → 2506.46] really,
[2506.58 → 2507.74] really so
[2507.74 → 2508.58] helpful to
[2508.58 → 2509.50] technical
[2509.50 → 2509.96] people,
[2510.06 → 2510.44] but also
[2510.44 → 2511.10] other people
[2511.10 → 2511.76] that are
[2511.76 → 2512.24] doing these
[2512.24 → 2512.76] tasks that
[2512.76 → 2513.12] they really
[2513.12 → 2513.82] actually don't
[2513.82 → 2514.36] want to do
[2514.36 → 2515.06] or can't
[2515.06 → 2515.86] scale to
[2515.86 → 2516.28] a certain
[2516.28 → 2516.70] point,
[2516.80 → 2517.00] right?
[2517.42 → 2517.88] So I think
[2517.88 → 2518.32] it's really
[2518.32 → 2518.70] awesome,
[2518.98 → 2519.34] and yeah,
[2519.44 → 2520.00] I'm looking
[2520.00 → 2520.48] forward to
[2520.48 → 2521.24] seeing your
[2521.24 → 2522.24] future work
[2522.24 → 2522.98] with Ask UI,
[2523.30 → 2523.72] and thank you
[2523.72 → 2524.26] so much for
[2524.26 → 2524.76] joining the
[2524.76 → 2525.18] podcast.
[2525.32 → 2525.80] Really appreciate
[2525.80 → 2526.28] it, Dominic.
[2526.44 → 2526.92] Thank you for
[2526.92 → 2527.36] having me.
[2536.04 → 2537.00] Thank you for
[2537.00 → 2537.72] listening to
[2537.72 → 2538.56] Practical AI.
[2539.28 → 2539.90] Your next
[2539.90 → 2540.72] step is to
[2540.72 → 2541.64] subscribe now,
[2541.84 → 2542.56] if you haven't
[2542.56 → 2543.74] already, and
[2543.74 → 2544.06] if you're a
[2544.06 → 2544.62] long-time listener
[2544.62 → 2545.10] of the show,
[2545.46 → 2546.26] help us reach
[2546.26 → 2547.10] more people by
[2547.10 → 2548.22] sharing Practical AI
[2548.22 → 2548.82] with your friends
[2548.82 → 2549.36] and colleagues.
[2550.00 → 2550.72] Thanks once again
[2550.72 → 2551.60] to Vastly and
[2551.60 → 2552.66] Fly for partnering
[2552.66 → 2553.38] with us to bring
[2553.38 → 2554.00] you all Change
[2554.00 → 2554.74] Talk podcasts.
[2555.32 → 2555.72] Check out what
[2555.72 → 2556.60] they're up to at
[2556.60 → 2557.96] Fastly.com and
[2557.96 → 2559.10] Fly.io.
[2559.50 → 2560.06] And to our
[2560.06 → 2560.46] Beat Freaking
[2560.46 → 2560.92] Residence
[2560.92 → 2561.90] Break master Cylinder
[2561.90 → 2562.80] for continuously
[2562.80 → 2563.86] cranking out the
[2563.86 → 2564.56] best beats in the
[2564.56 → 2564.84] biz.
[2565.12 → 2565.68] That's all for
[2565.68 → 2566.02] now.
[2566.32 → 2566.76] We'll talk to
[2566.76 → 2567.10] you again next
[2567.10 → 2567.44] time.
[2567.72 → 2570.66] Fairly break master
[2570.66 → 2579.42] Podcasts
[2579.42 → 2579.76] ares
[2579.76 → 2580.16] FM
[2580.16 → 2580.42] Lam
[2580.42 → 2580.82] y
[2580.82 → 2581.84] photos
[2581.84 → 2582.00] ые
[2582.00 → 2582.90] 112
