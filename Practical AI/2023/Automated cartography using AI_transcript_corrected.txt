[0.00 → 8.64] Welcome to Practical AI.
[9.20 → 15.96] If you work in artificial intelligence, aspire to, or are curious how AI-related technologies
[15.96 → 18.78] are changing the world, this is the show for you.
[19.20 → 24.36] Thank you to our partners at Vastly for shipping all of our pods superfast to wherever you
[24.36 → 24.66] listen.
[24.92 → 26.76] Check them out at Fastly.com.
[26.76 → 32.02] And to our friends at Fly, deploy your app servers and database close to your users.
[32.44 → 33.70] No ops required.
[34.04 → 36.08] Learn more at fly.io.
[42.66 → 46.02] Welcome to another episode of Practical AI.
[46.58 → 47.96] This is Daniel Whiten ack.
[48.04 → 51.38] I'm a data scientist and founder at Prediction Guard.
[51.38 → 59.62] And I am really excited today because my life has been filled with large language models
[59.62 → 61.22] for the past months.
[61.38 → 64.32] And I feel inundated with information about those.
[64.70 → 66.28] But there's so much going on.
[66.38 → 72.38] So many amazing things happening in the AI world outside the text modality.
[72.38 → 79.64] And today we have with us Gabriel Ortiz, who is Principal Geospatial Information Officer
[79.64 → 82.24] at the Government of Cantabrian in Spain.
[82.48 → 83.60] Welcome, Gabriel.
[83.76 → 84.20] How's it going?
[84.64 → 85.20] Thank you.
[85.32 → 85.80] Thank you.
[86.08 → 91.60] Thanks for having me on and giving me the opportunity to share with you and the audience what we have
[91.60 → 97.26] been after in the last few years regarding geospatial analysis and particularly artificial intelligence.
[97.26 → 97.82] Yeah.
[98.12 → 102.78] And one of the things that stood out when we started talking, well, first, you're
[102.78 → 103.98] a listener of the show.
[104.10 → 107.54] So I love it that you now get to be a guest on the show.
[107.88 → 108.86] That's so wonderful.
[109.06 → 114.46] I'm glad that we have listeners who are doing amazing things as practitioners.
[114.96 → 119.88] But also, you're in Spain, which is one of my favourite places.
[120.14 → 120.48] I did.
[120.92 → 125.46] My collaborators during my grad school days were in San Sebastián, and I spent time there.
[125.46 → 131.48] And I know there's so much innovation happening in that region and in Spain in particular.
[131.82 → 134.54] What's it like to be working in AI in Spain?
[134.90 → 141.32] Well, Spain, I think, is a great country to find professionals in all the branches of engineering.
[141.84 → 145.76] And there are many things happening in the AI industry.
[146.24 → 151.56] There is a lot of good environment of startups growing.
[151.56 → 158.02] And I really encourage you to engage and contract people from Spain.
[158.54 → 159.72] Yeah, that's so great.
[159.88 → 165.28] And not only is there amazing work going on there, but it's one of the most beautiful places
[165.28 → 166.34] I've been.
[166.50 → 170.96] And even when you logged in, so our listeners can't see it, but I see the beautiful sunshine
[170.96 → 174.72] and trees and town behind you through your windows.
[174.72 → 176.64] So I'm a little bit jealous.
[177.44 → 178.94] You mentioned San Sebastián.
[179.20 → 181.54] I am pretty close to San Sebastián.
[182.32 → 185.24] Santander is a really, really beautiful city.
[185.54 → 186.24] Yeah, yeah.
[186.58 → 189.90] So we mentioned that you work in geospatial.
[190.24 → 196.50] I know, so I've been on the Manscaping podcast a few times, which has been fun.
[196.50 → 203.94] And I know that that industry is really wrestling with kind of uses of deep learning, uses of
[203.94 → 206.94] AI and understanding how to integrate that into workflows.
[207.24 → 215.20] If my understanding is right, you didn't come from a data science researcher sort of background
[215.20 → 217.04] into this topic.
[217.42 → 220.64] You came more from the geospatial side.
[220.64 → 228.58] So could you tell us a little bit about how, as a geospatial practitioner, you first started
[228.58 → 235.84] kind of dipping your toes into deep learning and understanding what it meant for your industry?
[236.36 → 236.54] Sure.
[236.80 → 241.40] I have been working in the geospatial industry for more than 30 years.
[241.58 → 247.02] I started working for topographic control, bathymetric control of works.
[247.02 → 254.68] Then I moved on to engineering companies designing highways and railroads, dealing with environmental
[254.68 → 261.04] data and always using GIS, which stands for Geographical Information System.
[261.32 → 268.20] And as many of you know, it's a technology that lets you operate and do analysis over a
[268.20 → 269.24] huge amount of data.
[269.62 → 272.94] Then I started to work for Government de Cantabria.
[272.94 → 278.72] I am now in the role of principal geospatial officer, as you mentioned.
[279.28 → 285.00] But literally, if you translate directly from Spanish, it would be something like chief of
[285.00 → 287.60] the service of cartography and GIS.
[288.38 → 294.44] My role here is not only being in charge of the data production, but also in the development
[294.44 → 301.60] of the infrastructure for the analysis of geospatial data within our organization.
[301.60 → 308.88] It means for our staff, but also for our stakeholders outside, which is something very important for
[308.88 → 313.48] us, for the citizenship, for the community and for the companies that are working with
[313.48 → 314.34] geospatial data.
[314.96 → 321.78] Me and my team, we have something very ingrained in our DNA, which is the public service that
[321.78 → 326.22] we provide using AI and using another set of technologies.
[326.22 → 331.40] And we, every day, try to do our best to fulfill with that target.
[332.00 → 338.08] Yeah, it's really, really inspiring to hear kind of the motivations behind how you think
[338.08 → 341.76] about doing your work and the people you're serving, which is so great.
[341.96 → 349.54] I'm wondering, just practically, you mentioned kind of GIS tooling and, you know, the processing
[349.54 → 351.60] of data in that space.
[351.60 → 360.22] Of course, deep learning and the AI space has its own sort of unique tooling and sometimes
[360.22 → 361.56] weird tooling.
[361.84 → 368.84] So I'm wondering, could you comment in terms of what is it like for a geospatial practitioner
[368.84 → 376.24] to start adopting deep learning techniques and all of that, which I'm assuming have a different
[376.24 → 380.26] set of tools than geospatial people have used in the past?
[380.44 → 386.98] So what is the current state of, you know, the tooling around mixing deep learning with
[386.98 → 387.98] geospatial?
[388.46 → 389.52] Is it difficult?
[389.70 → 390.82] Is it fairly segmented?
[390.94 → 393.26] Or is it more integrated at this point?
[393.42 → 397.32] Well, at first sight, it seems daunting and intimidating.
[397.82 → 401.26] But I have to say that it is not so difficult, right?
[401.34 → 404.96] Just to demystify a little bit the AI technology.
[404.96 → 408.76] As you mentioned before, I am not a researcher on AI.
[409.14 → 412.32] I am an expert in geospatial industry.
[413.02 → 415.42] And I will tell you my story, how I began.
[415.70 → 421.90] My first, you know, contact, or at least the first time that I pay attention to AI was in
[421.90 → 425.96] 2012 with Alex Net, what happened in the ImageNet challenge.
[426.42 → 433.04] At that point in time, classification of images was great, but it was not very applicable to
[433.04 → 434.08] the geospatial industry.
[434.08 → 439.80] You know, it has an application, and you can leverage that, but it is not what we do every
[439.80 → 440.06] day.
[440.68 → 445.80] Previous to that, I have to say that it was in 2010 or 2011, something like that.
[445.88 → 452.16] I knew about the work of NVIDIA with the GPUs, the general purpose GPUs.
[452.16 → 456.80] I think Bill Daly talked about this in one of your early episodes.
[457.58 → 463.04] And that was very interesting for me because in the geospatial industry, we often have a
[463.04 → 466.18] lot of demand in terms of computing power.
[466.32 → 473.38] When we operate with what we call raster data, which is no more than data organized in a grid,
[473.94 → 475.02] topologically in a grid.
[475.02 → 477.80] For instance, an image is raster data.
[477.80 → 485.84] But also, for example, a digital terrain model, which is a grid where you storage in every pixel,
[485.94 → 491.84] in the centre of every cell, the value of the altitude of the terrain over the main sea level,
[491.92 → 492.42] for example.
[492.42 → 496.94] And you perform calculations over that digital models.
[497.50 → 502.88] For instance, you know, getting the watershed or the view shed of one part of the territory.
[503.38 → 506.98] And that calculations can span for several days or even weeks.
[507.20 → 512.46] Because in spite that the mathematics underlying running under the hood are not very complex,
[512.94 → 519.48] what happens is that you have so many pixels that it ends up being very demanding.
[519.48 → 528.36] And what NVIDIA started to do on those days was to be able to parallelize a lot of calculations.
[528.72 → 535.00] And instead of using four computational threads on your GPU or eight computational threads,
[535.32 → 542.76] they were able to spread all the calculations among hundreds or even thousands of computational threads.
[543.10 → 546.22] That caught my eye because it was very important for me.
[546.22 → 550.98] But at that point in time, I thought, you are going to need, Gabriel, you are going to need a GPU,
[551.22 → 552.76] but not for artificial intelligence.
[552.92 → 554.34] I was not thinking about that.
[554.66 → 557.78] But for calculations of a different nature.
[558.12 → 567.06] Then in 2015, 2016, we witnessed the blossom of a whole new generation of deep model architectures.
[567.18 → 571.74] Just to mention some of those who had a big impact in computer vision.
[571.74 → 576.10] Reset in 2015, I think it was presented in 2016.
[576.44 → 577.52] I'm not very sure.
[578.22 → 581.38] Then UNIT that has been extensively used.
[581.86 → 588.88] In 2017, the Facebook Artificial Intelligence Research Group presented and proposed mask R-CNN.
[589.22 → 592.78] You know, it was an evolution of fast R-CNN.
[592.78 → 602.88] And in 2018, I saw for the first time a demo within the geospatial realm of our data provider,
[603.08 → 604.68] which is ESR, actually.
[604.92 → 608.92] I think you also have a couple of guys from ESR in a previous episode.
[609.68 → 616.26] And what they were demonstrating is how you can detect swimming pools and oil rigs automatically
[616.26 → 619.22] using a single shot detector in that days.
[619.22 → 622.94] And that was kind of an aha moment for me.
[623.06 → 626.62] Because I realized, well, you have to invest your time.
[627.16 → 629.50] This is going to be definitely a game changer.
[630.08 → 632.36] And you have to start working on this.
[633.02 → 634.44] So that was the moment.
[634.70 → 638.66] And from that point, you know, there are two kinds of persons.
[639.44 → 642.26] I will use a metaphor to explain that.
[642.38 → 646.46] When you see the results of AI, some people think it's magic.
[646.46 → 649.24] And everybody likes magic, magicians, you know.
[649.74 → 653.08] Some people end up falling in love with the magicians.
[653.50 → 658.98] You know, they are obsessed with the persona and the mystery and the whole stick.
[659.54 → 663.42] But some other people just want how the trick is done.
[663.72 → 665.98] And I think I belong to the second group.
[665.98 → 670.94] So it was not only that this looks like magic.
[671.86 → 674.98] Many, the point was how this is done.
[675.22 → 677.92] And from that point, I started to work.
[678.16 → 680.76] We can delve into this if you want.
[681.36 → 684.02] But it's not so difficult, as I said before.
[684.36 → 685.28] Yeah, that's so great.
[685.42 → 688.42] Yeah, I think I applaud you for digging in.
[688.42 → 692.90] And, you know, not too early where it was only a research topic.
[692.90 → 703.84] But as it started getting into practical applications, you really took that and figured out how to apply it within your context appropriately.
[703.84 → 708.28] Which I think is maybe not everybody takes that approach.
[708.44 → 709.80] So I appreciate that.
[709.80 → 718.28] So with the tooling that you're using, I think maybe this is useful for people that haven't done geospatial as much.
[718.50 → 724.20] So I know there's major tools like ArcGIS and other ones.
[724.20 → 736.58] And then you've got sort of like Jupyter Notebooks where you, you know, train models or GPU services where you can run inference and other things.
[736.70 → 738.72] Have those merged at all?
[738.72 → 748.30] So like from within the tooling that you're using as a GIS professional, has some of the deep learning tooling been integrated into those tools?
[748.30 → 758.72] Or is it mostly at this point for you, I'm going to export my data from the geospatial side and then use a notebook and then import it back in or something like that?
[758.98 → 761.34] Well, that's a smart question.
[761.70 → 765.88] As I said before, our software provider is ESR.
[766.12 → 768.60] We work with ESR for a number of years.
[768.72 → 775.66] And they are doing an excellent job in integrating many open source frameworks into their platform.
[776.44 → 782.56] And I think because we try to follow the literature, but we are constantly falling behind.
[782.72 → 784.86] You know, it's extremely difficult every week.
[784.96 → 785.30] Me too.
[785.38 → 785.96] Every month.
[786.70 → 787.64] It's impossible.
[787.64 → 799.62] And even, you know, completing the puzzle and the issue of installing all the frameworks and putting everything into work can be very complex.
[799.62 → 804.58] So we have a big advantage working with ESR technology.
[804.58 → 810.36] They have a team, research and development team based in India.
[810.36 → 817.02] And I think these people is doing a great job facilitating the application of that.
[817.58 → 827.62] In some of your previous episodes, you have been talking about UX interfaces for using artificial intelligence, whether it makes a difference.
[827.62 → 835.54] And it really makes, because it's a way of, you know, democratizing and making accessible the technology.
[835.74 → 837.28] That is one part of the story.
[837.28 → 849.38] I think it has facilitated a lot of our work because you not only need the frameworks, you need all the platform to move across terabytes of data.
[849.70 → 854.78] Your spatial industry is highly demanding in terms of the data that you have to work.
[854.78 → 864.88] And it's not only the frameworks of open source, it's how you prepare the labelling, how you structure the databases, how there is a lot of more science.
[865.60 → 878.32] And also, apart from that, what I did is starting to gain the main concepts related with artificial intelligence from all the great resources that are completely free on the Internet.
[878.32 → 891.30] You know, on YouTube, you have lessons from MIT, from Stanford, that can introduce you to the simplest concepts, such as a perceptron or a bad propagation or a stochastic ready descent.
[891.86 → 895.42] So I designed it for myself, a twofold strategy.
[895.62 → 902.68] First, training to gain experience with getting hands on off the shelf models.
[902.68 → 912.64] But at the same time, training to also learn about the concepts underlying, pinpointing the AI world.
[912.80 → 914.14] I think that's important.
[914.88 → 917.96] Many people think that artificial intelligence is a black box.
[918.14 → 919.20] It's not a black box.
[919.34 → 922.18] It's mathematics in action.
[922.84 → 924.60] Of course, it's not linear.
[924.82 → 927.22] You cannot fully predict what is going on.
[927.28 → 930.08] But many of the things can be understood.
[930.08 → 938.02] Well, I love your perspective, Gabrielle, on how you've developed a mental model of how these technologies work.
[938.10 → 948.98] I think that's an encouragement to others to both explore these technologies, but also keep in mind what they are and how they should interact with them as tools.
[949.24 → 959.06] But I'm so fascinated by some of the projects that you've been able to accomplish during your time using this technology.
[959.06 → 962.32] And I want to start diving into those a little bit.
[962.32 → 971.50] One of the ones that you pointed me to that was really fascinating reminded me of standing on the beach in San Sebastián.
[972.26 → 976.82] Although it looks like you have really maybe more nice beaches up where you're at.
[977.24 → 985.36] So tell us a little bit about how standing on beaches and counting people on beaches, why is that important?
[985.36 → 991.12] And how did you get into this project of applying deep learning in that context?
[991.48 → 992.14] Yeah, definitely.
[992.46 → 996.54] I started working with deep learning at the end.
[996.62 → 999.64] I think it was the end of 2019 or something like that.
[999.74 → 1000.76] Then came the pandemic.
[1001.46 → 1007.36] And after the pandemic, you know, with the release of restrictions, somebody here at Government of Cantabrian said,
[1007.36 → 1014.26] hey, we are a little bit worried about the possibility of having uncontrolled crowds on the beaches,
[1014.26 → 1019.68] because I have to say that Cantabrian is a notable tourist destination.
[1019.98 → 1021.62] We have more than 100 beaches.
[1022.16 → 1027.48] So you can have a big problem in terms of spreading of the COVID-19.
[1027.94 → 1029.12] And they were worried.
[1029.12 → 1042.92] The first thing that they asked me is how can we get a calculation of how many people we have in every beach and when the tide is up and when the tide is down and things like that.
[1043.48 → 1049.94] But it was just a simple calculation in terms of the surface or the area that the beach has.
[1050.40 → 1052.96] And I said, I think I can go further.
[1053.56 → 1054.96] I will count the people.
[1055.18 → 1056.48] And they said, what?
[1056.64 → 1057.40] Are you crazy?
[1057.40 → 1060.24] Yeah, I'm not drunk.
[1060.36 → 1061.40] I think I can do it.
[1061.68 → 1066.30] Because I had some experience using single-cell detectors.
[1066.66 → 1070.36] And at that point in time, more models than single-cell detectors.
[1071.12 → 1073.02] And it's what we did.
[1073.20 → 1080.08] We started counting the people because normally we have an archive of aerial, you know, surveys conducted.
[1080.46 → 1087.28] Always as is normal in clear skies, sunny days when everybody is on the beach in summer.
[1087.40 → 1097.50] So we had very well the behaviour of use of every spatial behaviour of use of every beach all across Cantabrian.
[1097.50 → 1107.54] At different days, different months, different, no matter if it is a weekend or for Labor Day, we had a huge amount of data to analyze.
[1107.54 → 1119.28] And we developed some deep learning models that even if you are changing the input signal, that means changing the aerial survey, it works.
[1119.28 → 1132.52] We could predict the sectors of every beach, not only in terms of absolute figures of population in a beach, but which are the sectors where the people try to concentrate.
[1132.52 → 1143.98] And after that, we released a small application that you can see in the notes of the podcast when you can see some maps.
[1143.98 → 1161.86] And just for curious interest, if you want to go to a place, I want to go to a beach and I would stay quiet and loose-goosey, you know, without many disturbances, you can see what places are the most suitable for that use.
[1162.78 → 1167.18] So it was a great experience, our first experience releasing something.
[1167.18 → 1169.64] Yeah, that's so fascinating.
[1169.64 → 1172.26] And it makes so much sense after you say it.
[1172.40 → 1177.18] I know here I can think of so many more applications for something like this.
[1177.30 → 1190.20] I know like in the U.S. national parks, you know, thinking about crowding and the impact on the natural environment or other things like that and helping plan out for crowds at certain points of the year.
[1190.30 → 1192.78] There's so much practical use of this.
[1192.78 → 1204.26] And this was amazing because, yeah, you took this knowledge that you had been building up and really applied it at the moment during COVID-19 when there was this specific need.
[1204.26 → 1216.40] But then it sounds like there's continued usage past that because even if I'm just a consumer, like I'm a normal citizen and I want to enjoy the beaches, this information is really useful to me.
[1216.40 → 1225.12] I know myself, I probably would go to the quiet places of the beach and sit and listen to the waves.
[1225.46 → 1226.50] So that's...
[1226.50 → 1233.40] There are much more interesting problems to try to solve than the one that I described now.
[1234.28 → 1242.46] Later, we started to work trying to modelize or to model certain aspects of how the territory works.
[1242.46 → 1250.10] You have to understand the territory as a whole, as a living entity, where everything is related to everything.
[1250.30 → 1259.10] So we started to slice every variable and try to address those variables with the help of AI.
[1259.40 → 1262.88] For example, we have developed some interesting models.
[1263.58 → 1271.60] We can delve into the, you know, the architectures you want used later on or whatever you have interested in.
[1271.60 → 1276.98] But some interesting models for detecting and classifying vegetation.
[1277.74 → 1280.72] Also for the evolution of urban growth.
[1281.36 → 1285.74] Also for things like weird, like tracking cars, for example.
[1285.88 → 1291.16] That is like a kind of proxy of the society, how the society moves.
[1291.42 → 1300.48] And because everything is on our aerial surveys, you only have to have the skills to bring back that information and convert it in something useful.
[1300.48 → 1308.60] And we have been, as the years went by, we have been able to produce some more relevant results.
[1308.82 → 1314.98] I will not talk about deep learning models, but about solutions for tracking the territory.
[1315.50 → 1315.56] Yeah.
[1315.68 → 1318.64] And you've mentioned aerial surveys a couple of times.
[1318.76 → 1323.72] It may be useful for those in our audience who don't work in geospatial.
[1323.72 → 1330.92] They might have in their mind maps and things like Google Maps where, oh, I could go, and I could look at a satellite image.
[1331.18 → 1332.54] But it's not current, right?
[1332.58 → 1336.26] It's maybe one photo that was taken some while back.
[1336.50 → 1345.08] And you've talked about aerial surveys where you can actually learn, you know, both current information about what's going on in an area, but also historical information.
[1345.08 → 1353.04] Could you just help our audience understand, like, as a professional, what sort of data do you have access to?
[1353.20 → 1357.48] And how is that gathered practically and made available to you?
[1357.48 → 1365.24] Well, I have to say that everything that I have been talking about can be also executed with satellite images, you know.
[1365.38 → 1370.54] There are some differences, but of course, you can do it with satellite images.
[1370.54 → 1382.76] The reason that we work more with aerial surveys is because we are more focused on capturing this kind of information rather than working with satellite data.
[1382.96 → 1385.36] My region, Cantabrian, is not very big.
[1385.58 → 1394.76] And we have in Spain a national plan that covers every three years all the country with aerial surveys.
[1395.34 → 1398.26] And also we have a repository of satellite images.
[1398.26 → 1402.10] So anyway, you can do both of the input signals.
[1402.72 → 1404.60] The results will differ slightly.
[1405.20 → 1416.08] But apart from image capture with sensor, no matter if it is airborne or satellite sensor, we also work with a range of technologies.
[1416.30 → 1418.58] For example, LiDAR data.
[1418.98 → 1423.36] I know that many of the audience have been working with LiDAR data.
[1424.16 → 1425.98] LiDAR can be also airborne.
[1425.98 → 1432.28] In fact, it was the origin of the technology, LiDAR using from a plane, you know.
[1432.84 → 1437.66] And it has been increasingly important in our domain.
[1438.14 → 1446.72] We also work with, you know, system of records with traditional databases and a number of things.
[1446.72 → 1455.98] If I had to say something about my job is that it is fascinating because one day we are working with COVID data, for example.
[1456.56 → 1460.48] Another day you are working with energy data.
[1460.68 → 1462.60] Another work with environmental data.
[1463.18 → 1467.58] The government of Cantabrian has powers and duties in many domains.
[1467.58 → 1470.12] It's kind of one of your states.
[1470.82 → 1474.88] If you forget the difference of area cover.
[1475.12 → 1477.08] Only Texas or Florida.
[1477.42 → 1482.36] I think Spain is in the middle between the area of Texas and Florida.
[1482.54 → 1483.36] It's something in between.
[1483.52 → 1484.36] But the whole country.
[1484.74 → 1486.64] And my region is quite small.
[1486.64 → 1491.64] But it's a very interesting place to work with because of that reason.
[1492.04 → 1497.38] And the data comes from many different technologies and many different databases.
[1497.38 → 1505.48] This is a changelog news break.
[1506.42 → 1516.46] Open Observe is a cloud-native observability platform built specifically for logs, metrics, traces, and analytics designed to work at petabyte scale.
[1516.60 → 1517.36] Huge!
[1518.08 → 1519.74] According to its creators, quote,
[1519.74 → 1527.76] It's very simple and easy to operate as opposed to Elasticsearch, which requires a couple dozen knobs to understand and tune.
[1528.40 → 1531.78] With Open Observe, you can get up and running in under two minutes.
[1532.44 → 1538.44] It's a drop-in replacement for Elasticsearch if you're just ingesting data using APIs and searching using Diana.
[1539.24 → 1542.04] Diana is not supported nor required with Open Observe.
[1542.36 → 1546.48] Open Observe provides its own UI, which does not require separate installation.
[1546.94 → 1547.60] Unlike Diana.
[1548.28 → 1548.76] End quote.
[1548.76 → 1551.42] An interesting offering indeed.
[1552.02 → 1554.74] Here are a couple choice quotes from the comments section.
[1556.56 → 1559.72] User git2dachapa says, quote,
[1560.22 → 1561.64] I just tried this three days ago.
[1562.08 → 1565.68] As someone running the home lab and hadn't set up logging yet, it was a great find.
[1566.14 → 1568.90] I didn't have to learn and combine 3-plus log technologies.
[1569.22 → 1576.00] It's just a single all-in-one monitoring server with web UI, dashboards, log, filtering, slash search, etc.
[1576.00 → 1579.46] Ram usage of the Docker container was under 100 megabytes.
[1579.92 → 1580.26] End quote.
[1580.26 → 1585.80] And user surge axe says, quote, interesting product.
[1585.92 → 1586.64] Thank you for the effort.
[1587.00 → 1588.42] Definitely want to give it a try.
[1588.42 → 1592.22] For me, though, setting up a system is not the primary pain point today.
[1592.92 → 1595.86] For what it's worth, signing up for a cloud service is not hard.
[1595.86 → 1598.72] The problem starts at the ingestion point.
[1598.72 → 1599.40] End quote.
[1599.60 → 1604.78] You just heard one of our five top stories from Monday's Changelog News.
[1605.16 → 1617.56] Subscribe to the podcast to get all the week's top stories and pop your email address in at changelog.com slash news to also receive our free companion email with even more developer news worth your attention.
[1617.56 → 1621.44] Once again, that's changelog.com slash news.
[1621.44 → 1637.64] So, Gabrielle, we talked a bit about this kind of first project related to population and crowding on beaches, but you've done so much more.
[1637.64 → 1648.66] Could you highlight a few of these things in terms of other things you've been able to identify or track with deep learning from these aerial surveys?
[1648.66 → 1654.90] Yeah, we have an extensive work in the detection of vegetation.
[1655.70 → 1674.56] I have to say that we have been also only using supervised learning, that branch of the deep learning, and specifically working with different model architectures, such as I mentioned before, USED, you know, NASCAR, CNN, and some others.
[1674.56 → 1683.50] Now we are testing now some segment anything model, but we haven't done anything with zero shot learning for production.
[1683.88 → 1692.44] So, what I am going to tell has been achieved using model architectures that have been almost forgotten for the community.
[1692.44 → 1702.38] You know, everybody is focused on the SODA architecture, and there is so much that can be extracted from the old school of artificial intelligence.
[1702.38 → 1702.58] Yeah.
[1702.96 → 1705.32] Quote, unquote, it's not so old, right?
[1705.72 → 1706.36] Yeah, yeah.
[1706.38 → 1713.20] And I think, actually, this is maybe a misconception of people that occasionally we try to mention this on a show.
[1713.20 → 1720.92] The majority of applications across enterprise, not just in GIS, but in manufacturing or marketing even.
[1721.36 → 1729.68] People think of marketing with generative AI, but the majority of applications are still traditional, quote, traditional machine learning.
[1730.10 → 1736.92] You know, there are a lot of scikit-learn models out there still, or there's just supervised learning, you know, models out there.
[1736.92 → 1743.16] And, yeah, it's awesome to see, to highlight that here, because I think it is a misconception.
[1743.64 → 1750.48] Yeah, because, you know, when a paper appears, normally they do not run out the possibilities of the model.
[1751.06 → 1762.54] The professionals who are not very specialist in the AI domain, but have a lot of knowledge in a specific domain out of AI, in my case,
[1762.54 → 1766.72] we can prepare and curate better labels.
[1767.08 → 1770.48] We can understand the process that we are trying to model.
[1771.08 → 1776.54] And we can, we have so much to give and to propose to the community.
[1777.44 → 1783.10] And that's one of the reasons that some people have said that your models are quite good.
[1783.26 → 1784.56] How have you done it?
[1784.70 → 1787.48] It's a brand-new architecture.
[1787.48 → 1789.76] It's something that you have created on your own.
[1789.76 → 1792.22] And I always say, no, it is not.
[1792.36 → 1798.90] It's just using in a smart way model architectures proposed back in 2015, 2016.
[1799.30 → 1802.34] But with a lot of data, very well created.
[1802.78 → 1807.92] I also have to say that the computer power that we have at our disposal is quite modest.
[1807.92 → 1814.82] We don't have, from that point, something, you know, big or very extensive.
[1815.34 → 1817.86] And the key is how do you create the data?
[1817.86 → 1818.46] Yeah.
[1818.46 → 1818.52] Yeah.
[1818.72 → 1833.00] And one of the things that you had mentioned prior to recording was this idea of automated cartography as kind of integration of a bunch of these different models that you've been working on.
[1833.00 → 1839.96] I'm wondering if you could kind of first describe what do you mean by automated cartography?
[1840.28 → 1844.32] And maybe even for people that aren't familiar, what is cartography?
[1844.68 → 1856.90] And, you know, I'm assuming modern cartography isn't like, you know, Magellan getting on his paper and drawing, you know, maps on parchment paper or something.
[1856.90 → 1860.78] But what does cartography look like these days?
[1860.94 → 1867.44] And then what do you mean by sort of automated cartography with these sorts of models?
[1867.86 → 1878.40] Well, cartography is the art and the science of, you know, trying to model the reality and extract the reality and plot it in a flat surface.
[1878.40 → 1885.02] It's a science that has been developing for a number of centuries, from, you know, many centuries.
[1885.62 → 1897.78] And up until now, it was highly dependent on the human, you know, ability to trace and to, you know, to draw everything on the surface of the earth.
[1897.78 → 1905.80] As the technology has been developed from the 90s, we started to move very rapidly into digital technologies.
[1906.12 → 1914.14] And the automation of the cartography has taken place not only with the advent of AI, but several decades before.
[1914.58 → 1926.14] However, this is a revolution because we have never been able to produce high such degree of quality using so few people working.
[1926.14 → 1941.06] There are some similar technologies like remote sensing, which is the part of the technology in charge of analyzing from imagery of satellites and, you know, producing cartography also.
[1941.52 → 1948.56] You know, it recalls many things of the artificial intelligence, but it can match the results in many other fields.
[1949.20 → 1950.86] So the revolution continues.
[1950.86 → 1958.34] It started, as I said before, in the 80s, 90s, but now is a complete revolution.
[1958.64 → 1967.00] And I think that for the first time we are able, we have an example that you can check it out in the description of the podcast.
[1967.00 → 1984.38] But where we have been able to produce a map with basic coverage, where you have trees, where you have shrub, where you have no vegetation, where you have buildings or roads or railroads completely generated by AI.
[1984.38 → 1999.80] Of course, it has some mistakes, but we left on purpose, those mistakes on purpose, because we wanted that the rest of the community could evaluate the capacity and the ability of the models to work alone.
[1999.80 → 2006.82] This is a question that just popped into my mind as you were talking about these models, what's possible.
[2007.22 → 2009.18] And, you know, it's not perfect, right?
[2009.26 → 2012.48] No AI system is perfect, so there's going to be mistakes.
[2012.48 → 2027.44] I'm wondering, as someone who's been in GIS and been a practitioner for, I think you said, 30 years now, I also imagine that human-based processes are error-prone, or at least they're slow, right?
[2027.48 → 2033.58] So by the time a human maybe processes a certain map or something, things have been updated, right?
[2033.76 → 2036.46] And it's maybe not current anymore.
[2036.46 → 2066.20] What do you think about the what are the implications for maybe cartography or GIS as we move to the future where AI systems maybe can do things more up-to-date, but with some mistakes, but they're up-to-date and can really maybe highlight certain areas that are incomplete or something, combined with human efforts to correct those mistakes and keep the what do you see as this balance?
[2066.20 → 2081.80] Between trying to be automated with AI-based techniques and the role that human cartographers or GIS professionals play as these systems expand to more and more places?
[2081.80 → 2095.30] Yes, it's a very interesting question because, you know, one of the big problems that we have is to maintain up-to-date every single database that we release into the market for our stakeholders.
[2095.30 → 2100.98] That's a very big problem because it's always difficult.
[2101.60 → 2108.56] And one of the main advantages of artificial intelligence is that you can have a model and you know.
[2109.06 → 2117.68] It will not probably work perfectly with the next area survey because it will have some differences in terms of colours or shadows or whatever,
[2117.68 → 2131.60] but you can fine-tune, or maybe you can train the model from scratch again, start from scratch with the training, and you can update something in a reasonable time frame.
[2131.60 → 2140.66] So that is one of the things that I'm most attracted by, the capacity of updating things.
[2141.48 → 2143.50] And it's a game changer, as I said before.
[2143.90 → 2150.04] No other artificial intelligence offers things that other technologies really don't.
[2150.04 → 2153.26] Yeah, and of course there are limitations.
[2154.20 → 2166.86] You know, AI is never, the expectation should never be that it solves all of our issues, but it also should be that it, you know, it's going to solve some of our issues or solve some of our problems, but not all of them.
[2167.08 → 2176.78] From your perspective, how do you think about the current limitations of AI within GIS and cartography?
[2176.78 → 2179.66] What are some of the things on your mind with respect to that?
[2179.66 → 2184.24] Yeah, I think, of course, you have to bear in mind that we have limitations.
[2185.12 → 2193.10] What happens to me also happens in teams in India or in the US that I am always seeing what they are doing.
[2193.58 → 2195.98] I would like to point out two limitations.
[2196.20 → 2207.26] One is the computing power and another thing is the limitations of CNS, which is the technology that we are using right now, convolutional neural networks, right?
[2207.26 → 2211.84] We can talk a little bit about model architectures and things.
[2211.84 → 2223.60] In terms of computing power, I think it's worth delving into the role of GPUs because in the geospatial realm, it's not well understood why do we need a GPU.
[2223.60 → 2241.76] And it's something, I don't know if it happens in other markets, but in our industry, when you talk to somebody about a GPU, normally my fellows and mates, I don't know, they try to say its something related with the IT department.
[2241.76 → 2245.12] I don't want to be in charge of that, but it's not at all.
[2245.22 → 2249.34] You have to be aware of what technologies do you have for calculation.
[2249.60 → 2258.36] The hardware is so important, and you have to speak the same language as a data scientist that the rest of the community speaks.
[2258.36 → 2273.84] And that is very, very important to understand that it's not the same as a GPU in your laptop, that DGX or H100, if we are talking about NVIDIA hardware, it's not the same.
[2274.00 → 2279.24] And it's everything related with the amount of data that you want to put into the train.
[2279.24 → 2294.30] You know, the quality of your training, the level of the convergence that you are going to get, if you are going to stay in a local minimum in the convergence, or you are going to reach and assess the possibility of the level that you are ingesting into the model.
[2294.72 → 2296.64] Everything is related with the hardware.
[2297.08 → 2304.38] I think that Bill Daly and Anima and Kumar in many of their talks always talk about the trinity of AI.
[2304.38 → 2307.00] One of them is, you know, the data.
[2307.80 → 2314.24] Another is the software, the algorithms that many of them have been with us for a while.
[2315.36 → 2321.18] Propagation, you know, many of those algorithms have been from the 80s, if not before.
[2321.80 → 2323.84] But the hardware is the third part.
[2324.28 → 2329.56] Bill Daly always says that it's the spike that starts this engine of creativity of AI.
[2330.20 → 2331.82] And I think it's true.
[2331.82 → 2335.24] You have to pay a lot of attention to computer power.
[2335.74 → 2340.86] And there is another limitation that is ingrained in the DNA of the CNNs.
[2340.98 → 2348.64] As far as I know, from my experience, you cannot expect to perform exactly as a human being.
[2348.88 → 2359.24] And sometimes, in spite that you create very well your labels and your chips and your data, the model does not learn as good as you expect.
[2359.24 → 2367.40] But somewhere in between, you can have a reasonable amount of success in that.
[2368.00 → 2378.14] What we do to overcome is, you know, combining different model architectures is something very useful and widespread in the geospatial industry.
[2378.14 → 2382.54] For instance, we combine models at two different levels.
[2382.68 → 2389.74] From the architectural levels, it's quite common to see the combination of Reset with, for example, UNIT.
[2390.08 → 2397.62] In Reset, you remove the last part, the fully connected layers, and connect the remaining part with UNIT.
[2397.62 → 2401.54] So you are using Reset as a feature restriction.
[2401.54 → 2402.72] For feature restriction.
[2403.40 → 2408.54] And then the rest of the decoder happens during the rest of the UNIT architecture.
[2409.08 → 2411.70] It also happens with the mask R-CNN.
[2411.84 → 2414.64] We use constantly Reset as a backbone.
[2415.14 → 2417.06] But then the rest of the model goes.
[2417.06 → 2423.20] And there is a second point, which is combining the results or the inference.
[2423.64 → 2430.48] When you have inference from two different model architectures, for example, talking about vegetation.
[2430.68 → 2438.22] Imagine that you have one model that detects very well the big areas of vegetation, but fails in the small spots.
[2438.22 → 2446.16] And you have another model that works very well for small spots, but fails detecting the big areas.
[2446.30 → 2451.52] Because the big areas create artificial holes and mistakes.
[2452.18 → 2459.44] You can combine the results of the outcomes of those model architectures with traditional GIS techniques
[2459.44 → 2469.02] to mesh all the results together and obtain a bigger, the best quality of the layer that you want to infer.
[2469.26 → 2470.80] That has worked for me.
[2471.04 → 2477.62] And it's one of the ways that we are trying to overcome the limitations of artificial intelligence.
[2477.86 → 2478.70] That's great.
[2478.86 → 2479.68] Super practical.
[2479.92 → 2482.84] And I know that's what a lot of our listeners want to hear,
[2482.96 → 2486.16] is some of the practical ways they can explore these technologies.
[2486.16 → 2490.28] Well, Gabrielle, it's been an amazing pleasure to talk to you.
[2490.32 → 2493.26] As we close out here, there's a million things we could talk about.
[2493.36 → 2496.84] I know some we didn't get to, and we'll link in the show notes.
[2496.84 → 2503.06] But as you look to the future, could you just briefly, in the last minute or so,
[2503.46 → 2509.76] just briefly share with us what's exciting for you as a GIS professional looking to the future
[2509.76 → 2512.88] that either you want to dig into next,
[2512.88 → 2519.68] or what are you encouraged by or optimistic about as you look to the future of your own work
[2519.68 → 2522.32] and how AI influences that?
[2522.66 → 2527.96] Well, I have to say that in my 30 years plus of working in the spatial industry,
[2528.16 → 2533.80] these two last years, two or so, have been the most exciting part of my career
[2533.80 → 2535.48] because it's so creative.
[2536.02 → 2538.94] We are just scratching the surface of AI.
[2539.84 → 2541.12] Great things are coming.
[2541.12 → 2545.46] I think that with the advent of Zero Shot,
[2545.58 → 2549.88] we have been watching from the first week of April
[2549.88 → 2553.96] what can be done with the SAM, the Segment Anything model.
[2554.42 → 2560.24] And I'm sure that new versions will come of future versions of SAM
[2560.24 → 2564.56] when we combine that with LLMs, with large language models,
[2564.90 → 2567.86] and we can interact with the boys and say,
[2567.86 → 2570.04] hey, draw me all the trees in the image,
[2570.24 → 2574.08] or it will be much easier to use this set of technologies.
[2574.58 → 2576.62] Anyway, just to finish,
[2577.18 → 2579.68] I would like to send a message to the audience
[2579.68 → 2584.38] for those who are not artificial intelligence researchers like me
[2584.38 → 2588.86] that it's possible to apply this set of technologies
[2588.86 → 2593.50] even though you are not a specialist on that specific domain.
[2593.50 → 2596.76] It's also to get hands-on on one of the
[2596.76 → 2601.90] take one-of-the-shelf models and start playing around with them.
[2602.60 → 2608.74] And I know the future will be absolutely focused on artificial intelligence.
[2609.38 → 2614.70] There will be a different geography in the next few decades.
[2615.14 → 2615.44] Awesome.
[2615.64 → 2616.94] Yeah, this is so inspiring.
[2617.20 → 2618.32] Thank you for your work, Gabriel.
[2618.58 → 2620.64] And it was awesome to have you on the show.
[2620.76 → 2621.46] Thank you so much.
[2621.46 → 2622.14] Thank you.
[2630.78 → 2633.34] Thank you for listening to Practical AI.
[2633.84 → 2637.68] Your next step is to subscribe now, if you haven't already.
[2638.12 → 2639.90] And if you're a longtime listener of the show,
[2640.26 → 2644.14] help us reach more people by sharing Practical AI with your friends and colleagues.
[2644.58 → 2647.88] Thanks once again to Vastly and Fly for partnering with us
[2647.88 → 2649.52] to bring you all Change Talk podcasts.
[2649.52 → 2653.92] Check out what they're up to at Fastly.com and Fly.io.
[2654.30 → 2656.72] And to our Beat Freakin' Residence, Break master Cylinder,
[2656.88 → 2659.62] for continuously cranking out the best beats in the biz.
[2659.90 → 2660.80] That's all for now.
[2661.12 → 2662.22] We'll talk to you again next time.
[2662.22 → 2674.00] Have a good one.
[2674.00 → 2674.44] Take care.
[2674.44 → 2675.90] Game on!
