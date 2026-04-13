[0.00 → 6.70] Bandwidth for Changelog is provided by Vastly. Learn more at Fastly.com. We move fast and fix
[6.70 → 11.42] things here at Changelog because of Rollbar. Check them out at Rollbar.com. And we're hosted
[11.42 → 17.66] on Linde servers. Head to linode.com slash Changelog. This episode of Practical AI is
[17.66 → 23.28] brought to you by Hired. One thing people hate doing is searching for a new job. It's so painful
[23.28 → 28.32] to search through open positions on every job board under the sun. The process to find a new
[28.32 → 33.94] job is such a mess. If only there was an easier way. Well, I'm here to tell you there is. Our
[33.94 → 38.64] friends at Hired have made it so that companies send you offers with salary, benefits, and even
[38.64 → 44.04] equity up front. All you have to do is answer a few questions to showcase who you are and what type
[44.04 → 48.90] of job you're looking for. They work with more than 6,000 companies from startups to large publicly
[48.90 → 53.88] traded companies in 14 major tech hubs in North America and Europe. You get to see all of your
[53.88 → 58.88] interview requests. You can accept, reject, or make changes to their offer even before you talk
[58.88 → 62.68] with anyone. And it's totally free. This isn't going to cost you anything. It's not like you have
[62.68 → 66.52] to go there and spend money to get this opportunity. And if you get a job through Hired, they're even
[66.52 → 70.46] going to give you a bonus. Normally it's $300, but because you're a listener of Practical AI,
[70.82 → 75.74] it's $600 instead. Even if you're not looking for a job, you can refer a friend and Hired will send
[75.74 → 81.48] you a check for $1,337 when they accept the job. As you can see, Hired makes it too easy.
[81.48 → 84.72] Get started at Hired.com slash Practical AI.
[97.92 → 103.32] Welcome to Practical AI, a weekly podcast about making artificial intelligence practical,
[103.76 → 109.26] productive, and accessible to everyone. This is where conversations around AI, machine learning,
[109.26 → 113.38] data science happen. Join the community and snag with us around various topics of the show
[113.38 → 119.22] at changelog.com slash community. Follow us on Twitter. We're at Practical AI FM. And now onto the show.
[123.48 → 129.72] Well, Chris, having a background in physics, I'm pretty psyched about today's show. Today,
[129.84 → 136.32] we have Chris and Andrew joining us, Chris Shallow and Andrew Vandenberg. I'm really excited to talk to
[136.32 → 144.64] them. I remember seeing a blog post about their work quite a while ago. And it was one of the
[144.64 → 150.90] just most interesting and exciting things that I've seen in a while related to AI because of my
[150.90 → 156.32] background and AI being applied to this physics' data. So I'm really excited to talk to them. Welcome,
[156.56 → 156.98] Chris and Andrew.
[157.00 → 157.52] I can't wait.
[157.90 → 158.68] Thanks for having us.
[159.10 → 159.62] Yeah, thank you.
[159.62 → 164.98] Yeah. Well, why don't we start off Andrew Vandenberg. Is that how we say your name?
[165.00 → 165.26] Correct.
[165.78 → 169.82] Excellent. Well, why don't you give us a little bit of intro to yourself and where you're at and
[169.82 → 170.78] what you're working on right now?
[171.20 → 177.92] Yeah. So my name is Andrew Vandenberg. I am a postdoctoral fellow at the University of Texas at
[177.92 → 186.58] Austin. What that means is I basically have a three-year job to do research into anything I want
[186.58 → 191.42] related to exoplanets. And I kind of have, you know, a free rein to do anything I want
[191.42 → 196.22] research-wise in the realm of exoplanets. And a lot of what I'll be doing, we'll talk about today
[196.22 → 202.78] on the show. I got my undergraduate degree from the University of California, Berkeley. And then I
[202.78 → 209.04] went to graduate school at Harvard University and I got my PhD last year in 2017.
[209.86 → 210.78] Hey, congratulations.
[211.26 → 211.32] Awesome.
[211.32 → 211.96] Thank you.
[212.44 → 218.96] Yeah. Congrats. That's a great thing to have that freedom and be able to kind of explore what you
[218.96 → 219.22] want.
[219.46 → 220.28] Yeah, it's really fun.
[221.36 → 225.60] Awesome. And then we have Chris Shallow. Am I saying that right, Chris?
[225.76 → 226.54] Yes, that's correct.
[227.34 → 233.84] Excellent. I got lucky. So Chris, why don't you give us a little bit of intro to yourself?
[233.84 → 243.76] Sure. So my background is actually a bit of a mixed bag. I started out in mathematics. I was studying
[243.76 → 253.02] mainly pure and applied mathematics in my undergrad degree in Australia. And then I did some research
[253.02 → 262.00] in pure mathematics. But after a while, I kind of wanted to do something with a bit more of an
[262.00 → 270.74] application into the real world rather than the theoretical world. So I briefly moved into research
[270.74 → 278.30] in biomechanical engineering. But I realized after a short period that that wasn't really for me.
[278.68 → 286.52] And so I then decided to apply for a job at Google just because I knew that Google was doing some really
[286.52 → 292.88] exciting and interesting work that I thought I would love to be a part of. So I applied for a job
[292.88 → 299.48] at Google. And that was about four and a half years ago. And since I've been at Google, I'm a software
[299.48 → 306.74] engineer here. And I spent two years working in ads, trying to make sure we were serving sort of the most
[306.74 → 316.48] relevant ads to users. Now I work in the Google AI department. We do research in anything related to AI.
[316.52 → 322.96] We have a pretty varied portfolio, obviously, because here I am talking about astronomy.
[323.58 → 328.66] And yeah, so I've been working on this project in astronomy for about a year and a half now. But
[328.66 → 335.88] other things I've worked on here include image captioning, where we try and train a model to
[335.88 → 341.24] automatically caption images with English sentences, which is another kind of interesting
[341.24 → 342.46] thing that I've been working on.
[342.60 → 343.16] That's cool.
[343.50 → 349.72] Well, yeah, it is. It is very cool. How has it? Have you enjoyed being in the real world a little bit?
[350.44 → 359.00] Yeah, it's it is great. It is great that now I can tell my friends and family what I do. And it is kind
[359.00 → 365.70] of makes a little bit more sense. They can kind of understand like a little bit more the impact of my work.
[365.70 → 375.40] That's awesome. Yeah. So how does an astronomer and a software engineer at Google AI end up working
[375.40 → 375.76] together?
[376.76 → 384.64] So I guess I can take this question. Because I was the one who kind of pitched the idea originally to
[384.64 → 391.24] Andrew. So I, well, I'm, I don't really have a background, as I said, in astronomy. But I am
[391.24 → 396.80] generally interested in science. And about a year and a half ago, I was reading a book about astronomy
[396.80 → 404.52] and the origins of the universe and the evolution of life on Earth. And, and the book was talking
[404.52 → 409.70] about exoplanets. And it mentioned NASA's Kepler mission, which we're going to talk a lot about in
[409.70 → 416.74] this podcast, which launched in 2009. And, and one of the points that was made in this book is that
[416.74 → 423.12] our technology has advanced to the point, like, like the Kepler mission, where we simply have too
[423.12 → 430.76] much data for humans to manually analyze, which is in contrast to traditional science dating back,
[430.86 → 434.86] I guess, thousands of years, where humans would make observations and then just analyze them
[434.86 → 442.24] by eye. And, and when I read this, I, I, I got a bit interested because, you know, one thing that
[442.24 → 448.84] we work on here is problems that have a large amount of data that we need good automated methods
[448.84 → 454.60] to analyze. And so I wondered, well, I guess I thought it would be really cool if I could discover
[454.60 → 463.58] a planet. So I, how would that not be cool? Yeah. So I did a little bit of research on, on Google
[463.58 → 469.78] search, basically. And I found Andrew's name, as someone who had worked with this data a lot,
[469.78 → 477.10] and basically wrote an email to Andrew pitching a collaboration with him. And obviously I did a
[477.10 → 482.58] good job because we ended up working together on this project. So I guess, and this is Chris,
[482.64 → 488.34] I was wondering if you could kind of tell us a little bit about what the goals of Kepler are,
[488.34 → 493.22] as well as, as the project itself and kind of tie it all together for, for listeners that might not
[493.22 → 501.92] be familiar with it. Uh, yeah, so I can talk about that. Kepler is a telescope in space. It was launched
[501.92 → 508.34] in 2009. And when astronomers talk about telescopes, one of the most important things that we like to
[508.34 → 514.10] say is how big it is. So Kepler is a one-meter telescope, which means that its primary mirror,
[514.10 → 520.16] the thing that it uses to collect in a focus light is about a meter across in diameter. And
[520.16 → 528.86] Kepler was NASA's first space mission specifically designed to study exoplanets. Exoplanets are planets
[528.86 → 534.88] like the ones in our own solar system, but that orbit other stars. And only in the last 20 years or so
[534.88 → 539.92] has our technology advanced to where we can actually detect them and know that they're there because
[539.92 → 546.04] they're just so much smaller and so much fainter and so much less massive than the stars that they
[546.04 → 553.64] are in the orbit. So Kepler was originally pitched in the 1980s. And over the course of about 20 years,
[554.20 → 560.92] a team at NASA kept writing proposals, trying to figure out how they could detect small planets like
[560.92 → 567.00] this. And over the course of that time, technology was advancing, digital cameras were getting better.
[567.00 → 574.04] And eventually NASA decided to fund this telescope. And the main goal of it was to try to figure out
[574.04 → 580.92] how common are the planets about the size of the Earth orbiting around stars, kind of like our Sun,
[581.64 → 588.20] at distances far enough away from the star that liquid water can exist on their surface. So basically,
[588.20 → 595.88] how common are planets like our own Earth? Are there other Earths out there? Or are we rare? Are we lucky to be here?
[595.88 → 599.32] Were any known at the time that that was proposed?
[600.04 → 605.56] Kepler was proposed before any exoplanets of any kind were known. By the time Kepler was originally
[605.56 → 612.36] chosen and given funding to go ahead, there were a handful of exoplanets, but they were mostly very
[612.36 → 621.80] large, the mass of Jupiter or so, and nothing like our own Earth. And Kepler has really ushered in this
[621.80 → 628.04] era of starting to see and know about smaller planets closer to our Earth.
[628.04 → 633.00] And could you define for a moment what an exoplanet is for those who might not know?
[633.80 → 640.52] Yeah, an exoplanet is a planet just like the ones in our own solar system, Mercury, Venus, Earth, Mars,
[641.32 → 647.16] Jupiter. And the only difference between it and the planets in our own solar system is that an exoplanet
[647.16 → 652.12] orbits a star other than our sun. And that's why they're so much more difficult to find is because
[652.12 → 653.32] they're so much further away.
[653.32 → 660.60] Interesting. Yeah. And so Kepler is this big telescope in space, and it's looking for these
[661.32 → 667.48] exoplanets. And you mentioned that, or Chris mentioned that it's producing a lot of data.
[667.48 → 673.32] I'm assuming this is like data that's coming out of like the optics and all of those things
[673.32 → 679.40] on the telescope. What does the data look like and like how much are you collecting?
[680.04 → 688.36] Right. So behind the telescope, I guess inside the telescope is more accurate, is a giant digital
[688.36 → 698.28] camera. And the way Kepler works is that every 30 minutes, it takes a picture of about 200,000 stars
[698.28 → 705.88] all at once. This is how it operated during its original mission, which ran from 2009 to 2013. And that's
[705.88 → 712.76] what we'll focus most of our time on today. Since then, its operating has changed a little bit. But during
[712.76 → 719.64] its original mission, it took pictures of about 200,000 stars all at once. That's not really the data that
[720.36 → 726.60] Chris and I are working with though. What we look for with Kepler is not trying to take a picture of the
[726.60 → 736.04] planet itself. We're trying to see how bright the star is at all of these times. So what we do is we take
[736.04 → 745.32] the images that Kepler has acquired. We measure how bright the star is in each of those images. And we
[745.96 → 754.52] construct for ourselves a time series, measurements of how bright the star is at every 30 minute interval
[754.52 → 758.60] over the course of about four years. And that's what Chris and I are fundamentally working with.
[758.60 → 766.92] We call these light curves. So just for someone that's never done this before, to me, it sounds
[766.92 → 776.84] like, so you have these images, it sounds like a pretty good amount of data mugging. Because if I'm
[776.84 → 779.72] thinking about one of these images, how many stars did you say were in an image?
[779.72 → 788.92] Right. So Kepler observed about 200,000 stars every 30 minutes for four years. So that's about 65,000
[789.48 → 792.76] observations of each of those 200,000 stars.
[793.88 → 801.16] Yeah. So how do you know which dot is the same dot in both pictures?
[801.16 → 811.24] So often they don't move very much. The telescope is very, very steady. It points at the same place
[811.24 → 817.08] and it doesn't move. So you can just track one pixel and say for periods of time up to maybe a
[817.08 → 823.00] couple of months, the star is not going to move from that pixel. So you can just identify that it's
[823.00 → 828.76] around this region and it stays there. Then afterwards, after about three months,
[828.76 → 836.84] Kepler has to roll itself because it doesn't want to look at the sun. And as it orbits around the
[836.84 → 842.52] sun, the position of the sun changes. So it rolls itself to keep its solar panels pointed towards the
[842.52 → 848.20] sun and keep it from pointing towards the sun. And at that point, you've kind of lost everything because
[849.48 → 854.52] stars have moved onto different pixels. But you can use the patterns of stars in the sky.
[854.52 → 860.12] You can identify, you know, different stars based on what's nearby. Basically, like how
[860.12 → 865.08] ancient astronomers use the constellations and figure out what we're looking at and then
[865.08 → 866.92] where other stars should be based on that.
[868.12 → 874.60] So as you're collecting all this data, and it's coming in, how do you decide, you know,
[874.60 → 881.48] how to model it, and what features you're interested from the data to hone in on for development of the
[881.48 → 885.32] model? How do you do feature selection or is it very narrow?
[886.52 → 896.04] Yeah. So for that, I think that first I should explain how we actually see the planets and know
[896.04 → 901.24] that there are planets there in Kepler data, how it was done before we started using machine learning.
[901.80 → 901.88] Okay.
[901.88 → 908.12] And then I'll let Chris explain a little bit about how we ended up deciding what particular features to use.
[908.12 → 916.12] So the way Kepler finds planets is that instead of looking for the planets directly and taking
[916.12 → 923.56] pictures of them, it watches how bright the star is at each of those 30 minute exposures it takes.
[924.36 → 930.68] And it looks for small dimming of light. So it looks for times when the star appears to just
[930.68 → 935.96] get a little bit less bright for a short period of time, and then it recovers and becomes bright again.
[935.96 → 939.88] And would that be because an exoplanet is passing in front of that star?
[939.88 → 946.28] That's exactly right. So an exoplanet is passing in between the star and the telescope,
[946.28 → 953.64] and it's casting its shadow onto Kepler. And because Kepler is so sensitive and so precise,
[953.64 → 960.60] it's able to measure even very tiny shadows, even very tiny dimming that get cast onto it.
[960.60 → 968.68] So fundamentally, what we look for is we look for these dimming, and we look for them to repeat
[968.68 → 974.36] over and over and over again. Because every time it repeats is a different time that that planet has
[974.36 → 978.36] orbited around the star and come back in front of it to where we see it.
[978.36 → 985.08] Okay. And Chris, I guess, can you kind of carry that over into the machine learning model in terms
[985.08 → 988.68] of how you select the features and what you're doing from an architectural standpoint?
[988.68 → 997.00] Sure. So the machine learning problem that we are considering here is basically we want to classify
[997.00 → 1005.48] whether a particular sequence of dimming that we observe on a star was caused by a planet or not.
[1005.80 → 1011.72] Because as Andrew mentioned, when a planet passes in front of the star relative to the telescope,
[1011.72 → 1019.08] you'll see the brightness of the star dim and then come back up again. But there are other possible
[1019.08 → 1025.24] events that can also cause the brightness of the star to dim or apparently dim as measured by the telescope.
[1025.24 → 1033.80] So one thing that can happen is you can have two stars orbiting each other rather than a planet orbiting a star.
[1034.20 → 1040.04] And when one-star passes in front of another star, you'll also see a dimming in the measured brightness.
[1040.04 → 1049.48] Another example is star spots. So some stars have dark spots on them and the stars themselves can be rotating.
[1050.36 → 1058.04] And so every time that star spot rotates in the line of sight of the Kepler telescope,
[1058.04 → 1062.84] you'll see the measured brightness dimming because of that dark star spot.
[1062.84 → 1071.64] So the machine learning problem that we're focusing on here is, okay, we see this dimming of the star.
[1072.36 → 1084.12] Was this caused by a planet or not? And obviously, one of the main ingredients into machine learning is having a training set of data that has already been labelled.
[1084.12 → 1092.60] And luckily, in the case of the Kepler mission, which ran, at least the main Kepler mission ran from 2009 to 2013,
[1093.40 → 1103.40] astronomers had paid a lot of attention to the data already and had gone in and actually classified by eye over 30,000 of these signals.
[1103.40 → 1115.58] So we already had a training set of these dimming signals where some of them were known to be planets and some of them were known to be various other phenomena,
[1115.90 → 1123.48] false positives, like I mentioned, sometimes even instrumental false positives that can cause the star to apparently dim.
[1123.96 → 1126.84] And so you asked about the feature selection.
[1126.84 → 1131.56] So I guess there's perhaps two approaches you could take here.
[1131.64 → 1143.46] One of them is you could kind of sit down, and you could think about what features you think are important for classifying one of these detected signals as either a planet or not.
[1143.98 → 1146.80] And others have actually done this with the Kepler data.
[1147.14 → 1148.84] And, you know, it works kind of well.
[1148.92 → 1152.22] This is more of a traditional machine learning approach, I guess.
[1152.22 → 1156.94] You could sit down, and you could say, OK, well, you know, what's the brightness of the star?
[1157.38 → 1160.96] What's the period of the dimming that we observe?
[1161.74 → 1165.88] How, like what percentage of the star's brightness appears to dim?
[1166.60 → 1171.50] What's the signal-to-noise ratio is a statistic that we can measure.
[1172.26 → 1179.00] And you can feed all those into a machine learning model and use those as features to make a classification.
[1179.00 → 1187.52] In this project, we actually took a slightly different approach, and we didn't sit down and think about any of those features ourselves.
[1187.84 → 1195.44] Instead, we kind of treated these light curves that Andrew mentioned as kind of like a one dimensional image.
[1196.16 → 1202.68] So if you imagine that, for example, a photograph is actually a two-dimensional image, right?
[1202.72 → 1205.14] It's like a two-dimensional grid of pixels.
[1205.14 → 1210.96] Well, what we have is we have a sequence of brightness measurements over time.
[1211.74 → 1221.24] And so we treat that one dimensional sequence of brightness measurements as kind of like a 1D photo or a 1D image.
[1221.24 → 1233.64] And so we trained a type of model called a convolutional neural network, which is exactly the kind of model that we typically use to classify photos.
[1234.16 → 1237.08] That's actually been very successful in recent years.
[1238.00 → 1247.88] And so we kind of applied a very similar model to one that is used to detect, say, cats and dogs in the photos you take on your phone.
[1248.32 → 1250.46] And we applied that to this problem.
[1250.46 → 1256.12] And so we kind of give the input as actually the light curve itself.
[1256.38 → 1258.34] And that's the only input that our model gets.
[1259.20 → 1268.96] So just as a quick follow up to that, within the kind of the family of architectures and convolutional neural networks, is there a specific architecture you selected?
[1269.20 → 1270.30] And if so, why?
[1270.30 → 1270.70] Yeah.
[1270.70 → 1271.30] Yeah.
[1271.46 → 1279.72] So in this kind of family of neural network architectures, there's, I guess, some classic ones.
[1280.18 → 1282.90] And I guess I won't go into the details of them.
[1282.96 → 1291.04] But basically, you have your fully connected architectures and your convolutional architectures and your recurrent architectures.
[1291.04 → 1295.70] And these are kind of big, big categories of neural networks.
[1295.70 → 1303.04] And basically, in this project, my approach was just tried all of them and see what works.
[1303.04 → 1304.28] So I did.
[1304.54 → 1309.46] And it turned out that the convolutional architecture was the one that worked the best.
[1309.56 → 1311.58] And that actually matched quite well with my intuition.
[1311.90 → 1315.46] Because as I said, we're treating this as like a one dimensional image.
[1315.70 → 1320.24] And convolutional neural networks have been particularly successful on images.
[1320.24 → 1327.86] And in terms of the specific convolutional architecture, the approach was just like, start with the basics.
[1328.24 → 1340.90] So at this point, we have pretty much your vanilla convolutional neural network that you would see in, you know, chapter one or like section one on the chapter about convolutional neural networks.
[1341.16 → 1343.62] It's actually very basic.
[1344.04 → 1344.14] Gotcha.
[1344.24 → 1344.36] Yeah.
[1344.36 → 1345.88] If it works, that's what you need.
[1346.30 → 1346.44] Yeah.
[1346.50 → 1349.12] No, I'm actually glad to hear you say that.
[1349.12 → 1359.72] I love you, you know, kind of emphasizing the start with the basics and kind of, you know, add complication or difference from there.
[1359.94 → 1362.86] Because the basics might work reasonably well.
[1363.20 → 1363.76] Do you have other?
[1363.88 → 1371.76] I'm curious, you know, just being a person that's, you know, occasionally, you know, developing models myself as well.
[1371.76 → 1387.78] Like when you're coming to, because I'm, you know, I'm assuming that there was no kind of, you know, public, a bunch of, you know, neural network architectures out there that people had, you know, trained for exoplanets before you guys approach this.
[1387.78 → 1401.10] Do you have any recommendations for people that might be in kind of new domain or new, they're working with a new data set and trying to figure out, you know, kind of the best match of a model with that data set?
[1401.18 → 1407.18] Do you have any kind of general recommendations around, you know, how to start and that process?
[1407.18 → 1416.50] Yeah, I think it's a good idea to have a good understanding of the basics, I guess.
[1417.26 → 1422.62] So, as I said before, you know, so I work mainly with neural networks in my job.
[1422.62 → 1436.26] So, if you are going to be, if you are going to want to train a neural network for your problem, which is often a very good idea, you know, you should know, as I said, what the basic categories of neural network are.
[1436.64 → 1445.46] And often the different categories are kind of well known to be suited to particular types of tasks.
[1445.46 → 1453.20] So, you know, convolutional neural networks are very well known for image detection, anything with an image input.
[1453.62 → 1459.08] And then recurrent neural networks are very well known when your input is language.
[1459.08 → 1462.38] So, if you have like a translation problem or something like that.
[1462.82 → 1473.14] And so, for me, you know, part of it was knowing what the sort of strengths and weaknesses of these architectures were and in what domains they've been successful in the past.
[1473.14 → 1478.58] And then I guess it was, you know, okay, my problem isn't exactly any of those previous problems.
[1478.58 → 1484.94] But can I think of it, you know, with an analogy to some other problem that has been solved before?
[1485.12 → 1488.78] So, in this case, I have one of these light curves.
[1489.46 → 1491.76] You know, there's been no models on light curves before.
[1492.14 → 1498.38] But, you know, I can imagine this being an image, but it's just a one-dimensional image.
[1498.64 → 1501.74] And that sort of led me down that path, I think.
[1501.98 → 1502.30] Awesome.
[1502.30 → 1510.44] Yeah, I appreciate your insight there because I know a lot of, I've talked to a lot of people that kind of get blocked on certain things.
[1510.52 → 1513.96] It's great to hear your process and your thoughts around that.
[1514.44 → 1524.04] Andrew, I'm curious, you know, Chris is kind of coming from this side of things where, you know, he's maybe used to working with neural networks and that sort of thing.
[1524.04 → 1532.98] I imagine, you know, the number of astronomers working with neural networks, I mean, is probably increasing after what you guys have done.
[1533.12 → 1539.04] But, I mean, none of my astronomer friends when I was in grad school, I don't think, were using neural networks.
[1539.04 → 1542.78] So, how is the reception of this kind of technique?
[1542.96 → 1550.00] And, you know, when you talked to your colleagues about, you know, what you were doing, how is their perception of that?
[1550.10 → 1556.48] And, you know, is there kind of people welcoming this sort of approach in the physics community?
[1556.48 → 1570.86] Yeah. So, I would say that even before our paper came out, we were starting to, I was starting at least to pay more attention to all the papers that came out using these new techniques.
[1570.86 → 1580.92] You know, the neural network fad hit computer science in the last five or six years, and it hasn't quite made it to my field of astronomy.
[1581.90 → 1583.76] But it's starting to get there.
[1584.02 → 1590.28] And as we were writing this paper, we kept seeing more and more people starting to work towards this area.
[1590.54 → 1599.84] And we started to see even people working on this exact same problem or very similar problems to us using increasingly sophisticated techniques.
[1599.84 → 1619.36] So, I would say that our field is starting to catch on and figure out how powerful a tool this is and start to realize that maybe this tool could provide a revolution in astronomy in the way that it's provided revolutions in other fields like image processing or translation.
[1620.50 → 1625.42] So, the reception that I've gotten when I have talks about this is always very positive.
[1625.78 → 1627.90] People are very interested in the techniques.
[1627.90 → 1630.84] They're very interested in the scientific results that we're getting out.
[1631.44 → 1638.10] And I think they're eager for us to keep working on it and also maybe thinking about doing something similar themselves.
[1638.42 → 1643.80] I've had people come up to me and ask, well, what do you think about using a neural network for this problem?
[1643.86 → 1647.84] And I'd say, well, you should ask Chris because I don't really, I'm not the expert here.
[1648.06 → 1655.08] But I think that in a lot of cases, yeah, there is a really strong interest in this in the field.
[1655.08 → 1655.80] Yeah.
[1655.80 → 1655.92] Yeah.
[1656.10 → 1663.78] So, I remember I did some like computational chemistry sort of stuff in my research.
[1663.94 → 1675.68] I remember right at the time I was kind of a couple of years from graduating, someone started applying machine learning techniques to basically do what, you know, what we were trying to do analytically.
[1675.68 → 1686.14] And I think I, at the time I felt a little bit threatened by it because I felt like I was being, you know, machine learned out of a job, maybe.
[1687.04 → 1690.92] But I think I just, you know, at that time I really had no perspective.
[1690.92 → 1696.02] So, it's great to hear that there is some excitement around that.
[1696.84 → 1698.80] So, I got a quick question for you guys.
[1699.02 → 1709.02] Did you run into any kind of challenges on your side in terms of, you know, in terms of getting the data ready, having the right data, training, validating, anything?
[1709.46 → 1711.82] Or was it pretty smooth sailing all the way through for you?
[1712.70 → 1716.34] I bet the first model that they trained was the one in the paper.
[1716.92 → 1717.82] That's my guess.
[1718.06 → 1719.82] These guys are pros, Chris.
[1720.92 → 1728.10] No, I think it was probably number 100 or 200 or something like that.
[1730.00 → 1734.80] So, actually, like, I can think of a couple of challenges we faced.
[1735.16 → 1748.86] I mentioned before that scientists had actually classified about 30,000 of these, which, if you think about it, is a huge amount of, or a huge number of light curves to have analyzed by eye.
[1748.86 → 1755.18] In most cases, I think more than one astronomer actually analyzed each of these light curves.
[1755.72 → 1763.96] But in the world of machine learning, having sort of tens of thousands of training examples is actually pretty small.
[1763.96 → 1769.64] We typically work with data sets in the hundreds of thousands, if not millions.
[1770.14 → 1782.22] And machine learning, many of the machine learning techniques that we have really shined in those big data situations, or perhaps even have been developed with those big data situations in mind.
[1782.22 → 1788.52] So, going back and having a relatively small amount of training data was actually one challenge.
[1788.52 → 1802.52] So, you know, one of the things that we did to sort of alleviate this problem, which is a very common technique in machine learning, is what's called data augmentation.
[1802.52 → 1815.18] So, one simple example that we did is, okay, let's take all of our training examples that are these light curves, these time series of brightness measurements, and let's just reverse them all, right?
[1815.22 → 1818.82] And now we have, like, twice the number of training examples.
[1819.12 → 1825.54] Because we think that if we flipped them, you know, back to front, they still should look, you know, like planets or not like planets.
[1825.54 → 1827.38] So, that was one challenge.
[1827.60 → 1834.26] On the flip side, though, I guess having a small amount of training data means that these models were very quick to train.
[1834.48 → 1839.22] So, you don't need any specialized hardware to run the model that we published.
[1839.48 → 1845.32] It actually trains in under two hours on a pretty standard, you know, desktop computer.
[1846.10 → 1848.52] So, no giant GPU supercomputers?
[1848.96 → 1852.70] No, not necessary, you know, for our previous paper.
[1852.70 → 1856.96] We're definitely working on scaling up to more training data.
[1857.12 → 1866.80] We're looking into whether we can partially simulate some extra training data, which is kind of like a more advanced step of data augmentation.
[1867.70 → 1875.66] And in that case, we, you know, we're hoping to, yeah, scale up to the GPUs or maybe even Google's TPUs, the Tensor Processing Units.
[1875.84 → 1877.10] That's what I should have said up front.
[1877.20 → 1878.82] I thought about that right after I said that.
[1878.82 → 1884.20] Yeah, so I'm really excited to be training some of these models on the TPUs.
[1884.30 → 1888.00] I've been training models on TPUs, you know, for other projects.
[1888.30 → 1895.02] And they're very, very fast, you know, and they can process enormous amounts of data in a short amount of time.
[1895.22 → 1896.86] So, that's really fun.
[1897.56 → 1901.44] And people can access those now on Google Cloud, right?
[1901.72 → 1902.54] Yes, that's right.
[1902.74 → 1907.58] They're available on Google Cloud for training all sorts of models.
[1907.58 → 1909.50] I've got to try that out.
[1909.54 → 1910.44] Have you tried it yet, Chris?
[1910.90 → 1911.74] I haven't yet.
[1912.32 → 1913.72] Yeah, we need to get on that.
[1914.26 → 1920.88] Maybe we'll live train a model on TPUs in the background on one of our shows or something.
[1921.30 → 1922.46] That sounds like a great idea.
[1924.36 → 1926.80] So, I am curious.
[1927.38 → 1929.46] You set out to find planets.
[1929.46 → 1932.44] How many exoplanets have you discovered?
[1932.76 → 1937.08] And do any of them have aliens on them, to your knowledge yet?
[1938.74 → 1944.30] So, at the moment, we have discovered two exoplanets.
[1945.68 → 1951.86] This was in the announcement that we made, like, last December.
[1952.24 → 1953.46] The cool thing about...
[1954.24 → 1955.90] Well, there are several cool things about these two.
[1955.90 → 1960.00] So, first, we turned our attention...
[1960.00 → 1965.22] Once we had a model that worked, we turned our attention to actually a small subset of the stars to search.
[1965.38 → 1968.74] Because our first paper was more of a proof of concept.
[1969.26 → 1975.04] So, instead of, you know, being ambitious and searching the entire data set of 200,000 stars,
[1975.14 → 1979.18] we decided to search just a subset of 670 of those stars.
[1979.18 → 1985.54] And the stars that we searched were all stars that were known to have multiple planets around them already.
[1986.44 → 1992.32] And so, these stars had actually already been searched, you know, multiple times in the past.
[1992.44 → 1996.60] This data had been searched for new planets, you know, multiple times.
[1996.82 → 2004.72] And yet, our model was able to go in and find two planets that all the previous searches had missed.
[2004.72 → 2010.94] So, that was one of the first cool things was that, you know, our model was not only finding more planets,
[2011.06 → 2017.38] but it was finding planets that had kind of evaded detection of the previous techniques.
[2017.84 → 2020.24] So, you know, that was...
[2020.24 → 2022.12] Did you get to name them Andrew and Chris?
[2022.12 → 2025.32] No, unfortunately, we didn't get to name them.
[2025.72 → 2030.98] But the cool thing about these planets is one of the planets was the sixth planet discovered around its star.
[2031.20 → 2036.52] But the other planet, called Kepler-90i, was the eighth planet discovered around its star.
[2037.16 → 2038.40] And this is actually a milestone...
[2038.40 → 2038.68] Wow, that's crazy.
[2038.84 → 2044.46] Yeah, this is a milestone, actually, because this actually made that planet a record breaker,
[2044.60 → 2046.06] or at least a record equaler.
[2046.06 → 2052.22] Because as of that point, we did not know of any other star, apart from our own sun,
[2052.70 → 2054.52] that had eight planets around it.
[2054.90 → 2062.08] And so, our discovery of this planet kind of bumped off our own sun as the sole record holder
[2062.08 → 2064.30] of having the most known planets.
[2064.86 → 2065.20] So, now we know...
[2065.20 → 2066.16] A little history making.
[2066.28 → 2066.48] Yeah.
[2066.58 → 2071.42] So, now we know of actually two stars, at least, that have eight planets around them.
[2072.12 → 2072.90] That's amazing.
[2072.90 → 2076.90] So, as you were saying that, and I guess I didn't even really...
[2077.72 → 2081.62] You know, it didn't come to my mind before thinking about the multiple planets.
[2081.72 → 2088.80] So, if you've got eight planets, you know, are they all making these dips in the light curves?
[2088.98 → 2097.68] If so, how do you kind of distinguish between the dips, you know, for one planet versus another?
[2097.68 → 2103.02] Is that by, like, intensity or something in the depth of the dip?
[2103.40 → 2105.84] Or how does that work out?
[2105.96 → 2110.24] And was that kind of challenge in processing that data?
[2111.42 → 2112.86] Yeah, I can take this one.
[2113.34 → 2114.08] So, you're right.
[2114.54 → 2118.74] The different planets will cause dips that look a little bit different.
[2118.74 → 2124.44] So, the deeper the dip, the bigger the planet that must have caused it, because that means
[2124.44 → 2126.80] the larger the shadow that was cast on Kepler.
[2127.38 → 2133.64] So, you could actually use how much brightness was blocked to measure how big that planet was.
[2134.22 → 2137.24] So, if you have a big planet, it'll make a deep dip.
[2137.64 → 2139.58] If you have a small planet, it'll make a shallow one.
[2140.06 → 2141.90] That's one of the ways you can tell the difference.
[2141.90 → 2145.22] But the most fundamental way you can tell is just when it happens.
[2145.78 → 2151.40] Because generally, planets proceed along in their orbits, and it's almost like clockwork.
[2151.54 → 2156.78] They come back and go in front of their star after the same interval of time, every orbit.
[2157.54 → 2162.22] For our Earth, that interval of time is 365 days.
[2162.32 → 2162.70] It's a year.
[2163.48 → 2169.08] For the planets, these two new planets that we discovered, they were both about two weeks.
[2169.08 → 2176.04] So, when you look at the light curves for these stars that have many, many planets all going
[2176.04 → 2180.40] in front of the star, you'll see dips that repeat every 14 days.
[2180.54 → 2183.10] You'll see dips that repeat every 300 days.
[2183.24 → 2186.32] You'll see dips that repeat every 60 days, for example.
[2186.60 → 2190.14] And all of those dips, you can identify the periodicity.
[2190.34 → 2193.00] And that's how you separate out which planet is causing which dip.
[2193.74 → 2194.66] That helps a lot.
[2194.92 → 2195.68] Appreciate it.
[2196.18 → 2196.74] Thanks for that.
[2196.74 → 2200.04] So, I heard that you had made your model open source.
[2200.48 → 2204.42] And I guess I was just wondering what the reasoning behind open sourcing it was.
[2204.66 → 2207.92] And what do you hope others might achieve with it going forward?
[2209.24 → 2209.72] Yeah.
[2209.82 → 2219.08] Well, so, I generally, personally believe in open sourcing or releasing as much of the research
[2219.08 → 2221.52] that I do as possible.
[2221.52 → 2229.20] And I think I'm actually glad to work in this team at Google that is generally very open about
[2229.20 → 2229.90] our research.
[2230.12 → 2236.56] And so, I actually published this model in a TensorFlow repository on GitHub that has, you
[2236.56 → 2237.88] know, many, many models.
[2238.04 → 2242.62] I think it probably has dozens of models there that have all been open sourced.
[2242.62 → 2249.90] So, I just think, in general, you know, when you do some research, and you publish the paper,
[2250.02 → 2255.22] you do that, you know, not only to share the result that you got, but also in the hope that
[2255.22 → 2256.22] others can build on it.
[2256.40 → 2260.88] And so, you know, part of that is the paper, which details, you know, the methods.
[2261.14 → 2266.32] But, you know, in computer science, you also have the code that actually produce those results.
[2266.32 → 2271.62] And so, that was sort of the reasoning behind releasing the code.
[2271.92 → 2278.88] I certainly hope that this, you know, at the very least, is a starting point for, you know,
[2278.94 → 2285.36] anyone in astronomy or other fields that has a problem similar to ours that, you know, may
[2285.36 → 2287.26] be able to apply a similar technique.
[2287.44 → 2294.30] For example, I know that even Andrew has a student who is interested in using this code that,
[2294.30 → 2302.84] you know, we made public to search for exoplanets in the K2 mission, which is actually the Kepler's
[2302.84 → 2306.58] second mission, the same telescope, but looking at different areas of the sky.
[2307.28 → 2312.14] And so, I think that's, you know, that's like a real no-brainer, you know, in order to have
[2312.14 → 2316.92] maximal impact of this work we did is to sort of allow others to build off it.
[2317.60 → 2323.30] Is any of the data, you know, from the Kepler mission or maybe other things within NASA,
[2323.30 → 2325.26] I know some things are public.
[2325.80 → 2327.16] Is that data available?
[2327.36 → 2330.86] Like, can I detect my own planets, or how does that work?
[2331.44 → 2331.86] Absolutely.
[2332.16 → 2332.48] Awesome.
[2332.98 → 2338.94] Generally, NASA data is all public because it's paid for by the taxpayers.
[2339.16 → 2341.78] So, the taxpayers should be able to access their data.
[2342.46 → 2348.74] And that philosophy is really great because it encourages outsiders to the community like
[2348.74 → 2352.60] Chris and amateur astronomers to take a look through the data.
[2353.14 → 2356.24] When I say it's public, it doesn't have to be public immediately.
[2356.48 → 2359.66] Usually, there's some period of time before it becomes public.
[2360.20 → 2364.66] But if you wanted to look up a picture taken by Hubble, you can go to the Hubble archive.
[2365.20 → 2370.34] If you wanted to look up a picture taken by the Spitzer Space Telescope, you could go to
[2370.34 → 2371.16] the Spitzer archive.
[2371.54 → 2375.56] So, in general, all the data is public and freely available for people to go and make
[2375.56 → 2376.32] discoveries with.
[2376.32 → 2377.00] Awesome.
[2377.76 → 2384.48] And I would just add to that if you do want to download the Kepler data and train
[2384.48 → 2389.92] your own models, if you download the full Kepler data set, it's over 3 million files.
[2390.78 → 2395.06] And it took me about two weeks to download.
[2395.16 → 2395.52] Oh, wow.
[2396.16 → 2399.40] And I needed an external hard drive as well.
[2399.86 → 2401.04] So, you know.
[2401.06 → 2402.30] That's your caveat right there.
[2402.30 → 2402.78] Yeah.
[2404.46 → 2406.08] That's great.
[2406.24 → 2407.72] Good disclaimer.
[2408.66 → 2414.00] You know if you're sitting in Starbucks right now, you might not want to start the download.
[2414.70 → 2416.18] But yeah, awesome.
[2416.36 → 2419.82] So, I mean, you guys have discovered planets.
[2420.40 → 2421.70] Where do you go from there?
[2421.90 → 2422.86] What's next?
[2422.86 → 2431.96] So, I told you at the beginning of this podcast that the main goal of Kepler was to figure out
[2431.96 → 2434.34] how common planets like our Earth are.
[2434.34 → 2441.56] And after the mission launched, Kepler took data in its original mission for about four
[2441.56 → 2441.98] years.
[2442.68 → 2445.50] People started trying to estimate that number.
[2446.06 → 2449.94] But the numbers that people are getting are fairly discrepant.
[2450.24 → 2452.94] They can range over more than a factor of 10.
[2452.94 → 2459.96] And that means we really don't have a very precise and accurate estimate of how common
[2459.96 → 2461.36] planets like our own Earth are.
[2462.12 → 2463.62] And there are a couple of reasons for this.
[2463.90 → 2465.90] One of them is that they're very, very hard to detect.
[2466.34 → 2468.38] They're right at the edge of Kepler's sensitivity.
[2468.92 → 2471.12] Kepler is our most powerful planet hunter.
[2471.74 → 2477.78] But for planets this small and for planets orbiting that far away from their stars, it's just
[2477.78 → 2480.68] a really, really difficult challenge to detect them.
[2480.88 → 2482.50] So many of them get missed.
[2483.74 → 2490.28] Another challenge is that even for the ones that might get found, it's very hard to separate
[2490.28 → 2498.42] out these weak signals, the very weakest signals, from the signals caused by false positives.
[2498.42 → 2502.22] Like Chris was talking about earlier, maybe a star going in front of another star.
[2502.84 → 2510.96] Or perhaps a more scary example, something weird that happened on Kepler, on the spacecraft,
[2510.96 → 2513.20] that caused a glitch in the data.
[2513.96 → 2519.20] And those things are fairly common when you're looking at such tiny signals.
[2519.20 → 2526.62] So a big challenge in our field is to try to make this measurement more precise and more
[2526.62 → 2528.34] accurate and make it something believable.
[2528.98 → 2530.40] And a lot's riding on this.
[2530.62 → 2538.58] NASA built Kepler as part of its long-term strategy to eventually take pictures of planets like
[2538.58 → 2542.22] our own Earth and figure out if there are other planets with life on them.
[2542.22 → 2546.52] Because if you can take a picture of a planet with a very, very sophisticated, expensive,
[2546.76 → 2553.82] giant space telescope in the future, then you can search for indications that there might
[2553.82 → 2557.92] be life, such as oxygen and methane in that planet's atmosphere coexisting.
[2558.26 → 2562.80] That's something we have on Earth that is very difficult to produce without something biological.
[2562.80 → 2567.56] But in order to build these telescopes, we need to know how common planets like this are
[2567.56 → 2569.84] so we know how capable the telescopes need to be.
[2570.38 → 2574.30] So our sights are kind of set on trying to improve this measurement.
[2574.96 → 2580.50] We've shown already that if we use our new strategy and our new techniques and machine
[2580.50 → 2585.58] learning and deep neural nets, we can find signals that were previously missed.
[2585.58 → 2592.04] So the next question is, can we take this the next step and find these extremely exciting
[2592.04 → 2599.38] signals of Earth-like planets in long period orbits, periods of about a year around stars
[2599.38 → 2603.86] like our Sun and orbits where they could potentially sustain liquid water?
[2604.30 → 2610.42] And can we reliably separate them out from all the potential false alarms?
[2611.00 → 2612.44] So that's kind of the next step.
[2612.44 → 2614.92] That'll be another extra layer of difficulty.
[2615.58 → 2618.34] But the reward is huge if we can get there.
[2618.52 → 2623.12] It's a really important thing for us to measure if we want to continue down this path and eventually
[2623.12 → 2625.88] try to find signs of life outside our solar system.
[2626.66 → 2627.76] That is very cool.
[2628.22 → 2633.90] Well, thank you both for coming on to the show and telling us all this amazing things that
[2633.90 → 2637.58] you've been using with neural networks and astronomy to find exoplanets.
[2638.04 → 2638.94] You're real trailblazers.
[2638.94 → 2643.82] And I think a lot of other scientists out there hopefully will learn to use these same tools
[2643.82 → 2646.94] and find them as accessible as you guys did.
[2647.14 → 2648.60] So thank you very much.
[2648.92 → 2651.82] And I appreciate you guys coming on the show.
[2652.36 → 2652.60] Sure thing.
[2652.72 → 2653.92] Thanks for having us on.
[2654.20 → 2654.40] Yeah.
[2654.44 → 2655.22] Thanks for having us.
[2655.22 → 2657.96] All right.
[2658.02 → 2660.64] Thank you for tuning into this episode of Practical AI.
[2660.90 → 2662.36] If you enjoyed the show, do us a favour.
[2662.48 → 2663.08] Go on iTunes.
[2663.20 → 2663.86] Give us a rating.
[2664.12 → 2666.00] Go in your podcast app and favourite it.
[2666.08 → 2668.82] If you are on Twitter or social network, share a link with a friend.
[2668.90 → 2669.58] Whatever you got to do.
[2669.80 → 2671.26] Share the show with a friend if you enjoyed it.
[2671.54 → 2674.22] And bandwidth for changelog is provided by Vastly.
[2674.32 → 2675.78] Learn more at fastly.com.
[2675.98 → 2679.16] And we catch our errors before our users do here at changelog because of Rollbar.
[2679.16 → 2681.16] Check them out at rollbar.com slash changelog.
[2681.16 → 2684.60] And we're hosted on Linde cloud servers.
[2684.92 → 2686.56] Head to linode.com slash changelog.
[2686.66 → 2687.10] Check them out.
[2687.18 → 2688.02] Support this show.
[2688.42 → 2691.62] This episode is hosted by Daniel Whiten ack and Chris Benson.
[2692.10 → 2693.54] Editing is done by Tim Smith.
[2693.78 → 2695.82] The music is by Break master Cylinder.
[2696.26 → 2699.64] And you can find more shows just like this at changelog.com.
[2699.86 → 2701.78] When you go there, pop in your email address.
[2702.08 → 2705.90] Get our weekly email keeping you up to date with the news and podcasts for developers
[2705.90 → 2708.10] in your inbox every single week.
[2708.48 → 2709.26] Thanks for tuning in.
[2709.40 → 2710.18] We'll see you next week.
[2711.16 → 2712.16] Bye.
