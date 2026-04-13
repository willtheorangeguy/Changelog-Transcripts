[0.00 --> 6.06]  Hi everyone, this is Daniel coming to you with a slightly different episode of Practical AI this week.
[6.22 --> 12.20]  Recently, Purdue, Microsoft, Informs, and a few others put on a case competition,
[12.56 --> 18.02]  which included student teams from across the nation, around 170-something teams,
[18.14 --> 21.98]  all working on a shared task related to image captioning.
[22.08 --> 25.46]  This is a task where an image is input to a model,
[25.46 --> 30.86]  and then the job of the model is to output a text caption corresponding to that image.
[31.06 --> 35.60]  And I had the privilege of getting to be one of the judges for this competition,
[35.60 --> 42.32]  and I took the opportunity to interview some of the sponsors and the participants in the challenge.
[42.50 --> 47.72]  Also, it was really fun because the competition used some of our data,
[47.92 --> 51.92]  the data from SIL International and the Bloom Captionings dataset,
[51.92 --> 55.24]  which includes image captioning data for a lot of languages,
[55.46 --> 61.08]  but specifically this competition focused on image captioning in Thai, Hausa, and Kyrgyz.
[61.34 --> 65.12]  So hope you enjoy the discussion of this challenge, and here we go.
[75.06 --> 81.18]  Welcome to Practical AI, a weekly podcast making artificial intelligence practical,
[81.54 --> 83.32]  productive, and accessible to everyone.
[83.32 --> 84.46]  Subscribe now.
[84.60 --> 88.44]  If you haven't already, head to practicalai.fm for all the ways.
[88.90 --> 94.44]  Special thanks to our partners at Fastly for delivering our shows super fast to wherever you listen.
[94.76 --> 96.62]  Check them out at fastly.com.
[96.84 --> 99.00]  And to our friends at fly.io.
[99.42 --> 102.96]  We deploy our app servers close to our users, and you can too.
[103.28 --> 105.16]  Learn more at fly.io.
[105.16 --> 114.74]  Welcome to a very special episode of Practical AI.
[115.02 --> 116.38]  This is Daniel Whitenack.
[116.50 --> 119.06]  I'm a data scientist with SIL International.
[119.72 --> 123.68]  And this is a very special episode because I'm here at Purdue University,
[124.20 --> 129.08]  judging a really interesting case competition, Data Analytics for Good,
[129.08 --> 136.62]  that's sponsored by Purdue University, Microsoft, SIL International, my organization, and Informs.
[136.74 --> 142.44]  And I'm here with Matthew Lanham, who is the academic director of the MS Business Analytics
[142.44 --> 145.60]  and Information Management Program, or BAME program,
[146.04 --> 150.00]  which we've had the privilege of getting to know each other over the past few years.
[150.20 --> 153.80]  And it's really cool to collaborate and judge this competition.
[154.36 --> 157.40]  Matthew, could you tell us a little bit about it and how it came about?
[157.40 --> 158.96]  Sure. Yeah.
[159.08 --> 162.66]  So as the academic director for the Business Analytics Program,
[162.90 --> 167.82]  my job is basically trying to make sure our students are involved in analytics and data science competitions.
[168.50 --> 171.44]  And over the last seven years since we've had this program,
[171.70 --> 175.66]  our students have won or placed in many of these national competitions.
[176.18 --> 180.46]  So we've got a really well-established brand and name out there,
[180.48 --> 185.30]  and we thought, hey, why don't we create our own national data analytics competition,
[185.30 --> 189.72]  and let's do something that's for good, not necessarily just focus on trying to make money.
[189.98 --> 190.54]  Yeah, yeah.
[190.66 --> 195.08]  So tell us a little bit about the actual problem that the students are working on,
[195.18 --> 200.50]  and maybe a little bit about the mix of who is involved in the competition from across the nation.
[200.86 --> 201.22]  Sure.
[201.40 --> 204.96]  So the actual problem was sponsored by your company, SIL International.
[205.28 --> 210.62]  And basically what they're trying to do is use natural language processing to do image captioning,
[210.62 --> 213.40]  which is not a trivial task by any means.
[213.56 --> 217.54]  So when we put this problem out there to the students, they're like, oh, my gosh, what is this?
[217.78 --> 222.42]  And the great thing is it's not something that you would see in a traditional NLP course,
[222.58 --> 225.76]  this kind of problem, and there's been a lot of great learning involved.
[226.18 --> 232.54]  Overall, we had 172 teams across the nation apply and register for the competition,
[232.78 --> 235.82]  and there were 36 universities that were represented.
[236.30 --> 237.92]  Two of those were outside the United States.
[237.92 --> 240.32]  Wow, that's really great.
[240.56 --> 248.64]  Yeah, the competition, so this image captioning, it's been cool to see because recently SIL put out this data set around image captioning,
[248.72 --> 253.20]  and it was convenient timing because about a week or so later you reached out and said,
[253.28 --> 255.32]  hey, we're running this cool case competition.
[255.46 --> 257.64]  Do you have any cool data sets to work on?
[257.70 --> 258.98]  And that worked out really good.
[259.04 --> 264.88]  I think I've heard students all learning a lot about natural language processing,
[265.00 --> 266.22]  but also the world's languages.
[266.22 --> 271.34]  So when you try to do image captioning in Thai, for example, there's no spaces,
[271.68 --> 274.54]  and you can't tokenize words with just, like, spaces.
[275.10 --> 280.32]  So just even realizing things like that has been quite interesting to see for students.
[280.56 --> 285.30]  And I know I've worked sort of halfway through the day of judging at this point that we're recording,
[285.38 --> 289.70]  and I've already been surprised and encouraged by a lot of the solutions.
[289.70 --> 300.28]  One of the other sponsors of the competition is Informs, which I'd love people to know a little bit more about what Informs is generally,
[300.58 --> 303.70]  because it is a vibrant and large community.
[303.88 --> 305.30]  Could you tell us a little bit about what that is?
[305.60 --> 306.04]  Absolutely.
[306.04 --> 310.50]  So the Informs stands for the Institute for Operations Research and Management Science.
[310.82 --> 314.92]  It is my favorite professional organization.
[315.16 --> 317.50]  So it's been around for many years.
[317.86 --> 320.54]  And, you know, we used to call it Operations Research and Management Science,
[320.62 --> 324.28]  but now we refer to a lot of the stuff that we've done for years as analytics and data science.
[324.28 --> 331.60]  Within Informs, there's also a certification program called the Inform Certified Analytics Professional, or CAP.
[332.12 --> 332.94]  So I'm a CAP.
[333.02 --> 335.48]  I was one of the first CAPs many years ago.
[335.84 --> 341.12]  And basically the whole idea with the CAP is you don't have to be a technical person to get this CAP,
[341.18 --> 345.02]  or you don't have to be just, like, the business person.
[345.24 --> 346.56]  It's really for everybody.
[346.56 --> 353.18]  And the whole idea is how it came about was the people at Informs worked with business professionals
[353.18 --> 356.38]  from all different areas of analytics and data science operations research
[356.38 --> 361.24]  to identify what are the key kinds of tasks that you would do as a professional.
[361.84 --> 364.98]  And what they did is they came up with basically seven domains.
[365.48 --> 367.64]  Business problem framing is the first one.
[368.02 --> 373.38]  Then analytical problem framing, knowing your data, methodology or approach selection,
[373.38 --> 376.54]  model building, deployment, and lifecycle management.
[377.06 --> 379.44]  And if you guys, if the audience hears those kind of things, they're probably thinking,
[379.56 --> 384.58]  hmm, that sounds a lot like Chris BM that we all heard about, you know, in school or at some point,
[384.68 --> 385.38]  following a process.
[385.86 --> 388.14]  And that was the thing is a lot of times when we're working on these problems,
[388.40 --> 389.80]  you got to follow a process.
[390.36 --> 393.44]  And they kind of extended that Chris BM framework.
[393.66 --> 398.66]  And there's just a lot of tasks within there that we hope people are aware of and think about
[398.66 --> 400.86]  when they try to develop solutions and practice.
[400.86 --> 405.62]  Yeah, and we've been utilizing that framework and judging here at the competition,
[405.62 --> 411.56]  which has been really, really useful, I would say, to consider these different elements of the process.
[412.06 --> 417.40]  And maybe how would you say after working with teams in this process, you know, for years now,
[417.46 --> 419.76]  actually, like thinking about these different elements,
[420.26 --> 424.88]  how do you think that kind of rounds out someone's view of like an actual,
[424.88 --> 429.70]  solving an actual business problem with like AI or analytics or data science
[429.70 --> 436.76]  in ways that maybe is sometimes neglected in a lot of just sort of process when you step into a problem?
[436.92 --> 440.82]  What are the main areas that you think kind of stretch students?
[440.98 --> 443.00]  But then as they go into the professional workspace,
[443.00 --> 445.84]  how do you think that sets them up for solving real world problems?
[446.28 --> 447.00]  Great question.
[447.00 --> 451.64]  And this is why I just love InformsCap and why we make our students follow the InformsCap
[451.64 --> 456.40]  when they do projects with companies is because you'll see a team that maybe they're the data science team,
[456.44 --> 459.74]  the real technical team, and they love to get into the nitty gritty details.
[459.80 --> 461.36]  And there's absolutely nothing wrong with that.
[461.74 --> 463.64]  But at the same time, you need to know your audience.
[463.64 --> 470.14]  And I think just following those seven domains, those seven domains for InformsCap is important
[470.14 --> 473.78]  because before you even get into the nitty gritty details of your problem,
[474.20 --> 477.62]  you need to be able to say, well, how does, what is the business problem here?
[478.00 --> 479.10]  And then how do we frame it?
[479.24 --> 481.80]  What are the possibilities of framing it into an analytics problem?
[482.22 --> 483.86]  And then, so that's the front end of the thing, right?
[484.28 --> 487.70]  And then you'll get in the middle part, which a lot of the stuff that we would talk about as data scientists,
[487.84 --> 491.48]  the data, the methodology, the model building, all the stuff that we really like to do.
[491.48 --> 496.82]  But then the last part of it, the deployment and lifecycle management, that's so key, right?
[496.88 --> 500.26]  So that's when you get into architecting and make, developing the pipelines,
[500.38 --> 502.10]  all the stuff that I know you're an expert in.
[502.46 --> 503.12]  It's just so key.
[503.40 --> 507.56]  So basically, that's what the InformsCap's doing is to say, hey, let's lay all this out
[507.56 --> 510.42]  to make sure that when we architect a solution, we design a solution,
[510.48 --> 514.56]  we try to create a solution to a problem, that we've thought about all these things
[514.56 --> 516.14]  and we haven't missed anything along the way.
[516.46 --> 516.56]  Yeah.
[517.02 --> 519.74]  Well, thank you so much again for helping organize this.
[519.74 --> 521.46]  Matthew, it's been a pleasure.
[521.78 --> 525.34]  And yeah, I really just appreciate your work on this and also your work with Informs.
[525.54 --> 526.10]  Thank you, Dan.
[526.90 --> 530.18]  I want to share exactly how the funding happened.
[531.36 --> 531.78]  The funding?
[531.98 --> 534.02]  It was just about Azure and the SOX.
[534.28 --> 534.94]  I mean, what is this?
[535.96 --> 536.84]  From Microsoft.
[537.34 --> 538.30]  Oh, oh, yeah.
[538.38 --> 539.32]  So from Microsoft.
[539.80 --> 542.04]  So that's actually a really important point.
[542.12 --> 545.82]  So one of the interesting things about this competition that's different than all other competitions
[545.82 --> 550.26]  that my students have participated in is we designed it where there's three phases.
[551.14 --> 554.80]  And phase two is where they actually work on the problem provided by Dan's company.
[555.30 --> 559.50]  But the phase one is we wanted to actually provide some training on cloud services,
[559.80 --> 562.98]  which a lot of people in industry, they know you've got to be familiar with these services
[562.98 --> 566.18]  if you're going to architect a solution and put it into practice.
[566.18 --> 571.08]  So Microsoft offers free training on their Azure AI.
[571.30 --> 573.82]  Basically, everything's free if you're a student.
[574.26 --> 579.72]  And they also offer students free practice exams and certification vouchers, which is amazing.
[580.50 --> 584.70]  So we told them, they said, you know, we would like we could get a whole bunch of students
[584.70 --> 588.12]  to participate in your training events if we can kind of piggyback off of you.
[588.14 --> 588.96]  And they said, absolutely.
[589.08 --> 589.90]  We love this.
[590.28 --> 594.12]  So that's what the students did in the phase one was they had some training for Microsoft
[594.12 --> 594.70]  professionals.
[594.70 --> 596.72]  Some of them even set for certifications.
[597.36 --> 601.22]  And then in phase two, the goal was to try to apply some of those web services for this
[601.22 --> 601.96]  particular problem.
[602.40 --> 606.92]  The last phase, phase three, is when the top teams that perform the best in the Kaggle
[606.92 --> 611.84]  competition would come on campus, present their solution, and then show how they could follow
[611.84 --> 616.24]  the informs, the seven informs cap JTAs to architect their solution.
[616.64 --> 617.48]  That's how it all came about.
[617.80 --> 618.08]  Awesome.
[618.26 --> 618.40]  Yeah.
[618.50 --> 623.34]  And that definitely brings us right into the Microsoft involvement with this competition,
[623.34 --> 629.06]  which also pleased to have with us Mark Tabladillo, who is a cloud architect with Microsoft.
[629.40 --> 629.54]  Yeah.
[629.60 --> 634.46]  Thanks for thanks for being here and being part of the competition and also Microsoft's involvement
[634.46 --> 635.34]  in this.
[635.34 --> 643.66]  It's been interesting as we've seen some presentations already even to hear how students are sort of
[643.66 --> 649.88]  making that realization about, hey, I've been working on my laptop solving maybe like data
[649.88 --> 653.90]  science toy problems in my courses or something like that.
[653.90 --> 659.74]  But I got to this problem and even one of the student groups said, hey, I bought more RAM
[659.74 --> 662.66]  for my laptop to try to solve the problem.
[662.66 --> 664.44]  But then they're like, that's not doing it.
[664.52 --> 667.00]  So then they started thinking about cloud services.
[667.86 --> 674.54]  So how do you think, Mark, as I guess my question is, as students and maybe people getting into
[674.54 --> 679.94]  the field are kind of making this realization around the resources required to solve actual
[679.94 --> 681.50]  like business problems?
[681.96 --> 687.92]  What are those ways in which they can kind of start dipping their toes into cloud and experiment
[687.92 --> 694.04]  with things to kind of expand their horizons in terms of what's possible without, you know,
[694.10 --> 699.36]  knowing about maybe people don't know about Docker and Kubernetes and like all that stuff yet,
[699.36 --> 701.24]  but they want to start dipping into more resources.
[701.24 --> 705.64]  What's a good way for people to kind of get into that as you've seen these students kind
[705.64 --> 706.16]  of do that?
[706.62 --> 706.76]  Sure.
[706.92 --> 712.14]  And I think there's more resources available more than ever to do self-learning.
[712.86 --> 717.84]  And it was maybe 10 to 15 years ago where it was very common to go to a bookstore and
[717.84 --> 719.96]  find these big, thick books on Microsoft.
[719.96 --> 721.48]  With animals on the front and such.
[721.48 --> 721.86]  Yeah, maybe.
[722.46 --> 726.22]  They, you know, they would be training books for technologies.
[727.04 --> 729.22]  And of course, the publishers are still out there.
[729.22 --> 731.32]  O'Reilly is still out there producing books.
[731.48 --> 737.68]  And I have a friend, by the way, who's coming out this month with his book on practical machine
[737.68 --> 739.66]  learning and AI, Jeff Proces.
[739.88 --> 742.24]  And I'm so proud of him to write a new book.
[742.68 --> 745.56]  But the point is that so many things are online.
[745.84 --> 751.56]  And in the Microsoft ecosystem, there was a time when you had to pay to even get the proceedings
[751.56 --> 752.44]  from a conference.
[752.82 --> 755.20]  Like you didn't even go and you couldn't even get the recordings.
[755.20 --> 760.02]  Well, now Microsoft's making a lot of that available for free and in a way that people
[760.02 --> 760.76]  can find it.
[761.02 --> 767.64]  And so I think for the audience of this podcast, I would love to have them look on YouTube,
[767.86 --> 768.84]  what's available there.
[768.92 --> 772.44]  Microsoft's got a few channels of content on there.
[772.78 --> 774.58]  And that's a good way to get started.
[774.80 --> 778.04]  Sometimes they're short sessions between five and 10 minutes.
[778.18 --> 779.82]  Sometimes they go to an hour.
[780.34 --> 782.50]  But that's definitely one way to get started.
[782.50 --> 782.94]  Yeah.
[783.08 --> 784.28]  And could you help us?
[784.38 --> 787.84]  I think it's good for people to kind of organize certain categories in their mind.
[787.90 --> 793.72]  I've heard students talk about like the Microsoft Azure kind of studio environment.
[793.72 --> 799.56]  And then there's other things like these like cognitive services and like managed AI services.
[799.56 --> 801.86]  So how do these things differ?
[801.86 --> 805.04]  And like how might they be used?
[805.26 --> 809.50]  Or how have you seen them being used either in this competition or other places?
[809.50 --> 810.02]  Okay.
[810.28 --> 813.90]  So the unifying thing is either, and you can pronounce either Azure or Azure.
[814.30 --> 814.90]  Both correct.
[815.08 --> 815.64]  Both correct.
[815.94 --> 816.22]  Good.
[816.56 --> 818.80]  It's good to have the definitive answer on that.
[818.80 --> 821.06]  This is the definitive answer for all time.
[821.60 --> 823.96]  I tend to use Azure, but just because I'm out of habit.
[824.52 --> 828.40]  You know, the unifying factor is Azure Active Directory.
[828.68 --> 833.42]  So that's the main authentication path to going into an Azure subscription.
[833.98 --> 837.44]  And the subscription itself is, you know, think about it like a credit card.
[837.44 --> 844.88]  And there, you know, when you sign up for subscription, you would have to put your credit card on there to, you know, pay the bills.
[845.52 --> 847.10]  Again, another free path.
[847.72 --> 849.16]  Microsoft offers a lot of things.
[849.30 --> 852.82]  We have free subscriptions and we even send our customers to go get them.
[853.20 --> 856.34]  And I even tell my customers, I say, you know, it does run out.
[856.64 --> 861.06]  So I say, well, go make a new email at Outlook.com and then just make a new one.
[861.16 --> 861.38]  All right.
[861.38 --> 866.24]  We want you to get hands on because there's no substitute for experience.
[866.64 --> 868.66]  And that's even kind of the point of this competition.
[868.98 --> 870.16]  You know, you can study it in the book.
[870.24 --> 871.64]  You can do class exercises.
[872.38 --> 873.90]  But two things are true.
[874.04 --> 877.20]  First of all, putting into practice and working as a team.
[877.68 --> 879.24]  And that's what we're doing in this competition.
[879.24 --> 892.58]  So back to your earlier question, now that a team may all join the same subscription, the Azure Machine Learning Studio is our flagship technology for machine learning.
[892.92 --> 896.58]  And it can run on regular CPU or GPU instances.
[897.34 --> 899.62]  We have regions available around the world.
[900.02 --> 901.50]  I happen to work in the federal space.
[901.60 --> 904.56]  So we also have specific clouds just for that use.
[904.56 --> 907.48]  And there's different sovereign clouds now.
[907.98 --> 912.62]  And Microsoft's now beginning to build out specialty clouds on top of our regular clouds.
[912.98 --> 914.48]  And also call out to for students.
[914.66 --> 919.62]  We have a lot of promotionals for students where they get things at a discount rate and also nonprofits.
[919.92 --> 924.04]  Nonprofits will get special treatment inside the Azure ecosystem.
[924.40 --> 926.10]  But let me go back to the original question.
[926.34 --> 926.52]  All right.
[926.64 --> 929.92]  So there are two focuses that people will have.
[929.92 --> 931.02]  One is machine learning.
[931.62 --> 935.30]  And it tends to be thought of now as building a model.
[935.72 --> 938.26]  That is the way kind of to think about the products.
[939.00 --> 943.66]  AI is the marketing term for all our technologies now.
[943.82 --> 946.48]  So if you go to the main website, everything is AI.
[947.14 --> 951.68]  However, inside the Microsoft technology, there are cognitive services.
[952.28 --> 955.06]  And those are considered mostly APIs.
[955.30 --> 956.10]  They're REST APIs.
[956.52 --> 958.68]  And they're already pre-trained models.
[958.68 --> 959.88]  And they do certain things.
[960.56 --> 963.28]  And we've seen some of the teams here at the contest.
[963.44 --> 968.50]  They've been using maybe computer vision or text-to-image or image-to-text.
[969.08 --> 972.52]  You know, those types of technologies are already out there.
[972.84 --> 973.94]  And Microsoft's not unique.
[974.12 --> 975.28]  Other vendors have these.
[975.54 --> 981.30]  And Microsoft is now behind the scenes supporting all open source technologies.
[981.86 --> 985.18]  Some come pre-built inside machine learning studio.
[985.18 --> 989.32]  Like we have a certain version of a Python kernel that will run inside there.
[989.90 --> 990.98]  And another technology.
[991.14 --> 991.24]  Okay.
[991.32 --> 996.90]  So going back to the Azure Machine Learning Studio, we have doubled down on MLflow as the
[996.90 --> 999.22]  way we are organizing our workspace.
[999.56 --> 1004.04]  So on the new version of the API, that is the path forward.
[1004.08 --> 1005.10]  And that is open source.
[1005.10 --> 1008.50]  And could you just describe a little bit what that is, MLflow?
[1008.84 --> 1009.26]  MLflow.
[1009.44 --> 1013.98]  So it is a way to organize experiments and training and models and model deployment.
[1014.24 --> 1020.62]  And it has its own syntax in terms of vocabulary and API, you know, the way to work.
[1021.04 --> 1023.10]  And Microsoft's not alone in using MLflow.
[1023.78 --> 1027.24]  There's other vendors that use MLflow in their technology.
[1027.24 --> 1031.26]  But it is a way to organize kind of the technology and the assets.
[1032.06 --> 1037.72]  And Microsoft decided to make that native to our own API and how that works.
[1038.30 --> 1038.38]  Great.
[1038.56 --> 1038.74]  Yeah.
[1038.96 --> 1044.52]  And I think one of the things, like as we've been in the presentations here today, I think
[1044.52 --> 1048.24]  when I was in grad school, you know, I programmed.
[1048.84 --> 1052.52]  But it was like, you know, I'd use MATLAB or Python or whatever.
[1052.52 --> 1053.62]  And I did some things.
[1053.62 --> 1059.04]  I had no concept of like how infrastructure worked in industry or like, you know, the
[1059.04 --> 1065.08]  whole thing about doing programming and academia, it's just like not always a parallel to industry.
[1065.64 --> 1070.90]  So like coming from the Microsoft perspective, I found it really encouraging to see students,
[1071.00 --> 1076.60]  you know, saying things like object store or, you know, model registry or like these things
[1076.60 --> 1078.54]  and thinking through like the architecture.
[1078.54 --> 1083.84]  And I know that's one of the things in the informs like they emphasize is that sort of
[1083.84 --> 1087.14]  model deployment and model lifecycle management.
[1087.78 --> 1088.40]  So, yeah.
[1088.52 --> 1092.98]  Do you have any words of encouragement for maybe those, you know, listeners who are, you know,
[1093.04 --> 1098.30]  again, getting into this space or maybe they're students in terms of getting hands on with
[1098.30 --> 1103.36]  actual infrastructure that people use in industry and how that benefits kind of, you know,
[1103.52 --> 1107.92]  your understanding of how to create value with what you're producing rather than just
[1107.92 --> 1108.94]  creating a cool model?
[1109.36 --> 1109.56]  Right.
[1109.76 --> 1110.98]  So let me call it a few things.
[1111.04 --> 1115.00]  Now, some people aren't so lucky to be even admitted to Purdue.
[1115.00 --> 1121.04]  And if you were, I would certainly, you know, want to come to a program such as here and
[1121.04 --> 1123.04]  you can participate in all these cool events.
[1123.58 --> 1129.42]  But short of having that, you know, either undergraduate or graduate experience, Microsoft has, and this
[1129.42 --> 1130.82]  is what I believe is the front door.
[1131.38 --> 1133.66]  We have something called AI Business School.
[1133.66 --> 1140.80]  It is a series of courses that show how to tie in the value of AI in a business context.
[1141.30 --> 1145.46]  And a lot of the videos were done by our own leadership and they've shown how we've used
[1145.46 --> 1147.40]  AI inside the Microsoft business.
[1147.82 --> 1153.52]  Now, it's not intended to be a catalog of all possible ideas, but it does kind of cover the
[1153.52 --> 1158.06]  landscape of, you know, along the lines of the informs domains.
[1158.06 --> 1163.32]  It covers the landscape of here's, we have a challenge, here's how we're going to use
[1163.32 --> 1167.84]  data modeling and then put in production, and here's how we're evaluating use.
[1168.32 --> 1169.62]  And it just gets people started.
[1169.92 --> 1174.74]  So it's something I do recommend to my customers because people do have different roles.
[1175.52 --> 1180.00]  And even, you know, what I'm working, we're working on internally, we're now rethinking
[1180.00 --> 1184.48]  through who are the personas of people who touch data projects.
[1184.48 --> 1186.38]  And we talked about the domains, right?
[1186.88 --> 1190.54]  But we're going now to thinking about, all right, so who's that person?
[1190.90 --> 1192.20]  What does that person do?
[1192.42 --> 1193.80]  Are all modelers the same?
[1194.06 --> 1194.94]  We don't think so.
[1195.26 --> 1199.92]  So we're now beginning to think that because we're now serving a large internal community
[1199.92 --> 1202.08]  inside Microsoft in terms of our programming.
[1202.60 --> 1205.12]  So that's the first thing I think about is the AI Business School.
[1205.60 --> 1211.46]  And then also in terms of getting started, we have inside all our technologies, we have
[1211.46 --> 1213.50]  tutorials and samples to get started.
[1213.50 --> 1216.76]  Little sample data sets, notebooks that run quickly.
[1217.28 --> 1220.14]  They don't take hours, but then they show you a variety of things.
[1220.24 --> 1223.88]  They're guided toward, you know, specific outcomes.
[1224.06 --> 1225.12]  They begin to get better.
[1225.26 --> 1230.16]  I mean, I've seen Microsoft examples and how they have grown in the last 15 years, and they're
[1230.16 --> 1232.92]  just getting better and better because they're getting better minds thinking about it.
[1233.66 --> 1238.56]  But I'll also call out, you know, Microsoft also is always looking for partners that want
[1238.56 --> 1239.80]  to share their stories.
[1240.46 --> 1245.30]  And we have a lot of case studies of companies doing things in different industries, whether
[1245.30 --> 1247.14]  it's for-profit or non-profit.
[1247.98 --> 1250.34]  One, I'll call out, you know, one example.
[1250.48 --> 1254.96]  We work with the Metropolitan Museum of Art to digitize their entire holdings.
[1255.40 --> 1260.30]  And I don't know if they did 100%, but just they have the same challenge as a lot of art
[1260.30 --> 1261.36]  owners.
[1261.72 --> 1264.00]  And that is, not all their collection is on display.
[1264.36 --> 1266.92]  And some researchers want to have access to those products.
[1267.00 --> 1272.24]  So that's an example of, you know, anytime we do work with major organizations, we put
[1272.24 --> 1273.32]  those ideas out there.
[1273.78 --> 1279.56]  But more practically, and this may even be helpful for students or users, we have what's
[1279.56 --> 1281.70]  called the Azure Architecture Center.
[1281.70 --> 1285.50]  And inside, we see many architectures, very similar.
[1285.80 --> 1289.50]  By the way, we're only looking at the top presentations, but we are seeing architectures
[1289.50 --> 1290.66]  presented.
[1291.04 --> 1293.12]  It's the type of thing that I do in my own work.
[1293.74 --> 1298.64]  And the architectures will be in there, the diagrams and also the case study of what it
[1298.64 --> 1301.24]  did and, you know, kind of what the use case is.
[1301.64 --> 1308.04]  So it gives people, again, a catalog of different ideas of how do you use the different resources
[1308.04 --> 1309.52]  that are available.
[1309.86 --> 1311.10]  So between all that, it's a lot.
[1311.10 --> 1311.78]  Yeah, yeah.
[1311.86 --> 1312.82]  Thank you so much, Mark.
[1313.12 --> 1319.54]  We'll definitely link both to Informs, what they're doing to Purdue and the BAME program
[1319.54 --> 1323.98]  and to these resources from Microsoft in our show notes for the podcast.
[1324.32 --> 1326.18]  So make sure and check all those things out.
[1326.32 --> 1329.96]  Thank you again, Mark and Matthew, for what you're doing on this.
[1330.10 --> 1332.68]  And I'm looking forward to hearing the rest of the presentations.
[1333.12 --> 1333.56]  Thank you, Dan.
[1333.78 --> 1334.12]  Thanks.
[1341.10 --> 1343.30]  All right.
[1343.38 --> 1348.86]  Well, I'm here with the winning undergrad team from the competition, the image captioning
[1348.86 --> 1351.26]  competition, which is from Butler University.
[1351.26 --> 1355.98]  I've got Chris Stein, Andrea Markey, and Aaron Pinner with us.
[1356.10 --> 1360.58]  So congratulations on winning the undergraduate portion of the competition.
[1361.24 --> 1361.36]  Yeah.
[1361.42 --> 1362.24]  Thank you very much.
[1362.52 --> 1363.04]  We are thrilled.
[1363.28 --> 1363.52]  Yeah.
[1363.52 --> 1366.28]  So your solution was really interesting.
[1366.46 --> 1370.96]  Actually, all the undergraduate presentations, I was surprised they seemed like graduate student
[1370.96 --> 1371.58]  work to me.
[1372.18 --> 1374.06]  But tell us a little bit.
[1374.14 --> 1376.98]  So the task, again, was image captioning.
[1376.98 --> 1384.86]  So just tell us one highlight about maybe one of the challenges that you faced in the competition.
[1385.66 --> 1391.30]  So I think that one of the big challenges in this case was about the data set.
[1391.72 --> 1398.68]  Because for certain languages, like the house languages that we have to work on, the data
[1398.68 --> 1400.04]  set was kind of small.
[1400.68 --> 1404.96]  And also, there were not much variety into the pictures.
[1404.96 --> 1407.74]  So that was the biggest challenge.
[1408.06 --> 1416.66]  So we kind of overcome that challenge by either artificially augmenting the data set or adding
[1416.66 --> 1418.54]  new pictures to the data set.
[1418.70 --> 1418.94]  Great.
[1419.24 --> 1419.44]  Yeah.
[1419.94 --> 1426.00]  And specifically, part of the competition was thinking about different languages where maybe
[1426.00 --> 1427.62]  image captioning isn't supported.
[1427.96 --> 1432.42]  And I think one of the things I appreciated about your all's presentation as well was thinking
[1432.42 --> 1438.48]  through the business implications of something like this technology of image captioning that
[1438.48 --> 1443.40]  could enable new or expanded possibilities for local language communities that don't have
[1443.40 --> 1444.24]  this technology.
[1444.70 --> 1449.70]  Could one of you comment on maybe what you envision in terms of the impact something like this
[1449.70 --> 1454.18]  could make in terms of image captioning for a language where it's not supported yet?
[1454.18 --> 1454.66]  Yeah.
[1455.10 --> 1460.94]  So our idea was almost to create a web app or a mobile app that small businesses using
[1460.94 --> 1466.28]  like Kyrgyz or Thai or these small languages could go on this app and submit their photos
[1466.28 --> 1466.54]  there.
[1466.82 --> 1466.90]  Right?
[1467.00 --> 1469.94]  So everyone's got a cell phone in all communities nowadays.
[1470.32 --> 1475.52]  And if they can utilize that cell phone to almost leverage it and upload those pictures
[1475.52 --> 1480.08]  right then and there and get it captioned, that is handy for the small business and SIO and
[1480.08 --> 1480.52]  their mission.
[1480.52 --> 1484.92]  You know, a small business would want to use this because, you know, a lot of people are
[1484.92 --> 1486.66]  drawn to websites because of images.
[1486.76 --> 1488.28]  They click on images in Bing and Google.
[1488.80 --> 1494.40]  So if we can help small businesses, especially if they have a user base with a minority language,
[1494.50 --> 1496.94]  you know, that helps both SIL and the company.
[1497.40 --> 1501.58]  So really, you know, there's a monetary win, but really we're, you know, helping the world
[1501.58 --> 1501.90]  in a way.
[1502.04 --> 1502.82]  So it's really neat.
[1503.04 --> 1503.12]  Yeah.
[1503.28 --> 1503.44]  Yeah.
[1503.44 --> 1508.68]  And also, sorry, if I can add something like last night we had a brief talk, you know,
[1508.92 --> 1510.74]  about, you know, the languages around the world.
[1510.74 --> 1517.18]  And so also there is not only a business implication to this challenge, but we know that also we
[1517.18 --> 1520.04]  are losing a cultural heritage.
[1520.44 --> 1525.72]  Like you mentioned last night that every two weeks one language is lost forever.
[1525.72 --> 1526.12]  Right.
[1526.12 --> 1530.22]  So there is no way that we can keep those languages alive.
[1530.82 --> 1537.12]  So if this can also help make the world more open towards, you know, those small communities,
[1537.66 --> 1542.42]  you know, this is also a good thing also for the world because it makes the world a more
[1542.42 --> 1543.70]  interesting place.
[1543.80 --> 1544.02]  Right.
[1544.44 --> 1544.66]  Yeah.
[1545.04 --> 1545.26]  Yeah.
[1545.64 --> 1546.00]  Awesome.
[1546.12 --> 1548.90]  And maybe a comment from Aaron.
[1548.90 --> 1554.84]  Aaron, as far as this competition, maybe what's one of the highlights of something that you
[1554.84 --> 1559.70]  learned throughout the competition that you view differently now, either in terms of the
[1559.70 --> 1564.56]  technical challenges and that side of things or the business problem or something that you'll
[1564.56 --> 1566.72]  carry with you throughout the rest of your work.
[1567.36 --> 1567.56]  Yeah.
[1567.64 --> 1572.22]  I think one thing I learned was just, I think the challenge really opened my eyes to like this
[1572.22 --> 1573.20]  problem that existed.
[1573.20 --> 1579.28]  I would have never thought about like using AI or machine learning in a way that like directly
[1579.28 --> 1580.12]  impacts languages.
[1580.52 --> 1584.36]  So I think that was definitely something I learned and was really interesting.
[1584.80 --> 1585.32]  Great.
[1585.66 --> 1587.46]  Well, congratulations again.
[1587.96 --> 1590.62]  Hope your travels back home are safe.
[1590.82 --> 1592.26]  And yeah, congratulations.
[1592.52 --> 1593.30]  Hope to stay in contact.
[1593.70 --> 1593.84]  Yeah.
[1593.88 --> 1594.52]  Thank you very much.
[1594.62 --> 1594.92]  Thank you.
[1603.20 --> 1603.76]  Okay.
[1604.00 --> 1610.52]  Well, I'm with now the winning graduate team from the Purdue Using Analytics and Data Science
[1610.52 --> 1611.60]  for Good competition.
[1612.12 --> 1613.70]  This team is from Georgia Tech.
[1613.80 --> 1619.26]  Here I have with me Harsha, Varun, Ravi, and there was another team member, Sanchita, who
[1619.26 --> 1624.64]  couldn't make it to the competition here in person, but want to acknowledge her and her contribution.
[1624.98 --> 1625.96]  So congratulations.
[1626.44 --> 1633.18]  First of all, you all are the first out of, I think it was 170 something teams in this
[1633.18 --> 1639.96]  competition to come up with an image captioning model that performs well on three sort of
[1639.96 --> 1643.84]  diverse languages from around the world, Thai, Kyrgyz, and Hausa.
[1644.42 --> 1645.88]  So first off, congratulations.
[1646.38 --> 1652.08]  And I think one of the things that was really interesting to me about your all solution is
[1652.08 --> 1658.84]  one, kind of looking to state of the art models like Clip, which was something that featured
[1658.84 --> 1665.70]  in your solution, but then also using sort of a multi-stage approach where you actually
[1665.70 --> 1671.82]  determined if a caption existed already that you had in a database of captions, and then if it didn't
[1671.82 --> 1673.96]  exist, generating a caption.
[1674.58 --> 1680.28]  So could you, one of you describe a little bit about how you kind of eventually got to that solution,
[1680.42 --> 1684.64]  how you considered, you know, using Clip and got to thinking about that direction?
[1684.64 --> 1688.22]  So I think the problem itself was quite challenging.
[1688.50 --> 1693.58]  When you look into the data set and actually see what the data is, you can see poems, you
[1693.58 --> 1698.06]  can see philosophical statements, moral statements, parts of stories.
[1698.52 --> 1703.56]  And if you want to predict these kind of statements, you need information about the previous part of
[1703.56 --> 1707.64]  the story or the further part of the story in order to even build a model.
[1708.14 --> 1713.80]  A zero-shot captioning model is where it's very difficult to achieve a good zero-shot captioning
[1713.80 --> 1716.48]  model for such kind of prediction tasks.
[1717.18 --> 1721.82]  So the next step that we thought was maybe we could do some sort of classification model.
[1722.12 --> 1726.98]  That was the original thought process that we could select from a corpus of sentences.
[1727.20 --> 1729.62]  Can we select a sentence that best matches this?
[1730.20 --> 1733.18]  And from there, we started researching, basically.
[1733.54 --> 1737.10]  And when we went through hugging face models, we found the Clip model.
[1737.26 --> 1738.38]  And then we researched further.
[1738.76 --> 1742.26]  We found a multilingual Clip model that could handle different languages.
[1742.26 --> 1745.00]  And it sort of went through that process.
[1745.42 --> 1747.48]  And when we actually used it, it was decent.
[1747.64 --> 1748.74]  I wouldn't say it was perfect.
[1749.20 --> 1752.58]  But it certainly improved our overall solution quite a bit.
[1753.12 --> 1753.64]  Yeah, yeah.
[1753.78 --> 1761.96]  So when you were thinking about this idea of looking to existing captions and using those
[1761.96 --> 1767.06]  when you could, how often in the data set that you were looking at, which is this Bloom data
[1767.06 --> 1776.18]  set, how often did you have to generate image captions versus maybe looking to a list of captions
[1776.18 --> 1778.02]  and using one that pre-existed?
[1778.02 --> 1783.84]  So even in the training data set where we had the images and all the captions that we needed,
[1784.38 --> 1789.62]  when we actually used the multilingual Clip model, it was more about like 20-30% that were matching.
[1789.94 --> 1791.98]  And we had a very low threshold by that itself.
[1792.20 --> 1797.18]  And we didn't want to lower the threshold because we didn't want to get more false positives in a way.
[1797.76 --> 1800.92]  And basically, we just decided on that threshold.
[1801.02 --> 1802.80]  We didn't do any optimization on that particularly.
[1802.80 --> 1807.60]  From there, when we actually used the model on the test set, we suddenly got a huge jump in the score.
[1808.06 --> 1809.04]  That was basically it.
[1809.20 --> 1811.70]  So we were covering about 20-30% of the images.
[1811.92 --> 1817.22]  Even when you had all the captions for the images, only 20-30% were actually matched by the multilingual Clip model.
[1817.62 --> 1819.72]  All the other images went to the generative model.
[1820.26 --> 1820.40]  Yeah.
[1820.76 --> 1823.60]  And you mentioned sort of Clip, hugging face.
[1823.76 --> 1830.66]  These are all, you know, kind of the industry standard, state-of-the-art sort of things as a team getting into this problem.
[1830.66 --> 1841.56]  What were the kind of challenges that you faced in terms of maybe even finding where to start or maybe it's computational challenges or other issues?
[1842.20 --> 1846.38]  So when we initially started with this data set, we were like, we were stumped, honestly.
[1846.58 --> 1855.70]  Like, we hadn't even heard of a model that could generate like contextual information with as much depth as was required by the solution here.
[1855.70 --> 1864.46]  So, like, as I said, we did our initial EDA with, say, Microsoft Azure using their Computervision API and Translator model.
[1865.08 --> 1869.28]  So, like, we, when we actually used that, we thought, okay, these are reasonable guesses.
[1869.50 --> 1870.98]  Like, okay, human would make these guesses.
[1871.50 --> 1872.52]  But we had to go deeper.
[1872.70 --> 1874.30]  So we had to, like, match.
[1874.86 --> 1876.14]  We had other ideas as well.
[1876.20 --> 1878.68]  Like, we thought of, like, clustering common images.
[1878.68 --> 1885.14]  Maybe they belong to the same story or same piece of their part of a single book or something like that.
[1885.84 --> 1886.14]  Yeah.
[1886.20 --> 1887.56]  So that's how we got started off.
[1887.84 --> 1889.62]  The EDA that we did helped a lot.
[1889.84 --> 1896.52]  Like, understanding that they were poems and stuff mixed into the data helped us look for more deeper models that could generate context.
[1897.04 --> 1897.30]  Great.
[1897.60 --> 1897.88]  Yeah.
[1898.02 --> 1898.22]  Yeah.
[1898.22 --> 1899.68]  Thank you for that info.
[1899.68 --> 1911.70]  So I think, you know, as you look forward to kind of, I mean, I know all of you will be going very far just with the innovations that you've demonstrated here.
[1911.76 --> 1919.22]  I hope that maybe when you own billion-dollar startups, you'll hire me to, like, sweep the floors in your startup or something.
[1919.22 --> 1931.48]  But how do you think kind of working on a solution like this from start to finish has influenced how you'll think about maybe AI or data science problems in the future?
[1931.74 --> 1932.08]  Any input?
[1932.76 --> 1938.96]  So the amount of good that AI can do to the real world people, I have looked at a lot of things that SIL does.
[1938.96 --> 1949.88]  It's actually improving a lot of language proficiency among the students and also increasing the educational rate among the people who are not studying so much.
[1950.28 --> 1956.10]  So the amount of good the data or AI can do will definitely influence our thoughts in future as well.
[1956.58 --> 1964.44]  So it's like the kind of use cases all these things can have on the lives of the people are definitely going to stay in home.
[1964.44 --> 1970.60]  And we will definitely try to contribute wherever we can by keeping this in mind.
[1970.74 --> 1972.74]  So this is going to stay with us forever.
[1973.16 --> 1973.56]  Great.
[1973.70 --> 1973.96]  Great.
[1974.06 --> 1975.52]  Well, thank you for your participation.
[1975.82 --> 1977.02]  And congratulations again.
[1977.10 --> 1978.78]  I hope your travels are safe back home.
[1979.04 --> 1979.50]  Thank you.
[1988.88 --> 1989.78]  All right.
[1989.92 --> 1991.50]  That is our show for this week.
[1991.50 --> 1994.12]  If you dig it, don't forget to subscribe.
[1994.70 --> 1997.30]  Head to practicalai.fm for all the ways.
[1997.80 --> 2003.24]  And if Practical AI has benefited your life, pay it forward by sharing the show with a friend or a colleague.
[2003.56 --> 2006.54]  Word of mouth is the number one way people find shows like ours.
[2006.96 --> 2012.56]  Thanks again to Fastly for fronting our static assets, to Fly.io for backing our dynamic requests,
[2013.10 --> 2015.82]  to Breakmaster Cylinder for the beats, and to you for listening.
[2016.06 --> 2016.70]  We appreciate you.
[2017.04 --> 2017.92]  That's all for now.
[2018.16 --> 2019.60]  We'll talk to you again on the next one.
[2021.50 --> 2051.48]  We'll talk to you again on the next one.
