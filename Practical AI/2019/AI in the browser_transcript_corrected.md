[0.00 → 2.58] Bandwidth for Changelog is provided by Vastly.
[2.96 → 4.86] Learn more at Fastly.com.
[5.08 → 8.16] We move fast and fix things here at Changelog because of Rollbar.
[8.30 → 9.98] Check them out at Rollbar.com.
[10.22 → 12.40] And we're hosted on Linde cloud servers.
[12.76 → 14.74] Head to linode.com slash Changelog.
[15.72 → 20.34] This episode is brought to you by DigitalOcean, the simplest cloud platform out there.
[20.46 → 25.10] And we're excited to share they now offer dedicated virtual droplets.
[25.10 → 29.04] And unlike standard droplets, which use shared virtual CPU threads,
[29.04 → 32.88] their two performance plans, general purpose and CPU optimized,
[33.40 → 36.08] they have dedicated virtual CPU threads.
[36.42 → 40.86] This translates to higher performance and increased consistency during CPU intensive processes.
[41.34 → 45.20] So if you have build boxes, CCD, video encoding, machine learning, ad serving,
[45.50 → 49.98] game servers, databases, batch processing, data mining, application servers,
[50.18 → 54.92] or active front end web servers that need to be full duty CPU all day every day,
[55.14 → 57.92] then check out DigitalOcean's dedicated virtual CPU droplets.
[57.92 → 61.26] Pricing is very competitive starting at 40 bucks a month.
[61.66 → 66.38] Learn more and get started for free with a $100 credit at do.co slash Changelog.
[66.64 → 69.02] Again, do.co slash Changelog.
[69.02 → 86.38] Welcome to Practical AI, a weekly podcast about making artificial intelligence practical,
[86.76 → 88.56] productive, and accessible to everyone.
[88.94 → 93.44] This is where conversations around AI, machine learning, and data science happen.
[93.92 → 98.20] Join the community and slack with us around various topics of the show at changelog.com slash community.
[98.20 → 99.38] Follow us on Twitter.
[99.48 → 100.96] We're at Practical AI FM.
[101.22 → 102.28] And now onto the show.
[107.06 → 109.48] Welcome to another episode of Practical AI,
[109.84 → 115.10] where we try to make artificial intelligence practical, productive, and accessible to everybody.
[115.66 → 116.90] My name is Chris Benson.
[117.04 → 119.22] I'm Principal AI Strategist at Lockheed Martin.
[119.46 → 124.64] And with me today is my co-host Daniel, who is a data scientist at SIL International.
[125.08 → 125.94] How's it going today, Daniel?
[125.94 → 128.38] It's going great, Chris.
[128.62 → 133.84] It's a beautiful fall day here in Indiana, and can't complain at all.
[134.48 → 134.80] Cool.
[135.12 → 142.52] As we are looking into the fall here, I'm getting excited, I guess, a couple of weeks after this episode comes out.
[142.52 → 148.16] I will be at NVIDIA GTC DC in Washington, DC.
[148.16 → 148.48] Cool.
[148.48 → 151.50] And I just wanted to say if any of our listeners are there,
[151.60 → 156.18] I'll be walking around a good bit of the time in a Practical AI t-shirt with a jacket.
[156.42 → 159.52] And if you happen to see me, I hope you'll come up and introduce yourself and say hi.
[159.84 → 160.62] Sounds good.
[160.72 → 166.46] I can't wait to hear what you learned there and hear about some of the content that's presented.
[166.46 → 167.82] I'm sure it'll be good.
[168.16 → 168.80] Sounds good.
[169.18 → 172.02] Well, we have a pretty good episode, I think, lined up today.
[172.40 → 175.74] We are going to be talking about artificial intelligence in the browser.
[176.36 → 177.02] Ooh, exciting.
[177.34 → 177.74] I know.
[177.88 → 179.18] I'm pretty excited about it.
[179.26 → 186.34] And I know both of us have done, over time, a fair amount of web development separate from the AI stuff.
[186.44 → 190.12] So this is the episode where we get to start combining them together, hopefully.
[190.12 → 198.26] With us today, we have Victor Debit, and he is a research engineer at Cloudera's Fast Forward Labs.
[198.66 → 199.56] Welcome to the show, Victor.
[200.50 → 201.66] Well, thanks a lot.
[202.12 → 203.36] It's perfect to be here.
[203.56 → 207.44] And I totally look forward to discussing machine learning in the browser.
[208.06 → 208.54] Fantastic.
[208.82 → 213.44] Well, I guess if you would start off by telling us a little bit about yourself,
[213.82 → 216.44] kind of how you got into this area,
[216.44 → 220.30] and kind of how you found yourself arriving at Cloudera Fast Forward Labs
[220.30 → 223.54] so that you could start this interesting line of work.
[224.10 → 224.36] Sure.
[224.70 → 225.22] Absolutely.
[225.64 → 232.16] And so I could talk about it in terms of my educational background
[232.16 → 235.64] and then ease into the whole professional track.
[236.16 → 236.40] Sure.
[236.52 → 237.06] Whatever works.
[237.90 → 238.14] Yeah.
[238.14 → 242.08] And so my background is a mix of computer science,
[242.48 → 243.92] that's software engineering,
[244.64 → 246.66] and a bit of human-computer interaction,
[247.50 → 251.24] and more recently, applied artificial intelligence.
[251.24 → 254.36] I have a master's degree from Carnegie Mellon University
[254.36 → 258.52] that's focused on software engineering and some management courses.
[259.70 → 265.56] And as part of that, I did this thesis on building a web-based public key crypto system
[265.56 → 267.68] that was introduced by my advisor.
[268.22 → 269.76] And that was a nice experience.
[270.04 → 275.06] It's just that there was a lot of time spent implementing cryptographic functions in Java.
[275.82 → 277.72] And after that, I felt, you know,
[277.98 → 282.96] it would be nice to move away from just the technical aspects of computer science
[282.96 → 286.48] and also look at some of the human aspects of computer science.
[287.20 → 290.38] And right after that, I made an interesting choice.
[290.54 → 293.84] I moved to Africa, Lagos, Nigeria, to be specific.
[293.84 → 299.68] And I started a company focused on making software focused on the African market.
[300.30 → 301.80] And I did that for about a year.
[302.14 → 306.12] And as part of that, I also taught at a university in Lagos, Nigeria
[306.12 → 310.26] through some project that was co-sponsored by MIT and Google.
[310.90 → 313.10] And as at that time, I figured out, you know,
[313.18 → 317.34] I'm really interested in human aspects of computer science.
[317.74 → 322.82] And I had all this experience building software tools within the framework of a startup
[322.82 → 324.80] and also teaching at a university.
[325.42 → 327.80] And then I decided to do a PhD.
[328.04 → 332.56] And so my PhD was in information systems I did at a city university of Hong Kong.
[333.42 → 338.82] And it was, the main focus was quantitative user behaviour studies.
[339.58 → 344.78] And at some point during my PhD, I had the opportunity to do an internship at IBM Research.
[344.78 → 346.86] And that's kind of where I got into AI.
[347.52 → 353.80] And so I interned with a group called the Cognitive Environmental Lab at IBM.
[355.38 → 360.98] And most of what that group did was trying to figure out good user experiences
[360.98 → 363.92] for applied machine learning.
[363.92 → 369.06] And so we spent time taking APIs built by other research groups.
[369.34 → 374.76] And so APIs around speech-to-text, text-to-speech, and computer vision.
[375.26 → 381.08] And our goal was to use these tools and build them into interactive,
[381.64 → 383.72] in some cases, room-scale experiences.
[383.72 → 388.96] And that's kind of where all of my interests with AI kind of started.
[389.16 → 390.60] I started out applying models.
[390.92 → 395.34] And after a while, I spent time implementing some of these models in TensorFlow and Keras.
[396.20 → 401.88] And essentially made the transition to start applying some of these custom-built models
[401.88 → 403.10] to new problem spaces.
[404.10 → 409.44] And so I was at IBM Research as a postdoc and then a research scientist.
[409.44 → 413.50] And earlier this year, I joined Cloudera Fast Forward Labs as a research scientist.
[414.16 → 417.48] And so it's a bit of a journey, but that's kind of how it all went down.
[418.40 → 425.20] Yeah, so when you're talking about user interaction or interfacing with AI,
[425.62 → 431.34] are you mostly talking about the sort of experiences like in Gmail,
[431.70 → 434.58] like autocomplete or voice-to-text and these sorts of things?
[434.58 → 443.68] Or even deeper in terms of helping a user kind of understand AI or use AI more effectively?
[443.86 → 448.98] How would you classify that sort of field of the interaction between humans and AI?
[449.82 → 450.06] Right.
[450.24 → 454.46] So my work kind of cut across the two areas that you mentioned.
[455.14 → 461.58] And so on specific line of work has to do with using AI to make the user interaction easier.
[461.58 → 467.92] And so that might be in terms of reducing the cognitive load associated with specific tasks.
[468.70 → 472.72] And good examples of that are the kind of thing you see in Gmail autocomplete,
[472.84 → 479.34] just start typing out an email and some LSTM model recommends a few completions.
[480.30 → 485.46] And so an interesting project that I worked on in a similar line is something called Data2Vs.
[485.46 → 493.28] And so with that project, we designed a neural network, a sequence-to-sequence model that could take user data.
[493.98 → 501.52] And based on user data, it will propose about 10 to 15 visualizations that made sense for that sort of data.
[501.98 → 508.58] And so the value here is that an analyst who perhaps has limited experience with authoring visualizations
[508.58 → 513.24] or writing code for visualizations could take a tool like that, upload your data,
[513.94 → 519.94] and the model will actually generate code for about 10 to 15 visualizations that they could either accept
[519.94 → 522.46] or they could modify to get their task done.
[523.08 → 524.68] So that's one line of work.
[525.18 → 529.60] And so another interesting line of work at this intersection of HCI and AI
[529.60 → 538.14] has to do with tools that make AI more accessible and more essentially easier to use for software engineers
[538.14 → 546.42] or other type of technical or non-technical users who strictly don't have a background in machine learning and AI.
[546.88 → 549.48] I know some people talk about democratizing AI.
[549.66 → 551.66] Is that sort of what they're meaning, I guess?
[552.24 → 552.54] Yes.
[552.68 → 558.36] Yeah, that's a good umbrella term to kind of describe that sort of work, democratizing AI.
[558.36 → 566.00] AI, I'm always not in a hurry to use that because that term can be reloaded and people have used it in all sorts of ways.
[566.44 → 571.06] But yeah, it's a good-related term, the whole idea of democratizing AI.
[571.62 → 575.84] And it has its advantages and its disadvantages.
[576.84 → 583.52] But the goal here is that if we make AI more accessible, then there are a lot of benefits that can come up.
[583.52 → 593.20] And so, for example, we want people with various backgrounds, various interests, various domain expertise actually coming and using AI tools.
[593.60 → 597.86] And that way, you know, we can kind of increase the diversity that kind of comes into this space.
[597.86 → 603.14] And one example of a project I worked on in that area was something called TJ Bot.
[603.24 → 604.62] That was why that was at IBM.
[605.16 → 607.96] It's actually a maker kit made out of cardboard.
[608.32 → 610.32] And so it's a Raspberry Pi on the inside.
[610.54 → 615.06] It's a cardboard piece that you could fold up into a humanoid-looking robot.
[615.06 → 631.58] And we had actually gone ahead and written a JavaScript library that made it very easy to take a bunch of IBM pre-trained machine learning models, integrate that into the bots, and essentially prototype things like you would see on Siri or any other like AI-enabled hardware device.
[632.26 → 640.60] And so that had a lot of success with schools, teachers, designers actually using it to actually start to use AI tools in different ways.
[640.60 → 643.16] So I've got a question for you.
[643.40 → 650.56] You know, you were talking a few minutes ago on UI about, you know, with Gmail and things, and you've talked about JavaScript.
[650.88 → 656.40] And I was kind of curious to even take a step back a little for a moment and ask, we're talking about the browser here.
[656.50 → 663.08] Why do you think people would want to run machine learning and AI models in the browser versus other environments?
[663.22 → 666.74] What is it that kind of drove that interest into the browser?
[667.52 → 667.88] Right.
[667.88 → 671.98] So machine learning in the browser, it's a fairly new area.
[672.48 → 679.58] And I guess most of the time when I talk about it or discuss it with people, there's always a form of healthy skepticism.
[680.04 → 682.10] And I think it's for good reason.
[682.64 → 687.76] And so if I'm going to take a step back just to discuss the two interesting aspects of machine learning.
[687.76 → 688.76] So there's training.
[689.56 → 697.38] So this is the part where you create a model, which is essentially a function that learns mappings between your input data and some kind of target.
[697.88 → 700.98] And essentially you get all your data collected.
[700.98 → 702.98] You have it cleaned up.
[702.98 → 709.18] And you go through the process of kind of learning this function that solves a specific task.
[710.08 → 711.68] And so that's the training phase.
[711.80 → 719.88] And then the second part of machine learning is inference where at some test time you get this model that's trained, and you get it to actually perform the task.
[719.88 → 725.92] And typically we've used languages like Python, Java, C, R, Scalar, Julia.
[726.98 → 737.16] And these are typically back-end languages, and they have a lot of nice functionalities like hardware, direct hardware access, multi-threading.
[737.16 → 742.56] And it makes them work really well for intensive computations like machine learning.
[743.52 → 746.98] However, typically most of all this has been done on the back-end.
[747.56 → 755.02] There's been a clear separation between what you can do in the front-end in an environment like the browser because the browser has a bunch of limitations.
[755.38 → 757.32] And so it's single-threaded.
[757.32 → 765.80] And it's a sandbox environment with very limited access to system-wide features.
[766.40 → 771.88] However, it turns out that there are a few benefits that kind of make this proposition interesting.
[772.22 → 777.08] And some of my favourite reasons have to do with three specific benefits.
[777.62 → 779.10] And so the first would be privacy.
[779.10 → 784.82] And perhaps this is the most compelling and interesting benefit that I really care about.
[785.72 → 796.28] And so if you could take a model, and you could deploy that in the browser, then you could create an environment where the user data actually doesn't get down to any back-end server.
[796.72 → 801.36] And I could give some examples of that somewhere down the line as we continue the conversation.
[801.36 → 808.36] The second interesting benefit why machine learning might be interested in the browser has to do with the ease of distribution.
[809.48 → 814.72] And so a few years ago, I had a couple of friends who really wanted to get into machine learning.
[815.16 → 819.56] But they did give up because they spent a couple of days just trying to install TensorFlow.
[820.14 → 826.82] And so while over the last two years, the user experience has become a lot better, there are still a lot of challenges,
[826.82 → 835.30] especially if you want to get a machine learning model or an application that uses machine learning deployed in an end-user system.
[835.94 → 843.54] However, if you go ahead and do that in the browser, this is a much straightforward and much, much easier developer and end-user experience.
[844.44 → 849.46] And then finally, the last interesting feature has to do with interactivity and latency.
[849.46 → 858.46] And so off the bat, the browser is the web is designed to be interactive, and it's really valuable for crafting rich interactive experiences.
[859.76 → 869.76] And so if there are situations where you have a model, and you want to easily tailor that around user data, make changes and personalize that for a user,
[869.96 → 874.08] then the browser is a really excellent environment to interactively do all of that.
[874.08 → 879.54] And so these are three interesting reasons why I think it makes sense to actually explore machine learning in the browser.
[880.46 → 883.54] So, yeah, that's a great explanation.
[883.88 → 888.78] I'm wondering if kind of along with that explanation, since we're always trying to be practical here,
[888.88 → 895.16] and like you said, there are probably a lot of listeners who are familiar with Python or Java or whatever it is,
[895.48 → 897.82] this sort of backend languages.
[898.30 → 902.82] Could you just kind of describe the JavaScript ecosystem a little bit?
[902.82 → 909.30] So there's like JavaScript, but then there's probably things like Node.js and other things that people have heard of.
[909.74 → 919.52] Could you kind of describe, I guess, in general what those things are, and how like machine learning is kind of touching each of those?
[919.52 → 924.64] Or maybe it's specifically touching one thing like vanilla JavaScript or whatever it is?
[925.20 → 926.24] That's a great question.
[926.24 → 936.28] And so on way to think of what you could actually do in terms of machine learning in JavaScript is to think in terms of the tools that are available today.
[937.14 → 940.56] And right now, most of that is TensorFlow.js.
[941.06 → 943.74] For listeners who are not familiar with TensorFlow.js,
[944.02 → 953.24] it's a JavaScript library designed to enable machine learning in the browser and any other environment that's built with JavaScript like Node.js.
[953.24 → 957.04] And so most of my conversations around, you know,
[957.32 → 961.22] when I talk about essentially implementing machine learning in JavaScript,
[961.96 → 962.82] most of the time,
[963.00 → 968.42] I'm actually referring to implementing machine learning using the TensorFlow.js library.
[969.28 → 973.54] And so in regard to the environment and platforms that are supported,
[973.96 → 977.56] TensorFlow.js allows you to build, train,
[977.56 → 984.98] and perform inference both in the browser environment as part of a front-end web application.
[986.20 → 987.82] And it also lets you build, train,
[987.82 → 992.32] and perform inference as part of a back-end Node.js application.
[993.20 → 994.30] And so the library,
[995.00 → 1000.50] one way to think of it is to think of it as having a few different installation versions.
[1000.50 → 1004.90] And so there's a version that could be bundled into a web application.
[1005.32 → 1008.70] It could be a vanilla JavaScript application where you could just,
[1009.46 → 1010.22] in your web page,
[1010.28 → 1015.14] you could include a minified version of the TensorFlow.js library.
[1015.66 → 1020.68] Or you could install it using build tools as part of a React or Vue.js application.
[1020.98 → 1022.86] And so that's for the front-end browser.
[1023.42 → 1023.98] Similarly,
[1024.10 → 1024.80] on the back-end,
[1024.92 → 1027.60] you could NPM install TensorFlow.js.
[1027.60 → 1032.12] And essentially for your back-end applications built in Node.js,
[1032.26 → 1034.22] you could integrate TensorFlow models.
[1034.92 → 1036.86] And you could also integrate,
[1037.22 → 1040.78] install the GPU version of that same back-end library.
[1041.04 → 1043.24] So it would be NPM install TensorFlow.js.
[1043.80 → 1048.64] And one other thing that I guess people will be interested in learning about
[1048.64 → 1052.74] would be around the performance of TensorFlow.js
[1052.74 → 1054.76] and both the back-end and the front-end.
[1054.76 → 1056.60] And so in the browser,
[1056.92 → 1062.28] it turns out that TensorFlow offers a vanilla CPU back-end
[1062.28 → 1065.40] and also something called the WebGL back-end.
[1066.04 → 1069.84] And so most of us might be familiar with the WebGL standard.
[1070.08 → 1072.50] It's used for accelerated graphics compute.
[1073.22 → 1074.62] And the value here is that
[1074.62 → 1077.62] if you do have a GPU available on the machine,
[1077.86 → 1079.56] through the WebGL standard,
[1079.56 → 1082.16] you can actually accelerate your computations
[1082.16 → 1084.58] right there in the browser.
[1085.12 → 1087.88] And so underneath TensorFlow.js in the browser,
[1088.16 → 1090.44] we'll take advantage of optimizations
[1090.44 → 1093.52] already implemented in WebGL.
[1093.88 → 1097.72] And that's how it's able to accelerate computations in the browser.
[1097.72 → 1112.52] Hello there.
[1112.66 → 1113.76] This is Jared Santo,
[1114.02 → 1115.80] Managing Editor here at Changelog.
[1116.02 → 1117.56] The fact that you're listening to this
[1117.56 → 1119.30] means you are actively investing
[1119.30 → 1120.90] in your future in this industry.
[1121.50 → 1122.44] Things move fast,
[1122.64 → 1123.72] and keeping up is hard work.
[1124.08 → 1125.70] Help us help you stay relevant
[1125.70 → 1127.60] by subscribing to Changelog Weekly.
[1128.00 → 1130.68] We track, log, and contextualize
[1130.68 → 1132.98] what's happening in software throughout the week
[1132.98 → 1136.10] and deliver it directly to your inbox on Sunday mornings.
[1136.82 → 1138.76] Head to changelog.com slash weekly
[1138.76 → 1139.88] to browse the archives,
[1140.22 → 1140.56] subscribe,
[1141.02 → 1142.52] and push the easy button
[1142.52 → 1143.98] on your continuing education.
[1144.76 → 1145.82] That's all from me.
[1146.02 → 1146.56] Once again,
[1146.82 → 1148.94] that's changelog.com slash weekly.
[1155.70 → 1163.16] So, Victor,
[1163.28 → 1164.32] I was kind of curious.
[1164.88 → 1168.58] I know that you are involved with TensorFlow.js
[1168.58 → 1171.22] and have been using that.
[1171.52 → 1174.66] And I was really wanting to learn about what it is
[1174.66 → 1176.80] and kind of how it fits in
[1176.80 → 1179.10] to the world of regular TensorFlow.
[1179.44 → 1180.22] Or does it?
[1180.32 → 1180.44] You know,
[1180.48 → 1181.88] what's the relationship between the two?
[1181.88 → 1186.46] And so TensorFlow.js is one of the libraries
[1186.46 → 1189.10] or frameworks in the broader TensorFlow ecosystem.
[1190.28 → 1192.54] And the primary benefit it offers
[1192.54 → 1197.08] is allowing a developer design, build,
[1198.10 → 1200.04] train, and perform inference
[1200.04 → 1203.12] for machine learning models using JavaScript,
[1203.86 → 1205.62] either in the browser on the front end
[1205.62 → 1208.46] or on the back end in Node.js.
[1208.46 → 1211.30] And so in regard to how it plays
[1211.30 → 1213.86] with the rest of the TensorFlow ecosystem,
[1214.08 → 1215.00] I like to think of it,
[1215.32 → 1217.34] the TensorFlow.js workflows in three,
[1217.64 → 1219.48] using three main approaches.
[1220.58 → 1222.88] And so the first is what I'll describe
[1222.88 → 1224.10] as the online workflow.
[1224.44 → 1226.20] And so with this workflow,
[1226.34 → 1228.86] you can structure out your machine learning models.
[1229.26 → 1229.52] Essentially,
[1229.62 → 1231.62] if you're building a convolutional neural network,
[1231.74 → 1233.50] you will specify input layers,
[1234.00 → 1235.30] the convolutional layers,
[1235.68 → 1236.70] and your pulling layers,
[1236.70 → 1238.86] all of that using TensorFlow.js,
[1239.06 → 1241.74] you could train your model directly in the browser,
[1242.08 → 1242.66] use the data,
[1243.10 → 1244.80] and then perform inference.
[1245.52 → 1246.02] And so clearly,
[1246.38 → 1248.58] there are caveats around this.
[1248.76 → 1251.24] You probably want to do this with small models
[1251.24 → 1254.80] or models that didn't have a lot of data.
[1255.74 → 1257.02] And so that's the first approach,
[1257.10 → 1258.98] something I describe as the online approach.
[1259.32 → 1259.96] And in this case,
[1260.10 → 1260.56] the data,
[1260.78 → 1261.94] there's no actual data
[1261.94 → 1264.10] that's leaving the client device.
[1264.14 → 1264.58] Is that right?
[1265.18 → 1265.44] Yes,
[1265.44 → 1266.16] that is correct.
[1267.04 → 1269.04] And does that kind of fit into that,
[1269.06 → 1269.32] like,
[1269.44 → 1271.58] privacy advantage
[1271.58 → 1272.74] that you mentioned before?
[1273.62 → 1273.88] Yes,
[1274.00 → 1274.18] yes,
[1274.26 → 1274.70] absolutely.
[1275.50 → 1277.20] And in this case,
[1277.32 → 1278.78] imagine you had user data
[1278.78 → 1279.90] already available
[1279.90 → 1281.46] on their machine
[1281.46 → 1283.42] and your application,
[1283.60 → 1283.96] the browser,
[1284.08 → 1285.86] could get access to that data,
[1286.26 → 1286.84] train the model,
[1287.02 → 1288.26] and then perform inference
[1288.26 → 1289.82] without any data being sent
[1289.82 → 1290.86] to any backend server.
[1290.86 → 1292.32] So that kind of fits in
[1292.32 → 1294.04] with the privacy benefit.
[1294.54 → 1295.14] So the second,
[1295.46 → 1297.40] potentially more common flow
[1297.40 → 1299.02] is something called the offline flow,
[1299.36 → 1301.08] where you could train your model
[1301.08 → 1303.38] using a large amount of data
[1303.38 → 1305.18] and large GPU clusters
[1305.18 → 1306.98] or whatever hardware you have available.
[1307.64 → 1308.64] And for this process,
[1308.70 → 1309.92] you could use TensorFlow,
[1310.12 → 1310.46] Python,
[1310.66 → 1312.04] or Keras models.
[1312.04 → 1312.64] models.
[1313.52 → 1315.90] And so just how you would train your models
[1315.90 → 1317.84] traditionally in TensorFlow,
[1317.84 → 1318.28] Python,
[1318.40 → 1318.96] you could go ahead
[1318.96 → 1319.92] and build your models,
[1320.06 → 1320.56] train them,
[1321.14 → 1323.00] your GPUs or TPU clusters.
[1323.56 → 1325.52] And then you could export that model.
[1325.68 → 1327.10] That's the output of that process.
[1327.52 → 1328.56] And then you could use
[1328.56 → 1330.06] the TensorFlow.js converter
[1330.06 → 1331.38] to then convert that
[1331.38 → 1332.10] into a format
[1332.10 → 1332.94] that can be loaded
[1332.94 → 1333.60] in JavaScript
[1333.60 → 1335.26] or in a JavaScript application
[1335.26 → 1337.88] and then perform inference on that.
[1339.00 → 1339.52] So that's
[1339.52 → 1341.60] what I would refer to
[1341.60 → 1342.40] as the second
[1342.40 → 1343.58] or the offline flow.
[1344.30 → 1345.08] And then finally,
[1345.20 → 1346.00] the hybrid flow
[1346.00 → 1347.80] would be super similar
[1347.80 → 1348.92] to the offline flow
[1348.92 → 1350.48] where you train offline,
[1351.08 → 1352.10] you convert your model
[1352.10 → 1353.20] and you import it.
[1353.66 → 1354.80] And then in the browser,
[1355.00 → 1355.86] you could go ahead
[1355.86 → 1358.74] and fine-tune that model
[1358.74 → 1360.68] using user data
[1360.68 → 1361.96] right in the browser.
[1362.74 → 1363.58] And so these are three
[1363.58 → 1364.98] potential flows
[1364.98 → 1365.70] that a developer
[1365.70 → 1367.20] could take advantage of
[1367.20 → 1368.48] when using TensorFlow.js.
[1369.50 → 1370.28] And I guess
[1370.28 → 1371.30] the interesting thing
[1371.30 → 1372.54] to note here
[1372.54 → 1372.92] is that
[1372.92 → 1374.00] for models
[1374.00 → 1374.86] that you've trained
[1374.86 → 1376.60] using the traditional
[1376.60 → 1377.94] TensorFlow. Python,
[1378.84 → 1379.40] TensorFlow.js
[1379.40 → 1381.14] offers a converter software,
[1381.30 → 1381.62] a tool
[1381.62 → 1382.64] that lets you convert
[1382.64 → 1384.12] those pre-trained models
[1384.12 → 1385.38] into a format
[1385.38 → 1386.46] called the web format
[1386.46 → 1387.30] that can be loaded
[1387.30 → 1389.02] in a JavaScript application.
[1389.46 → 1389.96] And so there's
[1389.96 → 1391.28] that opportunity
[1391.28 → 1392.50] to integrate
[1392.50 → 1393.70] whatever work
[1393.70 → 1394.64] you've been doing
[1394.64 → 1396.86] with TensorFlow. Python
[1396.86 → 1397.76] and then bring that
[1397.76 → 1399.16] into the JavaScript
[1399.16 → 1400.90] of the web application space.
[1401.90 → 1403.50] So when a user,
[1404.02 → 1405.64] like if I'm a developer
[1405.64 → 1406.96] and I'm thinking about
[1406.96 → 1408.04] maybe like privacy
[1408.04 → 1409.04] is important to me
[1409.04 → 1409.52] or maybe
[1409.52 → 1411.46] the latency issues
[1411.46 → 1412.16] are important to me
[1412.16 → 1413.14] and I'm thinking about
[1413.14 → 1414.84] which of these scenarios
[1414.84 → 1415.86] I should pursue,
[1415.98 → 1416.62] whether I want to be
[1416.62 → 1417.48] fully online
[1417.48 → 1418.34] or offline
[1418.34 → 1419.60] or the hybrid situation
[1419.60 → 1420.68] like you're talking about,
[1420.68 → 1422.60] I guess part of that
[1422.60 → 1423.58] could be driven
[1423.58 → 1425.00] by the privacy concerns
[1425.00 → 1426.46] but in terms of performance
[1426.46 → 1428.64] like how much data
[1428.64 → 1430.06] or how big of a model
[1430.06 → 1431.28] can you train
[1431.28 → 1433.80] like in the online scenario
[1433.80 → 1435.84] versus like offline
[1435.84 → 1436.80] and also like
[1436.80 → 1437.74] are some models
[1437.74 → 1439.38] maybe the latest ones
[1439.38 → 1440.10] that are like,
[1440.42 → 1440.68] you know,
[1440.76 → 1441.68] however many billions
[1441.68 → 1442.44] of parameters,
[1442.60 → 1443.82] maybe you can't actually
[1443.82 → 1445.80], or can you optimize those
[1445.80 → 1446.80] and fit them
[1446.80 → 1448.60] into the browser to run?
[1448.60 → 1449.94] What are the sort of constraints
[1449.94 → 1451.14] with those things?
[1452.08 → 1452.28] Right.
[1452.48 → 1454.06] So experience-wise,
[1454.24 → 1455.36] I think most of the time
[1455.36 → 1457.98] people would only train models,
[1458.50 → 1459.72] low-parameter models,
[1459.92 → 1461.18] small models in the browser
[1461.18 → 1462.96] and I guess the reason
[1462.96 → 1463.74] is pretty clear.
[1463.86 → 1464.80] The browser is not
[1464.80 → 1465.90] the multithreaded,
[1466.02 → 1467.30] high-performance environment
[1467.30 → 1470.16] and it's perhaps not designed
[1470.16 → 1471.76] to train large models
[1471.76 → 1473.74] using large datasets,
[1474.28 → 1474.62] images,
[1474.94 → 1475.76] thousands of images
[1475.76 → 1476.66] right in the browser.
[1476.66 → 1478.76] And so what I've typically
[1478.76 → 1479.64] seen people do
[1479.64 → 1480.50] if they were going to
[1480.50 → 1481.70] train models from scratch
[1481.70 → 1483.02] and so they would use
[1483.02 → 1484.46] train smaller models,
[1484.82 → 1486.32] perhaps using tabular data
[1486.32 → 1488.86] with maybe a couple of thousand records
[1488.86 → 1491.56] and not much more than that.
[1491.82 → 1494.00] With respect to actually deploying
[1494.00 → 1495.50] high-performance models
[1495.50 → 1496.10] in the browser,
[1496.44 → 1498.82] I guess the good best practice
[1498.82 → 1500.38] would be to think
[1500.38 → 1501.66] of model optimization
[1501.66 → 1504.68] during your model construction phase.
[1504.68 → 1506.66] And there are a few ways
[1506.66 → 1507.56] to go about that.
[1508.50 → 1509.70] And the idea is
[1509.70 → 1511.80] train your model offline,
[1512.70 → 1514.56] apply a bunch of optimizations
[1514.56 → 1516.16] and this could be
[1516.16 → 1517.42] model quantization,
[1517.72 → 1518.98] this could be model compression
[1518.98 → 1520.42] and the goal would be
[1520.42 → 1521.58] to export a model
[1521.58 → 1522.64] that's small enough
[1522.64 → 1523.80] that it doesn't hinder
[1523.80 → 1526.60] the web or interactive experience
[1526.60 → 1528.78] and then you would
[1528.78 → 1530.78] typically then import that
[1530.78 → 1532.36] but mainly just for inference
[1532.36 → 1533.50] in the browser.
[1533.50 → 1535.94] So I guess, you know,
[1536.16 → 1537.86] how you've kind of covered
[1537.86 → 1538.92] these different ways
[1538.92 → 1539.60] of using it
[1539.60 → 1540.80] and how they integrate,
[1541.30 → 1542.34] do you have any insight
[1542.34 → 1545.08] into maybe with, you know,
[1545.14 → 1546.24] Fast Forward Labs clients
[1546.24 → 1548.08] or anyone else you've come across
[1548.08 → 1549.10] within the industry
[1549.10 → 1549.84] about how people
[1549.84 → 1551.80] are typically using
[1551.80 → 1552.82] TensorFlow.js
[1552.82 → 1554.26] and how they're fitting it in
[1554.26 → 1554.98] in real life
[1554.98 → 1556.18] kind of aside from
[1556.18 → 1558.66] the options that you've laid out,
[1558.72 → 1559.20] do you know what people
[1559.20 → 1560.26] are actually untaking on?
[1560.26 → 1561.74] Right.
[1561.90 → 1562.82] So there are a few
[1562.82 → 1564.22] interesting use cases
[1564.22 → 1565.98] I've seen across the community
[1565.98 → 1567.88] and have also been highlighted
[1567.88 → 1570.88] by the TensorFlow.js community
[1570.88 → 1573.32] and I think there's a really
[1573.32 → 1574.38] interesting experience
[1574.38 → 1576.22] or application by Airbnb
[1576.22 → 1578.28] whereas part of their
[1578.28 → 1579.70] user onboarding process,
[1580.08 → 1581.62] the user has to upload
[1581.62 → 1582.54] a photograph,
[1583.08 → 1584.62] an image of themselves
[1584.62 → 1586.88] and writing as part
[1586.88 → 1588.40] of their onboarding experience,
[1588.54 → 1590.28] they have a TensorFlow.js model
[1590.28 → 1591.04] in the browser
[1591.04 → 1592.50] that could look through
[1592.50 → 1593.30] whatever image
[1593.30 → 1594.10] has been uploaded
[1594.10 → 1595.30] and could tell the user
[1595.30 → 1598.16] if this particular image
[1598.16 → 1599.64] contains sensitive content
[1599.64 → 1600.04] or not.
[1600.66 → 1602.08] And so in some cases,
[1602.22 → 1603.50] users might upload
[1603.50 → 1604.56] their driver's license
[1604.56 → 1606.54] or other type of images
[1606.54 → 1607.98] that has potentially
[1607.98 → 1608.98] sensitive content.
[1609.56 → 1610.64] And the value proposition
[1610.64 → 1612.36] here would be to
[1612.36 → 1614.10] tell the user,
[1614.10 → 1614.50] you know,
[1615.04 → 1616.22] I'm able to offer you
[1616.22 → 1617.10] this service
[1617.10 → 1618.28] telling you that
[1618.28 → 1620.14] you have potentially
[1620.14 → 1621.42] privacy-sensitive
[1621.42 → 1622.66] information here.
[1623.20 → 1623.76] However,
[1624.70 → 1625.76] this data does not
[1625.76 → 1626.60] get to my server
[1626.60 → 1627.74] and I never see it.
[1628.60 → 1628.74] Yeah.
[1628.80 → 1629.68] So you don't even
[1629.68 → 1630.60] have to worry about
[1630.60 → 1631.36] storing that.
[1631.48 → 1632.64] You're just providing
[1632.64 → 1633.68] a service to the user
[1633.68 → 1634.34] on their side.
[1634.92 → 1635.16] Yes.
[1635.16 → 1636.34] So I think this is
[1636.34 → 1636.88] a perfect
[1636.88 → 1638.18] and strong notion
[1638.18 → 1638.88] of privacy.
[1639.38 → 1640.40] The alternative
[1640.40 → 1641.34] would be that,
[1641.42 → 1641.76] you know,
[1641.80 → 1642.92] companies would typically
[1642.92 → 1643.48] say,
[1644.02 → 1644.94] oh, we have your data.
[1645.42 → 1646.58] We don't store it.
[1646.64 → 1647.26] We see it.
[1647.66 → 1649.02] But even if we store it,
[1649.10 → 1650.38] we will only use it
[1650.38 → 1651.08] appropriately.
[1651.76 → 1652.34] And so I think
[1652.34 → 1653.44] it's a stronger notion
[1653.44 → 1653.94] to say,
[1654.06 → 1655.18] we're able to
[1655.18 → 1656.54] offer you a service,
[1657.04 → 1658.20] but we never
[1658.20 → 1659.12] actually see your data
[1659.12 → 1659.82] because it never
[1659.82 → 1660.68] gets to a service.
[1661.30 → 1661.96] So I think that's
[1661.96 → 1662.68] a fascinating
[1662.68 → 1663.72] application.
[1664.44 → 1665.66] And so for developers
[1665.66 → 1666.74] who have similar
[1666.74 → 1667.46] privacy,
[1668.06 → 1669.28] similar scenarios
[1669.28 → 1670.02] where, you know,
[1670.18 → 1671.12] having a strong notion
[1671.12 → 1672.38] of privacy is valuable,
[1672.54 → 1674.50] I think TensorFlow.js
[1674.50 → 1675.36] is a really strong
[1675.36 → 1675.84] candidate.
[1676.46 → 1677.50] Another interesting area,
[1677.68 → 1678.50] which is part of
[1678.50 → 1679.60] some work I have done,
[1679.86 → 1680.80] has been around
[1680.80 → 1682.54] attempting to
[1682.54 → 1684.26] design interactive
[1684.26 → 1685.36] experiences in the
[1685.36 → 1686.16] browser using the
[1686.16 → 1686.48] camera.
[1687.36 → 1688.12] And so I have this
[1688.12 → 1689.00] library called
[1689.00 → 1690.28] HandTrack.js.
[1690.68 → 1691.12] Essentially,
[1691.42 → 1693.26] it's an object
[1693.26 → 1694.10] detection model
[1694.10 → 1695.14] that's able to run
[1695.14 → 1695.78] in real time.
[1696.64 → 1697.60] And what it does
[1697.60 → 1698.28] is that it's able
[1698.28 → 1699.62] to track the location
[1699.62 → 1701.40] of human hands
[1701.40 → 1702.38] in any video frame
[1702.38 → 1703.18] or image frame
[1703.18 → 1704.06] right at the end
[1704.06 → 1704.46] of the browser.
[1705.90 → 1706.58] And so the idea
[1706.58 → 1708.22] is you could use
[1708.22 → 1709.80] interactions like that
[1709.80 → 1711.04] to create more
[1711.04 → 1712.14] engaging experiences
[1712.14 → 1714.12] like using your hand
[1714.12 → 1715.12] to control the game
[1715.12 → 1717.82] or for artistic
[1717.82 → 1718.50] installations,
[1718.80 → 1719.14] you could,
[1719.28 → 1720.32] rather than using
[1720.32 → 1720.82] the mouse
[1720.82 → 1722.00] to interact
[1722.00 → 1722.94] with that art
[1722.94 → 1723.32] installation,
[1723.64 → 1724.04] you could just
[1724.04 → 1725.36] have users
[1725.36 → 1725.98] done in front
[1725.98 → 1727.20] of the computer
[1727.20 → 1728.08] and based
[1728.08 → 1729.12] on the feed
[1729.12 → 1729.50] that's coming
[1729.50 → 1730.10] from the camera,
[1730.24 → 1730.82] they could perform
[1730.82 → 1731.30] things like
[1731.30 → 1731.84] selections,
[1732.12 → 1732.76] touch, grab,
[1732.82 → 1733.46] and all of that.
[1734.28 → 1734.90] And the good thing
[1734.90 → 1735.76] is before now,
[1736.14 → 1736.96] to perform this
[1736.96 → 1737.76] sort of engaging
[1737.76 → 1738.42] interactions,
[1738.74 → 1739.68] you had to have
[1739.68 → 1740.26] some kind of
[1740.26 → 1741.10] hardware sensor
[1741.10 → 1743.80] or some really
[1743.80 → 1744.68] complex backend
[1744.68 → 1745.10] server.
[1745.10 → 1745.84] but now with
[1745.84 → 1746.60] TensorFlow.js
[1746.60 → 1748.54] and a well-optimized
[1748.54 → 1748.80] model,
[1748.98 → 1749.52] you could actually
[1749.52 → 1750.18] do all of that
[1750.18 → 1750.72] in the browser
[1750.72 → 1751.78] with no additional
[1751.78 → 1753.32] hardware and just
[1753.32 → 1754.20] access to the user
[1754.20 → 1754.62] camera.
[1755.66 → 1756.16] And so these are
[1756.16 → 1757.12] two interesting
[1757.12 → 1758.30] examples I think
[1758.30 → 1759.32] are engaging.
[1759.64 → 1760.32] I think it's the
[1760.32 → 1761.00] space that's still
[1761.00 → 1761.36] growing.
[1761.96 → 1763.02] Yeah, so I'm
[1763.02 → 1764.04] curious, so I
[1764.04 → 1764.92] definitely see the
[1764.92 → 1765.70] advantage on the
[1765.70 → 1766.66] privacy side, I see
[1766.66 → 1767.50] the advantage on the
[1767.50 → 1768.38] sort of interaction
[1768.38 → 1769.24] side like you're
[1769.24 → 1770.16] talking about with
[1770.16 → 1771.04] the hand track
[1771.04 → 1772.38] JS, which I
[1772.38 → 1772.88] definitely want to
[1772.88 → 1773.72] get into here in a
[1773.72 → 1774.00] second.
[1774.28 → 1774.62] What I was
[1774.62 → 1775.58] wondering, I
[1775.58 → 1776.96] anticipate that
[1776.96 → 1777.72] maybe some
[1777.72 → 1779.24] companies that
[1779.24 → 1780.72] like their AI
[1780.72 → 1781.44] models or their
[1781.44 → 1782.32] machine learning
[1782.32 → 1783.22] models, maybe it's
[1783.22 → 1784.02] part of their sort
[1784.02 → 1784.52] of bread and
[1784.52 → 1785.28] butter and how
[1785.28 → 1786.52] they make money
[1786.52 → 1787.36] or it's their
[1787.36 → 1788.16] market advantage
[1788.16 → 1788.70] or something.
[1789.14 → 1790.02] Would it be a
[1790.02 → 1790.88] problem for them
[1790.88 → 1792.10] to kind of push
[1792.10 → 1793.38] that model out
[1793.38 → 1794.44] to the browser
[1794.44 → 1795.48] in the sense of
[1795.48 → 1796.88] like, can users
[1796.88 → 1797.82] that are using
[1797.82 → 1798.42] one of these
[1798.42 → 1799.52] applications just
[1799.52 → 1800.56] like open up a
[1800.56 → 1801.68] JavaScript console
[1801.68 → 1802.98] and like grab
[1802.98 → 1803.70] the model and
[1803.70 → 1804.90] use it themselves?
[1805.20 → 1805.84] What sort of
[1805.84 → 1806.90] like, are there
[1806.90 → 1807.80] certain concerns
[1807.80 → 1808.70] development-wise
[1808.70 → 1809.48] around like
[1809.48 → 1811.06] keeping your
[1811.06 → 1812.20] model in-house
[1812.20 → 1813.32] or things that
[1813.32 → 1813.90] you should be
[1813.90 → 1814.70] aware of as you
[1814.70 → 1815.68] actually port this
[1815.68 → 1816.68] model out to
[1816.68 → 1817.24] the browser?
[1818.34 → 1818.64] Right.
[1818.84 → 1819.26] Yeah, you
[1819.26 → 1820.26] definitely raise a
[1820.26 → 1820.70] concern.
[1821.06 → 1821.64] And so at the
[1821.64 → 1822.90] moment, your
[1822.90 → 1824.76] model is just
[1824.76 → 1825.34] like any other
[1825.34 → 1826.78] web assets on
[1826.78 → 1827.48] your web
[1827.48 → 1828.04] application.
[1828.04 → 1828.18] application.
[1828.98 → 1830.02] And so just
[1830.02 → 1830.66] the same way
[1830.66 → 1832.18] the developer
[1832.18 → 1833.02] is responsible
[1833.02 → 1834.06] for securing
[1834.06 → 1835.18] elements like
[1835.18 → 1836.60] images and
[1836.60 → 1838.16] videos and
[1838.16 → 1838.64] every other
[1838.64 → 1839.72] content that's
[1839.72 → 1840.40] integrated into
[1840.40 → 1841.12] the web page,
[1841.62 → 1842.10] they would need
[1842.10 → 1843.20] to think carefully
[1843.20 → 1843.94] around the
[1843.94 → 1844.72] security of the
[1844.72 → 1845.06] models.
[1845.72 → 1846.40] And so you're
[1846.40 → 1847.18] absolutely right.
[1847.38 → 1848.34] It will be
[1848.34 → 1849.86] possible without
[1849.86 → 1851.38] any specific
[1851.38 → 1852.38] security
[1852.38 → 1853.04] implementations.
[1853.04 → 1854.82] I mean, beyond
[1854.82 → 1855.96] putting the
[1855.96 → 1856.72] model behind
[1856.72 → 1857.54] some kind of
[1857.54 → 1858.66] login or
[1858.66 → 1859.60] restricting
[1859.60 → 1860.66] access to
[1860.66 → 1861.94] based on IP
[1861.94 → 1862.66] address or any
[1862.66 → 1863.48] other security
[1863.48 → 1865.06] practice, if
[1865.06 → 1865.52] those are not
[1865.52 → 1866.46] implemented, it
[1866.46 → 1867.44] will be possible
[1867.44 → 1868.52] for the model
[1868.52 → 1869.22] files to be
[1869.22 → 1869.98] downloaded and
[1869.98 → 1870.76] perhaps used
[1870.76 → 1871.14] offline.
[1871.32 → 1872.70] And so I guess
[1872.70 → 1873.88] this is a
[1873.88 → 1874.78] concern that
[1874.78 → 1876.40] the users
[1876.40 → 1877.68] should, developers
[1877.68 → 1878.50] should think about
[1878.50 → 1879.14] while they
[1879.14 → 1880.50] consider putting
[1880.50 → 1881.22] models in the
[1881.22 → 1881.48] browser.
[1883.04 → 1893.90] Hey, guess
[1893.90 → 1894.18] what?
[1894.30 → 1894.88] Brain Science
[1894.88 → 1896.08] is officially
[1896.08 → 1896.62] launched.
[1896.90 → 1897.40] Episode number
[1897.40 → 1897.96] one is on the
[1897.96 → 1898.60] feed right now,
[1898.74 → 1899.48] so head to
[1899.48 → 1900.24] changelaw.com
[1900.24 → 1901.20] slash brain science
[1901.20 → 1901.98] to listen, to
[1901.98 → 1903.20] subscribe, and to
[1903.20 → 1904.08] join us on this
[1904.08 → 1905.00] journey of exploring
[1905.00 → 1905.94] the human mind.
[1906.16 → 1906.72] Once again,
[1906.86 → 1907.76] changelaw.com
[1907.76 → 1908.80] slash brain science
[1908.80 → 1909.60] or search for
[1909.60 → 1910.68] brain science in your
[1910.68 → 1911.70] favourite podcast app.
[1913.04 → 1933.20] So I'm curious,
[1933.38 → 1934.00] you know, as we've
[1934.00 → 1934.98] kind of talked about
[1934.98 → 1936.08] doing AI in the
[1936.08 → 1937.38] browser all this
[1937.38 → 1938.64] time, as we start
[1938.64 → 1939.76] seeing AI in the
[1939.76 → 1940.64] browser come about,
[1940.94 → 1941.58] you know, how is
[1941.58 → 1942.42] that going to change
[1942.42 → 1943.84] how we're interacting
[1943.84 → 1945.00] with web apps now
[1945.00 → 1946.10] that these models
[1946.10 → 1947.40] are available to
[1947.40 → 1948.88] kind of drive or
[1948.88 → 1950.58] provide services to
[1950.58 → 1951.36] the apps that we're
[1951.36 → 1952.18] engaging in?
[1952.54 → 1953.94] And do you expect
[1953.94 → 1954.62] with, you know, you
[1954.62 → 1955.18] were talking about
[1955.18 → 1956.66] hand track JS, do
[1956.66 → 1957.60] you expect us to
[1957.60 → 1958.36] start having the
[1958.36 → 1959.16] ability to use
[1959.16 → 1960.58] gestures, control
[1960.58 → 1961.22] things and to
[1961.22 → 1962.48] scroll, and we're
[1962.48 → 1963.94] getting beyond just
[1963.94 → 1965.06] the mouse or
[1965.06 → 1966.00] trackpad and the
[1966.00 → 1967.26] keyboard into a
[1967.26 → 1968.44] more rich user
[1968.44 → 1969.72] experience on web
[1969.72 → 1969.90] apps?
[1969.90 → 1970.90] Right.
[1971.18 → 1971.98] As a researcher
[1971.98 → 1973.66] interested in human
[1973.66 → 1974.72] computer interaction
[1974.72 → 1976.40] and how AI can
[1976.40 → 1978.02] kind of influence or
[1978.02 → 1979.06] make that space
[1979.06 → 1980.72] better, I definitely
[1980.72 → 1981.84] and totally think
[1981.84 → 1983.86] that AI models,
[1984.48 → 1985.94] they're well posed to
[1985.94 → 1987.12] kind of create a
[1987.12 → 1988.08] future where we have
[1988.08 → 1990.44] a new set of
[1990.44 → 1991.56] interactions that are
[1991.56 → 1992.48] just purely enabled
[1992.48 → 1993.10] by AI.
[1993.50 → 1994.58] I think right now we
[1994.58 → 1995.26] have a lot of good
[1995.26 → 1996.72] examples and these
[1996.72 → 1997.98] things, they work so
[1997.98 → 1999.16] well that now we
[1999.16 → 1999.88] all take them for
[1999.88 → 2000.20] granted.
[2000.52 → 2001.74] And so examples like
[2001.74 → 2003.22] Smart Reply, Gmail
[2003.22 → 2004.52] Smart Reply, Smart
[2004.52 → 2006.18] Compose, even
[2006.18 → 2007.88] other complete on our
[2007.88 → 2008.14] phones.
[2009.16 → 2010.62] And so I think in
[2010.62 → 2012.66] similar vein, I
[2012.66 → 2013.70] definitely see, you
[2013.70 → 2014.98] know, the opportunity
[2014.98 → 2017.52] to have gesture based
[2017.52 → 2018.84] interactions based on
[2018.84 → 2020.60] camera and maybe
[2020.60 → 2023.34] command much better
[2023.34 → 2025.12] voice based interaction.
[2025.12 → 2027.46] So speech, voice,
[2027.70 → 2029.54] computer vision,
[2029.68 → 2030.54] pointing gestures.
[2031.24 → 2032.40] And hopefully as
[2032.40 → 2033.52] these models become
[2033.52 → 2035.48] much smaller, much
[2035.48 → 2038.10] well optimized, it
[2038.10 → 2038.88] should be just as
[2038.88 → 2040.38] easy as adding just,
[2040.54 → 2041.20] you know, a really
[2041.20 → 2042.92] light JavaScript file
[2042.92 → 2044.32] and getting that to
[2044.32 → 2044.54] run.
[2045.34 → 2046.56] And so we're still a
[2046.56 → 2047.52] bit far from that.
[2047.72 → 2048.34] The main challenges
[2048.34 → 2049.78] here is that it's
[2049.78 → 2050.88] mainly around the size
[2050.88 → 2051.54] of these models.
[2051.84 → 2053.36] And so, for example,
[2053.68 → 2055.30] HandTrack.js, the
[2055.30 → 2056.68] current version, in
[2056.68 → 2057.66] terms of megabyte, the
[2057.66 → 2058.82] model itself is about
[2058.82 → 2060.22] 18 megabytes.
[2060.90 → 2062.74] And in web standards,
[2062.90 → 2064.30] 500 kilobytes are
[2064.30 → 2065.62] already a lot of data.
[2066.56 → 2067.90] And so I guess this is
[2067.90 → 2069.30] one limitation that
[2069.30 → 2070.66] kind of bars people from
[2070.66 → 2071.70] widespread adoption.
[2072.16 → 2073.26] But there's a lot of
[2073.26 → 2075.06] research that's kind of
[2075.06 → 2076.32] pointing towards a
[2076.32 → 2077.12] future where high
[2077.12 → 2078.38] performance models, we
[2078.38 → 2079.68] could actually find
[2079.68 → 2080.52] ways to compress
[2080.52 → 2082.24] them with very
[2082.24 → 2083.48] little loss of
[2083.48 → 2083.92] accuracy.
[2084.12 → 2085.14] And I think that
[2085.14 → 2085.98] kind of research is
[2085.98 → 2086.70] really going to be
[2086.70 → 2088.38] key to getting more
[2088.38 → 2089.34] of these models in
[2089.34 → 2090.50] production and easily
[2090.50 → 2091.74] integrated into a lot
[2091.74 → 2092.64] of web applications.
[2093.74 → 2094.88] So how does this
[2094.88 → 2096.58] fit into the and
[2096.58 → 2097.60] this may be something
[2097.60 → 2098.30] you're familiar with
[2098.30 → 2099.12] or not, but I was
[2099.12 → 2100.12] kind of wondering
[2100.12 → 2100.66] while you were
[2100.66 → 2101.64] talking about that
[2101.64 → 2103.06] and in terms of the
[2103.06 → 2105.28] limitations of the
[2105.28 → 2106.32] size of models
[2106.32 → 2107.04] coming down to
[2107.04 → 2108.06] devices, does this
[2108.06 → 2109.56] fit into the whole
[2109.56 → 2111.38] like federated
[2111.38 → 2113.20] training side of
[2113.20 → 2114.24] things where like
[2114.24 → 2115.70] some data scattered
[2115.70 → 2117.16] like between different
[2117.16 → 2118.18] phones and that sort
[2118.18 → 2118.72] of thing, or maybe
[2118.72 → 2119.64] that's totally separate
[2119.64 → 2121.22] from the JavaScript
[2121.22 → 2122.28] side of things.
[2122.44 → 2123.72] Is the difference
[2123.72 → 2124.90] like, you know, in
[2124.90 → 2125.86] the federated sense
[2125.86 → 2127.36] you're utilizing data
[2127.36 → 2129.20] that's on people's
[2129.20 → 2130.24] different devices and
[2130.24 → 2130.92] training a larger
[2130.92 → 2131.68] model that you would
[2131.68 → 2132.42] still use on the
[2132.42 → 2134.16] backend, whereas like
[2134.16 → 2135.16] in the TensorFlow.js
[2135.16 → 2136.10] case, you're really
[2136.10 → 2136.94] interested in just
[2136.94 → 2137.64] kind of single
[2137.64 → 2139.62] user and their
[2139.62 → 2141.34] data, or are you
[2141.34 → 2142.20] aware of that, how
[2142.20 → 2142.98] that kind of fits
[2142.98 → 2144.22] into this picture?
[2144.98 → 2145.96] Right, so it's
[2145.96 → 2147.18] definitely related.
[2148.28 → 2149.06] Federated learning,
[2149.18 → 2149.80] like you mentioned,
[2149.90 → 2150.78] is the whole idea
[2150.78 → 2151.84] where we have a
[2151.84 → 2153.84] federated model and
[2153.84 → 2155.58] at each end user or
[2155.58 → 2156.76] client device, we
[2156.76 → 2158.24] could train client
[2158.24 → 2159.72] models and then send
[2159.72 → 2160.66] some kind of model
[2160.66 → 2161.94] updates back to the
[2161.94 → 2164.28] server to have a much
[2164.28 → 2165.18] better or higher
[2165.18 → 2166.28] performance federated
[2166.28 → 2166.62] model.
[2167.52 → 2168.52] And the value here is
[2168.52 → 2170.02] that data still stays
[2170.02 → 2171.04] on the client devices,
[2171.04 → 2172.28] but just these model
[2172.28 → 2173.32] updates that don't
[2173.32 → 2175.18] compromise privacy, data
[2175.18 → 2177.02] privacy, gets sent back
[2177.02 → 2177.60] to the server.
[2178.38 → 2180.28] And so how is TensorFlow.js
[2180.28 → 2181.84] kind of connected to all
[2181.84 → 2182.26] of these?
[2182.42 → 2184.66] I guess the value here is
[2184.66 → 2185.96] that TensorFlow.js could
[2185.96 → 2189.02] be a tool that lets you
[2189.02 → 2190.62] implement federated
[2190.62 → 2191.62] learning on a global
[2191.62 → 2192.02] scale.
[2192.02 → 2193.48] I mean, this choice is
[2193.48 → 2194.60] something that developers
[2194.60 → 2195.34] have to make.
[2196.32 → 2197.66] But with TensorFlow.js,
[2198.04 → 2199.30] you could definitely
[2199.30 → 2201.28] construct local models
[2201.28 → 2203.12] on end user devices
[2203.12 → 2204.18] using local data.
[2204.72 → 2206.36] And depending on how
[2206.36 → 2207.10] you want to structure
[2207.10 → 2208.26] your system, you could
[2208.26 → 2209.86] send model updates to
[2209.86 → 2210.94] some federated model
[2210.94 → 2212.46] within your server.
[2213.18 → 2214.04] And I think there's some
[2214.04 → 2215.02] experimental implementation
[2215.62 → 2217.86] of a federated learning
[2217.86 → 2219.20] model, I think, on the
[2219.20 → 2220.40] TensorFlow.js GitHub
[2220.40 → 2220.96] repository.
[2220.96 → 2222.44] And so if people are
[2222.44 → 2223.54] interested in exploring
[2223.54 → 2224.72] that more, that's a
[2224.72 → 2225.56] great place to start.
[2226.30 → 2227.56] So I got a follow-up
[2227.56 → 2228.78] question as well as we
[2228.78 → 2230.08] were talking about,
[2230.18 → 2231.44] you know, kind of the
[2231.44 → 2233.02] rise of gestures and
[2233.02 → 2234.48] richer interactions.
[2234.94 → 2236.32] And I'm just kind of
[2236.32 → 2237.04] curious what your
[2237.04 → 2237.90] thoughts are, you know,
[2237.90 → 2238.80] now that, you know,
[2238.90 → 2241.06] for on iPhone and other
[2241.06 → 2242.30] Apple devices, you have
[2242.30 → 2244.22] 4ML and, you know, on
[2244.22 → 2245.24] Android, you have the
[2245.24 → 2246.62] Google ML Kit.
[2246.62 → 2248.04] And is having those
[2248.04 → 2249.30] available on these end
[2249.30 → 2251.22] devices making a
[2251.22 → 2252.24] substantial difference
[2252.24 → 2253.58] in the ability to get
[2253.58 → 2254.92] there faster in terms of
[2254.92 → 2255.98] that richer user
[2255.98 → 2256.42] interface?
[2256.58 → 2257.30] Are you anticipating
[2257.30 → 2259.16] that those are, or are
[2259.16 → 2260.48] they already being used
[2260.48 → 2262.10] heavily with TensorFlow.js
[2262.10 → 2264.20] to try to get every
[2264.20 → 2265.54] possible processing
[2265.54 → 2266.58] capability out of
[2266.58 → 2267.38] whatever device you're
[2267.38 → 2267.54] on?
[2268.02 → 2268.90] Within the TensorFlow
[2268.90 → 2271.56] ecosystem, there's this
[2271.56 → 2273.06] tool called TensorFlow
[2273.06 → 2273.58] Lite.
[2273.78 → 2274.64] I don't know if you're
[2274.64 → 2275.46] familiar with that.
[2275.46 → 2276.56] Yep, we are.
[2277.12 → 2277.26] Yeah.
[2277.32 → 2278.48] And so TensorFlow Lite
[2278.48 → 2279.64] is all about, you know,
[2280.12 → 2282.50] finding ways to compress
[2282.50 → 2284.26] or optimize models such
[2284.26 → 2285.32] that they run on
[2285.32 → 2286.44] research-constrained
[2286.44 → 2287.00] environments.
[2288.10 → 2289.46] And there's a bit of
[2289.46 → 2290.46] relationship with
[2290.46 → 2292.32] TensorFlow.js because the
[2292.32 → 2293.20] main difference being
[2293.20 → 2295.10] that TensorFlow.js is all
[2295.10 → 2296.56] about managing the whole
[2296.56 → 2297.78] machine learning experience
[2297.78 → 2298.92] in JavaScript, while
[2298.92 → 2300.20] TensorFlow Lite is all
[2300.20 → 2301.84] about making models
[2301.84 → 2302.90] smaller such that they
[2302.90 → 2304.36] run in research-constrained
[2304.36 → 2304.94] environments.
[2305.46 → 2306.36] I think there's some
[2306.36 → 2307.50] relationship between
[2307.50 → 2309.08] both because TensorFlow.js,
[2309.38 → 2310.94] you know, it does have
[2310.94 → 2311.82] some focus.
[2312.02 → 2313.38] And so the TensorFlow.js
[2313.38 → 2314.50] converter has some
[2314.50 → 2315.64] applications in model
[2315.64 → 2317.96] quantization where you
[2317.96 → 2319.56] could actually explore
[2319.56 → 2320.60] ways to make your model
[2320.60 → 2321.98] smaller such that it runs
[2321.98 → 2322.88] fast in the browser.
[2323.40 → 2324.04] But I think these are
[2324.04 → 2325.34] slightly different efforts.
[2326.06 → 2327.52] And I also think the
[2327.52 → 2329.46] ability to have compressed
[2329.46 → 2331.04] models that run well on
[2331.04 → 2333.58] smartphones and resource-constrained
[2333.58 → 2335.02] devices like the Raspberry
[2335.02 → 2335.36] Pi.
[2335.36 → 2337.34] I think research in that
[2337.34 → 2338.82] general area should also
[2338.82 → 2340.38] be impactful and useful
[2340.38 → 2343.74] for and transferable, I
[2343.74 → 2345.36] guess, to work being done
[2345.36 → 2346.28] with TensorFlow.js.
[2346.28 → 2349.64] So let's say that, for example,
[2350.18 → 2352.86] I know almost nothing about
[2352.86 → 2354.14] JavaScript, which is actually
[2354.14 → 2354.64] the case.
[2354.78 → 2357.34] And even though I've, you
[2357.34 → 2358.28] know, worked with front-end
[2358.28 → 2359.90] developers and developed
[2359.90 → 2361.38] APIs and that sort of thing,
[2361.38 → 2363.06] I don't really know anything
[2363.06 → 2365.30] about JavaScript other than
[2365.30 → 2367.06] like an occasional like
[2367.06 → 2368.88] hacking into something.
[2369.36 → 2371.30] So for someone in my position
[2371.30 → 2372.40] that's maybe coming from
[2372.40 → 2374.14] Python, what would you
[2374.14 → 2375.88] recommend in terms of
[2375.88 → 2377.34] getting hands-on with
[2377.34 → 2378.26] TensorFlow.js?
[2378.48 → 2380.38] Is it best to kind of start
[2380.38 → 2381.66] by looking at some
[2381.66 → 2384.16] JavaScript, you know, code
[2384.16 → 2385.62] tutorial online and going
[2385.62 → 2386.74] through that and then
[2386.74 → 2388.26] jumping into TensorFlow.js?
[2388.62 → 2390.12] Or are there kind of
[2390.12 → 2392.10] combined tutorials or
[2392.10 → 2393.46] resources that would be
[2393.46 → 2393.80] helpful?
[2393.98 → 2394.52] What are your
[2394.52 → 2395.40] recommendations there?
[2395.92 → 2397.12] Of course, it's always
[2397.12 → 2398.86] always valuable to get a
[2398.86 → 2401.12] refresher on the
[2401.12 → 2402.12] JavaScript language.
[2402.12 → 2404.74] And for beginners, people
[2404.74 → 2405.78] who are interested in getting
[2405.78 → 2406.92] into TensorFlow.js, I
[2406.92 → 2409.44] always recommend the
[2409.44 → 2410.84] tutorials on the
[2410.84 → 2412.20] TensorFlow.js websites.
[2412.50 → 2413.14] And so that is
[2413.14 → 2415.34] TensorFlow.org slash
[2415.34 → 2415.82] JS.
[2416.36 → 2417.80] So they have a bunch of
[2417.80 → 2419.36] tutorials that walk you
[2419.36 → 2420.86] through the APIs that are
[2420.86 → 2422.36] available within the
[2422.36 → 2422.68] library.
[2423.48 → 2424.46] And so just to give an
[2424.46 → 2426.22] overview, TensorFlow.js
[2426.22 → 2428.20] supports two main types of
[2428.20 → 2428.70] APIs.
[2429.40 → 2431.22] So the first is a low-level
[2431.22 → 2433.38] linear algebra API.
[2433.74 → 2434.60] And so if you're interested
[2434.60 → 2436.58] in designing your
[2436.58 → 2437.88] multiplications, your
[2437.88 → 2439.44] additions, you want to
[2439.44 → 2440.50] implement your own loss
[2440.50 → 2442.16] functions, this would be
[2442.16 → 2443.16] the API to use.
[2443.50 → 2444.38] Definitely do not
[2444.38 → 2445.62] recommend it except you
[2445.62 → 2446.34] really know what you're
[2446.34 → 2446.56] doing.
[2447.56 → 2449.32] And the second API it
[2449.32 → 2450.28] provides is something
[2450.28 → 2451.52] called the layers API,
[2451.86 → 2455.54] which is really similar in
[2455.54 → 2457.34] spirit to the Keras API
[2457.34 → 2459.86] structure or Keras API
[2459.86 → 2460.76] design.
[2461.44 → 2463.16] And so it's a really great
[2463.16 → 2464.28] way to reason about
[2464.28 → 2465.94] neural networks.
[2466.26 → 2468.56] And so if you have used
[2468.56 → 2470.14] the Keras API previously,
[2470.50 → 2472.30] using the TensorFlow.js
[2472.30 → 2473.52] layers API should be
[2473.52 → 2474.44] something familiar and
[2474.44 → 2474.70] easy.
[2475.24 → 2477.74] So you find traditional
[2477.74 → 2479.92] building blocks like LSTMs,
[2480.82 → 2482.02] 2D convolutions,
[2482.52 → 2484.66] transpose layers, batch
[2484.66 → 2486.32] normalization layers, and
[2486.32 → 2487.28] essentially they are
[2487.28 → 2489.18] implemented just like you
[2489.18 → 2490.84] would implement that with
[2490.84 → 2491.08] Keras.
[2491.48 → 2492.72] And so if you have your
[2492.72 → 2494.20] model built, you could
[2494.20 → 2496.42] compile it and then also
[2496.42 → 2497.90] get your accuracy metrics
[2497.90 → 2499.74] very similar to how you
[2499.74 → 2500.62] would do that in Keras.
[2501.46 → 2502.72] And so for people just
[2502.72 → 2504.66] interested in making the
[2504.66 → 2505.78] switch from, let's say,
[2506.34 → 2509.00] regular Python or maybe
[2509.00 → 2510.10] machine learning with
[2510.10 → 2511.72] Python to TensorFlow.js, I
[2511.72 → 2512.92] would recommend looking at
[2512.92 → 2514.38] tutorials on the layers API.
[2515.62 → 2517.52] And the other interesting
[2517.52 → 2519.42] thing here is that if you
[2519.42 → 2520.82] have models that are
[2520.82 → 2522.84] already built using and
[2522.84 → 2524.10] exported using the
[2524.10 → 2525.32] TensorFlow.js models
[2525.32 → 2527.42] format or the Keras
[2527.42 → 2529.84] saved models format, you
[2529.84 → 2530.76] can actually use the
[2530.76 → 2532.36] TensorFlow.js converter to
[2532.36 → 2534.14] convert that directly into
[2534.14 → 2535.92] the TensorFlow.js web
[2535.92 → 2536.64] model format.
[2537.48 → 2538.58] And then all you have to do
[2538.58 → 2540.04] is just spent some time
[2540.04 → 2541.78] learning how to load those
[2541.78 → 2542.96] and use that for inference
[2542.96 → 2543.90] in the web application.
[2544.94 → 2545.70] And so these are kind of
[2545.70 → 2547.80] like the mental steps to go
[2547.80 → 2548.06] through.
[2548.40 → 2549.76] It's useful to get a
[2549.76 → 2550.70] refresh in JavaScript.
[2551.88 → 2553.10] And then if you have some
[2553.10 → 2555.42] experience with Keras, the
[2555.42 → 2557.28] learning curve isn't that
[2557.28 → 2557.94] bad anymore.
[2558.74 → 2560.12] And the TensorFlow.js
[2560.12 → 2561.36] website has a bunch of
[2561.36 → 2562.60] tutorials, and they have a
[2562.60 → 2564.60] perfect sample code on
[2564.60 → 2566.28] GitHub to get started.
[2567.28 → 2567.84] Yeah.
[2568.00 → 2569.94] So it sounds like the
[2569.94 → 2571.92] layers thing, like if I'm
[2571.92 → 2573.38] wanting to experiment like
[2573.38 → 2575.08] with layers, I could build
[2575.08 → 2577.56] a fairly easily build like a
[2577.56 → 2579.62] simple, you know, maybe a
[2579.62 → 2581.18] fully connected neural net
[2581.18 → 2583.44] that would, you know, solve
[2583.44 → 2585.64] some kind of toy problem,
[2585.76 → 2586.72] let's say iris
[2586.72 → 2587.90] classification or something.
[2587.90 → 2589.38] I could do that fairly
[2589.38 → 2590.66] easily with the layers and
[2590.66 → 2591.84] kind of get a feel for it.
[2591.84 → 2593.66] But then I could also take
[2593.66 → 2595.02] like maybe a pre-trained
[2595.02 → 2596.90] model for image
[2596.90 → 2598.80] detection that's existing
[2598.80 → 2602.02] and try just to do
[2602.02 → 2603.68] the inferencing part by using
[2603.68 → 2604.92] the TensorFlow converter.
[2605.10 → 2606.76] So those would be two
[2606.76 → 2607.86] things that would be reasonable
[2607.86 → 2609.26] to try first, maybe.
[2609.78 → 2609.92] Right.
[2610.02 → 2610.68] That is correct.
[2611.54 → 2611.86] Cool.
[2612.22 → 2613.42] You know, a lot of what you
[2613.42 → 2615.12] kind of have worked on
[2615.12 → 2616.96] personally as related to the
[2616.96 → 2618.30] hand tracking, that's that's
[2618.30 → 2621.20] related to image and video
[2621.20 → 2622.72] based techniques.
[2622.72 → 2624.88] And I had just seen before
[2624.88 → 2626.84] the before we started
[2626.84 → 2628.94] recording, I saw that
[2628.94 → 2630.14] you and the Fast Forward
[2630.14 → 2632.70] Labs team released this
[2632.70 → 2634.66] Cornet playground.
[2635.28 → 2636.20] And I was wondering if you
[2636.20 → 2637.70] could just mention, you know,
[2637.74 → 2638.24] what that is.
[2638.30 → 2639.38] That might be another great
[2639.38 → 2640.50] learning resource kind of
[2640.50 → 2642.52] beyond TensorFlow.js, but
[2642.52 → 2643.98] also related because a lot of
[2643.98 → 2645.42] the stuff shows image
[2645.42 → 2646.86] detection examples.
[2647.42 → 2647.72] Right.
[2647.88 → 2648.06] Yeah.
[2648.06 → 2648.58] Thanks for that.
[2649.00 → 2650.26] The tool you're referring to
[2650.26 → 2651.46] is Cornet Playground.
[2651.46 → 2653.76] And essentially, it's a tool
[2653.76 → 2655.76] that lets you experiment and
[2655.76 → 2658.20] learn about how
[2658.20 → 2660.12] convolutional neural networks
[2660.12 → 2661.72] can be applied to the task of
[2661.72 → 2663.00] semantic image search.
[2663.86 → 2666.00] And so within the framework of
[2666.00 → 2667.38] that application, we have a very
[2667.38 → 2669.60] simple definition where semantic
[2669.60 → 2672.08] search is all about giving an
[2672.08 → 2674.88] image, find all other images
[2674.88 → 2677.28] that are similar to this image, but
[2677.28 → 2678.74] just by looking at their content.
[2679.56 → 2681.10] And so the implementation is
[2681.10 → 2681.78] really simple.
[2682.10 → 2683.98] We get a convolutional neural
[2683.98 → 2685.72] network, and we use that as a
[2685.72 → 2687.14] feature extractor on all the
[2687.14 → 2687.58] images.
[2688.62 → 2689.60] And based on this feature
[2689.60 → 2691.60] extracted, we can compute some
[2691.60 → 2693.42] measure of similarities in, let's
[2693.42 → 2695.22] say, cosine distance or Murkowski
[2695.22 → 2695.66] distance.
[2696.00 → 2697.04] And essentially, that's how
[2697.04 → 2698.78] similarity is implemented.
[2698.78 → 2702.84] However, in practice, there's a
[2702.84 → 2704.42] bunch of decisions that a data
[2704.42 → 2705.68] scientist needs to make.
[2706.04 → 2708.60] And so what model do I use for
[2708.60 → 2709.42] feature extraction?
[2709.66 → 2710.64] If I was going to use a
[2710.64 → 2711.36] pretrained model.
[2711.76 → 2713.48] And so there are dozens of
[2713.48 → 2714.72] pretrained models out there.
[2714.92 → 2717.64] Inception, VG16, VG19.
[2718.48 → 2720.06] And even more recently, there are
[2720.06 → 2721.90] new architectures that are enabled
[2721.90 → 2723.76] by neural architecture search like
[2723.76 → 2725.90] Efficient Net and NAS Net and
[2725.90 → 2726.72] MNAS Net.
[2726.72 → 2729.64] And so the data scientist needs to
[2729.64 → 2732.76] make decisions on which one of
[2732.76 → 2734.42] these pretrained models do I use.
[2735.08 → 2736.26] And even when they select an
[2736.26 → 2738.22] architecture, they need to also
[2738.22 → 2739.84] decide, do I use the entire model
[2739.84 → 2742.78] or do I use a subset of this model
[2742.78 → 2744.98] constructed from the original model?
[2745.46 → 2746.48] And so once they've made these
[2746.48 → 2747.68] decisions, they finally need to
[2747.68 → 2750.36] decide what similarity metrics
[2750.36 → 2751.62] might be best for these.
[2752.26 → 2753.50] And so we built Connect
[2753.50 → 2756.48] Playground to kind of
[2756.72 → 2758.36] create an environment where all of
[2758.36 → 2759.76] these decisions and all the
[2759.76 → 2761.54] computation for these decisions have
[2761.54 → 2761.96] been made.
[2762.48 → 2763.70] And the user can essentially
[2763.70 → 2765.44] interactively explore what the
[2765.44 → 2766.38] results look like.
[2766.94 → 2768.14] And so there's a search interface
[2768.14 → 2769.96] where we have some datasets and you
[2769.96 → 2771.62] could, for each image in the
[2771.62 → 2772.82] dataset, you could make a
[2772.82 → 2775.16] selection and then view how each
[2775.16 → 2777.52] model performs in terms of search
[2777.52 → 2779.90] accuracy or search quality for that
[2779.90 → 2781.26] particular search query.
[2781.26 → 2783.80] And then we have visualizations that
[2783.80 → 2786.20] let you compare, you know, how do
[2786.20 → 2787.54] the different model architectures
[2787.54 → 2787.94] compare?
[2788.88 → 2791.00] How well does the semantics for each
[2791.00 → 2791.72] model perform?
[2791.82 → 2794.32] And so we have MAP visualizations of
[2794.32 → 2795.88] the feature embedding space.
[2796.42 → 2797.66] And we have a bunch of graphs that
[2797.66 → 2799.48] let you perform all of these
[2799.48 → 2800.04] comparisons.
[2801.34 → 2803.24] And so I'd really encourage everyone
[2803.24 → 2804.72] that has a chance and wants to learn
[2804.72 → 2806.56] about pretrained models to kind of
[2806.56 → 2807.32] explore that.
[2807.86 → 2809.12] These are some of the fascinating
[2809.12 → 2811.86] insights there that one common thing
[2811.86 → 2813.62] that data scientists do right now is
[2813.62 → 2815.48] that to extract features, they would
[2815.48 → 2819.58] just select VGG16 and select its last
[2819.58 → 2821.58] layer and use that as a feature
[2821.58 → 2822.06] extraction.
[2822.28 → 2823.68] And so it turns out that this might be
[2823.68 → 2824.18] inefficient.
[2825.00 → 2828.32] The VGG16 has about 130, over 130
[2828.32 → 2829.28] million parameters.
[2830.04 → 2833.30] But a model like Efficient Net B2 has
[2833.30 → 2835.30] about 5 million parameters and it
[2835.30 → 2838.18] actually works better than VGG16 in
[2838.18 → 2840.18] terms of extracted features for natural
[2840.18 → 2840.64] images.
[2841.76 → 2843.58] And these are some of the insights you
[2843.58 → 2845.18] could actually extract by exploring
[2845.98 → 2847.06] that interface.
[2848.16 → 2850.30] And depending on the type of your data,
[2850.52 → 2852.46] so if you have retail data, if you have
[2852.46 → 2854.60] natural images, these different
[2854.60 → 2857.08] performances will change, and you can
[2857.08 → 2858.62] kind of explore the space using
[2858.62 → 2859.44] Comet Playground.
[2859.82 → 2860.10] Cool.
[2860.30 → 2861.82] Well, this has been a fascinating
[2861.82 → 2862.50] conversation.
[2863.14 → 2865.04] Thank you, Victor, so much for coming
[2865.04 → 2867.00] on to the show and telling us all
[2867.00 → 2870.44] about TensorFlow.js and these other
[2870.44 → 2871.98] projects and stuff.
[2872.42 → 2873.48] Really great conversation.
[2874.04 → 2874.42] Thank you.
[2874.60 → 2876.00] And I guess for our listeners, we want
[2876.00 → 2878.92] to remind everyone that we have a
[2878.92 → 2880.56] number of different communities where
[2880.56 → 2882.10] you can reach out to us and have
[2882.10 → 2882.66] conversation.
[2882.82 → 2884.16] A lot of the show is built on your
[2884.16 → 2885.30] feedback and your comments.
[2885.96 → 2888.10] You can go to changelog.com slash
[2888.10 → 2890.02] community and opt in.
[2890.02 → 2892.18] If you're on LinkedIn, there is a
[2892.18 → 2894.60] Practical AI podcast group that you
[2894.60 → 2895.12] can join.
[2895.42 → 2896.96] We have our Slack community, which you
[2896.96 → 2897.88] can reach by the website.
[2898.06 → 2899.80] And also, because we're talking about
[2899.80 → 2901.44] JavaScript on this episode, we wanted
[2901.44 → 2903.90] to point out that the changelog also
[2903.90 → 2907.20] has the JS Party podcast, which is a
[2907.20 → 2909.24] fantastic podcast having to do with
[2909.24 → 2910.06] all things JavaScript.
[2910.34 → 2912.86] And you can find that at changelog.com
[2912.86 → 2914.52] slash JS Party.
[2914.88 → 2917.40] So we look forward to seeing you guys
[2917.40 → 2917.94] next time.
[2918.02 → 2918.68] Thank you very much.
[2920.02 → 2921.58] All right.
[2921.62 → 2923.32] Thank you for tuning into this episode
[2923.32 → 2924.26] of Practical AI.
[2924.52 → 2925.70] If you enjoyed the show, do us a
[2925.70 → 2925.96] favour.
[2926.08 → 2926.68] Go on iTunes.
[2926.80 → 2927.50] Give us a rating.
[2927.74 → 2929.42] Go in your podcast app and favourite
[2929.42 → 2929.62] it.
[2929.72 → 2931.00] If you are on Twitter or social
[2931.00 → 2932.44] network, share a link with a friend.
[2932.50 → 2933.68] Whatever you got to do, share the
[2933.68 → 2934.88] show with a friend if you enjoyed it.
[2935.16 → 2936.62] And bandwidth for changelog is
[2936.62 → 2937.82] provided by Vastly.
[2937.94 → 2939.38] Learn more at fastly.com.
[2939.56 → 2940.96] And we catch our errors before our
[2940.96 → 2942.20] users do here at changelog because
[2942.20 → 2942.76] of Rollbar.
[2943.00 → 2944.44] Check them out at rollbar.com
[2944.44 → 2945.38] slash changelog.
[2945.70 → 2947.52] And we're hosted on Linde cloud
[2947.52 → 2948.20] servers.
[2948.56 → 2950.00] Head to linode.com slash changelog.
[2950.00 → 2950.70] Check them out.
[2950.78 → 2951.62] Support this show.
[2952.02 → 2953.94] This episode is hosted by Daniel
[2953.94 → 2955.20] Whiten ack and Chris Benson.
[2955.66 → 2957.72] The music is by Break master Cylinder.
[2958.16 → 2959.70] And you can find more shows just like
[2959.70 → 2961.00] this at changelog.com.
[2961.64 → 2963.18] When you go there, pop in your email
[2963.18 → 2963.68] address.
[2963.98 → 2965.60] Get our weekly email keeping you up to
[2965.60 → 2967.42] date with the news and podcasts for
[2967.42 → 2969.66] developers in your inbox every single
[2969.66 → 2970.00] week.
[2970.40 → 2971.16] Thanks for tuning in.
[2971.32 → 2972.04] We'll see you next week.
[2972.04 → 2972.56] Bye.
[2972.56 → 2973.76] Ciao.
[2973.86 → 2974.52] Bye.
[2974.52 → 2975.02] you
