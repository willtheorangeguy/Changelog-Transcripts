[0.00 --> 6.48]  What we believe we can do better than any company in the world at Bundle IQ is we believe we can engineer eureka moments.
[6.48 --> 11.28]  So those aha moments that might come to you when they're least expected.
[11.72 --> 14.22]  That's kind of like our North Star as a company.
[14.62 --> 21.18]  And so when you think about research and analysis, whether it's on what models to use or other parts of your business,
[21.38 --> 28.84]  when you're going through this research process and trying to make sense of all of this information that's out there on the Internet or in your inbox,
[28.84 --> 32.74]  that's like disparate information that kind of lives in multiple places.
[32.74 --> 42.96]  And so what we aim to do is basically be that like centrifuge that can kind of crunch all that data and make those unexpected connections across information using math.
[45.54 --> 48.24]  Big thanks to our partners, Linode, Fastly and LaunchDarkly.
[48.60 --> 50.66]  We love Linode. They keep it fast and simple.
[50.78 --> 53.14]  Check them out at linode.com slash changelog.
[53.36 --> 55.44]  Our bandwidth is provided by Fastly.
[55.80 --> 57.12]  Learn more at Fastly.com.
[57.12 --> 59.34]  And get your feature flags powered by LaunchDarkly.
[59.60 --> 61.34]  Get a demo at LaunchDarkly.com.
[68.68 --> 75.72]  Welcome to Practical AI, a weekly podcast that makes artificial intelligence practical, productive, and accessible to everyone.
[76.04 --> 80.10]  This is where conversations around AI, machine learning, and data science happen.
[80.38 --> 85.14]  Join the community and Slack with us around various topics of the show at changelog.com slash community.
[85.14 --> 88.18]  And follow us on Twitter. We're at Practical AI FM.
[94.56 --> 97.28]  Welcome to another episode of Practical AI.
[97.64 --> 99.16]  I'm your host, Chris Benson.
[99.44 --> 101.80]  I am a technology strategist at Lockheed Martin.
[102.26 --> 106.20]  Normally, you would have Daniel Whitenack, my co-host, with me here today.
[106.38 --> 110.34]  Daniel is unfortunately on a plane right now and is not able to make this.
[110.34 --> 113.40]  So, I'm going to go right into introducing our guest.
[113.54 --> 117.64]  I'm excited because there's some topics here that I'm really looking forward to diving into.
[118.12 --> 125.20]  I'd like to introduce Nicholas Mohagny, who is the CEO and co-founder of Bundle IQ.
[125.80 --> 127.00]  Welcome to Practical AI, Nick.
[127.22 --> 128.20]  Thanks for having me, Chris.
[128.52 --> 129.12]  You're very welcome.
[129.38 --> 134.12]  I guess if you could start off a little bit, give me a little bit of background.
[134.12 --> 139.52]  We have some interesting topics, GPT-3 and others that I'm looking forward to.
[139.96 --> 148.12]  But if you could tell us a little bit about how you arrived into this space and a little bit about what you're all about to get us going.
[148.48 --> 149.08]  Yeah, definitely.
[149.42 --> 155.34]  Obviously, GPT-3 is, I wouldn't say a big topic of discussion, but it's definitely making mainstream news.
[155.66 --> 159.28]  And that's definitely something that we've been excited here at the team to explore.
[159.28 --> 165.20]  As part of this, could you tell us a little bit about what that is, just since you're already kind of referencing it right off the bat?
[165.46 --> 165.66]  Yeah.
[165.86 --> 167.68]  So, there's a company called OpenAI.
[168.28 --> 175.74]  And I don't know how accurate this is, but I would like to say that it's sort of like the next space race to create artificial general intelligence.
[176.20 --> 179.70]  And so, there's a company that was founded as a nonprofit initially.
[179.86 --> 181.72]  And I think they do have a for-profit arm as well.
[181.82 --> 186.82]  But basically, to go out and try to build some intellectual property and try to do just that.
[186.82 --> 194.14]  So, for people that maybe don't know what artificial general intelligence is, it's kind of trying to replicate the intelligence of human beings.
[194.70 --> 199.90]  You know, they've said that a fifth grader is more generally intelligent than the best AI out there.
[200.20 --> 204.88]  And that, you know, so long story short, we got into the beta program and we've been exploring.
[205.22 --> 209.58]  And we're probably one of maybe only a few hundred apps that is live currently.
[209.58 --> 214.04]  Because you do have to go through an application process and get approved to go live with GPT-3.
[214.04 --> 221.48]  So, they do have some throttles on the system, some checks in place to make sure maybe it doesn't get into bad actors' hands, so to speak.
[221.78 --> 225.38]  I wouldn't say that was my foray into AI and bundle IQ, per se.
[225.52 --> 234.78]  But, you know, having done some maybe preliminary modeling and then moving on to GPT-3 has been a nice step in the right direction for us as a company.
[234.78 --> 249.80]  Gotcha. And for those in the past, we've had folks from OpenAI come on and talk a little bit about, but I don't think we've ever had a show focused on capabilities, especially with someone like yourself who's gone in and started using GPT-3.
[250.26 --> 255.14]  Could you describe what GPT-3 is for anybody that's not familiar with that as an algorithm?
[255.14 --> 259.28]  Like, what space is it in? Was it trying to do? What kind of capabilities?
[259.76 --> 265.66]  And I understand that this is not your algorithm. It's one that your company is taking advantage of to great effect.
[266.00 --> 269.52]  But if you could just kind of give me your take on what GPT-3 is.
[269.78 --> 274.58]  Yeah. So, essentially what they've done is they've ingested like 10% of the internet.
[275.18 --> 280.88]  I think it's like 160-something billion parameters worth of data, which is mind-boggling.
[280.88 --> 287.86]  Right. So, they've done that. And by doing that, they've been able to create these really creative models for language.
[288.20 --> 293.48]  So, you could, as an example, you could maybe say something like in the GPT-3 playground, say,
[293.68 --> 300.38]  create a science fiction script for automated robots inside of battleships.
[300.80 --> 306.74]  You know, like, and it would like create the story for you, you know, so you can kind of create those really fun prompts.
[306.74 --> 310.38]  So, you could say, create a recipe for Halloween and it would come up with a recipe for Halloween.
[310.38 --> 316.16]  That's pretty cool. So, I mean, is it essentially unbounded in terms of the types of questions that you would ask?
[316.28 --> 320.34]  Or would you think of it as average everyday question that you might ask Google,
[320.44 --> 325.10]  which is kind of what it's sounding like a little bit, but then it goes and generates that output from scratch?
[325.30 --> 333.12]  Yeah. So, I think on the simplest level, it's a great mirror to hold up to any sort of inquiry or prompt.
[333.12 --> 339.54]  So, you can kind of start to get, you know, more context for maybe a very small amount of information,
[340.08 --> 343.00]  finishing a sentence or creating a tweet or creating a paragraph.
[343.00 --> 345.96]  And there's some apps out there that have taken full advantage of that.
[346.24 --> 349.54]  Namely, there's an app called Jarvis that helps with like marketing copies.
[349.68 --> 355.12]  So, let's say you're creating a LinkedIn ad and, you know, you want to target, you know, business professionals in the C-suite.
[355.12 --> 363.02]  You know, you can kind of use GPT-3 to come up with like 50 potential scripts for that ad within like six seconds.
[363.26 --> 363.42]  Wow.
[364.44 --> 370.58]  So, how did you get, I know you got into the beta program and I remember when they were, when OpenAI was soliciting that.
[370.86 --> 377.06]  And I know that later on Microsoft, I believe, has some sort of exclusive license to doing that.
[377.06 --> 382.82]  Are you still, are you still going through OpenAI's program or do you do this through Microsoft or?
[383.08 --> 389.00]  Yeah, we're not part of like any formal programming per se, but we are part of the beta and we're using the playground.
[389.00 --> 396.02]  And we've used a couple of their models to support the outputs, I guess, of like the results of the work that we do at BundleIQ.
[396.18 --> 400.78]  And we've also been transitioning away from GPT-3 because a lot of it is a black box.
[400.78 --> 407.80]  So, just from like a technical standpoint, you know, if you're going to build out a company, it's obviously not good to just use.
[408.06 --> 409.06]  There's a risk there.
[409.24 --> 409.40]  Yeah.
[409.54 --> 410.38]  Third-party software.
[410.54 --> 411.08]  Yeah, exactly.
[411.24 --> 416.30]  So, if they cut us off and, you know, we can't create the results for our end user that we want to.
[416.42 --> 421.62]  So, we used it mostly for training purposes and to see what the capabilities might be.
[421.74 --> 429.14]  But we've since even, I think, since you and I connected initially a month or so ago, we've already started to transition away from it.
[429.14 --> 430.22]  Okay. Understood.
[430.54 --> 440.50]  From a business standpoint, that's a very interesting perspective because clearly if you build a business around something that you don't, you know, control directly, especially as beta, let's talk about that for a moment.
[440.62 --> 450.46]  Like, how are you thinking about that as the CEO of your company and you're looking at this really cool technology, but it has a definite risk in terms of that dependency?
[450.76 --> 452.22]  How are you thinking about it?
[452.22 --> 464.54]  You know, if you're looking at other alternatives, other algorithms in the natural language processing space that help you get to the same destination that your company is going, how do you look at that landscape?
[464.70 --> 465.70]  How do you evaluate it?
[465.82 --> 467.88]  And what are the options looking like to you?
[468.02 --> 479.24]  Not trying to get you to reveal your specific business plan, but if you could give us a little perspective on how you see the world in that way, I imagine that's something a lot of people would wonder.
[479.24 --> 491.24]  Yeah, definitely. And it's a good question. You know, it's a question that obviously a lot of investors have asked, like, okay, if you're using this, then what, you know, what are your dependencies? What are your vulnerabilities? That sort of thing. What is your technical moat?
[491.60 --> 497.60]  Your technical moat really look like if you're sort of using this as a black box solution.
[497.60 --> 511.34]  So what we've had to do is basically build out our own ensembles. And in kind of the AI world, you and ensemble, you think of it as like, you know, like an orchestra, like you have the woodwinds and the horns and the, you know, the brass and the strings, right?
[511.34 --> 530.52]  So those different types of instruments and the ensemble of like, maybe an AI model that you'll be passing data through looks like, you know, maybe filtering, maybe summarization, maybe, you know, some other component that can help you sort of have this like beautiful symphony, you know, harmonious, like melody coming out on the other side.
[530.52 --> 543.74]  We basically looked at GPT-3 as kind of the benchmark. So, okay, if this is the best, and they're saying this is the best, then like, how close can we really get by doing it on our own? And that was kind of what we sort of used GPT-3 for initially.
[543.74 --> 569.58]  It kind of gives you something to target. But you're kind of inferring another point, I think, and correct me if I'm wrong, but GPT-3 is so big, and it's so expansive, if you look at the inputs about how much of the internet, you know, was used to develop the model. And any business, not just yours, though, has a narrower scope, you know, of trying, you have a specific business plan, you're trying to do stuff.
[569.58 --> 591.94]  Would it be fair to say that recognizing that GPT-3 is so expansive that you don't have to produce the same thing to satisfy your business need, that you can have a narrower, smaller scope and still be as good or better than you might have been with GPT-3 if you can get the right model going, if you get the right algorithm developed? Is that a fair way of looking at that?
[591.94 --> 604.60]  Yeah, you did a great job at reading between the lines there. So the answer is yes. So Chris's data is not 10% of the internet. We basically build the model, each individual model and ensemble is like attached to Chris's data.
[604.74 --> 604.98]  Okay.
[605.02 --> 612.48]  And the people that Chris works with, it's definitely much narrower and more explicit in nature. It's not as creative. It doesn't need to be.
[612.58 --> 616.28]  Gotcha. You're able to kind of personalize based on your user in that way.
[616.46 --> 617.00]  That's correct.
[617.00 --> 646.00]  That user has a certain amount of data. It's not everywhere. God, I hope my data is not everywhere on the internet. I know it is, but at least you can do that. And this is just a stab in the dark curiosity. Our last episode that we released as I recorded this was on federated learning. Is there any interest or intention of using federated learning to build up better models, but yet letting certain data, you know, that's in private, you know, you have a user and they don't want their data out, but you can train models on that and infer back to the aggregated model.
[646.00 --> 653.08]  Has there been any thought of doing that? And I'm mainly just curious because I've been talking about federated learning a lot the last few days.
[653.32 --> 657.98]  It's a good question and it's one that we've discussed, but it's not a bridge that we've crossed yet.
[658.26 --> 658.38]  Gotcha.
[658.70 --> 672.78]  So I'd be purely speculating on like where we might go with that, but I think there's definitely value in federated learning and sort of extrapolating context and meaning maybe based on industries or categories or et cetera.
[672.78 --> 679.52]  Gotcha. So it sounds like you're in a bit of a transition right now as you're looking at the world outside of GPT-3.
[680.10 --> 696.60]  Can you describe a little bit, aside from your choices and your decisions for your business, but just in a broader sense, you know, as you're looking at that, what does the state of this particular branch of natural language processing look like to you and your team at this point?
[696.60 --> 705.36]  You're a business that's already in flight. You're already moving and you already have users that you're supporting and you're out there doing what your business does.
[705.56 --> 709.60]  And this landscape is changing around on you on a day-to-day basis.
[709.92 --> 717.92]  How does that look and how do you evaluate all the options, whether they're options that are interesting to your specific use case at your business or not?
[718.24 --> 720.52]  How do you do that? How do you stay up with it?
[720.52 --> 728.30]  I think it's software in general is sort of always evolving. It's a living and breathing kind of organism unto itself.
[728.54 --> 733.12]  And so we're constantly iterating through the process of optimizing the outcome.
[733.12 --> 744.52]  And some of that includes, you know, maybe changing the infrastructure because some of our assumptions on how we were doing something one way with like tokenization of keywords and extraction and that sort of thing.
[744.64 --> 750.46]  And creating all these cues and like, you know, moving data in certain directions without, I guess, boring you with the details.
[750.46 --> 763.70]  Like what we've learned is that by instituting new models that maybe turn natural language into math, you don't have to do as much of the language part of it versus doing the math part of it.
[763.70 --> 776.78]  So like vectorizing data, for instance, you know, and then in building machine learning on an individual like customer basis is much more scalable than maybe trying to manage, you know, an entire organization's knowledge base.
[777.14 --> 779.40]  But just kind of maybe zooming out a little bit.
[779.52 --> 787.78]  So just for the audience, you know, what we believe we can do better than any company in the world at Bundle IQ is we believe we can engineer eureka moments.
[787.78 --> 793.14]  So those like aha moments that might come to you when they're least expected.
[793.68 --> 797.66]  And so, you know, that's kind of like our North Star as a company.
[797.88 --> 810.76]  And so when you think about like, you know, you do a lot of research and, you know, you're constantly doing analysis, whether it's on, you know, what models to use or, you know, other parts of your business or people that you bring onto your podcast.
[810.76 --> 827.38]  When you're going through kind of this research process and trying to make sense of all of this information that's out there on the Internet or in your inbox or a note that, you know, Daniel shared with you or whatever it is, that's like disparate information that just kind of lives in multiple places.
[827.38 --> 839.28]  And so what we aim to do is basically be that like centrifuge that can kind of, you know, like crunch all that data and like make those unexpected connections across information using map.
[839.60 --> 841.94]  That's kind of like the ultimate, you know, vision.
[842.20 --> 857.36]  And we've been able to achieve that, thankfully, by using working with our users and using their data sets initially from their notes and then now moving into their emails and now moving into their Google Docs and other forms of information like PDFs and, you know, SharePoint files.
[857.38 --> 858.28]  And things like that.
[887.38 --> 916.38]  So that sounds really cool.
[916.38 --> 925.12]  In terms of how you are trying to find or, you know, locate or maybe even to some degree construct those eureka moments for people from that.
[925.56 --> 932.20]  Before we dive into the fully into the kind of the logistics of what that means to the user, where did you get the idea from?
[932.32 --> 933.08]  I'm just curious.
[933.08 --> 938.68]  Like when you were you're in the space and you're looking and you're seeing these tools, you know, we talked about GPT-3.
[938.82 --> 942.98]  You've talked about other developing other algorithms based on your user's data.
[942.98 --> 946.88]  What was the inspiration for going down this path to begin with?
[947.18 --> 947.26]  Yeah.
[947.36 --> 949.54]  So we're going to zoom way, way, way, way out.
[949.62 --> 949.88]  Okay.
[949.94 --> 951.68]  And we'll talk about Internet 2.0.
[952.32 --> 958.00]  And basically, you know, as a society, we've done a really, really good job at getting a lot of information online.
[958.00 --> 965.20]  And so we've sort of encapsulated the information age with a ton of data and databases.
[966.26 --> 971.26]  And now we've like moved from the information age into the experience age.
[971.26 --> 976.10]  And now we're trying to figure out how do we get our time back from sorting through all of this information?
[976.50 --> 981.88]  And that's like the real problem is like, you know, information overload is not only is it real, it's like palatable.
[981.88 --> 984.88]  And we have like chronic stress as a result of it.
[985.06 --> 985.84]  Indeed we do.
[987.40 --> 992.20]  So thinking about like, you know, the whole elephant equation is like one bite at a time.
[992.20 --> 998.60]  It's like, okay, let's, let's like zoom in to now Chris and like just his, what does he want to do in life?
[998.60 --> 1000.94]  What is going to like help you solve problems?
[1001.08 --> 1002.86]  And what are the problems that you have?
[1002.94 --> 1007.82]  And it's like, you know, humans are really, really great at better than machines at three things.
[1008.20 --> 1010.52]  Creativity, innovation, and imagination.
[1010.52 --> 1021.46]  And so like for us, we, it's like, how can we stay in those lanes and let the machines like come alongside the machines to like do all the heavy lifting on the information management side?
[1021.78 --> 1024.40]  So that was kind of my thought process in it.
[1024.40 --> 1028.96]  So let's take that motivation and a little bit of that history.
[1029.42 --> 1034.98]  And what have you gone and kind of built out and kind of pulling some of the strings together?
[1034.98 --> 1041.02]  Because we opened up the conversation kind of talking about, you know, the algorithms and GPT-3 and what it can do.
[1041.02 --> 1051.12]  So you've talked about these different points that are the touch points in the user's life, you know, like email and, and, you know, we have all these different messaging platforms that we're all using and stuff like that.
[1051.12 --> 1059.64]  And you'd also talk just now about keeping us in that area that we're strongest at, which is innovation, creativity, and imagination.
[1059.64 --> 1068.74]  So how are you pulling these, all these little pieces together to create something at Bundle IQ that addresses that?
[1068.74 --> 1077.52]  Yeah, I guess this in the simplest form, we're basically vectorizing the information and attaching that to, to you, the user.
[1077.52 --> 1088.56]  So whatever you're inputting into the system in the form of emailing people or writing notes or saving a document to the cloud or whatever, that is tied to you.
[1088.62 --> 1097.02]  And then anything that you are shared, like on a folder or a drive or a channel that you're shared in, that is also tied to you.
[1097.24 --> 1102.06]  And then basically just storing that and building the mechanics around just that.
[1102.32 --> 1103.68]  That's like the simplest form.
[1103.68 --> 1113.96]  What do you do with it? Like taking that raw data, if I'm your user, you're taking all that Chris generated or received stuff, things that I'm touching in my day to day.
[1114.06 --> 1119.68]  And you mentioned the eureka moment, which kind of grabbed me a little bit because I'm looking for some eureka moments, quite honestly.
[1120.04 --> 1121.00]  How do we find that?
[1121.30 --> 1127.08]  What are you taking all of that input data about me and the thing in my activities and my day to day?
[1127.40 --> 1133.66]  How are you trying to find what is the kind of thing that you're going to pull out of that to give me that, that thing that you described?
[1133.68 --> 1138.08]  Right. So I'll give you a user story that just came to me about a week ago.
[1138.70 --> 1150.24]  So you're a manager, you sit down to email and you had just interviewed maybe five or six candidates and you need to reply to four of those with a rejection letter.
[1150.72 --> 1158.00]  So you know that like maybe three months ago, four months ago, you had just written an email that was the perfect email for this rejection letter.
[1158.00 --> 1160.92]  But the problem is it's not titled rejection letter.
[1161.24 --> 1163.56]  So how do you find that?
[1163.68 --> 1164.74]  And you're like, I don't know.
[1164.82 --> 1165.84]  It was Susan.
[1166.00 --> 1167.22]  I don't even remember her name.
[1167.36 --> 1168.68]  Like, I don't know her email address.
[1168.94 --> 1173.44]  And that's where it's like, again, connecting like information that's already out there.
[1173.60 --> 1176.08]  So imagine now you're writing this email.
[1176.08 --> 1182.54]  And within the first few sentences, this nudge comes up and says, hey, Chris, you might want to check this out.
[1182.96 --> 1186.44]  And it's the email that you wrote to Susan, you know, six months ago.
[1186.64 --> 1187.18]  And it was right.
[1187.26 --> 1190.92]  And you get to copy and paste that content into that email in that moment.
[1191.00 --> 1194.56]  That was a, you know, a pretty cool one that I was like, oh, wow, that's cool.
[1194.56 --> 1201.58]  So it's kind of you're using those capabilities in the NLP model that you're using.
[1201.82 --> 1203.32]  I know you started with GPT-3.
[1203.54 --> 1206.24]  You're looking at other options going forward at this point.
[1206.44 --> 1214.30]  But you're using that capability to kind of, I'm a little afraid to use the word, but kind of create some context around that person.
[1214.48 --> 1214.92]  Absolutely.
[1215.16 --> 1216.26]  In terms of what they're doing.
[1216.34 --> 1216.84]  Is that fair?
[1216.98 --> 1219.12]  So it's recognizing what you're saying.
[1219.44 --> 1221.68]  And it's like, oh, you might be talking about these things.
[1221.68 --> 1227.94]  And then it's looking into like the corpus of content or data from your emails and notes and all these different places.
[1228.24 --> 1234.14]  And then it's starting to recommend the most relevant suggestions that might be useful in that moment.
[1234.46 --> 1234.64]  Okay.
[1234.84 --> 1238.66]  In the use case you talked about, it kind of feels like personal assistant.
[1239.08 --> 1239.28]  Yeah.
[1239.50 --> 1245.48]  In terms of kind of helping me be better at what I am than I would be by myself, which is kind of ironic.
[1245.48 --> 1251.44]  Is that kind of the focus there is trying to help people with their own personal assistant that's trained on them?
[1251.44 --> 1251.64]  Yeah.
[1251.70 --> 1253.76]  It's meant to, we don't use the word assistant.
[1253.86 --> 1254.08]  Okay.
[1254.30 --> 1255.54]  It's a little bit hierarchical.
[1255.98 --> 1256.14]  Yeah.
[1256.22 --> 1258.26]  We're just like, you know, it's not really an assistant.
[1258.66 --> 1260.34]  And so we were like, what if it was Robin?
[1260.40 --> 1261.52]  It was like your sidekick.
[1261.68 --> 1261.94]  Okay.
[1262.16 --> 1266.12]  You know, so like it's your AI sidekick that sort of works alongside you.
[1266.14 --> 1268.84]  And it's like, it's got your back, you know, it's like helping you out.
[1268.84 --> 1269.98]  That makes me Batman though.
[1270.16 --> 1271.34]  Are you in that analogy?
[1272.00 --> 1272.36]  Exactly.
[1272.54 --> 1274.06]  You're Batman and this is Robin.
[1274.22 --> 1274.36]  Yeah.
[1274.58 --> 1277.10]  Oh, dude, I'm feeling much better about this already.
[1277.50 --> 1277.52]  So.
[1278.20 --> 1278.42]  Yeah.
[1278.42 --> 1280.88]  I mean, you don't want to like belittle Robin, right?
[1281.04 --> 1281.88]  No, Robin's cool.
[1282.06 --> 1282.64]  We like Robin.
[1282.70 --> 1282.88]  Yeah.
[1283.00 --> 1283.48]  Robin's cool.
[1283.62 --> 1283.82]  Okay.
[1284.04 --> 1285.26]  So I get to be Batman.
[1285.44 --> 1290.32]  I got my Robin coming along and Robin's kind of, kind of helping me get the things done
[1290.32 --> 1292.20]  that I need doing a bit better.
[1292.20 --> 1297.40]  And is that really, do you find that I know we've been doing a lot of NLP the last few
[1297.40 --> 1300.04]  years, but it's still exploding outward.
[1300.18 --> 1302.98]  We're still having so much, you know, work in that, that area.
[1303.12 --> 1307.02]  Are there other aspects of it or does that kind of, is it really NLP focused?
[1307.12 --> 1309.88]  Do you have other algorithmic things that have to be considered?
[1310.04 --> 1312.72]  Is there any kind of reinforcement learning, anything like that, or is this doing it?
[1312.76 --> 1314.56]  I'm not trying to push you in other directions.
[1314.56 --> 1319.44]  I'm just wondering, is that large area of NLP really cover it fully in terms of what you're
[1319.44 --> 1320.14]  trying to achieve?
[1320.14 --> 1324.44]  Are there any gaps might be a better question in terms of like, what do you wish was there
[1324.44 --> 1328.00]  or something that you guys are exploring even outside the NLP space?
[1328.28 --> 1328.40]  Yeah.
[1328.56 --> 1333.60]  So there's a lot of discussion internally about supervised versus unsupervised learning
[1333.60 --> 1336.62]  and everything to date has been unsupervised.
[1336.82 --> 1340.74]  You're not telling the model or telling the IQ to do anything.
[1341.10 --> 1346.44]  And so we're trying to sort of figure out, does it make sense for Chris to say like,
[1346.60 --> 1348.18]  attaboy, like high five, you know?
[1348.44 --> 1349.52]  Get the feedback.
[1349.52 --> 1351.00]  Yeah, exactly.
[1351.44 --> 1356.70]  So we're trying to sort of sort through that now as far as like machine learning is concerned.
[1356.90 --> 1357.02]  Yeah.
[1357.24 --> 1361.32]  So it sounds sort of like a reinforcement thing where you have a reward that you're offering
[1361.32 --> 1363.22]  back to kind of steer it a little bit.
[1363.40 --> 1364.84]  And that would make a lot of sense.
[1365.16 --> 1365.40]  Yeah.
[1365.58 --> 1369.32]  You know, there's like sort of knowledge graphs that exist in the world.
[1369.60 --> 1370.76]  Obviously we're graphing the knowledge.
[1370.88 --> 1374.28]  So that's why I bring forth the phrase knowledge graph that exists.
[1374.28 --> 1377.06]  But, you know, they're all brute force.
[1377.06 --> 1382.28]  So it's you having to make those connections and then having to go back and sort of roam
[1382.28 --> 1385.72]  through those graphs and figure out what the connections might be.
[1386.46 --> 1390.28]  And I think the challenge with that is ultimately is scale.
[1390.28 --> 1397.82]  So let's say you get 10,000 or 200,000 documents in like to make those connections.
[1397.82 --> 1402.52]  Like we, our minds just aren't really capable of doing that, like to continue making those
[1402.52 --> 1402.94]  connections.
[1402.94 --> 1406.64]  So unsupervised is the route that we chose to take.
[1406.64 --> 1408.00]  And we're, yeah.
[1408.08 --> 1412.02]  And I think that's ultimately where Eureka moments can live because I'll give you another
[1412.02 --> 1412.36]  example.
[1412.52 --> 1416.20]  So let's say this is like an investor or an investment advisor.
[1416.36 --> 1418.98]  Let's, so let's say I'm the advisor, you're my client.
[1418.98 --> 1421.42]  And you're like, I have $2 million I want to spend with you.
[1421.50 --> 1427.40]  And I want to spend it on like battery technology and like innovative real estate business models
[1427.40 --> 1429.90]  for millennials and like, et cetera, et cetera.
[1430.06 --> 1433.18]  And so like, you're telling me this and I'm like, how am I going to filter that?
[1434.02 --> 1435.02]  Like, you know what I mean?
[1435.02 --> 1437.88]  Like these models don't have what you just told me.
[1438.06 --> 1438.20]  Right.
[1438.28 --> 1442.04]  So there's a way to use bundle to like support you in that.
[1442.12 --> 1448.54]  So let's, let's pretend that my company uses bundle and, you know, bundles graphed 2000 investment
[1448.54 --> 1449.00]  models.
[1449.14 --> 1452.46]  And I just start typing in battery technology and real estate and whatever.
[1452.46 --> 1457.52]  And I just click analyze and like semantically I'm like, where, oh, oh wow.
[1457.56 --> 1463.64]  I didn't even know that this like ESG like value, whatever is like a, you know, moderate
[1463.64 --> 1468.82]  risk and they have like, you know, elements on the periodic table, like, you know, whatever
[1468.82 --> 1470.28]  lithium and et cetera.
[1470.66 --> 1473.64]  So anyway, you know, that's another way to kind of create a eureka moment.
[1473.76 --> 1474.82]  You're like, wow, I had no idea.
[1474.90 --> 1478.64]  And I don't even know how I would search for that otherwise, other than just spending a
[1478.64 --> 1480.12]  lot of time trying to figure it out.
[1480.36 --> 1481.66]  I like the two use cases.
[1481.66 --> 1486.48]  And the first one, it's a business use case, but it's also very personal in that you're
[1486.48 --> 1489.62]  busy trying to, to draw on your own creativity.
[1489.94 --> 1494.84]  And then the second one, you're trying to pull different data points that aren't necessarily
[1494.84 --> 1498.98]  just obviously connected together in such a way to create the value that you're looking
[1498.98 --> 1499.28]  for.
[1499.46 --> 1504.32]  I'm curious as you, and I'm starting to see how that goes out and there's both a personal
[1504.32 --> 1505.32]  and a business side of it.
[1505.56 --> 1509.70]  Can you talk a little bit about what data points you're integrating at this point?
[1509.80 --> 1511.16]  I know you mentioned email and stuff.
[1511.16 --> 1514.88]  What all are y'all pulling together currently that you're publicly talking about that you're
[1514.88 --> 1520.66]  able to, and what should users that want to get into this know about the data that they're
[1520.66 --> 1521.60]  sharing and privacy?
[1521.82 --> 1523.50]  What are, you know, kind of some of the disclaimer stuff?
[1523.56 --> 1524.26]  Can you share some of that?
[1524.62 --> 1525.16]  Yeah, absolutely.
[1525.42 --> 1530.06]  So first and foremost, we have a, have a workspace where you can take notes.
[1530.18 --> 1535.10]  That's a really easy way to kind of prime the system is you can take notes and bundle
[1535.10 --> 1540.30]  IQ workspace, and we have an AI that sits in the editor and sort of, you know, as you're
[1540.30 --> 1543.34]  writing saying, Hey, you might want to check this out, check this out.
[1543.66 --> 1544.64]  So there's notes.
[1544.64 --> 1547.36]  And then we also are connecting with the G suite.
[1547.56 --> 1549.94]  So we've got connected Gmail so far.
[1550.10 --> 1551.92]  So the next one is Google Docs.
[1551.92 --> 1556.04]  Those are, you know, long form information that we graph out.
[1556.04 --> 1561.66]  And then we have a new one, which is a custom integration that we've created called books.
[1562.12 --> 1564.02]  So you can upload, imagine this, right?
[1564.18 --> 1565.00]  We've been testing it.
[1565.10 --> 1567.46]  We just uploaded all seven Harry Potter books.
[1567.76 --> 1568.10]  Oh, okay.
[1568.16 --> 1568.54]  That's good.
[1569.12 --> 1570.36]  You just won me over.
[1570.86 --> 1571.10]  Yeah.
[1571.22 --> 1571.92]  I like Harry Potter.
[1572.06 --> 1573.66]  It took like six minutes, right?
[1573.66 --> 1576.14]  So we graph all seven books in six minutes.
[1576.52 --> 1580.50]  So you can literally like, as you're taking notes or asking, you can ask questions and
[1580.50 --> 1582.18]  like query against all seven books.
[1582.18 --> 1584.80]  So let's say now maybe you're an academic, right?
[1584.92 --> 1589.34]  And you, or a student getting your MBA and like, you have to do all these research papers.
[1589.34 --> 1595.14]  So you just dump in a bunch of, you know, PDF white papers and like, it just changes your
[1595.14 --> 1599.82]  life because like you could just write your article and like, it's literally bringing you
[1599.82 --> 1601.88]  stuff from these white papers as you're writing.
[1602.32 --> 1602.86]  That sounds good.
[1602.92 --> 1603.48]  I like that.
[1603.62 --> 1610.66]  It sounds like you're really into some pretty cool use cases for these modern algorithms in
[1610.66 --> 1612.76]  NLP in terms of things you can do.
[1612.90 --> 1614.84]  You're really focused on creativity.
[1615.20 --> 1616.24]  I like that.
[1616.32 --> 1617.84]  And being able to kind of enhance.
[1618.06 --> 1622.02]  Do you feel like you're still just scratching the surface on what might be possible here?
[1622.54 --> 1626.88]  What are your thoughts on, do you have anything that you're able to share on any things that
[1626.88 --> 1629.44]  you'd like to do next, you know, building on where you're already at?
[1629.72 --> 1633.16]  It seems like a pretty cool, a pretty cool space to be in.
[1633.42 --> 1633.54]  Yeah.
[1633.56 --> 1634.50]  It's been a lot of fun.
[1634.50 --> 1639.10]  And I think the challenge always is like, what do you focus on next, right?
[1639.22 --> 1643.68]  Like you have to do something really, really well, solve a really well-defined problem first.
[1643.68 --> 1646.64]  And then you sort of land and expand from there, right?
[1646.96 --> 1651.98]  We started with notes and then email because people spend so much time in email.
[1652.06 --> 1656.54]  And we sort of give people this sidekick to support their knowledge work in email.
[1656.54 --> 1660.06]  But that is really like a mile wide and an inch deep, you know?
[1660.14 --> 1661.50]  So where do we go next?
[1661.50 --> 1663.80]  And we're still trying to figure that out.
[1663.88 --> 1665.82]  Like I would love to go in the medical space.
[1665.92 --> 1666.96]  I think that'd be really cool.
[1666.96 --> 1669.46]  But there's so many barriers to entry on that front.
[1669.68 --> 1673.90]  So like you're a doctor and, you know, maybe you see a thousand patients a year and you're
[1673.90 --> 1678.28]  like, you know, you see a rash on somebody's left arm and like something you've never seen
[1678.28 --> 1680.00]  before, but you get to describe it.
[1680.00 --> 1684.76]  And then you're tapped into some, you know, the broader data set that could potentially pull
[1684.76 --> 1687.50]  up, you know, anonymized people's notes.
[1687.50 --> 1691.26]  But like, I wouldn't know that it was Chris that had the other rash, but start to make
[1691.26 --> 1692.30]  those connections, right?
[1692.74 --> 1693.72]  That would be pretty cool.
[1693.72 --> 1697.24]  But where we went recently is the climate crisis.
[1697.74 --> 1704.04]  When the IPCC launched their global climate crisis report that came out recently, it was
[1704.04 --> 1705.36]  like 3000 pages long.
[1705.62 --> 1707.14]  You and I are not reading this report.
[1707.40 --> 1708.52]  Who's reading this report?
[1709.10 --> 1709.34]  No one.
[1709.34 --> 1715.00]  So like, how do we support climate literacy, you know, for policymakers?
[1715.78 --> 1718.02]  You know, I'm a millennial, like I care about the environment.
[1718.02 --> 1721.02]  I'm like, you know, I'm constantly thinking about like social good.
[1721.14 --> 1723.36]  I know, like you're a plant eater, right?
[1723.40 --> 1724.60]  Like you're socially conscious.
[1724.96 --> 1725.70]  Yeah, I'm a vegan.
[1725.92 --> 1729.40]  So anyone that's listened to me for a while sadly probably knows that about me.
[1729.56 --> 1734.74]  So how can we maybe support this massive data set that doesn't have a whole lot of history
[1734.74 --> 1735.34]  behind it?
[1735.40 --> 1737.76]  There's certainly a lot of dissonance between it.
[1737.76 --> 1743.10]  You've got these like attorneys and Congress and municipalities are going to be writing
[1743.10 --> 1747.40]  legislation and writing policies to like solve these problems that they don't really
[1747.40 --> 1748.32]  even understand.
[1748.54 --> 1752.90]  And it's no different than the infrastructure bill that's 1300 pages or however many pages
[1752.90 --> 1753.76]  I think that one is.
[1754.16 --> 1756.34]  So I think we want to kind of go deep on that.
[1756.44 --> 1760.78]  We've got a meeting with a large international law firm on Friday to talk about that.
[1760.86 --> 1761.92]  They're pretty excited about it.
[1762.04 --> 1767.04]  They work with a lot of cities, you know, and climate policy is something that's at the
[1767.04 --> 1767.40]  forefront.
[1768.04 --> 1769.38]  You know, we got to figure this out.
[1769.46 --> 1771.08]  There's a ticking clock against it.
[1771.26 --> 1772.62]  So I like that aspect.
[1772.80 --> 1777.98]  You know, we're talking about the business, but you clearly have a motivation that is very
[1777.98 --> 1781.78]  personal there in terms of trying to address a big problem.
[1781.78 --> 1788.80]  With kind of a new set of tools in the large that people are still just learning and understanding
[1788.80 --> 1794.96]  with these capabilities as you have been exploring new grounds with a new set of tools and really
[1794.96 --> 1800.78]  kind of trailblazing use cases, whether we're talking GPT-3 or other similar capabilities.
[1800.78 --> 1806.58]  Have there been any moments where you have been kind of going, I found a gap or I found
[1806.58 --> 1807.12]  something.
[1807.28 --> 1810.94]  Have these algorithms really solved everything in the use cases?
[1811.14 --> 1814.88]  Or do you struggle at times with saying, I'm missing a tool?
[1815.14 --> 1819.62]  I have a great toolbox with some good tools here, but there are, you know, I wish I had
[1819.62 --> 1820.90]  something that did X.
[1821.52 --> 1825.88]  Have you had any moments like that where you were trying to solve a well-defined problem,
[1825.88 --> 1830.14]  to use your words a moment ago, and you said, I need this thing that's missing from my toolbox
[1830.14 --> 1830.68]  right now?
[1830.78 --> 1831.40]  Has that come up?
[1831.64 --> 1831.88]  Yeah.
[1832.16 --> 1837.78]  I think in some ways, like, so speaking specifically to the model side of it, the AI side of it,
[1837.84 --> 1842.82]  I think there's a lot of room for improvement, but I don't know that the technology is there
[1842.82 --> 1843.06]  yet.
[1843.28 --> 1847.14]  And I think there's just going to be a lot of R&D that needs to be had.
[1847.32 --> 1848.76]  Part of it's like adoption, right?
[1848.76 --> 1855.88]  So like, you know, up until just a couple years ago, like we didn't have these AI assistants,
[1856.24 --> 1859.56]  like conversion AI and like these tools didn't really exist.
[1859.88 --> 1866.60]  And now as we're moving into this, like human centered AI software as a service enterprise,
[1867.02 --> 1870.64]  companies, they've got big budgets carved out for AI, but they don't even know how to
[1870.64 --> 1871.12]  spend it.
[1871.54 --> 1872.08]  Most of them.
[1872.42 --> 1872.98]  I've noticed that.
[1873.10 --> 1874.26]  They don't know what to do with it.
[1874.26 --> 1879.84]  So there's kind of a gap in time and maybe usability where there's going to be so much
[1879.84 --> 1881.78]  just learning, right?
[1881.88 --> 1888.20]  So we're, I mean, we are so far ahead of where the world is already in kind of this knowledge
[1888.20 --> 1889.72]  sidekick that we created.
[1889.94 --> 1891.86]  But I think there's just a lot of unknowns.
[1891.98 --> 1895.36]  I mean, yeah, I wish we could get a lot, maybe a little bit more horsepower out of what we're
[1895.36 --> 1897.96]  doing, but it's already pretty damn good.
[1897.96 --> 1903.20]  So we just got to basically find more use cases and make more revenues so that we can buy
[1903.20 --> 1905.68]  ourselves more time to do more things, you know?
[1905.90 --> 1910.76]  So you're kind of getting back to, you know, that imagination, that creativity, that innovation,
[1910.94 --> 1912.10]  doing what humans do well.
[1912.22 --> 1916.42]  So I want to ask you, as we finish up here, you've kind of talked a little bit about where
[1916.42 --> 1919.64]  we're at and kind of what the things look like a little bit going forward.
[1920.12 --> 1924.10]  Can you just, Daniel and I do this all the time, where we will try to make a prediction
[1924.10 --> 1928.36]  on how we think the world might look, or maybe how we want the world to look going
[1928.36 --> 1928.76]  forward.
[1928.88 --> 1932.08]  But beyond just the immediate future, where do you think this is going?
[1932.08 --> 1935.66]  What kinds of use cases might you be able to address?
[1936.24 --> 1939.32]  What kinds of tools do you think might evolve out of where we're at today?
[1939.82 --> 1945.44]  Where is this space going as someone who is constantly thinking about the future and about
[1945.44 --> 1949.88]  how to bring these amazing new capabilities into productive use?
[1950.14 --> 1952.08]  Where's the world going with this at this point?
[1952.48 --> 1955.52]  So I'm definitely not like the technical guy per se.
[1955.62 --> 1957.50]  Like I've never written a line of code in my life.
[1957.60 --> 1959.52]  I'm not sure you have to be technical on this one.
[1959.52 --> 1963.30]  This is really like, how is the world changing going forward from where you're sitting?
[1963.72 --> 1964.54]  And trust me, I hear you.
[1964.60 --> 1965.72]  And I'm going to get there.
[1965.98 --> 1969.30]  I'm going to start with by saying like, I went to a liberal arts school.
[1969.60 --> 1973.84]  Like I didn't go to MIT, didn't go to Harvard or any of these tech schools, Berkeley.
[1973.84 --> 1977.54]  And I'm like such a humanities, like history.
[1977.98 --> 1980.90]  Like I want to go to the opera or the symphony and like that, you know.
[1981.10 --> 1986.42]  And ultimately what I think might happen is because there's so many knowledge workers,
[1986.80 --> 1992.06]  I think humans, like individual knowledge workers will be able to own their IP.
[1992.48 --> 1996.84]  And I think that will bridge the wealth disparity, like the gap in disparity.
[1996.84 --> 2003.96]  If Chris and Nick, like if you owned your IP and you're able to own all of the knowledge
[2003.96 --> 2008.64]  that you put forth in terms of like moving these enterprises forward, and you were able
[2008.64 --> 2012.28]  to attribute that as like your unique fingerprint, so to speak.
[2012.56 --> 2020.22]  I think Bundle IQ has the propensity to basically like say that Chris is worth this because of
[2020.22 --> 2022.04]  all of the knowledge he's brought forth.
[2022.04 --> 2027.24]  And like you'll have your own fingerprint, your own ID, and maybe you'll be paid royalties
[2027.24 --> 2027.64]  on that.
[2027.74 --> 2032.42]  I don't know how you would renegotiate your salary, but like essentially you would get
[2032.42 --> 2036.30]  paid dividends on like what you've been able to contribute within an enterprise.
[2036.94 --> 2042.98]  So by having the technology that we're using in terms of going forward gives me the ability
[2042.98 --> 2045.76]  to maintain IP that I create.
[2045.96 --> 2051.40]  And then you kind of just need a business model for how that works in terms of finding the value
[2051.40 --> 2053.86]  or other people finding the value from you and stuff going forward.
[2054.20 --> 2054.38]  Yeah.
[2054.48 --> 2058.92]  It's a beautiful idea in terms of it's very liberating in terms of the, you know, what
[2058.92 --> 2060.22]  it might imply going forward.
[2060.56 --> 2061.28]  Well, think about it.
[2061.44 --> 2066.92]  If we've bundled all of your knowledge, then the company, the organizations or multiple companies
[2066.92 --> 2073.08]  of your contract that you've contributed to, like there's transparency now on what you've
[2073.08 --> 2074.50]  been able to bring to the table.
[2074.92 --> 2078.04]  And you're able to basically have like a fingerprint.
[2078.04 --> 2082.12]  Like if you write an email to me, I would know that Chris wrote the email because of
[2082.12 --> 2084.32]  all the emails that Chris has ever written.
[2084.48 --> 2084.94]  That makes sense.
[2085.22 --> 2088.60]  If you wrote a marketing document, I would know that Chris wrote the marketing document
[2088.60 --> 2091.34]  at like a very high percentage of accuracy.
[2091.74 --> 2092.08]  Understood.
[2092.38 --> 2096.62]  So that's what I mean by like vectorizing and bundling your IQ and your knowledge.
[2096.78 --> 2097.06]  Gotcha.
[2097.34 --> 2102.40]  And potentially like you're a walking, talking digital wallet of Chris's like intellectual
[2102.40 --> 2106.66]  property that you could contribute somewhere else or just get paid on for everything that
[2106.66 --> 2108.92]  you've always contributed, already contributed rather.
[2109.44 --> 2111.10]  That is pretty inspiring right there.
[2111.30 --> 2112.96]  On that note, I'm just going to say that.
[2113.02 --> 2114.96]  Yeah, I can't think of anything that tops that.
[2115.38 --> 2117.90]  Thank you very much, Nick, for coming on the show.
[2118.02 --> 2119.40]  It's been a fascinating conversation.
[2120.00 --> 2123.70]  You've definitely given me something to think about here in terms of what that would mean.
[2123.80 --> 2124.60]  Very cool endeavors.
[2124.80 --> 2125.26]  Thanks a lot.
[2125.44 --> 2125.80]  Thank you.
[2125.88 --> 2126.64]  Thanks for having me.
[2126.82 --> 2128.08]  And give Daniel my regards.
[2128.30 --> 2128.66]  Will do.
[2128.80 --> 2129.20]  Thank you.
[2129.36 --> 2129.58]  Cheers.
[2133.14 --> 2134.16]  That's our show.
[2134.38 --> 2135.00]  Thanks for listening.
[2135.00 --> 2137.84]  For more like this, check out our master feed.
[2138.18 --> 2141.90]  It is all Changelog podcasts in one easy to consume place.
[2142.26 --> 2146.92]  Let your podcast app snag everything we produce and then pick and choose which ones to listen
[2146.92 --> 2147.12]  to.
[2147.48 --> 2152.34]  Subscribe today at changelog.com slash master or just search for Changelog Master in your
[2152.34 --> 2153.48]  podcast app of choice.
[2153.74 --> 2154.30]  You'll find it.
[2154.82 --> 2159.54]  Special thanks to Breakmaster Cylinder for providing our music and to our longtime sponsors,
[2159.94 --> 2161.78]  Fastly, LaunchDarkly, and Linode.
[2162.32 --> 2163.62]  That's all for this week.
[2163.62 --> 2165.14]  We'll talk to you next time.
[2165.14 --> 2166.08]  Bye.
[2188.08 --> 2189.20]  Bye.
[2189.20 --> 2189.56]  Bye.
[2189.58 --> 2189.78]  Bye.
[2189.78 --> 2190.06]  Bye.
[2190.06 --> 2191.26]  Bye.
[2191.26 --> 2191.46]  Bye.
[2191.46 --> 2191.54]  Bye.
[2191.56 --> 2192.08]  Bye.
[2192.08 --> 2194.08]  K-9
