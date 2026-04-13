[0.00 → 6.66] reinforcement learning in general is not like a model. It's a framework in which you can train
[6.66 → 13.10] agents or models. And if you think of self-driving car or something like that, if you say, I'm going
[13.10 → 17.64] to go from point A to point B in a self-driving car, well, there's a bunch of routes you
[17.64 → 23.42] could take. It's not really that there's one perfect solution to that problem. It's more about
[23.42 → 29.98] the decisions you make along your route based on what you've done so far and the feedback that
[29.98 → 31.36] you're getting from your environment.
[34.58 → 39.02] Big thanks to our partners, Linde, Vastly, and Launch Darkly. We love Linde. They keep it fast
[39.02 → 44.44] and simple. Check them out at linode.com slash changelog. Our bandwidth is provided by Vastly.
[44.80 → 49.36] Learn more at Fastly.com and get your feature flags powered by Launch Darkly. Get a demo at
[49.36 → 55.02] LaunchDarkly.com. This episode is brought to you by our friends at Rudder stack, and we're calling all
[55.02 → 58.92] data engineers to check out Rudder stack Cloud and start building smart customer data pipelines.
[58.92 → 64.64] Rudder stack is warehouse first, no more silos. Rudder stack builds your customer data lake on
[64.64 → 69.86] your data warehouse, not theirs, enabling all functionality of a CDP with more security and
[69.86 → 75.96] retaining full ownership of your data. It's open source and API first. Rudder stack can be easily
[75.96 → 80.16] integrated into your existing development processes and because they're open source,
[80.42 → 84.30] you can see all their code so you don't have to worry about vendor lock-in or black boxes.
[84.86 → 88.86] And best of all, they have transparent pricing. Stop paying your CDP a premium to store your data.
[88.92 → 94.22] Rudder stack is free up to 500,000 events and pricing scales transparently from there.
[94.64 → 102.94] Learn more and get started at Rudderstack.com. Again, Rudderstack.com. That's R-U-D-D-E-R-S-T-A-C-K.com.
[102.94 → 117.62] Welcome to Practical AI, a weekly podcast that makes artificial intelligence practical,
[117.94 → 122.94] productive, and accessible to everyone. This is where conversations around AI, machine learning,
[123.04 → 127.64] and data science happen. Join the community and Slack with us around various topics of the show
[127.64 → 131.92] at changeodd.com slash community and follow us on Twitter. We're at Practical AI.
[138.36 → 145.70] Well, welcome to another fully connected episode of Practical AI. This is where Chris and I keep you
[145.70 → 151.50] fully connected with everything that's happening in the AI community. We'll take some time to discuss
[151.50 → 157.54] the latest AI news, and we'll dig into some learning resources to help you level up your machine
[157.54 → 163.70] learning game. I'm Daniel Whiten ack. I'm a data scientist at SIL International. Furthermore, I'm joined as
[163.70 → 168.74] always by my co-host, Chris Benson, who is a tech strategist at Lockheed Martin. How are you doing,
[168.82 → 169.00] Chris?
[169.32 → 175.78] I am very well, Daniel. Looking forward to diving into some of today's topics. And as you will explain to
[175.78 → 178.26] the audience, we get to put you on the hot seat just a little bit today.
[178.26 → 185.82] A little bit. Yeah, yeah. Talk about some of the things in my life. But yeah, it's exciting. Lots
[185.82 → 194.40] of exciting things going on as we wrap up what is the last weeks of 2021. That seems like it went
[194.40 → 196.66] by fast. I don't know if it did for you.
[197.06 → 203.24] It has gone by incredibly fast. The last two years, just craziness. It's just like, where did they go?
[203.42 → 208.06] But you know what? We got some new things happening here, some new things to talk about that you can
[208.06 → 208.80] guide us through.
[208.80 → 215.86] Yeah. So I think maybe one of the things that we can talk about, which we've talked about several
[215.86 → 224.24] times on the show and has been a sort of developing theme that we visit occasionally, is GPT-3 and the
[224.24 → 235.74] OpenAI APIs. I don't know when you saw this, but recently I saw how OpenAI recently made their API
[235.74 → 242.84] available with no waitlist. So previously you had to sort of apply on a waitlist. They would approve
[242.84 → 249.58] you, and then you could use some of their models. And I think originally, even when we first talked
[249.58 → 257.68] about GPT-3, they released it, and it was fairly closely guarded. I think mostly because of what they
[257.68 → 263.28] considered, you know, they considered, you know, a safety process and making sure that people didn't
[263.28 → 270.68] misuse the model in certain ways. And I think based on the blog posts where they talk about, you know, them
[270.68 → 278.24] opening up some of the availability, they emphasize a lot of this kind of safety features that they have
[278.24 → 279.14] put in place.
[279.14 → 284.94] And that might be actually, before we dive into it, that might be a good place to start is why. For those
[284.94 → 292.76] who are not already very familiar with it, why would this model that they've released need all of this
[292.76 → 298.88] careful vetting and slow rollout and such? Because it's been quite a while since they did it. So you want
[298.88 → 299.88] to talk toward that a little bit?
[300.18 → 306.16] Yeah, I think it's probably, first, I'm not speaking for OpenAI, but I think in general,
[306.16 → 313.90] what people's thought process is around these types of models is that GPT-3, just kind of stepping
[313.90 → 321.60] back, is a sort of large-scale language model that enables a variety of natural language processing
[321.60 → 328.08] tasks to be performed. And some of those, for example, like natural language generation,
[328.94 → 335.38] are very, performance is very impressive from GPT-3. So one thought is, well,
[335.38 → 344.96] GPT-3 could be used to do sort of malicious things like to create a bunch of fake news type of stuff,
[345.40 → 354.54] misinformation, sort of distribute a lot of this kind of thing. As well, GPT-3 was trained on a huge
[354.54 → 362.12] amount of data that, you know, was kind of crawled from the internet and other places. And I think the
[362.12 → 368.30] behaviour of the model, because, you know, all the biases and other things that exist in that kind
[368.30 → 374.58] of large corpus aren't totally probed out. So another question is, like, how are biases showing
[374.58 → 379.84] up in this data? And, you know, if we just say, hey, everyone use this thing to generate text or
[379.84 → 387.00] integrate it in their applications, they might not take that sort of caution in mind if they're just
[387.00 → 392.86] kind of applying it wholesale across the board. Yeah. And just to name at least the nine categories
[392.86 → 399.26] without all the detail, they note that they prohibit users from knowingly generating or allowing
[399.26 → 404.26] others to knowingly generate with the account the following categories of content. There's nine.
[404.82 → 413.26] They are hate, harassment, violence, self-harm, adult, political, spam, deception,
[413.26 → 419.70] and malware. And apparently they have spent a fair amount of effort putting the safeguards around
[419.70 → 425.06] this so that it can do. It'll be interesting to see whether going forward, they're able to
[425.06 → 430.06] put safeguards around other models they release much faster now that they've kind of got some,
[430.34 → 435.06] the infrastructure in place. So it might speed up the ability to get onto new models. Because this has
[435.06 → 440.72] been, I mean, how long has it been now? Maybe a year and a half? It's been quite some time. Yeah. So
[440.72 → 445.76] it's interesting. I mean, they put a lot of thought process into this and I mean, they're to be
[445.76 → 453.48] commended for leading a lot of the thought around these areas. I think there are different views on how
[453.48 → 459.92] the community should go about addressing these things and whether it should be via a an access
[459.92 → 468.50] controlled API or via open source code and models and datasets or, you know, however it should be,
[468.50 → 476.04] be approached, but they have put a lot of thought into this. They talk about in the blog post, how they
[476.04 → 482.78] are putting things in place to review applications. So applications of the model applications of the AI
[482.78 → 490.98] before they go live monitoring those applications for misuse and, you know, supporting better supporting
[490.98 → 497.98] applications as they scale and, and understand the effects of the technology. So very interesting
[497.98 → 505.26] developments here from open AI. Chris, have you logged in and tried anything with the open AI
[505.26 → 510.86] playground or anything like that? I've just gotten an account now that they've opened it up. I am ready.
[511.08 → 517.64] So what I'm going to look for you to help me get into this. I have my, I have my brand-new account.
[517.78 → 524.12] I have the site that they send you to open where it says, welcome to open AI, start with the basics.
[524.12 → 530.14] I'm looking at their examples, have open AI codecs open. And by the way, for our listeners out there,
[530.44 → 534.68] this might be a good moment. If you don't already have the account, pause the podcast for a second,
[534.86 → 539.16] go grab an account and follow along with us. If you're not driving in the car or something.
[539.32 → 544.14] And I would love, I know Daniel, you've been working with this for some time. If you could kind of guide
[544.14 → 548.70] us through a little bit about what to see, you know, I know you're a practitioner, you're not with open AI,
[548.70 → 554.10] but as someone who has used it, if you can maybe give us a little boost on things that you've already
[554.10 → 560.46] learned, that would be fantastic. Yeah. So we can maybe just kind of look at some of the basic
[560.46 → 565.40] functionality that you can do here. And I mean, there's, you can do a lot of things. So this is
[565.40 → 574.46] by no means a complete introduction, but if you kind of log into the API interface, one really nice
[574.46 → 580.08] thing is that they do give a kind of big blocks that give you introduction and examples. So you
[580.08 → 585.96] can scroll through those, but they have this cool thing called the playground. So they have documentation
[585.96 → 591.22] examples, and then they have the playground. Ultimately, you can use the API in a variety of
[591.22 → 597.22] ways, including like a REST type interface, but they built this kind of playground to help you try out
[597.22 → 602.62] things and see like, what are the types of things that I could do and what's applicable to my specific
[602.62 → 612.02] use case. So if you, if you click on the playground, it kind of opens up this essentially a text box.
[612.24 → 618.82] The most basic of things that you could do is just start typing. You know, I could say Chris
[618.82 → 629.58] Benson is really cool. Oh, and knows. I thought no deception. Remember about AI? Yeah. So Chris Benson is
[629.58 → 635.76] really cool. And knows a bunch about AI. And then I could click generate, and it's going to start
[635.76 → 643.20] generating a bunch of text. So, so, so yeah, I don't know if you want to hear what it generated as a
[643.20 → 648.36] result of that, Chris. Uh, it's, so I put in Chris Benson is really cool and knows a bunch of AI.
[648.36 → 652.94] Oh, and then it started, it started saying, I said, I think he's still a bit of a newbie,
[652.94 → 659.62] but he's learning fast. This is his first post. Enjoy it. I, and then it goes on. I've been playing
[659.62 → 665.76] with this new stuff called machine learning lately, and I found it rather fun. What I'm going to talk
[665.76 → 670.48] about today. So you can keep, you know, clicking that button, and it's going to generate more and
[670.48 → 675.56] more of Chris Benson's new blog post about machine learning and how he's finding it rather fun.
[676.20 → 681.30] Oh boy. I was about to put yours in, but since you put such an unrealistic thing about me,
[681.30 → 688.10] I just put in, there was a guy named Chris who had nine dogs. And, uh, I started with that.
[688.10 → 694.72] It took an interesting path. It says he wanted to go for a drive in his new car, a 67 Ford Mustang.
[695.02 → 700.24] It was a nice car, and he was proud of it. He asked his neighbour if he could borrow his dog for a few
[700.24 → 706.40] minutes. The neighbour said, sure. Take him for a few minutes. Chris went to the garage. So that's what
[706.40 → 712.42] I had. Uh, so this is, this is fun. This is a, I have a feeling this is going to turn into my favourite
[712.42 → 718.28] Saturday night with a drink or two, not too many, of course, because we're responsible and no driving,
[718.42 → 724.38] but yet this might be the new game with friends on a Saturday night thing to do after a beer or a glass
[724.38 → 730.26] of wine. Yeah. But I mean, you can see, and I think the interesting thing is that there's a number of
[730.26 → 735.48] things that you can tweak here, right? Along the right-hand side of the playground, you can change the
[735.48 → 741.60] different sort of engines that are available to do this, but then also kind of response length.
[741.84 → 749.36] You can change various, uh, kind of parameters, hyperparameters about what's going on, and you can
[749.36 → 755.60] show probabilities or not. So there's more here that you can get. And a cool thing is to you that
[755.60 → 762.08] similar to like, uh, like if you were writing rest API calls or testing them in postman, you can
[762.08 → 768.28] generate code to make that call here in this playground. It's similar. You can actually
[768.28 → 775.48] generate code. So if you click on view code, you can then see, Hey, here's the Python code that will
[775.48 → 783.56] actually call the open AI API and get the similar response from the engine. And that way you can sort
[783.56 → 789.34] of integrate. So it's telling you how to integrate this sort of text completion into an application.
[789.34 → 795.82] And you can, you know, go down and see how to do that with Python or just calling a rest API,
[796.04 → 800.96] which is pretty cool. Yeah. Or rest API or curl. Yeah. So they give the JSON and the curl.
[801.22 → 806.04] Yeah. Now the interesting, so this is cool. The text completion thing is cool, but I think the
[806.04 → 813.68] maybe more interesting thing, at least for our team and how we've looked at models like these is that
[813.68 → 821.84] they can be quickly adapted to a very specific task that you are more interested in than maybe
[821.84 → 828.34] just kind of general text completion. So if you look, if you're in the playground, and you look at,
[828.50 → 831.20] there's a little dropdown called load a preset. Okay.
[831.46 → 839.46] You could load, for example, a Q and a preset. That's the first one that pops up for me. And you'll
[839.46 → 847.42] see what happens is the playground will sort of pre-fill a little bit of example data for the model.
[848.04 → 853.96] So it's giving a sort of pattern. You can kind of think about this like a very small amount of prompt
[853.96 → 862.44] data or a very kind of few shot example type of thing where you're giving just a little bit of
[862.44 → 866.92] warm-up to the model to tell it, hey, this is the sort of thing that I want to generate.
[866.92 → 873.50] Right. And so when you pull up the Q and a thing for those that are listening, there's a Q colon
[873.50 → 880.62] and there's a question and then an A colon answer, right? Q colon question, A colon answer,
[880.78 → 886.44] Q colon question, you know, A colon answer. And it provides a bunch of these answers. So
[886.44 → 892.62] the model all of a sudden is realizing, oh, it wants me to generate things that are like Q colon
[892.62 → 901.12] some question and A, give me the answer. And so now at the bottom, you can type in a new question.
[901.36 → 905.42] So we just recorded an episode about federated learning. So I'm curious if it knows what that
[905.42 → 911.26] is. So I'm going to say, what is federated learning? Question mark. And I'll generate.
[912.04 → 918.90] And it says federated learning is a machine learning technique that allows a single machine to learn
[918.90 → 925.08] from multiple sources of data, which is actually quite relevant. How did it know how to do that?
[925.18 → 930.44] Well, it's trained on a bunch of text data from the internet and, you know, the world,
[930.72 → 935.14] right? So at some point it maybe knows something about that or has been prompted.
[935.58 → 939.16] I just want to share with you what I put in while you were doing that. I put in for question,
[939.66 → 946.82] what is GPT-3? And the answer was, GPT-3 is a question answering system developed by IBM.
[946.82 → 952.70] Well, they should work on that. They might. Maybe we should switch over to the IBM Watson API.
[955.10 → 960.84] This is a lot of fun. And actually you could scroll through these. You'll actually see there's
[960.84 → 969.38] examples that they give for summarizing text or text to a command or parsing unstructured data or
[969.38 → 976.52] classification. And so it basically gives you an example of, hey, this is the way that you can sort
[976.52 → 984.96] of prompt GPT-3 in order to have it do a new sort of task for you. We've used this for kind of some
[984.96 → 992.54] data augmentation type things. So where we've wanted to generate data in a certain way for a
[992.54 → 998.42] purpose and actually use GPT-3 to kind of help us generate that data. And that's been very helpful
[998.42 → 1008.06] for us. So that's kind of maybe a general rundown of what is GPT-3 and why you might want to check it
[1008.06 → 1008.22] out.
[1008.32 → 1013.04] Yeah. Just to call out some of the things in that dropdown, there's chat, there's Q&A, which we
[1013.04 → 1019.68] talked about, grammatical standard English summarized for a second-grader, text to command, English to
[1019.68 → 1026.06] French, parse unstructured data, and classification. And then it has a more example section. But yeah,
[1026.06 → 1028.48] it looks good. I'm looking forward to diving into this.
[1040.48 → 1046.10] This episode is brought to you by me, myself, and AI. It's a podcast on artificial intelligence
[1046.10 → 1051.22] and business. And it's produced by our friends at MIT Sloan Management Review and Boston Consulting
[1051.22 → 1055.92] Group. And the question is, why do only 10% of companies succeed with artificial intelligence?
[1056.06 → 1061.00] That's the question they aim to answer with this podcast. Each episode, Sam Ransbotham and
[1061.00 → 1065.92] Sherwin Contraband talk to AI leaders from organizations like NASDAQ, Spotify, Starbucks,
[1066.26 → 1071.20] and IKEA. And as you'll hear the show discusses tough topics like bias and AI.
[1071.40 → 1078.00] We've built technological safeguards and prods. Some of it is actually having the technology prompt the
[1078.00 → 1084.90] human and say, hey, you're building a model. You have identified that maybe you don't want race
[1084.90 → 1089.08] as a variable in this model because it can introduce bias. But we see here you have a
[1089.08 → 1094.94] field that is zip code. And zip code can be highly correlated with race. There's a very human element
[1094.94 → 1101.18] to this question. But to address it at scale, you actually need to automate the solution as well.
[1101.72 → 1105.86] All right. Me, myself, and AI is a collaboration between MIT Sloan Management Review and Boston
[1105.86 → 1110.78] Consulting Group. It's available wherever you get your podcasts. Just search me, myself, and AI.
[1135.86 → 1145.80] Well, Chris, Hugging Face continues to be the darling of the AI world. Does it not?
[1145.80 → 1146.34] It does.
[1146.46 → 1153.68] New things all the time. Cool stuff. I've seen a couple of things come out from Hugging Face
[1153.68 → 1159.74] recently. So for those maybe listeners who are new to the AI community or aren't familiar,
[1159.74 → 1171.06] Hugging Face is an AI company and actually has a whole host of things that are quite relevant to AI
[1171.06 → 1176.54] development and research and application. One of those being a model hub where you can get models
[1176.54 → 1181.60] actually of all types. Now it started with natural language processing models, but now it has vision
[1181.60 → 1188.36] models and speech models. It has data sets that you can pull. It has spaces where you can host
[1188.36 → 1194.48] machine learning applications. It has an accelerated inference API where you can serve inferences from
[1194.48 → 1200.62] your models. And you can kind of think about this almost like, you know, people post their code to
[1200.62 → 1208.64] GitHub. People post their software containers to Docker Hub. You can post models and data sets to
[1208.64 → 1215.72] Hugging Face's Hub, and those can be public or private. And so you can version your models and data sets
[1215.72 → 1221.22] there and serve your models and data sets there for your company. So it's really kind of a it's becoming a
[1221.22 → 1230.92] one-stop shop for a bunch of really useful AI tooling. At least that's kind of how I'm starting to see it.
[1231.34 → 1238.72] That's totally right. Hugging Face is one of the names in the AI world that everybody respects and everybody
[1238.72 → 1244.64] recognizes. They just keep doing innovative things that are cool and they're super user-friendly.
[1245.32 → 1250.42] And so it's, they're kind of the go-to, one of the go-to in this space that you are always going to be using.
[1250.80 → 1259.56] Yeah. And one of the things that came out recently, which is really exciting, is a first ML agents
[1259.56 → 1263.52] reinforcement learning environment on Hugging Face.
[1263.84 → 1265.22] Called Snowball Fight.
[1265.22 → 1272.06] Oh yeah. Yeah. I mean, very relevant for the Christmas holiday season, right? Is Snowball Fight.
[1272.22 → 1277.68] Maybe people are in some place where you don't have snow. You can now have a snowball fight on
[1277.68 → 1282.26] Hugging Face. What was your first impression when you saw, when you saw this, Chris?
[1282.40 → 1286.64] I'm playing with it, right? I'm loading it up as we speak and it is cool. Good names,
[1286.78 → 1292.14] good graphics. And I am trying to load up the Snowball Fight demo here right now.
[1292.14 → 1297.84] Yeah. I was playing it a bunch earlier and had some fun. If you load into it, you can actually
[1297.84 → 1302.58] play the game interactively. So just to give people a sense of what we're looking at,
[1303.06 → 1311.24] you sort of load into it. It loads this interface where a game comes up and that's kind of driven by
[1311.24 → 1318.52] Unity. And you can move around this little guy in a snowball sort of field and throw snowballs at
[1318.52 → 1322.30] another avatar on the other side. It's a lot of fun.
[1322.54 → 1327.64] The music's playing in my earphones just so that you know. So, you know, you have a soundtrack going.
[1327.94 → 1328.16] Festive.
[1328.48 → 1332.38] Yeah. Oh boy. This is fun. Okay. Since nobody can see what I'm doing, I'll stop.
[1332.74 → 1334.80] Now we know what Chris is going to do the rest of the day.
[1334.92 → 1339.22] Oh, this is it. This is taking over. So don't let my boss know that I'm onto this.
[1339.22 → 1345.38] Well, one cool thing is I think we do have scheduled to have Thomas from Hugging Face who
[1345.38 → 1351.92] created this in an upcoming episode. So we'll dive into it more then. But I wanted to mention it here
[1351.92 → 1358.08] because I think it's cool that Hugging Face sort of made this transition. I mean, at first really
[1358.08 → 1364.76] centred around chat interfaces and then more broadly like open source NLP.
[1364.76 → 1374.78] Yep. And then kind of into open source and kind of general purpose AI tooling and, you know,
[1374.90 → 1382.54] hosting services. And now we see this reinforcement learning piece coming in where the goal is that
[1382.54 → 1389.48] within Hugging Face itself, you'll be able to kind of build and share reinforcement learning environments.
[1389.48 → 1397.38] Now, Chris, I know that we've talked about it a little bit in the past. Reinforcement learning in general is not like a model.
[1397.62 → 1405.22] It's a framework in which you can train agents or models. And if you think of self-driving car or something like that,
[1405.32 → 1411.70] if you say I'm going to go from point A to point B in a self-driving car, well, there's a bunch of routes you could take.
[1411.70 → 1426.66] Right. And it's not really that there's one perfect solution to that problem. It's more about the decisions you make along your route based on what you've done so far and the feedback that you're getting from your environment.
[1426.66 → 1432.44] And so in order to train an agent to execute decisions in that environment or make actions in that environment,
[1432.44 → 1438.90] you need to have a sort of simulated environment that will allow an agent to navigate in that environment,
[1439.16 → 1447.50] get feedback and rewards, and then be trained accordingly to operate in that environment, in this case, to win a snowball fight.
[1447.50 → 1463.50] So that's ultimately, although the game is interesting, that's ultimately the most interesting thing about this is that it provides a route towards training reinforcement learning agents in environments that are shared on Hugging Face.
[1463.86 → 1470.58] It's a powerful approach. And at a previous company, back when deep reinforcement learning was still fairly new,
[1470.98 → 1476.82] we were using it for training robots on our team at this other place and was perfect there.
[1476.82 → 1482.10] It's used in video games. It's used in the industry I'm in now in a nonspecific way.
[1482.26 → 1488.08] It's used to move all sorts of things we call platforms, things that move around and do things.
[1488.50 → 1493.00] And that's how we get autonomy to work these days. I mean, it is a fantastic tool.
[1493.54 → 1497.62] There is one that I think is worth calling out that was a DARPA. It's a public DARPA thing.
[1497.76 → 1503.04] And DARPA, it's an interesting place. It is the Defense Advanced Research Projects Agency.
[1503.04 → 1510.68] And they do all sorts of government-oriented and military-oriented experimentation, very cutting edge.
[1511.14 → 1514.48] And about a year ago, they did something called Alpha Dogfight.
[1514.58 → 1519.46] And I know I've brought it up in the past, but they, in a simulated environment,
[1519.94 → 1525.20] they trained a model to be able to do dogfighting against other models.
[1525.76 → 1526.58] Like in planes.
[1526.78 → 1528.12] Like as in airplanes. Right.
[1528.12 → 1531.62] I'm really glad you said that, just to be very, very clear.
[1531.98 → 1535.92] I didn't want people to think about like robot dogs fighting each other.
[1536.32 → 1539.04] Yeah. We're talking about, think of the movie Top Gun.
[1539.26 → 1543.68] Okay. That kind of dogfight, like pilot, Tom Cruise, all that kind of stuff.
[1543.72 → 1544.70] Not the same plane though.
[1545.10 → 1546.14] And they trained them.
[1546.14 → 1551.72] And so, and at the end of it, this was not the Navy, which is what Top Gun is, but the weapons school,
[1551.94 → 1558.08] which is the equivalent of Top Gun in the United States Air Force, they had a weapons school instructor.
[1558.28 → 1563.88] This would be like the equivalent of the instructors at Top Gun go up against the model.
[1564.00 → 1569.08] And the model demolished the instructor over and over and over again.
[1569.08 → 1581.46] And so you're talking about one of the best fighter pilots in the world, period, getting demolished by the simulated AI that was based on deep reinforcement learning, beating it in the simulator.
[1581.80 → 1584.56] They were using a real, I believe it was an F-16 simulator.
[1585.10 → 1587.40] I watched the whole thing live, and it was just amazing.
[1587.56 → 1591.58] So this is some pretty cool technology here, and it's evolving rapidly.
[1591.58 → 1607.62] But I think one of the things that I've always wondered as related to reinforcement learning is like you see the power of that, but then you see how hard it is to create these environments in which you need to train the reinforcement learning agent.
[1607.80 → 1611.28] So in order to train a reinforcement learning agent, you kind of have two choices.
[1611.28 → 1615.92] You can either like to train the agent in the real world scenario.
[1615.92 → 1620.58] Like if you're training something that's going to fly a plane, that's not very practical, right?
[1620.66 → 1624.96] Because you're going to crash a bunch of planes and maybe kill some civilians.
[1625.28 → 1626.04] People don't like that.
[1626.14 → 1628.60] So you have to create this sort of simulated environment.
[1629.06 → 1641.38] However, creating that is actually, I mean, it's not my core competency in terms of like 3D environments and like unity and games and simulation and all that stuff.
[1641.38 → 1657.36] So I think the idea that there could be a place in which these environments are created and shared more broadly on Hugging Face to enable kind of people to share things, modify them, update them, train agents on them.
[1657.42 → 1669.74] I think it's a fascinating concept because I wouldn't personally, it would be hard for me to know where to start in creating this sort of environment if I didn't have a good way to kind of jump off.
[1669.74 → 1682.32] So to generalize on that a little bit, it's a great way of accomplishing this in any kind of environment or industry that where the cost of that training would be prohibitively expensive.
[1682.50 → 1686.72] You know, you mentioned where you don't want to crash planes a thousand times and all the damage.
[1687.22 → 1688.96] Another area would be medicine.
[1688.96 → 1699.88] If you want to try new surgeries or alter surgeries and carry procedures forward, and you don't want to kill patients in the process, this is an area where you can use deep reinforcement learning for that.
[1700.20 → 1704.58] There are so many areas out there that are just very expensive to do that.
[1704.66 → 1708.74] And I don't mean just financially expensive, but, you know, loss of life and things like that.
[1708.74 → 1711.32] So it's, you're seeing it all over the place.
[1711.46 → 1712.68] You're seeing it more and more.
[1712.74 → 1721.48] And I think simulation is going to become ever more a part of businesses getting done what they are, organizations in general, getting done the things that they're trying to get done.
[1721.48 → 1731.20] So one more thing that I wanted to mention from Hugging Face just before we're moving on, they've had a couple of releases that are quite interesting.
[1731.42 → 1739.48] The other one I wanted to mention was what they're calling a data measurements tool, which is an open source project.
[1740.28 → 1742.52] This just was released as well.
[1742.60 → 1744.56] And you can kind of look through it.
[1744.56 → 1759.50] The data measurements tool, they say, is an interactive interface and open source library that lets data set creators and users automatically calculate metrics that are meaningful and useful for responsible data development.
[1760.06 → 1772.16] And so you can kind of, you know, this is new enough that I haven't dug into it, but I think this does certain things, everything from kind of basic things that you might expect from exploratory data analysis,
[1772.16 → 1784.30] like figuring out missing values and descriptive statistics, all the way to analyzing biases in data sets, maybe related to particular factors like gender or other things.
[1784.30 → 1801.62] And so I think ultimately what they're trying to do here is create a nice way for people that are maybe using data sets off of Hugging Face's data sets hub or creating new data sets to really understand a little bit more about them and document them a little bit better.
[1801.62 → 1808.78] So that people aren't just kind of pulling whatever data set looks good without understanding the implications of that.
[1808.94 → 1811.28] So it's a pretty cool route that they're going, I think.
[1811.54 → 1818.70] Even as we're talking, I'm looking through some of the like the graphs they have that do analysis on the data sets that they're offering.
[1818.84 → 1822.88] I mean, the one that I'm in right now is hate speech 18.
[1823.20 → 1825.82] And you can go explore things like that.
[1825.82 → 1828.90] So it's interesting in a bad way.
[1829.20 → 1830.92] Things I definitely wouldn't want my child to do.
[1830.96 → 1834.82] It kind of gives you all these different ways of analyzing and measuring.
[1835.00 → 1836.78] So very, very cool technology.
[1836.88 → 1839.94] A tool that is long overdue now that it's here.
[1840.12 → 1842.24] I mean, all kudos to them for doing it.
[1842.52 → 1843.76] Wish I'd had this for a while.
[1844.08 → 1848.48] So, you know, it's funny, Daniel, as we look at some of these tools right now,
[1848.48 → 1854.44] it feels like this industry is maturing a little bit in terms of not just having...
[1854.44 → 1855.92] Yeah, we have nice tools now, right?
[1855.94 → 1860.38] Yeah, not just having the models, but having some of the tooling we need around it to make it safe
[1860.38 → 1864.50] and get to what you need to get to for a good output without some of the missteps.
[1864.50 → 1894.48] We'll see you next time.
[1894.50 → 1898.72] Sherwin taught to leaders that are engaged in the theory and the practice of AI.
[1899.18 → 1900.86] I remember one project we had.
[1901.34 → 1903.08] We were training a chatbot.
[1903.68 → 1908.10] And it turned out we used raw, you know, logs, all privacy assured and everything.
[1908.22 → 1913.48] But we used these logs that a customer had provided because they wanted to see if we could build a better model.
[1913.84 → 1920.00] And it turns out that the chat agent wasn't exactly speaking the way we'd want another human being to speak to us.
[1920.00 → 1921.04] And why?
[1921.32 → 1926.16] Because people get pretty upset when they're talking to customer support.
[1926.72 → 1933.02] And the language that they use isn't necessarily language I think we would use with each other, you know, on this podcast.
[1933.58 → 1933.80] All right.
[1933.86 → 1938.50] Me, Myself and AI is a collaboration between MIT Slow Management Review and Boston Consulting Group.
[1938.50 → 1940.24] It's available wherever you get your podcasts.
[1940.36 → 1942.82] Just search me, myself and AI.
[1942.82 → 1972.80] So, Chris, you had just started to kind of talk about how we're getting to a point where there's a good number of tools that fulfill a lot of the
[1972.80 → 1975.92] needs that an AI researcher or data scientist.
[1976.70 → 1978.22] The needs are so diverse.
[1978.46 → 1984.10] Everything from analyzing data sets to serving models to dealing with infrastructure and tracking things.
[1984.26 → 1986.48] And there are a lot of good tools out there now.
[1987.10 → 1994.00] And I know that our team, and maybe this is a follow-up from a previous conversation that we had about building data teams.
[1994.00 → 1998.50] Our team at SIL, we've been in the sort of growth phase.
[1998.66 → 2003.14] We're building up a team that's doing NLP research and development.
[2003.56 → 2012.28] And we've gone through a kind of process of figuring out what tools work well for us and how to kind of plug all of these tools together.
[2012.28 → 2017.46] And it's kind of taken a year to work through a lot of those things.
[2017.70 → 2030.84] But I know there are a lot of things that we talked about on this podcast around Flops and GPU servers and tracking models and experiments and, you know, all of those things.
[2030.84 → 2042.46] And I thought it might be good to follow up on that conversation that we had before and talk a little bit about how some of these things might tie together in a real-world environment.
[2042.60 → 2044.72] Because we talked about a lot of them individually.
[2045.28 → 2047.26] I really want to hear what you're doing at SIL.
[2047.26 → 2062.80] And the reason I say that is for those of us who have followed the show for a while, when we've had some of these other related conversations, I know we talked about some of the infrastructure that we had at Lockheed Martin, which was, you know, a very large organization and kind of how we approach things.
[2063.12 → 2071.24] But that's a different set of business drivers and a different set of constraints about how you go and evaluate such software.
[2071.24 → 2078.34] And so you're coming from a different organization, different size, different constraints, different budgets, all that kind of thing.
[2078.46 → 2088.48] I would love not only for you to share what you have done and how you arrived at those, but kind of what some of those constraints were that you had to learn to live within and yet make it work.
[2088.76 → 2089.44] Yeah, for sure.
[2089.44 → 2113.56] So to give a little bit of context, we've now got probably a group of, depending on how you count them, probably 15 or so people between people on my team, plus kind of academic collaborators, plus other, you know, close collaborators that are working on kind of similar set of problems for NLP tasks.
[2113.56 → 2124.80] And how we sort of thought about this was, you know, we need a way for this team to do kind of a diverse set of experiments.
[2124.80 → 2134.08] So we're working on all sorts of things from machine translation to spoken language identification and speech related problems to chat and dialogue.
[2134.08 → 2139.08] And so we need people to be able to use a whole variety of tooling.
[2139.60 → 2150.30] But also we want to create some standardization and centralization around how we're tracking experiments, how we're running jobs, and how we're sharing models one with another.
[2150.94 → 2154.48] And so we're kind of, you know, settling down on some of that.
[2154.48 → 2159.96] Part of that was thinking about, okay, where are we going to run training?
[2160.64 → 2164.44] Where are we going to run inference in our context?
[2164.96 → 2170.50] And how, and where are we going to store and track models, data sets, and code?
[2170.84 → 2172.72] So some of that's a little bit easier than others.
[2172.88 → 2175.50] I mean, code, we version in GitHub.
[2175.96 → 2178.58] That's pretty standard for everyone.
[2178.58 → 2188.52] But also we use Google Cola a lot because our organization, we use G Suite for all of our kind of, you know, docs and drive and all of that.
[2188.60 → 2190.42] So we use Google Cola a lot.
[2191.04 → 2194.44] So if we think, okay, some people are going to have code that lives in GitHub.
[2194.72 → 2199.34] Some people are going to have code that's living in notebooks and Google Cola.
[2200.04 → 2202.54] Cola, of course, has some GPU resources.
[2202.54 → 2209.38] But in order to train some of these larger NLP and speech models, we need other more robust GPU resources.
[2209.38 → 2215.10] So we did end up getting an on-prem GPU server, which is sitting down in Dallas.
[2215.32 → 2217.04] But that brings up a new set of questions.
[2217.04 → 2237.30] So if we've got 10 to 15 people and sometimes more distributed sort of all over the U.S., but also in Europe, in Asia, basically all over the world, how do we get them all running things reasonably on this on-prem server in Dallas?
[2237.82 → 2240.08] You might be saying HPC stuff.
[2240.16 → 2242.86] I know you worked in HPC stuff for some time.
[2242.86 → 2247.40] I was going to say a scheduler, you know, is one of those things in terms of getting the jobs lined up and stuff.
[2247.60 → 2248.48] How did you approach it?
[2248.50 → 2251.36] I'm curious what's different from how we addressed it.
[2251.58 → 2266.90] So I think one of the things that we wanted to make sure was that our people running and supporting the server on the ground weren't really the ones that were going to, like, although they're installing the server, they're not really administrating the server.
[2266.90 → 2275.04] You know, we don't have a large kind of, you know, DevOps and engineering team behind our NLP team supporting us.
[2275.08 → 2279.98] So we wanted a kind of simple solution that we could work with on our distributed team.
[2280.10 → 2282.90] So we ended up using Clear ML for this.
[2283.10 → 2291.04] So Clear ML, we actually had a conversation on the podcast about a similar kind of tool, which is in the same vein as Weights and Biases.
[2291.04 → 2293.40] That's another very popular one.
[2293.54 → 2299.30] But Clear ML allows you to have a dashboard where you track all your experiments and your runs.
[2299.48 → 2299.58] Yep.
[2299.86 → 2302.18] And you can actually just buy.
[2302.50 → 2310.98] So I could be running a Google Cola notebook, import the Clear ML library and register that experiment in the Clear ML dashboard.
[2310.98 → 2324.76] But I could also, from the Clear ML dashboard, enqueue a job on the GPU server that will also be registered on the same dashboard and will be sent to the GPU server in Dallas, sort of like a scheduler.
[2324.76 → 2335.20] It's not as sort of full-featured as like these, you know, really robust, big schedulers that are used on supercomputers.
[2335.26 → 2343.70] But it's enough for our team because we can say, well, we have, you know, this many queues on our GPUs and you can put things in there, and they'll run in that order.
[2343.80 → 2346.34] We don't really need much more functionality than that.
[2346.68 → 2347.74] And all of that's registered.
[2348.02 → 2353.82] And all the input output data is registered in a backing data store in S3.
[2353.82 → 2361.96] For us, we're running code locally on our laptops, code in Cola and code on the on-prem server.
[2362.22 → 2367.38] All of that is importing Clear ML and all of those jobs are being registered in Clear ML.
[2367.76 → 2375.32] And all the input data and the output artifacts like model files are being stored in S3 in a version way.
[2375.46 → 2378.88] So we know what data was used to train this model.
[2379.20 → 2383.60] When it was created, we can look at the exact run and all of that type of stuff.
[2383.60 → 2388.28] Without diving like the alternatives that you didn't choose, because I don't want to do that to them.
[2388.82 → 2403.18] But kind of abstracting that a little bit, what's some of the reasoning that you chose Clear ML or conversely, that you didn't choose a competitor from a capability standpoint or from, you know, how it was satisfying the need?
[2403.54 → 2411.30] What were some of the things that made you arrive at this solution being the right one for your organization that were not universal across all the solutions?
[2411.30 → 2422.48] Yeah, I think it was a combination of one, just the simplicity of administrating the solution for not systems administrator people.
[2422.70 → 2424.24] Although we got their help, right?
[2424.42 → 2424.52] Sure.
[2424.64 → 2429.02] The majority of people running and operating this thing are data scientists and NLP people.
[2429.02 → 2436.70] So we needed something that we could support and not something that we would have to know a lot about HPC systems to support.
[2436.94 → 2437.04] Yeah.
[2437.18 → 2438.22] So that was one thing.
[2438.24 → 2440.50] And we needed a way to queue jobs.
[2440.66 → 2449.28] And the fact that, you know, we could also integrate that with our, you know, runs on Google Cola and all that was really nice.
[2449.28 → 2454.84] Now we do use also, so this is kind of for our training jobs.
[2455.18 → 2459.28] We do also use other solutions for kind of persistent data pipelines.
[2459.56 → 2472.12] We use Packager for that, which actually allows you to kind of create and subscribe to data sources and pump those through to, you know, update data sets in a version sort of way.
[2472.12 → 2478.68] So we use that for other purposes, but Clear ML gave us that sort of experimentation for NLP research.
[2478.82 → 2487.68] And what we found is we can run our experiments there, but then we can also kind of, and this is where I wanted to kind of get with the connecting the pieces.
[2488.02 → 2501.72] So we're using notebooks, we're using the GPU server, but then these models and data sets that we're creating in our experiments, we can upload those now to Hugging Face, Data Sets Hub, Models Hub.
[2501.72 → 2505.28] Those are versioned in that model hub.
[2505.44 → 2521.78] And then any inference we can do, we could either use the Hugging Face inference API, or we could call down the model using the Hugging Face libraries into Python code where we could serve that model in, you know, a custom application of some type.
[2522.18 → 2522.28] Right.
[2522.28 → 2541.72] It provides a really then flexible route towards inference as well, because if you can now store your models in a sort of standardized way in a hub and have a standardized way of serving them, it lets you have kind of consistency and efficiency around how you do that bit as well.
[2541.72 → 2548.08] I'm curious about one of your constraints in general, aside from, because I understand the solution you've taken us through so far.
[2548.38 → 2554.00] Are you able to keep things kind of cloud-based or at least locally on that server in its immediate environment?
[2554.42 → 2558.16] Do you have any kind of edge considerations that you have to push to?
[2558.38 → 2560.58] Is that part of your requirement or not?
[2560.58 → 2562.86] So it depends on the project.
[2563.00 → 2569.96] So some of our projects, the end target for deploying these models is some inference server in the cloud.
[2570.22 → 2572.50] So that's part of what we deploy to.
[2572.62 → 2580.58] And that could be, like I say, either a custom inference server that we've built or something that we're deploying to an inference, hosted inference service.
[2580.58 → 2589.46] But we also deploy to edge devices, particularly some of our speech solutions we're running on edge devices.
[2589.74 → 2593.74] That does have other concerns like you're talking about.
[2593.88 → 2601.42] But the nice thing is if you've got your models, for the most part on our edge devices, they are connected to the internet.
[2601.42 → 2606.16] So we can ship a Docker container to those edge devices.
[2606.16 → 2617.24] And if we're, for example, downloading a model from Model Hub or S3, it can directly download that version of the model from there at runtime.
[2617.82 → 2622.52] So we have a little bit of flexibility there on the edge devices because they are connected to the internet.
[2622.98 → 2623.06] Gotcha.
[2623.44 → 2631.60] I'm curious if, and I know a while back you took us through some specs in a previous episode for a GPU server that you had.
[2631.96 → 2634.68] Is this the same one that we're talking about or is this a different one?
[2634.68 → 2640.52] That's my one-off DIY build that you're talking about, the previous one, which was an interesting build.
[2640.60 → 2645.00] And I still use it more for sort of the one-off things that I'm doing.
[2645.24 → 2650.04] This server is, it's a rack mount unit with A100s in it.
[2650.24 → 2651.84] So A100 GPUs.
[2651.96 → 2652.10] Yep.
[2652.22 → 2660.28] Which is, another thing is nice about that solution is we can, the A100 GPUs have this MIG technology,
[2660.28 → 2665.44] which lets you split up the GPU into sort of multiple virtual GPUs.
[2665.66 → 2665.82] Yeah.
[2665.88 → 2675.08] Which is really great because we don't all the time, yeah, we don't all the time need to run like big jobs on, you know, whole combinations of our GPUs.
[2675.20 → 2678.62] We might need to run a bunch of small training jobs, right?
[2678.72 → 2678.84] Yeah.
[2678.84 → 2680.06] You get a lot more utility.
[2680.26 → 2680.88] Yeah, exactly.
[2680.88 → 2687.80] We can split them up and sort of slice and dice them the way that makes sense for, you know, the season of research that we're in.
[2688.20 → 2690.68] I think that's a really beneficial thing.
[2690.86 → 2696.00] So, yeah, I would highly recommend people look into that technology if they're able.
[2696.48 → 2696.64] It is.
[2696.72 → 2703.28] That was my single favourite feature when the A100s came out was that ability to do that instead of having, you know, having to use them all.
[2703.74 → 2704.62] It was otherwise.
[2705.02 → 2710.08] Once you had the A100s to look back, it felt very inefficient in terms of how you were going and doing training.
[2710.08 → 2711.08] I'm curious.
[2711.42 → 2715.16] I want to go back, go and hit a really basic question that people are facing a lot.
[2715.58 → 2730.46] And that is, how did you determine your crossover for the organization for when it needed to have an on-prem server versus when it could use cloud resources, whether that be Google Cola or AWS or any of the others that are out there?
[2730.60 → 2732.24] How did you make such a determination?
[2732.24 → 2744.98] Yeah, I think it was basically when we looked at for the year kind of estimate of the sort of scale of training that we would need to be doing for our models.
[2744.98 → 2753.68] And we realized that, like, we would be making back our cost on the GPU server with the amount of training that we're doing.
[2753.68 → 2755.84] I think it's partially that.
[2756.16 → 2758.04] So there was a breakeven point there.
[2758.56 → 2773.02] But then also it was when we realized kind of we could develop also some operational efficiencies by having people kind of centralize their jobs on the server in these queues.
[2773.02 → 2783.28] By kind of combining all of these people's work rather than like this person over here spinning up a GPU server in the cloud and this person over here spinning it up and this person over here spinning it up.
[2783.36 → 2787.38] And they're not utilizing all of those GPUs to their full extent.
[2787.62 → 2787.74] Right.
[2787.84 → 2792.18] By utilizing like a more of like a job queue thing, then we could do that.
[2792.30 → 2797.42] Now, you could also spin up a cloud server and implement like similar queues and such.
[2797.42 → 2799.48] But yeah, so there's a variety of options.
[2799.58 → 2804.52] There's also increasingly favourable options for running these things in the cloud.
[2804.66 → 2808.54] So it's still not a kind of story that's that's finished.
[2808.82 → 2809.26] I don't know.
[2809.36 → 2810.42] It's definitely evolving.
[2810.42 → 2823.34] But we are still at that point where there seems to be a crossover is you get more capable, sophisticated in your running models on a more consistent basis and not just doing it for a short while, you know, each day kind of thing.
[2823.40 → 2826.34] And it's sitting there not running during those off hours.
[2826.34 → 2831.58] Once you get to that point, it definitely seems to pay in the current economics to go there.
[2831.70 → 2832.38] You go that way.
[2832.70 → 2832.78] Yeah.
[2832.86 → 2839.36] So as we turn to other things, you have any learning resources we're sharing today?
[2839.86 → 2840.12] Yeah.
[2840.20 → 2853.20] I mean, I don't have that many, but I did want to point people to a quick thing that I saw, which I do think was really cool for people to explore, which is pandastutor.com.
[2853.20 → 2855.78] So pandastutor.com.
[2855.88 → 2866.04] If you go there, this is a way for you to visualize your Python pandas data transformation, which is really cool.
[2866.66 → 2873.08] So for those that don't know, pandas is a way to construct data frames of sort of tabular data in Python.
[2873.08 → 2878.38] It's kind of ubiquitous in the data science, AI world.
[2878.60 → 2882.40] It's very common to use, but it's so powerful.
[2882.66 → 2884.84] There are so many data transformations that you can do.
[2885.02 → 2894.42] Sometimes it's hard to visualize and strategize about like what your code's actually doing and some non-intuitive things can happen.
[2894.42 → 2905.82] From my perspective, a really cool thing that this is addressing is helping people gain that intuition about what certain transformations and pandas code does to data.
[2906.04 → 2908.78] And it does that in a very visual way.
[2909.10 → 2909.34] It does.
[2909.42 → 2909.98] Looks pretty cool.
[2910.06 → 2911.10] I'm looking through it now.
[2911.40 → 2912.52] Thank you for sharing this.
[2912.76 → 2913.60] Yeah, for sure.
[2913.60 → 2923.52] And, you know, there are also a bunch of things going on in the month of December around like the advent of code and 27 days of jacks.
[2923.58 → 2924.26] I've seen that.
[2924.40 → 2930.36] So there's a whole bunch of kinds of every day of December trying to do some coding thing out there.
[2930.48 → 2933.32] So if you're into that, you could look up some of those things.
[2933.40 → 2935.46] They're always good learning experiences.
[2935.46 → 2939.40] But, yeah, I wanted to share this pandas' thing that I ran across.
[2939.40 → 2940.06] Well, thanks.
[2940.18 → 2950.88] You know, you've really taken us on a bit of a tour today between OpenAI and Hugging Face and then how you guys put together your current approach to training.
[2951.10 → 2953.24] So thank you for sharing that.
[2953.56 → 2954.18] Yeah, for sure.
[2954.28 → 2954.90] It was fun, Chris.
[2955.08 → 2957.68] And I hope you have a good rest of the week.
[2957.76 → 2963.12] I'm going to put on my heavy coat and go through the cold back to my apartment because now it's winter.
[2963.82 → 2965.84] But, yeah, appreciate the conversation.
[2966.02 → 2967.66] Looking forward to chatting next week.
[2967.96 → 2968.36] Absolutely.
[2968.36 → 2969.22] Talk to you then.
[2969.40 → 2973.62] That's our show.
[2973.82 → 2974.48] Thanks for listening.
[2975.08 → 2977.26] For more like this, check out our Master Feed.
[2977.60 → 2981.34] It is all Changelog podcasts in one easy-to-consume place.
[2981.70 → 2986.58] Let your podcast app snag everything we produce and then pick and choose which ones to listen to.
[2986.92 → 2992.94] Subscribe today at changelog.com slash master or just search for Changelog Master in your podcast app of choice.
[2993.20 → 2993.74] You'll find it.
[2994.24 → 2998.82] Special thanks to Break master Cylinder for providing our music and to our longtime sponsors.
[2998.82 → 3001.24] Vastly, Launch Darkly, and Linde.
[3001.82 → 3003.08] That's all for this week.
[3003.08 → 3004.68] We'll talk to you next time.
[3004.68 → 3009.52] We'll talk to you again next time.
[3009.52 → 3039.50] Thank you.
