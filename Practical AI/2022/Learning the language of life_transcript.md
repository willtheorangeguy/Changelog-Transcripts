[0.00 --> 22.10]  AI has penetrated biotech before. It failed. It failed because of the data. But we have shown proof of concept that this works and it's here to stay. I mean, the advancements that Joshua and the breakthroughs that Joshua presented at NVIDIA GTC conference were the validation that AI is here to stay.
[22.10 --> 35.56]  I mean, being able to predict an antibody that can bind with a particular affinity that you want to the target is like incredible. We're just getting started. And that's the other beautiful part that there's so much more innovation left.
[35.56 --> 58.30]  Welcome to Practical AI, a weekly podcast making artificial intelligence practical, productive, and accessible to everyone. This is where conversations around AI, machine learning, and data science happen.
[58.30 --> 73.36]  Join us at practicalai.fm slash community and follow the show on Twitter. We're at practicalai.fm. Thank you to our partners at Fastly for shipping our pods super fast all around the world. Check them out at fastly.com.
[79.46 --> 88.00]  Welcome to another episode of Practical AI. This is Daniel Whitenack. I'm a data scientist with SIL International.
[88.30 --> 94.56]  And I'm joined as always by my co-host, Chris Benson, who is a tech strategist at Lockheed Martin. How are you doing, Chris?
[94.94 --> 105.70]  I'm doing okay today, Daniel. You know, it's spring and allergies and pollen. And so, you know, I keep taking medicines to try to keep it under control. I'm struggling just a little bit.
[106.28 --> 115.64]  I was going to say tissues, but it's actually a toilet paper roll right here of tissue paper so that if I sneeze from allergies, then I've got that there.
[115.64 --> 120.74]  So hopefully I'll hold off for the episode because we've got a really good one today.
[121.06 --> 128.86]  Yeah, we do. And I just want to say that before we get going, you know, there's some really good meds out there that you might be able to take to help with those.
[129.36 --> 133.06]  Probably some drugs that could be discovered related to allergies.
[133.26 --> 135.62]  And maybe it's something to talk about is all I'm saying, you know?
[135.62 --> 144.14]  Yeah, yeah. Well, speaking of finding me allergy meds or maybe even more important meds because there's more important ones out there.
[144.88 --> 160.80]  Today, this is something our guests have actually or our listeners have requested in terms of guests and topics is something around the topic of AI for drug discovery or other sort of pharma related applications.
[160.80 --> 170.52]  And today we've got Absize founder and CEO Sean McClain and also Joshua Meyer, who is the lead AI scientist at Absize.
[170.68 --> 170.94]  Welcome.
[171.60 --> 174.14]  Yeah. Thank you so much, Daniel and Chris, for having us on the show.
[174.22 --> 178.56]  We're really excited to be diving in with regards to the intersection of AI and biology.
[179.12 --> 181.70]  Yeah, yeah. We're super pumped to have this conversation.
[181.70 --> 191.34]  Maybe to get us started, assuming that maybe a lot of our audience isn't familiar with like the traditional process of drug discovery.
[191.68 --> 195.84]  Could you kind of fill us in in terms of like how are drugs discovered?
[196.12 --> 199.76]  Like typically if we kind of take AI out of the picture, how does that work?
[199.76 --> 202.38]  Oh, it's a very archaic process.
[202.38 --> 211.72]  And I can't tell you how excited I am that actually AI is starting to penetrate drug discovery because it's going to take, you know, from from the Stone Age to the 21st century.
[212.38 --> 216.70]  So if you look at drug discovery in particular with large molecules or proteins.
[216.70 --> 224.28]  And so just for the viewers here, we have really two types of drugs that are out there that have traditionally existed.
[224.28 --> 228.76]  You have small molecules, allergy medicines, Zyrtec that you take.
[229.20 --> 234.78]  And then you also have your large molecules or your biologics, your protein based therapies.
[235.22 --> 238.44]  I'm sure you all are very well aware of like the COVID antibodies.
[238.58 --> 240.68]  So an antibody is a protein.
[240.96 --> 245.58]  And we're really focused on AI drug discovery for protein based therapies.
[245.58 --> 250.28]  And in order to discover these, you have a couple different options to go from.
[250.38 --> 255.78]  You can go, you can take an antigen that you want your biologic to bind to like COVID.
[256.08 --> 260.14]  And you can inject that into a goat or a llama.
[260.66 --> 262.94]  You know, usually these are like humanized animals.
[263.24 --> 271.16]  And then the animals then generate an antibody through their immune system that we then extract out through the blood.
[271.16 --> 277.56]  We purify those and we're able to then take those antibodies and then further develop them.
[277.60 --> 283.98]  Either have it bind tighter to the target, develop it for certain formulation, be able to ensure that you can manufacture it.
[284.00 --> 286.30]  So it's like this very like tedious process.
[286.30 --> 296.00]  And the other option is going from what's called phage display or yeast display where you have a cell that basically puts the antibody on top of the surface.
[296.18 --> 298.58]  You screen it against all these different targets.
[298.76 --> 303.68]  And then you have to then further develop it for manufacturability, developability.
[303.88 --> 307.44]  And it's this like long iterative like process that just takes a long time.
[307.44 --> 312.94]  I mean, it takes years and like billions of dollars invested into getting a drug into into the clinic.
[313.08 --> 315.16]  And then most of the time they failed.
[315.26 --> 316.96]  It's a it's a four percent success rate.
[317.08 --> 320.42]  So even after all that time, all that money, four percent.
[320.60 --> 323.70]  I mean, it's it's it's incredible that like we haven't done better.
[323.96 --> 325.76]  And that's really to me where AI comes in.
[325.96 --> 326.14]  Yeah.
[326.26 --> 331.44]  So speaking of that, maybe, Joshua, if you could give us a little bit of a sense of like,
[331.44 --> 341.54]  what has been the impact of maybe like advanced technology and AI within the sort of drug discovery or bio space?
[341.74 --> 343.40]  Is there a long history with that?
[343.44 --> 345.08]  Is it really just like bleeding edge?
[345.10 --> 346.58]  Like we're just getting into it.
[346.92 --> 350.16]  You know, what's been the history there in terms of what people have tried?
[350.98 --> 351.08]  Sure.
[351.14 --> 352.46]  That's that's a great question, Daniel.
[352.46 --> 359.64]  So at a fundamental level, there's actually a lot of connections between AI and classical ideas and computational biology.
[359.64 --> 366.22]  I used to work at Facebook and I would always joke when we were developing these new AI methods that the biologists really discovered this 10 years ago.
[366.42 --> 376.68]  So at this like fundamental, like mathematical level, there are actually a lot of parallels between the kind of deep learning you're seeing emerging today and what biologists have been have been doing for many years.
[376.84 --> 386.76]  But in terms of actual practical outcomes of deep learning, AI and biology, it's actually been a bit disappointing that until recently you haven't seen a lot a lot of progress.
[386.76 --> 401.40]  And that's really because the lack of data, having a company where you can really integrate cutting edge AI research together with an experimental platform that can create massive amounts of data hasn't really started to happen until very recently.
[401.74 --> 403.04]  And that's what we're building at Absci.
[403.04 --> 414.76]  Is some of that like on the data side, is that also I mean, in terms of patients and biological data, I know that there's like privacy concerns and other things like that.
[414.94 --> 419.02]  Is it a matter of like that side of things like privacy related things?
[419.02 --> 426.28]  Or is it a matter of like you were saying, a platform to kind of like generate data related to these proteins and such?
[426.28 --> 430.06]  Yeah, so the kind of data we're generating is actually at the molecular level.
[430.52 --> 432.94]  It's not data, for example, related to clinical outcomes.
[433.06 --> 434.44]  So privacy is not an issue.
[434.56 --> 440.04]  What we're really getting at here is the fundamental biophysics, like protein protein interactions.
[440.30 --> 442.72]  And we can create that kind of data in the lab.
[442.86 --> 446.32]  You need to see real world examples of that in order to train our models.
[446.78 --> 452.04]  But this kind of data is coming out of cells and labs, and we can generate all that data in house.
[452.04 --> 461.40]  Yeah, and just to hit on that topic just a little bit, AI has like transformed every single industry, really, except for healthcare and biotech.
[461.48 --> 462.14]  And why is that?
[462.20 --> 463.96]  It's because of the lack of data.
[464.20 --> 467.72]  And it's because biological data is messy.
[468.26 --> 469.00]  It's low throughput.
[469.26 --> 470.18]  It's low resolution.
[470.48 --> 471.64]  The quality isn't there.
[472.32 --> 475.60]  And, you know, here at Absci, we've actually we were not an AI first company.
[475.60 --> 482.28]  We were a synthetic biology company that was developing technologies to generate biological data.
[482.96 --> 500.32]  And that's really the reason why we've had the success is because we spent the last 10 years developing technologies that allow you to get the throughput and the quality of wet lab biological data actually needed to train these AI models.
[500.64 --> 502.08]  And that's the most exciting part.
[502.14 --> 504.52]  And we're not the only company doing this.
[504.52 --> 505.36]  There's others.
[505.52 --> 513.14]  And that's why, to me, it's like we have the proof of concept now needed and the data needed to actually start leveraging AI and deep learning.
[513.34 --> 521.20]  And again, going back to all the other industries that have been transformed, once AI penetrates, an industry has transformed in two to three years.
[521.26 --> 528.50]  And I guarantee you, in two to three years, we're going to look back and be like, this has been one of the biggest transformational changes within the industry.
[528.50 --> 537.96]  I got a question. It's a bit of a framing question because I had I've had something in the back of my mind from outside our conversation that I'm trying to kind of connect back in.
[538.02 --> 540.12]  And you can tell me if there's a if there's a role or not.
[540.12 --> 543.84]  We're hopefully coming toward the end of this pandemic period.
[543.84 --> 551.68]  But we've all been learning so much about, you know, drug development and stuff as part of the as a byproduct of this over the last couple of years.
[551.68 --> 553.72]  And we've actually done some shows about that.
[553.72 --> 563.92]  I'm curious, you know, as we're hearing things like messenger RNA along the way as a drug delivery thing, is there a role for how AI impacts that?
[564.02 --> 567.38]  Is that a separate thing? Is that something that's kind of inbound to the conversation?
[567.96 --> 570.54]  I'm just wondering, how do those things fit together, if at all?
[570.70 --> 574.90]  You know, it's really funny you ask that. I was actually just talking to an investor about that yesterday.
[574.90 --> 578.16]  We're actually here in Boston at the Barenberg AI conference.
[578.16 --> 585.46]  And what I told this investor and I'll tell you, it answers your question is absolutely.
[585.84 --> 588.96]  So mRNA is just another way of manufacturing.
[589.18 --> 596.64]  So in order to manufacture a biologic or protein based drug, you have to make it in a living organism.
[596.64 --> 600.44]  We're making it in E. coli cells. Other people make it in mammalian cells.
[600.58 --> 605.36]  But the great thing about mRNA is that you can actually have the body make it.
[605.36 --> 610.02]  So you give the body the transcript in order to make it in the body.
[610.14 --> 619.64]  And so what we can do is develop the antibodies that would then go on to the mRNA, you know, transcript and then put that into humans.
[619.64 --> 623.78]  And you basically use the human body as a manufacturing platform.
[623.78 --> 629.14]  And so it is really exciting technology that is moving forward.
[629.40 --> 635.46]  And AI and the types of technologies we're developing are definitely going to have a huge impact on that.
[636.00 --> 644.78]  In terms of some of what you've touched on as well, I'm wondering, you've mentioned kind of testing and involving animals, testing involving E. coli.
[644.78 --> 654.78]  And like also the fact that after all of this work, you know, only maybe 4% in the traditional case are really making it to launch.
[655.00 --> 667.14]  I'm wondering if you could comment on maybe, Joshua, you have some thoughts on this, like that just how much of the drug discovery process, like as we're looking forward, could happen like in simulation.
[667.14 --> 677.20]  And maybe avoid like bad things that would happen in animals or bad things that would happen in like human trials that are maybe like not successful.
[677.20 --> 684.06]  How much of that risk can we shift in certain ways to computer simulations?
[684.06 --> 685.96]  Just your own opinion on that.
[686.22 --> 690.36]  Yeah, this is exactly what we hope will improve as you start to bring AI into the problem.
[690.36 --> 694.52]  So if you look at traditional drug discovery today, Sean gave a great overview.
[695.16 --> 697.60]  One of my colleagues likes to call it a phishing expedition.
[698.20 --> 701.46]  You're just looking for drugs that seem to do something that seem to work.
[701.64 --> 704.26]  They're not really designed in a data-driven way.
[704.74 --> 706.66]  And that's, again, what we're changing with AI.
[707.18 --> 714.72]  So by using AI and feeding it with the right data, we can actually generate molecules that the machines think have a higher chance of working.
[714.72 --> 720.80]  So instead of just finding something when you go fishing, you can actually build the molecule that you need to solve the problem.
[721.06 --> 728.28]  And we think that's going to result in molecules that tend to bind more tightly to a target or less tightly, depending on what you're trying to do.
[728.34 --> 732.66]  At Absai, we optimize something we call naturalness, how natural an antibody is.
[732.90 --> 736.70]  And we've showed that this score is associated with clinical success.
[736.70 --> 743.74]  So you can look at molecules that have entered the clinic and how they've done in terms of the body accepting or rejecting those drugs.
[744.04 --> 747.08]  And you can see it checking out with the kinds of techniques we're doing here.
[747.30 --> 748.80]  And it all starts, again, with the data.
[748.96 --> 755.74]  We can show our algorithms examples of hundreds of millions of antibody sequences that you see in humans and that you see in animals.
[755.92 --> 759.06]  And that's just one of the kinds of data that we use.
[759.36 --> 766.22]  And generating millions of sequences here that we can use in order to feed these models and show them what makes a good drug.
[766.22 --> 777.50]  One of the dirty secrets in pharma is that a lot of the best drug candidates that have the functionality you want ultimately don't make it into the clinic due to developability concerns.
[777.50 --> 783.86]  You can't produce it at high enough yields or tighter or, you know, you can't formulate it the way that you want.
[783.96 --> 790.26]  And so you're taking a drug candidate that isn't as ideal on the functionality side but can actually be manufactured.
[790.26 --> 797.40]  And with AI and what we're doing, you know, as Joshua was saying, we can go multi-parametric in our models.
[797.62 --> 802.46]  So we're never having to sacrifice functionality for developability or vice versa.
[802.64 --> 807.62]  We're able to hone in on the exact attributes of the drug that we want.
[807.68 --> 812.26]  So, you know, you ultimately get the functionality, you get the developability, you get the manufacturability.
[812.26 --> 827.58]  And that's what's going to increase probability of success throughout the clinic is being able to do that multi-parametric modeling for a particular target, for a particular indication to ultimately increase success rate throughout the clinic.
[827.58 --> 839.84]  I'm wondering, as you're going through these processes and you're doing, you know, this targeted approach across multiple efforts, you know, with different drug targets or however you're doing that concurrently.
[839.84 --> 849.02]  I know to draw another analogy, in kind of manufacturing, there's now the concept of digital twins, digital twinning, as people often say.
[849.32 --> 857.82]  There's an ability to kind of leverage the work and build on it to where you kind of say, you know, maybe in this case, you're digital twinning a molecule.
[858.08 --> 859.76]  Is that a decent way of looking at it?
[859.76 --> 871.92]  I mean, are you doing something along those lines where you're able to kind of create models that then accelerate, where you're able to borrow the digital infrastructure here that we're talking about across different efforts?
[872.28 --> 874.18]  And what would that, what does that look like?
[874.18 --> 878.92]  If so, are you able to build on the shoulders of giants in this capacity?
[879.24 --> 884.16]  I mean, at the highest level, what we're able to do is really search the whole search space.
[884.36 --> 887.74]  And so let's just take a look at an antibody sequence.
[887.74 --> 896.82]  There's more sequence variants in an antibody or different types of drug candidates we could develop than there are atoms in the universe.
[897.36 --> 903.56]  I mean, just think about that for a moment, that the search space and the possible combination of drug candidates is enormous.
[903.76 --> 911.12]  And so even if you have screening capabilities in the billions or trillions, like you're only searching a very, very small fraction.
[911.12 --> 924.38]  And what we're able to do now is actually unlock that whole search space and be able to find the absolute best drug candidate versus, you know, screening a very small fraction of the overall universe.
[924.52 --> 929.52]  I don't know, Joshua, on kind of a technical level on how you want to dive into that, but I'll hand it over to you.
[929.90 --> 930.00]  Yeah.
[930.00 --> 936.80]  Maybe to draw an analogy to digital twins, you can almost think of the models that we're developing as digital twins of what's in the lab.
[937.14 --> 941.54]  Like in a perfect world, you would just run things at like infinite throughput, right?
[941.56 --> 942.78]  But of course, that's impossible.
[942.78 --> 944.28]  There's cost with doing these things.
[944.28 --> 948.34]  And we have extremely ultra high throughput assays at AbSci.
[948.50 --> 952.04]  It still doesn't compare to what you can do in simulation on the computer.
[952.68 --> 960.96]  So one of the things that we do, and one way we measure actually the performance of the models is we ask, how closely does the model recapitulate what we would have seen in the lab?
[961.24 --> 971.10]  And in many cases, we're actually finding that the correlation between different techniques in the lab is almost as good as the correlation between our models and some technique in the lab.
[971.10 --> 977.02]  So basically, the AI models that we're developing are almost as accurate as just like a proxy measurement in the lab.
[977.06 --> 986.44]  And it's really exciting when you think about the ramifications of that, where you really do have this like digital twin that we can really see in various kinds of molecular properties as well.
[986.44 --> 1001.68]  Hello, friends.
[1001.84 --> 1008.34]  Jared here to tell you about Changelog++, our membership program for those of you who want to directly support our work.
[1008.34 --> 1018.56]  Your Plus Plus membership gets you closer to the metal with extended episodes, makes the ads disappear, and takes our audio to the next level with higher bitrate MP3s.
[1018.70 --> 1022.30]  You can join today at changelog.com slash plus plus.
[1022.30 --> 1041.98]  Joshua, I was listening to your talk recently at NVIDIA GTC.
[1042.24 --> 1043.70]  Some really interesting stuff there.
[1043.70 --> 1050.16]  I think one of the pictures that stood out to me was like where you're describing over here, we have a disease, right?
[1050.20 --> 1054.76]  And then you have a pipeline of things and out the end comes a drug.
[1055.06 --> 1058.42]  And, you know, AI is involved in multiple stages of that process.
[1058.42 --> 1073.92]  Could you just, at a high level, give us a kind of picture of what are the different stages along that pipeline from, you know, determining like what disease you're kind of targeting to like out the other end having kind of drug candidates?
[1074.40 --> 1078.84]  First of all, to just describe overall what the pipeline is and the vision we're trying to create here.
[1078.98 --> 1084.98]  We want to be able to go from a disease, from a patient to a drug fully in silico.
[1084.98 --> 1088.44]  And we're building the infrastructure here at Abcide to do that.
[1088.82 --> 1099.72]  So the first step is to take a blood sample from the patient and to be able to computationally reconstruct from the RNA sequencing of the blood the antibodies that the body is naturally producing.
[1100.04 --> 1107.94]  So if someone has a disease, say COVID, the body is going to naturally make antibodies against that, regardless of whether you've had a vaccine or taking an antibody therapy.
[1107.94 --> 1109.26]  You've got these natural antibodies.
[1109.72 --> 1111.84]  And those are potential drug candidates, actually.
[1111.84 --> 1113.50]  So there's some really interesting data there.
[1113.50 --> 1119.98]  But we can use those antibodies in order to figure out what the body is naturally targeting and then develop a drug from there.
[1120.38 --> 1122.04]  So that's the first entry point of AI.
[1122.24 --> 1125.80]  It's going from the blood sample to what is the target that we're trying to hit.
[1125.88 --> 1131.50]  Then from there, we want to take that target, take that receptor, for example, on a cell and develop a drug.
[1131.60 --> 1133.28]  We call that de novo drug discovery.
[1133.40 --> 1137.58]  So trying to get to a starting point drug candidate that binds to the target.
[1137.80 --> 1139.62]  We then do something called lead optimization.
[1139.62 --> 1145.40]  So we try to make that drug bind more tightly to the target or optimize whatever properties we're interested in.
[1145.78 --> 1147.80]  And then the final stage is biomanufacturing.
[1147.96 --> 1155.70]  So unique to Abcci is that all of this data is being generated within a cell line that we developed at Abcci called Solupro.
[1156.28 --> 1159.16]  And Solupro is actually a biomanufacturing machine.
[1159.28 --> 1163.84]  These bacteria that we've created at Abcci basically hacked them to make human protein drugs.
[1163.84 --> 1168.52]  We can actually use them in order to create large amounts of that drug that can then go to the patient.
[1168.88 --> 1172.52]  So you really see AI being introduced across the pipeline here.
[1172.72 --> 1177.54]  And the vision is as you start to build off these AI capabilities, you string them together.
[1177.64 --> 1183.74]  And then eventually you're able to go very rapidly from a disease to a drug at the click of a button.
[1184.48 --> 1185.44]  That's really cool.
[1185.78 --> 1187.56]  I have a follow up for Sean on this.
[1187.56 --> 1189.94]  Both of you weigh in, but I'm curious.
[1190.48 --> 1195.78]  I keep reading about how medicine is becoming more customized to me and stuff.
[1196.16 --> 1204.66]  Do you expect that this process will be able to get, is there too much overhead in terms of needing kind of the generalized data out there?
[1204.78 --> 1214.14]  Or is there possibly a mechanism for which eventually this becomes very custom to individual patients and you can give them the medicines?
[1214.14 --> 1219.20]  I know I've read about that over the years, always as an aspirational thing, but I'm in my 50s now.
[1219.28 --> 1221.60]  So I'm waiting for that to happen as soon as possible.
[1221.74 --> 1222.36]  You know, I'm needing it.
[1222.62 --> 1223.68]  Yeah, 100%.
[1223.68 --> 1225.52]  This is going to lead to personalized medicine.
[1225.74 --> 1228.56]  So let's just fast forward 10 years from now.
[1228.82 --> 1233.30]  We see a success rate go from 4% to 50%, let's say.
[1233.78 --> 1242.58]  And at this point in time, we can go to the FDA and start changing how clinical trials are done and actually have it be personalized.
[1242.58 --> 1257.62]  And it's able to actually occur as well from a cost perspective because you're fully in silico and 50% of the drugs you're designing actually work, which means that it's going to get new drugs to patients a lot faster.
[1258.10 --> 1260.58]  You're going to be paying for less of the drugs that have failed.
[1260.72 --> 1264.84]  So the cost per drug is going to dramatically decrease.
[1265.02 --> 1268.06]  And that altogether is going to enable personalized medicine.
[1268.06 --> 1279.86]  And what's going to be really interesting is I believe that health insurance is going to completely get disrupted as well because the cost has dramatically decreased as well as the speed it takes to get drugs to patients.
[1279.86 --> 1281.00]  And it's fully personalized.
[1281.42 --> 1290.40]  Think of it almost like a SAS model for health care that you have for a lifetime and you're able to get the drugs that are specifically tailored to you.
[1290.74 --> 1294.20]  That's the future that's going to occur within the next 10 to 15 years.
[1294.20 --> 1299.40]  So maybe when you're 60, you'll have personalized medicine delivered to your door.
[1299.64 --> 1301.42]  I'm volunteering to be your first customer.
[1301.52 --> 1302.54]  You can pay that with me.
[1303.22 --> 1310.54]  I'd love to dive into different elements of this pipeline that you described because I find it really fascinating.
[1311.00 --> 1316.18]  So if I understood right, there is this first stage where you kind of extract some blood.
[1316.18 --> 1325.08]  You find these like target antibodies and you mentioned there was kind of this initial discovery phase where AI is applied.
[1325.24 --> 1332.26]  Could you generally kind of give us a sense of like in that stage, kind of what's input and output of the AI?
[1332.40 --> 1340.06]  Like what's the what's the kind of downstream task that the AI is attempting to accomplish in that case?
[1340.70 --> 1340.80]  Yeah.
[1340.80 --> 1345.60]  When you think about an antibody therapy, the antibody is targeting a specific antigen.
[1345.96 --> 1349.42]  So those are the antigen targets that we're starting with in the beginning.
[1349.68 --> 1353.46]  And what we'd like to do is to generate an antibody that targets them.
[1353.56 --> 1357.40]  So that exactly parallels the inputs and outputs of our machine learning model.
[1357.80 --> 1359.84]  The input is going to be an antigen.
[1359.84 --> 1364.06]  So some receptor on the cell that we're trying to hit and the output is an antibody.
[1364.24 --> 1369.86]  Going back to that digital twin example, you can almost think of that model as an AI model of the immune system.
[1369.86 --> 1372.58]  So that's naturally what a body is going to do.
[1372.64 --> 1373.54]  It sees some infection.
[1374.00 --> 1375.40]  It's trying to create some antibodies.
[1375.82 --> 1378.52]  And what we're trying to do here is create a much better version of that.
[1378.56 --> 1383.50]  So to come up with a single antibody drug that can really hit that with the potency that you need.
[1383.76 --> 1386.46]  So that's what you can think of for that first de novo discovery.
[1386.46 --> 1389.52]  It's like that artificial immune system that's creating a new drug.
[1389.52 --> 1390.08]  Yeah.
[1390.36 --> 1404.34]  And this kind of prompts a lot of thoughts in my mind because oftentimes I like when I'm teaching a workshop or something like that, which I do occasionally, oftentimes I get a question of like, what is a good use case for AI and like what isn't?
[1404.90 --> 1410.76]  And oftentimes I frame that in terms of like two factors, both the scale factor.
[1410.76 --> 1414.66]  Like I want to recognize cats in these like billion images.
[1414.98 --> 1418.74]  That's you could do that with a human pretty easily, but the scale is an issue.
[1418.74 --> 1419.06]  Right.
[1419.38 --> 1424.58]  And then secondly, maybe there's a problem that a human like couldn't do right off the bat.
[1424.58 --> 1428.44]  So recognizing a cat in an image is really easy for a human.
[1428.78 --> 1428.98]  Right.
[1429.04 --> 1440.44]  But I'm guessing that like predicting these antibodies in relation to like the target disease, that's like that's something very foreign to like a human brain.
[1440.44 --> 1440.80]  Right.
[1440.84 --> 1445.12]  And there's like all this dimensionality and like related to that.
[1445.34 --> 1450.60]  I don't know if you would you would consider that part of the reason why AI is really applicable here.
[1450.60 --> 1452.30]  But yeah, I don't know.
[1452.36 --> 1460.26]  Could you describe a little bit of that kind of like the dimensionality of the problem that you're working with and like how that factors into this discovery bit?
[1460.46 --> 1464.38]  This is exactly why biology is such a good application of AI.
[1464.74 --> 1471.00]  AI has this property where it's really hard to get it working on the easy problems and a lot easier to get it working on the hard problems.
[1471.36 --> 1473.46]  A clear example of this is self-driving cars.
[1473.80 --> 1477.60]  Something that, you know, most people on the planet learn to do in their lifetime, drive a car.
[1477.60 --> 1482.02]  Or we've been working for, you know, years to create self-driving car technology.
[1482.38 --> 1486.32]  And it's just really hard because the baseline is so good to drive better than a human.
[1486.78 --> 1488.72]  I know that we have accidents, unfortunately.
[1489.20 --> 1492.02]  But to have an AI that's as good as that is actually quite challenging.
[1492.48 --> 1496.60]  But when you go to protein biology, I mean, you and I can't really read protein.
[1496.60 --> 1501.60]  You can't look at the sequences of a protein and like really understand at a fundamental level what's going on here.
[1501.60 --> 1508.34]  But when you show billions of examples of those proteins to a machine learning model, it can start to put together the pieces of the puzzle.
[1508.80 --> 1513.14]  So I think that's one of the key reasons why AI and biology is such an exciting application.
[1513.34 --> 1517.14]  We're just so bad at it today that there's really a long way we can go with AI.
[1518.00 --> 1522.04]  And, you know, we also don't want to offend the medicinal chemists and the protein engineers.
[1522.20 --> 1528.16]  Like there are really good protein engineers that can look at a protein, modify it and help with the functionality.
[1528.16 --> 1539.72]  But getting to your point of like the dimensionality, that's where it's like you can't have someone look at a protein sequence and know the functionality plus the stability plus, you know, how it's going to perform in humans.
[1539.86 --> 1541.80]  And so Joshua is exactly right.
[1542.06 --> 1544.86]  Humans are good at looking at one particular thing.
[1544.92 --> 1548.66]  But then when you look at all these other dimensions, it's impossible to do effectively.
[1548.80 --> 1550.70]  Again, it goes back to that 4% success rate.
[1551.02 --> 1552.62]  Like humans are terrible at it.
[1554.08 --> 1557.98]  Sean, I've also been mulling over your personalized medicine answer.
[1557.98 --> 1559.58]  You really hooked me on that, you know.
[1559.70 --> 1568.76]  And so I'm wondering as we scale this out and in between hearing the scale that Joshua was kind of addressing, is there a notion?
[1569.24 --> 1570.24]  And there may not be.
[1570.32 --> 1571.04]  I'm fishing here.
[1571.34 --> 1586.18]  Is there a notion of this becoming so common as we're looking at personalized medicine that it maybe kind of changes how we perceive medicine in the sense of we eat lots of different foods now.
[1586.18 --> 1589.02]  And we have lots of diversity available.
[1589.56 --> 1596.30]  But we tend to think of medicine, the general population, me, thinks of medicine as this special thing.
[1596.40 --> 1600.74]  And I'm, you know, I get sick and I take a medicine, but I don't do it all the time.
[1600.74 --> 1613.56]  Is there a notion of because it becomes more accessible with this amazing technology that you guys are utilizing that you're able to apply it to more common problems on a day-to-day basis?
[1613.56 --> 1623.36]  And you stop thinking about it as this special thing I'm going to take over there, but it becomes almost like food in that you're optimizing your body's performance at any given time?
[1623.68 --> 1625.16]  I don't know if that makes sense or not.
[1625.36 --> 1627.68]  It totally, it makes a ton of sense.
[1627.68 --> 1636.26]  And I think like the most exciting part about introducing AI to biology is that it's accelerating our knowledge of biology.
[1636.46 --> 1643.78]  I mean, we've already learned things that we as humans had never predicted before that our AI models are predicting.
[1643.78 --> 1652.12]  And so we're going to start getting a much better understanding of our bodies and how, you know, how we should be taking, you know, better care of ourselves.
[1652.12 --> 1658.74]  And so I think it is going to become this like holistic, you know, approach medicine with, you know, the foods you eat.
[1658.80 --> 1663.00]  I mean, what if you, you know, could engineer a grapefruit to produce the medicine you want?
[1663.06 --> 1665.46]  And, you know, there's a lot of really exciting possibilities.
[1665.46 --> 1677.76]  And that's kind of like where you have like AI merging with synthetic biology and AI to me is going to be the engine that generates the drug candidates, you know, the food that we should be eating.
[1677.76 --> 1691.42]  And then it's going to be the actual biology that manufacture it, whether it's like our own human bodies with like mRNA technologies or it's like what Ginkgo Bioworks is doing for manufacturing, you know, new fragrances.
[1691.42 --> 1701.20]  You know, it's a, to me, biology is going to be, or synthetic biology, however you want to phrase it, is going to be the next blue collar job.
[1701.30 --> 1705.92]  Like we're going to be using living organisms to do the manufacturing of the future.
[1705.92 --> 1708.00]  And it's going to be, it's green technology.
[1708.12 --> 1709.12]  It's better for the earth.
[1709.24 --> 1710.06]  It's cheap.
[1710.22 --> 1711.62]  You know, it's going to be cheaper, better.
[1712.00 --> 1721.00]  And so that's the exciting part to me is that it's this whole field, not only medicine, but SynBio, like that's going to be the future of society.
[1721.00 --> 1723.48]  And, and I mean, I'm really excited for it.
[1723.52 --> 1725.90]  I mean, in the next 50 years, seeing what, what occurs.
[1726.48 --> 1728.70]  Drug discovery is really just the start here as well.
[1728.78 --> 1734.26]  Once you bring AI into the equation, what you're doing is teaching models to learn the language of life, right?
[1734.26 --> 1737.32]  And you can use that to construct the building blocks of the future.
[1737.72 --> 1740.94]  So that can be fragrances, that can be biocomputing.
[1741.06 --> 1747.42]  So proteins that function as logic gates and kind of rebuilding what we use to power our phones and computers today.
[1747.72 --> 1749.16]  Really, the possibilities are endless.
[1749.16 --> 1750.06]  You just look around.
[1750.36 --> 1752.02]  Biology has done so much already.
[1752.70 --> 1756.76]  And once we can learn the building blocks that go into it, the possibilities are endless.
[1757.60 --> 1757.72]  Yeah.
[1757.94 --> 1763.54]  One of the things like related to that sort of like possibilities and like new learnings that this could unlock.
[1763.86 --> 1773.76]  One of the things that I remembered while both of you were talking was this thing that happened when they like were working on the board game Go with AI models.
[1773.76 --> 1784.22]  And because of all the possibilities of like gameplay in that game, it was like the moves that the model made were so different from the moves that like a human made.
[1784.22 --> 1787.76]  Like they were really effective in all of these like new ways.
[1787.76 --> 1796.54]  And I wonder kind of circling all the way back to this first stage that you were talking about this de novo discovery target to antibody lead.
[1796.68 --> 1805.72]  I'm wondering, are there any stories like that where like you put this data in the model and like no human might have thought that these would be great leads or whatever.
[1805.72 --> 1809.64]  But, you know, the computer came up with them and turns out like they really were.
[1810.00 --> 1811.78]  Yeah, this is exactly how it's playing out.
[1812.20 --> 1814.20]  We train these models to create new drug candidates.
[1814.20 --> 1821.20]  And then when we look at them or we send them to people in the lab who are really trained in like structural biology, like this doesn't make that much sense.
[1821.20 --> 1824.42]  But when you go and try in the lab, you actually see that these things are working.
[1824.60 --> 1828.84]  And, you know, when I saw that for the first time at Absci, I was just so excited.
[1828.90 --> 1830.24]  I'm like, did not expect this to work.
[1830.26 --> 1831.16]  It doesn't make any sense.
[1831.22 --> 1832.46]  We decided to try it anyways.
[1832.46 --> 1836.70]  And it's like, wow, the model has really figured out something that we never expected.
[1836.80 --> 1838.24]  It didn't make sense to us at first.
[1838.24 --> 1840.66]  But the neural networks have figured out something here.
[1840.96 --> 1846.30]  So, yeah, you definitely see those that AlphaGo example playing out in the real world and protein design.
[1846.30 --> 1846.90]  Yeah.
[1847.06 --> 1850.94]  Another interesting example is actually on the biomanufacturing side.
[1851.08 --> 1853.56]  We actually found this chaperone.
[1853.72 --> 1859.24]  Essentially, a chaperone is another protein that that helps make and produce your protein of interest.
[1859.24 --> 1868.04]  And our AI actually predicted this protein that was of unknown function when you blasted in public databases.
[1869.00 --> 1876.70]  And it actually that that protein increased our overall yields for that, you know, the protein of interest that we were making by 2x.
[1876.70 --> 1884.14]  And we ended up like finding out like, oh, my gosh, this is an actual chaperone that hasn't been ever classified as a chaperone before.
[1884.14 --> 1887.12]  It was it was unknown function in the databases.
[1887.12 --> 1891.60]  And this is like the sort of stuff that comes up day in and day out that you're just like you're blown away by.
[1891.66 --> 1893.56]  You're like, wow, like it's just incredible.
[1893.56 --> 1923.18]  So, I'm already just really inspired by.
[1923.18 --> 1929.50]  like what we've already talked about in terms of like the beginnings of your pipeline of processing
[1929.50 --> 1934.44]  with this kind of de novo discovery target to antibody lead. But I know that there's like
[1934.44 --> 1940.90]  other stages downstream between like what you're talking about going from this disease to an
[1940.90 --> 1946.38]  output drug. What comes out after this discovery phase? What does that lead into?
[1946.38 --> 1953.06]  Yeah, so it really goes into the clinical trials. And like, I think being able to apply like AI to
[1953.06 --> 1957.40]  clinical trial design, and there's companies already out there that are doing this is hugely
[1957.40 --> 1964.68]  important, like getting the right endpoint, as well as the patient population is super important for a
[1964.68 --> 1970.58]  drug getting approved as well. So it's not only the design, but endpoint as well as patient population.
[1970.58 --> 1977.84]  And so being able to utilize AI on that front, I think is a really exciting area that's going to
[1977.84 --> 1984.38]  also be able to help increase efficacy, decrease clinical trial timelines. And so, again, you're
[1984.38 --> 1990.06]  seeing AI start to penetrate in all these different areas and different companies focused on different
[1990.06 --> 1995.88]  aspects. But all of this like really good, again, ties back to this vision of personalized medicine,
[1995.88 --> 2003.30]  which is going to happen like AI has penetrated biotech before it failed, it failed because of the
[2003.30 --> 2009.96]  data. But we have shown proof of concept that this works, and it's here to stay. I mean,
[2009.96 --> 2017.12]  the advancements that Joshua and the breakthroughs that Joshua presented at NVIDIA GTC conference were
[2017.12 --> 2025.46]  the validation that AI is here to stay. I mean, being able to predict an antibody that can bind with a
[2025.46 --> 2031.32]  particular affinity that you want to the target is like incredible. I mean, it just blew my mind that
[2031.32 --> 2036.16]  we're already here. And it's just, we're just getting started. And that's the other beautiful
[2036.16 --> 2038.64]  part that there's so much more innovation left.
[2039.14 --> 2045.12]  Yeah. And to that point, I mean, I was really interested in all sorts of aspects of the GTC
[2045.12 --> 2050.86]  talk that you presented, Joshua. I know that you also talked about this element of like lead
[2050.86 --> 2056.42]  optimization, I think is what you called it. And I'd love to understand that a little bit more,
[2056.42 --> 2061.62]  like how that's a like critical piece of this puzzle and how it fits in.
[2062.08 --> 2067.66]  Yeah, of course. So what's really exciting about lead optimization is it allows us to dial in certain
[2067.66 --> 2072.86]  qualities that we're interested in for an antibody. So for example, we gave a case study in the
[2072.86 --> 2077.10]  presentation we gave at NVIDIA's developer conference, we talked about how we were able
[2077.10 --> 2082.88]  to take trastuzumab. This is a very well studied molecule. It's used as a treatment for HER2 positive
[2082.88 --> 2086.44]  breast cancer. And we showed that we could take trastuzumab. It's been so well studied,
[2086.54 --> 2090.76]  it binds very tightly to a target. And we were able to dial in its affinity to the target,
[2090.84 --> 2094.78]  we were able to make it bind two orders of magnitude more tightly and came up with a couple
[2094.78 --> 2099.34]  of variants like that. But where things start to get really interesting is when you start to
[2099.34 --> 2105.04]  optimize the model on a set of multiple parameters. So for example, you could create an antibody that
[2105.04 --> 2110.06]  doesn't just bind to HER2, but maybe binds to another target as well. For example, when you think
[2110.06 --> 2115.18]  about pandemic preparedness, we have these COVID antibody therapies, they were designed for the
[2115.18 --> 2120.16]  original COVID strain. As the COVID has started to evolve, they become weaker and weaker. We're at a
[2120.16 --> 2125.02]  point now with Omicron that almost none of them are showing binding anymore. Now imagine if from the
[2125.02 --> 2129.74]  get go, you could ask the model to make an antibody that works for all of them, that would have been
[2129.74 --> 2134.30]  really useful. And the thing is just the way traditional technologies work, like for example, if you
[2134.30 --> 2138.72]  discover an antibody in a mouse, you can't tell the mouse, I want you to make an antibody that works
[2138.72 --> 2142.96]  against multiple things that has these properties. I mean, you might even be able to infect the mouse
[2142.96 --> 2146.78]  with different kinds of COVID, and you'd get different antibodies for each of them. But then
[2146.78 --> 2151.96]  you're looking at like a whole cocktail of drugs. Whereas with AI, you could develop a single drug
[2151.96 --> 2156.34]  that has just the properties that you need. And that's where things become really interesting.
[2156.88 --> 2161.08]  And we've already shown that we presented data at that conference showing that we could optimize for
[2161.08 --> 2165.34]  multiple properties. So we could look at affinity, we could optimize for the property called
[2165.34 --> 2169.92]  naturalness that I talked about earlier. For a neural network, once you're optimizing for one
[2169.92 --> 2174.32]  property, it's pretty straightforward just to add a couple more heads to your neural network and say,
[2174.42 --> 2179.88]  well, I want you to predict these other properties as well. And then select proteins that are going to
[2179.88 --> 2183.20]  score favorably on the whole panel of properties you're interested in.
[2183.98 --> 2189.48]  That makes perfect sense. Because I think experiences that Daniel and I've had in completely different
[2189.48 --> 2195.52]  applications have some commonality in terms of how to approach that. But recognizing that the
[2195.52 --> 2201.04]  biology is evolving and moving, and you're getting these new strains out there, is the ability to
[2201.04 --> 2206.16]  track multiple strains in the way that you just described, something that takes a lot of lead time?
[2206.28 --> 2211.10]  Is it something that you can be very reactive to, as biology surprises you, and the new strain comes
[2211.10 --> 2217.18]  out, you know, the way we've seen with COVID? Or is this something that takes more effort to prep and get
[2217.18 --> 2222.20]  through, you know, can you turn on a dime? Or is that not realistically possible? And it takes a
[2222.20 --> 2225.24]  little bit of figuring it out ahead of time and prepping?
[2225.82 --> 2229.48]  So that's just one example that I was giving to kind of talk there intuitively how this works.
[2229.80 --> 2233.44]  One of the promises of AI and drug discovery is definitely allows you to move faster.
[2233.98 --> 2239.96]  So being able to go at the click of a button from a disease to a drug is a really exciting vision that
[2239.96 --> 2244.94]  we're creating here. You definitely still have to do that legwork, at least today, of going to
[2244.94 --> 2248.84]  clinical trials and actually testing it through patients. And it's really important to get those
[2248.84 --> 2253.12]  things right. But I think as you'll, what you'll start to see, and this is what Sean was mentioning
[2253.12 --> 2258.48]  earlier, is that as the success rate of the drug starts to go up, you might do a clinical trial on
[2258.48 --> 2263.04]  the algorithm instead of on the drug itself. So that's really what the future could look like here.
[2263.70 --> 2267.96]  Yeah, it's interesting that when you say that, it's almost like the blocker, or at least temporary
[2267.96 --> 2274.00]  blocker isn't so much the process of optimizing the model so much as you're still doing clinical trials,
[2274.00 --> 2279.64]  you're still doing the other things around that medical, that larger medical process. And therefore,
[2279.64 --> 2284.12]  given the fact that those are going to be present as well, you want to get it right up front, if
[2284.12 --> 2289.70]  possible. Okay. Yeah. And also to just to give an example of like the breakthroughs that both
[2289.70 --> 2296.36]  Joshua and Roberto, one of our other AI scientists have been like working on, if COVID struck now,
[2296.36 --> 2303.96]  we would be able to take a look at the spike protein and evolve it over time to look at the
[2303.96 --> 2309.04]  different epitopes that could evolve into, you know, various different COVID variants, and then be able
[2309.04 --> 2316.38]  to use our AI models to then design an antibody that binds to all of the epitopes that are likely going
[2316.38 --> 2322.08]  to evolve over time, which allows you to have an antibody that doesn't get out evolved by the virus.
[2322.08 --> 2327.02]  Because that's what we saw is these antibodies came out, and they were effective, but then the
[2327.02 --> 2332.90]  next virus or the next variant came and they weren't effective. And so this is the sort of stuff you can
[2332.90 --> 2340.16]  do that current existing technologies and drug discovery can't and it's only because of AI that
[2340.16 --> 2347.08]  you're able to do this. So pandemic preparedness and response times are going to dramatically change
[2347.08 --> 2354.20]  because of AI. With those response times in mind, and with the application of these techniques that
[2354.20 --> 2361.04]  you're using now, do you recognizing that regulation and such in the overall process beyond just the AI
[2361.04 --> 2366.86]  applicability, that, you know, it takes time for that to catch up and to absorb in change culture,
[2366.98 --> 2373.34]  if you will, do you think that clinical trials themselves and the other kind of regulatory steps
[2373.34 --> 2379.80]  that are involved will also speed up and adjust, recognizing that, you know, if you're shaping a
[2379.80 --> 2385.16]  clinical trial to optimize it with this AI technique that you're discussing, that eventually the
[2385.16 --> 2389.88]  regulators are going to kind of just expect that that's the norm, and you can get there faster.
[2390.14 --> 2393.58]  Is that kind of where we should expect to go over time?
[2393.58 --> 2398.56]  Yeah, definitely. I think with COVID, it really showed us how quickly we can get a drug approved.
[2398.64 --> 2403.52]  And I think it's starting to get regulators in that mindset of like, how can we start, you know,
[2403.54 --> 2409.30]  changing to adapt to new technology, you know, in particular AI, but at the end of the day,
[2409.54 --> 2416.74]  I don't want to say lobbying, but education to regulators and to government officials, like starts
[2416.74 --> 2422.16]  now, like telling them where things are going to be five, 10 years from now, so we can start to
[2422.16 --> 2426.68]  prepare and have those conversations is, is super important, because you can't have the once it
[2426.68 --> 2431.08]  occurs, you can't have the conversation, you got to start getting everyone prepared as to like,
[2431.08 --> 2437.60]  where the future is headed. So when it does occur, we're prepared to make the policy changes that are
[2437.60 --> 2437.90]  needed.
[2438.36 --> 2445.94]  I have a bit of a, I guess, AI nerd question, maybe, as you're seeing, I mean, the the field of AI is just
[2445.94 --> 2453.80]  so rapidly advancing. And there's like new models, you know, every week, there's like new types of
[2453.80 --> 2458.90]  approaches, whether that's graph neural networks, or like semi supervised methods, or like,
[2459.24 --> 2463.50]  prompting and like all of these things that are like happening so quickly, it's hard to keep up.
[2463.50 --> 2470.66]  I'm wondering, like, as you've applied certain things over the, over the recent past and seen
[2470.66 --> 2476.76]  their success, what do you what are you looking at, in terms of like, what are those areas of AI,
[2477.10 --> 2480.82]  maybe it's graph neural networks, or maybe it's something else? What are those areas of AI that
[2480.82 --> 2486.96]  you see impacting biology very much, you know, looking towards the next couple of years, what do
[2486.96 --> 2493.14]  you have your eyes on? And what do you expect to impact the world of biology in terms of those AI
[2493.14 --> 2493.70]  trends?
[2494.02 --> 2497.78]  So the trends happening right now are really exciting. Like you called out a couple of them right now,
[2497.78 --> 2502.48]  graph neural networks, figuring out ways to train large language models, and then use them effectively
[2502.48 --> 2506.94]  with things like prompting, we do a lot of work in those areas as well. And thinking about how to
[2506.94 --> 2511.82]  kind of apply those to biology. One of the things that we've realized, though, is that a lot of the
[2511.82 --> 2516.60]  work like happening in the field right now, like AI for biology, when you test it in the lab, it actually
[2516.60 --> 2521.30]  just doesn't work as well as you'd expect. And that's because the computational metrics that are
[2521.30 --> 2525.34]  available today are kind of flawed, like you don't have access to the right training data,
[2525.34 --> 2530.02]  you also don't have access to actually test things in the lab. And I'm very familiar with this. Like
[2530.02 --> 2535.04]  before Absi, I was working at Facebook, Facebook AI research, and there was an awesome team of AI
[2535.04 --> 2539.86]  researchers there, we wrote a series of really exciting papers, but we were never able to actually
[2539.86 --> 2544.78]  take sequences that we would, let's say, design with the models and test them in the lab. So we were
[2544.78 --> 2550.32]  fundamentally limited to just showing how our models would perform on data sets that we would just
[2550.32 --> 2554.92]  mine from previous publications. And when you start to take some of those methods and actually apply
[2554.92 --> 2559.62]  them in the lab, you start to really understand where the shortcomings are and identify areas
[2559.62 --> 2564.98]  for improvement. So there's a lot of very rich AI research happening at Absi right now, because we
[2564.98 --> 2569.52]  are really able to understand like, what is the surface level of the problem, where are the
[2569.52 --> 2575.32]  opportunities, and really do some cutting edge AI work there as well. So it's really inspiring a lot
[2575.32 --> 2579.98]  of the best AI researchers to come and talk to us, because we have this knowledge of what the right
[2579.98 --> 2584.72]  problems are. And we've got this extra dimension of what training data is useful, what's the right way to
[2584.72 --> 2590.22]  validate your model. So it really makes it a thrilling place to do AI research. So that, and we actually
[2590.22 --> 2596.72]  just opened up our new Absi AI research lab, we're calling it the AIR lab in New York City, and hiring a ton of
[2596.72 --> 2601.74]  people over there. So bringing on some of the brightest AI researchers in the space, and really creating an
[2601.74 --> 2607.48]  awesome environment to really make AI and drug discovery, some of the most exciting technologies
[2607.48 --> 2608.24]  of the decade.
[2608.68 --> 2614.84]  That's really cool. The last question to Sean, really about the biology is we've kind of delved into the AI.
[2615.08 --> 2620.56]  And you're looking as a founder, when you were envisioning this opportunity that you created and
[2620.56 --> 2626.46]  went and started the company, as you were looking at what might be the future of the field that you
[2626.46 --> 2631.84]  had been in. And you're saying, I can take this new technology, and I can go do this. From a biology
[2631.84 --> 2637.10]  perspective, what are the exciting things that when you go to bed at night, and you're laying there
[2637.10 --> 2642.08]  thinking before you go to sleep that are making you excited? Where do you think, can you paint a bit
[2642.08 --> 2647.32]  of a picture the way you see it, instead of just the questions that Daniel and I are asking about where
[2647.32 --> 2653.70]  we're going over the next 5, 10, 20 years, that, you know, it may incorporate that personalized
[2653.70 --> 2658.72]  medicine. But what's your vision for that? What are you trying to achieve? And what's driving you to
[2658.72 --> 2660.08]  push this process forward?
[2660.42 --> 2666.56]  Yeah, what gets me up every single day is being able to change the paradigm of healthcare, because
[2666.56 --> 2672.60]  healthcare is way too expensive right now. To be able to get a drug to the market, it takes billions
[2672.60 --> 2678.50]  and billions of dollars. And a lot of times, like, you don't even cure the disease, you just increase
[2678.50 --> 2685.58]  survival by six months. And so being able to actually design drugs that work better, and we
[2685.58 --> 2691.42]  can get them to patients faster and cheaper is really what drives me at the end of the day. And
[2691.42 --> 2697.96]  again, going to that personalized medicine where you have a subscription for life for healthcare, where
[2697.96 --> 2706.08]  every drug is designed for you, literally at a click of a button, and is able to help cure and prevent
[2706.08 --> 2713.46]  the diseases that you may occur over your lifetime. And we're going to just completely disrupt it like
[2713.46 --> 2720.40]  it shouldn't cost as much as it costs now. And we need to do better. And we are going to do better.
[2720.72 --> 2726.70]  And like, the future is so bright. And I even think of like, past personalized medicine, like,
[2726.78 --> 2732.08]  where does this go? It enables space travel. So you know, Elon wants to go to Mars and do space travel.
[2732.08 --> 2736.88]  Well, you need like medicine to ultimately get there. I mean, what if you could actually
[2736.88 --> 2744.34]  take it one step further, and actually design a box where it draws your blood, it predicts what
[2744.34 --> 2750.66]  drug you need, and then actually manufactures the drug there for you to then take during space travel.
[2750.78 --> 2756.06]  I know it's super futuristic. But like, these are the sorts of things that we need to ultimately
[2756.06 --> 2762.00]  accomplish. If we do want to explore space, we want to, you know, look at other planets to
[2762.00 --> 2766.78]  ultimately, you know, live on like, these are like the big questions that are hundreds, you know,
[2766.86 --> 2769.96]  500 years from from now, but it all starts, it all starts today.
[2770.46 --> 2776.70]  Well, I know me personally, like this has got me super excited. I love it how you and your team and
[2776.70 --> 2782.24]  Joshua, you are just like looking, you're going for the home run. And you're presenting a really,
[2782.38 --> 2788.34]  I think, also a positive story within like the healthcare space where there has been so much
[2788.34 --> 2795.32]  like, just cycles of negativity and negative things coming out, you know, related to whether
[2795.32 --> 2800.40]  it's the pandemic or other things. It's awesome to see this, this positive story come out and like
[2800.40 --> 2805.34]  all of this progress that you're making. So yeah, I really appreciate both of you and what you're
[2805.34 --> 2809.84]  doing and the way that you're pushing this forward. And thank you so much for taking time to join us on
[2809.84 --> 2813.52]  the podcast. It's been a pleasure. And yeah, I hope to talk again soon.
[2813.52 --> 2818.36]  Yeah, thank you so much, Daniel and Chris. This has been awesome to talk about the future of
[2818.36 --> 2820.80]  healthcare. And thanks so much for having us on the show.
[2820.98 --> 2824.02]  Thanks for the really thoughtful and future looking questions as well.
[2832.76 --> 2837.80]  All right, that is Practical AI for this week. If this is your first time listening,
[2837.80 --> 2844.30]  subscribe now at practicalai.fm or just search for Practical AI in your favorite podcast app.
[2844.50 --> 2848.52]  We're in there. And if you're a longtime listener, please do share the show with your friends.
[2848.74 --> 2853.72]  It is the best way you can help Practical AI succeed. Thanks again to Fastly for shipping our
[2853.72 --> 2859.04]  shows super fast all around the world to Breakmaster Cylinder for the Beats and to you for listening.
[2859.04 --> 2862.70]  We appreciate you. That's all for this week. We'll talk to you again next time.
[2867.80 --> 2872.90]  Bye-bye.
[2873.00 --> 2874.40]  Bye-bye.
[2875.06 --> 2876.60]  Bye-bye.
[2876.64 --> 2876.98]  Bye-bye.
[2877.00 --> 2877.16]  Bye-bye.
[2877.16 --> 2877.20]  Bye-bye.
