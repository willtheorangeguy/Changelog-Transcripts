[0.00 → 4.20] What we think is unique is the fact that when we are developing these tools, that one, we
[4.20 → 6.88] are involved together in the data collection.
[6.96 → 12.08] So if, for example, we are looking at our health, we go, and we are very involved in
[12.08 → 13.20] the collecting of the data.
[13.38 → 15.38] We are introduced to the place where the data will come from.
[15.44 → 19.16] So we are not like at the end of the computer or waiting for the data to come from or let's
[19.16 → 20.62] build the cool models and take them back.
[20.72 → 21.10] No, no, no, no.
[21.34 → 25.08] So it's that you understand, you go for the training with the radiologist, and they tell
[25.08 → 26.84] you, OK, this is how we're going to capture the image.
[26.90 → 28.24] This is how the image looks like.
[28.32 → 29.80] This is how the beelines look like.
[29.80 → 32.78] And so there's that involvement that we think is unique for us.
[33.02 → 38.02] And we build the data collection devices ourselves, and then we deploy them together with the
[38.02 → 40.10] community and collect the data.
[40.50 → 45.00] And so I feel like the unique aspect here is that we are involved in the data collection,
[45.16 → 46.42] in the data curation.
[46.60 → 51.48] And then also that along the journey of building the models that we do this concurrently with
[51.48 → 54.64] the eventual users of the technologies that we are building.
[54.64 → 60.18] Big thanks to our partners, Linde, Vastly and Launch Darkly.
[60.56 → 61.12] We love Linde.
[61.20 → 62.62] They keep it fast and simple.
[62.74 → 65.10] Check them out at linode.com slash changelog.
[65.34 → 67.40] Our bandwidth is provided by Vastly.
[67.76 → 71.30] Learn more at Fastly.com and get your feature flags powered by Launch Darkly.
[71.58 → 73.30] Get a demo at LaunchDarkly.com.
[73.30 → 85.60] Welcome to Practical AI, a weekly podcast that makes artificial intelligence practical,
[85.90 → 87.68] productive and accessible to everyone.
[88.00 → 92.06] This is where conversations around AI, machine learning and data science happen.
[92.30 → 96.54] Join the community and Slack with us around various topics of the show at changelog.com
[96.54 → 98.44] slash community and follow us on Twitter.
[98.44 → 100.18] We're at Practical AI FM.
[103.30 → 110.66] Welcome to a very special episode of Practical AI.
[111.32 → 112.90] This is Daniel Whiten ack.
[113.00 → 118.90] I am a data scientist with SIL International, and I'm joined as always by my co-host, Chris
[118.90 → 121.90] Benson, who is a strategist at Lockheed Martin.
[122.16 → 122.84] How are you doing, Chris?
[122.98 → 124.10] I am doing very well.
[124.22 → 128.54] I love the way you intoed that about a very special episode because I'm excited about this
[128.54 → 128.78] too.
[128.88 → 130.98] I'm going to get out of the way and let you introduce it.
[130.98 → 137.10] Well, you know, Chris, we've talked over the years about how there's so much amazing AI
[137.10 → 143.62] work going on all around the world and that we want to sort of feature more of that work
[143.62 → 147.40] that's going on outside the US, outside of Western Europe.
[147.72 → 155.20] And I'm really excited because recently I got connected with the Open for Good Alliance.
[155.20 → 161.60] This Open for Good Alliance is a multi-stakeholder group of about 13 members, which was formed
[161.60 → 162.50] in 2020.
[163.18 → 169.84] So that includes the DRC, the International Development Research Centre in Canada, GIG's
[169.84 → 175.08] Fair Forward, Artificial Intelligence for All Project, and Macarena University.
[175.86 → 182.08] And we're really privileged today because we have two individuals from Macarena AI Lab with
[182.08 → 184.76] us, Joyce Named and Madames.
[184.96 → 185.22] Welcome.
[185.62 → 186.28] Happy to be here.
[186.44 → 187.24] Great to have you.
[187.72 → 187.90] Yeah.
[187.92 → 188.58] Thank you, Daniel.
[189.10 → 190.14] Nice to be here.
[190.46 → 190.74] Yeah.
[190.90 → 195.42] And we're going to work with the Open for Good Alliance.
[196.04 → 203.00] And in particular, Joyce, you've agreed to join us for some follow-up episodes in a Spotlight
[203.00 → 205.86] on AI in Africa podcast series.
[205.86 → 211.74] So we're really excited to have you both join us today to talk about the great work happening
[211.74 → 217.76] with Open for Good and Macarena University, but also to follow up with you, Joyce, on future
[217.76 → 225.14] episodes featuring some other AI researchers and developers in Africa and about some of the
[225.14 → 227.98] AI community building that's going on in Africa.
[228.26 → 229.58] So it's really exciting.
[230.04 → 235.56] Joyce, how originally did you get involved with this sort of Open for Good Alliance and
[235.56 → 239.78] some of the community building and data set building that's going on with that?
[239.94 → 240.06] Yeah.
[240.10 → 240.66] Thanks, Daniel.
[240.92 → 241.12] Yeah.
[241.14 → 246.14] It's exciting to be joining this episode and also the future episodes that are coming up.
[246.66 → 251.98] So joining Open for Good started with a project that we've been working with Mozilla
[251.98 → 258.04] and Fair Forward around building resources for African languages, particularly Luganda.
[258.78 → 262.90] And the project, of course, that we're doing there is one, trying to build our automatic
[262.90 → 264.66] speech recognition systems.
[264.96 → 268.56] But we realized that you can't build a system without data.
[269.08 → 273.36] And so we had to go back and then think of how can we be able to collect the data that
[273.36 → 275.86] we can use for building our systems.
[276.18 → 281.02] And that's how the connection came in with Mozilla and Fair Forward because Mozilla has
[281.02 → 285.68] an open platform where we can be able to crowdsource voice recordings.
[286.16 → 290.64] But before we even get to crowdsource the voice recordings, we needed our text recordings.
[290.64 → 295.86] And so that brought in the need for data that is localized, that is built upwards, moving
[295.86 → 297.02] down, moving upwards.
[297.78 → 303.06] And also, so because of what was going on with that project in Uganda at the Maker AI lab,
[303.12 → 308.14] but also within Africa, we thought that the Open for Good Alliance is a good alliance.
[308.62 → 312.54] And so when we formed this alliance, what we acknowledged mainly was that there was lack
[312.54 → 315.64] of localized training data that was of sufficient quality.
[315.64 → 321.60] And that was one of the major obstacles for local AI innovation in Africa, but also in
[321.60 → 321.98] Asia.
[322.48 → 327.80] And so because of that, the alliance was formulated to provide a platform for the coordination
[327.80 → 333.36] and exchange of good practices on how to increase the availability and the quality of
[333.36 → 336.52] openly available training data for machine learning.
[336.52 → 341.98] And although I just gave an example just of NLP or data or speech data, there are several
[341.98 → 347.54] other kinds of data that we are seeing the need for to develop and to work on in the African
[347.54 → 348.06] context.
[348.20 → 352.72] And so the alliance is an association that brings organizations that are working on different
[352.72 → 353.62] kinds of data.
[353.96 → 355.14] Yeah, that's so awesome.
[355.36 → 360.38] I know that Chris, as a strategist with a major organization, is always telling me, you know,
[360.46 → 365.92] data strategy is a key piece to the overall AI strategy within any organization.
[365.92 → 373.14] And so it's awesome to see this alliance forum to really work on those localized data sets.
[373.66 → 379.24] I know that Macarena University is also one of the founding members of this alliance.
[379.46 → 384.62] Mujam Best, you work as a research scientist within the Macarena AI lab.
[384.74 → 390.84] Could you tell us a little bit more about that lab and some of the things that you're involved
[390.84 → 392.84] with and the membership in that lab?
[392.84 → 394.38] Thank you for having me over.
[394.72 → 395.40] Tim Best here.
[395.40 → 401.22] So at the Fischer Intelligence Research Lab here in Macarena University, this is an effort
[401.22 → 405.76] that it's pretty much a group, actually, once you get to look a bit closely, because
[405.76 → 409.12] there are members that have been through the pipeline, through the system.
[409.36 → 414.30] It's at the Macarena University here in Kampala, started as a group of people doing their doctorates
[414.30 → 418.30] in 2009, 10, about that period.
[418.30 → 424.12] And they were coming back from exchange programs that were, you know, with other universities
[424.12 → 425.00] abroad.
[425.00 → 435.14] And so they returned to be able to use these computational techniques that they had learned to solve issues that were pertinent to the local community,
[435.14 → 436.14] largely Africa.
[436.14 → 442.40] So some of the work that is measuring there is's a lot of work in agriculture, because
[442.40 → 448.18] the focus had had to be on issues that were of interest to the people, of interest to the
[448.18 → 448.64] communities.
[448.64 → 454.00] So agriculture, health, looking at infrastructure, languages now.
[454.00 → 459.50] And so some of these, for each, maybe I'll just highlight some of the works that have been done in there.
[460.02 → 471.08] For agriculture, the lab or the group has had a strong contribution to data representation of, say, crop diseases and pests on a large scale,
[471.20 → 475.40] being able to crowdsource that from communities of farmers with mobile phones.
[475.40 → 481.88] There's also been work on automating mundane tasks that are being carried out by experts.
[482.58 → 492.46] So it's sort of using a lot of machine learning and AI to be able to do, say, disease recognition and identification and, you know, classifying those diseases.
[493.20 → 500.18] There's been some work that has been around being able to diagnose the plants non-evasively.
[500.18 → 510.02] So that is using spectrometry light to be able to identify or classify the kinds of diseases that it matches with for some of the key crops.
[510.24 → 522.84] And when I say crops, the early efforts of the lab have been very focused on food security crops within the since about 2010, all the way down to about 2018,
[523.70 → 526.44] that the lab had been focused on, you know, food security crops.
[526.44 → 535.00] But now we see a greater divergence to other important income developing crops or crops that improve the nutrition.
[535.52 → 545.58] There's been work on being able to use radio because radio is still the biggest social media here in the global south, especially here in Africa.
[545.58 → 560.74] So to be able to use radio, which Joyce was lead, to be able to use radio to map where crises are for different crops or for different diseases or for different pest infestations or whatever topics that are around diseases.
[561.32 → 564.58] And that's just the highlight of the work that has been done.
[564.72 → 567.72] And this is in monitoring and evaluation for crops.
[567.72 → 583.52] We've also had work around being able to use AI to reduce, sort of make accessible credit scoring for historically unbanked smallholder farmers, amongst many other things.
[584.00 → 588.76] So this is just the tip of the iceberg of some of the works that have been done in agriculture.
[588.76 → 601.42] When we move over to health, some of the prominent work that we see has been around being able to produce artifacts that can then be attached to microscopes in, you know, in health care centres.
[601.68 → 602.64] Why is this important?
[603.52 → 614.10] It's because largely we have a ratio of, you know, one to 200 patients for every clinician or every lab tech, whereas the gold standard is like one to 20.
[614.10 → 622.06] And so you find that there is a need for being able to reduce the load on clinicians or in lab technicians.
[622.94 → 635.14] And also beyond that, once you are able to get that data, being able to use machine learning to identify which parasites on some of these microscopes you're looking at and then to be able to do a count.
[635.14 → 643.92] This would sort of reduce the load and, you know, 30 minutes procedure to about a two to five minute procedure.
[644.22 → 651.56] So it means that clinicians or the lab techs can work on more people effectively throughout the day within a reduced cost.
[651.94 → 662.56] So we've done some work where we're able to use machine learning to identify and do the counts within an ethical and responsible kind of way.
[662.56 → 675.06] Also in health, we have work that was previously done around using mobile cell phone tower data to track the mobility of people.
[675.06 → 700.24] This data was from a permanent telecom, again, you know, ethically anonymized to be able to just provide a network of how people move and then be able to use that as a feature for predicting the spatiotemporal patterns of diseases where the contributor is, you know, somebody gets infected here, travels to another place, gets bitten by another vector.
[700.24 → 708.24] So some of the diseases like malaria where mobility is a contributing factor.
[708.54 → 713.22] And so this is just, you know, an overview of some of the work in health.
[713.46 → 715.60] There's definitely much more in infrastructure.
[715.60 → 736.12] Some of the early work that has come out of the lab has been being able to identify motorcycles, trucks within traffic using very low cost bread sized devices to be able to identify and know, OK, this rod is probably jammed and predict where traffic scenarios are going to be.
[736.22 → 737.06] Why is this important?
[737.06 → 744.30] It's because there's very limited resources around, you know, city management or township management here.
[744.30 → 746.76] And so those are some of the early works.
[746.76 → 759.30] Of course, recently, there's been work that is using machine learning on COVID response, COVID data and response that was started at the height of the pandemic last year.
[759.30 → 768.12] There's also been work around being able to connect farmers to markets using their small button funds.
[768.30 → 776.26] Not to sure if you know them where a farmer and a willing buyer can send their requests to a central place.
[776.26 → 790.98] And their machine learning matching algorithm could be able to match who is the most potential buyer and the most potential seller based on the proximity of their price, geographical distance to multiple other features.
[791.32 → 795.82] And of course, this gets better and better as you have more data coming in.
[795.82 → 810.18] Yeah. So also maybe just one other last that I would like to highlight is we have a project that is looking at the ethics, the fairness, ethics, accountability and transparency of some of these algorithms that we build.
[810.18 → 823.62] Because we are our policy or our kind of mandate is so paper thin that even doing basic research within the global south, you end up impacting lives of people.
[824.32 → 836.30] So our permeation of our work is very paper thin that we always end up working with communities directly, which is one of the three ethos of the lab that I will talk about, you know, just after this.
[836.30 → 849.78] So one of the things that we also have to look at is, you know, what are the ethical implications of working within these communities, sort of measuring our impact and what are the kinds of fairness questions that we have to ask.
[850.18 → 861.52] Wrapping that up, there are a couple of other projects, but wrapping that up, this is based in a three-step ethos for the lab where the first is to be able to find a good local problem.
[861.52 → 868.98] That is the first ethos that we follow. That means a problem that matters, a problem that has democratic voice as, you know, being important.
[869.36 → 877.68] Then secondly, being able to match that problem to a good computational data, you know, sort of computational toolkit.
[877.68 → 890.16] Or, you know, once we have a problem, we try from a research point of view to see, does this match some technological or computational solution that is accessible to us?
[890.48 → 894.34] So, you know, within AI or within machine learning or within the computing.
[894.54 → 899.78] Then the last is to be able to tie the challenge, the technique to a local beneficiary.
[899.78 → 910.66] So pretty much every project that you will hear out of the lab, every one single project has a local community attached to it or has, you know, some beneficiaries.
[911.00 → 913.84] If it's health, there is a hospital that we are attached to.
[914.20 → 918.52] If it's languages, there's, you know, local radio stations that we're attached to.
[918.96 → 922.20] If it's agriculture, we're attached to the National Crop Service.
[922.38 → 925.14] We're attached to local farmer communities.
[925.70 → 928.76] If it's in roads, we're attached to the city management.
[928.76 → 937.32] If it's air quality monitoring, which is one of the works that has also been done at the lab by a gentleman called Professor Engineer.
[937.76 → 942.76] It's also attached to city management, to schools who have vulnerable communities.
[943.36 → 957.88] So, Joyce, Madames gave an amazing intro to all the things happening at Macarena AI Lab, which are just spectacular in terms of all the different projects that you're involved with and the amazing work that you're doing.
[957.88 → 969.50] He talked about this ethos of working on a problem that matters and connecting data and computational toolkit to that and also sort of attaching that problem to a beneficiary.
[969.50 → 979.40] I know as someone working in a nonprofit, but also having talked to a lot of people about sort of AI for good or social impact projects.
[979.60 → 995.12] One of the things that can happen is that AI people can develop like really great and interesting technology, but maybe that technology doesn't always benefit the end user or the local community that they might have in mind.
[995.12 → 1010.06] How do you think about that as a lab and make sure that the problems that you're choosing and how you're going about those solutions end up impacting the sort of local communities beneficially?
[1010.34 → 1011.04] Yeah, thanks, Daniel.
[1011.04 → 1018.48] I think that's a very good question and a very pertinent question, especially when you're developing AI for social good.
[1019.08 → 1020.76] I guess, how do we try?
[1021.08 → 1022.12] It's a learning process.
[1022.22 → 1024.72] So how do we try to ensure that we do this?
[1025.10 → 1027.12] Some of the issues come up organically.
[1027.44 → 1033.70] So for some, the people who actually need the AI tools can approach the lab and say, we want to work on a project with you.
[1033.70 → 1044.10] And that comes in, for example, with the project that we are working on for building tools for breast and prostate cancer diagnosis based on MRI and ultrasound.
[1044.72 → 1048.76] And so the people who actually need the technologies were very fascinated by AI.
[1048.94 → 1050.56] And then they learned about the AI lab.
[1050.70 → 1051.98] And then they came to us.
[1052.04 → 1053.62] And then we've begun to work together.
[1053.78 → 1056.38] First, of course, we start by writing joint proposals together.
[1056.64 → 1060.52] But eventually, we end up building the tools together with them.
[1060.52 → 1064.38] And many, many times when we do that, we actually have meetings with them.
[1064.76 → 1071.38] They host us at the centre where they actually do the testing and the actual recruitment of the patients.
[1071.64 → 1073.12] And then they take us through the process.
[1073.22 → 1077.52] And also, as we build the models concurrently, we do this concurrently with them.
[1077.56 → 1081.58] And then we are able to get feedback from them because they are very instrumental.
[1082.02 → 1086.80] Sometimes you look at an MRI and you don't know where the cancer is or the lesion is.
[1086.80 → 1091.44] And they come in very handy and say, OK, this is where the lesion is, this is how you're going to label this image.
[1091.82 → 1100.78] And eventually, when you build that tool, and you go to test the tool, then this is something that is usable for them because they've been part of the process or part of the journey of building the AI model.
[1101.24 → 1104.12] And so that's the thing that we've been working with in health.
[1104.58 → 1110.26] And then in agriculture, somehow also it's been like that before we even have a project assigned.
[1110.26 → 1117.02] So if we get maybe funding, and we are beginning a new funding phase or a new project in the lab, we actually go to them.
[1117.08 → 1119.60] We have the experts that we work with, the agriculture experts.
[1119.90 → 1125.62] We go to them, and we discuss the idea that we have, and we want to implement and the project that we want to implement.
[1126.12 → 1130.46] And it's only after they've understood what we want to do that we get a sign off from them.
[1130.46 → 1134.84] And then we get the support that we require to start building that technology.
[1135.26 → 1142.10] And so we are very intentional when we build the AI tools that we don't build them just to have a good tool or a good model.
[1142.34 → 1149.36] But this model that that should actually be able to work and perform in field or for which we are developing the model.
[1149.50 → 1157.68] So we work very, very closely with the agriculture experts, for example, work very closely with the smallholder farmers who are going to use the tools.
[1157.68 → 1164.38] And so many times we have farmer trainings where we have a tool that we are that we have developed, for example, a tool to give them recommendations.
[1164.38 → 1170.06] And we try as much as possible to hold workshops and trainings with them during COVID.
[1170.16 → 1177.08] It's a little bit difficult, but we aim to have physical workshops where we take them through the technology, as well as bring in the agriculture experts,
[1177.08 → 1183.06] because sometimes they might ask a question that's not really necessarily related to the technology, but it's related to that domain.
[1183.06 → 1187.06] And that's where the agriculture experts can come in during those workshops, during those trainings.
[1187.06 → 1196.74] And then we also get feedback from them, from the farmers who are going to eventually use the technology on what they think or what they like or what they don't like with that technology.
[1197.16 → 1207.04] And if we can have the physical trainings also through the lab, we have a dedicated call centre where we have the people who call in and check in on the farmers to find out if they have any problems with that technology,
[1207.20 → 1209.12] any problems with the tools that they are using.
[1209.12 → 1214.54] And then we get back this feedback, go through the feedback and try and improve the models that we are building.
[1215.12 → 1220.58] So it's both that sometimes it's us who go, but also other times it's the experts who come to us.
[1220.90 → 1224.92] And then they are able, we are able to build the technologies that are very impactful.
[1224.92 → 1232.00] And we are hoping that these technologies also can be usable because we don't want at the end of our funding phase that the technology ends there.
[1232.00 → 1236.90] We want something that there's continuity in usage of the AI tools that we are building.
[1237.54 → 1240.50] Joyce, I love the way you approach the problem.
[1240.66 → 1251.84] It's just delightful to listen to with the emphasis on trying to find solutions to problems that are specific to the African community at times.
[1252.06 → 1258.44] And those focuses and these creative things like having call centres to reach the farmers and others that you're working with.
[1258.44 → 1264.20] How did you come up with this particular model to serve this community that you're doing?
[1264.54 → 1268.98] I'm curious, as you look at the broader world of AI around the globe,
[1269.44 → 1275.94] what are some of the things that you feel are unique to what your lab is doing or very differentiated compared to others
[1275.94 → 1281.10] in the way that you're satisfying the problems that you're addressing at this point?
[1281.10 → 1285.84] So I think for the call centre, Daniel might have more ideas about it.
[1285.84 → 1290.80] But what happened is and how the call centre evolved is through our crowdsourcing projects.
[1290.94 → 1300.66] What we wanted is we wanted the farmers to be able to send us images of their gardens so that we can be able to build models that can map what is taking place in the garden over time.
[1300.78 → 1307.02] But because the farmers are out there, and we were introducing a new technology to them, which is the crowdsourcing tool,
[1307.02 → 1315.38] we thought it was interesting, or it would be interesting that we don't just throw the technology and then assume that everything will work out okay because not everyone is tech-savvy.
[1315.84 → 1318.10] And these were applications that are not on feature phones.
[1318.14 → 1324.80] These are applications that are on smartphones and not everyone knew or had an idea of how the smartphone is able to work.
[1324.88 → 1329.98] And so we felt that there was a need to actually reach out and follow up on the crowdsourcing.
[1329.98 → 1335.14] Because also sometimes you would, you know, give them technology and then maybe you don't hear from a farmer.
[1335.56 → 1338.00] Maybe after a week and you're wondering, oh, what happened?
[1338.12 → 1340.46] Is everything going okay because you're running a project?
[1340.58 → 1346.68] And so we thought it was intentional, and we thought it was good to try and reach out to the farmers through the call centre.
[1346.68 → 1355.74] And we think that this has helped us to gain traction in terms of the output and not only on the crowdsourcing, which we thought was beneficial for us because we were getting the image data,
[1356.18 → 1361.30] but in terms of the farmers continually continuing to use the technology that we have developed.
[1361.92 → 1369.84] And so what we think is unique is the fact that when we are developing these tools that we are, one, we are involved together in the data collection.
[1369.98 → 1371.74] I think that data is always the driving factor.
[1371.92 → 1375.74] So we are involved with the people from which we are collecting data.
[1375.74 → 1384.00] So if, for example, we are looking at health as an example, we go, and we are very involved in the collecting of the data.
[1384.18 → 1386.18] We are introduced to the place where the data will come from.
[1386.24 → 1391.40] So we are not like at the end of the computer or waiting for the data to come from or let's build the co-models and take them back.
[1391.52 → 1391.88] No, no, no, no.
[1392.10 → 1398.30] So it's that, you know, you understand, you go for the training with the radiologist, and they tell you, okay, this is how we're going to capture the image.
[1398.38 → 1399.76] This is how the image looks like.
[1400.14 → 1403.38] You know if it's for the lung, they'll tell you this is how the beelines look like.
[1403.38 → 1406.36] And so there's that involvement that we think is unique for us.
[1406.62 → 1410.86] And also speaking maybe about one of the other projects, which is the air quality project.
[1411.40 → 1419.22] And so with the air quality project, what's also unique about that is that, again, with the data collection, that we build the data collection devices ourselves.
[1419.22 → 1423.50] And then we deploy them together with the community and collect the data.
[1423.86 → 1429.86] And so I feel like the unique aspect here is that we are involved in the data collection, in the data curation.
[1430.22 → 1437.86] And then also that along the journey of building the models that we do this concurrently with the eventual users of the technology.
[1437.86 → 1442.86] And that's always a good sign to have acceptability with the stakeholders, with the policymakers.
[1443.68 → 1447.10] And we always have to make sure that when we have a project, we disseminate.
[1447.24 → 1449.50] You know, we kind of provide the findings out there.
[1449.64 → 1458.52] We are intentional to who we invite to the dissemination seminars because we want to ensure that they get to know what the work that's going on in the lab for continuity,
[1458.52 → 1465.18] but also for scalability to other sectors that can be interested in the AI models and the technologies that we are building.
[1465.18 → 1478.46] I think a lot of the points that you made there, Joyce, are just so valuable for any data scientists or AI researchers out there that are working on curating and crowdsourcing and analyzing their data.
[1479.00 → 1487.62] Having that connection with the group that's generating the data and being deeply involved there, I think is such an important point.
[1487.62 → 1495.54] And maybe that gets to some of the sort of ethics and bias type of issues that Luna Best, that you mentioned.
[1496.26 → 1506.30] As you're working on crowdsourcing and curating a lot of this data, Luna Best, maybe you can comment on how you think about bias in those data sets
[1506.30 → 1513.72] and work to make sure that your data collection and usage is ethical, and you're monitoring for bias.
[1514.20 → 1515.62] Yes. Thank you very much.
[1515.62 → 1520.32] One of the things that we really do is, so there are two ways to think about it.
[1520.46 → 1527.90] One of the ways is that you have a regulator or an authority on that kind of data that is working with you.
[1528.14 → 1535.52] If it's a hospital, and you're looking at working with patient data or clinicians, then you want to also be working with the lab techs.
[1535.52 → 1545.36] In agriculture specifically, which is sort of where our way in has been a bit greater is once you're working with groups of farmers,
[1545.56 → 1549.98] you're also working with the National Crop Service or National Animal Service.
[1549.98 → 1560.20] In that way, what you do is that you end up having a lot of work go into, you know, how fair can we be in our data collection geospatially?
[1560.36 → 1566.60] What are the important areas to go to so that there is data representation that has equity?
[1566.60 → 1573.30] If you're involving multiple teams or multiple groups within a certain community sensing exercise,
[1573.56 → 1579.36] you have to have a selection criterion, which is not developed by us alone.
[1579.66 → 1583.00] That has to be in collaboration with a national regulator,
[1583.00 → 1593.54] which means that such a selection protocol or a selection criterion is sensitive to different national or community needs.
[1593.84 → 1601.96] Say like, okay, we need people to participate, but they have to have, there has to be some gender equity in the participation,
[1602.50 → 1607.80] where we always, you know, try to balance participation of both women and the men.
[1607.80 → 1617.26] You know, of course, to some degree of success and in some places where it's actually a challenge due to some of the cultural norms that you have to overcome.
[1617.80 → 1625.38] But we look at the idea of ethics from that first point, the ethics, the bias in the data,
[1625.84 → 1631.38] looking at who is collecting that data geographically, where are they going,
[1631.38 → 1638.02] and being able to involve the subject-matter experts and then provide the subject-matter experts,
[1638.02 → 1645.64] they weigh in, and then we provide the technology that sort of sustainably has to be able to collect this data over time.
[1645.74 → 1654.72] So that's the first way we look at ethics or fairness or transparency or accountability for these data collection mechanisms.
[1654.72 → 1659.60] Coming around all the way at the end of the projects until recently,
[1659.90 → 1667.44] we started doing what are known as, you know, evaluations where we try and evaluate the impact that we have had on these communities.
[1668.00 → 1669.78] So we go back to the community.
[1670.18 → 1673.06] Of course, we have close-knit relationships with them.
[1673.68 → 1678.00] And so we have regular sessions where we have interfaces with them.
[1678.00 → 1685.02] But at the end of a certain trial period, we, you know, go back to them, and then we do some impact assessment.
[1685.52 → 1689.50] If we have collected data from you, has the data come back to help you?
[1689.90 → 1694.02] Ever since we gave you, you know, this tool, has this tool been of help to you?
[1694.42 → 1704.04] And using that kind of technique, you can be able to quickly evaluate which parts of the livelihoods have our technologies or this data collection impacted.
[1704.04 → 1711.20] You know, did it improve some metrics that we, you know, we thought it would improve on the holistic end-to-end picture?
[1711.86 → 1712.04] Okay.
[1712.10 → 1715.02] Has this had, you know, a significant impact?
[1715.64 → 1723.28] Or, you know, being able to measure that impact with some relative accuracy from a qualitative and quantitative point of view.
[1723.36 → 1729.88] So recently, maybe just as an example, really, to just be very clear, we had a livelihood assessment.
[1729.88 → 1739.04] We wanted to know from 2016, maybe 2018 more, we had been working with groups of about 200 farmers.
[1739.22 → 1743.20] We wanted to evaluate how well we have contributed to their livelihoods.
[1743.20 → 1752.56] Because when we first met these farmers, they were smallholder farmers, you know, with a very low income, just enough for their food and for their households.
[1752.56 → 1770.08] And so we tried to evaluate whether our tools that we have put into their lives, that is including a tool to diagnose their plants, tool for data collection, which they send to the national service and the national service gets back to them, the national crop service.
[1770.08 → 1786.70] We have had a tool, which, you know, we'd like to joke and call it like a farmer's WhatsApp, but it's really a question and answer tool that allows them to connect with experts and also connect with fellow farmers to increase the local knowledge transfer between and among them.
[1786.70 → 1794.34] And so we evaluated for a period of about three years that we've been, you know, trying with about 200 plus farmers.
[1794.84 → 1801.16] How has that impacted them financially, socially, economically, intellectually, and among other things?
[1801.30 → 1804.54] And you could see, you know, we're about to publish this work.
[1804.68 → 1808.64] You could definitely see a positive correlation with the use of these technologies.
[1808.64 → 1812.14] And many of the people that have come out to be leaders.
[1812.72 → 1823.38] And now many of these farmers, about half or more, are known or considered as village information points, where people within their villages or localities are able to run to them.
[1823.38 → 1845.12] So once you start seeing that positive impact trend within the communities, that is, you know, gender, then you start seeing the connection between the endpoints and the selection criteria that we had that sort of tries to, you know, minimize bias within the data, within the groups participating, and many other things.
[1845.16 → 1846.30] That's how we look at bias.
[1846.30 → 1850.40] It's a two-ended stick for us, before and then after.
[1853.38 → 1866.34] Changelog News is the best way to keep up with the fast-moving software world.
[1866.72 → 1874.70] We track, log, and contextualize the coolest projects, the best practices, and the biggest stories each and every week.
[1874.90 → 1882.84] Make changelog.com your daily destination, or hit the snooze button and subscribe to our weekly newsletter that hits inboxes on Sunday mornings.
[1883.38 → 1886.38] Join more than 15,000 enthusiastic readers.
[1886.64 → 1892.82] It'll cost you exactly zero dollars, and you can subscribe right now at changelog.com slash weekly.
[1892.82 → 1906.40] So, Joyce.
[1906.54 → 1906.78] Yes.
[1906.78 → 1914.94] Your lab is involved in so many different AI tasks, everything from computer vision and natural language processing.
[1915.38 → 1916.66] You do work in health.
[1916.92 → 1917.86] There's a lot of it.
[1918.34 → 1923.56] As I'm looking through that, I mean, it's, I struggle to keep up with kind of all of those topics myself.
[1923.56 → 1936.06] As I follow the field, how do you, how do you manage a group that is as involved in such a diverse set of tasks and kind of keep it all together and in your head and moving forward productively?
[1936.06 → 1944.30] Yeah, that's a good question because I keep thinking, I'm like, okay, now NLP is perfect, and then there's a need for that.
[1944.38 → 1946.84] So, you're like, oh, we really need to do a project in NLP.
[1947.22 → 1948.98] And then we get funding, and we are off.
[1949.08 → 1950.46] Off we go with our project in NLP.
[1950.62 → 1952.26] But there's also computer vision, you know.
[1952.26 → 1956.36] So, it's quite diverse, but I don't try to do this by myself.
[1956.72 → 1967.62] Daniel is here, but there are other colleagues that I work with, both in the College of Computing, but also in the College of Engineering, Design, Art and Technology, who also have backgrounds in machine learning and AI.
[1967.84 → 1969.64] And we co-lead some of the work together.
[1969.84 → 1974.60] So, there's a machine learning lab in the College of Engineering that we work together with.
[1974.60 → 1989.46] Yeah, and could you describe some of the I mean, you already mentioned some of the things you're doing with the Open for Good Alliance, but could you describe, it sounds like there's a number of collaborations that you are fostering even outside the university as well.
[1989.78 → 1990.10] Yes.
[1990.22 → 1999.12] So, the way we've designed it is the first series are really, first, trying to understand when people want data, where can they get data from?
[1999.12 → 2004.94] And so, the first series that we are having is really around the repositories of the data that are available.
[2005.06 → 2010.08] So, for example, Radiant Earth, where it's an open repository for satellite imagery data.
[2010.24 → 2014.60] And Radiant Earth is also one of the organizations that we have in the Open for Good.
[2015.04 → 2019.48] And so, part of the work that we do inside there is to try and publicize and make people know.
[2019.54 → 2026.94] Because one of the things that people said was, okay, if I want to start AI and I want to maybe do a problem with satellite imagery data, where do I get the data from?
[2026.94 → 2035.32] And so, part of the thing we are doing is awareness, where we are making sure that people are aware about the public repositories that are available there.
[2035.78 → 2039.94] But on the other hand, as well, we have the community building.
[2040.06 → 2046.44] Because, like, the organization that we shall talk to eventually, which is Malakand, where this is more specialized in one field.
[2046.52 → 2053.72] And that's NLP, where they do a lot of community building within the field of natural language processing and, you know, talking to people and dealing with people.
[2053.72 → 2060.10] And so, I think strengthening such organizations can be something that we can be able to work with and talk to.
[2060.60 → 2065.82] And then, and also another organization is much of the things that people also need is training.
[2066.34 → 2073.42] And so, some of the things that we are also doing out of the Alliance, not necessarily within, but out of the lab, is, of course, Data Science Africa.
[2073.42 → 2084.74] I think we've heard about Data Science Africa that does training and training, where we have a one-week-long workshop and summer school, where people come in and train people in AI and Data Science skills.
[2085.40 → 2089.34] And because Data Science is Africa-wide, and it comes, I think, twice a year.
[2089.40 → 2091.40] It used to be once a year, but now it's twice a year.
[2091.70 → 2093.56] And it keeps rotating around different countries.
[2093.56 → 2097.26] So, we thought that in Uganda, we would start something that's local here.
[2097.38 → 2105.98] And so, we've also begun a Data Science Africa local chapter, where we can be able to build capacity of AI and Data Science, but within the different universities in Uganda.
[2106.44 → 2109.06] But our focus is not necessarily just on universities.
[2109.06 → 2118.98] We want to focus on the intersection between the university, the private sector, the government as well, because we feel that connection between these different bodies are important.
[2118.98 → 2129.90] And so, there's work, which is not necessarily the project, but there's work that is really focused on capacity building, because we want to grow the next group of data scientists in Uganda and in Africa as well.
[2130.50 → 2133.92] So, Joyce, it's cool to hear about that community building.
[2134.12 → 2135.16] And I'm just amazed.
[2135.42 → 2147.60] I do think you probably have superpowers, because you're managing such a you're managing and leading this lab with so many different important projects going on, but also involved in data crowdsourcing and all of that.
[2147.60 → 2171.18] And, Mood and Desai, when I'm hearing you talk, I'm actually picking up on another thread, which I'm super impressed with and curious about, which is the fact that you're, as an AI lab, not only involved in doing sort of AI research at the cutting edge, but you're also involved in actually producing like software and applications that people can actually get their hands on and use.
[2171.18 → 2187.08] In industry, like in industry, like in most AI groups in industry, this is a struggle to sort of push from development and research and AI into like actual application of that AI in production and in actual software.
[2187.08 → 2207.76] How have you navigated that within your own work in terms of taking AI models from that research stage in the lab into maybe a mobile application or a website or whatever it is, or offline processing in production that people actually get their hands on and impact end users?
[2208.10 → 2211.18] What have been some of the challenges and successes along that way?
[2211.50 → 2212.64] Very interesting question.
[2212.86 → 2213.70] Thanks, Daniel.
[2213.70 → 2236.54] So one of the things you may want to keep in mind is that though the technical processes of being able to deliver or implement a piece of technology or invention or innovation to a community, you know, though that is standard of like, say, software development, the way you work with communities to be able to deliver that is different across the world.
[2236.54 → 2266.52] So for us, it's been a very different.
[2266.52 → 2268.52] To be able to be able to be able to be able to be able to be able to deliver that is different.
[2268.52 → 2272.24] To be able to share those stories, the experiences and resources across the African continent.
[2272.36 → 2282.36] Because when you look at our path, you know, we sort of skipped many of the computer age and went directly to a mobile age or the mobile era.
[2282.88 → 2287.24] So the way technology permeates within the African continent is also very different.
[2287.24 → 2308.26] And so this is one of the things that has ended up, you know, whichever project within the lab, you know, started as just a very simple basic research idea, either of a master's or somebody doing their master's or doing their PhD, ended up, you know, being highly needed once it hit with the community.
[2308.26 → 2322.74] And once you work with a small community of a small cohort of farmers or a small cohort of clinician or a small cohort of, say, radio teams, immediately there's an insatiable appetite from the community because they have been longing for tools like these.
[2322.74 → 2325.36] So there is a thin line.
[2325.36 → 2329.98] The lines are very blurred on how we've been developing with some of these.
[2330.20 → 2332.02] It is really hands-on deck.
[2332.68 → 2335.96] You're working with tools that are reaching directly to the communities.
[2336.52 → 2343.36] And of course, that had been earlier sort of permeated within some of the principles for the lab or for the group, actually.
[2343.36 → 2347.36] And I think also the group draws a lot of that from the university.
[2348.16 → 2357.92] The university, and I'm sure Joyce can talk about this more, from a holistic, you know, macro level, you know, it looks at research, education, but also outreach.
[2358.22 → 2368.64] A very, very strong component of Mario University that you have to have an outreach arm of your research as much as it ties into academia, being an academia hub.
[2368.96 → 2370.84] So there is already a need.
[2370.84 → 2378.14] So once you're working on any technology, no matter how small, you will always end up impacting people.
[2378.34 → 2385.84] There is a very thin membrane between the work that we do, you know, for academia or for school and the people that it impacts.
[2386.02 → 2389.14] So it's a very different ballgame in terms of the setting.
[2389.54 → 2391.20] I hope I've tackled that.
[2391.56 → 2393.86] Yeah, thank you so much for that answer, Manages.
[2393.86 → 2402.72] Really appreciate your perspective there and also emphasizing that no matter what technology we're building, it is going to have an impact on people.
[2402.88 → 2406.62] And we should keep that in the forefront of our minds.
[2407.12 → 2420.90] Well, I'm really just thrilled to have kicked off this AI in Africa Spotlight series on the podcast with this great conversation with Joyce and Manages from the Macarena AI Lab.
[2420.90 → 2437.78] Joyce, I'm wondering if you might close us out by just giving us an idea about what you're excited to talk about and discuss as we have some follow-up episodes about other things that are happening around in different areas and in different ways as related to AI in Africa.
[2437.78 → 2438.98] Yeah, thanks, Danielle.
[2439.26 → 2442.50] So for me, it's exciting, the series that we are going to have.
[2442.60 → 2454.54] One, to really understand, especially the community building, the groups that are out there in Africa that are building communities, that are training communities, that are providing support for communities.
[2454.80 → 2457.88] I think that's going to be very interesting for us to listen to.
[2457.88 → 2468.20] Another interesting thing is to really look at the big problem that we have around the data collection, data curation, making sure that we have data that's not biased.
[2468.36 → 2472.70] I think you hinted a little bit about it in the questions that you ask around how do we deal with biases.
[2473.28 → 2482.12] So for me, it's interesting to hear how other people have been able to deal with that to make sure that the data being collected doesn't have bias, is representative, is inclusive.
[2482.12 → 2484.94] That's interesting for me to hear about.
[2485.10 → 2493.56] A feminist AI is also something that's interesting as well, and I'm hoping that we can be able to hear more about it in the coming series.
[2493.88 → 2496.48] Of course, we are still in the COVID-19 pandemic.
[2496.96 → 2506.60] So also hearing about the work that's being done in the African context around dealing with COVID and integration between using AI for fighting the COVID-19 pandemic.
[2506.60 → 2510.72] I think that's also something that's interesting that I am looking forward to hearing.
[2510.72 → 2514.98] So, yeah, I'm very excited about the next episodes that we are going to have.
[2515.24 → 2515.70] Yeah, thanks.
[2516.04 → 2518.08] Yeah, and thank you so much, Joyce.
[2518.16 → 2520.66] Thank you for agreeing to join us on this journey.
[2520.94 → 2524.66] And thank you, Moves, for joining us in this kickoff episode.
[2525.26 → 2530.76] Appreciate both of you taking time and looking forward to having the follow-up conversation soon.
[2531.12 → 2532.20] We'll talk to you all soon.
[2532.34 → 2532.62] Bye-bye.
[2532.78 → 2533.02] Bye.
[2536.66 → 2537.70] That's our show.
[2537.90 → 2538.54] Thanks for listening.
[2538.54 → 2541.34] For more like this, check out our Master Feed.
[2541.70 → 2545.42] It is all Changelog podcasts in one easy-to-consume place.
[2545.78 → 2550.66] Let your podcast app snag everything we produce and then pick and choose which ones to listen to.
[2551.02 → 2557.02] Subscribe today at changelog.com slash master or just search for Changelog Master in your podcast app of choice.
[2557.28 → 2557.82] You'll find it.
[2557.82 → 2565.32] Special thanks to Break master Cylinder for providing our music and to our longtime sponsors, Vastly, Launch Darkly, and Linde.
[2565.90 → 2567.16] That's all for this week.
[2567.38 → 2568.64] We'll talk to you again next time.
[2568.64 → 2568.86] OK.
[2568.86 → 2576.74] We'll see you again next time.
[2576.74 → 2606.72] Thank you.
