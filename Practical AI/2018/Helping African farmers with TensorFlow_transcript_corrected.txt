[0.00 → 6.70] Bandwidth for Changelog is provided by Vastly. Learn more at Fastly.com. We move fast and fix
[6.70 → 11.42] things here at Changelog because of Rollbar. Check them out at Rollbar.com. And we're hosted
[11.42 → 17.54] on Linde servers. Head to linode.com slash Changelog. This episode of Practical AI is
[17.54 → 23.16] brought to you by Hired. One thing people hate doing is searching for a new job. It's so painful
[23.16 → 28.22] to search through open positions on every job board under the sun. The process to find a new
[28.22 → 33.84] job is such a mess. If only there was an easier way. Well, I'm here to tell you there is. Our
[33.84 → 38.54] friends at Hired have made it so that companies send you offers with salary, benefits, and even
[38.54 → 43.94] equity up front. All you have to do is answer a few questions to showcase who you are and what type
[43.94 → 48.80] of job you're looking for. They work with more than 6,000 companies from startups to large publicly
[48.80 → 53.76] traded companies in 14 major tech hubs in North America and Europe. You get to see all of your
[53.76 → 58.78] interview requests. You can accept, reject, or make changes to their offer even before you talk
[58.78 → 62.58] with anyone. And it's totally free. This isn't going to cost you anything. It's not like you have
[62.58 → 66.42] to go there and spend money to get this opportunity. And if you get a job through Hired, they're even
[66.42 → 70.36] going to give you a bonus. Normally it's $300, but because you're a listener of Practical AI,
[70.72 → 75.64] it's $600 instead. Even if you're not looking for a job, you can refer a friend and Hired will send
[75.64 → 81.38] you a check for $1,337 when they accept the job. As you can see, Hired makes it too easy.
[81.38 → 84.60] Get started at Hired.com slash Practical AI.
[98.84 → 104.26] Welcome to Practical AI, a weekly podcast about making artificial intelligence practical,
[104.68 → 110.16] productive, and accessible to everyone. This is where conversations around AI, machine learning,
[110.16 → 114.30] data science happen. Join the community and snag with us around various topics of the show
[114.30 → 120.12] at changelog.com slash community. Follow us on Twitter. We're at Practical AI FM. And now onto the show.
[122.88 → 131.90] So Chris, I am super excited today. I have seen a lot of amazing things in my life, but this next
[131.90 → 137.56] project that we're going to talk about is really pretty amazing. I think you probably agree with that.
[137.56 → 145.98] Absolutely. Yeah. So we have Amanda, Peter, and Latina with us here. Two joining from Pennsylvania
[145.98 → 152.96] and Latina joining from Tanzania. So the first thing I'd like to do is just have you guys intro
[152.96 → 157.48] yourselves a little bit. Maybe one of you can do that for all three of you. Amanda, do you want to
[157.48 → 164.28] take that? Sure. So hi, everyone. My name is Amanda. I am a postdoctoral research fellow here at Penn
[164.28 → 170.70] State. And I got my PhD in Agricultural Engineering and Computer Science. And I work with Plant Village
[170.70 → 180.02] to design models that diagnose plant diseases on a phone. And with me, I have Pete. Pete is a research
[180.02 → 186.96] technician for Plant Village. And he's my right-hand guy to help us like train the models and test the
[186.96 → 195.22] models. And he also helps a lot with the development on TensorFlow. And with us is Latina. Latina is a
[195.22 → 204.32] grad student out of Tanzania. She works with us. Her field is microbiology. Right, Latina? Did I get
[204.32 → 214.28] that right? Not really. Nope. Nope. Okay. Well, that's what was in the video. It was... So what is your degree in, Latina?
[214.28 → 222.44] Latina. Molecular biology and biotechnology. Yes. Okay. Latina is a grad student in molecular
[222.44 → 229.90] biology and biotechnology. And she's been really, really helpful to us to test the model and how the
[229.90 → 235.72] app works out in the field with scientists, as well as extension workers for agriculture, as well as
[235.72 → 245.30] farmers. Awesome. And did you guys all meet, I guess, you met around this project, right? How did the
[245.30 → 251.32] project get started? And maybe just give us a little bit of an intro on what the project is and what
[251.32 → 260.78] you're trying to do. So the foundation of Plant Village is to make technology available to farmers.
[260.78 → 266.86] So make the latest technology available to farmers to improve food security globally. And one of the
[266.86 → 272.36] technologies right now with the highest potential is artificial intelligence and machine learning.
[273.08 → 279.38] So... And phones are a very prevalent technology right now across the globe. So we wanted to combine
[279.38 → 286.30] those two technologies to create tools that farmers can access to help them grow food better.
[286.30 → 293.80] One of the major crops grown in the world is cassava. And there are many diseases and pests that affect
[293.80 → 302.74] cassava and reduce the yields. So we wanted to combine AI with phones to help farmers grow cassava better.
[303.44 → 309.64] And for those who don't know cassava, could you just mention briefly what that is? Because not
[309.64 → 311.38] everybody in the audience will be familiar with that.
[311.38 → 319.06] I think I would, I would, I'm going to ask Latina, the cassava expert to, to, to define cassava. I think
[319.06 → 320.18] she can do it the best.
[321.18 → 333.14] Okay. Cassava is a root crop, just like potatoes and yams. So here we, we planted to use the roots as
[333.14 → 341.20] source of starch, which you can boil, you can fry, you can mix it up with coconut milk. But also we use the
[341.20 → 348.08] leaves and the leaves, we use it as source of vegetables. So you can basically just boil it and put it in salt
[348.08 → 355.42] and you can eat the cassava and the leaves. But one of the other important uses of cassava is we make
[355.42 → 363.30] the starch into flour, and we cook it in a way that is almost like polenta. And you can have that with
[363.30 → 371.54] any other thing like vegetables and beef and stew or sauces. So it's a it's a root crop that is high
[371.54 → 378.24] content of starch and the leaves are used as source of vegetables for vitamins and other micronutrients.
[378.64 → 380.32] Sounds really versatile then.
[380.62 → 381.24] Yeah, it is.
[381.24 → 381.74] Yeah.
[381.74 → 381.98] Yeah.
[381.98 → 383.82] And you're making, making me hungry.
[383.82 → 393.34] And I haven't eaten yet. And, uh, and I'm, I'm kind of craving some cassava now. Um, so, uh,
[393.56 → 399.10] so yeah, you, you mentioned that, um, you know, you, you want to kind of help, help these farmers,
[399.10 → 407.54] um, in, in the field, uh, grow cassava better. What is kind of the range of diseases that,
[407.54 → 413.76] that affect this plant and how, you know, how are they dealing with these diseases in the
[413.90 → 418.00] in the absence of, you know, the solution that you've developed around AI?
[418.26 → 424.14] So mainly the way cassava is being grown in most of, um, sub-Saharan Africa where we grow it,
[424.64 → 430.68] uh, people just grow it as a crop in the field. So it's a substance called crop, something that can
[430.68 → 436.66] grow it, uproot it within six months, make their flour and have food. But, um, right now it's being
[436.66 → 442.12] commercialized and people are growing it to export and making flowers for export. So the main problem
[442.12 → 447.06] with the diseases that we have that there are a lot of diseases, but the main diseases,
[447.78 → 453.22] the two viral diseases, these are caused by viruses. And one is the mosaic disease. We call it
[453.22 → 458.78] cassava mosaic disease. And basically this affects the leaves of the plants and the leaves become
[458.78 → 464.66] destroyed to a point that it does not make enough food for the plant as it should be when it's healthy.
[464.66 → 469.96] And because it destroys the leaf and the leaf, the plant does not grow very well. It becomes
[469.96 → 475.26] stunted. It doesn't grow and it doesn't produce good roots. So when people come to harvest,
[475.38 → 479.64] eventually they find out they actually don't have enough roots or no roots at all.
[479.96 → 484.34] With the other disease is called the brown streak disease. It's also a viral disease.
[484.84 → 489.44] This affects the leaves too, but the leaves are not destroyed. And what it does,
[489.44 → 496.40] it actually destroys the roots. So when you harvest, you find roots, but when you cut the roots, and they're
[496.40 → 501.90] rotten inside, so they're useless. So it's either you don't have product or you have useless product.
[502.16 → 510.08] So at the moment, there is no viable solution other than identifying the plants that are infected
[510.08 → 518.42] and those that are healthy so that you can plant healthy plants or remove those infected ones so the disease does not spread.
[519.06 → 525.06] But that's where the challenge is. Some of these symptoms for these diseases are difficult to identify.
[525.80 → 534.24] So sometimes people don't know if their plants are infected until when they harvest, and they realize they don't have any products that is useful.
[534.24 → 536.46] Yeah, that must be frustrating.
[537.12 → 547.54] Oh, yes, it is. Because you can lose the whole farm and people depend on cassava for food or source of to sell to get income to for their livelihood.
[548.30 → 552.98] So it would be pretty disastrous for the harvest to fail in that way, right?
[553.14 → 553.54] Yes.
[553.54 → 566.00] And so as we turn toward, you know, how you're what you're doing with this project, you know, what are the goals of the project? And how are you finding that AI has become a useful tool for you in accomplishing this?
[566.00 → 572.12] So one of the main goals is to sort of use AI to democratize access to technology.
[572.84 → 584.26] So the conventional way of diagnosing these plant diseases is for someone with that expertise to go out into the field and look at the plant and tell you what's wrong with the plant.
[584.26 → 589.82] But there's just not enough people in places like sub-Saharan Africa to do that.
[590.24 → 598.86] So what we want to do is put that knowledge and collaborate with the scientists who have that knowledge to input that into a model in a phone.
[598.86 → 607.02] And now farmers can just download an app and then have the eyes of an expert look at their crop and tell them what's wrong.
[607.60 → 608.84] That is so cool.
[609.62 → 610.68] But yeah, that's awesome.
[610.68 → 618.40] So in a sense, the like they're getting that expertise via the model on the phone that they just essentially would not have otherwise.
[619.60 → 620.16] Exactly.
[620.72 → 621.28] Yes.
[621.48 → 627.60] And we definitely work in collaboration with the scientists and experts to create a model like this.
[627.60 → 636.26] I think one of the sort of negative sides of AI is people always saying that, oh, AI is going to take our jobs.
[636.26 → 645.32] But we actually can't build these models without the human experts there to tell us what type of data to collect and how the model should perform.
[645.32 → 647.34] Yeah, that's that's so true.
[647.34 → 652.28] And I definitely think this is a great example of that kind of augmentation.
[652.28 → 652.72] Right.
[652.78 → 656.82] Because you're also you're not creating like a robot farmer.
[656.82 → 657.26] Right.
[657.26 → 661.68] That does all the cassava things with AI and replaces everyone.
[661.68 → 666.72] But really, you're putting expertise into the hands of the farmers in the field.
[666.72 → 672.18] That's really allowing them to improve their quality of life and increase their yield.
[672.18 → 672.48] Right.
[672.48 → 674.30] Yeah, exactly.
[674.30 → 674.50] Exactly.
[674.50 → 675.50] Yeah.
[675.50 → 676.50] Awesome.
[676.50 → 684.16] So how like in terms of I guess we can kind of, you know, steer things a little bit more on the AI side.
[684.16 → 688.92] Now I'm really interested, you know, in some of the technical things around that.
[688.92 → 697.94] First off, I imagine that there was a problem of even, you know, finding cassava data to train your models.
[697.94 → 698.20] Right.
[698.20 → 706.72] How did what was the process like in terms of starting out this project and even just finding the data that you needed to train these models?
[706.72 → 707.60] Yeah.
[707.60 → 720.36] So the data collection process actually, I think, took about two years from the beginning of 2016 through October 2017.
[720.36 → 731.18] So that was just like a kind of mass photograph period where there was at least three trips, one before I came onto the project.
[731.18 → 745.00] And then my first two trips where we just went to Tanzania with some cameras and spent anywhere between like five and eight hours out in the field just photographing leaves.
[745.00 → 757.96] And then my first time was coming back and sorting them out and making sure that like what we were photographing is what or what we thought we were photographing was what it was actually there in terms of like the correct ground truth labels.
[757.96 → 767.80] Because that's one of the more difficult things, too, when you're dealing with any type of, you know, health or sciences, especially plant sciences.
[767.80 → 780.88] Correctly labelling the data is really, really difficult process because of the different symptoms looking differently on different varieties and at different stages of the infection.
[780.88 → 784.30] They look different as well as having like coinfection.
[784.48 → 785.74] So how do you deal with that?
[785.74 → 800.30] And so that I would say the data collection process was probably the biggest, most intensive, hardest part of this project because there is just like no publicly available, especially cassava data.
[800.44 → 803.68] But generally, like plant disease data sets are not publicly available.
[804.14 → 813.06] And then so we had to build our own and then go through all the, you know, the troubleshooting and difficulties that are there come along with building your own data.
[813.06 → 815.34] So a couple of follow-up questions on that.
[815.34 → 820.72] First, what kind of sample size did you have in terms of how big was the data set that you used of those leaves?
[821.48 → 829.40] So the data set that we use for the final model or that we're using now is made up of about like 2200 images, I think.
[830.48 → 839.22] But like our entire cassava data set, I think, has somewhere between 15 and 8, 10 and 15000 images.
[839.22 → 849.52] But like I said, like not all of those images are useful because it could be incorrectly labelled or because they're just a bad style of image.
[849.52 → 857.36] So we really only have about like 22 or 2500 really high quality images that we can build a model with.
[857.36 → 861.86] So it was it was it challenging given the fact that it takes that expertise?
[862.12 → 866.58] You know, this is a domain expertise that that most people don't have for the labelling.
[866.58 → 876.80] So whereas in other projects not like this, you know, you can kind of outsource some of that labelling if it's something that that your typical layperson could address.
[876.80 → 881.04] But I imagine that recognizing the disease states took some level of expertise.
[881.24 → 883.12] How did you approach that?
[883.66 → 889.26] So that's where IIT comes in, and they are the cassava experts for us.
[889.32 → 896.40] And so we in October sat down with, I think, three cassava experts and went through the data set.
[896.82 → 905.20] And because so they give us the so when we go out and collect the data, we go out with a cassava expert, and they point us to like, OK, this is what this virus looks like.
[905.20 → 907.32] All of these leaves are infected with this.
[907.86 → 916.62] So during the whole process of the data collection, the IATA cassava experts are there with us making sure that we're we're getting the right data.
[917.04 → 918.56] And so IATA.
[918.66 → 919.22] Yeah, go ahead.
[919.28 → 920.40] I think that that was my question.
[921.48 → 921.80] Yeah.
[921.98 → 929.28] So IATA is the International Institute for Tropical Agriculture and their East Africa office is based in Dar es Salaam, Tanzania.
[929.42 → 930.34] And that's where we met.
[930.62 → 930.72] Gotcha.
[931.12 → 931.60] Yeah.
[931.60 → 942.74] Yeah. So in a sense, you're I mean, it wasn't like you went you guys went and then just took a bunch of pictures and then ship the pictures off to some people to identify disease plants.
[942.74 → 948.12] But you kind of did it on the fly in the field saying, you know, this is a disease plant at this stage.
[948.12 → 952.86] I'm going to take a bunch of pictures of it so that I, so I know those are labelled correctly.
[953.02 → 954.68] Is that kind of right?
[955.08 → 955.48] Yes.
[955.96 → 957.28] Yeah, exactly.
[957.28 → 966.80] It's part of a bigger, bigger role of Plant Village to sort of have a data set of images of all the plant diseases of the world.
[967.24 → 967.50] Awesome.
[967.62 → 976.06] Are there other existing data sets that kind of fit into this the same category of disease plants?
[976.22 → 978.50] I'm just not, not familiar enough.
[978.66 → 978.90] Yeah.
[979.14 → 979.54] That field.
[979.54 → 981.64] There are.
[981.74 → 988.18] There are a number of different international organizations that keep databases like this, but they're not open access.
[988.58 → 988.84] Gotcha.
[989.26 → 989.48] OK.
[989.62 → 992.62] And is this Cassava data that you're producing?
[992.84 → 994.54] Is that going to be available publicly?
[995.64 → 997.84] That's sort of yet to be determined.
[998.06 → 1001.18] We're definitely sharing it with researchers for research purposes.
[1001.68 → 1005.72] But whether it'll be publicly available, I'm not sure yet.
[1006.34 → 1006.88] Right.
[1006.88 → 1012.46] We're definitely open to sharing the model and the weights on the model.
[1013.94 → 1018.74] So we can because we're making the model openly available and free.
[1019.06 → 1019.84] That's awesome.
[1020.08 → 1020.24] Yeah.
[1020.74 → 1021.10] Yeah.
[1021.56 → 1021.82] Yeah.
[1021.82 → 1022.66] That's that's great.
[1022.76 → 1031.58] So even if people, you know, wanted to integrate, you know, Cassava intelligence into other apps, at least that at least that model would be out there.
[1031.58 → 1031.90] Right.
[1032.66 → 1033.14] Exactly.
[1033.46 → 1033.60] Yeah.
[1033.60 → 1034.42] That's that's awesome.
[1034.42 → 1041.52] And in terms of I mean, you guys mentioned the importance of mobile devices in this process.
[1041.52 → 1051.22] You know, could you explain a little bit more maybe like why mobile devices were the target device for this work?
[1051.22 → 1062.10] And then maybe someone can share as well, like what how you eventually landed on TensorFlow as the framework that would allow you to kind of target that device.
[1062.10 → 1062.60] Right.
[1062.60 → 1063.10] Right.
[1063.10 → 1069.28] So mobile is sort of is emerging as the most ubiquitous platform for technology.
[1069.98 → 1074.78] It's also the great thing about an app is that you can run it offline.
[1074.78 → 1078.30] And in a lot of these farms and these locations, there's no Internet access.
[1079.30 → 1081.58] Farming is done in usually rural locations.
[1081.58 → 1091.48] So we had to sort of set our restrictions there for meeting the population of users that we wanted to use this technology.
[1091.48 → 1093.78] So that's why we chose mobile.
[1093.78 → 1097.10] And then what was your second question?
[1097.10 → 1097.94] Yeah.
[1097.94 → 1098.32] So.
[1098.32 → 1101.46] So, yeah, my second question, that's that's great.
[1101.46 → 1112.56] I definitely figured that would be the answer as far as, you know, the access to computing devices, but also kind of the connectivity and all of that.
[1113.52 → 1125.64] What I mean, given that you knew that you were targeting the mobile devices in terms of the actual like, you know, enabling the model to run on the mobile devices and all of that.
[1125.64 → 1130.62] What were the particular challenges and solutions that you found to those?
[1130.62 → 1134.32] You know, I know like maybe battery usage is a thing.
[1134.32 → 1141.46] I know I can, you know, I can run, you know, Slack and watch a couple of YouTube videos on my phone, and then I have to I have to charge it.
[1141.46 → 1141.72] Right.
[1141.72 → 1147.18] So maybe there's like what were the particular challenges that you found with that?
[1148.14 → 1148.70] Yeah.
[1148.88 → 1156.64] So definitely the first model iterations that we did when we took it out in the field, the phones just got so hot so fast.
[1156.92 → 1160.24] And then the inference times slowed down considerably.
[1160.62 → 1162.24] And again, the battery was draining.
[1162.48 → 1170.10] So we had to kind of step back and think, OK, we need a different model design to work in these conditions.
[1170.32 → 1173.60] And that's when we moved from classification to object detection.
[1174.60 → 1182.32] With the new object detection models, the inference time stayed low, and the phones didn't heat up as fast.
[1182.32 → 1185.38] And the battery didn't drain as quickly.
[1185.38 → 1188.18] So that was a big change that we had to do.
[1188.18 → 1200.66] And what was really nice about the object detection was it when you can really see how the model is working because it draws these boxes around what it is classifying as a specific disease or problem.
[1200.66 → 1204.90] So in a way, it's also teaching people using the app.
[1205.14 → 1206.52] This is what I'm looking at.
[1206.58 → 1208.38] And this is what this disease is.
[1209.58 → 1221.58] Yeah, that's that's fascinating that, you know, you started out actually thinking it sounds like you started out thinking like, oh, the thing to do is just really to tell them like disease or not like classification.
[1221.58 → 1236.48] But really, you found a lot of value both operationally and like in terms of teaching the people more and bringing that intelligence to them as far as just detecting objects and disease portions of plants.
[1236.48 → 1237.70] That's that's fascinating.
[1238.36 → 1240.22] Yeah, it was a win-win.
[1240.22 → 1251.12] One of the things I was under I was curious about is as you is you got out and did this and had to select the devices and your computation and memory and stuff on it.
[1251.24 → 1259.24] What did you run into from an inference standpoint in terms of like, you know, not every mobile device can support inferences.
[1259.24 → 1269.90] And in terms of computationally, what how did you go through the process of saying these mobile devices are in or these are not, or you selected a particular one?
[1269.90 → 1271.00] And how did you approach that?
[1271.10 → 1272.64] And what were the constraints that you faced?
[1272.78 → 1272.94] Yeah.
[1273.12 → 1278.26] So earlier this year, we went out and tested a number of different mobile devices to see how they did.
[1278.84 → 1284.44] And we were actually pleasantly surprised that so the app that we have is compatible with Android 5.0 and above.
[1286.38 → 1295.88] And there was a range of performance between the older mobile phones to the newer ones, but they weren't as wide a range as we expected.
[1296.68 → 1298.60] So they did a pretty good job.
[1298.60 → 1303.10] So we kind of further tested the app with a mid-range phone.
[1305.02 → 1311.02] We did see a lot more variability in with the response of the camera to how they did.
[1311.02 → 1323.12] But one of the variables that we're interested in is whether the app is misdiagnosing or not diagnosing at all, because if it's not diagnosing at all, that's OK, because we can design around that.
[1323.46 → 1327.32] But if it's misdiagnosing based on different phones, then that's a huge problem.
[1327.32 → 1336.28] So then we start to get more nuanced into, OK, what are the metrics that we're going to use to really evaluate the app on different phones?
[1336.28 → 1340.32] Because it's not all equal, and it's not going to be perfect.
[1341.02 → 1343.94] So what do we want to sort of aim for?
[1343.94 → 1353.60] And we were aiming for more false negatives as opposed to false positives in the way the app performs.
[1354.06 → 1356.66] And do you want to add to that a little bit?
[1357.20 → 1362.70] Yeah, it's just kind of along the lines of we would like the model to be more conservative in its predictions.
[1362.70 → 1369.26] And instead of saying the wrong thing, it will just say, I don't know, or I'm not confident enough or look at more.
[1369.70 → 1372.80] Yeah. Yeah. Show me another leaf that maybe has more symptoms.
[1373.18 → 1377.52] Because when a human goes out into the field, they don't just look at one leaf and tell you your problem.
[1377.52 → 1380.28] They're looking at the whole plant, the whole field.
[1380.28 → 1392.74] And people tend to be more conservative about how they, you know, tell somebody bad news as opposed to being like, well, I'm just going to tell you all the possible problems you have out there, and I'm not sure.
[1392.88 → 1398.04] So we wanted our model to sort of replicate being conservative.
[1398.04 → 1415.18] So as you were having to go through and decide exactly what the architecture of your model would be, and you know that you are deploying it into, you know, an area where you have a lot of mobile constraints around it, both from the device itself and maybe from the environment.
[1415.90 → 1425.52] How did that affect the decisions you made on what architectures to go with, whether you could utilize transfer learning or not, how many layers, that kind of thing?
[1425.52 → 1428.80] How did the environment affect your modelling decisions?
[1429.48 → 1440.66] So definitely we had to use transfer learning because there was no way we can collect that many images to train a model from scratch with these specific classes, disease classes.
[1440.66 → 1442.42] There's just not enough data out there.
[1442.46 → 1443.64] It'll take a really long time.
[1444.40 → 1451.52] But then we were really constrained to the mobile net architecture because, you know, the inference time is the shortest.
[1451.90 → 1453.26] It ran the fastest.
[1453.26 → 1460.52] We've also tried, and we're continuing to try different ways to shrink other more complicated, deeper models.
[1461.24 → 1466.48] But we really got a good performance with the mobile net architecture.
[1466.78 → 1468.76] Like it really worked for our test case.
[1469.00 → 1478.36] So we didn't have to do a lot of extensive testing of different architectures for this specific Cassava problem.
[1478.36 → 1486.28] Did you have to remove layers or anything just given the vast number of layers in mobile net or anything?
[1486.40 → 1490.42] Are we able to just take it as is, transfer that over and then train on top of it?
[1490.72 → 1491.80] We did exactly that.
[1491.80 → 1497.80] We took it as is, transferred over and trained and did transfer learning on the mobile net model.
[1497.80 → 1506.22] And it's vastly better than when we first started off with the Inception v4 model to do classification.
[1507.02 → 1509.14] It was much more robust on a mobile device.
[1509.92 → 1510.98] Yeah, that's that's awesome.
[1511.14 → 1513.30] And that's great to that's great to hear.
[1513.30 → 1522.62] You know, it definitely seems to be there 's's more and more, you know, I remember there are a lot of pre-trained models out there.
[1522.70 → 1526.00] There are a lot of different architectures, you know, used to it.
[1526.00 → 1533.78] It was pretty hard for me to kind of go through that process of just getting a kind of off the shelf model and having it perform well.
[1533.78 → 1536.40] But I think, you know, that's that is changing.
[1536.40 → 1545.16] And especially with, you know, a lot of stuff I heard around TensorFlow estimators and other things at at at TensorFlow Dev Summit.
[1545.34 → 1552.52] I know that there 's's a lot of emphasis on that sort of that sort of application, which is really great to hear.
[1552.98 → 1554.64] So kind of.
[1554.64 → 1554.94] Yeah.
[1555.10 → 1560.48] Speaking of, you know, speaking of TensorFlow Dev Summit, which is where I met you guys.
[1560.48 → 1571.46] Just to be real, real here, if is Jeff Dean featured my project in his talk, I think I would like to flip out.
[1571.62 → 1572.42] What was that like?
[1574.32 → 1574.98] All right.
[1575.06 → 1575.84] Full disclosure.
[1576.04 → 1577.86] I was like, wait, who's Jeff Dean?
[1577.96 → 1578.46] What's happening?
[1578.78 → 1578.90] Yeah.
[1578.90 → 1581.36] And then Pete's jaw just dropped.
[1581.46 → 1582.82] He's like, what is wrong with you?
[1586.20 → 1589.18] You guys, you guys are just so wrong.
[1589.18 → 1592.34] Like you're all about, you know, saving the world with A.I.
[1592.74 → 1596.36] And Jeff Dean is just tagging along and trying to.
[1600.40 → 1611.46] It was actually pretty funny for me because so my brother is working at Google now, and he is working in the Google brain, you know, part of it with A.I.
[1611.46 → 1614.70] And works several levels underneath Jeff Dean.
[1614.90 → 1619.92] And I was so I guess they were streaming the summit around the Google offices.
[1619.92 → 1622.80] And my brother was texting me like, oh, my God, I'm so jealous.
[1622.86 → 1624.50] You just got a shout-out from Jeff Dean.
[1624.50 → 1625.90] Like, that's so crazy.
[1626.30 → 1628.76] And then I was like, yeah, this is awesome.
[1628.76 → 1636.96] And then we actually got to talk to Jeff for like a solid 20 minutes after sometime, you know, during the summit.
[1637.44 → 1639.84] And that was just like unreal.
[1639.84 → 1651.24] So, yeah, it was super validating because we were really able to talk to him, get all geeky about the models and how the models perform and the performance metrics.
[1651.24 → 1656.34] And we were able to relate a lot to the work that we were doing because he does a lot of work with health data.
[1656.34 → 1661.94] So, yeah, so it was like, OK, like we're on the right track.
[1662.48 → 1663.32] That's awesome.
[1663.58 → 1665.88] If we can hold a conversation with Jeff Dean.
[1666.02 → 1666.30] Great.
[1666.64 → 1666.86] Yeah.
[1666.88 → 1669.20] I mean, just like incredible stuff.
[1669.20 → 1677.26] And of course, we'll put the'll put the link to the video, the featured video and his talk in the show notes for everyone to see.
[1677.82 → 1679.16] But that's just super cool.
[1679.38 → 1682.26] And so it was so awesome to see all of you guys there.
[1682.26 → 1694.26] And are you getting is Google kind of other than kind of, you know, featuring you and kind of bringing some publicity around it?
[1694.42 → 1700.48] Were you able to kind of like foster some collaboration with Google on the project?
[1701.36 → 1702.08] Yeah, definitely.
[1702.76 → 1710.94] There are some of the engineers at Google are a bit are like our mentors when we run into problems, and we want to we have different challenges.
[1710.94 → 1715.56] There 's definitely a handful of engineers there that I reach out to get their thoughts.
[1716.16 → 1717.98] They're super helpful all the time.
[1718.06 → 1719.26] They respond really quickly.
[1719.86 → 1723.66] They're really they really like this project and like to help us out.
[1724.24 → 1725.26] Yeah, that's that's great.
[1725.34 → 1730.68] And I don't necessarily bring that up to, you know, to advertise Google.
[1730.68 → 1738.86] But I think it's great that they're supporting projects like this, which like you mentioned before, there's a lot of emphasis on, you know, malicious AI and all sorts of things.
[1738.86 → 1755.48] But this is so awesome to see, you know, see a project like this and see, you know, kind of at least some level of support, you know, in among major industry companies around this sort of thing, which is just really encouraging.
[1755.48 → 1758.14] Yeah, I definitely want to shout out to Pete Warden.
[1758.22 → 1763.80] Pete Warden's been super helpful and is a really great resource to us here at Plant Village.
[1764.08 → 1764.42] Awesome.
[1764.66 → 1764.88] Yeah.
[1765.32 → 1768.26] So we really appreciate his expertise.
[1768.72 → 1768.92] Yeah.
[1769.20 → 1769.60] Awesome.
[1769.74 → 1770.42] Awesome work.
[1770.86 → 1773.86] And Latina, I want to follow up with you.
[1773.86 → 1788.84] I was wondering if you could just kind of describe a little bit how is the app currently being used in the field and what are kind of the next steps to get, you know, cassava farmers using all using the app, which I don't know.
[1788.90 → 1789.90] Does the app have a name?
[1790.54 → 1791.88] Maybe you can share that as well.
[1791.88 → 1792.46] Yes.
[1792.68 → 1801.62] The app is called Guru, which is a Swahili word name, rather a female name for it means light.
[1801.62 → 1809.96] So we use Guru as a light that the farmers can use to look at the disease.
[1810.12 → 1812.20] I mean, look at their plants and their farming.
[1813.08 → 1813.76] So, yeah.
[1815.12 → 1815.42] Awesome.
[1815.86 → 1816.02] Yeah.
[1816.08 → 1823.72] And are people using the app now in the field or is it kind of in alpha beta version?
[1824.18 → 1825.76] Do people have access to it now?
[1826.56 → 1827.66] No, not yet.
[1827.66 → 1830.86] We are sort of in our beta version.
[1831.62 → 1835.42] And ideally, we will start the thing.
[1835.62 → 1842.18] We can't get to every farmer because not every farmer can afford a smartphone at the moment.
[1842.18 → 1850.40] So we start working with extension offices, agriculture extension offices up to village levels who actually work with farmers.
[1850.40 → 1859.34] So if we get to one extension office, we'll probably be able to get to 10 to 50 farmers, depending on the size of the village.
[1859.86 → 1863.14] So our aim is to actually get it to the extension offices.
[1863.14 → 1872.84] And as more times go and farmers be able to get smartphones, then we'll be able to now get to farmers directly.
[1872.84 → 1888.66] So Latina, they recently did an experiment with testing how Guru did compare to scientists and extension officers and farmers in a district in Tanzania.
[1888.76 → 1891.86] So I don't know if Latina, you want to kind of share those preliminary results.
[1891.86 → 1894.10] I think that was really exciting to see that.
[1894.34 → 1897.88] So it's quite interesting, actually, because the experts.
[1898.86 → 1903.38] So I did we did a study with about 10 experts, so groups of 10.
[1903.92 → 1911.78] And the experts, even though they're experts, their ability to identify the different diseases also varies.
[1911.78 → 1921.44] And mainly it varies on how exposed they are to the symptoms, to the variety, and how long they've been working in the area.
[1922.18 → 1927.26] And then when you go to extension offices, the agricultural extension offices are more or less the same.
[1927.62 → 1933.56] If they have been exposed to these diseases, then they're more inclined to know and understand them.
[1933.82 → 1940.80] But those agricultural extension offices who have not been exposed to the diseases, they actually are sort of clueless.
[1940.80 → 1943.58] And more or less the same for the farmers.
[1944.08 → 1959.04] So having a tool that it can educate and aid extension worker to be able to do his job and help the farmers is going to help a lot more than just helping them to identify the diseases.
[1959.04 → 1965.10] It's also teaching them and giving them more expertise while they are learning and using the app.
[1965.38 → 1966.80] That is super cool.
[1966.80 → 1972.54] I guess as we start finishing up here, I wanted to ask all three of you to kind of hop in.
[1972.92 → 1986.74] And, you know, we hear so much these days in AI about people's concerns and worries and kind of the downside of what AI may bring to humanity and to the world at large.
[1986.74 → 1990.64] But, you know, you guys are in the middle of doing some pretty amazing stuff.
[1990.80 → 1999.34] I just want to get a sense of what it feels like to know that you've been successful using AI in these contexts and how people react to that.
[2000.20 → 2001.46] Yeah, I think so.
[2001.74 → 2002.48] Yeah, I can start.
[2002.66 → 2005.18] I think it's I mean, we're all so surprised.
[2005.18 → 2005.82] Like what?
[2005.92 → 2006.34] It worked.
[2010.14 → 2013.94] Did you think it was a did you think it was a long shot when you started out?
[2014.20 → 2015.12] I just didn't know.
[2015.18 → 2015.70] Nobody else.
[2015.84 → 2018.58] Nobody else sort of did this very specific project.
[2018.58 → 2024.76] So a lot of the research data sets in computer vision have, you know, a thousand classes or 80 classes.
[2025.18 → 2034.26] And we were really honing in on a very specific classes, a very small data set, and then putting it onto a phone and testing it in a field.
[2034.42 → 2037.08] So it was very much applied and real.
[2037.20 → 2038.76] You couldn't get more real world than that.
[2038.76 → 2046.80] And I'm like, I don't I don't know if it's really going to work as well as all these super high metrics that people report in the research.
[2047.44 → 2049.74] So it isn't in the real world.
[2049.80 → 2054.94] It isn't as high as 90 percent accuracy, but it's still pretty good and it's still useful.
[2055.56 → 2058.70] So, you know, that was that's just great news.
[2058.76 → 2062.50] And I think that I'm I'm I'm just naturally a cautious person.
[2062.82 → 2064.96] I'm always sort of looking for the nuance.
[2064.96 → 2066.64] OK, where the model does well, that's great.
[2066.70 → 2067.94] But where does it not do well?
[2067.94 → 2069.60] And where can we continue to improve?
[2069.60 → 2085.58] And I would like that as we talk about AI in society and AI for good, that we start having much more nuanced arguments than, oh, it's going to like to destroy our lives, or it's just going to like to make every change our entire world.
[2086.18 → 2089.92] I think we need to just get more nuanced into how we think about technology.
[2091.88 → 2093.56] Peter Latina, what do you think?
[2093.56 → 2103.22] Yeah, for my end, I think I'm still I still have a streak alive where every single person I've ever told about this project has responded with.
[2103.56 → 2105.32] That's the coolest thing I've ever heard.
[2105.72 → 2118.78] I can't believe that like you're you're using your skills and your resources to like help, you know, help these people in Africa and not just like creating cool filters for Instagram.
[2118.78 → 2134.94] You know, and so that's been like just the most rewarding thing for me to know that like what I'm doing is really meaningful and like could eventually like to change the lives of millions of people.
[2134.94 → 2145.82] So but I think it's really important to like reemphasize that like we are we're building a tool that helps people be better at their jobs.
[2145.82 → 2151.40] And we're not building a robot to take over their jobs and do all the farming for them.
[2151.40 → 2159.24] We're just trying to help them produce more food and live better lives that and and and sort of adapt to that.
[2159.44 → 2165.04] And like our end goal is really to just like to teach farmers and spread knowledge.
[2165.24 → 2170.22] And so we'll, you know, they'll use our app, you know, for a couple of months or a year, a couple of seasons.
[2170.22 → 2176.40] And then hopefully they know, you know, what the disease symptoms look like, and they don't need our app to show them.
[2176.88 → 2181.70] And so then we're like educating farmers and eventually putting them off on their own.
[2181.78 → 2185.68] And so they don't, you know, rely on us anymore, and they can provide for themselves.
[2186.64 → 2188.92] That's super cool. Latina, how about yourself?
[2188.92 → 2204.36] Um, for my side, this is like quite new, particularly in Africa, where when you talk about AI technology, mobile devices, the mass are more aware of Facebook and Instagram.
[2204.36 → 2218.92] And when you have a tool that can be used positively and has a lot of impact in people's life, it's plus for everyone.
[2219.32 → 2232.60] And what Guru is doing at the moment is helping us as researchers and scientists share our knowledge with the farmers, with the end users,
[2232.60 → 2236.12] because we actually need them to see what we see.
[2236.26 → 2238.36] We need them to see the diseases that we see.
[2238.70 → 2253.36] So we are using Guru to help us portray our knowledge into the farmers so that they can be able to improve their farming practices using the research that has been done and has been proven.
[2253.36 → 2265.96] So when you have a tool like that, a tool that can integrate what the experts know what the end users need and improve their way of life,
[2266.02 → 2269.26] and it actually fits in the way they lead their life.
[2269.26 → 2275.00] It's a tool that can actually work and will be able to sustain in the system.
[2275.52 → 2286.08] And it paves a way into other researchers using AI and the same technology to also follow the same practice to generate products that can help people.
[2286.16 → 2291.90] Because at the end, you might have good products, but they do not fit in the way in people's lives.
[2291.90 → 2295.46] And now people will start getting scared that, oh, do you want to replace us?
[2295.80 → 2305.30] But now we are fitting the technology into people's lives, and that gives them a bit of confidence, a boost, and also comfortability in actually using the tool.
[2305.66 → 2311.44] So I think we are moving to the right direction, and I'm so excited and looking forward to seeing where this can go.
[2312.40 → 2313.24] That's awesome.
[2313.80 → 2316.08] And I am super inspired.
[2316.08 → 2327.64] I think I should just take that recording of what Latifah just said and make sure that everyone in industry listens to that at least once.
[2328.18 → 2338.82] So such a great and inspiring challenge and encouragement as far as the talents that we have
[2338.82 → 2347.28] and the way that they can make an impact, a real impact on people around the world is just super encouraging and inspiring.
[2347.28 → 2352.56] And I think that person making the Instagram filters is crying right now.
[2354.10 → 2362.56] Well, maybe they'll just make an Instagram filter now that detects cassava plants and labels them.
[2362.56 → 2368.10] So the next tie-in is the Instagram plug-in.
[2370.02 → 2379.70] But I know we're kind of wrapping up, but I know before we jumped on the recording here, I know, Amanda, you were talking.
[2379.82 → 2384.72] You were just super excited about next steps and really just viewing this as the beginning.
[2384.72 → 2391.78] Do you want to kind of close us out by just mentioning some of the future directions that you guys are excited about
[2391.78 → 2396.26] and maybe other challenges that people could get involved with as well?
[2396.74 → 2396.94] Yeah.
[2397.04 → 2405.92] So we're really excited about getting the app out to people, to farmers, to use, to test, to give us feedback on what works and what doesn't work for them.
[2406.46 → 2408.84] Building an app like this is a really iterative process.
[2408.84 → 2413.96] We don't really expect to get it right the first time, but we really would appreciate as much feedback.
[2414.38 → 2415.90] The earlier we get it, the better.
[2416.54 → 2422.74] And we're also going to be using this technology to diagnose diseases and pass in other crops.
[2423.16 → 2426.42] Crops like wheat, like corn we're moving towards.
[2426.68 → 2428.80] Potato is another crop that we're interested in.
[2429.30 → 2435.60] And we're always excited to hear from people about what problem they think that this technology would be perfect for.
[2436.12 → 2438.34] We're also continuing to publish our research.
[2438.34 → 2452.58] We're going to have a paper out soon with these results from testing the app in the field and providing much more metrics than what's conventionally provide to show people where the app does well and where it doesn't.
[2452.68 → 2456.92] Again, going more towards the nuance of performance in a real world setting.
[2457.90 → 2459.44] And yeah, that's about it.
[2459.78 → 2460.06] Awesome.
[2460.34 → 2465.16] Well, we'll post some links to some of those things in our show notes.
[2465.16 → 2469.34] Definitely, you know, keep up with what this team is doing.
[2469.56 → 2470.36] It's awesome.
[2470.70 → 2471.68] Awesome to hear.
[2471.90 → 2475.36] And just really appreciate you guys taking time to join us.
[2475.58 → 2477.72] And it's just so great to talk to you.
[2477.80 → 2478.60] Thank you so much.
[2479.12 → 2480.28] You've really inspired us.
[2480.62 → 2480.96] Thank you.
[2481.02 → 2484.12] I'm always excited to talk about technology and agriculture.
[2484.12 → 2487.82] And when people are interested in food and farming, that makes us super happy.
[2488.16 → 2488.56] Awesome.
[2488.56 → 2489.16] Awesome.
[2490.10 → 2491.32] Well, thank you guys again.
[2491.56 → 2494.68] And I hope to keep up with what you're doing.
[2495.14 → 2495.58] Thank you.
[2495.68 → 2496.70] Thank you so much.
[2496.70 → 2499.16] All right.
[2499.20 → 2501.84] Thank you for tuning into this episode of Practical AI.
[2502.10 → 2503.58] If you enjoyed the show, do us a favour.
[2503.68 → 2505.06] Go on iTunes and give us a rating.
[2505.38 → 2507.20] Go in your podcast app and favourite it.
[2507.30 → 2510.02] If you are on Twitter or social network, share a link with a friend.
[2510.10 → 2512.46] Whatever you got to do, share the show with a friend if you enjoyed it.
[2512.76 → 2515.44] And bandwidth for Changelog is provided by Vastly.
[2515.44 → 2516.98] Learn more at Fastly.com.
[2517.22 → 2520.38] And we catch our errors before our users do here at Changelog because of Rollbar.
[2520.60 → 2523.00] Check them out at Rollbar.com slash Changelog.
[2523.00 → 2525.80] And we're hosted on Linde Cloud Servers.
[2526.12 → 2527.76] Head to Linode.com slash Changelog.
[2527.86 → 2528.32] Check them out.
[2528.38 → 2529.22] Support this show.
[2529.62 → 2532.80] This episode is hosted by Daniel Whiten ack and Chris Benson.
[2533.32 → 2534.74] Editing is done by Tim Smith.
[2534.98 → 2537.02] The music is by Break master Cylinder.
[2537.36 → 2540.84] And you can find more shows just like this at ChangeLog.com.
[2540.84 → 2543.00] When you go there, pop in your email address.
[2543.30 → 2549.32] Get our weekly email keeping you up to date with the news and podcasts for developers in your inbox every single week.
[2549.72 → 2550.48] Thanks for tuning in.
[2550.64 → 2551.40] We'll see you next week.
[2553.00 → 2582.98] We'll see you next week.
