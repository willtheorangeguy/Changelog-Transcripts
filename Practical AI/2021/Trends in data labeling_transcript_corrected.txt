[0.00 → 7.86] We put a lot of effort into making sure that the actual interface inside Label Studio is very intuitive and easy to follow.
[8.40 → 16.24] Because as a data scientist, we always focus on ourselves, but we also put specific focus on non-tech-savvy users.
[16.50 → 23.86] Because those users can actually have a lot of very specific domain interest in knowledge.
[24.16 → 25.56] And you want to be capturing that.
[25.56 → 31.26] But if you build a tool that is very complicated, they would spend a lot of time figuring out how to use that.
[31.50 → 34.92] So we are trying to make it as simple as possible, but yet powerful.
[37.76 → 40.34] Big thanks to our partners, Linde, Vastly, and Launch Darkly.
[40.74 → 42.78] We love Linde. They keep it fast and simple.
[42.92 → 45.28] Check them out at linode.com slash changelog.
[45.50 → 47.58] Our bandwidth is provided by Vastly.
[47.92 → 51.48] Learn more at fastly.com and get your feature flags powered by Launch Darkly.
[51.74 → 53.44] Get a demo at launchdarkly.com.
[53.44 → 57.32] This episode is brought to you by our friends at Rudder stack.
[57.54 → 62.06] And we're calling all data engineers to check out Rudder stack Cloud and start building smart customer data pipelines.
[62.54 → 65.46] Rudder stack is warehouse first, no more silos.
[65.92 → 69.26] Rudder stack builds your customer data lake on your data warehouse, not theirs.
[69.52 → 74.96] Enabling all functionality of a CDP with more security and retaining full ownership of your data.
[75.26 → 77.72] It's open source and API first.
[78.04 → 81.48] Rudder stack can be easily integrated into your existing development processes.
[81.48 → 84.80] And because they're open source, you can see all their code.
[85.02 → 87.44] So you don't have to worry about vendor lock-in or black boxes.
[88.00 → 89.56] And best of all, they have transparent pricing.
[89.76 → 92.00] Stop paying your CDP a premium to store your data.
[92.50 → 97.36] Rudder stack is free up to 500,000 events and pricing scales transparently from there.
[97.78 → 99.80] Learn more and get started at rudderstack.com.
[100.14 → 102.36] Again, rudderstack.com.
[102.50 → 106.02] That's R-U-D-D-E-R-S-T-A-C-K.com.
[106.02 → 122.94] Welcome to Practical AI, a weekly podcast that makes artificial intelligence practical, productive, and accessible to everyone.
[123.28 → 127.34] This is where conversations around AI, machine learning, and data science happen.
[127.60 → 132.42] Join the community and Slack with us around various topics of the show at kingjaw.com slash community.
[132.42 → 133.72] And follow us on Twitter.
[133.88 → 135.44] We're at Practical AI FM.
[136.02 → 144.56] Well, welcome to another episode of Practical AI.
[144.96 → 146.56] This is Daniel Whiten ack.
[146.74 → 150.28] I am a data scientist with SIL International.
[150.64 → 156.04] And I'm joined as always by my co-host, Chris Benson, who is a strategist at Lockheed Martin.
[156.36 → 157.08] How are you doing, Chris?
[157.40 → 158.18] Doing very well.
[158.30 → 159.10] Glad to be here.
[159.10 → 159.54] Yeah.
[159.76 → 165.60] You were just telling me before we started recording that you had an animal rescue emergency right before.
[165.60 → 166.16] I did.
[166.40 → 168.50] And so I'm just glad to show up.
[168.58 → 169.82] I'm glad to be here today.
[170.00 → 171.14] It's a good day for me.
[171.64 → 171.78] Yeah.
[171.98 → 172.78] Yeah, for sure.
[173.06 → 173.66] And you know what?
[173.72 → 174.92] Even more good news.
[175.24 → 178.26] So I don't know if you remember 2019, Chris.
[178.40 → 180.20] That's like pre-pandemic, isn't it?
[180.28 → 181.22] Pre-pandemic.
[181.60 → 183.12] That's a history book thing now.
[183.12 → 184.24] I mean, yes.
[184.46 → 192.78] But pre-pandemic 2019, we had this great conversation about data labelling with Michael Seljuk of Label Studio.
[193.60 → 195.02] And Michael's back with us.
[195.10 → 195.72] How are you doing, Michael?
[196.10 → 196.60] Hey, guys.
[196.86 → 197.56] Doing great.
[197.82 → 201.40] I mean, it seems like we're post-pandemic now, so we somehow survived.
[203.12 → 206.18] Yeah, it's crazy that it's been two years since we talked to you.
[206.30 → 207.18] Right, right.
[207.32 → 208.34] Different world, right?
[208.34 → 209.20] Yeah, it's insane.
[209.34 → 211.52] Like, we first were on a podcast pre-pandemic.
[211.64 → 213.52] Now we're on a podcast post-pandemic.
[214.26 → 220.44] So if ever we make the third podcast, I'm kind of wondering what would happen in that time frame.
[220.74 → 221.14] I don't know.
[221.18 → 224.82] I'm so envious of you because we're still having it here in the American South.
[224.82 → 226.66] I live in the Atlanta metro area.
[226.82 → 231.86] And it's right now as bad as it was in the worst of the previous things.
[232.10 → 233.60] So we have some work to do here.
[233.60 → 238.88] But I am incredibly envious of you fellows being in areas where things are getting a little bit better.
[239.50 → 239.98] Well, yeah.
[240.10 → 242.24] I mean, who knows what the future holds?
[242.40 → 245.66] Who knows what the next, like you say, Michael, the next two years will hold?
[246.12 → 250.12] But I mean, the one thing that's true is people will need to label data.
[250.50 → 253.60] I think that that's something we can all agree on.
[253.72 → 254.70] That was such a good transition.
[254.84 → 255.54] You know, I tried.
[255.62 → 256.58] Oh, my gosh.
[256.60 → 257.30] That was great.
[257.46 → 258.58] I love the way you did that.
[258.58 → 271.54] So I'm curious, Michael, just from your perspective, as you're day in and day out in data labelling world, like and through the pandemic, what has shifted or changed?
[271.54 → 277.58] Or do you see like maybe certain trends happening over the past two years in data labelling?
[277.78 → 279.72] What are some of those shifts that you're seeing?
[280.26 → 281.00] Yeah, good question.
[281.26 → 283.58] It depends on how you look at like the whole markets.
[283.58 → 301.44] What I guess we are seeing from our side when we are talking to our customers and to potential customers is just previously, two years ago, five years ago, the market they were thinking about the data labelling is something that they just need to get done as quickly as possible.
[302.16 → 307.82] Not paying too much attention into some of the gritty details of the labelling process.
[307.82 → 319.96] I think is now changing is that companies are realizing that labelling is actually a way of making your raw data set into what I call a liquid asset.
[320.44 → 332.20] And because of that, they're starting to pay more and more attention around into the process and everything that goes into the process, all the reports, the analytics, the metrics inside the labelling process.
[332.20 → 339.78] I think previously it was kind of, hey, we just need to get our data labelled and go to the next step as quickly as possible.
[340.48 → 350.00] Now it's something where they are actively investing resources into building the internal process and practices around labelling.
[350.54 → 354.38] I mean, we probably knew that for quite some time now.
[354.64 → 360.18] The accuracy of the model kind of more or less directly correlates with the quality of your labelled data sets.
[360.18 → 366.80] And I think that now becomes more and more like this common knowledge for the whole market, for the whole ML markets.
[367.38 → 374.70] Do you think that that's a sign of just kind of this whole industry that we're in maturing and recognizing that people are moving from that?
[374.96 → 376.92] Because I remember I'm totally guilty of that.
[377.04 → 378.16] Just get it done.
[378.40 → 380.50] I want to get through my labelling so I can get to my training.
[380.70 → 383.26] And that's the exciting part, you know, the way we were thinking back then.
[383.38 → 387.54] And now people are recognizing that labelling is kind of strategic to their business.
[387.54 → 392.50] Yeah, I think it's if you look at the whole ML kind of market, it's pretty new.
[392.84 → 398.40] And there were a lot of perfect developments in the infrastructure world.
[398.82 → 403.76] And because of that, the infrastructure for ML kind of becomes a commodity more or less right now.
[403.76 → 412.86] And where your actual strategic investments may be laying in is the labelling, how you process the data and how you prepare the data.
[413.34 → 417.62] Especially if you're working with a data that requires some sort of expert knowledge to be labelled.
[417.62 → 427.30] So everything around how you capture this expert knowledge into the way of labelling data, that's a very liquid asset that you have on your hands after you're done.
[427.76 → 427.86] Right.
[428.00 → 434.86] Back when we talked the first time and kind of the world was always about the GPUs and everybody was buying the latest GPU coming out.
[435.12 → 438.20] But there's no competitive advantage because that's available to everybody.
[438.42 → 446.04] And the same thing, whereas the way you label is something that you can create strategic advantage for your business that's based on your expertise.
[446.22 → 446.98] Right. Exactly.
[446.98 → 449.32] If you have a great tool to do that with.
[449.46 → 453.18] And so I think that's really changed mindset wise since we talked last.
[453.38 → 454.18] Yeah, exactly.
[454.32 → 454.68] Exactly.
[454.90 → 465.38] And that's a great point because when you start paying more attention into the process and how you set up the process, the software that enables you to do that becomes very important.
[465.76 → 473.48] And from the software perspective, it needs to provide you with all sorts of reports around the labelling process.
[473.48 → 477.10] So you can understand all the metrics where we are, like, and where are we going.
[477.10 → 480.32] So you have very tight control over that.
[480.32 → 484.46] And those metrics around the data labelling process.
[484.66 → 492.40] Do you see customers kind of putting the importance on the quality of the labels?
[492.66 → 497.62] Like how consistent they are, how correlated they are with this or that?
[497.62 → 500.56] Or is it more important sort of quantity?
[501.10 → 502.32] Does what I'm asking make sense?
[502.46 → 509.22] Like in terms of quantity and quality, how have you seen people thinking about balancing those two things recently?
[509.78 → 510.50] Yeah, good question.
[510.50 → 515.20] I think it depends on where the company is in terms of their ML adoption.
[515.62 → 517.18] What is the product that we are building?
[517.62 → 525.00] Is it just out of the R&D stage, and it's something new, and we need to test it out, so the quantity is more important over the quality?
[525.70 → 530.00] Or is it something that we are using, for example, in trading on the markets?
[530.52 → 538.62] Because there, the quality becomes very correlated with the dollar impacts that your model is going to make, right?
[538.62 → 543.76] So it depends on the model and like what is the company's, like their actual business use case.
[544.08 → 548.90] I think over time, quality will dominate over the quantity.
[549.40 → 559.70] And you mentioned culture a couple of times, like the culture around data labelling and also like experts within an organization participating in labelling.
[560.48 → 566.84] Something that I've sort of both struggled with and tried to move forward with, but it's been a struggle.
[566.84 → 588.66] It's figuring out like all the best practices around like how you present a labelling task to your labels, how they view the task, how there can be so much variability between labels, how like different groups need sort of like different types of instructions or onboarding and this sort of thing.
[588.66 → 601.50] Like how does a company approach that type of situation and maybe start to build up a bit of that culture and like a bit of that knowledge internally around like expertise in data labelling, I guess.
[601.90 → 605.32] It's a very, very good question and a very complicated one.
[605.32 → 611.80] I would love to know the answer because I don't quite yet know the answer.
[612.04 → 613.56] I need to, probably to.
[614.60 → 620.70] I think you asked a fantastic question there, Daniel, because I myself really want to understand that.
[620.80 → 622.98] That's the hard part when you're getting in.
[623.12 → 626.40] It's a complicated set of answers maybe, but yeah.
[626.56 → 628.48] You're closer to this than we are, Michael.
[628.48 → 628.76] Okay.
[629.30 → 630.40] You're very right.
[630.50 → 640.78] Like, because when it comes to the data that is subjective in its nature, that's where you have all those struggles with labelling that because there can be so many different scenarios.
[640.78 → 652.94] For example, one of the more or less obvious things when you are dealing with subjective data, you want to distribute the same sample that you're labelling to multiple people and look at their consensus, right?
[653.40 → 654.92] So what can happen next?
[655.04 → 656.98] You distribute the same sample to three people.
[657.14 → 658.14] You look at their consensus.
[658.42 → 660.12] All three of them agree, right?
[660.20 → 668.90] But that doesn't necessarily mean that they label it correctly because they may label that based on their knowledge that all three of them have.
[668.90 → 670.70] But this knowledge are incorrect.
[671.12 → 672.12] So there's a bias there.
[672.40 → 673.52] Yeah, it is a bias.
[673.76 → 673.90] Yeah.
[674.10 → 677.50] They basically, all three of them are biased, and they're biased in the wrong way.
[677.94 → 680.58] So there needs to be a verification step after that.
[680.98 → 685.46] But that's kind of on the when you actually start labelling data, right?
[685.52 → 689.84] What comes before that is what you mentioned, instructions for the data labelling.
[689.84 → 701.52] What comes even before that, what we have found out working with the large organizations is the teams inside large organizations, they can run multiple data labelling projects.
[701.82 → 708.82] They may use the same semantically named labels, but the actual name of the label is different.
[709.38 → 714.62] So you can think about all the varieties, how you can use the label name for the first name and last name.
[714.82 → 718.88] It can be F name, first name, can be just name and things like that.
[718.88 → 729.58] So even on the company level, when you start, and you launch the labelling project, it can be already inconsistent with how other teams inside the organization are thinking about it.
[730.24 → 730.34] Right.
[730.34 → 731.64] That begs the follow-up.
[731.74 → 742.38] If you're in a company that is wanting to move, you may have dabbled in deep learning, but there are so many organizations out there that are still not fully in.
[742.48 → 743.84] They're not at a mature level.
[744.02 → 745.34] They're exploring it still.
[745.72 → 750.72] And they're trying to understand how to be productive without wasting lots of money and folks on that.
[750.72 → 754.86] And so how should a company be thinking strategically?
[755.08 → 774.76] So not just the practitioner who's doing the labelling themselves, but if your leadership, and you're wanting to invest in workflow and an infrastructure to support it, how should you be thinking about that in terms of what your company is trying to achieve so that you get the best out of your practitioners when you have them go in and actually do the thing?
[774.76 → 775.98] Yeah, great question.
[776.48 → 783.44] So what I think from the company perspective, from the leadership perspective, take very small steps towards the goal.
[783.78 → 789.78] I think validating the use case with a very little labelling, as little as possible is the first step.
[789.78 → 797.12] And understand the process, basically the process that gets you to a consistent, high quality labelling in the end.
[797.76 → 801.74] And this process would be different for every organization, right?
[801.82 → 804.22] And it depends on a number of things.
[804.38 → 806.74] One of those is what type of data we are labelling.
[807.08 → 807.86] Is it subjective?
[808.16 → 811.06] Does it require subject-matter experts, et cetera, et cetera.
[811.30 → 816.20] And another kind of dimension is what resources do you have to do that?
[816.20 → 819.40] Do you want to include people from the operations teams?
[819.80 → 822.90] Is it going to be a data scientist labelling for the most part?
[823.18 → 825.68] How are we going to be doing the verification step?
[825.76 → 826.84] Who is going to be doing that?
[827.56 → 836.58] So understanding this process to get you to a consistently labelled results, I think this is a critical part in thinking strategically about the data labelling.
[837.14 → 844.74] And one of the things that I've sort of run into a few times recently is even just like the concept of data labelling.
[844.74 → 849.34] It's so common to us as data scientists or practitioners.
[849.34 → 856.12] And we totally get right away why we need this and often the huge value that it provides.
[856.32 → 871.06] But then convincing other groups within your organization about an investment in this area and thinking about this area, it's actually more difficult than I expect in many cases.
[871.48 → 872.24] That's a good point.
[872.24 → 879.84] Yeah, I mean, I don't know if it's they think, oh, we're investing in AI, not data labelling or, you know, whatever the like thought process is.
[880.04 → 881.20] What's this label thing?
[881.30 → 881.44] Yeah.
[881.58 → 882.30] Yeah, I don't know.
[882.36 → 893.36] As like the CEO of a data labelling company, I'm sure you have many of these conversations with like maybe non-technical people about this process.
[893.36 → 904.92] Any tips for like explaining sort of the value of this investment in this area to people that are maybe not data scientists or aren't doing this sort of aren't using the data themselves.
[905.44 → 910.30] It's so central and yet it's kind of invisible to people who aren't actually doing the work.
[910.30 → 922.26] It's more or less like that because you kind of when you think about the data labelling, and you think about the budget that you would need to invest into that, you kind of start thinking, oh, well, maybe we can figure something out.
[922.26 → 941.50] So the way I'm thinking about it and the way I usually talk about it with our potential customers is we are right now in a pretty unique stage when ML and AI is being integrated almost into every organization in the world.
[941.50 → 945.92] One way or another products are being built based on the ML models.
[946.34 → 955.24] And for the companies, one of the easiest way to improve their model performance is actually improved their data labelling processes.
[955.78 → 962.80] And improving your model's performance would mean that your product becomes more competitive on the markets.
[963.24 → 969.88] If your product is more competitive, you can capture more data with your products, and you can improve your model even further.
[969.88 → 984.06] I look at it from the way why Google dominates the search space because they were the one to figure out the algorithm that would make their engines stronger with more of web pages that they crawl.
[984.86 → 984.98] Right.
[985.36 → 987.02] And the same thing with the data labelling.
[987.32 → 994.14] You can improve the models and make the models stronger, more competitive, capture more data and keep improving.
[994.14 → 1002.28] And basically over time, I think those companies that are investing into the data labelling now would dominate their specific markets.
[1002.72 → 1004.64] That makes a lot of sense when you think about it.
[1004.66 → 1009.68] And I think it's something that is that outside of our tiny community, it's not really understood very well.
[1009.82 → 1009.96] Right.
[1010.12 → 1018.12] The effect of labelling can either make a data set really, really useful and really productive across multiple things.
[1018.12 → 1023.20] And yet, if you don't do it well, you can end up with very poor results with the same data.
[1023.38 → 1023.62] Right.
[1023.62 → 1029.60] I think going to Daniel's comment a few minutes ago, I don't think that's well understood in a lot of executive ranks.
[1029.60 → 1059.58] Thank you.
[1059.60 → 1089.58] Thank you.
[1089.60 → 1091.60] Thank you.
[1091.60 → 1092.60] Thank you.
[1092.60 → 1093.60] Thank you.
[1093.60 → 1094.60] Thank you.
[1094.60 → 1095.60] Thank you.
[1105.60 → 1115.92] So I think we've done a good job at really diving into the sort of value of data labelling and how people are thinking about it now, which is fascinating.
[1115.92 → 1117.92] But I'm curious on the tooling side.
[1117.92 → 1124.78] I definitely want to get into Label Studio and what has progressed since then because I have some thoughts and questions there too.
[1124.78 → 1135.34] But in terms of the space in general, how are you seeing this space of tools around data labelling kind of grow and shift over these past couple of years?
[1135.34 → 1136.34] It's pretty crazy.
[1136.34 → 1137.34] It's pretty crazy.
[1137.34 → 1140.34] It's very crowded market in some sense.
[1140.34 → 1141.34] There are a lot of tools.
[1141.34 → 1142.34] There are a lot of tools.
[1142.34 → 1146.34] Even two years ago when with our previous podcast, it was already pretty crowded.
[1146.34 → 1155.04] Now there are kinds of more players and more tooling around the data labelling tools, which I think is interesting.
[1155.04 → 1160.04] So there are like all sorts of data exploration tools as well that are now available.
[1160.04 → 1168.04] On another hand, it's very exciting to see a lot of smart people putting a lot of effort into building all that ecosystem at the moment.
[1168.04 → 1179.20] Yeah. So with that, why don't you tell us a little bit about Label Studio itself in case people haven't caught the previous episode, but also a lot, you know, a lot has been updated since then.
[1179.20 → 1189.84] And I've got a little bit of a secret to tell, you know, Chris, I'm not unbiased in this conversation because I am a Label Studio fan and user.
[1190.06 → 1197.38] So our organization uses Label Studio, and I've used it on a bunch of different things over the past couple of years.
[1197.38 → 1210.66] So I am personally very happy that we had that conversation two years ago because it saved me a lot of work over the past couple of years, you know, looking at Google Sheets where people have tried to label something or, you know, something like that.
[1210.76 → 1215.34] Anyway, tell us a bit about what Label Studio is and how people can use it, maybe.
[1215.88 → 1219.92] Yeah, sure. So Label Studio, it's an open source data labelling tool.
[1219.92 → 1230.10] One of the key features that was a key feature two years ago and still one of the key features today is that it's the most flexible data labelling tool.
[1230.80 → 1242.92] So instead of us giving you the interface that we think would work for your use case, you use the configuration language that we have created to build the interface for your specific data sets.
[1243.32 → 1244.86] It's multi-data type.
[1244.86 → 1247.46] So it supports a variety of data types.
[1247.46 → 1254.62] If you want to label for text, for audios, for images, and it's also multimodel.
[1254.82 → 1262.36] So you can put the text and the audio and multiple images on the same screen and label them at the same time.
[1262.76 → 1265.24] To install, there is our website.
[1265.58 → 1267.08] You can Google Label Studio.
[1267.70 → 1269.28] As I said, it's open source software.
[1269.76 → 1271.26] So there is a PIP package.
[1271.48 → 1272.50] There is a Docker container.
[1273.30 → 1277.00] All of that you can get up and running in a couple of minutes.
[1277.00 → 1277.40] Yeah.
[1277.56 → 1280.52] I love the fact that I can just launch the server, right?
[1280.66 → 1284.00] So, Chris, I'm going to brag on Michael's work here first.
[1284.12 → 1294.80] I can launch the Label Studio server, and then it's available, and then I can build different data labelling projects within the one server, right?
[1294.80 → 1300.58] So it's not like I have to pre-configure my labelling task and then launch it.
[1300.64 → 1305.20] I can launch it and then build my labelling task in the interface, which is kind of fun.
[1305.32 → 1308.60] Because I'm not a UI person by any means.
[1308.86 → 1321.42] So being able to do that and the sort of customization has been cool for us, I know, because, for example, the last one I set up was question answering data set labelling.
[1321.42 → 1334.42] And even if there's like a pre-configured thing for question answering, it's like there's a question, maybe a context or a passage from which you're answering that question, and you like to select the answer in the text or something like that.
[1334.42 → 1342.30] But for our task, we actually had nine different contexts, and we had to select the answer in each one of the nine different contexts.
[1342.66 → 1356.56] So like in another tool that wasn't like this, I would sort of have to shove all of that together and maybe like the same text and then like create little like markers to separate them and do pre and post-processing.
[1356.56 → 1360.68] But here I could just add like nine different text blocks to like label.
[1360.84 → 1365.46] So I think for me, that customization is like a really key feature.
[1365.88 → 1371.30] Maybe you have stats on this in terms of like what people are using, or maybe you don't, but you have templates.
[1371.30 → 1375.30] But do you see a lot of people like in your Slack channel and other things?
[1375.48 → 1379.68] What are some of the creative ways that you see people customizing these tasks?
[1379.68 → 1386.48] I think one of the powerful features of Label Studio is that you usually just need around 10 lines.
[1386.58 → 1397.02] Well, depending on the number of labels that you have, but sometimes you just need 10 lines of this configuration language to build a pretty complicated interface.
[1397.82 → 1404.94] And that's what we usually see in people coming up with the interfaces with like 10, 20, 30 lines of code.
[1404.94 → 1414.00] But at one point I was on this interesting call with one of our potential customers at the moment, and they just shared their screen.
[1414.36 → 1421.24] They used 400 lines of configuration language to basically almost be like a web portal inside Label Studio.
[1421.78 → 1426.94] It was crazy just to look at that, like all the different things that they have put in there.
[1427.48 → 1430.92] Like how much time they've spent in that window making that thing.
[1431.48 → 1432.80] Right, right, right.
[1432.80 → 1436.90] That sounded sort of like almost another mea culpa from Dan right there.
[1437.00 → 1438.84] Like I've done that, you know, kind of like, oh yeah.
[1439.34 → 1440.56] We won't get into that.
[1442.62 → 1449.54] But it was interesting to see like what are some of the like extreme use cases that people have done with the tool.
[1449.86 → 1458.08] So I'm going to follow up since I got to tell you, Michael, I don't think I've ever seen him this just surely excited in one of our episodes about something.
[1458.18 → 1459.66] So I'm very impressed.
[1459.72 → 1461.62] Oh yeah, I'm a total fanboy.
[1461.62 → 1466.40] He totally and the listeners can't see, but we can see each other in the thing.
[1466.52 → 1467.98] And yeah, totally, man.
[1468.20 → 1474.26] I want to convert what the excitement that Daniel has over to our listeners that haven't used it before.
[1474.48 → 1480.32] Can you take that and kind of talk a bit about your workflow for someone who hasn't had a chance yet?
[1480.32 → 1481.82] And they're sitting there in their car.
[1481.98 → 1483.76] They're in traffic right now.
[1483.76 → 1487.32] And they're going, when I get to the office, this is I'm going to open this up and go do it.
[1487.60 → 1488.38] What should they expect?
[1488.48 → 1489.52] What should they be thinking about?
[1489.58 → 1490.58] What's the workflow look like?
[1490.84 → 1491.00] Yeah.
[1491.12 → 1493.00] So in a nutshell, it's a web app, right?
[1493.06 → 1495.16] So this is something that runs in your browser.
[1495.16 → 1501.78] This is something that you can launch on your EC2 instance or whatever the server you're running on your laptop.
[1502.12 → 1503.58] It doesn't need a connection to the internet.
[1503.92 → 1507.94] You go to your browser, and you can start creating the data labelling projects.
[1507.94 → 1510.04] As I said, it's very flexible.
[1510.30 → 1515.10] So you can configure it specifically for your data sets, no matter what your data sets consist of.
[1515.60 → 1525.10] Images, data set, if you're doing the computer region, the NLP tasks, named engine recognition, audio segmentation, all a variety of the use cases.
[1525.80 → 1532.14] And then what's also interesting is you can start connecting the machine learning models to help you do the annotation.
[1532.14 → 1542.16] And the flow of that is very interesting because you do the annotation, a batch of annotations, and you retrain your model.
[1542.16 → 1547.60] And then you do another batch, and you retrain your model again, and you get the new predictions out.
[1548.12 → 1551.60] And you keep improving the model predictions this way.
[1551.76 → 1558.00] It almost feels like teaching a child to do a certain specific task for you, right?
[1558.00 → 1570.42] And this is something that I personally find very exciting because for me, it was like, okay, I can see the actual improvement of the model in its predictions in the real time, right?
[1570.62 → 1574.08] And this is just one of the setups, how you can set up the Label Studio.
[1574.28 → 1585.20] Another one might be that if you're running some sort of human in the loop types of like ML pipeline, where if the model is not sure in its prediction, you send that to a person.
[1585.20 → 1592.12] And the person would be labelled inside Label Studio as soon as the label that gets back into their retraining phase, right?
[1592.24 → 1593.48] And that's another use case.
[1593.98 → 1602.30] But we put a lot of effort into making sure that the actual interface inside Label Studio is very intuitive and easy to follow.
[1602.30 → 1611.34] Because we, as a data scientist, we always focus on ourselves, but we also put specific focus on non-tech savvy users.
[1611.76 → 1619.48] Because those users can actually have a lot of very specific domain and interesting knowledge.
[1619.78 → 1621.18] And you want to be capturing that.
[1621.30 → 1626.88] But if you build a tool that is very complicated, they would spend a lot of time figuring out how to use that.
[1626.88 → 1631.02] So we are trying to make it as simple as possible, but yet powerful.
[1631.40 → 1633.60] I hope that got somebody interested.
[1634.38 → 1635.26] I bet you did.
[1635.40 → 1635.56] Yeah.
[1635.74 → 1650.56] And maybe that's part of like going back to the hard questions that we discussed earlier about like building that culture of data labelling, getting instructions right, setting up the task right, doing verification, all of these sorts of very hard things.
[1650.56 → 1663.36] If you don't have to add to that, like an interface that people like is very unfamiliar, and they can't like figure out how to use, then that's at least one less thing to like to complicate those muddy waters.
[1664.10 → 1664.26] Yeah.
[1664.40 → 1668.98] So like a web app and a browser where people can just sort of click things.
[1669.30 → 1671.22] That's a nice scenario, I think.
[1671.58 → 1677.50] And I'm sure you've looked at sort of user experience, UI type things over time, Michael.
[1677.50 → 1690.60] What has that experience been like as you've developed the front end of Label Studio and maybe things that you thought would work and didn't work or maybe things that you integrated and people love, but you didn't think would have been as big of a deal?
[1690.84 → 1692.52] He's smiling before he answers.
[1693.80 → 1695.10] Many, many.
[1695.10 → 1709.32] What I think is interesting, one other reason why we want to give you this flexibility of building the UI is because you can keep only the relevant parts that are relevant to your data sets.
[1709.74 → 1712.10] And that minimizes the error on the annotators.
[1713.12 → 1717.78] So they don't have something that they actually don't need to use in terms of the UI elements.
[1717.78 → 1725.22] Another thing on the UX and UI design, I want to really praise our open source community.
[1725.94 → 1731.38] So we have had dozens of UX sessions with our open source users.
[1731.70 → 1737.16] We basically just invite them, and we ask them to click around and show them their prototypes.
[1737.56 → 1740.86] They've been very, very helpful in designing the application.
[1740.86 → 1746.42] We have right now more than, well, not more than, but close to 2,500 people in our Slack.
[1747.20 → 1750.60] And some of those community members are very, very helpful.
[1750.88 → 1753.78] And we can do ourselves only as much.
[1754.08 → 1762.90] But then the other bigger part comes from all the contributions in terms of like how we may think about certain cases from our community.
[1763.28 → 1767.72] On the mistakes part, we have done a lot of things that didn't really work.
[1767.72 → 1777.64] But we were quickly identifying those things that are kind of not really user-friendly and just removing them.
[1777.96 → 1783.38] So we have this tendency to really understand what doesn't work.
[1783.74 → 1785.52] Try not to clutter the application.
[1785.92 → 1792.20] Because again, we try to make the tool as simple as possible, but yet to have all those powerful features.
[1792.50 → 1796.30] Which is more of an art than a science, I guess.
[1796.30 → 1797.66] So I'm curious.
[1797.98 → 1799.68] You've got me excited all over again.
[1799.76 → 1807.02] I remember the excitement of this because I went, I haven't been doing as much hands-on as Daniel has, but I went and started using it as well afterwards.
[1807.26 → 1808.26] I just don't know it as well.
[1808.62 → 1818.30] I'm wondering, though, as you've done these improvements over the last couple of years, and you're looking at a world where this is just going to become more and more embedded in business.
[1818.30 → 1821.06] And so it's not this off thing.
[1821.66 → 1829.56] And the amount of data as people are finally starting to learn how to collect their data and not have it transient and gone, and they're storing it.
[1829.76 → 1833.68] And the volume of that data goes up by orders of magnitude.
[1833.68 → 1839.20] And to some degree for use cases, the quality of the data may vary tremendously on that.
[1839.20 → 1852.64] How do you envision the process of labelling going forward in the years to come as the problem, you know, it's solved in the sense of what you've done so far, but it's an ever-changing problem.
[1852.88 → 1855.30] And so you're constantly going to have to chase that down.
[1855.56 → 1858.18] How are you seeing that curve into the future?
[1858.18 → 1859.20] Yeah, great question.
[1859.46 → 1862.86] I think in the future, well, there are different vectors.
[1863.38 → 1869.50] First, with ML adoption itself, we're just going to have more and more use cases that ML can support.
[1870.00 → 1879.82] Meaning that from the labelling perspective, we would need to do a lot of the multimodal labelling and just different varieties of labelling that we are not thinking about right now.
[1879.82 → 1892.88] Then from the perspective of the volume, we're going to have a lot of the really well-pre-trained models that are going to help us label a vast amount of data automatically.
[1893.74 → 1906.36] And then basically what people would be concentrating on are their edge cases, domain-specific cases, and just the cases where there are not good pre-trained common knowledge models available yet.
[1906.36 → 1921.30] So I think with more ML adoption in the business, we'll see that the need for the labelling is only going to grow just because from the fact that ML is going to support more and more use cases within the business.
[1921.30 → 1939.18] Do you get any sort of weak signals off of what people are doing with Label Studio in terms of the different domains of machine learning, AI, in terms of like people's focus on NLP or people's focus on audio or like new things with computer vision?
[1939.74 → 1948.10] Do you happen to see like trends in that with like new people coming into Slack wanting to do all of a sudden or, you know, something like that?
[1948.10 → 1952.00] Yeah, it's a good question, but it's not that easy to answer that too.
[1952.22 → 1959.90] Because what we see, for example, we are one of the very, very few tools that supports time-series labelling.
[1960.28 → 1964.56] And the majority of the people that are doing time-series labelling, they use Label Studio.
[1965.22 → 1967.08] So we see a lot of those people.
[1967.32 → 1971.96] But then on the other hand, we see a lot of people who are doing labelling for computer vision.
[1971.96 → 1981.10] And they're, well, not comparable, there is more people doing computer vision, but we have more competitors in terms of the computer vision data labelling tools.
[1981.48 → 1990.40] So I would not be able probably to say that there is a one dominant data type that we see people using the tool to label.
[1990.40 → 1993.04] Again, because of the flexibility of the tool.
[1993.24 → 1998.86] And over time, I don't think that we see a lot of the change because it's the data types are distributed more or less equally.
[1999.32 → 2004.94] Just because from the fact that people usually use a few of the data types at the same time on the same screen.
[2005.24 → 2008.78] You can think about audio and then there is a description for the audio.
[2008.94 → 2012.50] And you kind of want to have the audio on the same screen just for the reference.
[2012.80 → 2014.42] And then you're labelling the transcript.
[2014.42 → 2022.94] So it's hard to pick something and identify the change just given the flexibility of the tool and what it provides to the end user.
[2023.34 → 2027.62] Are there a lot of use cases for having kind of that multimodel approach?
[2027.82 → 2036.24] If you go back a couple of years and people would tend to be either really focused on, you know, NLP or really focused on, you know, labelling convolutional.
[2036.42 → 2039.44] But they tended to be one or the other in my experience.
[2039.44 → 2045.82] And what I've seen since then is a lot more integration and less emphasis on what it is.
[2045.96 → 2048.14] Are you seeing more of that in the tool?
[2048.36 → 2055.48] And how does the tool accommodate that workflow as it's evolved into this kind of mesh of different approaches together?
[2055.86 → 2056.32] Yeah, totally.
[2056.50 → 2061.46] So I think there is a clear trend for multimodel being on the rise.
[2061.46 → 2071.18] And from the tooling perspective, it's, yeah, because you're building the interface yourself, you can put as many data types on the same screen as you want.
[2071.66 → 2078.30] And because you have this ability, even if you don't do the multimodel labelling, you label, let's say, just the text, right?
[2078.48 → 2086.34] Having the audio for the context, if the text is not clear because the transcription was screwed, you still would want to do that.
[2086.48 → 2090.14] So the tool kind of naturally supports this type of use cases.
[2090.14 → 2095.78] But yeah, I agree that I think that we are definitely moving into more of the multimodel world.
[2096.22 → 2099.22] So we've talked a lot about the tool itself.
[2099.48 → 2101.10] It is an open source tool.
[2101.38 → 2118.12] And I'm always curious, too, like in terms of people that are building a business around open source, whether that be a label studio or hugging face or, you know, this sort of grid AI people with Apache TVM or, you know, all of these different cases.
[2118.12 → 2124.82] It seems like people, of course, are always playing with that model and figuring out how it works.
[2125.26 → 2129.16] So you've got the open source tool, but then also you're dealing with a lot of data.
[2129.38 → 2132.36] And open data is very much a topic right now.
[2132.36 → 2139.08] So how do you think about building your business in this space around an open source tool?
[2139.28 → 2143.86] And has that been a struggle in terms of that balance?
[2144.12 → 2146.10] For the open source company, it's always a struggle.
[2146.22 → 2149.86] Because it's open source, you have to identify what you actually want to sell as a product.
[2150.38 → 2152.18] So that's always a complexity.
[2152.18 → 2159.10] But I think there are some really strong advantages to being the open source company.
[2159.46 → 2160.94] One of them is a community.
[2161.50 → 2163.66] You get a lot of insights from the community.
[2163.90 → 2169.36] They help you improve your software the way you would not be able to improve your paid product.
[2170.06 → 2177.46] Another one, because of the community, you have one of the largest community of testers of your software.
[2177.46 → 2184.10] Meaning that your software becomes so well tested just because of the pure adoption of that.
[2184.62 → 2188.84] That you have one of the most stable tools out there, which I think is great.
[2189.38 → 2197.80] And those advantages, I think, at least to myself, they compound over those disadvantages where you have to struggle sometimes to identify
[2197.80 → 2202.72] if this needs to go into the open source or that goes into the paid product.
[2202.72 → 2208.38] And then another one that I think is really important from the company perspective is all our developers,
[2208.38 → 2212.60] they have direct access to the users of their software.
[2213.26 → 2217.84] And that makes them really happy when somebody is getting a lot of value out of it.
[2218.30 → 2220.96] And they talk about you on Twitter or somewhere else.
[2221.36 → 2225.46] And they just tell you how great is the tool that you have built for the developers.
[2225.76 → 2227.48] It's basically the best they can get.
[2228.04 → 2229.68] And they get very excited about that.
[2229.68 → 2239.12] So I think, at least for myself, the advantages of being the open source company clearly beats all those disadvantages that we may have.
[2239.44 → 2246.96] We've seen a lot of the tooling in the larger kind of AI ML space start as open source, which was very different.
[2247.36 → 2251.72] And I can say this because I'm on the older side from the way the software world started off.
[2251.76 → 2254.06] It was all commercial and open source kind of came in.
[2254.22 → 2257.18] And it was small for a while, but it grew and took over.
[2257.18 → 2260.70] We've had the benefit in ML of being able to kind of start from that.
[2261.08 → 2266.26] Do you think that that will continue to be the model just because of the benefits that you just now drew out,
[2266.34 → 2271.06] that it allows you to kind of accelerate and be totally connected with your user base?
[2271.26 → 2276.18] I think there are going to be, I hate to hypothesize on what future holds for us.
[2276.28 → 2282.56] Like if two years ago you would ask me about the future, I would probably not be able to predict the pandemic coming.
[2282.88 → 2283.92] Nor did any of us.
[2283.92 → 2288.72] But I think it's going to be a mixture of both.
[2288.84 → 2294.02] I think there are going to be a market, a huge market for the commercial only closed source solution.
[2294.28 → 2296.44] And they're going to be a market for the open source.
[2296.64 → 2298.14] It's just, it's a different model.
[2298.28 → 2301.06] And I think both of them have their advantages and disadvantages.
[2301.82 → 2309.50] So I'm kind of not thinking about commercial being kind of in the way of open source.
[2309.70 → 2311.50] I think they can just go in parallel.
[2311.50 → 2316.72] Yeah. And data labelling, I'm guessing, will always remain fairly challenging.
[2317.28 → 2324.84] There'll always be an opportunity, I think, for people to build a business out of those things just because it is so challenging.
[2325.28 → 2325.68] Right.
[2325.68 → 2336.04] Yeah. I like what you were mentioning earlier about like one of the things you're sort of keeping track of is people using sort of models to seed their labelling.
[2336.36 → 2338.42] So pre-trained models to do that.
[2338.58 → 2341.56] And that's definitely something that has benefited us.
[2341.56 → 2346.88] So it's cool to see that you're integrating some of that ML layer within Label Studio.
[2346.88 → 2355.70] I'm curious as a user, maybe not as futuristic of a question, but what does the roadmap look like for Label Studio?
[2355.90 → 2363.74] What are those things that you're really like you're getting a lot of requests for or you really sort of at the top of your mind in terms of enabling in the tool?
[2363.74 → 2368.66] Yeah. I think first, we do have a public roadmap on our GitHub.
[2369.10 → 2372.16] I'll share one that I think probably the most exciting one.
[2372.42 → 2376.44] In the next couple of months, we're going to be releasing the support for video.
[2376.60 → 2385.06] Right now, you already can do the video classification type of tasks, but we'll be releasing the one where you'll be able to do the object tracking.
[2385.26 → 2385.82] That's cool.
[2385.82 → 2387.36] Yeah, this is going to be huge.
[2387.76 → 2394.96] With the introduction of this proper video labelling, we'll be covering all major data types.
[2395.76 → 2398.92] And that was our kind of goal for the labelling tool.
[2399.22 → 2400.50] So that's pretty exciting.
[2400.98 → 2405.98] Yeah. I mean, I know that there's like cloud video editing, like tools and stuff.
[2405.98 → 2415.38] Now, I'm sure that that does definitely like put a bit, maybe more of a strain on the tool in terms of its performance than other things.
[2415.38 → 2422.08] Is that like, is that coming last because that major category that you're talking about coming last because of some of those challenges?
[2422.08 → 2425.82] Or is it just sort of like the growing need for that?
[2425.94 → 2427.88] And that's what sort of came next.
[2428.16 → 2429.28] It's a mix of both.
[2429.28 → 2435.78] It's both challenging from the it's just the complexity of the video labelling is very high.
[2436.30 → 2441.52] Then we see more need in terms of our users asking us about labelling.
[2441.52 → 2453.38] And then we just started with images, audios and tags, just because the founders of the company, they're like, we all were coming from exactly these backgrounds ourselves.
[2453.92 → 2457.36] So the video labelling, for some reason, it comes to the last one.
[2458.04 → 2464.04] But I think it's a it would be a good kind of thing to get all of them under the one hood.
[2464.04 → 2464.48] Yeah.
[2464.66 → 2477.70] So it's interesting to me that you said that, and they announced that because I think it puts pressure maybe on an area in software that, you know, wasn't really thinking of themselves as, as having to worry quite so much about ML.
[2477.86 → 2479.62] It's not central to the thing.
[2479.84 → 2485.36] It's ancillary in some, but there's a whole new arena that you're going to be moving into in that sense.
[2485.36 → 2486.16] Yeah, totally.
[2486.52 → 2495.94] And I think what's also exciting is because, again, you can put different data types, and we try to make them talk to each other.
[2496.58 → 2501.24] There are very interesting use cases that can be uncovered by that.
[2501.48 → 2512.34] One of the use cases that was very much requested by our community is, for example, when you're doing the time series labelling, and you want to have the reference with your video stream.
[2512.34 → 2512.82] Right.
[2513.26 → 2519.94] Because when you think about labelling those plots, they may not provide you enough information by themselves to do the labelling.
[2520.06 → 2530.30] But when you have those video stream that is kind of acts as a reference for what the for example, the robot arm was doing, then you can effectively label the time series.
[2530.56 → 2541.72] And I think this kind of merge of different data types on the same screen supporting each other just like opens another box of the use cases that would be available to the community.
[2541.72 → 2542.32] Awesome.
[2543.04 → 2551.10] In two years from now, when we are having this conversation again, what do you think we'll be talking about?
[2551.18 → 2552.18] No more pandemics though.
[2552.36 → 2552.54] Yeah.
[2552.62 → 2553.94] I mean, hopefully no more pandemics.
[2554.48 → 2560.02] Maybe the data labelling world will be fully taken over by Label Studio.
[2560.36 → 2563.00] But yeah, I certainly hope that we have that conversation.
[2563.22 → 2565.92] I think he's going to have Steven Spielberg sitting next to him at that point.
[2567.68 → 2568.16] Yeah.
[2568.80 → 2570.08] Maybe I already have him.
[2570.08 → 2575.42] Well, it's been super fun, Michael.
[2575.58 → 2576.56] I really appreciate it.
[2576.64 → 2579.94] I'm looking forward to that conversation in a couple of years.
[2580.12 → 2581.60] So thank you so much for joining.
[2581.94 → 2582.22] Likewise.
[2582.58 → 2587.18] And we'll make sure our show notes include all the links to great Label Studio stuff.
[2587.36 → 2589.94] So all of you who are listening, definitely check it out.
[2590.02 → 2591.30] And we'll talk to you soon, Michael.
[2591.54 → 2591.98] Thanks, guys.
[2592.22 → 2592.90] Thanks for having me.
[2592.90 → 2598.36] Thank you for listening to Practical AI.
[2598.36 → 2610.94] We have a bundle of awesome podcasts for you at changelog.com, including our brand-new show, Ship It with Gerhard Leon, a podcast about getting your best ideas into the world and seeing what happens.
[2611.28 → 2615.18] It's about the code, the ops, the infra, and the people that make it happen.
[2615.18 → 2619.22] Yes, we focus on the people because everything else is an implementation detail.
[2619.56 → 2624.92] Subscribe now at changelog.com slash ship it or simply search for Ship It and your favourite podcast app.
[2625.00 → 2625.48] You'll find it.
[2625.64 → 2628.88] Of course, the galaxy brain move is to subscribe to our master feed.
[2629.02 → 2634.26] It's all changelog podcasts, including Practical AI and Ship It in one place.
[2634.74 → 2639.34] Search changelog master feed or head to changelog.com slash master and subscribe today.
[2639.34 → 2644.54] Practical AI is hosted by Daniel Whiten ack and Chris Benson with music by Break master Cylinder.
[2644.76 → 2647.26] We're brought to you by Vastly, Vaughn Starkly, and Linde.
[2647.56 → 2648.28] That's all for now.
[2648.48 → 2649.44] We'll talk to you again next week.
[2649.44 → 2649.46] We'll talk to you again next week.
[2669.34 → 2678.48] We'll talk to you again next week.
[2678.48 → 2678.76] We'll talk to you again next week.
