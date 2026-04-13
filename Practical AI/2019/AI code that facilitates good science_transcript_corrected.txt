[0.00 → 2.58] Bandwidth for Changelog is provided by Vastly.
[2.96 → 4.84] Learn more at Fastly.com.
[5.08 → 8.16] We move fast and fix things here at Changelog because of Rollbar.
[8.30 → 9.98] Check them out at Rollbar.com.
[10.22 → 12.40] And we're hosted on Linde cloud servers.
[12.76 → 14.74] Head to linode.com slash Changelog.
[15.72 → 20.34] This episode is brought to you by DigitalOcean, the simplest cloud platform out there.
[20.46 → 25.10] And we're excited to share they now offer dedicated virtual droplets.
[25.10 → 29.02] And unlike standard droplets, which use shared virtual CPU threads,
[29.02 → 32.86] their two performance plans, general purpose and CPU optimized,
[33.40 → 36.08] they have dedicated virtual CPU threads.
[36.40 → 40.86] This translates to higher performance and increased consistency during CPU intensive processes.
[41.36 → 45.20] So if you have build boxes, CCD, video encoding, machine learning, ad serving,
[45.50 → 49.98] game servers, databases, batch processing, data mining, application servers,
[50.20 → 54.92] or active front end web servers that need to be full duty CPU all day every day,
[55.14 → 57.92] then check out DigitalOcean's dedicated virtual CPU droplets.
[57.92 → 61.26] Pricing is very competitive starting at 40 bucks a month.
[61.66 → 66.38] Learn more and get started for free with a $100 credit at do.co slash Changelog.
[66.64 → 69.02] Again, do.co slash Changelog.
[69.02 → 86.38] Welcome to Practical AI, a weekly podcast about making artificial intelligence practical,
[86.78 → 88.56] productive, and accessible to everyone.
[88.94 → 93.44] This is where conversations around AI, machine learning, and data science happen.
[93.92 → 98.20] Join the community and Slack with us around various topics of the show at changelog.com slash community.
[98.20 → 99.38] Follow us on Twitter.
[99.48 → 100.96] We're at Practical AI FM.
[101.46 → 102.28] And now onto the show.
[106.54 → 110.50] Welcome to another episode of Practical AI.
[111.18 → 112.88] I'm Daniel Whiten ack.
[112.96 → 115.54] I'm a data scientist, and I'm joined by Chris Benson,
[115.54 → 120.56] who is a chief strategist for AI and high performance computing at Lockheed Martin.
[120.80 → 121.60] Hey, Chris, how are you doing?
[121.96 → 122.62] I'm doing good.
[122.66 → 123.30] How are you today?
[123.58 → 124.48] Doing pretty good.
[124.48 → 129.88] Made it through the 4th of July without blowing myself up or anything like that.
[129.92 → 130.64] Always a good thing.
[130.76 → 131.70] How about you?
[131.76 → 132.48] Did you have a good holiday?
[132.74 → 133.18] I did.
[133.42 → 134.94] I had just family stuff.
[135.06 → 136.32] I got kissed by a llama.
[136.82 → 137.54] I'll have you know.
[137.54 → 137.84] Oh, wow.
[137.92 → 138.72] I went to a friend's house.
[138.82 → 142.24] They had llamas and the llama came up and planted one right on my face.
[142.30 → 143.70] So that was an interesting experience.
[143.84 → 145.68] I was not sure what to do about that.
[145.76 → 147.74] I declined to take it further with the llama.
[147.88 → 150.66] I decided that that was not the relationship I wanted to pursue.
[150.66 → 153.50] But that was the highlight of my 4th, sadly.
[153.78 → 155.06] Probably a good thing.
[155.38 → 156.22] But yeah.
[156.68 → 161.34] Well, on that note, maybe a more relevant note.
[161.82 → 172.64] Given that this is practical AI in our community on Slack, which you can find by going to changelog.com
[172.64 → 179.56] But oftentimes we're asked maybe what are good practical ways to start learning about AI.
[180.36 → 186.24] Maybe from software engineers or those with an engineering background who are getting into AI and data science.
[186.90 → 194.80] And pretty much I always tell them that a great place to start is with Joel Ruse's book, Data Science from Scratch.
[194.80 → 200.86] That was one of the kind of instrumental things in helping me understand what data science is.
[201.00 → 203.44] And I frequently go back and reference that book.
[203.98 → 206.20] Well, Joel has joined us today.
[206.38 → 210.74] I'm really excited to talk to him about his book, which now has a second edition.
[211.02 → 216.86] And also some things he's doing at the Allen Institute for AI in Seattle.
[217.04 → 217.80] So welcome, Joel.
[218.18 → 219.14] Thanks for having me here.
[219.48 → 219.74] Yeah.
[219.74 → 225.62] Maybe you could start by just giving us a little bit of background about yourself.
[226.64 → 233.64] You know, how you got into data science, how you got to Allen AI, and what you're working on now.
[233.96 → 234.24] Right.
[234.38 → 236.94] So originally I studied math and economics.
[237.22 → 238.16] This was a long time ago.
[238.36 → 240.20] Well before data science was a thing.
[240.88 → 245.90] And so what I did, what a lot of people with math backgrounds do, is that I went into quantitative finance.
[245.90 → 249.10] Options, pricing, financial risk, things like that.
[249.10 → 251.16] And I discovered I didn't like it very much.
[252.10 → 255.68] And so I was working at a hedge fund, and it went out of business and I got laid off.
[255.98 → 267.36] And I was lucky enough, and this was 2006, to get hooked up with a startup called Fair cast, which was an online travel site doing basically price predictions on airfare.
[267.44 → 271.66] So they'd use machine learning, and you'd say, I want to fly from Seattle to Los Angeles on these dates.
[271.66 → 277.98] It would tell you, you know, the best price is $300 on Alaska, and we predict the price is going up, so you should buy now.
[278.08 → 280.56] Or we predict the price is going down, so you should wait.
[280.76 → 285.54] So they were doing a lot of machine learning before putting machine learning in consumer products was particularly popular.
[286.18 → 287.62] I was not doing machine learning.
[287.62 → 291.70] I was doing BI, writing SQL queries, building spreadsheets, things like that.
[292.12 → 299.58] But as time went on, I started getting a little bit into the machine learning side of things, a little bit into the Python scripting side of things.
[299.58 → 308.34] And just started to grow my skills in that area and learn by osmosis from some of the data miners, as we called them.
[308.66 → 317.60] And so by the time it was, you know, 2011 or so, and data science was just starting to become a thing, I said, you know, that's like what I've been doing, but kind of better.
[317.78 → 318.90] And now there's a name for it.
[318.90 → 329.72] So I want to become a data scientist, and I sort of pushed myself in that direction, managed to talk my way into a data science job, and spent three years basically running data science at a startup called Volumetric.
[330.14 → 338.86] While I was at Volumetric, I ended up writing a fair amount of production code, for better or for worse, because that was a startup doing analytics on enterprise collaboration data.
[339.40 → 342.22] And so the data science kind of was the product.
[342.58 → 345.40] And so that meant that the data scientists ended up writing a lot of production code.
[346.02 → 347.26] And I found that I really liked it.
[347.26 → 348.30] I liked building things.
[348.52 → 349.66] That was a lot of fun for me.
[350.46 → 354.74] And so I wanted to look for opportunities to really grow out that skill set.
[354.84 → 356.54] And I had the opportunity to interview at Google.
[357.06 → 364.00] So I sort of crammed for a while, teaching myself all the computer science that I should have learned but never did, because I didn't study computer science.
[364.42 → 372.18] Somehow passed the interview, went to Google for a couple of years, and really kind of levelled up in terms of software engineering, you know, writing code, building things.
[372.18 → 386.26] But after a couple of years there, I sort of felt like I wasn't excited about the projects I was working on, you know, building tools to help ad salespeople sell more ads, or writing back-end services in C++ to replace spreadsheets, things like that.
[386.26 → 397.30] And so, you know, I had the opportunity to interview at AI2, which is a research nonprofit doing fundamental AI research.
[397.80 → 400.26] And I decided to move over here.
[400.58 → 402.18] I've worked on a couple different projects here.
[402.18 → 407.46] The first one was called Ariosto, which is basically teaching computers to pass science exams.
[408.08 → 417.40] And now I work on a team called Allen NLP, which does fundamental NLP research, as well as we build a library called Allen NLP, which is a deep learning library for doing NLP research.
[417.56 → 429.30] And so most of my job is working on building that library, supporting people using that library, adding features, adding models, fixing bugs, giving tutorials, giving talks, and so on and so forth.
[429.30 → 436.54] Yeah, it's interesting that you mentioned kind of having to level up your computer science skills.
[436.68 → 450.82] I remember kind of like getting into data science from a physics background, and I feel kind of similar to you in that like it was around the same time a little bit later, but data science was still kind of the hype was growing.
[450.82 → 461.48] And I felt like similar that I kind of talked myself into a position and then learned a bunch of these coding things later and like learned how to do a bunch of things like on the fly.
[461.62 → 469.90] I'm not sure now, like if I was in the same place, things are so competitive now in like data science and like it was really hard interviews and all of these things.
[469.90 → 477.36] I'm not really sure if I'm not really sure if I would have like made it in given where I was back in the day.
[477.56 → 480.90] So it's interesting that you had a similar experience.
[481.42 → 494.46] Yeah, so basically my interview to be basically the data scientist of Volumetric was me meeting with the CEO, him handing me a printed out SQL query and asking, do you understand this?
[494.46 → 496.88] And I said yes, and then he hired me.
[497.42 → 506.36] But so he hired me basically in like a contract to hire position because it was so early in the company that they weren't set up to have full-time employees yet.
[506.76 → 511.88] So in that sense, he wasn't taking a ton of risk because he could have easily not converted me to full-time employee.
[512.04 → 515.00] But still, it was not a very rigorous process.
[515.64 → 517.46] You don't happen to remember that SQL query, do you?
[517.84 → 520.54] It was about five pages long.
[520.92 → 521.52] Oh, boy.
[521.68 → 523.18] Okay, serious SQL right there.
[523.18 → 535.72] So I guess to turn toward the book, I guess I'd like to start off by just asking you, why do you think it's important to think about data science from scratch since you used from scratch in the title of the book?
[536.02 → 540.90] And why is that approach useful to get people into data science and AI?
[541.22 → 542.62] What's your take on it?
[542.62 → 561.58] So the practical answer is that, you know, it's very easy to install scikit-learn points, you know, random forest classification at some data set and spit out a result and sort of have no idea what's going on, which, you know, is good in some ways.
[561.58 → 567.32] And it's also bad in some ways that if it goes wrong, it's very hard for you to figure out why it's gone wrong.
[567.54 → 573.94] Or it's possible you've made some conceptual mistake, or you're cheating by looking at the testator, things like that.
[573.94 → 579.46] And so if you don't know those things, it's very easy to lead yourself astray.
[580.00 → 581.38] So that's kind of the practical answer.
[581.76 → 585.32] The moral answer is that, as I mentioned, my background is mathematics.
[585.32 → 595.06] And one thing that's a very strong, almost moral principle in mathematics is that you're not allowed to use theorems if you haven't proved them yet.
[595.32 → 602.84] So, you know, math classes are set up so that the first quarter will prove these theorems and then the second quarter will build on them and third quarter will build on them.
[602.84 → 610.90] So much so that, you know, when I was in grad school, I had a year-long class, but the professor changed between the first semester and the second semester.
[610.90 → 617.64] And the second semester, he came in on the first day, and he says, I'm so glad you proved, like, theorem X because I need to use it.
[617.86 → 623.70] And with the premise being that, like, if we hadn't gone through that proof, he couldn't use it, and then we'd be, like, in a bad spot.
[624.06 → 634.34] And so somehow that, like, burned really deeply into me, this idea that you shouldn't use things like that if you don't really understand how they work.
[634.34 → 648.04] And so, you know, when I want to sit down and say, what is linear regression, you know, what is a random forest, what is a neural network, I feel like I need to really understand under the covers what's going on here, what is it doing behind the scenes.
[648.40 → 651.56] Otherwise, I don't feel comfortable using those things.
[651.94 → 658.52] And so that's kind of the maybe moral, you'd call it, reason for doing it that way.
[658.62 → 659.96] I feel like it's a good approach.
[659.96 → 664.96] Yeah, so, I mean, I definitely get what you're saying.
[665.12 → 674.44] I remember someone telling me when I was in physics, like, one of the ways that you can tell, like, the difference between, like, a math physics person and, like, a physics person.
[674.56 → 682.34] So there's this, like, group of physics people called math physics people is that, like, physics people are okay with just, like, trying something.
[682.44 → 683.98] And if it works, they're happy.
[683.98 → 689.92] Whereas, like, math physics people, they would never, like, use something unless they had proved it first.
[689.92 → 693.52] So, like, I definitely get that.
[693.62 → 708.58] But also, I love how in this book in particular, like, I've looked at some kind of statistical learning, machine learning, AI sorts of books that kind of start from the beginning and explain everything.
[708.58 → 714.72] And it is kind of all very, it's very math, right, which is good.
[714.82 → 717.54] And it's good to learn those things as well.
[717.68 → 720.96] But then it's, like, somehow disconnected from the coding side of things.
[721.10 → 726.96] And I think one of the reasons why I latched on to a lot of your content was, like, the code is right there.
[726.96 → 730.28] And you can go ahead and see, oh, yeah, like, there's, like, this abstract thing.
[730.40 → 733.88] But this is how it's directly connected to, like, Python code.
[734.02 → 741.28] And, like, I can see that it's, you know, it's not that hard to implement this thing in a few lines of code.
[741.28 → 742.90] And it kind of makes sense.
[743.14 → 749.08] Was that kind of something you saw as a gap and part of the reason why you wrote this book?
[749.12 → 752.92] Or why was it important for you to kind of take this code-first approach?
[753.74 → 755.88] So here's what I'll say.
[755.88 → 762.92] I think that when you put a lot of math equations in a technical book like that, people will zone out and not follow it.
[763.40 → 764.60] And for good reasons.
[764.60 → 768.06] You don't want to be reading a ton of math equations in a tech book.
[768.06 → 778.62] But the other thing is that a lot of times those equations are actually not the best way to explain something if you're using it in kind of applied context, right?
[778.86 → 784.56] So, you know, basically what I tried to do was, okay, here's a mathematical concept I want to teach.
[784.56 → 791.52] But instead of teaching it by giving you, you know, some latex up equations, I want to teach it by writing code that embodies it.
[791.86 → 795.22] And so that way, hopefully you understand the math that's going on.
[795.22 → 799.98] But also you can see from a Python point of view exactly what's happening.
[800.78 → 809.20] And so it's sort of this middle ground where I want the math to be part of, you know, the text and part of the pedagogy.
[809.36 → 815.32] But I also want the math to be framed in terms of Python code, not in terms of equations.
[815.32 → 821.96] So I guess in the book, when you're building from scratch, what do you kind of start with?
[822.20 → 831.26] And what is that order upon which you're building layer after layer so that the reader is kind of rocking it all in their head?
[831.60 → 832.50] How do you approach that?
[832.72 → 836.32] You know, it took me a long time to figure out a good order for doing this.
[836.32 → 843.06] But in essence, the structure is, you know, a brief introduction to Python.
[844.36 → 846.24] And then now we've got Python.
[846.40 → 849.72] Let's talk about linear algebra, which is mostly just working with vectors.
[849.94 → 855.50] And like I went serious from scratch where we're going to represent vectors as lists of floats.
[855.72 → 858.10] And we're going to do arithmetic on list of floats.
[858.48 → 862.72] So starting from pure Python and just what is a list, now we've got linear algebra.
[862.96 → 863.76] You know, I can take vectors.
[863.92 → 864.56] I can multiply them.
[864.60 → 865.56] I can do their dot product.
[865.56 → 870.40] And now that I'm equipped to do those things, I can say, let's start talking about doing statistics.
[870.70 → 872.12] So, you know, take the mean of these vectors.
[872.28 → 873.62] And I can start talking about probability.
[873.76 → 875.86] What does it mean to have a distribution over things?
[875.88 → 881.42] And I can start talking about hypothesis testing and drawing inferences and just building step by step.
[881.50 → 885.82] And now once I've spoken about all these things, there's a slight detour.
[885.90 → 888.10] And let's talk about how do I get data?
[888.20 → 889.34] How do I work with data?
[889.86 → 891.00] How do I clean data?
[891.04 → 891.96] How do I process data?
[891.96 → 897.26] And because of the machinery we've built, we can talk about things like, okay, now I want to do principal component analysis.
[897.38 → 898.02] What does that mean?
[898.02 → 910.80] And now once I've done sort of linear algebra and statistics and, you know, probability fundamentals, and once I've done working with data fundamentals, now I can start to push into machine learning.
[910.94 → 911.90] What is machine learning?
[912.18 → 915.38] Like, what do I need to understand about machine learning independent of what model I'm using?
[915.38 → 919.74] And then just start building up, okay, what is, you know, simple linear regression?
[919.90 → 920.88] What is multiple regression?
[921.06 → 922.16] What is logistic regression?
[922.56 → 923.60] What is a decision tree?
[923.74 → 924.66] What are neural networks?
[924.76 → 928.40] And then once you build up all those things, then you can start talking about even further applications.
[928.68 → 931.74] What, you know, what does it mean to do natural language processing?
[931.94 → 933.98] What does it mean to do kind of recommender systems?
[934.08 → 934.78] Things like that.
[934.78 → 939.56] And so that's kind of the not kind of, that is pretty much the progression of the book.
[940.36 → 949.44] And why, so why the second edition, I guess, you know, were there things that you felt like, you know, were left out?
[949.54 → 956.88] I know that there's, of course, now we're kind of in, we're, I don't know if we're past the data science hype, but we're definitely into the AI hype, right?
[956.88 → 962.52] And I think, I think if I'm not mistaken, you have a little bit more content about neural networks and that sort of thing.
[962.82 → 965.66] Was that part of the reason for, for the second edition?
[966.16 → 969.02] There was one overriding reason for the second edition.
[969.18 → 972.88] And that's that the first edition was written in Python 2.7.
[973.40 → 975.94] And basically told people to use Python 2.7.
[976.08 → 982.32] And every day I woke up and felt guilty as hell that there was a book out there with my name on it, telling people to use Python 2.7.
[982.32 → 987.82] And, and, and so I said, I'm going to do a second edition that's Python 3.
[988.04 → 991.76] And then once I was like, so, so that was like 99% of the reason I did it.
[992.22 → 996.88] And then once I was doing that, I thought, okay, well now maybe I'll add, you know, a chapter on deep learning.
[996.88 → 999.30] Cause that's a pretty important thing to know.
[999.30 → 1006.42] And let me flesh out some of the other chapters and add some new stuff, and I'll take the time to clean up the code and, and so on and so forth.
[1006.42 → 1010.80] But really the Python 2, Python 3 thing was, was 99% of my motivation.
[1010.80 → 1012.86] I like, I like your answer, by the way.
[1012.90 → 1013.62] I like the mea culpa.
[1013.86 → 1014.54] It's, that's funny.
[1015.02 → 1023.70] I don't even want to call it a mea culpa because I think at the time the first edition came out, probably Python 2.7 was the right choice.
[1023.86 → 1032.84] I, what I should have done is I should have written the code in the first edition in a way that was compatible with either Python 2 or Python 3, which wouldn't have been a ton of work, but I didn't do it.
[1033.18 → 1035.18] And so that was, that was a bad call on my part.
[1035.18 → 1044.60] But the reality is, is that even if I had written, you know, a Python 3 version, it would have been like Python 3.4, maybe like at the time I wrote that book or 3.3.
[1044.88 → 1048.22] And that's not like a great long-term version to be on anyway.
[1048.22 → 1048.62] So.
[1048.62 → 1064.60] The Data Engineering Podcast is a weekly deep dive on modern data management with the engineers and entrepreneurs who are shaping the industry.
[1064.88 → 1073.18] Go behind the scenes on the tools, techniques, and difficulties of data engineering so you can learn and keep up with the knowledge to make you and your business successful.
[1073.18 → 1081.06] Can you give a bit of an outline about the motivation for choosing Jupyter Notebooks in particular as the core interface for your data teams?
[1081.44 → 1081.62] Yeah.
[1081.76 → 1087.52] And actually, when I first joined Netflix, it was sort of tossed at me, and I was definitely like, well, are we crazy?
[1087.74 → 1089.42] And the answer was like, we might be a little crazy.
[1089.92 → 1096.24] Go to dataengineeringpodcast.com to listen, subscribe, and share it with your friends and colleagues.
[1103.18 → 1116.78] So, Joel, we've talked a little bit about data science from scratch and what you put into the book and like the code first approach.
[1116.78 → 1127.16] I've also noticed like with some of the other content that you've put out like both in the book but also in like, you know, talks that have gotten like a good bit of attention.
[1127.16 → 1132.96] Like I don't like notebooks and I saw another one writing code for NLP research.
[1133.16 → 1142.82] It seems like you put a lot of focus on sort of bringing good software engineering practices into like data science and AI.
[1142.82 → 1148.84] Is there a particular reason why that's kind of become a passion of yours and like a driving force?
[1149.42 → 1149.62] Yes.
[1149.74 → 1150.02] One.
[1150.72 → 1151.18] Yes.
[1151.26 → 1155.00] That is kind of like my big pet cause.
[1155.54 → 1164.48] So, the selfish reason is that I've become sort of over my best judgment sort of software design geek.
[1164.68 → 1171.52] And what I mean is I spend a lot of time thinking about what is the difference between good code and bad code even if both work.
[1171.52 → 1182.04] And in particular, you know, as someone who uses code to teach, I spend a lot of time thinking about what is the clearest way I can express the idea I'm trying to express in code.
[1182.42 → 1191.30] And what I found is that going through that exercise over and over again has really drilled into the importance of doing that and has spilled over into, you know, my actual work.
[1191.30 → 1199.32] So, even when I'm not teaching data science, but I'm writing code for my job, I'm still always thinking what is the clearest way I can express what I'm trying to do.
[1199.54 → 1203.28] Because, you know, in a month I'm going to come back and look at it or someone else is going to come back and look at it.
[1203.80 → 1206.72] And, you know, if it's not clear, they want people to understand it.
[1206.78 → 1208.22] So, that's kind of the selfish reason.
[1208.36 → 1212.02] The practical reason is there's a lot of bad data science code out there.
[1212.02 → 1215.82] And I think some data scientists even sort of take pride in, you know, I'm a data scientist.
[1215.96 → 1216.92] I write data science code.
[1217.30 → 1220.46] And I think that's unfortunate because for a couple of reasons.
[1220.72 → 1226.26] One, I think that by not understanding software engineering best practices or how to write good code,
[1226.26 → 1234.92] you're basically putting yourself in a position where you cannot contribute to, or you should not be contributing to production code, say, at your job.
[1235.06 → 1239.06] And you get this artificial division where I'm the data scientist, I'll write a model,
[1239.26 → 1245.06] and then I'll hand it off to someone who's not a data scientist to, you know, put it in production or make it work in code.
[1245.28 → 1247.38] And I think that's unfortunate for a couple of reasons.
[1247.38 → 1253.08] One, I think data scientists can have a lot more impact if they can cross, you know, that divide.
[1253.08 → 1260.44] And I think they also become better data scientists if they can cross that divide because the ideas from good software engineering kind of flow back.
[1260.94 → 1266.02] You know, a second reason why, or maybe third, another reason why it's really important, I think,
[1266.30 → 1274.38] is that a lot of the things that are software engineering best practices are intended to help you, one, write correct code,
[1274.70 → 1276.36] and two, get better at writing code.
[1276.68 → 1279.86] And those are both things that are equally important for data scientists.
[1279.86 → 1284.32] If you're a data scientist, even if you're writing code, you know, to run some experiment or something,
[1284.56 → 1285.76] you want that code to be correct.
[1286.02 → 1290.54] And you should be writing unit tests for that code because unit tests help make sure your code is correct.
[1290.84 → 1294.66] And you should be getting code reviews on that code because code reviews are a second set of eyes,
[1294.70 → 1298.04] and they'll find bugs, and they'll point out things that may, maybe they're not wrong,
[1298.08 → 1302.80] but you could have done better or, hey, did you know that scikit-learn has this thing that would have done that for you?
[1302.80 → 1308.14] And so all of these best practices will make you a better data scientist.
[1308.28 → 1309.04] You know, it's funny.
[1309.34 → 1310.22] I'm sorry, keep going.
[1310.50 → 1311.78] No, no, that's it.
[1311.96 → 1319.22] I was just going to say I actually sympathize tremendously with that take on it because I came into this from a software development,
[1319.32 → 1321.12] software engineering background.
[1321.12 → 1327.56] And as I moved fully into the AI space and started working with data scientists, in a lot of cases,
[1327.98 → 1333.20] straight out of school and into the job, and they kind of, they were weak on the programming side,
[1333.60 → 1338.16] that was definitely created a tension that I noticed, you know,
[1338.20 → 1342.96] where you had people that had different skill sets kind of working and bringing different things to bear.
[1343.28 → 1345.08] That certainly was the case for us.
[1345.08 → 1348.82] I know that, like, as we were thinking about the product of what we were doing,
[1348.92 → 1355.82] having to be productized and getting into, you know, the data science pipelines that had been created at the company I was at the time,
[1356.84 → 1361.54] with that tension, have you experienced that where, you know, people are like, well, I'm a data scientist.
[1361.70 → 1362.96] I just don't care.
[1363.16 → 1364.78] It sounds sort of like you may have.
[1365.66 → 1370.82] What kind of, how did you get through those dynamics in terms of dealing with those different perspectives together?
[1370.82 → 1375.30] I think you really have to do a sales job, right?
[1375.40 → 1378.22] And so that's one thing I've been trying to do with some of my talks,
[1378.70 → 1382.12] and also in the second edition of my book, to some degree, is to say, look,
[1382.36 → 1384.00] writing a unit test sounds like a hassle.
[1384.20 → 1390.14] Doing code review sounds like a hassle, but I'm going to show you how your life will be better if you adopt these practices.
[1390.34 → 1394.98] And I think it's really hard to convince people to do it without having that sales pitch.
[1395.24 → 1396.74] This is going to make your life better.
[1396.90 → 1399.10] And that's not like me talking BS.
[1399.10 → 1402.98] Yes, I do think as a data scientist, it will make your life better to do those things.
[1403.18 → 1407.80] Yeah, I definitely, like I remember when I was in my first data science position,
[1407.80 → 1411.92] and I realized like, you know, people started talking to me about like, you know,
[1411.92 → 1417.50] not cutting over to master before you like to have a review and a past test and all these things.
[1417.50 → 1422.32] And I was like, I was very confused by a lot of that, because I did not come from a software engineering background.
[1422.32 → 1425.54] And so I was like terrified when I first went into code reviews.
[1426.02 → 1430.84] But over time, like I realized that, yeah, I could like to skip those things.
[1431.02 → 1434.38] And then like the whole system crashes down, and it's my fault.
[1434.38 → 1437.92] And then it's like a big situation where like I caused this big thing.
[1437.92 → 1442.56] Or I could go through a code review and like have some assurance about how this thing,
[1443.06 → 1447.18] you know, have some like knowledge sharing, but also have some assurance that like,
[1447.60 → 1450.54] I my logic was sound on this or that.
[1450.66 → 1456.90] And now I feel like I don't feel good pushing anything into a place where it's going to be used
[1456.90 → 1458.42] without having someone review it.
[1458.48 → 1461.04] So I think it is like a shift of perspectives.
[1461.04 → 1467.44] You have to, I'm glad that there's kind of this, this effort going on to educate people on these things.
[1467.78 → 1468.68] You know, that's one angle.
[1468.84 → 1474.48] Another angle is that by doing code reviews, you learn a lot, both in terms of having a second
[1474.48 → 1478.48] set of eyes on your code that can tell you, you know, here's another way you could have done this,
[1478.48 → 1482.98] or by reviewing someone else's code and saying, wow, I never would have thought to do it that way.
[1483.18 → 1484.66] But that's a cool way to do it.
[1484.98 → 1490.08] And so doing code reviews is a great way to, you know, keep learning and building skills and getting
[1490.08 → 1491.02] better at what you do.
[1491.50 → 1495.42] And hopefully if someone's a data scientist, that's, you know, something that they're interested in.
[1495.82 → 1500.76] Yeah, I think hopefully a lot of people in this field have that passion for learning.
[1500.76 → 1507.40] And it's definitely true that like, as you have a more diverse set of people and ideas working
[1507.40 → 1510.70] together, you can definitely learn a lot of things that you wouldn't have learned otherwise.
[1511.28 → 1517.12] So in particular with your writing code for NLP research talk, I was kind of just looking through
[1517.12 → 1520.48] that as we were preparing for this interview.
[1520.70 → 1525.48] And you talk about how to write code in a way that facilitates good science and reproducible
[1525.48 → 1527.18] experience experiments.
[1527.30 → 1533.66] Given that this is like practical AI, you know, that is a lot of our focus is giving people
[1533.66 → 1535.94] like practical discussions on this topic.
[1536.04 → 1541.40] I was wondering if you could just give us a few, like maybe some of the most important
[1541.40 → 1547.80] points from from that talk or maybe other talks in terms of what are some like
[1547.80 → 1552.92] immediate wins that you can have in terms of writing code that is reproducible or writing
[1552.92 → 1554.80] code that facilitates good science?
[1555.02 → 1555.12] Yeah.
[1555.26 → 1560.98] So that talk is actually a tutorial from EM NLP last year that it wasn't just me.
[1561.12 → 1565.28] I presented it and wrote it with two of my colleagues here at AI2.
[1565.28 → 1571.18] But since then, I've sort of gone on the circuit of academic AI conferences, sort of beating
[1571.18 → 1577.04] this software engineering practices for AI researchers drum with reproducibility in mind.
[1577.22 → 1582.94] So, you know, the first thing is just what I said before, write unit tests.
[1582.98 → 1586.86] And that sounds weird to say write unit tests for your research code.
[1587.06 → 1592.64] But if your model is not doing what you think it's doing, I mean, that's bad science out of
[1592.64 → 1593.18] the gate, right?
[1593.18 → 1598.08] Like if your model is like accidentally ignoring one of its inputs, then it's not going to be
[1598.08 → 1598.64] doing the right thing.
[1598.78 → 1604.80] So if you write tests and the way we tend to do it is taken a data set like the one you want to use,
[1605.14 → 1609.36] get a very small version, you know, maybe it has two or three instances in it.
[1609.66 → 1613.62] And now write a unit test that takes that data, reads it in, puts it through your model,
[1613.72 → 1617.98] checks that, you know, checks that the output looks right, that the model can run on it without
[1617.98 → 1621.18] crashing, checks that the model can learn to predict it perfectly.
[1621.18 → 1623.76] Because if you have three instances, your model should be able to learn it perfectly,
[1623.96 → 1624.68] things like that.
[1625.02 → 1629.64] And you make these actual unit tests that run along with your code, then that gives you
[1629.64 → 1635.82] this really simple but basic guarantee that code is doing at least sort of what you think
[1635.82 → 1636.18] it's doing.
[1636.44 → 1638.90] So that's one, I would say, really important aspect.
[1639.50 → 1644.52] Another one is that typically you're going to run a lot of experiments, you know, maybe with
[1644.52 → 1645.16] minor variations.
[1645.16 → 1650.24] I'll vary some hyperparameters, or I'll try different kinds of word embeddings, or I'll try
[1650.24 → 1651.58] different number of hidden units.
[1651.90 → 1657.06] And so what you want to do is you want to structure your code that makes it as easy as possible to run
[1657.06 → 1657.60] these experiments.
[1657.80 → 1662.56] And so what that speaks to then is making a real clean division between what I'll call
[1662.56 → 1665.24] library code and experiment code.
[1665.32 → 1670.86] So I want one code that's like, this is the details of how my model works, and this is the details of how
[1670.86 → 1671.98] data gets right off disk.
[1672.42 → 1676.30] And I want this code in a module that's like well tested, and it's not going to change.
[1676.76 → 1678.36] And now I want to run an experiment.
[1678.54 → 1682.64] And maybe that experiment needs to point into a specific data path, and it needs to use, you know,
[1682.68 → 1684.92] some other parameters and various other parameters.
[1685.46 → 1690.02] And I want the experiment code to basically lean very heavily on that module.
[1690.08 → 1696.78] And just, you know, all it's really doing is taking the parameters that I fed in and calling that
[1696.78 → 1697.32] model.
[1697.32 → 1703.22] And so when you separate things out this way, it makes it really easy to, you know, run an
[1703.22 → 1703.52] experiment.
[1703.70 → 1707.16] You don't have to be saying, oh gosh, when I did this one, what version of the code was I
[1707.16 → 1707.32] using?
[1707.38 → 1709.46] When I did this one, which version of the code was I using?
[1709.60 → 1711.78] In all cases, you're using the same code.
[1712.02 → 1714.82] You're just feeding in different parameters to it.
[1714.92 → 1720.56] And so this was a little bit, you know, this was one of my gripes against notebooks is that
[1720.56 → 1724.88] notebooks don't really lend themselves to this kind of division very easily.
[1724.88 → 1730.86] Either you have to, you know, pull all your library code out into a module, in which case
[1730.86 → 1733.10] you're only half working the notebook and half not working the notebook.
[1733.48 → 1738.42] Or you have to do something really elaborate like the system that Netflix uses, where you
[1738.42 → 1743.68] parametrize your notebooks and have, you know, a 50-piece system that runs them and instantiates
[1743.68 → 1745.82] them and saves them and so on and so forth.
[1745.98 → 1750.52] So I think making that clear division is another one.
[1750.84 → 1751.88] It's Python, so depending...
[1751.88 → 1756.80] Not letting the notebook be a crutch, in essence, to where, you know, it's inhibiting you in
[1756.80 → 1757.58] terms of good practice.
[1757.66 → 1757.84] Yeah.
[1757.94 → 1761.80] I mean, I could talk about that in various other contexts at great length.
[1762.02 → 1764.90] But yes, that is certainly one aspect of it.
[1765.12 → 1768.70] The other one, it's sort of obvious, but a couple more.
[1768.86 → 1772.96] One is written good instructions for how to use your code, obviously, because someone's going
[1772.96 → 1774.54] to want to rerun it and reproduce it.
[1774.54 → 1777.68] And if it's not obvious how to do that, then that's no good.
[1778.30 → 1782.68] And, you know, finally, the other one that's important is Python dependency management, like
[1782.68 → 1784.66] in most other languages, is a real pain in the ass.
[1785.38 → 1789.72] And whatever experiment you're running is going to depend in very intricate ways on,
[1789.84 → 1793.16] oh, you know, I use this version of PyTorch and I use this version of Spacey.
[1793.38 → 1797.86] And being as clear as possible about here's how to set up the environment.
[1798.30 → 1799.54] And, you know, that can be your requirements.txt.
[1799.54 → 1802.10] That could be a Docker container.
[1802.42 → 1803.78] It could be anything like that.
[1804.16 → 1808.66] But if you go out and look on GitHub at like data science projects, you can find a ton of
[1808.66 → 1813.46] them where there's literally no indication of how did I set up the environment to do this?
[1813.52 → 1816.42] It just starts with import PyTorch, and it goes from there.
[1816.66 → 1819.68] And your chances of being able to reproduce that are very small.
[1820.12 → 1823.38] Yeah, I definitely have felt that pain.
[1823.62 → 1825.28] I was curious on another point, too.
[1825.28 → 1830.70] You've mentioned tests a couple of times when I'm teaching workshops or something.
[1830.84 → 1835.04] A question that comes up a lot of times when we start talking about testing and this sort
[1835.04 → 1841.64] of thing is like, oh, well, you know, people will tell me like, oh, well, machine learning
[1841.64 → 1847.02] and AI is kind of different, you see, because there's these non-deterministic pieces and there's
[1847.02 → 1847.70] randomness.
[1847.76 → 1850.00] So you're not always going to get the same answers.
[1850.26 → 1851.86] So how do you test that?
[1851.86 → 1856.88] They give the example, like in software engineering, you could have a bunch of like table driven
[1856.88 → 1859.34] tests, and you expect all those things to pass.
[1859.48 → 1864.96] But when you're testing on a test set in machine learning, you don't expect all of them to
[1864.96 → 1866.40] pass and that sort of thing.
[1866.58 → 1871.52] And I kind of like I kind of take issue with that because like if there was no way to test
[1871.52 → 1877.10] like randomness and non-deterministic sort of processes, then like physics wouldn't exist,
[1877.22 → 1877.58] basically.
[1877.58 → 1881.70] But I was curious to hear like your perspective on that.
[1881.80 → 1886.06] Like there's definitely cases where you have like some randomness and other things in your
[1886.06 → 1886.46] code.
[1886.46 → 1890.62] But it seems to be a point that people get hung up on when they start talking about testing.
[1891.14 → 1892.92] So there's a there are a couple of answers to that.
[1893.06 → 1898.80] One is that there are a number of things you can test that should be there in variants of
[1898.80 → 1900.62] your code that don't depend on the randomness.
[1900.62 → 1905.64] So, for instance, given an input, it should run without crashing like that's not a function of
[1905.64 → 1906.06] randomness.
[1906.28 → 1910.54] Given a model and an input that has the right shape, the output should have the right shape
[1910.54 → 1912.08] and it should have the right fields or whatever.
[1912.28 → 1913.86] Again, that's not a function of randomness.
[1913.92 → 1916.76] That should be an invariant of your code.
[1916.96 → 1918.98] And so those things are easy, and they don't depend on randomness.
[1919.32 → 1924.38] As I mentioned earlier, there are other things that depend on randomness, but you can test them
[1924.38 → 1927.38] in ways that are sort of randomness invariant.
[1927.38 → 1933.40] So, you know, I trained my model for on a small data set for 10 epochs and I checked
[1933.40 → 1934.98] that the loss goes down each epoch.
[1935.24 → 1940.12] So is it possible that there's some weird random setup that would make that not be true?
[1940.40 → 1940.76] Possibly.
[1940.90 → 1942.64] But that test is basically always going to pass.
[1943.06 → 1946.04] And if it's going to fail, you know, one time out of a million, you mark it with a
[1946.04 → 1947.72] at flaky decorator and that's fine.
[1948.34 → 1951.36] Similarly, it's true that I have a big neural network.
[1951.44 → 1952.14] It has random weights.
[1952.22 → 1953.34] Who knows what it's going to do?
[1953.66 → 1957.06] But again, if I take a data set that has three examples in it.
[1957.06 → 1963.08] And I train that data set for, you know, 100 epochs with this big model, I can be sure
[1963.08 → 1967.00] that model is going to learn to predict perfectly on those three data points.
[1967.18 → 1968.18] Like, it just has to.
[1968.54 → 1973.94] And so, again, you can come up with these tests in a way that give you some confidence that
[1973.94 → 1979.12] the model is doing what it's supposed to do and are robust enough that they don't care,
[1979.32 → 1982.06] you know what the random initialization of the weights happened.
[1982.46 → 1983.38] They should work regardless.
[1983.38 → 1993.28] Well, hello there, listeners of Practically I.
[1993.38 → 1993.84] How are you?
[1993.92 → 1995.22] This is Adam Stachowiak.
[1995.36 → 1998.98] If you haven't heard yet, we're launching a new show called Brain Science.
[1999.42 → 2001.30] It's a podcast for the curious.
[2001.42 → 2002.10] Are you curious?
[2002.66 → 2008.00] Because if so, we're exploring the inner workings of the human brain to understand things like
[2008.00 → 2012.64] behaviour change, habit formation, mental health, and what it means to be human.
[2013.10 → 2014.96] It's brain science applied.
[2015.42 → 2019.74] Not just how does the brain work, but how do we apply what we know about the brain that
[2019.74 → 2021.56] can transform our lives?
[2022.14 → 2026.40] Learn more about the show and subscribe at changelog.com slash brain science.
[2026.78 → 2031.32] Until then, here's a preview of episode one, where we talk about the fundamentals of being
[2031.32 → 2031.68] human.
[2031.68 → 2034.86] We're also all designed to be in relationship.
[2035.62 → 2041.60] We are fundamentally hardwired to have social groups and this sense of attachment.
[2042.56 → 2048.54] And because I'm sort of a geek when it comes to research, what researchers have found is
[2048.54 → 2054.32] that attachment, which that's what we label how we relate and connect with others.
[2054.32 → 2061.36] Attachment is 100% learned, which means our genetics don't actually contribute to how we learn to
[2061.36 → 2063.46] stay in proximity with other people.
[2063.88 → 2071.36] And with that, that we all develop ways to manage the threat of the loss of a relationship.
[2072.30 → 2076.80] But nobody gets to opt out of going, I need to be in relationship with others.
[2077.00 → 2080.82] It's almost like we need to have that echo from another human being to let us know that
[2080.82 → 2085.78] we're there, or we're alive or just some sort of feedback loop.
[2085.84 → 2087.20] I'm not really sure how to describe that.
[2087.84 → 2090.68] Well, it really is this sense of being with, right?
[2090.74 → 2096.72] Like I can't fight battles on my friend's behalf or on my kid's behalf, right?
[2096.80 → 2102.78] But the simple fact that I know of what's going on makes a difference because I would contend
[2102.78 → 2106.66] it's sort of like I help them hold that weight emotionally.
[2107.56 → 2109.86] And so that actually leads me into the third thing.
[2109.86 → 2114.88] And the third thing that I would say in regard to the fundamentals of being human is that
[2114.88 → 2116.98] we all struggle.
[2117.70 → 2118.08] Oh, yes.
[2118.66 → 2119.10] Right?
[2119.66 → 2120.32] Big time.
[2120.86 → 2125.82] And that, you know, we don't always get to pick the way in which we struggle, but we all
[2125.82 → 2126.28] struggle.
[2127.38 → 2131.74] Well, if you like what you hear, you should go to changelog.com slash brain science.
[2131.84 → 2134.40] The show is not out yet, so don't get too excited.
[2134.40 → 2139.42] But you can subscribe and be notified as soon as the show launches.
[2139.98 → 2143.04] Once again, changelog.com slash brain science.
[2143.04 → 2165.88] So turning toward Allen AI, could you tell us a little bit about the purpose of the organization,
[2166.12 → 2169.66] what its mission is, and the types of problems it's oriented on?
[2169.66 → 2173.68] Yeah, so Allen Institute is a nonprofit research institute.
[2173.68 → 2179.22] It was founded by Paul Allen, and it's funded by him and I guess now his state.
[2179.52 → 2183.32] Yeah, you may want to note who Paul Allen is just in case there's anyone out there who's
[2183.32 → 2183.98] not familiar with him.
[2184.46 → 2186.14] Paul Allen was one of the founders of Microsoft.
[2186.54 → 2188.42] So he got pretty wealthy that way.
[2188.52 → 2193.20] And then after he left, he started a company called Vulcan, which does like a million different
[2193.20 → 2193.62] things.
[2193.62 → 2196.46] And, you know, he was a big Seattle person.
[2196.56 → 2197.44] He was a big everywhere person.
[2198.00 → 2204.88] And so our mission, at least if you look at like the sign on the website, it says AI for
[2204.88 → 2205.88] the common good.
[2206.22 → 2208.00] What that means is a little bit vague.
[2208.08 → 2212.14] I once interviewed someone who was very disappointed to find out that it didn't mean that we used
[2212.14 → 2215.04] like we were working on like the homeless problem or anything like that.
[2215.10 → 2219.76] But what we do is fundamental research in various areas of AI.
[2219.76 → 2225.02] So as I mentioned, the team that I work on, it's called Allen NLP, and we work on sort of
[2225.02 → 2226.76] fundamental research and NLP.
[2226.98 → 2231.54] So not super different from what people who are NLP researchers in a computer science department
[2231.54 → 2232.30] would be working on.
[2232.36 → 2234.02] In fact, we collaborate with them.
[2234.10 → 2235.54] We go to the same conferences they do.
[2235.68 → 2237.68] We present with them, things like that.
[2238.08 → 2242.48] There's another team called Prior, which works on problems in computer visioning and visual
[2242.48 → 2243.00] reasoning.
[2243.72 → 2248.94] We have a project called Semantic Scholar, which is an AI enabled search engine for academic
[2248.94 → 2254.20] papers, where it indexes the academic papers, but it also tries to figure out what papers
[2254.20 → 2257.80] were influenced by this one and what information can I extract from the paper programmatically
[2257.80 → 2258.80] and things like that.
[2258.98 → 2264.08] And we have a project called Ariosto, which I mentioned earlier, which does science question
[2264.08 → 2264.32] answering.
[2264.42 → 2267.20] So can we get an AI to answer science questions?
[2267.20 → 2272.60] And we have a project called Mosaic, which tries to get an AI to do common sense reasoning.
[2272.96 → 2278.20] So you can ask questions about, the science question is like, when a plant makes food,
[2278.20 → 2279.60] what is that called?
[2279.74 → 2281.06] A, photosynthesis, B, whatever.
[2281.60 → 2286.42] But the common sense reasoning is more around understanding folk physics and folk psychology.
[2286.84 → 2288.14] Billy did XYZ.
[2288.54 → 2290.44] Why is it likely that he would have done this?
[2290.70 → 2294.38] And so those are kind of the different areas that you focus on.
[2294.38 → 2294.60] Yeah.
[2294.70 → 2301.36] So at Allen AI, is there like, there's obviously a lot of sorts of academic like research going
[2301.36 → 2307.00] on, but there's also like you've mentioned projects like Allen NLP and there's like, I
[2307.00 → 2312.24] guess, products like, you know, Semantic Scholar that are people are using and out there.
[2312.24 → 2315.70] So there's obviously like some mix of like researchers and engineers.
[2315.70 → 2320.24] I was just kind of curious, like how the teams are structured there, like, and how that might
[2320.24 → 2325.28] be different from like maybe regular academic research where thing, maybe it's that things
[2325.28 → 2328.18] are more geared towards open source or like, I don't know.
[2328.22 → 2330.72] I was curious what that sort of looked like.
[2331.20 → 2333.26] So I would say one, it varies a lot by team.
[2333.54 → 2337.12] So like my team, Allen NLP is actually very researcher heavy.
[2337.12 → 2340.06] It's mostly researchers and only a handful of engineers.
[2340.68 → 2344.30] Whereas Semantic Scholar, you know, they're running a website that has to be up.
[2344.56 → 2349.76] So they have a lot more engineers and, you know, they have to be on call, and they have
[2349.76 → 2352.34] a lot more front end people and things like that we don't really have.
[2352.44 → 2353.92] So it really varies by team.
[2354.24 → 2358.14] In terms of comparison with the academic department, I would say the engineering support that the
[2358.14 → 2364.12] researchers get here is, I would say, mostly not comparable to what people get in an academic
[2364.12 → 2365.12] research department.
[2365.12 → 2370.16] I mean, the engineers here are, you know, I'm Google, other people are ex-Google, ex-Amazon,
[2370.26 → 2371.52] ex-Microsoft, and so on.
[2371.92 → 2376.80] And my understanding, I mean, I've never been in a computer science department, but my understanding
[2376.80 → 2381.02] is that if you're working, you know, as a professor in a computer science department, typically
[2381.02 → 2386.18] you don't have this kind of engineers who are there to collaborate with you and support
[2386.18 → 2386.40] you.
[2386.58 → 2391.82] So I think that's a real deep difference between the way we do things and the way that an academic
[2391.82 → 2392.56] department does things.
[2392.56 → 2396.66] Now, if you go to somewhere like, you know, Google Research or Facebook AI Research, they
[2396.66 → 2400.96] do, or Microsoft Research, they do, those places do have this kind of engineering support.
[2400.96 → 2406.82] So I noticed, I'm looking at the webpage for Allen NLP, and you were talking about that
[2406.82 → 2411.46] being your own project, and it describes that it's an open source NLP research library built
[2411.46 → 2412.08] on PyTorch.
[2412.58 → 2415.10] I'm wondering, like, who is that geared for?
[2415.94 → 2418.44] You know, what is the audience for using it?
[2418.46 → 2421.40] What are the main use cases that you might apply it to?
[2421.68 → 2422.40] Any thoughts there?
[2422.40 → 2428.00] Yeah, so I mean, officially, the target customer is someone doing NLP research.
[2428.50 → 2433.24] So, you know, originally, originally, our target customers were the researchers here at AI2,
[2433.54 → 2436.12] but it was always an open source project, you know, from day one.
[2436.42 → 2440.72] And so then we quickly started, you know, taking on as customers, researchers over at the UW,
[2441.28 → 2446.18] researchers at other universities, people at more corporate research institutes.
[2446.18 → 2454.40] And then, you know, the line between research and work is really narrowing a lot in a lot of ways.
[2454.52 → 2458.14] So there are a lot of companies that you could go to them, startups or big companies or whatever,
[2458.60 → 2463.20] and they're doing things that are, say, at the cutting edge of NLP for their own problems.
[2463.46 → 2469.00] And so their workflows for solving these problems look a lot like the workflow of an academic
[2469.00 → 2470.78] researcher trying to solve an NLP problem.
[2470.78 → 2477.00] And so we do have some customers who, you know, work in companies but still use it anyway.
[2477.32 → 2482.24] And it's always, it's sort of an ongoing source of debate to what extent we should, you know,
[2482.24 → 2488.82] be actively soliciting, supporting more corporate customers versus academic customers.
[2489.08 → 2495.72] I'm giving a tutorial on NLP and NLP more in general at the O'Reilly AI Conference in September,
[2495.72 → 2499.22] which is more of a practitioner-focused conference, not an academic conference.
[2499.22 → 2503.34] And when this was mentioned, you know, someone asked me,
[2503.42 → 2506.74] are we focusing on those practitioners now as customers for the library?
[2507.00 → 2511.84] And I'm like, well, you know, we've always sort of wink-winked that those are our customers,
[2512.20 → 2516.22] but they're not officially who we're focused on, but we want them using it too.
[2516.60 → 2516.68] Yeah.
[2516.82 → 2521.08] And what are, so I'm just trying to think of like the workflow-wise,
[2521.18 → 2526.06] like if I'm an NLP researcher, like where Allen NLP might fit in.
[2526.06 → 2529.48] And so I'm thinking of like a comparable, people might be familiar with something like
[2529.48 → 2533.88] Spacey or something like that, where Spacey has like, you know, pre-trained things that
[2533.88 → 2534.70] are available, right?
[2534.72 → 2540.34] Like I can do some types of NER and other things, and it's all pre-trained, but I can also train
[2540.34 → 2541.44] custom models.
[2541.44 → 2546.68] But I'm not really like messing necessarily with a lot of the like architecture that's,
[2546.68 → 2549.90] the architectures of the neural nets or something like that.
[2549.90 → 2556.34] Is Allen NLP kind of like a level down from that to where like you have more of the ability
[2556.34 → 2560.00] to mess with your models and all of that sort of stuff?
[2560.04 → 2562.56] Or I'm just trying to kind of like gauge where it sits.
[2562.82 → 2563.76] Yeah, that's exactly right.
[2563.92 → 2569.70] So Allen NLP is not, for the most part, it would not be a substitute for Spacey.
[2570.08 → 2576.74] Instead, it would be a substitute for someone who's doing NLP stuff in PyTorch or in TensorFlow
[2576.74 → 2581.32] and says, you know what, there are a lot of problems that are caused by my working with
[2581.32 → 2581.72] text.
[2582.14 → 2588.26] And so I would like to, you know, use a library that has in it abstractions that are really
[2588.26 → 2594.88] intended at people tackling NLP problems and allow me to not worry about some of the nitpicky
[2594.88 → 2599.56] details around masking and padding and recurrent layers and things like that.
[2599.56 → 2606.24] But working in Allen NLP is much more similar to, I mean, when you work in Allen NLP, you basically
[2606.24 → 2607.58] are working in PyTorch.
[2607.70 → 2612.14] You're just working in a PyTorch that has a bunch of higher level abstractions in it.
[2612.34 → 2612.44] Gotcha.
[2612.62 → 2615.32] So it's built on PyTorch essentially, right?
[2615.56 → 2620.68] So if you were coming at it, I'm just curious, from TensorFlow, do you need to kind of go learn
[2620.68 → 2624.08] PyTorch first and then move into it as an intermediate thing?
[2624.08 → 2629.40] Or, you know, what would be with all the people out there that are also doing TensorFlow in addition
[2629.40 → 2630.26] to PyTorch?
[2630.52 → 2632.96] What's kind of the migration path that you would see into that?
[2633.72 → 2634.98] That's an interesting question.
[2634.98 → 2641.30] You would want to learn some PyTorch because Allen NLP is not really insulating you from
[2641.30 → 2643.02] understanding how PyTorch works.
[2643.50 → 2647.50] The way I would describe it is, and this is going to be a terrible analogy, and I'm going
[2647.50 → 2653.14] to regret saying it as soon as I say it, but imagine you have like a big bag of Legos,
[2653.24 → 2653.46] right?
[2653.72 → 2656.12] And just like only the squares and the rectangles, right?
[2656.32 → 2656.60] Okay.
[2656.60 → 2662.82] And then you're building houses or whatever, cars or whatever, and you build everything using
[2662.82 → 2663.60] the little square blocks.
[2663.68 → 2665.54] And then someone comes in and says, hey, you know what?
[2665.94 → 2668.10] I noticed you're making like a lot of walls.
[2668.50 → 2670.08] So here's a piece that's just a wall.
[2670.32 → 2673.56] And now you can use this one piece to make a wall instead of having to build each wall
[2673.56 → 2674.86] out of like little blocks, right?
[2674.86 → 2677.76] And so that's kind of my analogy for what we're doing.
[2678.04 → 2682.74] And so that allows you to, you know, now I don't have to worry about walls, or now I don't
[2682.74 → 2686.28] have to worry about doors, but you still have to know how Legos work, and you still have to
[2686.28 → 2687.36] know how to build with Legos.
[2687.48 → 2688.60] You know what I mean?
[2688.72 → 2689.22] Does that make sense?
[2689.56 → 2689.78] I do.
[2689.96 → 2690.82] And it's a good analogy.
[2691.14 → 2693.52] I have a seven-year-old, so we have Legos all over the place.
[2693.56 → 2694.38] That was perfect for me.
[2694.38 → 2700.68] So I'm kind of curious, like being, you know, I've been involved in certain open source
[2700.68 → 2706.30] projects over time, but always geared towards kind of like the I don't know what you want
[2706.30 → 2708.62] to call it, like the regular software engineering community.
[2708.90 → 2713.98] What have you found to be kind of like unique challenges of creating an open source project
[2713.98 → 2718.08] for the AI community or more for the research side of things?
[2718.56 → 2720.46] Have there been unique challenges with that?
[2720.46 → 2724.56] So this is like the biggest open source project I've ever really worked on.
[2724.78 → 2728.88] In fact, it's probably the only like multi-person open source project I've ever worked on.
[2728.98 → 2733.50] So it's hard for me to say whether the challenges we face are unique.
[2733.80 → 2739.02] I can tell you some of the challenges that we face are people who submit issues without
[2739.02 → 2742.22] enough information about what they're doing or how to reproduce the problem they're running
[2742.22 → 2742.50] into.
[2742.50 → 2746.38] But I imagine most open source projects probably face that issue.
[2746.38 → 2754.12] The one that we struggle with a lot, I think, is that we have extremely high coding standards.
[2754.48 → 2759.92] So we have just a ton of continuous integration checks before you can merge your code.
[2760.08 → 2764.38] So we use Python 3 type annotations, and we actually run MYP on the code base.
[2764.46 → 2770.38] And so if you submit a PR that doesn't type check or MYP, the CI system will spit it out.
[2770.38 → 2775.94] And we use Point with, Point is sometimes the bane of my existence.
[2776.22 → 2779.48] But again, if you don't format your code right, Point's going to choke on it.
[2779.86 → 2783.96] And we have some code to make sure that you've actually written, you know, Sphinx documentation
[2783.96 → 2786.16] for every class you've added.
[2786.42 → 2791.96] So basically, in order to maintain this very high bar for code, what that means is that
[2791.96 → 2795.26] contributing to the library is sort of a pain in the ass because most people who want
[2795.26 → 2798.82] to contribute, they might not know about MYP, they might not know about Point, especially
[2798.82 → 2799.80] if they're, you know, researchers.
[2800.06 → 2805.30] And so getting them over that hurdle can be pretty difficult sometimes.
[2805.48 → 2806.14] So that's one aspect.
[2806.28 → 2812.10] The other aspect that I think we always struggle with is when you own an open source project
[2812.10 → 2815.62] and, you know, it's an open source project, but it's also our project.
[2815.90 → 2818.56] You have to support people, and you have to maintain it.
[2818.70 → 2822.70] So every time someone wants to contribute something to the library, someone who's not on our team,
[2822.78 → 2824.34] say, like on one hand, that's awesome.
[2824.42 → 2825.74] I love that you want to contribute to my library.
[2825.74 → 2829.74] On the other hand, like you're putting this piece of code in the library and now if it
[2829.74 → 2831.54] breaks, I'm the one who's going to have to fix it in a month.
[2831.62 → 2833.28] And maybe I didn't even understand it when you wrote it.
[2833.50 → 2835.94] And when people have questions with it, they're not going to go to you.
[2836.00 → 2836.74] They're going to go to me.
[2836.98 → 2840.70] And so it's this constant tension between, yes, I love that you want to contribute to the
[2840.70 → 2840.98] library.
[2841.22 → 2846.82] But at the same time, do I want, you know, your contribution to be something that I'm going
[2846.82 → 2851.32] to sign up to support and maintain forever, basically.
[2851.32 → 2856.08] And that's another ongoing struggle that I don't think we found the right answer to,
[2856.16 → 2856.42] exactly.
[2856.96 → 2861.18] You know, it's funny, that last answer, I'm going to, I had a question for you, but I'm
[2861.18 → 2865.98] actually going to ask you two, because since you're working on a team that is, you know,
[2866.04 → 2869.84] it's more than just yourself, and you have to juggle multiple people and their perspectives
[2869.84 → 2870.18] and all.
[2870.36 → 2874.78] What I was going to ask you which I'd like to address, but I'm going to tag on to, is what
[2874.78 → 2876.44] is the team working on right now?
[2876.52 → 2877.52] You know, what are some of the cool things?
[2877.52 → 2883.34] But also, as an individual on the team, what are you excited about in terms of, you know,
[2883.38 → 2886.78] the future for AI and natural language and the types of things you guys are working on?
[2886.92 → 2889.70] So, you know, kind of team perspective and also your own.
[2889.80 → 2890.40] I'm curious.
[2890.88 → 2896.56] So our team, like I said, is mostly researchers, and they're doing research around things like
[2896.56 → 2903.42] paragraph understanding, semantic parsing, question answering, language modelling, sort of
[2903.42 → 2907.20] wide variety of NLP topical research kind of things.
[2907.20 → 2911.14] We have a handful of, like I said, we have a lot more researchers than we do engineers.
[2911.32 → 2914.70] What I'm working on right now is mostly, I don't know if you got a chance to check out
[2914.70 → 2918.28] the NLP demo, but we have this demo.alanlp.org.
[2918.54 → 2921.16] We have these interactive demos for a lot of our models.
[2921.52 → 2925.24] And that's one of the value propositions of the library is that, you know, once you've
[2925.24 → 2928.60] trained a model, we make it sort of easy to get an interactive demo.
[2928.72 → 2932.34] And so on of the things I'm working on right now is basically once you've trained a model,
[2932.50 → 2936.98] basically for free, you can get a hideous demo, which is like text in and JSON out.
[2936.98 → 2943.06] How can I make it so that you can get for almost free, like a beautiful interactive demo that's
[2943.06 → 2947.68] like text in and widgets out and make it so that someone who doesn't know, you know, a
[2947.68 → 2950.78] ton of JavaScript or React can get it working very easily.
[2950.92 → 2953.70] So that's, that's kind of one of my main areas of focus.
[2953.86 → 2958.12] Right now we have other people who are working on things like, how can I train more efficiently?
[2958.62 → 2960.42] You know, how can I speed up these models?
[2960.76 → 2961.96] How can I use less compute?
[2961.96 → 2963.88] As well as just adding various other stuff.
[2964.20 → 2969.22] Well, I, for one, would love to see this, this demo functionality that you're, you're
[2969.22 → 2969.80] talking about.
[2969.92 → 2971.64] I would be super excited to use that.
[2971.74 → 2975.44] It would like to make me seem way cooler than I actually am.
[2975.70 → 2976.30] So you're cool, buddy.
[2976.44 → 2978.38] I would always appreciate things like that.
[2978.46 → 2982.38] So to kind of wrap up, first off, thank you so much for joining us.
[2982.38 → 2987.80] Um, as I already mentioned, like I've been a fan for quite some time, so it's been a real
[2987.80 → 2991.08] honour to, to get to chat with you a little bit and get to know you a little bit.
[2991.16 → 2995.24] Um, just as we wrap up, where can people find your book first?
[2995.28 → 3000.12] And then maybe also what's the best place where people could start learning about, um,
[3000.18 → 3000.76] Allen NLP?
[3000.88 → 3003.84] I know there's, it's probably on GitHub, but are there other places?
[3003.84 → 3005.36] Do you have like a website?
[3005.36 → 3007.92] Are there like Slack groups or anything like that?
[3007.98 → 3009.36] What's the best way to get engaged?
[3009.36 → 3009.80] Yeah.
[3010.02 → 3012.82] So, um, you can get my book anywhere books are sold.
[3012.94 → 3015.88] I, I went in the Barnes and Noble a couple of weeks ago, and they had a copy there.
[3016.00 → 3019.94] So I took it out from nowhere it was hiding and put it right in the front of the rack very
[3019.94 → 3020.46] prominently.
[3020.76 → 3021.16] Of course.
[3021.26 → 3022.36] You can get it from Amazon.
[3022.90 → 3025.78] Uh, O'Reilly shut down their bookstore, so you can't buy it directly from them.
[3025.82 → 3031.34] But if you want to buy a PDF version, currently those are sold through something called eBooks.com,
[3031.40 → 3035.96] which is where you can buy PDFs of O'Reilly, but really any, any online bookstore, you should
[3035.96 → 3037.24] be able to get it.
[3037.24 → 3041.02] If you want to find out about Allen NLP, the best place is to start just at our website,
[3041.20 → 3042.52] AllenNLP.org.
[3042.56 → 3046.98] That will take you to demos and tutorials and so on.
[3047.08 → 3049.62] If you want to look at the actual code itself, that's on GitHub.
[3049.98 → 3051.98] It's Allen AI slash Allen NLP.
[3052.26 → 3056.82] You can go there and see our enormous backlog of issues and pull requests and laugh at us
[3056.82 → 3058.00] for having such a big one.
[3058.64 → 3059.86] Can I pitch all my other presences?
[3060.28 → 3060.96] Yes, please do.
[3060.96 → 3062.34] Um, so I have a website.
[3062.54 → 3064.60] Uh, it's just my name, joelgruce.com.
[3064.70 → 3067.52] I blog very infrequently, but when I do, it's pretty good.
[3067.78 → 3069.16] I am on Twitter all the time.
[3069.24 → 3071.26] That's at joelgruce, and you can find me there.
[3071.34 → 3076.82] And it so happens that I have my own podcast, uh, with Andrew Mussulman called Adversarial
[3076.82 → 3080.02] Learning, uh, which we rarely record, but sometimes we record it.
[3080.14 → 3082.48] And that's at adversarialearning.com.
[3082.58 → 3082.90] Awesome.
[3083.10 → 3083.30] Yeah.
[3083.34 → 3088.34] And I must say it's, uh, both on the blogs and the podcast when they do come out, I highly
[3088.34 → 3088.98] recommend them.
[3089.08 → 3090.78] So thanks for, thanks for sharing those.
[3090.90 → 3091.56] Oh, and one more.
[3091.74 → 3095.04] Um, I like to make live coding videos and those are all up on YouTube.
[3095.04 → 3097.30] And I think that's just YouTube.com slash joelgruce.
[3097.42 → 3101.50] So if you want to watch me, uh, live coding, uh, frequently problems that, that I haven't
[3101.50 → 3104.30] looked at before I started live coding them, go there and check those out.
[3104.42 → 3104.64] Cool.
[3104.84 → 3105.16] Awesome.
[3105.50 → 3106.30] Definitely will.
[3106.50 → 3107.98] Um, thanks again for joining us.
[3108.06 → 3112.76] Hope we can meet up at a conference sometime, but look forward to, uh, to more great content
[3112.76 → 3113.28] online.
[3113.46 → 3115.64] And, uh, thank you so much for the discussion.
[3115.92 → 3116.10] Yeah.
[3116.16 → 3116.88] Thanks for having me.
[3118.34 → 3119.74] All right.
[3119.80 → 3122.48] Thank you for tuning into this episode of practical AI.
[3122.70 → 3126.80] If you enjoyed this show, do us a favour, go on iTunes, give us a rating, go in your podcast
[3126.80 → 3127.78] app and favourite it.
[3127.90 → 3131.10] If you are on Twitter or social network, share a link with a friend, whatever you got to
[3131.10 → 3132.34] do, share the show with a friend.
[3132.42 → 3137.54] If you enjoyed it and bandwidth for change log is provided by fast learn more at fastly.com
[3137.54 → 3141.40] and we catch our errors before our users do here at change law because of roll bar, check
[3141.40 → 3143.56] them out at robert.com slash change log.
[3143.56 → 3148.34] And we're hosted on Linde cloud servers and a leno.com slash change log.
[3148.44 → 3148.88] Check them out.
[3148.96 → 3149.80] Support this show.
[3149.96 → 3153.42] This episode is hosted by Daniel Whiten ack and Chris Benson.
[3153.64 → 3158.96] The music is by break master cylinder, and you can find more shows just like this at change
[3158.96 → 3159.70] law.com.
[3159.70 → 3163.92] When you go there, pop in your email address, get our weekly email, keeping you up to date
[3163.92 → 3168.18] with the news and podcasts for developers in your inbox every single week.
[3168.18 → 3169.36] Thanks for tuning in.
[3169.50 → 3170.26] We'll see you next week.
