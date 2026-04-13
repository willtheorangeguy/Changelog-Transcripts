[0.00 --> 8.66]  Welcome to Practical AI.
[9.34 --> 19.54]  If you work in artificial intelligence, aspire to, or are curious how AI-related tech is changing the world, this is the show for you.
[20.24 --> 24.92]  Thank you to our partners at Fly.io, the home of changelog.com.
[24.92 --> 35.44]  Fly transforms containers into micro VMs that run on their hardware in 30 plus regions on six continents, so you can launch your app near your users.
[35.84 --> 37.84]  Learn more at Fly.io.
[42.68 --> 45.96]  Welcome to another episode of Practical AI.
[45.96 --> 47.72]  This is Daniel Whitenack.
[47.86 --> 53.42]  I am founder and CEO at Prediction Guard, where we're safeguarding private AI models.
[54.12 --> 63.94]  And I'm really excited today because I'm joined by a friend who I've had the pleasure of getting to know a little bit over the past weeks in the startup community.
[64.16 --> 72.20]  Joined by Ramin Mohammadi, who is the AI and ML lead at TauSite and also an adjunct professor at Northeastern.
[72.52 --> 73.04]  Welcome, Ramin.
[73.56 --> 74.94]  Hi, and thanks for having me.
[74.94 --> 77.02]  Yeah, yeah, it's great to have you here.
[77.10 --> 84.80]  It's been cool to visit the Boston startup community a couple times and participate in a few events together.
[85.46 --> 92.38]  I've been really fascinated to hear about some of the things that you're doing at TauSite, so I'm excited to dig into those a little bit.
[92.38 --> 111.20]  I'm wondering if you could share a little bit with us about kind of your really thinking deeply about the intersection of AI and privacy, but specifically as related to privacy and personally identifying information, but also personal health information.
[111.20 --> 125.62]  So PHI, so TauSite is thinking deeply about how companies are handling very private, sensitive data and knowing about where that data is, which is actually a huge problem.
[125.62 --> 137.88]  I'm wondering if you could talk a little bit about, I was kind of shocked when I heard one of your presentations and you were talking about just the size of this problem and the scope of this problem related to PHI.
[138.04 --> 149.24]  So could you give us just a little bit of a sense of what PHI is, why companies handling PHI is kind of a problem and some of the challenges related to that?
[149.84 --> 150.94]  Sure, I can do that.
[150.94 --> 158.04]  So first to give introduction, what's a PHI or personal health identifier rules?
[158.82 --> 170.88]  So based on the HIPAA rule, there are 18 identifiable, which can lead to identify an entity or a person within a healthcare organization.
[171.68 --> 178.12]  And this information is valuable and being targeted by hackers.
[178.12 --> 191.64]  One of the reasons is that they have high value because they contain your sensitive personal information, such as medical history, social security number and insurance details, which makes it very valuable on black market.
[191.78 --> 193.94]  They also use this for monetary gains.
[194.38 --> 202.46]  So hackers can sell this stolen PHI to criminals who use it for identity theft, insurance fraud or other legal activities.
[202.76 --> 205.34]  They also use it for exploitation and extortion.
[205.34 --> 213.54]  Basically, they use this stolen health information to use for blackmailing and blackmailing individual organizations.
[214.80 --> 224.42]  So 133 million healthcare data was breached in 2023, which means one out of three Americans' life was affected.
[224.86 --> 234.16]  This means about 160% increase in compared to 2022 and about 240% increase since 2018.
[234.16 --> 247.64]  So like for our listeners, if at least if they're in the US, one out of every three of those listeners has had some portion of their health information exposed in some type of breach.
[247.78 --> 248.20]  Is that right?
[248.52 --> 249.22]  That is correct.
[249.68 --> 252.76]  That record came out in 2023.
[253.40 --> 254.80]  Yeah, yeah, that's insane.
[254.80 --> 256.50]  And you mentioned hacking.
[257.02 --> 258.90]  How is this data being breached?
[259.10 --> 262.74]  Mostly by hackers or by sort of mistakes?
[263.66 --> 267.26]  What is the combination of ways that this data is getting exposed?
[267.60 --> 268.54]  That's a great question.
[269.08 --> 278.82]  So actually, based on the report on 23, 78% comes from hacking of the network storage where the data resides in healthcare.
[278.82 --> 296.06]  And a small amount, which is about like a two percent happens by when someone stole a laptop, for example, and the laptop contained PHI or sending an email via email or basically phishing emails, stuff like that.
[296.26 --> 300.28]  So there's like a breakdown, but majority comes from hacking, 78%.
[300.28 --> 308.94]  And are these companies sort of mostly healthcare companies or like who has this data and how is it given?
[309.26 --> 319.62]  So that's really interesting because technically healthcare organization like hospitals are only, I think, accountable for 30% of this incidence.
[319.62 --> 333.52]  And the remaining 70% happens by hacking through the business partners, like third-party organizations that they have some sort of softwares or the storage for keep tracking of the medical data.
[334.08 --> 338.42]  But at the end, the cost comes to the healthcare organizations.
[338.98 --> 342.94]  So that cost, what happens when this data is breached?
[343.12 --> 347.06]  What is the bad case scenario, I guess?
[347.62 --> 347.86]  Sure.
[347.86 --> 352.50]  So let me first tell you how the overall cost of this has been.
[352.98 --> 359.08]  So healthcare cybersecurity has spent about $28 billion over five years spent.
[359.48 --> 363.52]  And we are still not able to protect the PHI.
[364.26 --> 373.70]  And the way that it is that when an organization getting hacked or that there's some data breached, depending on the states, there are some cap.
[373.70 --> 384.02]  If, for example, if you have been breached and you have lost more than 500 entities or live data, you need to go public about it.
[384.74 --> 386.72]  And also you will basically get sued.
[387.06 --> 388.92]  And also you need to also get fined.
[388.92 --> 395.08]  So we have this wall, which we call it wall of shame, unfortunately.
[395.64 --> 404.46]  And government posts the names of the organization where they got hacked or they lost, basically, PHI data.
[404.46 --> 407.78]  And this wall being constantly updated.
[408.14 --> 413.34]  And the last thing that any CIO wants is that to see their name on that wall.
[413.68 --> 413.90]  Yeah.
[414.00 --> 416.22]  And their brand is hurt by that.
[416.22 --> 421.30]  But also there's fines, right, for this sort of breach.
[437.62 --> 438.62]  What's up, friends?
[438.74 --> 440.96]  Do you remember when ChatGPT launched?
[441.16 --> 441.60]  I do.
[441.60 --> 446.12]  It felt like the LLM was this magical tool out of the box.
[446.44 --> 449.86]  However, the more you use it, the more you realize that's just not the case.
[450.12 --> 451.10]  The technology is brilliant.
[451.22 --> 455.78]  Don't get me wrong, but it's prone to issues like hallucination on its own.
[455.84 --> 456.44]  But there's hope.
[456.76 --> 458.14]  There is still hope.
[458.56 --> 460.42]  Feed the LLM reliable current data.
[460.62 --> 463.08]  Ground it in the right data and context.
[463.32 --> 468.02]  Then and only then can it make the right connections and give the right answers.
[468.02 --> 475.14]  The team at Neo4j has been exploring how to get results by pairing LLMs with knowledge graphs and vector search.
[475.50 --> 482.24]  Check out their podcast episode about LLMs and knowledge graphs throughout 2023 at graphstuff.fm.
[482.36 --> 486.22]  They share tips on retrieval methods, prompt engineering, and so much more.
[486.46 --> 487.16]  Don't miss it.
[487.42 --> 489.00]  Find a link in our show notes.
[489.42 --> 490.28]  Yes, check it out.
[490.54 --> 491.92]  Graphstuff.fm.
[491.92 --> 493.32]  Episode 23.
[493.32 --> 518.80]  Could you talk a little bit about like, let's say that I'm a healthcare company and I want to not be on that wall of shame.
[518.80 --> 523.34]  And I want to do the best practices and all of that.
[523.48 --> 534.88]  Like, what is the reality of, you know, I know that, of course, you have been thinking very deeply about solving these issues with AI and machine learning or some related issues.
[535.02 --> 537.56]  But let's just say that doesn't exist.
[537.72 --> 545.52]  Like, what are the choices that a company has in terms of and what are the challenges that they face in terms of securing this data?
[545.52 --> 554.44]  So, currently, healthcare organizations have a series of tools, some of them like maybe four or five tools that they're going to do the same task.
[555.04 --> 562.10]  And the way that these traditional tools work is that they have a series of patterns like a regex, for example.
[562.10 --> 574.26]  And when someone tries to download the data, if this matches, for example, with some regex that they have, it will say, hey, you transferred PHI or hey, you downloaded PHI.
[574.68 --> 583.70]  So, those types of files, which are coming directly out of EMR, electronic medical records, are easy to detect.
[583.70 --> 599.84]  The problem is with what we call dark PHI, a PHI that resides on your network, on your machines, but you are not able to detect it because the patterns that you are using are basically not capable of detecting.
[600.08 --> 606.92]  You know, we have, for example, organizations that have millions of patients in your network.
[606.92 --> 611.34]  And I don't know if you probably have written regex before.
[612.28 --> 615.12]  Regex is always as good as the person who is writing it.
[615.52 --> 615.90]  Yeah, yeah.
[616.04 --> 617.92]  And it also, what is that meme?
[618.66 --> 626.08]  It's you decide to solve a problem with regex and then you just end up having another problem, which is regex.
[626.08 --> 627.08]  That's correct.
[627.08 --> 627.38]  That's correct.
[627.58 --> 638.38]  So, current, from the prospects that we have talked with, is that updating these rules is costly and requires a dedicated engineers or IT professionals.
[639.14 --> 641.06]  And no one likes the right regex.
[641.78 --> 642.28]  Very true.
[642.50 --> 644.94]  At least I can say that.
[645.36 --> 646.96]  So, that's a problem.
[647.12 --> 652.84]  They have tools in place, but, you know, it's incapable of solving the problem.
[652.84 --> 664.22]  And when you say dark PHI, is this, I'm assuming there's like, okay, you might have a regex for a social security number or something like that.
[664.32 --> 676.40]  But if I just think of like a doctor recording a dictation of a patient visit or something like that, there's a lot of natural text in there about diseases and all of those sorts of things.
[676.62 --> 681.76]  So, is that more natural text sort of health information?
[681.76 --> 684.82]  Is that what leads to kind of the dark PHI?
[684.94 --> 692.76]  Or does it also have to do with, you know, oh, it's easy to detect in this file format because I know the pattern I'm getting.
[692.88 --> 699.18]  But then someone scanned in this document and it's in like a PDF or something.
[700.00 --> 704.46]  And my script doesn't know how to scrape these different data types.
[704.54 --> 706.00]  What could you kind of go into?
[706.14 --> 711.04]  I'm super fascinated by this idea of this dark PHI sitting around.
[711.04 --> 716.90]  So, the first thing is that point out that is 80% of healthcare data are unstructured.
[718.00 --> 723.04]  Unstructured means that from image to audio transcript, like all sorts of PDFs.
[723.04 --> 730.70]  And what we have seen also on the healthcare, it's a variety of data extensions.
[731.76 --> 738.52]  So, you will be surprised that you will see file extensions that they don't exist.
[738.78 --> 745.64]  But what the clinicians or researchers do is that when they did a file, they put dot, their last name.
[745.64 --> 747.30]  Oh, jeez.
[747.42 --> 758.52]  So, I think in the last study we did, we found 8,000 extensions on our prospects environment.
[758.78 --> 762.32]  So, literally the personal information is in the file extension.
[762.66 --> 763.18]  That's correct.
[763.18 --> 775.94]  Personal extensions could be in the extension, but also random file extension that they might use in order to basically bypass some rules.
[776.48 --> 777.18]  Oh, okay.
[777.32 --> 777.80]  I gotcha.
[777.88 --> 787.32]  So, they're doing a workaround because there's like this annoying tool that prevents this data from being transferred around is blocking this file type.
[787.32 --> 789.08]  So, if I just change the file type.
[789.34 --> 789.74]  That's correct.
[789.94 --> 795.40]  So, one thing also here to point out is that healthcare lives on data.
[795.86 --> 798.76]  Clinicians need to access that data.
[799.18 --> 804.06]  And you should not stop them basically from doing the job.
[804.66 --> 811.46]  You just need to have a better way to detect and basically maybe, for example, encrypt the file.
[811.56 --> 815.24]  So, if someone else stole that file, they cannot open the file.
[815.24 --> 819.92]  Our goal here is not to prevent clinicians from doing something.
[820.10 --> 821.62]  It's just to make it more secure.
[822.08 --> 822.16]  Yeah.
[822.36 --> 832.04]  And maybe that starts to get a little bit to kind of transitioning to how AI and machine learning fit into this puzzle.
[832.30 --> 836.36]  Before we exactly describe how it does fit into that puzzle,
[836.36 --> 847.14]  I think there might be a lot of listeners out there that are very intrigued by what the challenges might be of applying AI or machine learning in the context of healthcare.
[847.72 --> 849.86]  Like, what are the unique challenges?
[849.86 --> 860.08]  If you're a data scientist and you're, you know, building a model or wanting to use an LLM or building your own model to use in a healthcare context,
[860.72 --> 869.30]  what's unique about that context that makes it more challenging to maybe, maybe it's on the deployment side or the model building side.
[869.30 --> 874.84]  What are some of the challenges related to working in healthcare specifically with this technology?
[875.16 --> 876.54]  This is an interesting question.
[877.08 --> 880.16]  As someone who's keen on MLOps,
[880.62 --> 881.84]  Yes, exactly.
[881.98 --> 885.28]  I always say the main challenge is the whole project.
[885.28 --> 891.78]  But for us, these challenges are a bit more than some other AI technology due to the space which we are in.
[891.94 --> 896.58]  For example, we don't have access to real patient data to train our model.
[897.12 --> 903.12]  And no healthcare organization will agree to let you use the data.
[904.06 --> 907.56]  And probably if one of them agreed to it,
[907.72 --> 910.80]  I'm guessing you couldn't use that same model for a different organization
[910.80 --> 915.66]  because you trained on specific data that's sensitive for one organization.
[915.98 --> 916.38]  Is that right?
[916.70 --> 917.86]  That's absolutely correct.
[918.00 --> 922.32]  We have a huge data heterogeneity problem.
[922.96 --> 928.40]  And that comes like, for example, one organization, it's for cancer organization.
[928.54 --> 931.14]  The other organization is like it's a dental organization.
[931.82 --> 933.66]  These datas are different.
[934.44 --> 936.48]  Other challenges that I can say is that
[936.48 --> 941.48]  you also cannot collect or transfer any data to the cloud.
[942.02 --> 944.24]  That means everything needs to happen at the edge.
[944.82 --> 947.16]  Data labeling is highly difficult.
[947.50 --> 954.84]  Even human level performance has about 8% to 10% labeling error for detecting PHIs.
[954.84 --> 958.76]  Again, for example, you have lots of types and extensions.
[960.24 --> 962.18]  Data normally contains bias.
[962.18 --> 966.20]  Certain demographics have higher amount of data than other.
[966.88 --> 975.20]  Model development is confined by first model performance and then optimization metrics.
[976.30 --> 983.10]  And model deployment on the edge has its own difficulties, which we can talk about later.
[983.92 --> 991.32]  I think lastly, unsupervised model monitoring makes it more challenging to detect drifts.
[991.32 --> 996.42]  And just to kind of define a couple of those things, when you say the edge, what is your...
[996.42 --> 1002.50]  Because people might have different definitions in their mind of whether that's some staff member's laptop
[1002.50 --> 1010.10]  or a desktop in a lab or something like that, or like a phone or a microcontroller somewhere.
[1010.30 --> 1011.80]  People have a range of that.
[1011.92 --> 1014.58]  So in the context of healthcare, what is the edge environment?
[1014.58 --> 1019.86]  Edge could be from laptop that the clinician is working with, from the desktops.
[1020.12 --> 1023.76]  Could be the tablet, for example, that you're using.
[1024.02 --> 1027.34]  And could be the storage, server storage, basically.
[1027.94 --> 1028.14]  Gotcha.
[1028.30 --> 1034.96]  But all sort of on-site with some healthcare data center or where staff are working on-site.
[1035.10 --> 1035.78]  That is correct.
[1036.04 --> 1036.28]  Gotcha.
[1036.28 --> 1042.66]  And when you say unstructured model monitoring, what do you mean around that?
[1043.00 --> 1045.44]  So what are you monitoring for?
[1045.84 --> 1046.56]  You mentioned drift.
[1046.64 --> 1052.82]  So I'm assuming that that has to do with like this PHI might also be changing itself in terms
[1052.82 --> 1054.10]  of what it's like.
[1054.10 --> 1058.82]  There's a new form type or there's a new thing that starts being collected.
[1058.96 --> 1062.46]  Is that what you mean by model monitoring and that drift element?
[1062.46 --> 1067.46]  One of the things that we will say is that the change in the distribution of the data, as
[1067.46 --> 1073.96]  you scan across different groups within the same whole organization, for example, there's
[1073.96 --> 1080.22]  a group for radiology versus there's a group for like a normal PCPs.
[1080.86 --> 1087.70]  And the datas have different distribution and we need to be able to detect any drift in the
[1087.70 --> 1089.94]  data distribution as early as possible.
[1089.94 --> 1097.42]  Sometimes you also might find something like concept drifts where it's more like a contextual,
[1097.78 --> 1103.70]  maybe a file that under certain scenarios considered as PHI.
[1104.24 --> 1108.04]  In some scenarios, it's not actually PHI.
[1108.60 --> 1112.66]  There are some rules over here, which makes it more difficult.
[1113.60 --> 1113.76]  Yeah.
[1114.06 --> 1114.24]  Yeah.
[1114.44 --> 1117.22]  Contextualization, I guess, is a challenge.
[1117.54 --> 1117.90]  Interesting.
[1119.94 --> 1127.00]  What's up, friends?
[1127.18 --> 1128.30]  I love Backblaze.
[1128.38 --> 1129.88]  I'm happy to have them as a sponsor.
[1130.36 --> 1134.50]  Backblaze makes backing up and accessing your data astonishingly easy.
[1134.84 --> 1137.24]  This is a service I personally use.
[1137.32 --> 1140.48]  Go to backblaze.com slash practical AI.
[1140.48 --> 1146.68]  You get unlimited cloud backups for Macs, PCs, businesses for just $99 a year.
[1146.94 --> 1151.36]  You can easily protect business data through a centrally managed admin, protect all the
[1151.36 --> 1156.46]  data on your machines automatically, easily deploy across multiple workstations with various
[1156.46 --> 1157.50]  deployment options.
[1157.96 --> 1163.06]  You can add on enterprise control, including granular access permissions, advanced single
[1163.06 --> 1166.32]  sign on group management controls and compliance support.
[1166.32 --> 1172.06]  They even offer multiple restore options, including rapid recovery in the event of data loss or
[1172.06 --> 1173.02]  ransomware.
[1173.22 --> 1173.68]  That sucks.
[1174.02 --> 1178.68]  You can access your backed up data from anywhere in the world using their web app or their iOS
[1178.68 --> 1179.86]  or Android app.
[1180.10 --> 1181.84]  You can even restore by mail.
[1182.14 --> 1185.46]  They'll give you a hard drive with all your data shipped to your door.
[1185.46 --> 1191.54]  You buy a hard drive restore, send the hard drive back within 30 days and get a full refund and get one
[1191.54 --> 1197.78]  year file retention and version history over 55 billion with a B files restored for customers.
[1197.90 --> 1200.38]  So far, visit backblaze.com slash practically.
[1200.38 --> 1203.98]  I so they know where you came from and continue to support the show.
[1203.98 --> 1211.36]  This is a service obviously recommended by me, but also by New York times, Inc magazine, Mac world,
[1211.50 --> 1217.40]  PC world, life wire, wired, Tom's guide, nine to five Mac, and just so many more.
[1217.40 --> 1224.96]  You receive a fully featured or no risk trial at backblaze.com slash practical AI.
[1225.36 --> 1227.00]  Again, there's support in the show.
[1227.20 --> 1228.38]  Go there, play with it.
[1228.66 --> 1231.04]  Start protecting yourself from potential bad times.
[1231.34 --> 1231.98]  Start today.
[1233.98 --> 1251.12]  Yeah, so maybe we could get a little bit now kind of into some of how you've been thinking
[1251.12 --> 1256.28]  about and approaching this problem and thinking about it from the Tau site perspective.
[1256.98 --> 1262.26]  So in the context of this edge environment, in the context of this unstructured data, in
[1262.26 --> 1267.60]  the context of the constraints that we just talked about, how did you, you and your team
[1267.60 --> 1274.80]  specifically think about applying AI and machine learning in the context of detecting PHI?
[1274.80 --> 1277.18]  And maybe also like, what is your goal here?
[1277.28 --> 1280.46]  Is your goal to stop breaches?
[1280.46 --> 1284.72]  Is your goal to provide sort of insights about this PHI?
[1284.72 --> 1290.74]  How did you decide on what the main problem is you wanted to solve and why AI or machine
[1290.74 --> 1293.44]  learning was relevant to solve that problem?
[1293.78 --> 1295.96]  I'd like to actually first tell a short story.
[1296.10 --> 1296.52]  That'd be great.
[1296.78 --> 1296.92]  Yeah.
[1297.04 --> 1301.84]  Six months ago, I was on a going to tell the AI summit in Austin.
[1302.30 --> 1307.64]  I got to the airport and I was passing the TSA pre where the TSA agent asked me to check
[1307.64 --> 1308.04]  my bag.
[1308.04 --> 1313.68]  It turned out that the machine picked up on this pre-workout container, which I had in
[1313.68 --> 1314.30]  my bag.
[1315.24 --> 1320.40]  The agent used this device on the box and the result was positive.
[1320.72 --> 1326.30]  It was like, oh man, I need to call for this special unit to come and check this.
[1326.68 --> 1327.62]  I was like, sure.
[1327.62 --> 1336.76]  Then this special unit with something like a hazmat suit, they came and used a kit with
[1336.76 --> 1341.58]  bunch of different reagents to more specifically test my pre-workout.
[1341.74 --> 1346.68]  They started sampling from the pre-workout and added to a bunch of these test tubes.
[1347.36 --> 1350.20]  Long story short, the agent was like, yeah, you're good.
[1350.46 --> 1352.32]  He was like, this happened to my cousin also.
[1352.48 --> 1355.18]  These pre-workouts are causing false positives.
[1355.18 --> 1363.24]  So we are like that special unit with bunch of different model trains to find and protect
[1363.24 --> 1364.40]  the dark PHI.
[1364.58 --> 1369.30]  While the current tools in the market are like the first and the second machine, which leads
[1369.30 --> 1373.20]  to false positive or unknown false negative.
[1373.60 --> 1378.18]  At Tau side, we do see this problem as a personal problem.
[1378.18 --> 1381.70]  It's our PHI that's being targeted.
[1382.48 --> 1386.30]  And clearly the current tools in the market, they cannot protect it.
[1386.90 --> 1392.52]  So HIPAA security rule says that you must do a complete and true assessment of all your
[1392.52 --> 1395.22]  risk and vulnerabilities to ePHI.
[1395.46 --> 1398.56]  It is so fundamental to what we need to do.
[1398.56 --> 1404.92]  And AI is such a critical piece of taking advantage of the newer technology around.
[1405.62 --> 1413.04]  Solving what used to be a labor intensive problem that are could be much easier if you can define
[1413.04 --> 1419.00]  the scope of the problem and you can have machine learning models which can run effectively and
[1419.00 --> 1421.38]  accurately in a calibrated manner.
[1421.90 --> 1423.00]  That's what we do.
[1423.00 --> 1426.54]  We take advantage of the AI to find sensitive data.
[1427.36 --> 1432.78]  And I think we get to the point that where risk and threats and vulnerabilities are going to be detected
[1432.78 --> 1434.54]  at the edge using the AI.
[1434.74 --> 1441.64]  As opposed to, gee, I have all these heuristic rules, which is how do we lots of stuff today
[1441.64 --> 1443.62]  when it comes to recognizing patterns.
[1444.36 --> 1450.78]  So at Tau side, we use AI, for example, to recognize when the sensitive data is in unstructured content.
[1450.78 --> 1455.14]  It doesn't require us to say, hey, there's a keyword here.
[1455.22 --> 1459.60]  There's another keyword here that would be how you do heuristic programming.
[1459.96 --> 1462.58]  Combination of these three words must mean this.
[1462.68 --> 1464.76]  Combination of this four must mean this.
[1465.60 --> 1469.18]  Those, you never get to do all the rules.
[1469.32 --> 1471.42]  You will never get to the variability you need.
[1471.78 --> 1476.80]  So in our model, for example, one of our model with about 50 million parameters model
[1476.80 --> 1480.20]  that can be set to recognize this stuff.
[1480.20 --> 1487.46]  You will never, in years of programming, get that much logic into your rejects.
[1488.46 --> 1494.88]  So now, the other main factor is for us to ability to run these models right at the edge
[1494.88 --> 1499.42]  where the data is being created, emailed, printed, copied, or faxed.
[1499.64 --> 1505.02]  We bring the AI to the data rather than taking the data to the AI,
[1505.16 --> 1507.66]  which most of the current AI solution do that.
[1507.66 --> 1513.92]  By doing so, we can ensure that our data is always protected, agnostic of hardware spec,
[1514.70 --> 1516.36]  or network connections.
[1516.92 --> 1517.08]  Yeah.
[1517.22 --> 1522.34]  So all of what you said makes a lot of sense in terms of the approach and how you're applying
[1522.34 --> 1524.04]  AI and machine learning.
[1524.04 --> 1530.70]  But also in my practical sort of data scientist mind, I'm like, oh, man, that's really, really
[1530.70 --> 1537.22]  difficult to sort of have these deployments of models, especially against sort of heterogeneous
[1537.22 --> 1545.18]  types of data, run them on the edge, run them across a diverse set of hardware.
[1545.18 --> 1551.58]  From your perspective as a practitioner, where do you think was the most challenging of those
[1551.58 --> 1551.88]  issues?
[1552.02 --> 1555.96]  Was it having to do with the deployment targets and the diversity of those?
[1556.36 --> 1562.38]  Was it having to do with the types of models that you could or couldn't run in those edge
[1562.38 --> 1562.88]  environments?
[1563.44 --> 1566.32]  Did it have to do with the actual training and labeling of the data?
[1566.32 --> 1571.66]  I imagine all of those are really difficult problems to solve and you had to tackle all
[1571.66 --> 1571.98]  of them.
[1572.40 --> 1579.48]  But what were you maybe, what was some of the hardest problems to solve with respect to those
[1579.48 --> 1579.80]  things?
[1580.16 --> 1587.62]  I definitely will say the first but the most challenging problem is the data labeling and
[1587.62 --> 1588.96]  data creation.
[1588.96 --> 1596.48]  Because we don't have access to real patient data, so we need to create our own curated data
[1596.48 --> 1603.58]  set, which we need to ensure that we don't introduce bias, creation bias in that data.
[1604.42 --> 1606.90]  The other thing comes around the model training.
[1607.46 --> 1615.90]  So our solution needs to be able to live alongside other programs that are running on a given machine
[1615.90 --> 1619.30]  within a certain performance boundaries.
[1619.90 --> 1623.40]  One example I give you is that IT has set of rules.
[1623.82 --> 1631.32]  If there is an application surpasses certain memory or CPU, it will block that application.
[1631.80 --> 1637.88]  So you need to be sure that all these ML models that you have or this ML pipeline that you have
[1637.88 --> 1642.20]  always remains below this basically boundary.
[1642.20 --> 1647.58]  And is that because these are essentially, I mean, I might say mission critical, but these
[1647.58 --> 1649.96]  are sort of life critical systems, right?
[1650.02 --> 1652.26]  Like they're using these to treat patients, right?
[1652.36 --> 1652.98]  So if they...
[1652.98 --> 1653.54]  That is correct.
[1653.74 --> 1660.36]  If you pull all the memory and the thing stops working, then it's potentially a life
[1660.36 --> 1664.66]  threatening type of situation or at least a very concerning situation in the healthcare
[1664.66 --> 1665.92]  context, right?
[1666.08 --> 1667.26]  That is absolutely correct.
[1667.56 --> 1667.82]  Gotcha.
[1668.42 --> 1668.66]  Yeah.
[1668.66 --> 1676.72]  And in light of those constraints, of course, some people now might just say, oh, well, we've
[1676.72 --> 1681.16]  got all these LLMs now and they're great at doing all of these things.
[1681.40 --> 1686.88]  But I'm guessing a lot of those aren't sort of fitting for this sort of environment, these
[1686.88 --> 1687.82]  memory constraints.
[1688.18 --> 1689.20]  So where do you go with that?
[1689.20 --> 1695.02]  Is it looking back to sort of traditional NLP sorts of things?
[1695.20 --> 1696.34]  Is it model optimization?
[1696.88 --> 1698.44]  Is it a combination of those?
[1698.66 --> 1704.28]  How are you balancing the constraints, but also kind of looking forward to these new
[1704.28 --> 1706.42]  generations of models and that sort of thing?
[1706.72 --> 1713.54]  Regarding the LLMs, I was reading about this Phi 3 by Microsoft, the small model.
[1713.80 --> 1713.96]  Yeah.
[1714.18 --> 1721.80]  And even that model requires certain amount of core, RAM, or GPU.
[1722.02 --> 1722.38]  Correct.
[1722.38 --> 1728.00]  None of the healthcare organizations have computer with those specs.
[1728.00 --> 1734.90]  They all have like four gigabytes of RAM maximum and some legacy CPUs.
[1735.78 --> 1744.16]  The other problem with LLM is that it introduced some additional risk to the health screen.
[1744.16 --> 1751.38]  Some clinicians or researchers, they're using tools like, for example, chat GPT to copy paste
[1751.38 --> 1757.62]  patient data to get some summary extraction, which it's not how it should be used.
[1757.62 --> 1765.02]  I know, for example, I know actually your company, prediction guard, you are trying to solve a problem like that.
[1765.18 --> 1765.32]  Yeah.
[1765.54 --> 1769.26]  There's certainly a lot of people pasting things into chat interfaces.
[1769.26 --> 1770.52]  That's very concerning.
[1770.78 --> 1772.42]  I'll definitely say that.
[1772.60 --> 1773.34]  Yeah, for sure.
[1773.88 --> 1774.42]  That is great.
[1774.42 --> 1784.60]  Now, when it comes to model optimization, we take a series of approaches to be sure that our models are optimized for such an environment.
[1784.96 --> 1792.88]  This could be from knowledge distilation or student-teacher networks, quantization, and model pruning.
[1793.36 --> 1800.74]  We do a technique combination of all of these to ensure that every model that we have lives within a certain boundary.
[1801.12 --> 1801.38]  Gotcha.
[1801.66 --> 1802.16]  Yeah, yeah.
[1802.16 --> 1802.88]  That makes sense.
[1802.88 --> 1804.00]  So it's very important.
[1804.00 --> 1809.96]  And I'm guessing the model architectures and the approaches that you can only go so far.
[1810.06 --> 1819.44]  It's not like you're going to take LAMA 370 billion and do these optimization techniques and fit it into four gigabytes of memory and run it on a CPU.
[1819.76 --> 1821.42]  So it's super interesting.
[1821.68 --> 1829.86]  And I think, I don't know, what is your view as maybe you observe in the marketplace, people are exploring these open models, exploring bigger models.
[1829.86 --> 1840.46]  But at least in the space that you work in, the only way that you kind of move forward is with small models or customized models, optimized models.
[1840.46 --> 1845.96]  How do you view that kind of shifting into the future?
[1845.96 --> 1854.12]  Do you think there will always be this sort of diverse set of environments in the healthcare space that you need to optimize models for?
[1854.52 --> 1861.58]  Will they eventually, you know, get over their hurdles of using kind of a cloud or large models?
[1861.58 --> 1865.58]  How do you see that developing moving forward and into the future?
[1865.58 --> 1875.06]  A report by Schneider Electric indicates that currently 95% of AI workload operates on data centers.
[1875.62 --> 1884.20]  They have forecast that this number to go to 50% between edge and cloud by 2028.
[1884.20 --> 1898.24]  When you're monitoring the current developments in the market, you can see that most of the chip manufacturers are moving towards creating much stronger chips or machines where they allow to run the AI at the edge.
[1898.66 --> 1903.62]  For example, Intel's Meteor Lake or the AI PCC, right?
[1903.62 --> 1914.12]  But it will take quite a while for healthcare organization to have that change adapted because, you know, it requires budgets.
[1914.96 --> 1921.24]  And I think healthcare organization, they go through machine update once every five years.
[1921.70 --> 1926.28]  I don't think they do it over all data machines, only maybe certain machines.
[1926.28 --> 1934.22]  But definitely, I do see the future that you can bring much larger models right at the edge.
[1934.48 --> 1936.86]  But I don't think we are there yet, not.
[1937.34 --> 1947.18]  Yeah, I appreciate that perspective because some people, I think, in our listener base, like they're constantly overwhelmed by this news about these new big models.
[1947.18 --> 1955.28]  But it's harder to get this sort of story of a practitioner on the ground working with specific companies in certain constraints.
[1955.28 --> 1964.96]  There's still quite a diversity of constraints that practicing data scientists or AI engineer has to work within.
[1965.22 --> 1967.90]  So I think that viewpoint's very important.
[1967.90 --> 1985.82]  As you kind of look at what you've done with TauCite and these tools that you've built in detecting PHI, helping companies know where their PHI is, reducing false positives, figuring out how to run these models on edge devices and all of those things.
[1985.82 --> 1988.82]  Do you have anything that stands out in your mind?
[1988.82 --> 2001.88]  You don't have to mention specific customers or anything, but success stories or really things that you're proud of that you're glad that you've been able to be a part of in terms of helping protect this PHI?
[2002.04 --> 2006.20]  Any sort of case studies or use cases that pop into your mind?
[2006.20 --> 2010.88]  Yeah, I can give some examples without naming anyone.
[2010.88 --> 2011.28]  Sure.
[2011.28 --> 2023.16]  But we were in this meeting and this CISO was in the call and it's like, I had these laptops that was stolen and I don't know what's on that laptop.
[2023.58 --> 2031.56]  But because we have our software on that laptop, we kept doing inventory and it turns out the laptop contains lots of PHIs.
[2031.56 --> 2045.14]  So they never have that view on this type of scenarios that where the PHI is or who has access to it, but we can basically give you that.
[2045.88 --> 2053.36]  I was on another customer call and it was like, we are happy with the tools that we have.
[2053.36 --> 2057.98]  They have less false positive, but unknown false negative.
[2058.74 --> 2062.50]  And we are quite unhappy for writing the rules.
[2063.16 --> 2063.28]  Yeah.
[2063.54 --> 2064.96]  You know, it takes us a while.
[2065.58 --> 2070.74]  But when you use our tool, there's no rules that you need to write.
[2070.82 --> 2075.42]  It's basically out of the box after you're installing our product.
[2075.42 --> 2081.94]  It will start scanning all the files and also monitoring what's happened on the machine.
[2082.06 --> 2090.54]  So if someone copying or pasting, for example, PHI into an email or into another file, we can read that.
[2091.04 --> 2091.92]  We can detect that.
[2092.08 --> 2095.86]  If someone faxing it, we can basically detect that.
[2095.86 --> 2111.64]  So these customer calls that they have been on, they also got to be positive and sometimes scary for customers because, you know, we are able to find really detailed information around your network.
[2112.14 --> 2113.44]  You're pulling the curtain back.
[2113.78 --> 2116.32]  There's work to do once you understand it.
[2116.32 --> 2129.74]  Yeah, well, maybe as we kind of draw pretty close to a close here, as you are kind of plugged in both on the academic side, you're plugged in on the startup side with TauCite.
[2129.98 --> 2136.42]  You're, you know, investing in this healthcare industry from the perspective of AI and ML.
[2136.94 --> 2139.24]  What gets you excited as you look to the coming year?
[2139.34 --> 2140.84]  Maybe it's things with TauCite.
[2140.98 --> 2143.40]  Maybe it's things more generally in the AI community.
[2143.40 --> 2151.40]  What are you excited about and what do you think is some of the positive things that you're seeing kind of develop over the coming year?
[2151.78 --> 2154.44]  I think there are two things that I'm really interested.
[2154.68 --> 2161.94]  One is the development around these large models and the fact that they're getting smaller and smaller.
[2162.64 --> 2172.50]  I am looking for the day that I could work with those SLM or small large models and deploy those on right edge.
[2172.50 --> 2180.12]  And I think the other thing that I'm quite interested in right now actively working on is the federated learning.
[2180.54 --> 2184.72]  I know federated learning is kind of in the background.
[2184.92 --> 2192.46]  Not many companies actively are doing it due to all the challenges that it has and also some security concerns.
[2192.46 --> 2209.04]  But for a domain like healthcare, where you cannot transfer data and you cannot see the data, I found that absolutely necessary that for your models to be able to train themselves and update themselves.
[2209.42 --> 2213.42]  So I think those are the two main things that I'm looking for the upcoming years.
[2213.42 --> 2214.24]  That's awesome.
[2214.50 --> 2217.86]  Yeah, I'm definitely excited by both of those things as well.
[2218.00 --> 2222.90]  And I know Chris and I on this podcast have mentioned federated learning for years.
[2223.16 --> 2230.12]  I hope that it kind of comes more to the forefront as people figure out paths to do this.
[2230.28 --> 2231.46]  I think that will be interesting.
[2232.12 --> 2235.56]  Well, Ramin, it's been great to have you on the show.
[2235.56 --> 2240.86]  I think we'll see each other again in Boston before too long, I think.
[2241.04 --> 2242.90]  But yeah, it was great to have you on the show.
[2243.06 --> 2247.48]  And thanks for taking time out of your schedule to share some of these insights with us.
[2247.78 --> 2249.68]  Yeah, thanks for having me, Daniel.
[2250.02 --> 2252.04]  And see you soon in Boston.
[2252.34 --> 2252.86]  Sounds good.
[2252.96 --> 2253.24]  See ya.
[2253.24 --> 2264.48]  All right, that is Practical AI for this week.
[2265.22 --> 2266.32]  Subscribe now.
[2266.48 --> 2271.46]  If you haven't already, head to practicalai.fm for all the ways.
[2271.46 --> 2277.88]  And join our free Slack team where you can hang out with Daniel, Chris, and the entire ChangeLog community.
[2278.42 --> 2283.08]  Sign up today at practicalai.fm slash community.
[2283.72 --> 2290.62]  Thanks again to our partners at fly.io, to our beat freaking residents, Breakmaster Cylinder, and to you for listening.
[2290.98 --> 2292.74]  We appreciate you spending time with us.
[2293.10 --> 2294.28]  That's all for now.
[2294.52 --> 2296.20]  We'll talk to you again next time.
[2305.42 --> 2307.16]  Game on.
