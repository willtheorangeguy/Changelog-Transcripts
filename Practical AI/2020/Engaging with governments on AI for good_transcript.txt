[0.00 --> 9.08]  One thing that I strongly advocate for is to be doing race conscious data analysis instead of racial blind analysis.
[9.40 --> 14.10]  So using things like zip codes can very, very easily be a proxy to race and socioeconomic status.
[14.10 --> 19.48]  But that doesn't necessarily mean that you should not look at those things, like just covering your eyes and being like, I'm not going to look at race.
[19.50 --> 28.82]  I'm not going to touch race is not the not the way to do it to make sure that you are being equitable and you are thinking critically about how your data analysis affects different people.
[28.82 --> 32.82]  You need to really be thinking about who those people are, where they come from, what their needs are.
[33.34 --> 39.92]  And to do that, you should be looking at things like race and like zip codes and the relationship between those things when you're doing your analysis.
[42.50 --> 47.02]  Bama for ChangeLog is provided by Fastly. Learn more at Fastly.com.
[47.26 --> 51.62]  Our feature flags are powered by LaunchDarkly. Check them out at LaunchDarkly.com.
[51.86 --> 57.64]  And we're hosted on Leno cloud servers. Get $100 in hosting credit at Leno.com slash ChangeLog.
[57.64 --> 60.80]  This episode is brought to you by DigitalOcean.
[61.28 --> 71.66]  Droplets, managed Kubernetes, managed databases, spaces, object storage, volume block storage, advanced networking like virtual private clouds and cloud firewalls.
[71.86 --> 78.10]  Developer tooling like the robust API and CLI to make sure you can interact with your infrastructure the way you want to.
[78.52 --> 82.02]  DigitalOcean is designed for developers and built for businesses.
[82.02 --> 89.14]  Join over 150,000 businesses that develop, manage, and scale their applications with DigitalOcean.
[89.42 --> 92.86]  Head to do.co slash ChangeLog to get started with a $100 credit.
[93.18 --> 95.34]  Again, do.co slash ChangeLog.
[95.34 --> 122.92]  Welcome to Practical AI, a weekly podcast that makes artificial intelligence practical, productive, and accessible to everyone.
[122.92 --> 126.60]  This episode breaks from our normal format just a bit.
[127.02 --> 134.06]  We are running Daniel's panel about AI for good in partnership with the R Data Science Conference that took place online this December.
[134.38 --> 135.48]  We hope you enjoy it.
[135.48 --> 145.96]  It is great to be back at our conference.
[146.62 --> 151.18]  So I spoke, I think, R Conference New York when it was in person.
[151.18 --> 159.72]  And I remember a heated discussion since I was living near Chicago at the time, a heated discussion about various types of pizzas.
[159.72 --> 165.06]  And, you know, there were things said and all was in good fun, but it was a good time.
[165.14 --> 165.72]  So I miss that.
[166.48 --> 168.06]  But this has been a great experience.
[168.06 --> 169.24]  It's great to be here.
[169.64 --> 175.74]  We're going to discuss today how data professionals can engage with governments on AI for good projects.
[175.74 --> 183.78]  This panel will actually be recorded and released after the conference as well on the Practical AI podcast.
[184.10 --> 186.68]  So if you're a podcast listener, there's a link there.
[186.78 --> 191.72]  You can follow along and listen again because it's going to be such a good time.
[191.90 --> 200.64]  Today we have with us a couple of great panelists who have agreed to share their vast expertise with us.
[200.64 --> 205.42]  We have Dania Murali, a quantitative analyst at Arcadia Power.
[205.84 --> 210.12]  She's a data scientist with a passion for energy, environment and climate.
[210.66 --> 224.72]  And currently she's working on the data team at Arcadia Power, a fast growing startup in the Washington, D.C. area, seeking to create a 100 percent renewable energy future while saving customers money on their power bill.
[224.72 --> 234.46]  We also have with us Emily Martinez, who is an interoperability unit chief at the NYC Department of Health and Mental Hygiene.
[234.88 --> 240.02]  She has her master's degree in public health from Columbia's Mailman University of Public Health.
[240.02 --> 255.82]  And she currently spends her time connecting health care providers to the CIR in anticipation of the COVID-19 vaccine, which is, of course, very timely and also very much fitting within the AI for good space.
[255.82 --> 268.50]  So I'd like to maybe just start out this panel by asking, maybe we can start with Dania just to get her sense of when we say AI for good or data for good or data practitioners working for good.
[268.64 --> 273.90]  What does that mean to you in terms of your day to day and things you've seen in your career?
[274.42 --> 277.26]  Yeah. Thanks, Daniel. And thanks, Jared, for having me back.
[277.34 --> 281.74]  I am so excited to be able to be at this conference, even if it's virtual this year.
[281.74 --> 286.70]  So, yeah, AI for good. That's something that I care about immensely.
[287.12 --> 302.54]  What I think about when I hear just the term AI for good, it's the idea that we should be using data and we should be using AI for things that are equitable and helpful to communities kind of across the board.
[302.54 --> 315.62]  So not just one particular community or group of people, but kind of helping all people together and being very aware and cognizant of how you can use that data and how you can use AI to achieve that goal.
[316.14 --> 324.74]  And I guess a follow up on that. What do you think about the current state of how data and AI or data science is being used?
[324.92 --> 330.52]  Do you see it being used equitably now or are there places where that's not true?
[330.52 --> 344.46]  Yeah, that's a really good question. I think it's on a path of improvement, but still in a place where we should be all more aware of what impact our use of data and our use of AI can have.
[344.58 --> 356.02]  There's definitely I've heard some like scary cases of using things like facial recognition for like police related things, which could disproportionately affect communities of color and hurt various communities.
[356.02 --> 369.52]  So there's there's scary moments like that. But then there's also like really great things with like what we heard today with the panel was tracing COVID and using data and using AI to try and help just general health of our population.
[369.52 --> 379.50]  At Arcadia, we're more focused on trying to get renewable energy as something that is just accessible to all people, no matter what your community is from.
[379.58 --> 386.96]  And also to do it in a way that we're making sure that we're not removing, but enhancing energy justice.
[386.96 --> 389.62]  And so there's that's something that we really care about.
[389.68 --> 399.76]  That's something that as a data scientist at Arcadia, we're constantly thinking about how the our products affect different people and how we can help how we can build for all.
[400.50 --> 413.22]  Awesome. That's exciting. I want to pose the same question to Emily to see your perspective on what triggers in your mind when you're thinking of using data for good or being an AI practitioner working for good.
[413.22 --> 417.04]  Yeah. First, thanks, Jared and the team for having me tonight.
[417.38 --> 425.30]  I think from my perspective, coming from a public health and local government bubble, I think we're always working for good.
[425.62 --> 433.56]  And we have in our fingertips access to incredible data, data that we can take action pretty quickly and impacts communities very quickly.
[433.56 --> 445.80]  So I think we're kind of on the receiving end, too, of outside private companies that work with government companies so that we're able to create and use newer technologies or methods.
[446.12 --> 449.90]  I know I view things a little different. I've always been using data for good.
[450.62 --> 451.70]  Yeah. Yeah, that's great.
[451.70 --> 462.30]  And you mentioned this sort of interplay between governments, whether they be federal or local governments and private entities.
[462.30 --> 479.16]  I was wondering, you know, of course, now that we're in this whole time of COVID and pandemic and we're getting to hopefully on the horizon, some distribution of vaccines like like was mentioned in your bio that you're specifically involved in that work.
[479.16 --> 487.16]  That necessarily involves, you know, a number of private companies that involves logistics companies and all of those sorts of things.
[487.16 --> 500.86]  So I was wondering if from that perspective, you could give us a little bit of a sense of at least from your own experience, how governments and private entities, commercial entities can work effectively together.
[501.06 --> 508.08]  Yeah, I think from my perspective and with the COVID examples, I think the collaboration has been great.
[508.08 --> 512.52]  It's been nice to be able to contract with outside companies.
[512.96 --> 522.22]  I know particularly we were kind of interviewing different vendors that we could partner with to establish a new point of dispension system.
[522.22 --> 527.28]  So previously to working with these vendors, everything was on paper.
[527.28 --> 537.24]  So point of dispensing means we're set up to pop up, let's say, for example, a mobile clinic at a school where staff will be able to vaccinate people
[537.24 --> 541.48]  and people can just approach a school to get vaccinated and all that needs to be tracked somehow.
[541.84 --> 543.36]  And previously this was all on paper.
[544.46 --> 547.18]  So that can still be happening in 2020.
[548.00 --> 559.50]  So it's nice that we're able because of the severity and the impact that COVID has had worldwide that we can move forward with using better and efficient data products.
[559.50 --> 560.66]  Yeah, great.
[561.10 --> 576.32]  And of course, one of the underpinnings of this, like you mentioned, governments, whether they be national or local governments, have a lot of data that can be immediately put to use for certain AI for good purposes,
[576.32 --> 582.14]  whether that be as related to health or I think as related to energy and other things.
[582.14 --> 593.24]  So, Dania, I want to kind of kick it back to you and hear from your perspective what the role of data from governments is in your own work in the energy industry.
[593.78 --> 597.12]  Yeah, we use a lot of government data.
[597.62 --> 605.20]  So before I worked at Arcadia, I used to work at the Energy Information Administration, which is the statistical hub of the Department of Energy.
[605.20 --> 613.18]  So it's been a it's been a cool transition to go from like the government agency that collects the data to like being a private entity that uses the data.
[613.96 --> 628.34]  But one really big one example I can give about how we use EIA data for good is we try and give our customers an understanding of what their CO2 impact is of their monthly residential electricity use.
[628.34 --> 635.16]  So sort of like being able to keep track of your carbon footprint, but in a very, very precise way that is very much related to like your individual usage.
[635.52 --> 637.70]  And we do that using EIA data.
[637.88 --> 647.80]  So the power of government is you have the ability to go and collect data and sort of like mandate that the data that your surveys get responded to, which is great.
[647.80 --> 654.18]  So one example is EIA has a survey of all the combustion power plants across the U.S.
[654.18 --> 666.16]  So all the coal power plants, natural gas, oil, all of those power plants and how much of each fossil fuel is being used in a year for each of those and also how much CO2 is being emitted.
[666.16 --> 679.00]  And so using that data set and using our individual customer data, we're able to create individualized forecasts and calculations of how much CO2 is released by using a certain amount of electricity.
[679.00 --> 684.60]  And then also how much CO2 is averted when you're able to source your power from places like wind and solar.
[684.82 --> 690.76]  So there's a very direct relationship between how we use government data and our data to achieve that.
[691.20 --> 692.18]  Yeah, that's awesome.
[692.18 --> 705.34]  It's cool to see how granular you can be with some of that thing, some of that stuff and see how it affects individual people's energy usage and maybe their own mindset around that, which is really cool.
[705.82 --> 710.30]  We had a question from our audience, which I'd like to propose here.
[710.36 --> 711.14]  I think it's a good one.
[711.22 --> 721.16]  So we're on the topic of data sets and how some of these government data sets can be used with great success for AI for good projects.
[721.16 --> 725.44]  I was wondering, maybe we can start with Emily in the healthcare space.
[725.90 --> 737.48]  What are some sort of go-to resources out there for people that are maybe wanting to either contribute in the healthcare space or look at data from the healthcare space?
[737.56 --> 742.24]  Of course, some of that has some privacy concerns and all of that with that.
[742.32 --> 749.42]  So what's the situation there in terms of data that people can access and data that needs to be protected in certain ways?
[749.42 --> 751.04]  Yeah, that's a great question.
[751.16 --> 755.64]  I think right now there's a lot of data that's been public and easily accessible.
[756.06 --> 763.80]  I know in New York City there's the open data platform where different data sets from actually different agencies, including from the health department.
[764.52 --> 765.86]  So there's a range of things.
[766.44 --> 767.96]  I think they're pretty much up to date.
[767.96 --> 778.40]  There might be a lag in how recent the data is, but there's actually quite a big variety of data that can be used by anyone who just wants to play around with the data.
[778.92 --> 784.90]  I think there's also New York State's public data sets and other states as well.
[784.90 --> 792.02]  So I think right now data is very much accessible to anyone who wants to take a look.
[792.30 --> 799.40]  In terms of security, yes, there's a lot of security, especially patient demographic information, all of that.
[799.50 --> 805.10]  Most of the data that's cleared is probably aggregate or has no way that can be connected to a particular patient.
[805.10 --> 811.54]  So that is very much kept very tightly within the health department.
[812.10 --> 812.24]  Yeah.
[812.34 --> 815.82]  What about in the realm of energy, Dania?
[815.94 --> 825.10]  What's the situation in terms of it sounds like you have this tool where people are able to utilize your analysis to kind of understand their own energy use.
[825.10 --> 835.60]  What about maybe for participants in this conference who are interested in maybe coming up with their own analyses or doing a little bit deeper study as related to energy?
[835.74 --> 838.78]  What is available out there for them to potentially utilize?
[839.32 --> 844.50]  Yeah, there are a lot of great government and otherwise data sets surrounding energy.
[844.78 --> 845.88]  Two things I highly suggest.
[845.96 --> 847.46]  So one, I sound like a broken record.
[847.46 --> 854.86]  I would highly suggest you go to EIA.gov where you can see that they just collect a ton of data about all energy across the board.
[854.98 --> 866.12]  But also going to the EPA website, they have a really cool green energy calculator where you can put in like how many miles you drove or how many like airplane rides you took, which I'm sure is not very many this year.
[866.76 --> 872.24]  And what that, how that led to like CO2 emissions and other environmental factors.
[872.68 --> 875.98]  Another place I would also suggest is just going to Kaggle.
[875.98 --> 886.20]  I don't know if you guys have used Kaggle before, but that is a really great place to get a lot of different types of data, both like healthcare data and energy data and pretty much any type of data you want.
[886.34 --> 895.44]  And also one of the things that's really nice about Kaggle is that oftentimes people have already done analysis and it's a very open source place where you can contribute to other people's things or pull from other people's things.
[895.70 --> 897.36]  So that's a, that's a really good source.
[898.00 --> 898.22]  Yeah.
[898.40 --> 898.60]  Yeah.
[898.60 --> 899.18]  Those are great.
[899.26 --> 901.60]  And I'll kind of throw in my own contribution here.
[901.60 --> 908.72]  So I work mostly in the language space for an NGO and there's a lot of great language and speech data out there.
[908.88 --> 919.90]  In particular, Mozilla has done an amazing job with Common Voice, which is a large data set of transcribed speech, which is out there in, in all sorts of languages.
[919.90 --> 925.88]  And then there's a whole bunch of open data that you can use for like machine translation projects.
[926.08 --> 931.82]  If you search for Opus, which is an open parallel corpus, you can download a bunch of that.
[932.40 --> 935.16]  And yeah, I would encourage people to dig into that.
[935.26 --> 948.10]  It's pretty interesting when you start doing some natural language processing on languages other than English, especially because for one, it can help benefit tools and support for languages.
[948.10 --> 958.74]  But also you run into all sorts of things fairly quickly with scripts other than Latin script and, you know, really long words or languages that don't use spaces.
[959.12 --> 962.04]  And so you have to think about all sorts of interesting problems.
[962.04 --> 964.96]  And so it's also really interesting from that perspective.
[964.96 --> 993.00]  While we're still on the topic of data and using data for good, I know that one element of this is also making sure that we're responsible, no matter what project we're working on, making sure that we are using data in a responsible way and not either showing bias against certain populations or possibly even unintentionally doing things that might harm people.
[993.00 --> 1006.58]  So, Dania, do you have any thoughts on that front in terms of in your own work or just what you've seen in practice across industry, some good practices or things that people should keep in mind with respect to that?
[1007.02 --> 1007.26]  Yeah.
[1007.68 --> 1019.54]  So one thing that I strongly advocate for is to be doing race conscious data analysis instead of like racial blind analysis.
[1019.54 --> 1024.82]  So using things like zip codes can very, very easily be a proxy to race and socioeconomic status.
[1025.16 --> 1030.58]  But that doesn't necessarily mean that you should not look at those things, like just covering your eyes and being like, I'm not going to look at race.
[1030.60 --> 1034.50]  I'm not going to touch race is not the not the way to do it to make sure that you are being equitable.
[1034.50 --> 1041.78]  And you are really thinking critically about how your data analysis affects different people.
[1041.78 --> 1045.78]  You need to really be thinking about who those people are, where they come from, what their needs are.
[1046.34 --> 1054.68]  And to do that, you should be looking at things like race and like zip codes and the relationship between those things when you're when you're doing your analysis.
[1054.68 --> 1062.84]  So when is the time to do that? Is that when you're sort of doing your initial pre-processing and setting up your project?
[1063.20 --> 1067.28]  Is that like while you're doing your analysis, is that afterwards and monitoring?
[1067.68 --> 1069.90]  You know, where can that sort of fit in?
[1070.34 --> 1071.94]  I think it fits in in many places.
[1071.94 --> 1080.76]  So I would say that it should be kind of like in every step of the analysis, like when you're collecting data, making sure that you're collecting representative sample, for example.
[1080.76 --> 1087.76]  When you're doing the analysis, making sure that you're not making decisions or taking averages or doing things that are biased.
[1088.62 --> 1094.56]  So sort of like in every step of the data analysis lifecycle, being cognizant of that.
[1094.74 --> 1098.00]  I can give a better, a more particular example is at Arcadia.
[1098.32 --> 1103.78]  One, we recently started a chapter, a diversity, equity and inclusion chapter.
[1104.00 --> 1106.96]  And that contains people from all across the organization.
[1106.96 --> 1111.86]  So we have engineers, we have data scientists, we have people that work on the member experience team.
[1112.12 --> 1123.62]  And we all come together and we talk about how our different products relate to diversity and inclusion and how the data that we collect and data that we use to create products affect that.
[1123.62 --> 1132.82]  And so by having an outside, outside of your day job, like outside chapter that looks into these things and considers these things is also good.
[1132.90 --> 1140.76]  Like having checks in place to make sure that we are looking at different types of data, diversity data.
[1141.28 --> 1148.20]  Another thing that we've been doing recently is just looking at the demographics of our customers to make sure that we're not over indexing in a certain population.
[1148.20 --> 1150.96]  And if we are like applying the corrective features.
[1151.30 --> 1157.82]  So it's definitely one of those things where you can you can mess up and that's OK and you can fix it.
[1158.04 --> 1165.56]  And if you're just aware of it through all the different steps of your data analysis process and your product development process, I think you could really do some good.
[1166.06 --> 1167.48]  Yeah, appreciate that perspective.
[1167.48 --> 1171.94]  I kind of want to return over to Emily to the health care space.
[1172.04 --> 1181.24]  I know one of the things that you mentioned when we were talking prior to the panel is your work, you know, connecting patients to services during this pandemic.
[1181.24 --> 1201.76]  And this maybe connects to one of the questions we got as well from the audience, which is, you know, I guess in that scenario, there's also this element where certain populations, certain demographic factors have been shown to, you know, have higher risk and higher concentrations of COVID, higher death rates, all of that sort of thing.
[1201.76 --> 1219.94]  How do you balance like collecting and using sensitive, maybe racial information or demographic information when maybe some people are, you know, might not want to give that information, but you you might want to utilize it, particularly in health care for certain purposes.
[1219.94 --> 1235.00]  What questions go through your mind and how do you handle some of those sensitive pieces of data, making sure that you're not, you know, exploiting those or making them, you know, gathering them when you shouldn't, but also gathering them when you should for for good reasons.
[1235.70 --> 1241.50]  Yeah, I think the city already has a good picture of where those areas are.
[1241.50 --> 1252.76]  So reaching out to the community where with low resources, socioeconomic status, a lot of programs are developed to help those particular communities.
[1253.52 --> 1256.80]  So I think we kind of already know where that is.
[1256.88 --> 1262.06]  And a lot of the data reflects, we use a lot of data to find where these disparities are.
[1262.22 --> 1265.12]  And they always align wherever there's a high index.
[1265.12 --> 1268.06]  It also matches poverty numbers.
[1268.06 --> 1273.00]  So there is a, you know, a good match correlation on that.
[1273.00 --> 1283.64]  So I don't know, in terms of sensitivity, I think the data has, I don't know, we always use the data carefully and we already have these ties to the community.
[1283.90 --> 1292.66]  So I don't think there there's a problem that we might backfire in our communication or I think there's a lot of trust in that sense.
[1292.66 --> 1304.06]  Yeah, I think that's a really great point in terms of the connection to the community and not creating projects sort of without any communication and trust between you and the community.
[1304.28 --> 1309.80]  And then sort of forcing a solution in and saying, hey, this is going to, you know, fix all of your problems.
[1309.80 --> 1312.16]  There needs to be an open line of communication there.
[1312.24 --> 1313.96]  And I think that's a really good point.
[1313.96 --> 1319.62]  So I think we're pretty much out of time, but I do want to just give one more question to both of you.
[1319.74 --> 1321.82]  We can start with with Dania.
[1321.90 --> 1329.36]  I would just be curious to know, you know, what excites you about the future of using data for good?
[1329.50 --> 1332.84]  What excites you about the potential there and what impact it could have?
[1333.38 --> 1335.08]  Yeah, I love data.
[1335.54 --> 1337.16]  I also especially love art.
[1337.16 --> 1347.18]  One of the things that I'm really excited about that has grown in probably the last decade is the use of open source data and open contributing to software like R.
[1347.38 --> 1362.34]  And then also conferences like this and different organizations like R.Ladies that really kind of try and get more people of various types of communities to come in and be data analysts and like make it so it is accessible across the board.
[1362.34 --> 1374.68]  Like things like General Assembly and these other types or like Code Academy, these online classes where you don't need to get a degree to be able to do data analysis and have an impact and bring your own like personal bit to it.
[1375.12 --> 1376.92]  You can go off and do that online.
[1377.04 --> 1386.48]  And so it's it's I feel like a lot of the barriers to being data literate and being able to make really smart decisions and choices has lessened.
[1386.62 --> 1389.20]  And I think it's going to continue to continue to lessen.
[1389.32 --> 1390.70]  So it's it's very exciting.
[1390.70 --> 1393.50]  I think it's an exciting time to be in this data space.
[1394.12 --> 1394.44]  Awesome.
[1394.68 --> 1394.80]  Yeah.
[1394.82 --> 1395.66]  What about you, Emily?
[1396.12 --> 1397.40]  What are you excited about?
[1397.98 --> 1398.68]  Yeah, I agree.
[1398.80 --> 1400.72]  And I echo everything that Dania said.
[1400.72 --> 1410.38]  I think also particularly in local government, there has been an increase in using open source tools, using R, particularly in the health department.
[1410.78 --> 1415.12]  I think it was a couple of years ago where we got an R server and we were all excited about that.
[1415.16 --> 1417.76]  And that has really pushed a lot of new R users.
[1418.10 --> 1419.46]  We've been mostly SaaS users.
[1419.46 --> 1422.84]  So I think we're going in a really good direction.
[1422.84 --> 1428.66]  And there's a really big interest of we're saying local government about data science.
[1429.10 --> 1431.26]  And it's just been very accessible.
[1431.48 --> 1435.30]  And I think that the biggest part is a sense of community in every sector.
[1435.70 --> 1437.38]  Data analysts have some form.
[1437.48 --> 1441.22]  They can reach out and ask others like them if they have any questions.
[1441.22 --> 1445.74]  So I think that that's been the biggest thing, that sense of community.
[1446.38 --> 1446.66]  Awesome.
[1446.96 --> 1450.74]  Well, thank you both for such a great discussion.
[1451.14 --> 1452.32]  I really enjoyed it.
[1452.68 --> 1457.60]  As a reminder to everyone, this will be published again on the Practical AI podcast.
[1458.48 --> 1460.82]  Check that out if you're into podcasting.
[1461.24 --> 1464.06]  Thank you again to the R conference for making this happen.
[1464.06 --> 1468.84]  I'm really glad that this conversation happened and this content will be accessible.
[1469.52 --> 1471.38]  And enjoy the rest of your conference.
[1471.38 --> 1481.20]  Come hang out with Daniel, Chris, and hundreds of other AI practitioners in our community Slack.
[1481.46 --> 1482.52]  It's a cool place to be.
[1482.64 --> 1483.60]  Not a lot of noise.
[1483.82 --> 1484.70]  Some great signal.
[1484.90 --> 1486.52]  And best of all, it's totally free.
[1486.92 --> 1489.26]  Check it out at changelog.com slash community.
[1489.26 --> 1495.06]  And don't forget to follow the show on Twitter for AI news and links, highlights from past episodes, and more.
[1495.42 --> 1497.18]  We are at Practical AI FM.
[1497.40 --> 1498.56]  We'd love to have you following along.
[1498.90 --> 1502.78]  Thanks to Daniel and Chris for hosting Practical AI week in and week out.
[1502.90 --> 1507.22]  To the mysterious Breakmaster Cylinder for the excellent beats you hear on all Changelog podcasts.
[1507.56 --> 1511.66]  To our sponsors who have our back, Fastly, Linode, and LaunchDarkly.
[1511.90 --> 1512.78]  And to you for listening.
[1513.08 --> 1514.70]  We appreciate your time and attention.
[1515.28 --> 1516.42]  That's all for now.
[1516.82 --> 1518.10]  We'll talk to you again next week.
[1519.26 --> 1549.24]  We'll see you again next week.
