[0.00 --> 3.66]  You know, the goal is always to get that mom care as quickly as possible.
[3.98 --> 10.32]  We are looking at what other data, what other information will help us increase a risk rating
[10.32 --> 15.62]  for a mother, will help us understand which facility she should be referred to.
[16.02 --> 18.02]  Half of the organization works with providers.
[18.02 --> 22.72]  And so we have a lot of data and insights from that layer of the health system.
[22.92 --> 27.82]  And so can we use these layers of data to really route those moms more effectively to
[27.82 --> 29.28]  care in a timely manner?
[29.28 --> 33.42]  And just scratching the surface of it is to look at conversational history and look
[33.42 --> 38.62]  to see if there are triggers, trigger intents that could be predictive of a future danger
[38.62 --> 39.00]  sign.
[39.30 --> 43.62]  And it actually looks like we may have enough data to develop a model just from the initial
[43.62 --> 44.70]  work that's been done.
[47.34 --> 50.00]  Big thanks to our partners, Linode, Fastly, and LaunchDarkly.
[50.36 --> 50.92]  We love Linode.
[51.00 --> 52.42]  They keep it fast and simple.
[52.56 --> 54.90]  Check them out at linode.com slash changelog.
[55.12 --> 57.20]  Our bandwidth is provided by Fastly.
[57.20 --> 61.10]  Learn more at Fastly.com and get your feature flags powered by LaunchDarkly.
[61.26 --> 63.08]  Get a demo at LaunchDarkly.com.
[63.08 --> 66.96]  This episode is brought to you by our friends at Rutterstack.
[67.18 --> 70.66]  And we're calling all data engineers to check out Rutterstack Cloud and start building smart
[70.66 --> 71.68]  customer data pipelines.
[72.18 --> 73.92]  Rutterstack is warehouse first.
[74.10 --> 75.04]  No more silos.
[75.56 --> 78.90]  Rutterstack builds your customer data lake on your data warehouse, not theirs.
[79.14 --> 84.28]  Enabling all functionality of a CDP with more security and retaining full ownership of your
[84.28 --> 84.60]  data.
[84.86 --> 87.36]  It's open source and API first.
[87.68 --> 91.12]  Rutterstack can be easily integrated into your existing development processes.
[91.12 --> 94.44]  And because they're open source, you can see all their code.
[94.66 --> 97.08]  So you don't have to worry about vendor lock-in or black boxes.
[97.64 --> 99.20]  And best of all, they have transparent pricing.
[99.40 --> 101.64]  Stop paying your CDP a premium to store your data.
[102.12 --> 107.00]  Rutterstack is free up to 500,000 events and pricing scales transparently from there.
[107.46 --> 109.44]  Learn more and get started at Rutterstack.com.
[109.78 --> 112.00]  Again, Rutterstack.com.
[112.14 --> 115.66]  That's R-U-D-D-E-R-S-T-A-C-K.com.
[115.66 --> 117.66]  Rutterstack.com.
[125.52 --> 130.54]  Welcome to Practical AI, a weekly podcast that makes artificial intelligence practical,
[130.84 --> 132.58]  productive, and accessible to everyone.
[132.92 --> 136.98]  This is where conversations around AI, machine learning, and data science happen.
[137.24 --> 141.46]  Join the community and Slack with us around various topics of the show at changeodg.com
[141.46 --> 142.04]  slash community.
[142.24 --> 143.36]  And follow us on Twitter.
[143.36 --> 145.10]  We're at Practical AI FM.
[145.10 --> 154.04]  Welcome to another Practical AI.
[154.46 --> 156.12]  This is Daniel Whitenack.
[156.26 --> 159.92]  I am a data scientist with SIL International.
[160.74 --> 169.22]  And I'm very excited today to be joined from Kenya by Jay Patel, who is technology and analytics
[169.22 --> 170.94]  manager at Jacaranda Health.
[171.10 --> 178.10]  And Sathi Rajasekharan, who is executive director in Africa of Jacaranda Health.
[178.16 --> 178.58]  Welcome.
[179.16 --> 179.78]  Thank you.
[180.04 --> 181.08]  Thanks for having us, Daniel.
[181.50 --> 181.80]  Yeah.
[181.80 --> 184.02]  It's wonderful to talk to you both.
[184.42 --> 188.34]  We've already had a lot of great conversation even before we started recording.
[188.44 --> 190.06]  So I'm really excited about this.
[190.06 --> 195.54]  Maybe Sathi, could you give us a little bit of an introduction to Jacaranda and some of
[195.54 --> 197.34]  the things you're doing and how it came about?
[197.54 --> 198.32]  Yeah, absolutely.
[198.82 --> 205.16]  So Jacaranda is a nonprofit organization that works in Kenya, primarily in Africa.
[205.16 --> 214.24]  And the challenge we're trying to address is one of the fact that mothers and babies die
[214.24 --> 221.06]  during childbirth in this part of the world, probably six or seven times more frequently
[221.06 --> 225.48]  than happens in more developed countries in North America and Europe.
[225.48 --> 231.72]  And we've recognized that it's not really a question of not having enough hospitals or
[231.72 --> 238.98]  providers or services, although there's certainly challenges there, but the quality of care,
[239.16 --> 243.08]  so the kinds of care that are being provided really needs to improve.
[243.68 --> 249.58]  And this has been shown in the literature and by many, many other groups as well as ours.
[250.70 --> 255.46]  And so Jacaranda works with governments, with the government hospitals in kind of
[255.46 --> 259.78]  to try and improve the quality of the care that's being delivered in hospitals.
[260.44 --> 266.76]  And we do that by using low-cost, scalable solutions that can be deployed within government
[266.76 --> 272.36]  hospitals to increase the number of moms who are seeking care at the right time and the
[272.36 --> 276.96]  right place, and to improve the care they're receiving from providers when they actually get
[276.96 --> 277.62]  to a hospital.
[278.22 --> 280.98]  And that's where our digital health tools come in.
[281.32 --> 285.22]  They're one of those low-cost solutions that we're delivering through government hospitals.
[285.74 --> 286.40]  Yeah, that's awesome.
[286.66 --> 289.70]  I really, really appreciate your work in this area.
[290.44 --> 292.90]  Jay, maybe you could sort of give us some context.
[293.20 --> 297.34]  So that's a wonderful story and setup and context.
[297.58 --> 300.22]  But Sathi, you mentioned digital tools.
[300.58 --> 305.82]  Maybe Jay, you could let us know, hey, where does AI and NLP and these sorts of things fit in?
[305.82 --> 309.28]  So why are we talking about this on the Practical AI podcast?
[309.92 --> 310.04]  Sure.
[310.44 --> 316.06]  So what happens when a mother enrolls in our service is that she will first go to one of
[316.06 --> 320.56]  these so far 700 public health facilities that we're partnering with.
[320.98 --> 325.98]  She will enroll in the service and then we will start sending her messages about her health,
[326.10 --> 328.40]  about the health of her baby, about her pregnancy.
[328.40 --> 334.08]  And messages include everything from nutrition all the way up to danger signs.
[334.74 --> 338.78]  And she can then ask us any questions that she has at no charge.
[339.42 --> 342.04]  This is primarily run all off of SMS.
[342.32 --> 343.82]  And again, it's free to the mother.
[344.38 --> 345.74]  Yeah, maybe you could.
[346.12 --> 350.50]  Because I think a lot of times, at least in many people's context, they might be thinking
[350.50 --> 355.60]  about chat as like a little window pop up on their customer service site or something.
[355.60 --> 358.76]  But it sounds like you're focused primarily on SMS.
[359.10 --> 359.52]  Is that right?
[360.00 --> 360.50]  That's correct.
[360.96 --> 365.06]  We checked with our users and more than half of them are still using feature phones.
[365.06 --> 371.14]  So even though mobile phone penetration in Kenya is in the high 90s, a lot of users don't
[371.14 --> 376.02]  have smartphones and are still using, you know, like the old Nokia feature phones.
[376.92 --> 377.06]  Sure.
[377.06 --> 381.60]  And how, so I guess you're having these conversations.
[382.52 --> 390.28]  When did you start thinking about what machine learning or NLP sort of techniques could benefit
[390.28 --> 390.56]  you?
[390.66 --> 392.10]  How did that come about originally?
[392.72 --> 398.16]  I was going to sort of tell the story from the perspective of how Jay came to be part of
[398.16 --> 398.74]  the team.
[399.02 --> 399.56]  That'd be awesome.
[399.82 --> 399.94]  Yeah.
[400.24 --> 400.54]  Yeah.
[400.62 --> 405.54]  You know, we launched a service now four years ago with 200 moms.
[405.54 --> 408.94]  You know, we're super excited that we had 200 moms using the platform.
[409.52 --> 414.36]  It was an accident that we actually opened up two-way communication for free.
[414.78 --> 416.44]  We didn't originally intend for that.
[416.50 --> 420.54]  We just thought we'll send moms a bunch of messages and that'll improve their knowledge
[420.54 --> 421.28]  about pregnancy.
[422.08 --> 428.42]  And then I distinctly remember one of our program team members coming in and saying, hey, these
[428.42 --> 429.62]  moms are asking questions.
[429.92 --> 432.56]  I've been answering them, but the questions are increasing.
[432.56 --> 440.02]  So it turned out we had learned of this latent demand for just a whole bunch of questions
[440.02 --> 441.12]  needing to be answered.
[441.84 --> 443.94]  I mean, you know, back to what Jay was talking about.
[444.10 --> 445.92]  Many of these moms have feature phones.
[446.14 --> 450.84]  Many don't use data on a regular basis because it's still relatively expensive here.
[451.58 --> 454.30]  And so Googling something isn't really an option.
[454.60 --> 457.96]  The complexity of language when you Google something, I mean, we all know it's really hard.
[457.96 --> 462.44]  So the minute they realized someone was sending them messages about their pregnancy, they started
[462.44 --> 463.52]  sending in questions.
[464.24 --> 467.96]  The question volume started increasing as we started to enroll more and more moms.
[468.66 --> 472.36]  You know, we were getting to hundreds of moms per month, to a thousand moms per month.
[472.48 --> 474.92]  We're at almost at a hundred thousand per month now.
[475.64 --> 483.20]  And we pretty early realized, early on realized that we need a way to triage the questions coming
[483.20 --> 483.50]  in.
[483.68 --> 490.54]  So some of the moms were asking about, you know, what can I eat for during pregnancy?
[490.80 --> 493.18]  Is it okay to eat avocados, for example?
[493.48 --> 496.10]  Which is a surprisingly common question that we get asked.
[496.44 --> 502.90]  But out of, you know, every 30 questions we get asked, one or two of them will be really
[502.90 --> 503.50]  serious.
[503.78 --> 505.44]  A mom may say, I'm bleeding.
[505.74 --> 506.58]  What should I do?
[506.58 --> 512.48]  And we recognize that if we sort of did a first in, first out approach to answering questions,
[512.48 --> 517.06]  we'd miss that mom or be late to answering that mom who needed to know about bleeding.
[517.58 --> 523.14]  So our journey to think about machine learning actually came in thinking about how do we effectively
[523.14 --> 525.10]  categorize these messages?
[526.18 --> 529.24]  And I had, this is when we had a tiny team.
[529.24 --> 535.32]  I had been messing about with dialogue flow to see if we could put some of the conversations
[535.32 --> 541.42]  in and quickly, you know, in addition to realizing that we were onboarding more and more users,
[541.88 --> 547.14]  recognizing that we actually needed someone with a lot more development expertise to come
[547.14 --> 553.52]  to the team, which is how Jay comes into the picture and kind of changes the way we do business
[553.52 --> 554.90]  with these incoming questions.
[554.90 --> 559.68]  I'm happy to now hand over to Jay to talk about how he actually solved this challenge.
[560.28 --> 560.42]  Sure.
[560.58 --> 560.76]  Yeah.
[560.86 --> 565.76]  And just before we kick it over there, I guess, so you mentioned Dialogflow Sathi, which is
[565.76 --> 571.30]  offering from Google to help build chat conversations and that sort of thing.
[571.30 --> 576.80]  When you started looking to solve this problem, was it clear that, I guess, machine learning
[576.80 --> 579.80]  and AI even could provide a solution?
[580.16 --> 583.80]  Or was that still something that was relatively unclear?
[583.80 --> 587.00]  You just knew that, you know, technology needed to be brought to the table.
[587.80 --> 587.90]  Yeah.
[587.94 --> 590.72]  We knew tech needed to be brought to the table.
[590.98 --> 595.74]  I was actually, you know, in the ecosystem here in Nairobi, there was a number of people
[595.74 --> 596.96]  working on chatbots.
[597.78 --> 603.16]  And so the original thought was, okay, maybe there's also a chatbot opportunity here where
[603.16 --> 607.74]  we don't even need people at the other end answering questions and we can create conversational
[607.74 --> 611.50]  histories and, you know, intent classification, et cetera, et cetera.
[611.50 --> 619.90]  And I think it just took a few weeks to realize that with the complexity of language and information
[619.90 --> 623.70]  coming through, we'd actually needed a different solution.
[623.90 --> 627.22]  So this automated chat idea was quickly discarded.
[627.58 --> 632.84]  Also from a user perspective, moms didn't seem to like getting these kind of cookie cutter
[632.84 --> 638.16]  responses back from whoever was on the other end of the texting service.
[638.16 --> 644.38]  Yeah, that's definitely something I've run into as well in working in chat and dialogue.
[644.64 --> 646.08]  So yeah, that's interesting.
[646.34 --> 652.28]  So Jay, how did then when you started approaching this problem and getting involved, what was
[652.28 --> 656.36]  the process like in terms of figuring out what was the right tech solution?
[656.36 --> 664.52]  We were initially connected to a gentleman by the name of Matt Capers, works in Square in
[664.52 --> 665.14]  Silicon Valley.
[665.62 --> 668.88]  He volunteered to help us figure this kind of stuff out.
[669.54 --> 673.66]  And we started out by testing various solutions.
[673.88 --> 680.08]  So the data set that Sati had put together from the previous two years, we used that.
[680.40 --> 683.58]  This was a list of questions that moms had asked us.
[683.58 --> 690.88]  And so we took a few thousand of them and had our team label the questions according to
[690.88 --> 692.16]  what the mom was asking.
[692.24 --> 693.32]  So just a one word label.
[693.74 --> 695.30]  And it could have been nutrition.
[695.58 --> 697.22]  It could have been something else.
[698.34 --> 706.72]  And we fed this list of intents into the three most popular, like off the shelf commercial
[706.72 --> 707.94]  models of it.
[708.02 --> 711.56]  In fact, four NLP models that were available at the time.
[711.56 --> 717.84]  Dialog flow was one, then the usual suspects between Google, Amazon, and Microsoft.
[719.80 --> 728.04]  And after some testing, it became apparent that Google's NLP for this particular use case
[728.04 --> 729.26]  was most useful.
[729.94 --> 732.56]  And so then we took a larger data set.
[732.64 --> 735.46]  I think it was something like 13,000 questions.
[735.46 --> 741.96]  And the way we figured is to run each of these questions through a translator.
[742.56 --> 747.48]  And then the output of the translator, along with the intent that we had classified for
[747.48 --> 752.36]  each question, would be used to train the model.
[753.12 --> 758.90]  After that, it then took a little bit of extra figuring out, you know, how granular do we want
[758.90 --> 759.68]  the intents to be?
[759.68 --> 768.60]  So we could have four or five very broad intents, or we could have many dozens of, or 50, you
[768.60 --> 770.98]  know, or 60, very, very fine grained intents.
[771.68 --> 777.38]  And it turned out that the best mix was kind of like the middle, the Goldilocks middle.
[777.52 --> 782.26]  So we ended up with an intent list, which was about 33 in length.
[782.26 --> 789.50]  And I mean, that sounds like a pretty labor intensive process getting through that data
[789.50 --> 789.90]  labeling.
[790.16 --> 798.16]  What was that process like in terms of actually getting into this task of data labeling?
[798.70 --> 801.26]  And what challenges along the way did you face there?
[802.08 --> 804.14]  Yeah, it was quite labor intensive.
[804.30 --> 805.12]  It was very manual.
[805.52 --> 811.94]  So we just threw up, you know, all 13,000 questions on a spreadsheet and then assign a few
[811.94 --> 816.94]  members of the team to go in and read each question and actually assign a label from a
[816.94 --> 818.28]  list that we had predefined.
[818.44 --> 821.80]  And then, you know, they'd have the option to add labels as they went along.
[822.28 --> 827.38]  That took several weeks and it took, you know, a lot of our team members time when they could
[827.38 --> 828.54]  have been doing other things.
[829.56 --> 829.96]  But we couldn't.
[830.06 --> 833.98]  Yeah, everyone was super nice to volunteer to do it, for sure.
[835.20 --> 839.44]  Yeah, you need some grace from people when you're asking for that sort of task.
[839.44 --> 843.08]  But I'm sure hopefully now they see some of the value coming through from that.
[843.86 --> 844.70]  Yeah, for sure.
[844.94 --> 851.58]  One other challenge, you know, this is still something that we work on is the sort of specificity
[851.58 --> 852.82]  of labeling something.
[853.00 --> 855.76]  You know, there's a lot of subjectivity involved, right?
[855.80 --> 862.48]  Like if a mom texts in and says, my baby hasn't stopped crying, someone may label it as, you
[862.48 --> 863.32]  know, crying baby.
[863.32 --> 866.30]  And someone else may label it as general baby concern.
[867.04 --> 872.62]  And so we learned the hard way that we needed to do a lot of training around what is it that
[872.62 --> 874.34]  we mean for each of these labels.
[874.86 --> 879.22]  So I think that was the tougher part, certainly for this initial data set.
[879.46 --> 881.28]  But we did, you know, Jay will talk about this.
[881.38 --> 886.94]  We did a much bigger round of training a year later and had to put in a lot more rigor to
[886.94 --> 888.02]  the process after that.
[888.02 --> 888.52]  Yeah.
[888.52 --> 888.82]  Yeah.
[888.82 --> 889.02]  Yeah.
[889.02 --> 889.52]  Yeah.
[889.52 --> 890.02]  Yeah.
[890.02 --> 890.52]  Yeah.
[890.52 --> 891.02]  Yeah.
[891.02 --> 891.52]  Yeah.
[891.52 --> 892.02]  Yeah.
[892.02 --> 892.52]  Yeah.
[892.52 --> 893.02]  Yeah.
[893.02 --> 895.02]  Yeah.
[897.02 --> 903.42]  Signal Wire is real time video tech to help you create interactive video experiences previously
[903.42 --> 904.08]  not possible.
[904.52 --> 910.40]  It gives you access to broadcast quality, ultra low latency video that's proven and trusted
[910.40 --> 913.56]  by Amazon, Ring Doorbell, Zoom and others.
[913.90 --> 917.92]  See why the future of video communication is being built on Signal Wire.
[917.92 --> 923.00]  They have easy to deploy APIs, SDKs for the most popular programming languages,
[923.02 --> 927.56]  and expert support from the OGs of software-defined telecom tech.
[927.56 --> 933.58]  Try it today at SignalWire.com and use code AI for $25 in developer credit.
[933.58 --> 934.58]  Just visit SignalWire.com.
[934.58 --> 936.18]  Just visit SignalWire.com.
[936.18 --> 940.58]  That's SignalWire.com and use code AI to receive that $25.
[940.58 --> 944.78]  Once again, that's SignalWire.com, code AI.
[944.78 --> 945.78]  Bye.
[945.78 --> 949.38]  Bye-bye.
[949.38 --> 950.76]  Bye-bye.
[950.76 --> 954.26]  Bye-bye.
[954.26 --> 954.98]  Bye-bye.
[954.98 --> 955.72]  Bye-bye.
[955.72 --> 956.78]  Bye-bye.
[958.42 --> 959.12]  Bye-bye.
[959.12 --> 960.56]  Bye-bye.
[960.56 --> 962.62]  Bye-bye.
[962.62 --> 963.20]  Bye-bye.
[963.20 --> 963.54]  Bye-bye.
[963.54 --> 969.36]  So, Sathy, you just mentioned how there was kind of this initial round of labeling and
[969.36 --> 975.44]  defining the different classes that you're working with. And then as you went along in that process,
[975.44 --> 981.44]  you realized you needed more data and to kind of switch up the labeling. Jay, what did that
[981.44 --> 988.14]  process look like in terms of training maybe a bigger model with more data? How did you go about
[988.14 --> 995.52]  that scaling and what was needed to facilitate that? So when we had run the first round of
[995.52 --> 1001.26]  labeling, we hadn't even collected that many questions. Then across the following year,
[1001.76 --> 1005.52]  as the questions, as the service grew and the questions continued to come in, we just
[1005.52 --> 1012.08]  basically stored them somewhere. At the end, we had over 100,000 questions, but we decided to limit
[1012.08 --> 1020.30]  the labeling exercise to 100,000 questions. Along with the questions, the help desk also had now
[1020.30 --> 1027.50]  much more experience on what kinds of questions that they get. And so instead of me or Sati pulling
[1027.50 --> 1035.66]  together a list of intents, we asked the help desk to help us figure out what now that we're evolving
[1035.66 --> 1042.24]  to a second version, what's the best list of intents and do we expand this? Are there, for example,
[1043.08 --> 1048.02]  if you have an intent for general baby concerns, how can you break that down and how do we make it
[1048.02 --> 1054.72]  more specific? What are the questions that come in that are being caught as general baby that we can
[1054.72 --> 1062.04]  identify better or help triage better? And this time we had to outsource and we used a service that
[1062.04 --> 1067.86]  or a company that actually helped us go through and label each of these 100,000 questions.
[1068.26 --> 1075.00]  But as Sati mentioned, we had to train the team and then the training had to be quite rigorous.
[1075.00 --> 1081.22]  But even after the training, we had to go through several rounds of cleaning and just making sure
[1081.22 --> 1088.94]  that what we might identify as one particular intent was identified by the team as another
[1088.94 --> 1092.86]  intent because they're not really exposed to the work we do on a daily basis.
[1093.32 --> 1100.14]  Yeah, that brings up a really interesting question, which is striking me is that there's probably a lot
[1100.14 --> 1106.16]  of I imagine there's a lot of health expertise within your team and those that you're working
[1106.16 --> 1112.46]  with, but it sounds like you're not primarily a machine learning startup or something like that.
[1112.96 --> 1121.08]  So what was it like culture wise? And when you're explaining what you're trying to do to your team,
[1121.30 --> 1129.12]  to your board of directors, to those you're serving, how did that sort of culture change happen?
[1129.12 --> 1134.78]  And what strategies did you employ to sort of help you bring along people with the solutions
[1134.78 --> 1137.62]  that you were trying to build? Maybe that's a question for Sati.
[1138.26 --> 1145.46]  Yeah, I think one thing that Jay and the team do really well is try and frame for the team,
[1145.72 --> 1150.24]  how is this going to make your life easier, right? If we're able to label questions,
[1150.80 --> 1154.98]  you get to prioritize them, then you can tag the high priority ones first.
[1154.98 --> 1161.34]  But actually, what was even more exciting was what if we could automate responses to a class of
[1161.34 --> 1170.56]  questions that we are 95% certain of in terms of intent classification. And that reduces the volume
[1170.56 --> 1177.62]  for the help desk. So by sort of sharing, what does this mean for you at the front lines, essentially,
[1177.62 --> 1183.56]  I think Jay and the rest of the team really brought everyone into this kind of, this is a shared
[1183.56 --> 1191.86]  mission mindset versus, oh, it's the tech team doing something, you know, AI-esque again. So what's
[1191.86 --> 1197.96]  really cool is everyone talks intense and classification now on the help desk team, they all know what they're
[1197.96 --> 1202.92]  looking at. It's really fun to watch that journey. It has been fun to watch it over the last couple of
[1202.92 --> 1208.84]  years to see people kind of ignore what me and Jay were doing in the background to now being,
[1208.94 --> 1211.10]  you know, front and center and understanding how it works.
[1211.42 --> 1217.00]  And that's really cool to hear. I think that many of us in different organizations listening to this
[1217.00 --> 1223.20]  are probably, you know, wishing and hoping we can bring along our teams in that same way and build
[1223.20 --> 1228.54]  that excitement. I'm assuming part of that is, you know, you talk to them about those pain points,
[1228.54 --> 1235.18]  but then also they actually saw value out of what you were producing. How quickly did it,
[1235.34 --> 1241.38]  that bit happen? How soon was it in terms of the time when you first started showing them maybe
[1241.38 --> 1247.36]  prioritization of questions or classification of questions and when they were actually seeing
[1247.36 --> 1251.18]  value out of that? How was that rollout period? How did that happen?
[1251.72 --> 1254.88]  I mean, I have an opinion. I'd love to hear Jay's opinion. I actually think
[1254.88 --> 1261.20]  we were more excited about the classification and the sort of, you know, precision and recall
[1261.20 --> 1266.82]  that we were getting after the first training round. But then after a while, we realized the
[1266.82 --> 1271.92]  help desk team was like, yeah, it doesn't really work that well, which is what really pushed us to
[1271.92 --> 1277.72]  try and improve the classification. And I say us, but I mean, Jay and the team really worked on,
[1277.72 --> 1283.94]  you know, capturing statements like when someone says yes or thank you, how do you filter that out?
[1283.94 --> 1290.92]  The sort of real life annoying things that happen when you run something at a relative scale. We're
[1290.92 --> 1297.56]  doing 2,500 questions now. I think questions per day. I think where we really started to see
[1297.56 --> 1304.10]  it making a difference is once those practical things were ironed out, then I think the team
[1304.10 --> 1309.90]  started to see, huh, this actually works. And that's what enabled us to get their buy-in to do that
[1309.90 --> 1314.28]  bigger round of training later. I don't know, Jay, what do you think? Does that track or is that just
[1314.28 --> 1316.14]  my assumption from high above?
[1316.88 --> 1321.40]  No, that makes sense. And there was a lot of hiccups getting it to work. There's a lot of
[1321.40 --> 1326.76]  patients from the team, especially the help desk on maybe they don't have full context on why it's
[1326.76 --> 1333.24]  working, but they had enough trust in us to let us be about experimenting. And as you mentioned,
[1333.24 --> 1338.74]  once we get, once we figure out how to filter the stuff that the help desk doesn't need to answer,
[1339.58 --> 1345.44]  that's when they really bought into, okay, now this is how it's having a practical impact on my day.
[1346.24 --> 1351.82]  Makes sense. So I'm always interested, if you listen to the podcast, in the very practicalities of how
[1351.82 --> 1358.08]  this all works, which you've brought up, Jay. And one curiosity I'm having is around the integration
[1358.08 --> 1363.80]  of all of this. I think one of the areas that machine learning and AI practitioners often get
[1363.80 --> 1370.26]  blocked in is, you know, they can train a model, but sort of integrating it in a workflow or in
[1370.26 --> 1376.82]  existing systems is often very difficult and error prone. It sounds like you're dealing with SMS here.
[1376.82 --> 1383.32]  And I know that there's APIs like Twilio and other things that you can use to interact via SMS,
[1383.32 --> 1388.32]  but then, you know, you've got your model sitting somewhere. I don't, I don't know where that's,
[1388.32 --> 1392.66]  you know, stored and sitting. And then somehow you've got to integrate those things together
[1392.66 --> 1398.80]  along with actual humans in the loop. So what does that integration piece look like for Jacaranda?
[1399.60 --> 1406.12]  So on one, one end, we have a messaging platform that's called Rapid Pro that's plugged into the
[1406.12 --> 1413.30]  telcos and handles the traffic for the SMS. On the other end is the ticketing platform or the
[1413.30 --> 1421.36]  ticketing software where the help desk is responding to these messages. And the triage or the NLP model
[1421.36 --> 1426.06]  sits in the middle. And what happens is just by reading and writing the APIs for these three
[1426.06 --> 1432.48]  platforms, we grab the messages as they come in, run them through the translator, run them through
[1432.48 --> 1438.78]  then the NLP model. And all the information that comes out of both of these gets posted to the
[1438.78 --> 1444.72]  ticketing platform. Any responses then go straight out the other way, but bypassing the middle bit
[1444.72 --> 1450.56]  and hit Rapid Pro just for delivery to the mother. But basically all this was integrated by way of the
[1450.56 --> 1458.12]  APIs for the three platforms. You know, Daniel, I was just thinking that as reflecting, as we're talking
[1458.12 --> 1464.58]  about this, we used to be really cagey about talking about, oh, do we use, you know, Google's platform or
[1464.58 --> 1471.86]  IBM, whatever. And the sort of the real experience has been that it's what Jay affectionately calls the
[1471.86 --> 1478.58]  glue that holds all this together is really where all the hard work and iteration and innovation came
[1478.58 --> 1484.68]  in. The development of a ticketing software that works with this workflow and can incorporate the AI
[1484.68 --> 1492.32]  in a useful way. That's actually been the sort of innovation here over and above the use of machine
[1492.32 --> 1498.70]  learning or NLP in what we do. And so it's kind of fun to hear our evolution of caginess being like,
[1498.78 --> 1504.66]  now we just, we tell everyone what we do, but we recognize that there's so much stacked in here that
[1504.66 --> 1508.90]  is unique to what, what Jacaranda does that we don't have to be super cagey about it anymore.
[1508.90 --> 1515.88]  Yeah, that's a very interesting observation, Satya. And I think it's true that, you know, it's one thing
[1515.88 --> 1521.52]  that you can go to like GitHub or somewhere and you can just see all the implementations of all of these
[1521.52 --> 1527.62]  models that people are releasing and, you know, state of the art models, but the process of getting that to
[1527.62 --> 1534.42]  work for you and your context and integrated with your systems and your employees and that glue, like you
[1534.42 --> 1542.36]  mentioned. To me, that's, that's almost always where projects get blocked or held up. And so sharing
[1542.36 --> 1548.92]  sort of what you're doing in the sense of the AI or NLP side actually is in some ways, you know, it's
[1548.92 --> 1555.28]  significant. It's definitely a driving factor, but it's only a small factor of a much larger system
[1555.28 --> 1561.26]  that needs to be put into place. So yeah, I definitely, I definitely appreciate that comment and
[1561.26 --> 1567.04]  context for our listeners as well. I know. So one of the things that was mentioned very briefly,
[1567.04 --> 1571.94]  I forget who mentioned it was translation. So I want to talk about that a little bit more,
[1572.02 --> 1577.34]  but maybe before we talk about that, could one of you maybe just describe a little bit for those that
[1577.34 --> 1583.84]  aren't familiar with Kenya or African languages, what is the sort of linguistic diversity look like
[1583.84 --> 1591.40]  where you're at? So in Kenya, you know, we have two major languages in the country. So that's English
[1591.40 --> 1598.60]  and Swahili, but of course you have local languages in the various regions, the various counties that we
[1598.60 --> 1606.74]  have. And then you have dialects of those languages as well. Because of the strong public education system
[1606.74 --> 1612.90]  that the country's had, you're actually, we're actually quite lucky that we can send text-based
[1612.90 --> 1618.56]  information and receive text-based information primarily in English and Swahili because, you know,
[1618.74 --> 1624.44]  everyone is comfortable texting in that. The one challenge, and this is a pretty big challenge,
[1624.44 --> 1631.44]  is when you start to see a mixture of the languages and more informal Swahili, which is known as
[1631.44 --> 1639.44]  Sheng. So you get a real mishmash of languages, more hip words coming in, and that tends to
[1639.44 --> 1645.04]  break things a little bit. Although I believe now we've gotten around it. Niyana Jay, do you want to
[1645.04 --> 1651.60]  talk about some of those language-related issues? Yeah. So most of the messages we get,
[1652.24 --> 1660.36]  some 60 or 70% are in Swahili, but not pure Swahili. It's always a mixture of Swahili and English.
[1660.36 --> 1666.08]  And even the English messages have Swahili words in them. But the shang or the slang, as Sati mentioned,
[1666.08 --> 1672.86]  that in itself is a mixture of English and Swahili and other languages. And it evolves quite quickly.
[1673.44 --> 1680.94]  And so it's not something that is maybe as stable as an official language. And when we're running all
[1680.94 --> 1687.52]  of this through the translation, what comes out at the other end is quite often very garbled and often
[1687.52 --> 1694.86]  doesn't resemble what the original question was. However, the NLP model seems to be able to parse it
[1694.86 --> 1701.86]  for context and apply the correct intent most of the time. And we have gotten the accuracy to about
[1701.86 --> 1710.78]  87 odd percent for general questions and for danger sign questions. It's in the mid to low 90s.
[1710.78 --> 1713.06]  And we'll continue to try and improve that.
[1724.86 --> 1730.86]  So
[1730.86 --> 1738.28]  changelog plus plus is the best way for you to directly support practical AI. Join today and unlock access
[1738.28 --> 1744.42]  to a private feed that makes the ads disappear, gets you closer to the metal and help sustain our
[1744.42 --> 1751.30]  production of practical AI into the future. Simply follow the changelog plus plus link in your show
[1751.30 --> 1757.18]  notes or point your favorite web browser to changelog.com slash plus plus. Once again,
[1757.18 --> 1760.30]  that's changelog.com slash plus plus.
[1760.30 --> 1781.20]  So Jay, you're mentioning some of the results and the sort of current state of what you're
[1781.20 --> 1785.66]  doing. You mentioned there's kind of these different categories of questions and you're
[1785.66 --> 1791.42]  tracking your metrics in those different areas like danger sign questions and others. Could you
[1791.42 --> 1797.90]  just describe maybe a little bit the makeup of your data set in terms of how many of these questions
[1797.90 --> 1804.24]  that are coming in are sort of danger sign questions that you need to triage with very high priority and
[1804.24 --> 1810.16]  what sorts of questions are those and what does that percentage look like with in terms of the rest of the
[1810.16 --> 1812.28]  questions and general information questions?
[1812.70 --> 1818.72]  So about 30% of the questions that come in could potentially be a danger sign and danger signs include
[1818.72 --> 1827.40]  questions like bleeding or I have swelling in my in my feet and my legs. I have a headache and of those
[1827.40 --> 1835.50]  30% I think overall of out of the questions might be three or 5% which are actual danger signs.
[1836.36 --> 1844.18]  And what we're trying to do is throw a wider net so that even if we capture a lot of questions which
[1844.18 --> 1851.22]  are not strictly a danger sign, we want to make sure that we do capture those which are and the help desk
[1851.22 --> 1858.44]  can then you know filter for urgent and high priority figure out what needs to be answered now and then what
[1858.44 --> 1864.30]  can wait an hour or two and then questions about you know nutrition and whether it's okay to eat
[1864.30 --> 1868.26]  avocados during pregnancy that kind of thing can can wait maybe half a day or a day.
[1868.80 --> 1873.56]  Yeah and maybe just to add what what happens is you know the agents who are texting back
[1873.56 --> 1880.08]  will escalate messages that they feel a nurse needs to review and then the nurse may pick up the phone and call
[1880.08 --> 1886.34]  the moms and so that's where that three to five percent you know confirmed danger sign mom needs
[1886.34 --> 1892.82]  to be referred to the hospital metric comes from. But it's definitely an area that we're really
[1892.82 --> 1898.64]  actively looking at in terms of analytics you know data science and even a little bit of predictive
[1898.64 --> 1905.42]  modeling now to be able to okay in the haystack of danger signs find the needle of absolutely needs
[1905.42 --> 1912.00]  to be referred right now without having to make the phone call first. Yeah so you mentioned potentially
[1912.00 --> 1920.72]  in the future kind of providing some automated responses how do you view that workflow coming in
[1920.72 --> 1927.50]  and for what types of questions and you know sort of over the progression of the system how do you see
[1927.50 --> 1934.42]  automation being used best versus the way that it's interacting with humans in the loop?
[1934.42 --> 1941.32]  We are responding automatically to a subset of the questions we get already and how it started
[1941.32 --> 1949.44]  is that when the AI detects that this is a danger sign question we would send the mother a menu saying
[1949.44 --> 1956.18]  hey it sounds like you're asking about danger signs please select the specific issue you're having
[1956.18 --> 1963.62]  from the menu below and that would list you know the three or five danger signs. What we realized is that
[1963.62 --> 1970.26]  or what we noted is that we got a response rate of around three percent to that menu and it should
[1970.26 --> 1975.76]  have been obvious in retrospect that moms and probably everyone else hates interacting with menus I hate
[1975.76 --> 1982.52]  interacting with menus and so we iterated to version two where you know if the AI detects it's a headache
[1982.52 --> 1989.00]  question we'll send only the headache response if it's a swelling question we'll send only the swelling
[1989.00 --> 1996.10]  response and then we follow up with the mom and ask also automatically did this information answer
[1996.10 --> 2001.68]  your question and so we went from a response rate of three odd percent to about 45 percent.
[2002.84 --> 2007.98]  Now if the mom says yes that's great and we close the ticket so the help desk doesn't have to worry
[2007.98 --> 2013.62]  about it but if the mom says no it didn't or if she doesn't respond then that particular question
[2013.62 --> 2017.62]  gets red flagged for the help desk to look at as a priority.
[2018.62 --> 2022.80]  So you've got agents sort of in the loop you're always responding which I think is really wonderful
[2022.80 --> 2031.32]  taking that perspective on it. How does that feedback maybe from your agents or the new questions
[2031.32 --> 2038.56]  that come in how does that feed back into your data set in terms of model updates and when you
[2038.56 --> 2043.24]  update your data set and how you update your data set how are you handling that loop?
[2043.62 --> 2051.30]  Great question. So the second round of labeling the hundred thousand it was expensive it was painful
[2051.30 --> 2058.38]  and we didn't want to have to go through that again. So in the help desk ticketing platform we've
[2058.38 --> 2065.56]  built an option for the agents to correct where they note that the AI had flagged the intent incorrectly.
[2066.48 --> 2070.76]  So every time they see that they'll just from the drop down menu select the correct intent
[2070.76 --> 2079.08]  and now you know once we collect enough data we can just feed that back into the model and update it
[2079.08 --> 2085.10]  without having to manually label you know hundreds of thousands of questions every every now and then.
[2085.70 --> 2091.22]  Yeah that's wonderful. I know a lot of my questions are on the the data side of things but as both of you
[2091.22 --> 2099.00]  have emphasized that you know that's a real key part of any of these types of solutions and I know in the health
[2099.00 --> 2107.00]  space in particular you know data is is difficult in certain ways to deal with because you know we're
[2107.00 --> 2112.76]  dealing with people's personal health information information about maybe personally identifying
[2112.76 --> 2120.76]  information very sensitive data. It sounds like that one of the strategies you're taking is is definitely
[2120.76 --> 2129.00]  people sort of opting into this service and making sure you have some information from them. How has it been on that
[2129.00 --> 2136.60]  side of things in terms of you know keeping your data secure making sure that things are kept confidential while at the
[2136.60 --> 2142.72]  same time being able to sort of combine this data in a meaningful way to create useful models?
[2143.72 --> 2148.66]  The first step and Satya can add some context but the first step is to collect as little as possible.
[2148.66 --> 2155.06]  So we don't know our users names. We don't ask for things like age or other demographic information.
[2155.70 --> 2160.94]  Obviously we need a phone number and we'd like to know where which health facility they signed up in
[2160.94 --> 2165.60]  and how many months pregnant they are so that we can tailor the message campaigns according to
[2165.60 --> 2172.98]  the stage of pregnancy or whether they've delivered. And then on the back end just making sure that
[2172.98 --> 2181.58]  everything is stored according to industry best practices on you know the one of the major cloud
[2181.58 --> 2190.80]  providers and using their security tools. I think that rather than me trying to manage a server here
[2190.80 --> 2196.10]  just using the resources that are already available helped us better able to secure the data.
[2196.90 --> 2197.18]  Satya?
[2197.18 --> 2204.38]  Yeah I would just add that it's such an evolving conversation because I feel like knowledge and
[2204.38 --> 2210.42]  literacy around machine learning, what it requires from an infrastructure perspective,
[2210.92 --> 2218.12]  what that data is being used for. I mean it's hard enough for the general public
[2218.12 --> 2226.10]  as a Nokia feature phone and is in the middle of a village. How do you consent appropriately
[2226.10 --> 2233.52]  and provide a terms of service appropriately so that she's fully aware of you know how this
[2233.52 --> 2238.30]  information is being used you know and we're using it to improve the service that they get.
[2238.30 --> 2246.14]  The other sort of area where I think there's a lot of work to be done is in helping you know our
[2246.14 --> 2252.52]  government partners understand how that data is used. You know what are these systems, what are these
[2252.52 --> 2258.84]  processes, a question we get asked frequently is where is the data stored you know is it in Kenya or
[2258.84 --> 2264.92]  somewhere else and I think that kind of that's indicative of actually missing the more challenging
[2264.92 --> 2271.22]  question which is how is this data being used by you know a machine learning platform, how are you using
[2271.22 --> 2279.08]  it to respond to women, what's your threshold for risk, etc. And I don't think we're there yet in terms of
[2279.08 --> 2285.48]  conversations here but there's a lot of groups doing some great work around building capacity
[2285.48 --> 2290.70]  to improve those conversations and I think that's true not just for Kenya that's true around the world
[2290.70 --> 2296.14]  with the conversations we're having with data and privacy. Yeah to some degree this is definitely new
[2296.14 --> 2302.14]  for everyone and also you know like you're talking about helping people understand the ways in which
[2302.14 --> 2308.04]  their data might be used. I know a lot of companies have developed different principles and other things
[2308.04 --> 2313.54]  around that so it's really interesting to hear from your perspective how you're approaching that I think.
[2314.14 --> 2321.54]  In terms of looking you know maybe forward a bit I'd be curious to hear maybe first on the
[2321.54 --> 2328.30]  technical side but then also just on the user side what do you feel like are the challenges and
[2328.30 --> 2334.36]  opportunities moving forward that you haven't addressed yet that you'd like to dive into? Maybe on the
[2334.36 --> 2342.12]  technical side first Jay what are the main challenges you're facing in terms of scaling this or improving
[2342.12 --> 2347.98]  your models or extending this system? One of the technical challenges is getting the accuracy up
[2347.98 --> 2354.16]  higher than what it is much higher than what it is so the off the shelf of the commercially available
[2354.16 --> 2361.30]  models that we can plug into without actually being machine learning engineers ourselves they do it well
[2361.30 --> 2367.54]  enough they don't do it quite as well as we'd like and so one of the next steps is to partner with
[2367.54 --> 2374.72]  some machine learning experts and try and figure out how do you go from processing or just pattern
[2374.72 --> 2380.70]  matching on these words to maybe building in some sort of understanding and context into what the
[2380.70 --> 2388.58]  questions are about and then respond appropriately. In terms of scaling I think we've gotten our cost down
[2388.58 --> 2395.60]  it's running pretty cost effectively in those terms and in terms of the number of questions that we can
[2395.60 --> 2403.34]  process we seem to have gotten a handle on that we just need to increase the accuracy and maybe
[2403.34 --> 2409.42]  Sati can also mention what's next in terms of some of the predictive analytics stuff that we're looking at.
[2409.88 --> 2417.08]  You know the goal is always to get that mom care as quickly as possible and so now we're looking at
[2417.08 --> 2424.90]  what other data what other information will help us increase a risk rating for a mother will help us
[2424.90 --> 2431.58]  understand which facility she should be referred to. Something we didn't even talk about is half of the
[2431.58 --> 2436.30]  organization works with providers and improving the skills of providers and so we have a lot of
[2436.30 --> 2443.68]  data and insights from that kind of layer of the health system and so can we use these layers of data
[2443.68 --> 2450.08]  to really route those moms more effectively to care in a timely manner. So that's work that's going on
[2450.08 --> 2456.06]  now and just scratching the surface of it is to look at conversational history and look to see if there are
[2456.06 --> 2462.20]  triggers trigger intents you know that could be predictive of a future danger sign and it actually
[2462.20 --> 2467.26]  looks like we may have enough data to develop a model just from the initial work that's been done.
[2467.26 --> 2473.82]  And then Daniel you were asking a question about the users and I think the ultimate goal is to support
[2473.82 --> 2480.68]  moms with what they need in terms of information whether that's you know they want to know where
[2480.68 --> 2486.12]  should I get my baby vaccinated what kind of diet should the baby be on you know like how do you
[2486.12 --> 2490.54]  transition from foods and these are questions the moms are asking us right they want more and more
[2490.54 --> 2497.70]  information because in the context that we live and work in that information that kind of support is
[2497.70 --> 2505.30]  hard to come by so the lower cost the more digital the more close to the mom we can get on her phone or
[2505.30 --> 2513.54]  you know maybe phone plus the better so we're looking at things like voice we're looking at a home record
[2513.54 --> 2518.30]  on you know in terms of their own medical information that they wish to choose on their
[2518.30 --> 2523.60]  free to access for them so that it can help them provide a case history to a provider easier.
[2524.22 --> 2529.62]  So there's a lot of kind of future thinking around this but the principle is always what does that mom
[2529.62 --> 2534.56]  need to get care quicker. So lots of work going on in the background right now.
[2534.78 --> 2540.36]  That's wonderful. Well I really appreciate what you all and Jacaranda are doing. I think it's
[2540.36 --> 2550.48]  it's wonderful and also a great illustration of how AI and NLP can be utilized by an organization in a very
[2550.48 --> 2557.44]  practical way that really benefits the users. So I appreciate you sharing this story and joining me on the
[2557.44 --> 2561.10]  podcast. It's been wonderful to talk to you both. So thank you very much.
[2561.48 --> 2562.74]  Thanks a lot. It's been great chatting.
[2562.92 --> 2564.16]  Thanks. Yeah, it's been fun.
[2564.16 --> 2574.46]  Thank you for listening to Practical AI. We have a bundle of awesome podcasts for you at changelog.com
[2574.46 --> 2581.12]  including our brand new show Ship It with Gerhard Lezou. A podcast about getting your best ideas into the world
[2581.12 --> 2586.64]  and seeing what happens. It's about the code, the ops, the infra, and the people that make it happen.
[2586.90 --> 2590.62]  Yes, we focus on the people because everything else is an implementation detail.
[2590.62 --> 2596.08]  Subscribe now at changelog.com slash ship it or simply search for Ship It and your favorite podcast
[2596.08 --> 2600.96]  app. You'll find it. Of course, the galaxy brain move is to subscribe to our master feed. It's all
[2600.96 --> 2607.96]  changelog podcasts including Practical AI and Ship It in one place. Search changelog master feed or head
[2607.96 --> 2613.86]  to changelog.com slash master and subscribe today. Practical AI is hosted by Daniel Whitenack and Chris
[2613.86 --> 2618.70]  Benson with music by Breakmaster Cylinder. We're brought to you by Fastly, Vaughn Starkly, and Linode.
[2618.70 --> 2620.88]  That's all for now. We'll talk to you again next week.
[2648.70 --> 2650.02]  Game on!
