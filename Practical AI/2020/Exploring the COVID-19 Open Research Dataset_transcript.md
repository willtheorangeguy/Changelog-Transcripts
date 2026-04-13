[0.00 --> 3.80]  The scientific engine has really spun up to handle this current situation.
[4.14 --> 10.38]  As far as I know, there's been more than 4,000 papers released since January on COVID-19.
[10.66 --> 11.08]  Wow.
[11.08 --> 19.14]  And that the number of papers continues to grow, but more importantly, the number of papers released every day continues to grow.
[19.34 --> 23.38]  So we're up to maybe more than like several hundreds of new papers a day.
[25.04 --> 27.96]  Bandwidth for Change Log is provided by Fastly.
[27.96 --> 30.24]  Learn more at Fastly.com.
[30.46 --> 33.54]  We move fast and fix things here at Change Log because of Rollbar.
[33.68 --> 35.36]  Check them out at Rollbar.com.
[35.60 --> 37.78]  And we're hosted on Linode cloud servers.
[38.12 --> 40.10]  Head to linode.com slash Change Log.
[42.76 --> 47.68]  Do not underestimate the power of the independent open cloud for developers.
[47.88 --> 49.96]  Yes, I'm talking about Linode.
[50.42 --> 54.76]  Linode is our cloud of choice and it's the home of Change Log.com.
[54.76 --> 57.56]  What we love most about Linode is their independence.
[57.96 --> 59.70]  And their commitment to open cloud.
[60.12 --> 66.50]  Open cloud means being unencumbered by outside investment and maximizing value for the community, not shareholders.
[66.92 --> 68.50]  And that's exactly what Linode represents.
[68.94 --> 69.96]  No vendor lock-in.
[70.30 --> 71.72]  Open at every layer.
[72.12 --> 74.62]  If you want to learn more, head to linode.com slash open.
[74.88 --> 77.26]  Again, linode.com slash open.
[77.26 --> 93.54]  Welcome to Practical AI, a weekly podcast that makes artificial intelligence practical, productive, and accessible to everyone.
[93.80 --> 97.94]  This is where conversations around AI, machine learning, and data science happen.
[97.94 --> 103.00]  Join the community and Slack with us around various topics of the show at changeog.com slash community.
[103.34 --> 104.30]  And follow us on Twitter.
[104.44 --> 106.10]  We're at Practical AI FM.
[106.34 --> 106.78]  Okay.
[106.96 --> 107.84]  Take it away, guys.
[107.84 --> 115.54]  Welcome to another episode of Practical AI.
[115.92 --> 117.42]  This is Daniel Whitenack.
[117.54 --> 120.48]  I'm a data scientist with SIL International.
[121.12 --> 127.18]  And I'm joined, as always, by my co-host, Chris Benson, who is a principal AI strategist at Lockheed Martin.
[127.40 --> 129.68]  How are things down in Atlanta, Chris?
[130.28 --> 131.86]  Doing very well down in Atlanta.
[132.22 --> 134.64]  Got a bit of a cold, so I may cough my way through the episode.
[134.80 --> 136.38]  But other than that, doing great.
[136.66 --> 137.44]  Spring has sprung.
[137.52 --> 138.00]  It's beautiful.
[138.20 --> 139.22]  Hopefully just a cold.
[139.86 --> 141.92]  Hopefully, yeah, we're just crossing our fingers.
[142.22 --> 143.52]  Took my daughter a couple of weeks.
[143.56 --> 144.62]  I'm hoping it was her cold.
[144.92 --> 147.46]  Took her to a pediatrician a couple of weeks ago.
[147.78 --> 149.52]  We actually had to go in because it kept going.
[149.72 --> 155.06]  And it was a frightening thing to say, well, it could be strep, could be this, or it could be COVID-19.
[155.16 --> 156.18]  We can't exclude that.
[156.52 --> 157.92]  And as a parent, that was like, whoa.
[157.92 --> 160.00]  But I've gotten through that.
[160.20 --> 160.78]  Just a cold.
[160.88 --> 161.30]  We're good.
[161.82 --> 162.50]  Good, good.
[162.52 --> 163.16]  Rolling forward.
[163.62 --> 168.20]  Well, we're surviving here in lockdown in Indiana.
[168.38 --> 170.30]  It's actually pretty nice outside.
[170.48 --> 172.66]  It's mushroom season here.
[172.80 --> 177.22]  So there's these wild mushrooms that come out in Indiana just around this time.
[177.30 --> 178.40]  They're called morel mushrooms.
[178.62 --> 179.74]  And we go every year hunting.
[180.00 --> 182.70]  So my family has some property that's all forested.
[182.76 --> 183.64]  No one else is there.
[183.64 --> 189.68]  So we've found some good times just going out there and walking through the forest and getting outside.
[189.68 --> 191.58]  So that's been nice.
[192.12 --> 194.38]  Yeah, that sounds nice whether you find any mushrooms or not.
[194.64 --> 195.14]  Exactly.
[195.42 --> 203.84]  Well, I guess a related topic because it's really the only topic these days affecting us in all of our lives in a big way.
[203.84 --> 213.12]  We've had another episode a couple of weeks ago about the COVID QA system, which is a question-answer system related to COVID-19.
[213.78 --> 216.66]  And they were also using this data set called CORD-19.
[217.56 --> 222.70]  And today we've got Lucy Lu Wong from the Allen Institute for AI.
[222.94 --> 224.46]  She's a research scientist there.
[224.58 --> 230.24]  And we're going to be talking all about the CORD-19 data set, the ins and outs, and the story behind it.
[230.30 --> 231.22]  So welcome, Lucy.
[231.22 --> 235.92]  Hi. Thank you, Daniel and Chris, for having me on the show.
[236.40 --> 238.20]  Yeah, it's great to have you here.
[238.30 --> 239.52]  I appreciate you joining us.
[239.64 --> 241.68]  This is, of course, a big topic.
[242.02 --> 247.04]  Everyone on Twitter and all around is talking about this data set and how it's being used.
[247.10 --> 250.76]  So we're really excited to talk about it a little bit more here.
[250.92 --> 261.02]  But before we do that, I'd love to hear a little bit about your background, how you got into AI-related things and ended up at the Allen Institute.
[261.64 --> 262.30]  Sure. Yeah.
[262.30 --> 266.12]  So I guess my background is maybe a little less traditional.
[266.54 --> 275.96]  I started out more in kind of biomedical engineering and physics and worked in like a host of biomedical startup companies creating medical devices.
[275.96 --> 287.72]  And over time, I was kind of doing more simulations and incorporating more data science and machine learning techniques into my work and found that that was what was very motivating for me.
[287.72 --> 311.18]  So I decided to pursue a PhD in biomedical informatics where I focus primarily on biomedical applications of natural language processing techniques and creating models to try to connect these automated methods with the type of improvements in clinical care and biomedical text mining that we so desperately need these days.
[311.18 --> 328.84]  Yeah. So when you're talking about NLP for like biomedical applications, are we talking mostly here about like medical records and doctor's notes or like whatever that is and trying to extract relevant information from those and patterns and mine those for useful things?
[328.84 --> 331.06]  Is that the main sort of drive there?
[331.46 --> 333.76]  That's definitely one aspect of things.
[333.76 --> 344.24]  I am also very interested in looking into the scientific literature and trying to extract entities and relationships and useful information out of that body of work.
[344.24 --> 350.44]  And I think that's what I'm working on at the Allen Institute for AI or AI2.
[350.94 --> 357.38]  I'm part of a team called Semantic Scholar, which I think a couple of weeks back you had an episode about Semantic Scholar.
[358.06 --> 361.20]  And it's a literature search engine project.
[361.64 --> 364.98]  And for Semantic Scholar, we've indexed, you know, 180 million papers.
[365.26 --> 368.42]  There's a really rich corpus of texts to work with.
[368.42 --> 378.52]  And as part of the research team there, I've created a number of tools and work on a number of projects to kind of understand more about the content of that text.
[378.68 --> 387.34]  And that's kind of what brought us to the Core 19 dataset is we have this kind of underlying infrastructure for processing scientific text.
[387.48 --> 391.94]  And we were asked to contribute some of that expertise to creating the dataset.
[392.46 --> 393.38]  Awesome. Yeah.
[393.38 --> 400.34]  And I'm curious, so I'll definitely reference the Semantic Scholar episode in our show notes so people can listen to that,
[400.40 --> 407.74]  because I think that provides a really good baseline for like the sort of data that you came into this recent work having,
[407.94 --> 417.10]  which is a really great way to find and discover scientific information and related data across scientific literature, which is amazing.
[417.10 --> 422.10]  I was wondering if you could comment before we jump into Core 19 specifically.
[422.10 --> 430.92]  I know we're kind of in a really interesting time where a lot of people are publishing a lot of things about COVID-19 very rapidly.
[431.38 --> 434.84]  What does that situation currently look like?
[434.96 --> 442.34]  Is it like, you know, are we talking thousands of papers over how much time, how rapidly are they coming out?
[443.16 --> 448.46]  Yeah, I think the scientific engine has really spun up to handle this current situation.
[448.46 --> 455.62]  As far as I know, there's been more than 4,000 papers released since January on COVID-19.
[456.20 --> 456.30]  Wow.
[456.78 --> 464.50]  And that the number of papers continues to grow, but more importantly, the number of papers released every day continues to grow.
[464.88 --> 468.90]  So we're up to maybe more than like several hundreds of new papers a day.
[469.30 --> 469.66]  Wow.
[469.66 --> 476.44]  And it's kind of intimidating to look at this source of information and kind of see what people are discovering.
[476.94 --> 481.22]  So the fact that you have so many new coming in every day, are you refreshing the data set?
[481.32 --> 486.74]  Is the data set static at some point in time, or is it something that you're constantly updating and refreshing?
[486.74 --> 499.06]  Yeah, so I guess maybe folks already know what the COVID-19 data set is, but it's a kind of a collection of papers about COVID-19 research, including historic coronavirus research.
[499.22 --> 505.96]  So we have a collection of historic research, and then we also have all of the new research that is being released daily.
[506.18 --> 515.10]  We update the data set currently at a weekly cadence, but we are rapidly moving to a daily cadence since there's just so many new papers released every day.
[515.10 --> 522.30]  Yeah, so since we kind of went that direction, I was wondering if you could maybe tell a little bit of the story of how this data set came about.
[522.40 --> 534.88]  I mean, obviously you had data about scientific literature within Semantic Scholar, and you were already doing certain things as relating to, you know, tracking entities or topics covered in those.
[535.20 --> 537.66]  How did the idea for COVID-19 come about?
[537.66 --> 540.00]  And I know that there's others involved in this too.
[540.00 --> 546.76]  So there's Allen AI, but there's also, I think, Microsoft and the Chan Zuckerberg Foundation and others.
[546.88 --> 548.12]  So how did this come about?
[548.80 --> 555.78]  Yeah, so the entire project is kind of a coordinated effort by the White House Office of Science and Technology Policy.
[555.78 --> 571.64]  And I think sometime in early March, a group at Georgetown, the Center for Security and Emerging Technologies, Georgetown CSET, they reached out to us at Allen AI to help coordinate the release of this data set along with a couple of different organizations.
[571.64 --> 575.22]  You mentioned MSR, Microsoft Research, Chan Zuckerberg.
[575.62 --> 580.80]  Kaggle was also involved and the National Library of Medicine, which is part of the NIH.
[580.80 --> 595.00]  So all of these groups were going to come together to essentially create this data set to help, I guess, create text mining and information retrieval tools that could assist medical experts in understanding more of what was going on with the epidemic.
[595.86 --> 606.46]  And for Allen AI, the way that we got involved is we had recently sort of created a new pipeline to revamp our research corpus, our open research corpus.
[606.46 --> 625.36]  So we had a pipeline for essentially taking these paper documents, which are traditionally in kind of a PDF format, not very easy for text mining, not very accessible, and converting them into kind of like a structured full text format where you could run these natural language processing models on them more easily.
[625.36 --> 641.28]  So that's sort of our major contribution to the data set is the pipeline for both harmonizing the paper metadata that we've collected over the years and also producing these structured full text parses so that we can run our models over that text.
[641.28 --> 658.40]  And I know one of the big things that we talked about when we talked about semantic scholar was the ability to kind of find relevant data that might be buried in the wealth of scientific literature that we have about a certain subject that is of interest.
[658.40 --> 666.40]  So when you came to CORD-19, there's the extraction of the metadata and the actual content of the paper.
[666.98 --> 673.62]  But then how do you even go about saying like these are all the papers related to coronavirus?
[674.16 --> 678.12]  I mean, I know, and I'm a little bit ignorant on this subject, so you'll have to forgive me.
[678.24 --> 682.14]  I know that coronavirus is kind of a family of things.
[682.14 --> 690.92]  It's not just this COVID-19, which is associated with coronavirus, but there's coronavirus associated with the common cold and all these things.
[690.96 --> 702.54]  So how do you go about saying like this is what we're scoping down our data set to and finding that and along with that deciding what you're going to exclude, I guess, as well?
[703.18 --> 703.98]  It's a great question.
[704.30 --> 708.02]  And I think it's a question with very open answers.
[708.02 --> 716.62]  So what we started with were a couple of trusted sources that we knew needed to be included in this data set.
[716.88 --> 723.56]  And those sources were a collection of papers curated by the World Health Organization on COVID-19 specifically.
[724.02 --> 733.40]  And we also performed searches over PubMed Central, which is a biomedical paper repository run by the NLM, the National Library of Medicine,
[733.40 --> 741.76]  as well as these preprint servers, BioArchive and MedArchive, which were publishing the latest research on COVID-19.
[741.76 --> 757.56]  And we went out and collected papers from these sources using a set of essentially keyword searches to make sure that they were relevant to both COVID-19 or the family of coronaviruses in general.
[757.68 --> 764.92]  Because I think historical coronaviruses like SARS and MERS are also extremely relevant in the current case.
[764.92 --> 765.92]  Yeah.
[765.92 --> 765.96]  Yeah.
[765.96 --> 766.02]  Yeah.
[766.02 --> 766.42]  Yeah.
[766.42 --> 767.34]  I'm kind of curious.
[767.34 --> 774.12]  As you reached out and made the data set available and you look across some of your partner websites, like Kaggle has a call to action and stuff,
[774.12 --> 782.26]  and you're trying to get AI practitioners and data scientists to focus on kind of important questions that need answering for this purpose.
[782.64 --> 787.12]  How do you provide guidance in that way for people who are going to engage on the data set?
[787.20 --> 789.96]  Is it something where people just grab it and do whatever they want?
[790.04 --> 792.80]  Is there any kind of organization across teams?
[792.80 --> 795.62]  You know, there's a lot of human factors involved in this.
[795.72 --> 796.68]  And how was that conceived?
[797.22 --> 797.42]  Yeah.
[797.62 --> 798.88]  So there were a lot of challenges.
[799.04 --> 809.46]  For Kaggle, when we opened the challenge initially, the COVID-19 challenge, there was a set of kind of 10 slightly open-ended clinical route questions, which were given to the community.
[809.96 --> 815.44]  And the engagement at Kaggle, the response we've received, has been like absolutely incredible.
[815.86 --> 820.60]  There's been like millions of views on the landing pages.
[820.60 --> 823.72]  The data set has been downloaded 70,000 times or more.
[824.14 --> 830.80]  There's been lots of teams that have cropped up and self-organized to work on this data set.
[830.92 --> 833.18]  I think there's a group called Corona Y.
[833.60 --> 843.44]  That's like several hundred data scientists and medical experts who've like bonded together to work on the COVID-19 data set and other coronavirus data sets.
[843.44 --> 848.98]  And we really want to just offer support to these community members.
[849.22 --> 855.16]  So there's, you know, a couple of sources of information that we've created to help facilitate these things.
[855.64 --> 858.28]  So on Kaggle, the forums have been super active.
[858.60 --> 865.42]  There have been a lot of people answering questions for each other, including from the organizations that have created these data sets.
[865.42 --> 871.90]  We've also established like a discourse to answer questions specifically about COVID-19, the data set.
[872.28 --> 873.94]  So that's a great place to get answers.
[873.94 --> 896.80]  And finally, I think for these Kaggle challenges and for these shared tasks, one of the things that we're really trying to do by hosting these shared tasks is to connect ML experts with the medical community and kind of experts who can judge the answers that are being retrieved and extracted by these machine learning experts and see whether they have practical application in the clinic.
[897.22 --> 898.40]  So that's been a challenge.
[898.40 --> 898.48]  Thank you.
[903.94 --> 906.00]  What's up?
[906.08 --> 913.82]  This is Daniel Whitenack, one of your Practical AI co-hosts, and I hope you're enjoying this episode and staying healthy during these crazy times.
[914.00 --> 927.22]  I'm working on some pretty cool AI stuff here from my home office, but I've also found that I'm having to get a bit creative and be intentional when it comes to honing my AI skills and virtually connecting with the AI community.
[927.22 --> 939.60]  If you're in a similar situation or you've been inspired by the practical AI we talk about on this show, I want to invite you to a live online AI training event I'm hosting this May called AI Classroom.
[939.94 --> 947.44]  In AI Classroom, I'm going to teach you the practical skills I've learned over the years using the latest open source AI technology.
[947.44 --> 953.62]  You'll learn AI theory along with practical hands-on implementations in both PyTorch and TensorFlow.
[953.62 --> 969.20]  And after the training, you'll be able to understand the latest AI models, implement your own models in code, train computer vision and NLP models, create model inference servers, and experiment with state-of-the-art methods like reinforcement learning.
[969.86 --> 972.24]  AI Classroom is taking place this May.
[972.62 --> 979.22]  It'll be taking place live and completely online in a high-quality virtual classroom, so no travel is required.
[979.22 --> 984.44]  There'll also be two cohorts with convenient time zones for Eastern and Western hemispheres.
[984.98 --> 990.20]  Don't miss out. Tickets and more information are available at datadan.io.
[990.66 --> 992.44]  That's datadan.io.
[992.86 --> 998.50]  And practical AI listeners can use the code practicalAI10 for 10% off.
[998.76 --> 1000.84]  See you online in AI Classroom.
[1009.22 --> 1020.74]  So, Lucy, you just brought up something that I think is really interesting, which is the sort of interaction between the AI community and the medical community.
[1020.74 --> 1039.98]  And I was actually wondering while you were talking about, like, okay, this Core 19 dataset exists, but I know I have some AI expertise, but I don't necessarily have a lot of medical expertise outside of knowing, like, that I should wash my hands and these other things that kind of the top five that have been going around.
[1039.98 --> 1051.74]  I guess I was wondering, as you've got more experience with this kind of intersection between the AI community and the medical community, what has that interaction been like in the past?
[1051.96 --> 1057.26]  Has there been much overlap between the AI community and medical practitioners?
[1057.76 --> 1067.94]  And then secondly, as we enter into this new Core 19 challenge, has that changed in any sort of way or been rapidly, you know, advancing in any sort of way?
[1067.94 --> 1077.26]  I've sort of worked on the intersection of these communities for a number of years, and I think there's a lot of great collaborations going on.
[1077.58 --> 1093.86]  I think a lot of folks in the computing community are incredibly motivated by these, like, very practical questions that need to be addressed, ways to improve patient care, ways to help with drug development or vaccine development, and questions of this nature.
[1093.86 --> 1109.86]  As for kind of COVID-19 specific initiatives, so I can kind of give you two anecdotes for ways that we had annotators or, I guess, medical experts interact with computing experts.
[1109.86 --> 1125.34]  So for the Kaggle challenge, it seems that what is happening is a lot of people are developing different systems, different information retrieval, different information extraction systems, and those systems need to be reviewed by experts for usefulness.
[1125.34 --> 1153.34]  So in Kaggle, there's essentially kind of like an army of medical students and other people who are willing to provide their medical expertise and volunteer their medical expertise, who are actually going through and manually reviewing a lot of the extractions that are coming out of these Kaggle challenges and creating these kind of living systematic review pages with the answers to some of these questions.
[1153.34 --> 1161.64]  So if you go to the Kaggle page, you can see these reviews kind of being created in real time and updated in real time as new literature is released.
[1162.54 --> 1170.80]  And another thing that I've been involved in lately is we're kind of running a TREC challenge on this data set.
[1170.90 --> 1179.84]  So TREC is the text retrieval conference, and it's been a project at NIST, which is the National Institute of Standards and Technology, for the last 20 years.
[1179.84 --> 1185.14]  And these folks are really good at information retrieval and judging information retrieval systems.
[1185.64 --> 1200.80]  And the way that these systems are judged is by having expert medical annotators review all the results and provide gold rankings of what is most relevant to a query and what is the kind of least relevant.
[1200.80 --> 1211.34]  So there's a lot of this, like how incorporating experts in the loop, incorporating humans in the loop to kind of bolster our machine learning systems.
[1211.34 --> 1215.18]  And that is not something that we're going to be moving away from anytime soon.
[1215.90 --> 1226.42]  As you're talking here, I'm looking at the various questions there that are listed on Kaggle, the tasks to go answer and kind of extending this thing about this collaboration between the AI community and the medical community.
[1226.42 --> 1230.16]  The questions themselves, where did they originate from?
[1230.56 --> 1236.66]  How were they decided as the important questions that we could all give a shot at going and answering with the data set?
[1236.78 --> 1237.14]  How was that?
[1237.80 --> 1246.72]  Yeah, I may be wrong, but I believe this set of questions originated from the White House Office of Science and Technology Policy in collaboration with Kaggle.
[1246.72 --> 1258.98]  And you have to understand, so this challenge and the data set during the early days, we literally had just a few days to turn around this data set, put it out there and kind of publish this challenge.
[1259.12 --> 1262.90]  We wanted people to start looking at this as quickly as possible.
[1262.90 --> 1268.04]  So there were, you know, a lot of the questions that you see on Kaggle right now are very open-ended.
[1268.64 --> 1270.78]  They can be interpreted in different ways.
[1271.20 --> 1277.36]  And as time has gone on, as we've learned in this last month, there's actually some of those questions are more useful in clinic.
[1277.70 --> 1280.00]  Some of those questions are less useful.
[1280.38 --> 1283.12]  Like clinicians already know the answers to some of these questions.
[1283.12 --> 1296.58]  So now as we move into the second month of this challenge, there will be a new batch of questions released to kind of motivate new work and kind of questions that have not yet been answered by the community.
[1297.22 --> 1298.92]  Yeah, so I'm curious with that.
[1299.02 --> 1303.36]  It seems like you could have various bottlenecks in this situation.
[1303.36 --> 1314.76]  And one of those I think you highlighted is this sort of useful interaction between medical practitioners and the AI people that are trying to do something with the data set.
[1314.90 --> 1329.32]  So I was wondering, do you have a sort of healthy community of medical practitioners that are very deeply involved in kind of looking at what's coming through Kaggle or these other teams that are kind of self-organizing?
[1329.32 --> 1332.60]  Because I know that's one, having worked at a nonprofit for a bit.
[1332.60 --> 1340.36]  One of the things I've seen is like, oh, people really get behind like the social good like challenge and they work on it like on the hackathon on the weekend.
[1340.60 --> 1342.90]  And then the project kind of dies.
[1342.90 --> 1351.90]  So how are you kind of what are the ways for people if I want to step into the some chord 19 related work?
[1352.64 --> 1361.90]  What are the ways that I can kind of step into that, but also get connected with the right sort of medical people to make sure that what I'm doing is useful and not just like an kind of thing.
[1362.60 --> 1364.38]  Interesting weekend thing.
[1365.12 --> 1365.96]  Yeah, of course.
[1366.08 --> 1370.36]  I think like now that COVID-19 has sort of taken over all of our lives.
[1370.36 --> 1378.58]  A lot of people are feeling very motivated to do something in this direction, contribute their skills.
[1378.82 --> 1385.78]  And I think I mentioned some groups earlier, groups like Corona Y, which is self-organizing to analyze this type of data.
[1386.02 --> 1392.56]  And that's a group made up of data scientists, machine learning experts, medical practitioners and so on.
[1392.56 --> 1397.28]  And so it's like a good place to get feedback on one's work.
[1397.84 --> 1399.62]  And Kaggle forums similarly.
[1400.02 --> 1409.44]  I think there are a couple of threads out there essentially continuing this discussion of how to connect to medical experts, how to verify results and so on.
[1409.62 --> 1414.54]  A lot of people have, you know, taken it upon themselves to build systems.
[1414.54 --> 1421.00]  There's tons of systems out there for searching cord 19, for extracting information out of cord 19.
[1421.58 --> 1428.78]  And, you know, to be perfectly honest, not all of those systems are going to be like highly usable or used by any kind of clinical audience.
[1429.16 --> 1440.98]  But we as a community need to essentially figure out which of those systems are most promising, figure out where to expend additional energy, like more development time and so on.
[1441.14 --> 1442.62]  And that's where our annotators come in.
[1442.62 --> 1447.46]  Going back to what you said a moment ago, you have put this together so quickly and gotten it out there.
[1447.66 --> 1451.48]  And the whole world has kind of dived into it, the whole world of data science, at least.
[1452.10 --> 1456.34]  And, you know, that's very different from how most communities, you know, form.
[1456.50 --> 1461.78]  And I'm kind of wondering with hindsight, totally recognizing that you had no choice.
[1461.84 --> 1466.48]  You had to get it out there and you did a fantastic job with what the kind of pressure that you were under.
[1466.48 --> 1483.22]  If you could go back, knowing what you know today, what are some of the things around community that you would like to have done and that maybe going forward as you're looking at, like, the tasks and how to move us going into the second month, how to move us in the next set of directions that you need people to take?
[1483.58 --> 1487.56]  What are some of the ideas that you're planning to implement there to kind of evolve this process?
[1487.56 --> 1489.32]  Let me try to unpack that.
[1489.62 --> 1490.26]  No worries.
[1490.82 --> 1492.22]  Any way you want is fine.
[1492.52 --> 1492.82]  Sure.
[1493.20 --> 1496.60]  I think we've learned a ton over the last month.
[1497.02 --> 1510.50]  Speaking with some of our collaborators at Kaggle, like Anthony Goldblum was mentioning how they've really fallen or Kaggle has fallen into this place with this challenge where they're kind of in new territory.
[1510.50 --> 1517.40]  Like the type of challenge that the Chord 19 challenge is, is very unlike most of the challenges hosted by Kaggle.
[1517.86 --> 1520.42]  And there's a very open-ended nature of it.
[1520.42 --> 1525.52]  We're like trying to discover answers, but there's no sense of like what a gold answer is.
[1525.52 --> 1542.64]  And they've reacted to that in a very like kind of wonderful way by essentially harnessing these medical students as a resource to make judgments on people's extractions and kind of putting an effort there where it seemed like the results were most useful or were going to be the most useful.
[1542.64 --> 1556.56]  So I guess that's one thing, which is trying to figure out as early as possible where the most useful results are and putting in additional effort there and maybe even like abandoning things that are not worth pursuing.
[1556.56 --> 1561.72]  And then I don't even remember what the second half of that question was.
[1562.02 --> 1562.64]  No, it was.
[1562.70 --> 1565.20]  Things that you might be thinking going forward, but no worries.
[1565.26 --> 1565.98]  We can come back to that.
[1566.10 --> 1566.40]  That's right.
[1566.46 --> 1569.64]  I mean, I have lots of thoughts on that as well.
[1569.64 --> 1575.70]  So certainly we're going to be supporting CORD-19 for as long as it makes sense to do so.
[1575.94 --> 1580.82]  Certainly until the epidemic seems to wind down a bit.
[1580.94 --> 1586.08]  There have been lots of requests for additional features and additional content.
[1586.48 --> 1588.96]  So that is one of our priorities.
[1589.30 --> 1591.66]  Additional content comes in two forms.
[1591.66 --> 1597.90]  One is simply providing more faithful parses of the papers.
[1598.76 --> 1607.30]  So right now, first things might be including things like inbound and outbound citations, tables and figures, other places where the answers might be.
[1607.66 --> 1611.10]  And these have been requested by a lot of folks.
[1611.60 --> 1614.48]  Another is content in the sense of more papers.
[1614.48 --> 1624.10]  So one thing that we've been very grateful for is that a lot of publishers have made their COVID-19 articles open access.
[1624.50 --> 1628.36]  And by making them open access, they've allowed us to release a data set like CORD.
[1628.58 --> 1635.68]  But the fact is, if you look kind of at the data set and at the papers that are being cited by the papers in the data set,
[1635.68 --> 1644.22]  there's actually a lot of content that are outside of this direct core set of articles on COVID-19 and coronaviruses.
[1644.48 --> 1649.16]  That are also very relevant to the content of the data set.
[1649.16 --> 1663.28]  So it would be great if we could work with publishers or they could work with us essentially to provide additional content that could be useful for kind of discovering information about COVID-19 and its treatments.
[1663.98 --> 1664.06]  Yeah.
[1664.18 --> 1667.64]  So it's like you've amassed this kind of central hub.
[1667.64 --> 1673.86]  But from that hub of papers, obviously those papers cite other papers and those papers cite other papers.
[1673.86 --> 1675.48]  And there's other related work.
[1675.48 --> 1677.14]  And you can kind of go down a rabbit hole.
[1677.28 --> 1685.48]  I know we talked on the Semantic Scholar episode about this sort of graph of relations and that sort of thing as papers cite each other.
[1685.82 --> 1688.88]  I mean, there is a wealth of papers already in the data set.
[1688.96 --> 1691.82]  What is the kind of current size of the data set?
[1691.82 --> 1694.58]  And, you know, you mentioned a few different sources.
[1694.58 --> 1701.68]  Could you just give us a sense of kind of the descriptive statistics of the data set at this point, I guess?
[1701.98 --> 1702.18]  Sure.
[1702.38 --> 1704.00]  Probably should have started with that.
[1704.24 --> 1704.44]  Yeah.
[1704.82 --> 1710.28]  So the data set currently consists of more than 50,000 papers.
[1710.96 --> 1715.52]  And approximately 40,000 of those papers have full text content available.
[1715.52 --> 1719.82]  And these papers, as I mentioned, come from a diversity of sources.
[1720.50 --> 1728.48]  There's a list of WHO COVID-19 papers, several hundred of those that have been curated by the WHO.
[1728.96 --> 1733.68]  And there's preprints from BioArchive and MedArchive.
[1733.68 --> 1735.48]  That's numbers in the thousands.
[1736.10 --> 1740.66]  And actually the vast majority of papers come to us via PubMed Central.
[1740.66 --> 1751.26]  And this number will actually continue to grow because many publishers are now depositing all COVID-19 content into PubMed Central.
[1751.70 --> 1753.18]  So, Lucy, I'm kind of curious.
[1753.40 --> 1758.40]  So recognizing that your responsibility has been putting this together and getting it out into the world,
[1758.60 --> 1764.64]  I imagine that you've probably talked with various teams or at least observed some of the efforts and work that's going on.
[1764.64 --> 1770.00]  And so I'm kind of curious, what are some of the more interesting or innovative or, you know,
[1770.08 --> 1776.30]  pick your adjective of the efforts that you've heard of and kind of gone, wow, that's a pretty cool way of approaching this.
[1776.62 --> 1778.24]  Any stories to tell us on that?
[1778.62 --> 1783.26]  I think folks have done a really great job diving deeply into this data set.
[1783.48 --> 1789.50]  There's so many different kind of search engines that have cropped up over this data set.
[1789.50 --> 1799.04]  If you go to the data set landing page on Semantic Scholar, there's like a list of maybe several dozen that we've heard of and are enumerating there.
[1799.36 --> 1801.78]  I'm sure there's many more that we aren't aware of.
[1801.98 --> 1807.12]  People are pursuing lots of different technologies for these kind of search engines.
[1807.40 --> 1813.76]  Some are kind of using the latest kind of state of the art transformer models, neural models for ranking.
[1813.76 --> 1821.42]  I think CovidX from Waterloo and NYU is using kind of the latest Psy-T5 model.
[1821.62 --> 1822.38]  Very cool stuff.
[1822.64 --> 1835.16]  And some of the search engines are actually using very traditional methods using Lucene or Elasticsearch and focusing more on how to search and filter using entities or other paper features.
[1835.16 --> 1852.84]  And we've kind of a funny thing that we heard from Kaggle is that for many of the questions on the Chord 19 challenge, something simpler methods, the more traditional methods have actually worked better for kind of extracting answers.
[1853.18 --> 1855.12]  And this came as a surprise to me.
[1855.12 --> 1862.40]  So I have a follow up on that, and that is like for working better, you know, kind of putting that in quotes.
[1862.86 --> 1863.64]  What does that mean?
[1863.72 --> 1876.08]  Who out there is looking at the various results that are coming back from teams and making those evaluations and kind of and obviously you've already said that you'll be steering into the new tasks on Kaggle, learning what we know.
[1876.18 --> 1882.12]  Who's making those evaluations and the decisions associated with that to keep everything focused?
[1882.12 --> 1895.06]  So I think this is a primarily work that has been taken on by organizers at Kaggle and kind of medical students that they've had come in and evaluate some of these answers.
[1895.44 --> 1900.16]  So really, like, they put in a ton of effort in curating these results.
[1900.16 --> 1915.40]  And I think as for, like, the metrics that we use to judge these results, I think currently, like, they're mostly kind of information retrieval based metrics of success.
[1915.40 --> 1928.20]  Yeah, to give people an idea, I'm on the Kaggle website and just looking at some of the tasks to maybe for those listeners out there that don't have a good idea of the kind of scope of these.
[1928.40 --> 1934.80]  There's information or some of the tasks that are listed are what do we know about COVID-19 risk factors?
[1935.60 --> 1938.58]  What do we know about vaccines and therapeutics?
[1938.64 --> 1940.98]  What has been published about medical care?
[1940.98 --> 1956.90]  And if I kind of dive into each of these, there's a number of submissions, but things like, you know, cord 19 analysis with sentence embeddings, COVID-19 literature clustering, full text search of research papers.
[1957.38 --> 1958.72]  And so you can kind of already see.
[1958.88 --> 1963.50]  And here's another one, BERT squad for semantic corpus search.
[1963.50 --> 1973.92]  So you get a sense, I think, of what you were talking about, Lucy, that some people are kind of going after these sort of transformer based, maybe extractive QA sort of things.
[1974.08 --> 1984.36]  Others are maybe using full text search capabilities that have been out there for a while, like elastic search sort of capabilities, like we talked about on a previous episode.
[1984.36 --> 1996.44]  Also, if I'm looking at the data, just to kind of have something in people's mind, I'm seeing, of course, you have the categories of source, like the bioarchive and that sort of thing.
[1996.54 --> 2002.16]  But if I'm looking at the individual papers, I can see the abstract of the paper and the body text.
[2002.16 --> 2013.84]  And if I'm looking at, you know, the body text of this one, I'm reading things like to assess the effects of truncation of the policy tracked on replication, blah, blah, blah.
[2014.26 --> 2020.34]  Which some of that doesn't mean a lot to me, but this is the sort of data that's in there.
[2020.34 --> 2029.16]  I was wondering, as a complete noob to, you know, a lot of this medical terminology, what are maybe some good ways?
[2029.16 --> 2041.44]  I know you've got this kind of co-vis from the Allen Institute, which is helping kind of explore some of the looks like the genes and cells and diseases and chemicals that are connected throughout the data set.
[2041.58 --> 2051.46]  What are some good ways of kind of onboarding into the CORD-19 work for people that might be sort of new to medical terminology?
[2051.46 --> 2060.14]  Are there ways to kind of pick up some of that or explore some of it and form some of those connections in a reasonable sort of way?
[2060.70 --> 2061.44]  The domain knowledge?
[2061.78 --> 2062.02]  Yeah.
[2062.68 --> 2069.22]  I think domain knowledge is one of the greatest barriers for working on this data set.
[2069.50 --> 2072.30]  And thanks for mentioning the Covis project.
[2072.30 --> 2080.26]  That's a tool that was released by Allen AI for exploring this data set in a slightly more meaningful way.
[2080.26 --> 2096.50]  And for that tool, we essentially ran models to perform extractions of these entities from the text, entities of different classes like drugs, genes, diseases, phenotypes, things of that nature.
[2096.84 --> 2105.68]  And created a visualization to allow you to browse the relationships that are most prevalent between pairs of these entities.
[2106.28 --> 2109.62]  So that's a great way to kind of explore what's in the data set.
[2109.62 --> 2112.74]  There's also just like exploring the articles.
[2113.06 --> 2115.52]  We have kind of a CORD-19 explorer to help you do that.
[2115.72 --> 2124.28]  But in general, I think unless you're willing to spend sort of a couple years of your life in medical school, it is very hard to understand what some of these terms mean.
[2124.38 --> 2129.08]  Certainly knowing what class or category of entity is being mentioned is important.
[2129.52 --> 2135.70]  So knowing something is a protein, knowing something is a receptor, knowing something belongs to a particular biological pathway.
[2135.70 --> 2143.36]  These are kind of key for gaining an initial understanding of what is being said in a text snippet.
[2143.44 --> 2149.54]  But that's also why we need medical experts to assess the actual utility of some of these extractions.
[2149.54 --> 2154.02]  So I'm wondering, I happen to have a daughter who is a third-year medical student.
[2154.36 --> 2161.04]  And I've told her very recently because we had the other episode about this and stuff, but she hadn't been aware of it.
[2161.08 --> 2163.62]  Is there any need to connect with medical schools?
[2163.62 --> 2168.40]  Has anybody kind of taken that on to try to gather those together and stuff?
[2168.40 --> 2176.48]  Because obviously there's been an enormous effort in a very short amount of time, totally recognizing the constraints of the reality that we're in today.
[2176.74 --> 2176.82]  Yeah.
[2177.14 --> 2182.46]  Is that something that y'all are kind of thinking about in terms of going forward, maybe for stage two or whatever you want to call it?
[2182.74 --> 2183.38]  Yeah, absolutely.
[2183.74 --> 2185.70]  I'm sure your daughter knows that.
[2185.86 --> 2190.46]  I mean, I don't know if she's still, if medical school is continuing as usual.
[2190.64 --> 2193.58]  But I think during the third and fourth years, you're mostly in clinic.
[2193.58 --> 2206.62]  So I know of a lot of medical schools where there are these kind of more senior medical students who really want to contribute how they can, but really aren't able to be in clinic at this moment.
[2206.74 --> 2211.82]  Yeah, they've been kicked out of the ER for, you know, they're working with the health department locally.
[2211.86 --> 2217.28]  And I think that kind of alternative work is really common right now for advanced medical students.
[2217.46 --> 2218.20]  Yeah, exactly.
[2218.20 --> 2238.16]  So for the TREC task that I was mentioning that we're hosting, we actually are enlisting medical students from a number of institutions, from the Oregon Health and Science University and University of Texas and University of Washington to kind of help with provide annotations on some of these extractions.
[2238.16 --> 2249.50]  So I think depending on where your daughter is or where some of these medical students are, there's probably going to be other initiatives like this one that really need their help.
[2250.16 --> 2253.44]  So I would definitely encourage anyone to look out for that.
[2253.44 --> 2257.22]  I guess I have one more follow-up to that that you just mentioned.
[2257.46 --> 2264.96]  Do you think recognizing that and recognizing that we're going to be past this moment at some point, this kind of very unique moment in our history,
[2264.96 --> 2281.74]  but just as, you know, the kind of the widespread introduction of like open source software really changed, you know, industry itself from being highly proprietary to being, you know, open source became not only a part of business models,
[2281.74 --> 2284.90]  but even underlying part of a lot of commercial software that's out there.
[2284.94 --> 2286.64]  And it fundamentally changed how that worked.
[2286.64 --> 2296.26]  Do you think this is a moment just because COVID-19 passes us, you know, and we get past this, that maybe there are other challenges,
[2296.54 --> 2301.42]  whether they be things that we've been dealing with a long time, like cancers or new things that may come,
[2301.74 --> 2311.50]  that this may fundamentally change how we attack, you know, really hard medical challenges with AI and that integration with the communities that has happened out of necessity?
[2311.94 --> 2314.58]  I'm certainly hoping that to be the case.
[2314.58 --> 2321.46]  So we've definitely seen what people can do when they come together for a month or two.
[2321.82 --> 2323.44]  And it's, it's incredible.
[2323.44 --> 2329.30]  Like there's so many people being engaged and building like interesting tools and useful tools.
[2329.46 --> 2335.18]  I think there's a couple of maybe things that I'd love for us to be able to extend into the future.
[2335.18 --> 2346.08]  One thing is definitely publishers coming together to release more open access content on really kind of important topics such as COVID-19.
[2346.30 --> 2352.20]  And then the community coming together, especially crossing boundaries, crossing boundaries between computing,
[2352.94 --> 2359.62]  the computing community, the medical community and policymakers to really build something useful.
[2359.62 --> 2364.84]  So I'm curious, a little bit of a follow up, I guess, to that, that question as well.
[2365.28 --> 2371.50]  I know there've been things as I've worked on related work with SIL where I was thinking,
[2371.68 --> 2379.98]  oh, I, if I would have done this prior to this crisis, like I would be able to do something better than what I'm able to do now.
[2379.98 --> 2383.58]  In hindsight, it's easy to see those opportunities.
[2383.94 --> 2387.28]  I'm curious on your side with your own research and work.
[2387.68 --> 2396.62]  I mean, you were kind of, I'm assuming you were working on various things related to Semantic Scholar prior to this crisis.
[2396.62 --> 2401.94]  And now you're heads down working on Chord 19 and getting this in shape.
[2402.08 --> 2404.80]  What are you interested in exploring in the future?
[2404.80 --> 2414.64]  Not necessarily Chord 19 related, but how has this whole process shifted like what you want to work on in your own research in the future?
[2415.34 --> 2415.52]  Yeah.
[2415.66 --> 2423.90]  So I think this brings up a slightly earlier point, which is we really became involved in the creation of this data set
[2423.90 --> 2430.02]  because we had at Semantic Scholar built a bunch of infrastructure for scientific papers.
[2430.02 --> 2443.64]  And a collaborator of mine, Kyle Lowe, and I had also been working for the past nearly year on a way of essentially creating a full text extraction pipeline for some of these papers that we are using in Chord 19 today.
[2444.04 --> 2446.44]  So a lot of this was infrastructural work.
[2446.44 --> 2450.54]  It's not particularly glamorous, but it is really important.
[2450.76 --> 2455.72]  And it really became more important in light of what happened in the last few months.
[2455.72 --> 2464.02]  I guess one thing is infrastructural improvements can be really important, even if it's not particularly sexy.
[2465.04 --> 2471.36]  And then kind of going forwards, there's certainly things I care about besides kind of creating data sets of papers.
[2471.68 --> 2479.70]  And my research focuses on making scientific literature and making this content more available to biomedical researchers and more understandable.
[2479.70 --> 2490.12]  And as you mentioned before, there's so many entities, so many kind of like very domain specific words and relationships that exist in the biomedical literature.
[2490.12 --> 2497.02]  And even for someone who is a domain expert, some of those terms can be very hard to parse through and understand.
[2497.02 --> 2505.02]  So a lot of my ongoing projects are trying to create systems that understand particular types of relationships.
[2505.02 --> 2511.18]  For example, those that understand drug-drug interactions or can mine them out of the literature.
[2511.70 --> 2515.14]  Those that can understand medical images better.
[2515.34 --> 2519.36]  These are the types of projects that I am hoping to continue to work on in the future.
[2519.54 --> 2520.22]  Awesome.
[2520.76 --> 2532.32]  We're for sure going to have the links to the main data set website in the show notes, along with the Kaggle challenge and the various other projects and groups that you've talked about.
[2532.32 --> 2540.52]  Really appreciate you coming on the show and describing a bit more about the data set, how it came about and your own work with it.
[2540.76 --> 2545.18]  Really encouraged by the work that the Semantic Scholar team and collaborators are doing.
[2545.70 --> 2549.34]  And thank you for your hard work on this and taking time to talk to us.
[2549.94 --> 2551.42]  Yeah, thank you so much for having me.
[2551.52 --> 2556.70]  And we really hope that other folks are encouraged to kind of contribute and become involved in this project.
[2557.00 --> 2557.84]  Yes, please do.
[2557.84 --> 2564.20]  Thank you for listening to this episode of Practical AI.
[2564.86 --> 2568.52]  More like this at changelog.com slash practical AI.
[2568.88 --> 2574.26]  There you'll find our latest as well as lists of our most popular episodes and the ones we recommend.
[2574.72 --> 2579.34]  If this show has helped you on your AI journey, please leave us a five-star review on Apple Podcasts.
[2579.48 --> 2580.68]  Part us on Spotify.
[2581.04 --> 2582.48]  Star us on Overcast.
[2582.58 --> 2584.10]  And tell a friend what they're missing out on.
[2584.34 --> 2587.20]  Practical AI is hosted by Daniel Whitenack and Chris Benson.
[2587.20 --> 2588.82]  It's produced by me, Jared Santo.
[2589.06 --> 2591.56]  And our music is brought to you by the Beat Freak, Breakmaster Cylinder.
[2591.96 --> 2593.28]  We have awesome sponsors.
[2593.40 --> 2594.10]  Please support them.
[2594.18 --> 2594.82]  They support us.
[2595.02 --> 2597.12]  Thanks again to Fastly, Linode, and Rollbar.
[2597.56 --> 2604.96]  If you and your organization could benefit from speaking directly to all the AI practitioners out there, you should sponsor the show.
[2605.42 --> 2610.22]  Podcast advertising is one of the most effective ways to spread your message in an authentic way.
[2610.54 --> 2613.02]  Plus, you get the added bonus of supporting something you love.
[2613.26 --> 2614.02]  That's all for now.
[2614.40 --> 2615.34]  We'll talk to you next time.
[2615.34 --> 2615.98]  Time for now.
[2615.98 --> 2616.58]  Thanks for listening.
[2631.20 --> 2643.32]  Wow.
