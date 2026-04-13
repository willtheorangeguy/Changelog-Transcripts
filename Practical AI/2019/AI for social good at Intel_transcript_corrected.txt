[0.00 → 2.58] Bandwidth for Changelog is provided by Vastly.
[2.96 → 4.86] Learn more at Fastly.com.
[5.08 → 8.16] We move fast and fix things here at Changelog because of Rollbar.
[8.30 → 9.98] Check them out at Rollbar.com.
[10.24 → 12.40] And we're hosted on Linde cloud servers.
[12.76 → 14.76] Head to linode.com slash changelog.
[20.96 → 26.24] Welcome to Practical AI, a weekly podcast about making artificial intelligence practical,
[26.68 → 28.40] productive, and accessible to everyone.
[28.40 → 33.32] This is where conversations around AI, machine learning, and data science happen.
[33.80 → 38.06] Join the community and snag with us around various topics of the show at changelog.com slash community.
[38.58 → 39.22] Follow us on Twitter.
[39.36 → 40.62] We're at Practical AI FM.
[41.10 → 42.14] And now onto the show.
[47.04 → 49.04] Welcome to the Practical AI podcast.
[49.44 → 53.78] This is Chris Benson, your co-host, as well as the chief AI strategist at Lockheed Martin,
[54.02 → 55.46] RMS, APA innovations.
[55.46 → 60.54] This week, you're going to hear one of a series of episodes recorded in late January 2019
[60.54 → 63.92] at the Applied Machine Learning Days conference in Lausanne, Switzerland.
[64.26 → 68.88] My co-host, Daniel Whiten ack, was going to join me, but had to cancel for personal reasons
[68.88 → 69.88] shortly before the conference.
[70.28 → 72.22] Please forgive the noise of the conference in the background.
[72.62 → 75.46] I recorded right in the midst of the flurry of conference activities.
[75.92 → 80.86] Separately from the podcast, Daniel successfully managed the AI for Good track at Applied Machine
[80.86 → 83.62] Learning Days from America, and I was one of his speakers.
[84.20 → 86.86] Now, without further delay, I hope you enjoy the interview.
[90.32 → 96.34] My guest today is Anna Bethe, who is the head of AI for Social Good at Intel.
[96.66 → 97.76] Welcome to the show.
[98.14 → 98.58] Well, thank you.
[98.64 → 99.82] And thanks for having me on here.
[99.94 → 104.36] Well, could you start us off by telling us a little bit about you and how you got where
[104.36 → 104.66] you are?
[104.66 → 105.34] Sure.
[105.64 → 112.74] So I studied aerospace engineering at MIT and focused, I guess, in grad school on human
[112.74 → 113.54] factors engineering.
[113.74 → 117.70] So this is basically how users interact with computers.
[118.36 → 125.10] So specifically, my lab was looking at complex algorithms and scenarios for having a single
[125.10 → 126.90] operator operate multiple drones.
[127.10 → 130.30] This is where the aerospace ties very loosely into it.
[130.30 → 135.02] And this was probably about 10 years back, so drones were starting to be utilized more
[135.02 → 135.40] and more.
[136.10 → 141.82] But then how does somebody integrate all this information and be able to do path planning,
[141.94 → 142.22] et cetera?
[142.68 → 146.96] Gave me a taste to statistics as well as data visualization.
[147.64 → 154.32] So once I graduated, I was doing some geospatial data analytics, first at MIT Lincoln Labs, then
[154.32 → 158.40] at Argonne National Labs, moved to a data science consulting type of place.
[158.40 → 160.50] And now I'm here at Intel.
[160.72 → 167.06] When I joined Intel, I was still doing like data science, looking at natural language processing
[167.06 → 172.06] in particular, doing some deep learning research, trying to figure out how do we make these algorithms
[172.06 → 173.22] really run quickly.
[173.88 → 180.80] But I'd always been very interested in, I guess, applying these skills in a way that was more
[180.80 → 184.22] beneficial for humanity, beneficial for the world.
[184.22 → 188.26] I had been volunteering with an organization called Delta Analytics.
[188.80 → 193.82] They paired data science volunteers, software engineer volunteers with like nonprofit organizations.
[194.46 → 197.74] And I just wanted to make it more of my day-to-day job.
[198.00 → 203.64] We, I had seen a number of different projects at the company that we'd been doing that had
[203.64 → 204.22] these missions.
[204.22 → 209.94] So like helping detect like which kids are most at risk of online predators based on their
[209.94 → 212.02] conversations, other things like this.
[212.02 → 216.78] And I can go into those more, but I sort of decided that this was what I really wanted
[216.78 → 217.22] to do.
[217.38 → 222.28] So, but I didn't see a very easy way of getting involved in them.
[222.36 → 225.00] It was like, you know, go talk to that person or that person.
[225.00 → 227.08] And it's like just scattered and crazy.
[227.08 → 232.42] So I suggested this role, said, you know, I think we should have a program.
[232.54 → 237.06] I think that there should be a way to bring in more of these types of programs.
[237.06 → 243.48] So talking to the nonprofits, talking to individuals, talking to organizations or for profits too,
[243.56 → 249.44] that are really trying to move the meter on helping out individuals, helping out the environment,
[249.64 → 251.42] helping the world, basically.
[251.42 → 255.74] I know that sounds a little bit cliché, but these social impact projects.
[256.04 → 262.76] So that's sort of how I became what I am doing today, which is being that coordinator,
[263.00 → 265.98] point of contact, as well as an advocate for these programs.
[266.66 → 271.84] So I love the fact that you saw that need and kind of created your own job by way of suggestion.
[272.30 → 277.28] Before you got to that point, was there a moment you talked, you just alluded to some of these
[277.28 → 281.40] initiatives that you got involved in before you ever even got to Intel that had an impact
[281.40 → 282.72] Was there a moment in particular?
[282.86 → 285.74] Could you tell us about maybe one of the projects you were working on,
[285.80 → 288.48] which made you realize this was what you wanted to do?
[288.58 → 290.54] And what was it about that project that did it?
[290.98 → 291.14] Sure.
[291.46 → 296.44] And I guess it actually even started before I was a volunteer with Delta Analytics.
[296.44 → 302.28] But I had been hearing about this AI for good type of and data for good type of idea
[302.28 → 309.58] and went to DSSG, the Data Science for Social Good conference out brief at the University of Chicago.
[309.58 → 315.40] So they had like a couple of day conference-y type thing and just showcased a bunch of these
[315.40 → 319.52] different projects, talked about, you know, like what these different grad students were
[319.52 → 321.14] doing, what these nonprofits were up to.
[321.50 → 327.72] So when I heard about Delta, like I started to like to follow these different things on social
[327.72 → 328.04] media.
[328.22 → 332.94] And it seemed perfect because, you know, it was a way to really get my hands dirty.
[332.94 → 337.10] I was working with the organization Open Media Foundation.
[337.38 → 342.94] And basically what they do is they go into these local town halls, governments, and help
[342.94 → 347.94] them record their meetings so that everybody in the community can hear what happened.
[348.14 → 353.50] They do some like speech-to-text translation to transcribe all the meetings.
[353.96 → 356.02] And so they have a bunch of different text.
[356.54 → 359.98] So I was like, oh, you know, this is like my kind of data.
[359.98 → 360.62] I love this.
[360.88 → 367.02] Tons of data, tons of text, very messy, no punctuation, which was really difficult with
[367.02 → 368.58] a lot of different NLP techniques.
[369.30 → 374.36] And the issue that OF was seeing is that, you know, they had all this information, but
[374.36 → 377.08] they didn't have any tags on it.
[377.16 → 381.52] So they didn't know if a town hall was about water usage, it was about urban development,
[381.70 → 383.98] planning, taxes, et cetera.
[384.20 → 386.62] So what they wanted to do was do label.
[386.62 → 389.84] This is something that NLP is quite good at.
[390.18 → 396.98] So, you know, with a team of three other individuals, we looked at the data and tried to figure out
[396.98 → 397.70] how to do this.
[397.76 → 402.34] And one of the hardest parts is that there are no labels whatsoever.
[402.34 → 404.60] So it's completely unsupervised.
[404.72 → 407.36] So used some techniques called LDA.
[407.36 → 412.28] So this is an unsupervised type of text clustering-is type thing.
[412.78 → 415.46] And, you know, figured out suggestions.
[415.86 → 418.20] Had a few like very simple dashboards.
[418.90 → 421.06] Both this was mostly done in Python.
[421.20 → 422.34] The dashboards were done in R.
[422.46 → 425.76] So a combination of different types of tools along the way.
[425.76 → 431.36] And at the end of the day, we were able to figure out, you know, three or four tags per
[431.36 → 432.02] meeting.
[432.82 → 435.20] And, you know, it works pretty well.
[435.48 → 438.44] So handed that off to OF.
[438.66 → 445.52] And now they are putting that into their website so that the local town governments can bring
[445.52 → 450.46] that in to their into their APIs and say, oh, yeah, you know, like this is what we were
[450.46 → 451.08] talking about.
[451.08 → 456.34] And then somebody who is very interested in this type of information can then say, I really
[456.34 → 461.18] want to know just in general, either at a local level or an entire national level, because
[461.18 → 467.66] they have different government groups that are nationally, you know, I want to know whenever
[467.66 → 472.48] there's any talk about gun control potentially or whenever there's anything about like health.
[473.14 → 473.34] Fascinating.
[473.48 → 478.88] When you got to Intel and you had had these experiences, I assume you came in under a different
[478.88 → 480.00] role initially.
[480.56 → 480.78] Yeah.
[480.78 → 483.70] What prompted you to say, hey, this is what I want to do.
[483.80 → 487.82] I'm going to go invent my own job and go make this thing happen here in this organization.
[488.14 → 491.06] That's, you know, I had you been there long or were you still new?
[491.36 → 492.50] I was still pretty new.
[492.56 → 497.20] So I guess I've been at Intel for about two years now, and I created this role last April.
[497.36 → 499.50] So I'd been there just a little bit over a year.
[499.94 → 503.58] And my title beforehand was a deep learning data scientist.
[503.58 → 505.46] So completely different.
[505.46 → 508.36] Very much hands on coding, research oriented.
[508.36 → 512.00] And so I guess like a little bit more into the backstory.
[512.00 → 519.34] When I had joined Intel, like there was this idea of having like sort of a more core data
[519.34 → 520.52] science type of group.
[520.52 → 525.72] And I thought that I was going to be working on more of a social impact project.
[525.72 → 528.86] And no, I didn't come in as a deep learning data scientist.
[528.86 → 533.04] I came in as sort of data scientist just in general into another group.
[533.04 → 537.12] That group got merged into another all sorts of complexities.
[537.12 → 540.68] But I was essentially doing sports data analytics first.
[540.96 → 543.86] And then I was doing the deep learning natural language processing.
[544.32 → 545.96] So, but it was short.
[546.08 → 547.42] So I usually just skip that over.
[547.76 → 548.62] Well, that's not unusual.
[548.80 → 552.76] Right now with the field evolving as fast as it is, not only deep learning specifically,
[552.92 → 557.74] but data science in general, that it seems like people are moving around from position
[557.74 → 559.92] to position within organizations pretty quickly.
[560.30 → 560.68] Exactly.
[560.68 → 567.10] No, and I knew that sports data analytics was not going to be like where I wanted to
[567.10 → 567.32] be.
[567.48 → 572.82] I know for many people, that's like their dream job because sports and data science.
[573.34 → 573.78] Oh yeah.
[573.96 → 580.98] It's like, but yeah, no, I call a lot of sports ball, and you know, it's, it is interesting
[580.98 → 583.48] data, but it wasn't the data for me.
[583.92 → 585.28] It wasn't just the right fit.
[585.44 → 587.84] So how did you know that this was going to be the right fit?
[587.84 → 590.62] What actually got you to put it forth?
[591.30 → 595.72] It's just something that I knew that I am super passionate about.
[595.98 → 600.52] I'd been loving the work that I was doing for, with Delta analytics.
[601.50 → 605.56] And I don't know, I guess I just decided to give it a shot.
[605.64 → 611.50] I've always heard that you can create your own role, that you can advocate for what you
[611.50 → 612.36] would like to do.
[612.36 → 616.42] And you can talk to your manager, talk to like other managers.
[616.42 → 620.78] I approached probably like five or six different people about this.
[620.78 → 629.30] Um, and I was very pleasantly surprised when they were very like unanimously for this and
[629.30 → 635.10] like had my back and, you know, helped me clarify like what I was going to be doing.
[635.10 → 640.08] And it's, it's changed a little bit, and it's like ever morphing, but I don't know.
[640.14 → 640.98] It's, it's cool.
[640.98 → 645.90] So can you share with us what your vision is for this role?
[645.90 → 650.38] And not, not only I'd like to get a sense of what did you pitch to them originally and
[650.38 → 653.40] how has it evolved, uh, in this time that you've been in the role?
[653.98 → 654.28] For sure.
[654.52 → 659.02] So one of the biggest things that I would like to do, and this is something that I'm still
[659.02 → 663.38] figuring out how to do most efficiently is to bring in more programs.
[663.38 → 668.52] So to be able to help more organizations that are having a social impact.
[668.52 → 675.42] And the hardest thing with that so far has been trying to figure out like, where are all
[675.42 → 677.64] of the resource areas?
[677.78 → 682.28] So who are the different people that have the capacity to take on another project?
[682.28 → 687.46] Because we're all, you know, like working as hard as we can already on a lot of other
[687.46 → 692.48] things, whether it's research or research and development, or like working on these proof
[692.48 → 698.54] of concept projects with other groups, you know, our time is pretty much, well, their time
[698.54 → 699.48] is pretty much tapped.
[699.48 → 706.08] So trying to figure out with the managers of other organizations, what we can do and how,
[706.18 → 709.20] how to sort of like leverage the company.
[709.20 → 714.82] One of the things I'd love to be able to do, and I'm still figuring it out, is to involve
[714.82 → 717.56] more than also just like my own business unit.
[717.80 → 719.80] Like Intel is ginormous.
[720.12 → 723.88] I don't know the stats on like how many employees we have, but it's a lot.
[724.22 → 725.42] And it's everywhere.
[725.54 → 727.10] It's a very global organization.
[727.88 → 734.60] So how do I get more people that are, you know, like me really wanting to work on these
[734.60 → 735.44] types of projects?
[735.44 → 739.34] And sometimes I get emails being like, oh, I want to do this so badly.
[739.50 → 743.56] And so like, you know, I have a little list going of, of people that can help on the projects,
[743.56 → 751.30] but you know, I don't, I also don't want to like be taking them from like their day jobs
[751.30 → 751.64] too.
[751.94 → 757.42] So, you know, it's, it's sort of like a, a line, I guess, to walk.
[757.42 → 759.08] So, no, it sounds great.
[759.22 → 764.92] So as you did this and as you're making the pitch internally to get the role into place,
[765.06 → 768.40] how did you approach justifying it?
[768.46 → 773.34] Given the fact that, you know, you're working for a for-profit corporation, it's in business
[773.34 → 774.50] to make a profit.
[774.72 → 777.28] And as are all of many of our employers, certainly mine.
[777.42 → 781.24] So how did you approach that on them seeing the value of this kind of role?
[781.24 → 782.32] For sure.
[782.46 → 787.38] And I think one of the things that's been the most beneficial of this last nine month
[787.38 → 792.18] or something period is to really start to see how to do that.
[792.40 → 796.26] So coming from an engineering background, you know, didn't really have a lot of business
[796.26 → 798.68] classes, didn't really have a lot of marketing classes.
[799.14 → 804.50] So, but one of the things that I've been doing a lot is talking about these projects, both
[804.50 → 808.86] internally and externally and showing a few different things.
[808.86 → 815.06] So when I pitched it, you know, I didn't give any business objectives or any metrics or
[815.06 → 816.42] like things like that.
[816.48 → 818.46] And now I'm starting to put those together.
[819.36 → 823.88] And a lot of what we're seeing, though, is it sort of helps the business in a few different
[823.88 → 824.14] way.
[824.60 → 830.44] One is marketing, you know, talking about these really socially beneficial projects.
[830.64 → 834.82] It gives you all the warm feels, and they're lovely to talk about.
[834.90 → 836.34] They're fascinating as well.
[836.34 → 838.10] So that's one thing.
[838.86 → 841.78] The other is hiring and retention.
[842.18 → 847.68] A lot of the workforce today really just want to work on these projects that are impactful.
[848.36 → 853.26] You know, recommender systems are great or like figuring out the sentiment of Twitter.
[853.92 → 854.64] It's also great.
[854.72 → 859.48] Like these projects have a place in things, but a lot of the workforce want to do something
[859.48 → 861.10] that is more impactful.
[861.10 → 866.96] So instead of looking at a social media, we'll just, you know, anonymize the social media source,
[867.12 → 874.18] looking at any social media for or online source for a sentiment or a categorization, instead
[874.18 → 879.46] looking at it to figure out what is harassing text or not, or to try to figure out, you know,
[879.48 → 883.42] like what types of information do kids globally have access to?
[883.42 → 885.94] And that's the things that we really want to be working on.
[886.72 → 890.74] The third actually is really relevant also to our hardware.
[890.86 → 892.68] So Intel, we sell a bunch of hardware.
[892.84 → 893.88] That's our bread and butter.
[894.62 → 901.00] And without being able to do these types of projects, we wouldn't see the entire range of use cases.
[901.00 → 904.62] So we've done a bunch of different medical types of projects.
[904.78 → 910.32] So one of them is using like very large 3D images and trying to figure out where tumours are.
[910.44 → 914.76] So basically revolutionizing the healthcare industry.
[915.66 → 922.00] And the issue with these data sets, though, is that they are, the images are so large.
[922.00 → 926.06] So it takes a large amount of memory to put them in your compute power.
[926.06 → 929.22] And there's something called tiling, which exists.
[929.34 → 932.72] So if you can't fit it all in memory, you can like chunk it up.
[932.86 → 938.48] But that doesn't do very well if you're doing a segmentation type of deep learning where you're trying to show an entire area.
[939.04 → 940.96] So you want to keep your image whole.
[941.30 → 949.04] And that really helps us then be able to make certain that our hardware is designed in a way that supports this data set.
[949.04 → 954.22] You know if we were always just looking at ImageNet, then it's like these tiny, tiny images.
[954.22 → 957.98] And that has an area, and it has a place.
[958.24 → 962.46] But, you know, we want to see the breadth of what is out there.
[963.08 → 964.46] And that's just one example.
[964.70 → 969.36] So like a lot of these other data sets are just also very large, very messy.
[969.78 → 972.40] So creating the tools to support those.
[973.20 → 976.16] So I'm wondering, you had just mentioned hardware support.
[976.16 → 979.70] And I know we're working through some of the different initiatives that you've done.
[979.70 → 983.66] And I'd like to both kind of if you could take us through some of the initiatives.
[983.66 → 990.46] And then I would like to afterwards kind of delve into what kind of hardware support you've needed, how that's affected Intel's business.
[990.60 → 993.62] And also, you know, which algorithms you all are tending to use.
[993.68 → 1000.26] But let's start at the beginning before I rush forward too far and just talk about some of the different projects that you all have that you've done at Intel.
[1000.52 → 1000.74] Sure.
[1001.00 → 1003.02] And there have been a lot.
[1003.02 → 1009.36] So I'm just going to highlight a few, and then we have a few more on our website, which will be in the show notes.
[1009.38 → 1010.54] Yeah, we'll have those in the show notes.
[1011.08 → 1017.66] So one of them, and this actually gets to the hardware support as well, is called Trail guard AI.
[1018.20 → 1025.78] And the premise behind this is that the poaching is a giant issue both in Africa and globally.
[1025.78 → 1042.94] Actually, there was an employee who reached out to try to figure out if we could help install this type of camera in, I think, Sedna, Arizona, where this wild horse herd like has been drastically impacted by people that are killing these wild horses.
[1043.10 → 1045.10] So it is an issue everywhere.
[1045.54 → 1049.42] But the park rangers that are monitoring these areas, there's not a lot of them.
[1049.42 → 1059.12] So one of the statistics that I've heard is that in, I believe, the Strength, there is an area about the size of Maryland and 150 park rangers.
[1059.76 → 1061.66] So it's a large area.
[1062.72 → 1065.76] And, you know, the poachers are, how do I say it?
[1065.76 → 1079.96] They basically have a very large financial incentive to poach these animals because the ivory that they are getting from it or the bushmeat or whatever they're trying to pull out is very financially invaluable to them.
[1080.44 → 1083.66] So basically what we did was worked with a company called Resolve.
[1083.88 → 1088.22] And they have these motion capture cameras that they've been trying out.
[1088.48 → 1090.88] And motion capture cameras are great.
[1090.88 → 1099.36] They are able to detect if there's any movement, take images, and then an early version of trail guard sent all these images to the park rangers.
[1099.70 → 1103.14] Now, the issue, though, with the system is that they're very noisy.
[1103.50 → 1107.36] So change in lighting, any like movement in the trees.
[1107.50 → 1111.68] Basically, if the bushes move, the motion capture camera goes off.
[1111.94 → 1113.24] You want them to be pretty sensitive.
[1113.80 → 1117.88] So these park rangers were getting tons and tons of images without anything in it.
[1117.88 → 1122.84] So we helped Resolve embed a Movies vision processing unit.
[1123.14 → 1126.16] This is a very small chip that's low power.
[1126.64 → 1130.18] It's specifically designed for inference on the edge.
[1130.32 → 1135.34] So you don't have to send any of these images to the cloud, which saves on battery power.
[1135.44 → 1140.22] And also there's not a lot of cloud connectivity in, you know, these wildlife reserves.
[1140.62 → 1142.40] You know, they're pretty remote.
[1142.40 → 1147.96] So basically what happens is an image is taken because the motion capture camera goes off.
[1148.16 → 1150.54] That image is sent to the Movies CPU.
[1151.42 → 1158.50] And there is a SSD type of neural network that goes off, which is a type of like convolutional neural network.
[1158.76 → 1161.88] And it detects if there is a person or a vehicle.
[1162.06 → 1165.72] And these are the things that, you know, the park rangers are the most interested in.
[1165.72 → 1169.34] So, yes, of course, we can like to extend this to animals as well.
[1169.56 → 1171.52] So just a basic object detection.
[1172.12 → 1184.02] And if there is a person or a vehicle detected, it'll place a bounding box around that object and send that image with the bounding box to the park rangers along with like a little text file that says like the probability.
[1184.54 → 1190.62] This drastically reduces on the false alarms, which has a few different advantages for the entire unit.
[1190.62 → 1192.86] One, it really saves on the battery life.
[1193.20 → 1200.44] So basically this unit can be out in the field for like a year, year and a half, as well as reduces the noise that the park rangers are getting.
[1201.06 → 1207.04] So hopefully they can like they can now like to intervene before the poachers get to the animals.
[1207.56 → 1210.88] And they can also see like what is the information being given.
[1211.04 → 1216.70] So they're being able to decide, oh, yes, this is a poacher, or it's a lot of poachers with a lot of guns.
[1216.90 → 1218.40] We need to respond differently.
[1218.48 → 1219.00] Or it's a farmer.
[1219.00 → 1222.68] You know, they're just getting their cows, things like that.
[1223.32 → 1228.82] So for any of our listeners who have listened to many of our podcasts, they may have heard me.
[1229.12 → 1230.44] That's something I'm very passionate about.
[1230.52 → 1232.74] I know you know that as well, animal advocacy.
[1233.26 → 1237.94] So I would like to say thank you very much for taking that particular issue on.
[1238.08 → 1241.34] I just absolutely love that you guys are doing work in that.
[1241.44 → 1243.20] So definitely touches my own heart.
[1243.42 → 1246.16] What are some of the other things that you all have engaged in?
[1246.16 → 1246.64] Yeah.
[1246.96 → 1253.30] So one of the other projects, this one's also a vision one, but it's using facial gesture recognition.
[1253.62 → 1258.76] So we worked with a company called Who Box on this vehicle called the Wheelie.
[1259.02 → 1263.56] And basically it's designed for somebody who's had a spinal cord injury,
[1263.80 → 1266.16] specifically potentially someone who is quadriplegic.
[1266.16 → 1272.48] And so they don't have the use of their arms to be able to control motorized wheelchair.
[1272.72 → 1277.40] This lets them use whichever facial gesture is most natural for them.
[1277.64 → 1281.24] So like smiling, open mouth, raised eyebrows, etc.
[1281.72 → 1288.34] To control the motorized wheelchair in any public spaces or at home, wherever they want to go.
[1288.34 → 1292.56] Basically allowing them to have more options and mobility.
[1292.82 → 1298.74] A lot of the devices that are out there aren't super, they can be, I guess, like expensive.
[1299.02 → 1300.32] They can be invasive.
[1300.60 → 1302.90] So one of the things is like this like little pipe thing.
[1303.32 → 1307.98] So just, you know, some options that are just not great for them.
[1307.98 → 1313.42] So we worked with them to use that basically using a bunch of different hardware choices.
[1313.66 → 1317.26] There's like this, the Intel has a real sense 3D camera.
[1317.48 → 1320.30] So that helps capture a lot of information about the face.
[1320.44 → 1326.80] And then all the processing is done on the Nook, which is a miniaturized PC with a customizable board.
[1326.80 → 1329.80] So you can be done all on the device.
[1329.92 → 1333.62] Again, you don't have to send it to the cloud because you want it to go really, really fast.
[1333.70 → 1335.96] Like if I want to stop, then I want to stop now.
[1336.60 → 1337.72] That sounds fantastic.
[1337.72 → 1347.30] So there are so many use cases I would, I could imagine that that can be applied to in terms of people that their mobility is entirely in a wheelchair for the most part in the larger world.
[1347.30 → 1349.84] So I would imagine that can be pushed out everywhere.
[1350.14 → 1363.76] So when you, you know, you've talked about two of them so far, when, when you are engaging in these kinds of initiatives, how does the larger organization beyond just your group that's, that's kind of bringing these, you know, to bear, how does that affect the large organization?
[1363.76 → 1374.34] Do, are these things where, are these things where both from a business opportunity, but also from a social goods standpoint, how do, how do you spread your, your ripples out through this large corporation?
[1374.34 → 1380.88] For sure. So there's, there are a bunch of different programs that have been helping these projects.
[1381.10 → 1385.30] And this, these are just a number of different business units as well.
[1385.30 → 1390.52] So there's something called the software innovator program and the AI Academy.
[1390.84 → 1395.16] That's where some of these, well, the Hotbox example came through that.
[1395.16 → 1400.56] And basically they help support, get access to hardware as well as software.
[1400.56 → 1407.42] And anybody can, you know, help in those projects, in those programs, any employee of Intel.
[1407.62 → 1413.60] And basically anybody who wants to be involved with it can go there, and I can send you those links too.
[1413.80 → 1415.40] But there are a few different things.
[1415.40 → 1425.10] So one of the things that we have done in the past and will continue doing is, I guess, oh gosh, forgetting the name of it right off the top of my head.
[1425.10 → 1437.62] But we have a program that employees can volunteer to work with, like do hackathons or in-depth types of teaching programs in local communities as well.
[1437.62 → 1452.06] So one of the cool things that we've done in the past is, especially at these hackathons, utilize some of the AI for good programs and use them as a way to teach students.
[1452.06 → 1462.30] So high schoolers, middle schoolers, college kids about, about AI, about computer programming and basically spreading the knowledge that way.
[1462.30 → 1469.60] One of the things that we do as a company that I love is that we try to open source as much as we can.
[1469.86 → 1471.86] So we have courses online.
[1472.26 → 1479.60] We have different like Python packages or other types of language packages that are out there to serve as examples.
[1480.18 → 1491.82] Whenever we are doing a project for either for research or with a customer, you know, whenever we can put it out there for somebody to take up, to utilize and use as their own as well.
[1491.82 → 1493.50] So that's one way of doing it.
[1493.74 → 1498.36] And then, yeah, just sort of, I guess one of the biggest thing is to continue to talk about it.
[1498.42 → 1505.34] We have these, you know, internal groups where we come and discuss different whatever, like interest and stuff.
[1505.44 → 1507.58] So there's like a deep learning community of practice.
[1507.90 → 1510.56] There is like an ethical AI group.
[1510.74 → 1516.40] There is an AI for social good group where we have like these online spaces and forums to chat.
[1516.40 → 1523.86] As you do this, and you've kind of talked about these different, you know, organizations within the larger organization, different capabilities.
[1524.34 → 1525.26] How do you engage them?
[1525.36 → 1532.42] So, I mean, I assume that you're thinking of them from, wow, that group over there has a capability we could really use in this social good project.
[1532.42 → 1535.74] So, as you typically bring them in, how do you do that?
[1535.94 → 1538.76] Does it tend to surprise them compared to their normal day jobs?
[1539.02 → 1543.52] Or, you know, I'm sure they're, I can't imagine they wouldn't be enthusiastic about being able to help.
[1543.58 → 1549.06] But I'm just curious how the politicking of those internal communications across department works in this case.
[1549.88 → 1551.34] No, that's a great question.
[1551.50 → 1554.22] And I think it's one that I'm still figuring out.
[1554.28 → 1557.84] It's been a lot of email for the most part or, you know, I am chat.
[1557.84 → 1569.82] But it's funny because when I introduce myself or when I am introduced to somebody, one of the responses that often happens is like, oh, we have, you exist, basically.
[1570.00 → 1572.46] It's like, you know, we have an AI for social good.
[1572.78 → 1582.72] And it's fascinating because, you know, we have projects that go back years that I would totally put under the umbrella of AI for social good.
[1582.72 → 1590.58] And the web page that we have that are like highlighting these programs, a lot of them have happened like even before I joined Intel.
[1590.94 → 1598.88] So just because we didn't have a name or a program or like a person that was like taking it under their wing.
[1599.72 → 1601.72] Yeah, it doesn't mean that we weren't doing it.
[1602.08 → 1603.38] So it's fantastic, though.
[1603.50 → 1608.08] So I totally get that, you know, that social good didn't start, you know, when you came to the company.
[1608.08 → 1617.88] But you essentially create a group where you have a flag to plant, and it gives you a firm place for the company to rally around for these kinds of things and to tie different components together, I assume.
[1618.26 → 1618.66] For sure.
[1618.82 → 1618.98] Yeah.
[1619.02 → 1633.64] And one of the nice things is that a lot of groups and individuals reach out and talk to me about like when we were talking about the wheelie on the International Day of Disability back in December.
[1633.64 → 1639.44] I got a bunch of different emails from our disability group, and they were like, hey, these are the things we're doing.
[1639.68 → 1642.36] And, you know, it's like we're super glad that you exist.
[1642.44 → 1643.48] We love this story.
[1643.64 → 1644.78] Can we use it on our slides?
[1644.82 → 1646.06] It's like, yes, please.
[1647.16 → 1647.88] Of course.
[1648.38 → 1650.58] And so then, you know, there's that communication.
[1651.24 → 1657.56] So it's really helped me see more of the projects that are happening at Intel, which are fascinating.
[1657.56 → 1678.30] So, like, there are things on education, there are things on accessibility, there are things on, you know, trying to make sure that we're using even like one of the projects that we did, I don't, a few years back is like making sure that we're using like conflict-free minerals in all of our silicon.
[1678.30 → 1683.24] So, you know, when we're making our chips, that's not having a harmful impact as well.
[1683.68 → 1692.58] So all of these different, you know, pieces and parts and the players who have been advocating for this, you know, I've gotten to know.
[1692.74 → 1696.90] And then when somebody asks, like, oh, yeah, like I want to do something on education.
[1697.26 → 1698.22] Who do I talk to?
[1698.26 → 1699.90] It's like, oh, you know, go talk to Ray Sana.
[1700.30 → 1701.56] It's like, she'll hook you up.
[1701.56 → 1711.78] Or, you know, like knowing the AI Academy people or the AI Builders group, and they help, you know, startups get access to AI technology.
[1712.14 → 1720.32] All of those different, like, pieces and parts connecting them to each other as well as to organizations that I think we can help.
[1720.32 → 1728.58] I love the fact that not only are you doing social good, but there's the benefit for the company because that's going to keep them motivated on doing these.
[1728.68 → 1738.96] When you talked about making sure that, you know, that the raw materials that go into the chips, you know, are from conflict-free areas and so that people are not being exploited and all that.
[1738.96 → 1750.92] And with the work that you've done, obviously, in the poaching and with accessibility, with wheelchairs and such, do you have any other kind of areas that you're either engaged in now or would like to get engaged in?
[1750.98 → 1752.26] I mean, what's your aspiration there?
[1752.26 → 1767.24] One of the things that has really interested me about this program and seeing what the problems are and what we can do is that we can really just reutilize a lot of the technology that we already have.
[1767.24 → 1780.86] So we can use the compute types of power, we can use the frameworks, be them like computer vision, NLP, et cetera, and really, you know, just rejigged them, massage it into these new use cases.
[1780.94 → 1796.32] So like the segmentation example that we were talking about earlier for cancer detection, that same technology is used to show like where in an image is a dog or where in an image is a person if you're doing like some sort of self-driving car types of things.
[1796.32 → 1803.18] So the same technology, but just utilized in a different and, in my opinion, more meaningful way, I guess.
[1804.24 → 1805.28] That's a great example.
[1805.36 → 1816.40] One of the things I was just thinking about is that some of the examples we've talked about so far in the conversation have been very much around computer vision, you know, where you're going to apply different CNN architectures to solve it.
[1816.40 → 1830.94] I'm just curious, and the answer maybe no, I don't know what's going, but outside the computer vision, have you found there are any other deep learning algorithms in particular or even outside deep learning that have been particularly useful or that you expect that you may be seeing based on some of the conversations coming?
[1830.94 → 1831.98] No, for sure.
[1832.22 → 1838.66] One of the projects that Intel did a few years back was called Hack Harassment.
[1838.86 → 1850.36] So basically what they were doing was working with Vox and the Lady Gaga Foundation to identify harassing speech online and be able to work in these communities to mitigate it.
[1850.36 → 1859.80] So we were using LSTMs and other NLP architectures to try to detect these types of comments that were occurring.
[1860.04 → 1863.14] And it's interesting, like, using that in there.
[1863.22 → 1873.44] And we've actually, like, are working with some grad students now to continue that types of projects and, you know, bring the state of the art forward in that area.
[1873.44 → 1879.60] There are other things that you could do that we've done with the National Centre for Missing Exploited Children.
[1880.04 → 1886.30] So basically NEC MEC, they get a bunch of different pings from anyone that has data online.
[1886.30 → 1895.68] And if there's ever any content that looks like a child might be in danger from an online or a real-life predator, they get this.
[1896.16 → 1898.90] And it takes them a large amount of time to go through it.
[1898.90 → 1903.54] So basically it takes 30 days to, like, respond to every single types of things.
[1903.54 → 1906.58] And they basically need to figure out, like, where is this located?
[1907.14 → 1909.54] Is it actually hazardous?
[1909.80 → 1911.66] Because they get some false information too.
[1912.00 → 1914.94] And, you know, like, what is the response that's necessary?
[1915.10 → 1915.90] What's going on?
[1916.04 → 1921.94] So we worked on a couple of different algorithms, some of which are NLP, some of which are just machine learning,
[1921.94 → 1928.42] to determine, like, if there are multiple different types of IP addresses, like, which one is the one where it's located?
[1928.58 → 1932.02] Basically, who are the different authorities that need to be brought into this case?
[1932.22 → 1938.90] As well as do a prioritization of saying, yeah, these are definitely ones that we have to look into rapidly.
[1939.24 → 1943.24] And, you know, with missing kids especially, like, the sooner that you respond, the better.
[1943.68 → 1949.16] Or, you know, this is, you know, a case that is important but might not need the same response.
[1949.60 → 1950.78] So working with them on that.
[1951.24 → 1952.46] No, that's amazing.
[1952.66 → 1955.32] So you have so many amazing examples that you're working on.
[1955.68 → 1962.80] So, you know, and that's, I think, you know, aside from the animal advocacy, I love children's issues.
[1962.80 → 1966.16] And elderly issues as well are things that I personally care a lot about.
[1966.62 → 1974.18] So, you know, if somehow I'm ever on the market for another job, I may come knocking on the door at Intel and beg you to take me onto your team here.
[1974.48 → 1975.10] Very cool.
[1975.10 → 1979.68] So with this success, you know, you talked about that you only came into this in April.
[1980.06 → 1988.44] And you've had tremendous success in doing this in a very short amount of time, which leads me, I have to pick your brain a little bit.
[1988.66 → 1998.04] There are going to be other people out there in other organizations that really want to do something similar in their own organization, be it a small or a large one.
[1998.04 → 2007.68] As you have come through and maybe have some battle scars on setting this up and having to figure it all out, what kind of recommendations do you have to help people do something similar?
[2008.08 → 2008.66] For sure.
[2008.80 → 2019.98] And one thing that I definitely want to mention is that, you know, the projects that I've talked about are all ones that I didn't bring in or that I didn't like work directly on.
[2019.98 → 2025.94] And, you know, I am this is work of many, many people over many years.
[2026.42 → 2031.98] So and I think that's important to make sure that the credit goes where it's due.
[2032.48 → 2037.56] What I would suggest, though, is if you're wanting to do this type of role is like kudos.
[2037.56 → 2038.74] I think it's great.
[2039.22 → 2053.14] One of the things that, you know, I did before this is to, you know, volunteer for one of these types of will for to volunteer with Delta Analytics, which is an organization that is located in the San Francisco Bay Area.
[2053.24 → 2056.44] But there are ones that are more nationally and globally.
[2056.76 → 2058.12] So data kind is one.
[2058.24 → 2059.36] There are many others.
[2059.36 → 2064.56] And that really helps you start to see what are the issues that are out there?
[2065.00 → 2066.46] What are the ways that I can help?
[2066.46 → 2075.34] It does help to have sort of a data science, software engineering background so that you understand the tech, you understand the AI lingo.
[2075.76 → 2085.30] And then, you know, get ready to network because a lot of it is figuring out, like, who has the issues, who has the solutions, and how do we get each other to work together?
[2085.88 → 2087.28] So it's a lot of networking.
[2087.96 → 2089.20] But it's interesting.
[2089.20 → 2098.52] So, you know, I definitely suggest going to some of the AI for Good workshops or symposiums that are starting up.
[2098.66 → 2105.54] A lot of them are occurring at this traditional ML, AI, different types of conferences.
[2105.96 → 2111.54] So, I mean, here at AMID, we have there are a couple of different sessions and as well as on the big stage.
[2111.54 → 2115.90] So it's becoming more of a topic that is spoken about.
[2116.22 → 2117.14] And they're great.
[2117.24 → 2120.42] Like, if you're a grad student, check out DSSG.
[2120.60 → 2123.98] Check out some of these other labs that are at universities.
[2124.72 → 2125.34] And yeah.
[2125.34 → 2136.32] One thing that I neglected to do at the beginning of the conversation, while I know listeners know that we're at Applied Machine Learning Days in Switzerland, I neglected to say that you were one of the speakers.
[2136.54 → 2137.44] And I was, too.
[2137.52 → 2148.06] And we were on the AI for Good track, which our good friend Daniel Whiten ack, my co-host, he ironically was not able to be here at the last minute due to a family situation.
[2148.06 → 2153.64] But he actually organized the track and a lot of us on the AI for Good kind of banded together and stuff.
[2153.92 → 2162.38] So I wanted to say thank you very much for everything you're doing and for being here and taking the time to not only do the work, but to share it with us.
[2162.86 → 2168.18] And I guess for listeners who might want to reach out, get in touch with you, how was best to do that?
[2168.54 → 2171.96] So I'm definitely on Twitter and I check that a lot.
[2171.96 → 2182.18] So I'm data underscore Beth on Twitter and there will be a link to the website, which is just intel.ai slash AI for Social Good.
[2182.26 → 2185.74] And the four is a number because I am a nerd and I love that.
[2186.04 → 2187.98] And we will definitely include that in the show notes.
[2188.40 → 2193.20] So those are great ways to reach out and get more information about what I'm doing.
[2193.34 → 2199.28] I would definitely not suggest emailing me because my inbox is a little backlogged at the moment.
[2199.28 → 2201.76] So we'll go the Twitter route for now.
[2202.20 → 2202.74] Sounds good.
[2202.82 → 2206.60] Well, Anna, thank you so much for coming on the show, sharing all this with you.
[2206.72 → 2209.46] I'm quite sure there's some people out there that are inspired to do the same.
[2209.58 → 2210.80] And thanks for giving some advice.
[2211.34 → 2212.74] And thanks so much.
[2212.78 → 2215.98] I'll see you at the next AI for Good conference somewhere in the world.
[2216.18 → 2216.54] Pretty sure.
[2216.64 → 2217.78] No, I look forward to it.
[2220.34 → 2220.84] All right.
[2220.88 → 2223.50] Thank you for tuning into this episode of Practical AI.
[2223.76 → 2225.24] If you enjoyed the show, do us a favour.
[2225.34 → 2226.74] Go on iTunes, give us a rating.
[2226.74 → 2228.88] Go in your podcast app and favourite it.
[2229.00 → 2231.70] If you are on Twitter or social network, share a link with a friend.
[2231.70 → 2234.14] And whatever you got to do, share the show with a friend if you enjoyed it.
[2234.44 → 2237.10] And bandwidth for Changelog is provided by Vastly.
[2237.22 → 2238.66] Learn more at Fastly.com.
[2238.88 → 2242.06] And we catch our errors before our users do here at Changelog because of Rollbar.
[2242.32 → 2244.66] Check them out at Rollbar.com slash Changelog.
[2244.98 → 2247.46] And we're hosted on Linde cloud servers.
[2247.80 → 2249.44] Head to Linode.com slash Changelog.
[2249.54 → 2249.98] Check them out.
[2250.06 → 2250.88] Support this show.
[2251.26 → 2254.50] This episode is hosted by Daniel Whiten ack and Chris Benson.
[2254.50 → 2257.06] The music is by Break master Cylinder.
[2257.46 → 2260.84] And you can find more shows just like this at ChangeLog.com.
[2261.02 → 2262.98] When you go there, pop in your email address.
[2263.24 → 2267.10] Get our weekly email keeping you up to date with the news and podcasts for developers
[2267.10 → 2269.28] in your inbox every single week.
[2269.70 → 2270.46] Thanks for tuning in.
[2270.60 → 2271.38] We'll see you next week.
